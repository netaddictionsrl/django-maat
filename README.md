
Django Maat
---------------

This application optimizes large ordered data set retrieving **when using MySql**.

Suppose you have a model counting a very large number of instances and you need to display them by using a complicated ordering heuristic. Moreover, you are not really interested in showing all of them - much like Google does when you try to navigate search results beyond a certain page.

That being the case, Django Maat can be helpful.

The high speed is due to an external table thoughtfully indexed that optimizes both the join and the ordering of the rows **without file sorting**.


Sample usage:

- Make sure `djangomaat` is listed among your `INSTALLED_APPS`

- Run the `syncdb` command

- Subclass and register an handler for a given Django model.  
  Implement one or more `get_pk_list_for_[typology_name]` methods.  
  The `typology_name` is then used to retrieve the ordered list.
  This method must returns a list or an iterator over the model
  primary keys in the order you want them to be retrieved.

        from djangomaat.register import maat
        from djangomaat.handlers import MaatHandler
        
        class ArticleMaatHanlder(MaatHandler):
            
            def get_pk_list_for_comment_count(self):
                return Article.objects.filter(
                    thread__content_type=ContentType.objects.get_for_model(Article),
                ).order_by('-thread__comment_count').values_list('pk', flat=True)[:1000].iterator()
            
            def get_pk_list_for_popularity(self):
                return Article.objects.filter(
                    popularity__content_type=ContentType.objects.get_for_model(Article),
                ).order_by('-popularity__score').values_list('pk', flat=True)[:1000].iterator()
    
        maat.register(Article, ArticleMaatHanlder)

- Run the `./manage.py populate_maat_ranking` command to create or update data for each registered handler

- Retrieve your queryset using the `maat` attribute attached to your model:

        most_popular_articles = Article.maat.ordered_by('popularity')
        most_commented_articles = Article.maat.ordered_by('comment_count')

  You can also retrieve them in inverted order:

        less_popular_article = Article.maat.ordered_by('-popularity')
        less_commented_article = Article.maat.ordered_by('-comment_count')

For further documentation and examples have a look at the doc string of the `MaatHandler` class.

Plus, run 

    ./manage.py populate_maat_ranking --help
for extra parameters.   
Being that the order is not dynamically calculated, you might want to schedule the command to be run at regular intervals.


Requirements:

- Django >= 1.5, < 1.8
