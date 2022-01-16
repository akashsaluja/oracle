# Main entry point for the project
## Step 1: Load the Ontology, once loaded we will have a standardization
## Step 2: Define the event json keys to actual data and object properties, this is to ensure that we know what a field in a json really means
## Step 3: Write function to create individuals, ideally should happen dynamically, for now putting if else to do so
## Step 4: Write function to listen to event and create the individuals
## Step 5: Once individuals are created, link them intelligently. The way this will happen is if we 
##                assume each individual in an event is somehow bound to be linked together


from kg import *
import json


    
def load_file(file_path):
    with open(file_path, "r") as read_file:
        data = json.load(read_file)
    return data

def search_property_with_domain_and_range(ontology, domain, range):
    # print("Looking for domain" + str(domain) + "and range " + str(range))
    for property in ontology.properties():
        # print("Property " + property.name + " Domain: " + str(property.domain) + " Range: " + str(property.range))
        if domain[0] in property.domain and range[0] in property.range:
            # print("Found---------------------")
            return property
    return None


### Process raw string
def process_event(file_path):
    data = load_file(file_path)
    dict = {}
    for key in data.keys():
        dict[key] = create_individual(key, data[key])
    linkage_data = {}
    for domain in dict.keys():
        for range in dict.keys():
            print(domain)
            print(range)
            if domain == range:
                continue
            if domain not in linkage_data and range in linkage_data:
                continue
            property = search_property_with_domain_and_range(onto, get_mappings()[domain].domain, get_mappings()[range].domain)
            # print("Getting property for domain " + str(domain) + " and range " + str(range) + " is " + str(property))
            if property != None:
                print("Found a mapping")
                # print(dict[domain])
                # dict[domain][property.name].append(dict)
                setattr(dict[domain], property.name, [dict[range]])
                linkage_data[domain] = 1
                linkage_data[range] = 1
    

    if len(linkage_data.keys()) == len (dict.keys()):
        print("All good, all fields in the payload are linked")
    else:
        print("Error fields not linked", str(linkage_data))



## Processes the graph of the event metadata which will help us create the relations on the knowledge graph            
def process_event_graph():
    pass

def process_event1():
    booking = Booking("" + str(123))
    booking.booking_id = 123
    country = Country("" + str(10))
    country.country_id = 10
    user = User("" + str(5))
    user.user_id = 5
    booking.booking_country = [country]
    booking.linked_to_user = [user]

def process_event2():
    booking = Booking("" + str(123))
    booking.booking_id = 123
    trip = Trip("" + str(543))
    trip.trip_id = 543
    user = User("" + str(5))
    user.user_id = 5
    trip.trip_end_time = 1642322244
    booking.associates_to_trip = [trip]

process_event1()
process_event2()
## run the reasoner to get the required values
sync_reasoner(infer_property_values = True)
list = onto.search(trip_id = 543)
for item in list:
    print(item.associates_to_booking)
# list = list(default_world.sparql("""
#         SELECT *
#     """))
# print(list)



    


# # process_event("sampleEvent1.json")
# print(onto.get_instances_of(Booking))
# # process_event("sampleEvent2.json")
# print(len(onto.get_instances_of(User)))



