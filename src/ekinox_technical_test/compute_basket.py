import argparse
import yaml
import os


def compute_basket_price(movies: list[str], movie_price: int, franchises: list[dict]) -> int:
    """
    Compute a basket price based on a list of movies, a base movie price and a list discounted franchises.
    Parameters
    ----------
    movies : list[str]
        List of movies in the basket.
    movie_price : int
        Base price of an unfranchised movie.
    franchises : list[dict]
        List of dictionaries describing the franchises.
        A franchise must have the following attributes:
            name: str
                name of the franchise.
            price: int
                price of one movie of this franchise.
            discount_per_movie: dict[int, int]
                dictionary describing the discount off the basket based on the number of UNIQUE franchised movies.
                Example:
                {2: 10, 3: 20}
                For 2 DIFFERENT movies of the same franchise, 10% discount is applied on the basket
                For 3 DIFFERENT movies of the same franchise, 20% discount is applied on the basket
    """
    price = 0

    unfranchised_movies = len(movies)
    for franchise in franchises:
        found_franchised_movies = sum(
            franchise['name'].lower() in movie.lower() for movie in movies)
        found_unique_franchised_movies = sum(
            franchise['name'].lower() in movie.lower() for movie in set(movies))
        discount_level = min(franchise['discount_per_movie'], key=lambda discount_level: abs(
            discount_level - found_unique_franchised_movies))
        if found_unique_franchised_movies < discount_level:  # no discount
            price += found_franchised_movies * franchise['price']
        else:
            price += found_franchised_movies * \
                franchise['price'] * \
                (100 - franchise['discount_per_movie'][discount_level]) / 100
        unfranchised_movies -= found_franchised_movies

    return price + max(0, unfranchised_movies) * movie_price


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='compute_basket', description='Applies discount on the provided basket based on the provided configuration')
    parser.add_argument(
        'basket', type=str, help='file containing the list of movies in the basket')
    parser.add_argument('config', type=str,
                        help='file containing the price and franchises configuration')
    args = parser.parse_args()

    with open(args.config, 'r') as yaml_config:
        config = yaml.safe_load(yaml_config)

    if not os.path.exists(args.basket):
        raise Exception("basket file not found")

    with open(args.basket) as movies:
        print(compute_basket_price(movies=movies.read().splitlines(),
              movie_price=config['base_price'], franchises=config['franchises']))
