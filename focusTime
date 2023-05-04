import time

def focus_timer(minutes):
    """Start a focus timer for the specified number of minutes."""
    
    # Convert minutes to seconds
    seconds = minutes * 60
    
    # Start the timer
    print("Focus timer started for {} minutes.".format(minutes))
    while seconds > 0:
        print("Time remaining: {} seconds.".format(seconds))
        time.sleep(1)
        seconds -= 1
    
    # Timer is finished
    print("Focus timer finished.")
