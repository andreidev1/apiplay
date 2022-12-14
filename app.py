from flask import Flask 
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_language = api.model('Language', {'language' : fields.String('Lang')})

languages = []
python = {'language' : 'Python', 'id': 1}
languages.append(python)

@api.route('/language')
class Language(Resource):

    @api.marshal_with(a_language)
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(new_language)
        return {'result' : 'Language added'}, 201 
'''
    @api.expect(a_langua_ge) api.payload
    def post(self):
        languages.append(api.payload)
        return {'result' : 'Language added'}, 201 
        :D
'''