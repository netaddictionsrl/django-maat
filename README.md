
Django Maat
---------------

This is an application that tries to optimize large ordered data set retrieving when using MySql.

Suppose you have a model counting a very large number of instances and you need to display them by using a complicated ordering heuristic. Moreover, you are not really interested in showing all of them - much like Google does when you try to navigate search results beyond a certain page.

That being the case, Django Maat can be helpful.

The high speed is due to an external table thoughtfully indexed that optimize both the join and the ordering of the rows without file sorting.


Sample usage:

- Make sure `djangomaat` is listed among your `INSTALLED_APPS`

- Run the `syncdb` command

- Subclass and register an handler for a given Django model.  
  Implement one or more `get_pk_list_for_[typology_name]` methods.  
  The `typology_name` is then used to retrieve the ordered list.

        from djangomaat.register import maat
        from djangomaat.handlers import MaatHandler
    
        class ArticleMaatHanlder(MaatHandler):
            def get_pk_list_for_popularity(self):
                return Article.objects.filter(
                    popularity__content_type=ContentType.objects.get_for_model(Article),
                ).order_by('-popularity__score').values_list('pk', flat=True)[:1000].iterator()
    
        maat.register(Article, ArticleMaatHanlder)

- Run the `./manage.py populate_maat_ranking` command to create or update data for each registered handler

- Retrieve your queryset using the `maat` attribute attached to your model:

        ordered_article_list = Article.maat.ordered_by('popularity')

  You can also retrieve them in inverted order:

        inverted_article_list = Article.maat.ordered_by('-popularity')

For further documentation and examples have a look at the doc string of the `MaatHandler` class.

Plus, run 

    ./manage.py populate_maat_ranking --help
for extra parameters.   
You might want to schedule the command to be run at regular intervals.


Requirements:

- Django >= 1.5, <= 1.6
