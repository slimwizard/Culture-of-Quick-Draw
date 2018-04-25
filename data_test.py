import numpy as np
import jsonlines as jl
from pprint import pprint
import itertools

file_list = ['car', 'shoe', 'backpack', 'sun', 'power_outlet']
for _file in file_list:

    NorthAmerica = ["AI", "AG", "AW", "BS", "BB", "BZ", "BM", "BQ", "VG", "CA", "KY", "CR", "CU", "CW", "DM", "DO", "SV", "GL", "GD", "GP", "GT", "HT", "HN", "JM", "MQ", "MX", "PM", "MS", "CW", "KN", "NI", "PA", "PR", "BQ", "SX", "LC", "PM", "VC", "TT", "TC", "US", "VI"]
    SouthAmerica = ["AR", "BO", "BR", "CL", "CO", "EC", "FK", "GF", "GY", "GY", "PY", "PE", "SR", "UY", "VE"]
    Africa = ["DZ", "AO", "SH", "BJ", "BW", "BF", "BI", "CM", "CV", "CF", "TD", "KM", "CG", "CD", "DJ", "EG", "GQ", "ER", "ET", "GA", "GM", "GH", "GN", "GW", "CI", "KE", "LS", "LR", "LY", "MG", "MW", "ML", "MR", "MU", "YT", "MA", "MZ", "NA", "NE", "NG", "ST", "SN", "SC", "SL", "SO", "ZA", "SS", "SH", "SD", "SZ", "TZ", "TG", "TN", "UG", "CD", "ZM", "TZ", "ZW"]
    Europe = ["AL", "AD", "AT", "BY", "BE", "BA", "BG", "HR", "CY", "CZ", "DK", "EE", "FO", "FI", "FR", "DE", "GI", "GR", "HU", "IS", "IE", "IM", "IT", "RS", "LV", "LI", "LT", "LU", "MK", "MT", "MD", "MC", "ME", "NL", "NO", "PL", "PT", "RO", "RU", "SM", "RS", "SK", "SI", "ES", "SE", "CH", "UA", "BG", "VA", "RS"]
    Asia = ["AF", "AM", "AZ", "BH", "BD", "BT", "BN", "KH", "CN", "CX", "CC", "IO", "GE", "HK", "IN", "ID", "IR", "IQ", "IL", "JP", "JO", "KZ", "KW", "KG", "LA", "LB", "MO", "MY", "MV", "MN", "MM", "NP", "KP", "OM", "PK", "PS", "PH", "QA", "SA", "SG", "KR", "LK", "SY", "TW", "TJ", "TH", "TR", "TM", "AE", "UZ", "VN", "YE"]
    Oceana_Australia= ["AS", "AU", "NZ", "CK", "TL", "FM", "FJ", "PF", "GU", "KI", "MP", "MH", "UM", "NR", "NC", "NZ", "NU", "NF", "PW", "PG", "MP", "WS", "SB", "TK", "TO", "TV", "VU", "UM", "WF"]


    overall_list = []
    NA_list = []
    SA_list = []
    AF_list = []
    EU_list = []
    AS_list = []
    OA_list = []

    with jl.open(f"./data/{_file}.ndjson") as reader:
        index = 0
        for obj in reader:
            d={}
            d['countrycode'] = obj['countrycode']
            d['drawing'] = obj['drawing']
            index += 1
            overall_list.append(d)

    for i in overall_list:
        if i['countrycode'] in NorthAmerica:
            NA_list.append(i)
        elif i['countrycode'] in SouthAmerica:
            SA_list.append(i)
        elif i['countrycode'] in Africa:
            AF_list.append(i)
        elif i['countrycode'] in Europe:
            EU_list.append(i)
        elif i['countrycode'] in Asia:
            AS_list.append(i)
        elif i['countrycode'] in Oceana_Australia:
            OA_list.append(i)
    file = open(f'./data/NA_{_file}.jsonl', 'w')
    for json in NA_list:
        json['countrycode'] = 'NA'
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/SA_{_file}.jsonl', 'w')
    for json in SA_list:
        json['countrycode'] = 'SA'
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/AF_{_file}.jsonl', 'w')
    for json in AF_list:
        json['countrycode'] = 'AF'
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/EU_{_file}.jsonl', 'w')
    for json in EU_list:
        json['countrycode'] = 'EU'
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/AS_{_file}.jsonl', 'w')
    for json in AS_list:
        json['countrycode'] = 'AS'
        file.write(f'{json}\n')
    file.close()
    file = open(f'./data/OA_{_file}.jsonl', 'w')
    for json in OA_list:
        json['countrycode'] = 'OA'
        file.write(f'{json}\n')
    file.close()

    print(f"Total {_file} doodles: " + str(len(overall_list)) + "\n")

    print("North America total: \n" + str(len(NA_list)) + "\n")

    print("South American total: " + str(len(SA_list)) + "\n")

    print("Africa total: " + str(len(AF_list)) + "\n")

    print("Europe total: \n" + str(len(EU_list)) + "\n")

    print("Asia total: " + str(len(AS_list)) + "\n")

    print("Oceana/Australia total: " + str(len(OA_list)) + "\n")

    print("-"*20)


print('done :)')
