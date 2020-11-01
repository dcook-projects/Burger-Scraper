import openpyxl as xl
import scraping


def scrape_burger_data(burgers):
    scraping.get_burger_bros(burgers)
    scraping.get_longboard_cafe(burgers)
    scraping.get_gordon_biersch(burgers)
    scraping.get_wegmans_burger(burgers)
    scraping.get_abbey_burger_bistro(burgers)
    scraping.get_alaska_stand(burgers)
    scraping.get_doghaus_biergarten(burgers)


def create_spreadsheet(burgers, filename):
    workbook = xl.Workbook()

    # set up the initial sheet
    ws = workbook.active
    current_restaurant_name = burgers[0].restaurant_name
    ws.title = current_restaurant_name

    # Go through the list of burgers and extract the data to put into the spreadsheet
    current = 0
    for burger in burgers:
        row = [burger.restaurant_name, burger.name, burger.price]
        if burgers[current].restaurant_name == current_restaurant_name:
            ws.append(row)
        else:
            current_restaurant_name = burgers[current].restaurant_name
            ws = workbook.create_sheet(current_restaurant_name)
            ws.append(row)

        current += 1

    workbook.save(filename)


def run():
    burgers = []
    scrape_burger_data(burgers)
    create_spreadsheet(burgers, "burgers.xlsx")


run()