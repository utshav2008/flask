from flask_restplus import Api

from .dummy_api1 import api as api1
from .dummy_api2 import api as api2

api = Api(
    title='Dummy Platform',
    version='1.0'
)

api.add_namespace(api1)
api.add_namespace(api2)
