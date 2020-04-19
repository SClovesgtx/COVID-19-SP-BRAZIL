import tabula
import pandas as pd
import os
import re
import argparse

# regex to identify names of municipalities followed by numbers related to covid-19
# exemple:
# s = 'ÁGUAS DE LINDÓIA 1 1 ILHA COMPRIDA 9 - POÁ 9 1'
# M.findall(s) |--> output: [('ÁGUAS DE LINDÓIA ', '1 1 '), ('ILHA COMPRIDA ', '9 - '), ('POÁ ', '9 1')]
M = re.compile(r'([A-ZùÙÁÁÀÂÄÃÉÈÊÍÌÓÒÔÖÕÚÙÜÇ ]{1,100})([0-9- ]{1,10})')

def parse_ugly_df(ugly_df):
    data = []
    for _, row in ugly_df.iterrows():
        string = ''
        for col in row.index:
            string  += " " + str(row[col])
        data.append(string)

    del data[0]
    data2 = []
    for string in data:
        data2 += M.findall(string)
    data3 = []
    for item in data2:
        cases = item[1]
        cases = cases.split(" ")
        cases = [int(s) if s != '-' else 0 for s in cases if s != '']
        data3.append([item[0][:-1]] + cases)
    petty_df = pd.DataFrame(data=data3, columns=["City", "Confirmed", "Deaths"])
    return petty_df

def do_geocode(address):
    geolocator = Nominatim(user_agent="clovesgtx@hotmail.com")
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)

def rightDf(df):
    right_column = "Casos de COVID-19 por município de residência, São Paulo"
    columns = df.columns
    for col in columns:
        if right_column in col:
            return True
    return False

def main(args):
    bulletins_names =  os.listdir(args.path)
    df_list = []
    for pdf in bulletins_names:
        boletim_and_date = pdf.split("_")
        boletim = boletim_and_date[1]
        date = boletim_and_date[2][:-4] + "20"
        file_path = args.path + '/' + pdf
        ugly_df_list = tabula.read_pdf(file_path, pages='all')
        for ugly_df in ugly_df_list:
            if ugly_df.shape[0] > 0:
                rigth_df = rightDf(ugly_df)
                if rigth_df:
                    break
        petty_df = parse_ugly_df(ugly_df)
        petty_df["Date"] = date
        petty_df["Bulletin"] = boletim
        df_list.append(petty_df)

    df_covid = pd.concat(df_list)
    df_covid = df_covid = df_covid[["Date", "Bulletin", "City", "Confirmed", "Deaths"]]
    df_covid.to_csv("data/covid-19-municipios-sp.csv", index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='Epidemiological bulletins PDF parser')

    parser.add_argument('-p', '--path', type=str, required=True,
                        help='Path to the directory where epidemiological bulletins are found')

    args = parser.parse_args()
    main(args)
