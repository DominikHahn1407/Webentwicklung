import sqlalchemy as sa

from fh.aalen.data.modelbase import ModelBase
from fh.aalen.relations.favours import Favours


class Person(ModelBase):
    __tablename__ = "Person"

    pid = sa.Column('pid', sa.Integer, primary_key=True, autoincrement=True)
    surename = sa.Column('surename', sa.String, nullable=False)
    birthdate = sa.Column('birthdate', sa.String, nullable=False)
    videos = sa.orm.relationship('Favours', back_populates='person')

    def to_dict(self):
        return dict(pid=self.pid,
                    surename=self.surename,
                    birthdate=self.birthdate)