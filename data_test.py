import numpy as np
import jsonlines as jl
from pprint import pprint
import itertools

#file_LIST = ['car', 'shoe', 'backpack', 'sun', 'power_outlet']
file_LIST = ["bird", "birthdaycake"]


for _file in file_LIST:

    NorthAmerica = ["AI", "AG", "AW", "BS", "BB", "BZ", "BM", "BQ", "VG", "CA", "KY", "CR", "CU", "CW", "DM", "DO", "SV", "GL", "GD", "GP", "GT", "HT", "HN", "JM", "MQ", "MX", "PM", "MS", "CW", "KN", "NI", "PA", "PR", "BQ", "SX", "LC", "PM", "VC", "TT", "TC", "US", "VI"]
    SouthAmerica = ["AR", "BO", "BR", "CL", "CO", "EC", "FK", "GF", "GY", "GY", "PY", "PE", "SR", "UY", "VE"]
    Africa = ["DZ", "AO", "SH", "BJ", "BW", "BF", "BI", "CM", "CV", "CF", "TD", "KM", "CG", "CD", "DJ", "EG", "GQ", "ER", "ET", "GA", "GM", "GH", "GN", "GW", "CI", "KE", "LS", "LR", "LY", "MG", "MW", "ML", "MR", "MU", "YT", "MA", "MZ", "NA", "NE", "NG", "ST", "SN", "SC", "SL", "SO", "ZA", "SS", "SH", "SD", "SZ", "TZ", "TG", "TN", "UG", "CD", "ZM", "TZ", "ZW"]
    Europe = ["AL", "AD", "AT", "BY", "BE", "BA", "BG", "HR", "CY", "CZ", "DK", "EE", "FO", "FI", "FR", "DE", "GI", "GR", "HU", "IS", "IE", "IM", "IT", "RS", "LV", "LI", "LT", "LU", "MK", "MT", "MD", "MC", "ME", "NL", "NO", "PL", "PT", "RO", "RU", "SM", "RS", "SK", "SI", "ES", "SE", "CH", "UA", "BG", "VA", "RS"]
    Asia = ["AF", "AM", "AZ", "BH", "BD", "BT", "BN", "KH", "CN", "CX", "CC", "IO", "GE", "HK", "IN", "ID", "IR", "IQ", "IL", "JP", "JO", "KZ", "KW", "KG", "LA", "LB", "MO", "MY", "MV", "MN", "MM", "NP", "KP", "OM", "PK", "PS", "PH", "QA", "SA", "SG", "KR", "LK", "SY", "TW", "TJ", "TH", "TR", "TM", "AE", "UZ", "VN", "YE"]
    Oceana_Australia= ["AS", "AU", "NZ", "CK", "TL", "FM", "FJ", "PF", "GU", "KI", "MP", "MH", "UM", "NR", "NC", "NZ", "NU", "NF", "PW", "PG", "MP", "WS", "SB", "TK", "TO", "TV", "VU", "UM", "WF"]

    OVERALL_LIST = []
    NA_LIST = []
    SA_LIST = []
    AF_LIST = []
    EU_LIST = []
    AS_LIST = []
    OA_LIST = []
    NON_NA_LIST = []

    with jl.open(f"./data/{_file}.ndjson") as reader:
        for obj in reader:
            d={}
            d["continentcode"] = ""
            d["drawing"] = obj["drawing"]
            if obj["countrycode"] in NorthAmerica:
                d["continentcode"] = "NA"
                NA_LIST.append(d)
            elif obj["countrycode"] in SouthAmerica:
                d["continentcode"] = "SA"
                SA_LIST.append(d)
                d["continentcode"] = "NON_NA"
                NON_NA_LIST.append(d)
            elif obj["countrycode"] in Africa:
                d["continentcode"] = "AF"
                AF_LIST.append(d)
                d["continentcode"] = "NON_NA"
                NON_NA_LIST.append(d)
            elif obj["countrycode"] in Europe:
                d["continentcode"] = "EU"
                EU_LIST.append(d)
                d["continentcode"] = "NON_NA"
                NON_NA_LIST.append(d)
            elif obj["countrycode"] in Asia:
                d["continentcode"] = "AS"
                AS_LIST.append(d)
                d["continentcode"] = "NON_NA"
                NON_NA_LIST.append(d)
            elif obj["countrycode"] in Oceana_Australia:
                d["continentcode"] = "OA"
                OA_LIST.append(d)
                d["continentcode"] = "NON_NA"
                NON_NA_LIST.append(d)

    file = open(f'./data/{_file}/1/NA_{_file}.jsonl', 'w')
    for json in NA_LIST:
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/{_file}/2/NA_{_file}.jsonl', 'w')
    for json in NA_LIST:
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/{_file}/1/SA_{_file}.jsonl', 'w')
    for json in SA_LIST:
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/{_file}/1/AF_{_file}.jsonl', 'w')
    for json in AF_LIST:
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/{_file}/1/EU_{_file}.jsonl', 'w')
    for json in EU_LIST:
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/{_file}/1/AS_{_file}.jsonl', 'w')
    for json in AS_LIST:
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/{_file}/1/OA_{_file}.jsonl', 'w')
    for json in OA_LIST:
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/{_file}/2/NON_NA_{_file}.jsonl', 'w')
    for json in NON_NA_LIST:
        file.write(f"{json}\n")
    file.close()

    print(f"Total {_file} doodles: " + str(len(OVERALL_LIST)) + "\n")

    print("North America total: \n" + str(len(NA_LIST)) + "\n")

    print("South American total: " + str(len(SA_LIST)) + "\n")

    print("Africa total: " + str(len(AF_LIST)) + "\n")

    print("Europe total: \n" + str(len(EU_LIST)) + "\n")

    print("Asia total: " + str(len(AS_LIST)) + "\n")

    print("Oceana/Australia total: " + str(len(OA_LIST)) + "\n")

    print("Non North America total: " + str(len(NON_NA_LIST)) + "\n")

    print("-"*20)


print('done :)')
