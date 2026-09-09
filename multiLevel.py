# Parent Class 1
class Camera:

    def take_photo(self):
        print("Photo taken successfully.")

    def record_video(self):
        print("Video recording started.")


# Parent Class 2
class MusicPlayer:

    def play_music(self):
        print("Music is playing.")

    def stop_music(self):
        print("Music stopped.")


# Parent Class 3
class GPS:

    def current_location(self):
        print("Current location: Pune, Maharashtra")

    def navigate(self):
        print("Navigation started.")


# Child Class - Multiple Inheritance
class SmartPhone(Camera, MusicPlayer, GPS):

    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def display_details(self):
        print("Brand   :", self.brand)
        print("Model   :", self.model)
        print("Price   :", self.price)
        print("Storage :", self.storage)


# ==================================================
# Create 3 Smartphone Objects
# ==================================================

phone1 = SmartPhone(
    "Samsung",
    "Galaxy S25",
    79999,
    "256GB"
)

phone2 = SmartPhone(
    "Apple",
    "iPhone 17",
    99999,
    "256GB"
)

phone3 = SmartPhone(
    "OnePlus",
    "OnePlus 13",
    69999,
    "512GB"
)


# ==================================================
# Demonstrating Smartphone 1
# ==================================================

print("\n========== SMARTPHONE 1 ==========")

phone1.display_details()

print("\n--- Camera Functions ---")
phone1.take_photo()
phone1.record_video()

print("\n--- Music Player Functions ---")
phone1.play_music()
phone1.stop_music()

print("\n--- GPS Functions ---")
phone1.current_location()
phone1.navigate()


# ==================================================
# Demonstrating Smartphone 2
# ==================================================

print("\n========== SMARTPHONE 2 ==========")

phone2.display_details()

phone2.take_photo()
phone2.record_video()
phone2.play_music()
phone2.stop_music()
phone2.current_location()
phone2.navigate()


# ==================================================
# Demonstrating Smartphone 3
# ==================================================

print("\n========== SMARTPHONE 3 ==========")

phone3.display_details()

phone3.take_photo()
phone3.record_video()
phone3.play_music()
phone3.stop_music()
phone3.current_location()
phone3.navigate()