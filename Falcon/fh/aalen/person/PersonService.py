from fh.aalen.person.Person import Person
from fh.aalen.data.db_session import DBSession
from fh.aalen.relations.favours import Favours


class PersonService:
    @classmethod
    def __json_to_person(cls, person, json_person):
        person.surename = json_person["surename"]
        person.birthdate = json_person["birthdate"]
        return person

    @classmethod
    def get_persons(cls):
        session = DBSession.get_session()
        person_list = session.query(Person).all()
        return person_list

    @classmethod
    def get_person(cls, pid):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        return person

    @classmethod
    def create_person(cls, json_person):
        person = Person()
        person = cls.__json_to_person(person, json_person)
        session = DBSession.get_session()
        session.add(person)
        session.commit()

    @classmethod
    def update_person(cls, pid, json_person):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        cls.__json_to_person(person, json_person)
        session.commit()

    @classmethod
    def delete_person(cls, pid):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        session.delete(person)
        session.commit()

    @classmethod
    def add_video_to_favourites(cls, person_id, video_id):
        session = DBSession.get_session()
        fav = Favours()
        fav.person_id = person_id
        fav.video_vnr = video_id
        session.add(fav)
        session.commit()
