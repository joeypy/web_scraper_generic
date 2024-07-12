import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_website_table(url, table_selector=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    if table_selector:
        table = soup.select_one(table_selector)
    else:
        # Si no se proporciona un selector, busca la primera tabla en la página
        table = soup.find("table")

    if not table:
        # Si aún no se encuentra una tabla, busca todas las tablas y permite al usuario elegir
        tables = soup.find_all("table")
        if not tables:
            raise ValueError("No se encontraron tablas en la página")
        elif len(tables) == 1:
            table = tables[0]
        else:
            # Aquí podrías implementar una lógica para que el usuario elija la tabla correcta
            # Por ahora, simplemente tomaremos la primera tabla
            table = tables[0]

    df = pd.read_html(str(table))[0]
    return df.to_dict("records")
