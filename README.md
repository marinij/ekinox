# ekinox_technical_test

## compute_basket
<pre>
NAME
    ekinox_technical_test.compute_basket

FUNCTIONS  
    compute_basket_price(movies: list[str], movie_price: int, franchises: list[dict]) -> int  
        Two-dimensional, size-mutable, potentially heterogeneous tabular data.  
        Data structure also contains labeled axes (rows and columns).  
        Arithmetic operations align on both row and column labels. Can be  
        thought of as a dict-like container for Series objects. The primary  
        pandas data structure.  
        Parameters  
        ----------  
        movies : list[str]  
            List of movies in the basket.  
        movie_price : int  
            Base price of an unfranchised movie.  
        franchises : list[dict]  
            List of dictionaries describing the franchises.  
            A franchise is must have the following attributes:  
                name: str  
                    name of the franchise  
                price: int  
                    price of one movie of this franchise  
                discount_per_movie: dict[int, int]  
                    dictionary describing the discount off the basket based on the number of UNIQUE franchised movies  
                    Example:  
                    {2: 10, 3: 20}  
                    For 2 DIFFERENT movies of the same franchise, 10% discount is applied on the basket  
                    For 3 DIFFERENT movies of the same franchise, 20% discount is applied on the basket  
</pre>