"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("""<!DOCTYPE html>

<html lang="en">
  
<head>
  
  <meta charset="utf-8">
   
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
<meta name="viewport" content="width=device-width, initial-scale=1">
    
<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  
  <title>Python Chat App Yo</title>

   
 <!-- Bootstrap -->
   
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" 
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <style>
      div.msg_bbl {
        background-color: #ddd;
        padding: 5px 10px;
        border-radius: 10px;
        color: #555;
        margin-bottom: 5px;
      }
    </style>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
     
 <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>

      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
 
   <![endif]-->
 
 </head>

  <body>

    
<div class="text-center well"><b>Discussion Forum</b>
</div>

   
 <div class="container">

      <div class="col-sm-8">
       
 <div class="no_message">
      
    <h1 style='color: #ccc'>No message yet..</h1>
     
     <div class="message_holder"></div>
     
   </div>
     
 </div>
    
  <div class="col-sm-4">
   
     <form action="" method="POST">
        
  <b>Type your message below <span class="glyphicon glyphicon-arrow-down"></span></b>
     
     <div class="clearfix" style="margin-top: 5px;">
</div>
          
<input type="text" class="username form-control" placeholder="User Name">
      
    <div style="padding-top: 5px;">
    </div>
        
  <input type="text" class="message form-control" placeholder="Messages">
     
     <div style="padding-top: 5px;">
</div>
      
    <button type="submit" class="btn btn-success btn-block">
<span class="glyphicon glyphicon-send">
</span>
 Send</button>
    
    </form>
     
 </div>
   
 </div>



    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
   
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js">
</script>
   
 <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.7.3/socket.io.min.js">
</script>
    
<script>

      var socket = io.connect( 'http://' + document.domain + ':' + location.port )
      
// broadcast a message
      socket.on( 'connect', function() {
  
      socket.emit( 'my event', {
          data: 'User Connected'
        } )
      
  var form = $( 'form' ).on( 'submit', function( e ) {
 
         e.preventDefault()
          
let user_name = $( 'input.username' ).val()
         
 let user_input = $( 'input.message' ).val()
    
      socket.emit( 'my event', {
            user_name : user_name,
 
           message : user_input
          } )
          // empty the input field
    
      $( 'input.message' ).val( '' ).focus()
      
  } )
    
  } )

    
  // capture message
   
   socket.on( 'my response', function( msg ) {
   
     console.log( msg )
     
   if( typeof msg.user_name !== 'undefined' ) {
    
      $( 'h1' ).remove()
        
  $( 'div.message_holder' ).append( '<div class="msg_bbl"><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
   
     }
      } )
    </script>
  </body>
</html>""")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length)
        
        # Doesn't do anything with posted data
        print (post_data)
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
