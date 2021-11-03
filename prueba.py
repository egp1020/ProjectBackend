from flask import make_response
mensaje = make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
print(mensaje)