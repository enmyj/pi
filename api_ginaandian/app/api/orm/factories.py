import factory

from api.orm.models import RSVP


class RSVPFactory(factory.alchemy.SQLAlchemyModelFactory):

    name = factory.Faker("name")
    plus_one_name = factory.Faker("name")
    rsvp = factory.Faker("pybool")
    shuttle = factory.Faker("pybool")
    hotel_location = factory.Faker("pystr")
    driving = factory.Faker("pybool")
    available_seats_in_car = factory.Faker("pyint")
    food_restrictions = factory.Faker("pystr")
    mobility_restrictions = factory.Faker("pystr")
    children_count = factory.Faker("pyint")

    class Meta:
        model = RSVP
