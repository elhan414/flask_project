from flask import Flask


aap = Flask(__name__)
@aap.route('/')
def hello():
    return 'Hello World!'

@aap.route("/about_my")
def about_my():
    return "My name is Elhan"

@aap.route("/Elhan")
def Elhan():
    return "Я сегодня встретил Элхана. Он выглядел очень довольным.Элхан обещал помочь с этим проектом. Надеюсь, у него получится.Мы обсуждали последние новости с Элханом. Интересный разговор получился."

if __name__ == '__main__':
    aap.run(debug=True)