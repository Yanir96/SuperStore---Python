from Home_work_year_2.Super_store.Exceptions_Classes.Errors import IdError, PriceError \
    , SecondEntryError, YearError, ThirdEntryError

VALID_YEARS = list(range(2018, 2024))


def validate_year(year):
    """A function that gets year and make exceptions, if ok returns the year else raises exceptions"""
    if type(year) != int and not year.isnumeric():
        raise YearError(f"         Year should be a number! [{year}]")
    year = int(year)

    if not year in VALID_YEARS:
        raise YearError(f"Year ({year}) must be one of:\n {VALID_YEARS}")
    else:
        return year


def validate_id(product_id):
    """A function that gets ID and make exceptions, if ok returns the year else raises exceptions"""
    if not product_id.isnumeric() or product_id == "":
        raise IdError(f"ID should be a number! [{product_id}]")
    else:
        return product_id


def validate_price(product_price):
    """A function that gets price and make exceptions, if ok returns the year else raises exceptions"""
    if not product_price.isnumeric() or product_price == "":
        raise PriceError(f"Price should be a number! [{product_price}]")
    else:
        return product_price


def validate_second_entry(second_entry):
    """A function that gets input from the second entry and make exceptions,
     if ok returns the year else raises exceptions"""
    if not second_entry.isnumeric() or second_entry == "":
        raise SecondEntryError(f" should be a number! [{second_entry}]")
    else:
        return second_entry


def validate_third_entry(third_entry):
    """A function that gets input from the third entry and make exceptions,
         if ok returns the year else raises exceptions"""
    if not third_entry.isnumeric() or third_entry == "":
        raise ThirdEntryError(f" should be a number! [{third_entry}]")
    else:
        return third_entry
