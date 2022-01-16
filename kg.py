from pickletools import long4
from owlready2 import *

onto = get_ontology("http://oracle.akash.com")
with onto:
    class Booking(Thing):
        pass
    class Trip(Thing):
        pass
    class User(Thing):
        pass
    class Country(Thing):
        pass
    class associates_to_trip(ObjectProperty):
        domain = [Booking]
        range = [Trip]
    class associates_to_booking(ObjectProperty):
        domain = [Trip]
        range = [Booking]
        inverse_property = associates_to_trip
    class linked_to_user(ObjectProperty):
        domain = [Booking, Trip]
        range = [User]
    class country_id(DataProperty, FunctionalProperty, InverseFunctionalProperty):
        domain = [Country]
        range = [int]
    class user_id(DataProperty, FunctionalProperty, InverseFunctionalProperty):
        domain = [User]
        range = [int]
    class booking_country(ObjectProperty):
        domain = [Booking]
        range = [Country]
    class booking_id(DataProperty, FunctionalProperty, InverseFunctionalProperty):
        domain = [Booking]
        range = [int]
    class trip_id(DataProperty, FunctionalProperty, InverseFunctionalProperty):
        domain = [Trip]
        range = [int]
    class trip_end_time (DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [int]
    class trip_country(ObjectProperty, FunctionalProperty):
        domain = [Trip]
        range = [Country]
    rule = Imp()
    rule.set_as_rule("""Booking(?b), Trip(?t), associates_to_booking(?t, ?b),booking_country(?b, ?c)  -> trip_country(?t, ?c)""")



def get_mappings(): 
    return  {
        "bookingId": booking_id,
        "userId": user_id,
        "tripId": trip_id,
        "tripEndTime": trip_end_time,
        "countryId": country_id
    }

def create_individual(property_name, property_value):
    obj = None
    if (property_name == "bookingId"):
        obj = Booking("" + str(property_value))
        obj.booking_id = property_value
    elif property_name == "tripId":
        obj = Trip("" + str(property_value))
        obj.trip_id = property_value
    elif property_name == "userId":
        obj = User("" + str(property_value))
        obj.user_id = property_value
    elif property_name == "countryId":
        obj = Country ("" + str(property_value))
        obj.country_id = property_value
    elif property_name == "tripEndTime":
        obj = Trip("some name")
        obj.trip_end_time = property_value
    return obj