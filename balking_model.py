import heapq

global arrival_time, process_time, machine_state, machine_count, queue, simulation_time
EVENT_TYPE_ARRIVAL = "Arrival"
EVENT_TYPE_LOAD = "Load"
EVENT_TYPE_UNLOAD = "Unload"
EVENT_TYPE_ENTER = "Enter"
arrival_time = 2
process_time = 3
capacity = 2

event_queue = []

# Define an event class
class Event:
    def __init__(self, time, event_type, queue, machine_count):
        self.time = time
        self.event_type = event_type
        self.queue = queue
        self.machine_count = machine_count

    def __lt__(self, other):
        return self.time < other.time

# Function to process an arrival event
def process_arrival():
    global simulation_time
    simulation_time += arrival_time
    schedule_enter_event()

def process_enter():
    global capacity, queue
    if queue <= capacity:
        schedule_load_event()

def process_load():
    global machine_count, simulation_time, queue
    machine_count += 1
    simulation_time += process_time  
    schedule_unload_event()

def process_unload():
    global machine_count 

def schedule_arrival_event():
    global arrival_time, simulation_time, queue, machine_count
    arrival_event = Event(simulation_time, "Arrival", queue, machine_count)
    heapq.heappush(event_queue, arrival_event)

def schedule_enter_event():
    global queue, simulation_time, machine_count
    queue += 1
    enter_event  = Event(simulation_time, "Enter", queue, machine_count)
    heapq.heappush(event_queue, enter_event)

def schedule_load_event():
    global process_time, simulation_time, machine_count, queue
    machine_count -= 1
    queue -= 1
    load_event = Event(simulation_time, "Load", queue, machine_count)
    heapq.heappush(event_queue, load_event)

def schedule_unload_event():
    global simulation_time, machine_count
    unload_event = Event(simulation_time, "Unload", queue, machine_count)
    heapq.heappush(event_queue, unload_event)

# initialize queue
machine_count = 1
simulation_time = 0
queue = 0

# initialize all events
schedule_arrival_event()
schedule_arrival_event()

# Main simulation loop
while event_queue:
    current_event = heapq.heappop(event_queue)

    print("Event: ", current_event.event_type, ", Elapsed_time: ", current_event.time)
    print("state_variable[Q] = ", current_event.queue)
    print("state_variable[M] = ", current_event.machine_count)

    if current_event.event_type == EVENT_TYPE_ARRIVAL:
        process_arrival()
    elif current_event.event_type == EVENT_TYPE_LOAD:
        process_load()
    elif current_event.event_type == EVENT_TYPE_UNLOAD:
        process_unload()
    elif current_event.event_type == EVENT_TYPE_ENTER:
        process_enter()
