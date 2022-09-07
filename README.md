# This projet contains django rest api api project

# Vagrent is container based facility

Apiviews: describe logic to make api endpoint
 http get post put patch delete  customize the function for all the menthod and give controle to write http method login
-need full control over the login updating multiple datasource in one call

- processing files and rendering a synchronous response
- calling other api services

- seriealizer : helps convert object to readable format


# ViewSet 
- CRUD openration on Database, 
- a quick simple API, 
- little to no customization on the login, 
- working with standard data structure

/api/profile - list all profiles when http get method is called
create a ew profile when http post method is calls

/api/profile/id - view/ update/ delete the profile
- creating an profile api
- create a new profile
- listing existing profile
- view specific profile
- updating the profile of logged in users
- delete the profile


/api/feed - 

- list all feed items

get (list feed items)
post (create feed item for logged in user)

/api/feed/<feed_item_id>  

delete
show feed
