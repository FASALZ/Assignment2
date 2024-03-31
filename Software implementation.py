class Artwork:
    def __init__(self, title, artist, creation_date, historical_significance, location):
        self.title = title
        self.artist = artist
        self.creation_date = creation_date
        self.historical_significance = historical_significance
        self.location = location

    def display_info(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Creation Date: {self.creation_date}, Historical Significance: {self.historical_significance}, Location: {self.location}")

class Exhibition:
    def __init__(self, name, start_date, end_date, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

class Visitor:
    def __init__(self, name, age, visitor_type):
        self.name = name
        self.age = age
        self.visitor_type = visitor_type
        self.tickets = []

    def purchase_ticket(self, ticket):
        self.tickets.append(ticket)

class Ticket:
    VAT = 0.05

    def __init__(self, event_name, event_date, location, base_price, is_group=False):
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.base_price = base_price
        self.is_group = is_group

    def calculate_price(self):
        discount = 0.5 if self.is_group else 1
        final_price = (self.base_price * discount) + (self.base_price * Ticket.VAT * discount)
        return final_price

    def display_receipt(self):
        print(f"Event: {self.event_name}, Date: {self.event_date}, Location: {self.location}, Price: {self.calculate_price()} AED")

class Tour(Ticket):
    def __init__(self, event_name, event_date, location, base_price, visitor_group_size, guide_name):
        is_group = visitor_group_size >= 15
        super().__init__(event_name, event_date, location, base_price, is_group)
        self.visitor_group_size = visitor_group_size
        self.guide_name = guide_name

class SpecialEvent(Ticket):
    def __init__(self, event_name, event_date, location, special_ticket_price):
        super().__init__(event_name, event_date, location, special_ticket_price)

# Test Cases
def run_test_cases():
    # Test Case A: Adding new art
    napoleon_crossing_the_alps = Artwork("Napoleon Crossing the Alps", "Jacques-Louis David", "1801", "Symbolizes Napoleon’s strength and determination", "Permanent Gallery")
    napoleon_crossing_the_alps.display_info()

    # Test Case B: Opening a new exhibition
    neoclassicism = Exhibition("Neoclassicism and Revolution", "2024-01-01", "2024-12-31", "Exhibition Hall 2")
    neoclassicism.add_artwork(napoleon_crossing_the_alps)
    print(f"New exhibition: {neoclassicism.name}")
    for artwork in neoclassicism.artworks:
        artwork.display_info()

    # Test Case C: Purchasing tickets
    faton_alzaabi = Visitor("Faton Alzaabi", 30, "adult")
    night_at_museum = SpecialEvent("Night at the Museum", "2024-05-15", "Main Hall", 100)
    faton_alzaabi.purchase_ticket(night_at_museum)
    print(f"{faton_alzaabi.name} purchased a ticket for {faton_alzaabi.tickets[0].event_name}")

    # Test Case D: Displaying payment receipts
    historical_tour = Tour("Historical Tour", "2024-06-20", "Museum Grounds", 63, 20, "Mr. Smith")
    faton_alzaabi.purchase_ticket(historical_tour)
    for ticket in faton_alzaabi.tickets:
        ticket.display_receipt()

if __name__ == "__main__":
    run_test_cases()
