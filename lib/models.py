from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref, declarative_base

# Create the engine
engine = create_engine('sqlite:///one_to_many.db')

# Create a base class
Base = declarative_base()

# Define the Game model
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Define the one-to-many relationship with Review
    reviews = relationship('Review', backref=backref('game', uselist=False))

    def __repr__(self):
        return (f'Game(id={self.id}, title={self.title}, ' +
                f'platform={self.platform})')

# Define the Review model
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    def __repr__(self):
        return (f'Review(id={self.id}, score={self.score}, ' +
                f'game_id={self.game_id})')

# Create all tables
Base.metadata.create_all(engine)
