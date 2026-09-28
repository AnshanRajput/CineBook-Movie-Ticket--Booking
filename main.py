movies = {
    1: {
        "name": "Avengers: Endgame",
        "language": "English",
        "price": 220,
        "seats": [f"A{i}" for i in range(1, 7)] + [f"B{i}" for i in range(1, 7)]
    },
    2: {
        "name": "Demon Slayer: Infinity Castle",
        "language": "Japanese",
        "price": 200,
        "seats": [f"A{i}" for i in range(1, 7)] + [f"B{i}" for i in range(1, 7)]
    },
    3: {
        "name": "Jujutsu Kaisen",
        "language": "Japanese",
        "price": 180,
        "seats": [f"A{i}" for i in range(1, 7)] + [f"B{i}" for i in range(1, 7)]
    },
    4: {
        "name": "Spider-Man: No Way Home",
        "language": "English",
        "price": 200,
        "seats": [f"A{i}" for i in range(1, 7)] + [f"B{i}" for i in range(1, 7)]
    }
}

bookings = {}
next_booking_id = 1001


def line():
    print("═" * 55)


def display_movies():
    line()
    print("                    AVAILABLE MOVIES")
    line()

    for movie_id, movie in movies.items():
        print(f"{movie_id}. {movie['name']}")
        print(f"   Language : {movie['language']}")
        print(f"   Price    : ₹{movie['price']}")
        print()

    line()


def display_seats(movie_id):
    movie = movies[movie_id]
    booked_seats = []

    for booking in bookings.values():
        if booking["movie_id"] == movie_id:
            booked_seats.append(booking["seat"])

    print()
    line()
    print(f"              SEATS - {movie['name']}")
    line()
    print("                 SCREEN")
    print("              ─────────────")
    print()

    for row in ["A", "B"]:
        for number in range(1, 7):
            seat = f"{row}{number}"

            if seat in booked_seats:
                print(f"[{seat}: X]", end=" ")
            else:
                print(f"[{seat}: O]", end=" ")

        print()

    print()
    print("O = Available    X = Booked")
    line()


def get_movie_choice():
    display_movies()

    while True:
        choice = input("Enter movie number: ")

        if choice.isdigit() and int(choice) in movies:
            return int(choice)

        print("Invalid movie number. Please try again.")


def book_ticket():
    global next_booking_id

    movie_id = get_movie_choice()
    display_seats(movie_id)

    movie = movies[movie_id]

    while True:
        seat = input("Enter seat number: ").upper()

        if seat not in movie["seats"]:
            print("Invalid seat number. Please try again.")
            continue

        already_booked = False

        for booking in bookings.values():
            if booking["movie_id"] == movie_id and booking["seat"] == seat:
                already_booked = True
                break

        if already_booked:
            print("This seat is already booked. Choose another seat.")
        else:
            break

    name = input("Enter customer name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter customer name: ").strip()

    amount = movie["price"]

    bookings[next_booking_id] = {
        "name": name,
        "movie_id": movie_id,
        "movie": movie["name"],
        "seat": seat,
        "amount": amount
    }

    line()
    print("                 BOOKING CONFIRMED")
    line()
    print(f"Booking ID : {next_booking_id}")
    print(f"Customer   : {name}")
    print(f"Movie      : {movie['name']}")
    print(f"Seat       : {seat}")
    print(f"Amount     : ₹{amount}")
    line()

    next_booking_id += 1


def cancel_booking():
    if not bookings:
        print("\nThere are no bookings to cancel.")
        return

    booking_id = input("Enter Booking ID: ")

    if not booking_id.isdigit():
        print("Invalid Booking ID.")
        return

    booking_id = int(booking_id)

    if booking_id not in bookings:
        print("Booking not found.")
        return

    booking = bookings[booking_id]

    line()
    print("                 BOOKING DETAILS")
    line()
    print(f"Booking ID : {booking_id}")
    print(f"Customer   : {booking['name']}")
    print(f"Movie      : {booking['movie']}")
    print(f"Seat       : {booking['seat']}")
    print(f"Amount     : ₹{booking['amount']}")
    line()

    confirm = input("Cancel this booking? (Y/N): ").upper()

    if confirm == "Y":
        del bookings[booking_id]
        print("Booking cancelled successfully.")
    else:
        print("Booking cancellation stopped.")


def view_bookings():
    if not bookings:
        print("\nNo bookings available.")
        return

    line()
    print("                    ALL BOOKINGS")
    line()

    for booking_id, booking in bookings.items():
        print(f"Booking ID : {booking_id}")
        print(f"Customer   : {booking['name']}")
        print(f"Movie      : {booking['movie']}")
        print(f"Seat       : {booking['seat']}")
        print(f"Amount     : ₹{booking['amount']}")
        print("-" * 55)


def search_booking():
    if not bookings:
        print("\nNo bookings available.")
        return

    booking_id = input("Enter Booking ID: ")

    if not booking_id.isdigit():
        print("Invalid Booking ID.")
        return

    booking_id = int(booking_id)

    if booking_id not in bookings:
        print("Booking not found.")
        return

    booking = bookings[booking_id]

    line()
    print("                 BOOKING FOUND")
    line()
    print(f"Booking ID : {booking_id}")
    print(f"Customer   : {booking['name']}")
    print(f"Movie      : {booking['movie']}")
    print(f"Seat       : {booking['seat']}")
    print(f"Amount     : ₹{booking['amount']}")
    line()


def main():
    while True:
        print()
        line()
        print("                 🎬 CINEBOOK")
        print("          MOVIE TICKET BOOKING SYSTEM")
        line()
        print("1. Display Movies")
        print("2. View Available Seats")
        print("3. Book Ticket")
        print("4. Cancel Booking")
        print("5. View All Bookings")
        print("6. Search Booking")
        print("7. Exit")
        line()

        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            movie_id = get_movie_choice()
            display_seats(movie_id)

        elif choice == "3":
            book_ticket()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            view_bookings()

        elif choice == "6":
            search_booking()

        elif choice == "7":
            print("\nThank you for using CineBook!")
            print("Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()