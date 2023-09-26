import heapq

global arrival_time, process_time, machine_state, machine_count, queue, simulation_time
EVENT_TYPE_ARRIVAL = "Arrival"
EVENT_TYPE_LOAD = "Load"
EVENT_TYPE_UNLOAD = "Unload"
arrival_time = 2
process_time = 3

event_queue = []

# Define an event class
class Event:
    def __init__(self, time, event_type):
        self.time = time
        self.event_type = event_type

    def __lt__(self, other):
        return self.time < other.time
    
    
def schedule_unload_event():
    unload_event = Event(simulation_time, "Unload")
    heapq.heappush(event_queue, unload_event)

# Schedule a load event
def schedule_load_event():
    if machine_count > 0 and queue > 0:
        global process_time
        load_time = simulation_time + process_time  
        load_event = Event(load_time, "Load")
        heapq.heappush(event_queue, load_event)

# Function to process an arrival event
def process_arrival():
    global queue
    queue += 1
    schedule_load_event()

def process_load():
    global machine_count, queue
    machine_count -= 1
    queue -= 1
    schedule_unload_event()

def process_unload():
    global machine_count 
    machine_count += 1

# Schedule an arrival event
def schedule_arrival_event():
    global arrival_time, simulation_time
    arrival_time = simulation_time + arrival_time  
    arrival_event = Event(arrival_time, "Arrival")
    heapq.heappush(event_queue, arrival_event)

# initialize queue
machine_count = 1
simulation_time = 0
queue = 0

# initialize all events
schedule_arrival_event()
schedule_arrival_event()
schedule_arrival_event()
schedule_arrival_event()

# Main simulation loop
while event_queue:
    current_event = heapq.heappop(event_queue)
    simulation_time = current_event.time

    print("Event: ", current_event.event_type, ", Elapsed_time: ", simulation_time)
    print("state_variable[Q] = ", queue)
    print("state_variable[M] = ", machine_count)

    if current_event.event_type == EVENT_TYPE_ARRIVAL:
        process_arrival()
    elif current_event.event_type == EVENT_TYPE_LOAD:
        process_load()
    elif current_event.event_type == EVENT_TYPE_UNLOAD:
        process_unload()


