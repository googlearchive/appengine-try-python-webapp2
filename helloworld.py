import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

def handle_404(request, response, exception):
    response.write('Sorry, nothing at this URL.')
    response.set_status(404)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

application.error_handlers[404] = handle_404
