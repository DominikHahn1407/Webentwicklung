import sqlalchemy as sa
from sqlalchemy.orm import relationship

from fh.aalen.data.modelbase import ModelBase


class Favours(ModelBase):
    __tablename__ = 'Favours'

    video_vnr = sa.Column(sa.ForeignKey('Video.vnr'), primary_key=True)
    person_id = sa.Column(sa.ForeignKey('Person.pid'), primary_key=True)
    video = relationship('Video', back_populates='persons')
    person = relationship('Person', back_populates='videos')
