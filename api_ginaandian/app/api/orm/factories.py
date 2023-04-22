import factory

from api.orm.models import RSVP, Guest


class GuestFactory(factory.alchemy.SQLAlchemyModelFactory):

    id = factory.Faker("pyint")
    name = factory.Faker("name")
    has_plus_one = factory.Faker("pybool")

    class Meta:
        model = Guest


class RSVPFactory(factory.alchemy.SQLAlchemyModelFactory):

    id = factory.Faker("pyint")
    guest_name = factory.Faker("name")
    plus_one_name = factory.Faker("name")
    attending = factory.Faker("pybool")
    shuttle_or_driving = factory.Faker("pybool")
    shuttle_lodging_location = factory.Faker("pystr")
    driving_num_seats = factory.Faker("pyint")
    dietary_restrictions = factory.Faker("pystr")
    mobility_restrictions = factory.Faker("pystr")
    num_children = factory.Faker("pyint")

    guest_id = factory.Faker("pyint")

    class Meta:
        model = RSVP
