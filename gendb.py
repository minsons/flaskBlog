from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps import  create_app
#app.config.from_object('app.config')

# configuration
# SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@117.48.202.102/flaskAdmin'
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app = create_app('../config.py')

from apps.models import  db
#db.init_app(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()

"""
python  gendb.py  init
python  gendb.py  migrate
python  gendb.py  upgrade
"""