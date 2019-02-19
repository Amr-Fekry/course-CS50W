
# API : Application-Programming Interface
# a protocol for communication (sharing information) between different web apps, or different parts of the same web app.

# APIs standard language is JSON (JavaScript Object Notation)
# JSON represent info in a way that is readable for both humans and computers.

# JSON consists of key:value pairs just like Python dict
{
	"origin": "Tokyo",
	"destination": "Shanghai",
	"duration": 185
	"passengers": ["Alice", "Bob"]
}

# JSON can be nested to represent info in an organized way
{
	"origin": {
		"city": "Tokyo",
		"code": "HND"
	},
	"destination": {
		"city": "Shanghai",
		"code": "PVG"
	},
	"duration": 185
	"passengers": ["Alice", "Bob"]
}

# interacting with APIs is usually done via urls
# /flights
# /flights/28
# /flights/28/passengers
# /flights/28/passengers/6

# interacting method might vary from one API to another, 
# but it is fairly conventional to use this nested url structure 
# to describe the different end points used to get particular info inside the API.


# APIs can be used to perform all HTTP request methods:
# GET: retrieve resource (info)
# POST: create a new resource
# PUT: replace a resource
# PATCH: update a resource
# DELETE: delete a resource


# status codes:
# 200 OK : request was successful
# 201 Created : request was successful, and something new was created
# 400 Bad request : error, something wrong with the request you made
# 403 Forbidden : error, resource need special permissions (i.e. log in)
# 404 Not Found : error, resource doesn't exist
# 405 Method Not Allowed : error, route doesn't accept this request method
# 422 Unprocessable Entity : error, something wrong with part of the request

# see files 18 to 22

# API developer keys:
# too many requests might overload the API and make it harder for others to access it
# so, larger APIs need "rate limiting" for the number of requests allowed per user or per a period of time
# one way to achieve that is via API keys

