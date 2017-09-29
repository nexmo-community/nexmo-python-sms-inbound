import hug
from tinydb import TinyDB, Query
from jinja2 import Environment, FileSystemLoader
from sms_types import telephone_number

db = TinyDB('./messages.json')


@hug.post()
def sms(
    messageId: hug.types.text,
    to: telephone_number,
    msisdn: telephone_number,
    text: hug.types.text,
    keyword: hug.types.text,
    type: hug.types.one_of(['text', 'unicode'])):

    db.insert({
        'id': messageId,
        'to': to,
        'from': msisdn,
        'keyword': keyword,
        'message': text,
        'type': type
    })

    return db.search(Query().id == messageId)


@hug.get('/', output=hug.output_format.html)
def list_all():
    env = Environment(
        loader=FileSystemLoader('./'),
        extensions=['pypugjs.ext.jinja.PyPugJSExtension']
    )
    template = env.get_template('list.pug')
    return template.render(messages=db.all())
