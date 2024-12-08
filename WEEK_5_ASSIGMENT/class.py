class Smartphone:
  """Represents a smartphone device."""

  def __init__(self, brand, model, color, storage):
    """Constructor to initialize a Smartphone object."""
    self.brand = brand
    self.model = model
    self.color = color
    self.storage = storage
    self.battery_level = 100  # Initial battery level

  def make_call(self, number):
    """Simulates making a phone call."""
    print(f"Calling {number}...")

  def send_message(self, recipient, message):
    """Simulates sending a text message."""
    print(f"Sending message to {recipient}: {message}")

  def check_battery(self):
    """Displays the current battery level."""
    print(f"Battery level: {self.battery_level}%")

  def charge(self, minutes):
    """Simulates charging the phone."""
    charging_rate = 2  # Example charging rate: 2% per minute
    self.battery_level += charging_rate * minutes
    self.battery_level = min(self.battery_level, 100)  # Ensure battery doesn't exceed 100%

# Example usage:
my_phone = Smartphone("Apple", "iPhone 15", "Midnight", 256)
my_phone.make_call("555-1234")
my_phone.send_message("Friend", "Hey, how are you?")
my_phone.check_battery()
my_phone.charge(30)
my_phone.check_battery()