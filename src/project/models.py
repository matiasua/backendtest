from project import db, bcrypt


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        self.password = self.generate_password_hash(**kwargs)

    def generate_password_hash(self, **kwargs):
        if 'password' in kwargs:
            return bcrypt.generate_password_hash(kwargs['password']).decode()

        return None
