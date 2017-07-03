import jsonrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoo10_test1'
USER = 'admin'
PASS = '1'

# server proxy object
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
server = jsonrpclib.Server(url)

# log in the given database
uid = server.call(service="common", method="login", args=[DB, USER, PASS])

# helper function for invoking model methods
def invoke(model, method, *args):
    args = [DB, uid, PASS, model, method] + list(args)
    return server.call(service="object", method="execute", args=args)

# create a new note
args = {
    'color' : 8,
    'memo' : 'This is another note',
    'create_uid': uid,
}
note_id = invoke('note.note', 'create', args)