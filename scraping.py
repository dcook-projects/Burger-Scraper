import burger_data as bd
import requests
from bs4 import BeautifulSoup


def get_soup_object(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_burger_bros(burger_list):
    soup = get_soup_object("http://www.burgerbrosburgers.com/Menu.html")
    b_tags = soup.find_all("b")

    # strings that contain the burger item and price
    hamburger = b_tags[1].string
    cheeseburger = b_tags[2].string
    bacon_cheeseburger = b_tags[3].string
    bacon_cheeseburger_price = b_tags[4].contents[0]
    bacon_cheeseburger_price_only = bacon_cheeseburger_price[-4:]  # bacon cheeseburger is formatted differently than the others

    # Extract the burger names and prices without the dots
    hamburger_name = hamburger[:9]
    hamburger_price = hamburger[-4:]
    cheeseburger_name = cheeseburger[:12]
    cheeseburger_price = cheeseburger[-4:]

    # Create burger objects and add them to the list
    burger_list.append(bd.Burger("Burger Bros.", hamburger_name, hamburger_price))
    burger_list.append(bd.Burger("Burger Bros.", cheeseburger_name, cheeseburger_price))
    burger_list.append(bd.Burger("Burger Bros.", bacon_cheeseburger, bacon_cheeseburger_price_only))


def get_longboard_cafe(burger_list):
    soup = get_soup_object("https://www.longboardcafe.net/menu#menu=served-all-day")
    h4_tags = soup.find_all("h4")

    # locations in the h4 tag list where the burgers are located
    lower_bound = 15
    upper_bound = 21
    current = lower_bound

    # Extract burger data and make new Burger objects to add to the list
    while lower_bound <= current <= upper_bound:
        burger_list.append(bd.Burger("Longboard Cafe", h4_tags[current].string,
                                     h4_tags[current].next_sibling.contents[0].string[1:]))

        current += 1


def get_gordon_biersch(burger_list):
    soup = get_soup_object("https://gordonbiersch.olo.com/menu/gb-annapolis")
    burger_name_tags = soup.find_all("span", class_="product-name")
    burger_price_tags = soup.find_all("span", class_="product__attribute--price")

    # location in the span tags where the burgers are located
    lower_bound = 29
    upper_bound = 33
    current = lower_bound
    while lower_bound <= current <= upper_bound:
        burger_list.append(bd.Burger("Gordon Biersch", burger_name_tags[current].string,
                                     burger_price_tags[current - 1].string[1:]))  # price tags are one off from the food name tags

        current += 1


def get_wegmans_burger(burger_list):
    soup = get_soup_object("https://www.wegmansburgerbar.com/menus/owings-mills-md-menu/")
    h1_tags = soup.find_all("h1")
    h4_tags = soup.find_all("h4")
    span_fr_tags = soup.find_all("span", class_="fr")

    # The first burger on the menu is under a different tag than the rest
    burger_name = h1_tags[1].string
    burger_price = span_fr_tags[0].string[1:]
    burger_list.append(bd.Burger("Wegman's Burger Bar", burger_name, burger_price))

    # Get the rest of the burgers
    burger_index_lower_bound = 4
    burger_index_upper_bound = 8
    current = 0
    for tag in span_fr_tags:
        if burger_index_lower_bound <= current <= burger_index_upper_bound:
            burger_name = h4_tags[current].string.replace("*", "")  # a few of the burgers have an asterisk in the name
            burger_price = span_fr_tags[current].string

            # Get rid of the calorie information from the burger price string
            burger_price = burger_price.split(" ")
            burger_price = burger_price[0][1:]

            # Create Burger objects and add them to the list
            burger_list.append(bd.Burger("Wegman's Burger Bar", burger_name, burger_price))

        current += 1


def get_abbey_burger_bistro(burger_list):
    soup = get_soup_object("https://abbeyburger.com/menu/")

    # burger names and prices are in div tags with different classes
    name_tags = soup.find_all("div", class_="av-catalogue-title")
    price_tags = soup.find_all("div", class_="av-catalogue-price")

    # find the burgers in the tag list
    lower_bound = 17
    upper_bound = 27
    current = lower_bound
    while lower_bound <= current <= upper_bound:
        # Add burgers to the list
        burger_list.append(bd.Burger("Abbey Burger Bistro", name_tags[current].string,
                                     price_tags[current].string[1:]))

        current += 1


def get_alaska_stand(burger_list):
    soup = get_soup_object("https://alaskastand.com/menu/")
    burger_tags = soup.find_all("h4")
    price_tags = soup.find_all("div", class_="dish-price")

    # find the burgers in the tag list (20-30, 61-62, 67)
    lower_bound = 20
    upper_bound = 30
    current = lower_bound
    while lower_bound <= current <= upper_bound:
        burger_list.append(bd.Burger("Alaska Stand", burger_tags[current].string,
                                     price_tags[current].string))

        current += 1

    lower_bound = 61
    upper_bound = 62
    current = lower_bound
    while lower_bound <= current <= upper_bound:
        burger_list.append(bd.Burger("Alaska Stand", burger_tags[current].string,
                                     price_tags[current].string))

        current += 1

    lower_bound = 67
    upper_bound = 67
    current = lower_bound
    while lower_bound <= current <= upper_bound:
        burger_list.append(bd.Burger("Alaska Stand", burger_tags[current].string,
                                     price_tags[current].string))

        current += 1


def get_doghaus_biergarten(burger_list):
    soup = get_soup_object("https://order.doghaus.com/menu/dog-haus-bethesda")
    burger_name_tags = soup.find_all("span", class_="product-name")
    burger_price_tags = soup.find_all("span", class_="product__attribute--price")

    # find the burgers in the tag list (22-28, 32-33)
    lower_bound = 22
    upper_bound = 28
    current = lower_bound
    while lower_bound <= current <= upper_bound:
        # Add burger objects to the list
        burger_list.append(bd.Burger("Doghaus Biergarten", burger_name_tags[current].string,
                                     burger_price_tags[current].string[1:]))

        current += 1

    lower_bound = 32
    upper_bound = 33
    current = lower_bound
    while lower_bound <= current <= upper_bound:
        # Add burger objects to the list
        burger_list.append(bd.Burger("Doghaus Biergarten", burger_name_tags[current].string,
                                     burger_price_tags[current].string[1:]))

        current += 1