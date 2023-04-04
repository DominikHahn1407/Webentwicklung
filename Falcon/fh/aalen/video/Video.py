import sqlalchemy as sa

from fh.aalen.data.modelbase import ModelBase
from fh.aalen.relations.favours import Favours


class Video(ModelBase):
    __tablename__ = 'Video'

    vnr = sa.Column('vnr', sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column('title', sa.String, nullable=False)
    age_rating = sa.Column('age_rating', sa.String, nullable=False)
    description = sa.Column('description', sa.String, nullable=False)
    genre = sa.Column('genre', sa.String)
    persons = sa.orm.relationship('Favours', back_populates='video')

    def to_dict(self):
        return dict(vnr=self.vnr,
                    title=self.title,
                    age_rating=self.age_rating,
                    description=self.description,
                    genre=self.genre)
