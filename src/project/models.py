from project import db, bcrypt

subs = db.Table('subs',
     db.Column('user_id', db.Integer, db.ForeignKey('usuario.user_id'), primary_key=True),
     db.Column('grupo_id', db.Integer, db.ForeignKey('grupos.grupo_id'), primary_key=True)
)

element = db.Table('element',
        db.Column('grupo_id', db.Integer, db.ForeignKey('grupos.grupo_id'), primary_key=True),
        db.Column('aparato_id', db.Integer, db.ForeignKey('aparatos.aparato_id'), primary_key=True)
)

class Usuario(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    subscriptions = db.relationship('Grupos', secondary=subs, backref=db.backref('subscribers', lazy='dynamic')) 

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        self.password = self.generate_password_hash(**kwargs)

    def generate_password_hash(self, **kwargs):
        if 'password' in kwargs:
            return bcrypt.generate_password_hash(kwargs['password']).decode()

        return None

class Aparatos(db.Model):
    aparato_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_aparato = db.Column(db.String, nullable=False)
    consumo = db.Column(db.String, nullable=False)

class Grupos(db.Model):
    grupo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_group = db.Column(db.String, nullable=False)
    elementos = db.relationship('Aparatos', secondary=element, backref=db.backref('elementos', lazy='dynamic'))
    users = db.relationship('Usuario', secondary=subs, backref=db.backref('users', lazy='dynamic'))
    # user = db.relationship('Usuario', secondary=subs, back_populates='grupo')
    # user_id = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)
    # user = db.relationship('Usuario', backref='grupos')
