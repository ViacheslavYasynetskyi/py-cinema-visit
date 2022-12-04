from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers_list = []
    for guest in customers:
        customers_list.append(Customer(guest["name"], guest["food"]))
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_staff = Cleaner(cleaning_staff)
    for customer in customers_list:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie_name, customers_list, cinema_staff)
