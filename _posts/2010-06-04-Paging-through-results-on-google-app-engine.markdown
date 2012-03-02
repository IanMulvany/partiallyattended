---
layout: post
title: Paging through results on google app engine
categories:
- appengine
- paging
- coding
---

The sample code given on the appengine article about paging through results is incomplete for the method of paging through a results set by item key. Here is an example that will page forward and backward through a result set by item key. This example will display items oldest first. The next link will bring you to the set of next newest items.

# Template code for displaying the results, let's say it's called listitems.html #


{% literal %}
    {% if previous %}      
    	<p><a href="?previous={{ previous }}">previous</a></p>        
    {% endif %}
    {% if next %}
    	<p><a href="?next={{ next }}">next</a></p>        
    {% endif %}  
    {% for item in items %}
    	item  
    {% endfor %}
{% endliteral %}

# Try now with 'pre' blocks #

_underline_
	

# The relevant code in your application file. 

{% highlight python %}
#assume you have imported all of the googley goodness
#this sets the paging size

FETCHLIMIT = 10
 # an empty class for testing against.

 class Item(db.Model):
 	created = db.DateTimeProperty(auto_now_add=True)

 class ListItems(webapp.RequestHandler):
 	def get(self):
 		query = Item.all()
 		items = query.fetch(FETCHLIMIT+1)  
 		  
 		forward = self.request.get("next")       
 		back = self.request.get("previous") 

 		if forward:
 			items = Item.all().order("__key__").filter('__key__ >=', db.Key(forward)).fetch(FETCHLIMIT+1)
 		elif back:
 			items = Item.all().order("-__key__").filter('__key__ <=', db.Key(back)).fetch(FETCHLIMIT+1)
 			items.reverse()

 			# in order to go backwards through the set we need to reverse the order so that we get the newest keys on top         
 			# the filter than drops the items we have already seen
 			# but to get the previous link to pass the oldest key in the set we need to reverse the items before heading on     
 		else:
 			items = Item.all().order("__key__").fetch(FETCHLIMIT+1)
 			
 		# the key part here missing from the example code is making the right call 
    # against the right passed variable
 		# forward = self.request.get("next") returns a string, 
    # we convert that to a key object with the line:
 		# db.Key(forward)

 		# do we show next and previous links?
 		# start with none
 		next = None
 		previous = None

 		# we need to get the key of the very first item in the results set,
 		query = Item.all()
 		first_item_key = query.fetch(1)[0].key()
 		previous = activities[0].key()
 		# if previous key is the same as the key of the first item in the class then don't display a previous link
 		if previous == first_item_key: 
 			previous = None
 			# we have just asked for a batch of items. if the returned set is bigger than the amount we want on a page       
 			# we know there are some results left to get so we set a next link
 			if len(items) == FETCHLIMIT+1:
 					next = items[-1].key()
 					items = items[:FETCHLIMIT]
 					# perhaps we want to display the total count of objects in the datastore
 					item_number = Item.all().count()
 					template_values = {'count':item_number, 'items':items, 'next':next, 'previous':previous}
 					path = os.path.join(os.path.dirname(__file__), 'listitems.html')
 					self.response.out.write(template.render(path, template_values))
{% endhighlight %}
