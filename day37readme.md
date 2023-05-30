D A Y T H I R T Y S E V E N

# TODAY'S GOAL

Advanced authentication and POST/PUT/DELETE requests

Build a habit tracker with the pixela API

## HTTP post requests

* GET requests *get* data
* POST, PUT, DELETE requests also exist
* 
| Type | Code   | Action |
|---|--------|---|
|GET| .get() | request data |
|POST | .post() | give system data, get success/fail|
|PUT | .put() | update piece of data in external service |
| DELETE |.delete() | delete piece of data in external service |

building habit tracker using [pixela](https://help.pixe.la/en/getting-started)

1. Create account with a POST request
* get more information about failed requests by calling .json() or .text

# More Secure Authentication

2. create a graph

## HTTP headers

  * doesnt show up in the URL

3. Access the graph

using requests.get(), you get the HTML code in the response

can use the datetime [`strftime(code)`](https://strftime.org/) function to format the date

## Update and delete pixels with PUT and DELETE
PUT changes existing data, DELETE deletes it