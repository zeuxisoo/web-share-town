from flask.ext.script import Manager
from flask.ext.assets import ManageAssets
from sharetown.app import create_app

app = create_app()

manager = Manager(app)
manager.add_command("assets", ManageAssets())

if __name__ == "__main__":
	manager.run()
