import random
import time

def generate_iot_data():
    """Simulate IoT data - temperature readings."""
    return {'temperature': round(random.uniform(20.0, 30.0), 2)}

# Example of generating data every 5 seconds
if __name__ == "__main__":
    while True:
        data = generate_iot_data()
        print(f"Generated IoT Data: {data}")
        time.sleep(5)
