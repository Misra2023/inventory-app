from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base  # Import the Base from your models

class Database:
    def __init__(self):
        # Define the database URL for SQLite (creates 'inventory.db' in the same directory)
        self.engine = create_engine('sqlite:///inventory.db')

        # Create a session factory
        self.Session = sessionmaker(bind=self.engine)

        # Initialize the database schema
        Base.metadata.create_all(self.engine)

    def get_or_create(self, model, **kwargs):
        instance = self.session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = model(**kwargs)
            self.session.add(instance)
            self.session.commit()
            return instance

    @property
    def session(self):
        return self.Session()
