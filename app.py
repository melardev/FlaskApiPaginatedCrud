from api_crud.factory import db, app
from routes import blueprint
from todos.models import Todo

app.register_blueprint(blueprint, url_prefix='/api')


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return dict(app=app, db=db, todo=Todo)

    app.shell_context_processor(shell_context)


register_shellcontext(app)
if __name__ == '__main__':
    app.run(port=8080)
