import numpy as np
import jsonlines as jl
from pprint import pprint
import itertools
import matplotlib.pyplot as plt

file_LIST = ['car', 'shoe', 'backpack', 'sun', 'power_outlet', 'bird']


for _file in file_LIST:
    npy_data = np.load(f'./new_data/{_file}/{_file}.npy')

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

    with jl.open(f"./new_data/{_file}/{_file}.ndjson") as reader:
        index = 0
        for obj in reader:
            d={}
            d['countrycode'] = obj['countrycode']
            d['drawing'] = npy_data[index]
            index += 1
            OVERALL_LIST.append(d)

    for i in OVERALL_LIST:
        if i['countrycode'] in NorthAmerica:
            NA_LIST.append(i['drawing'])
        elif i['countrycode'] in SouthAmerica:
            SA_LIST.append(i['drawing'])
            NON_NA_LIST.append(i['drawing'])
        elif i['countrycode'] in Africa:
            AF_LIST.append(i['drawing'])
            NON_NA_LIST.append(i['drawing'])
        elif i['countrycode'] in Europe:
            EU_LIST.append(i['drawing'])
            NON_NA_LIST.append(i['drawing'])
        elif i['countrycode'] in Asia:
            AS_LIST.append(i['drawing'])
            NON_NA_LIST.append(i['drawing'])
        elif i['countrycode'] in Oceana_Australia:
            OA_LIST.append(i['drawing'])
            NON_NA_LIST.append(i['drawing'])

    np.save(f'./new_data/{_file}/NA_{_file}.npy', np.array(NA_LIST))
    np.save(f'./new_data/{_file}/SA_{_file}.npy', np.array(SA_LIST))
    np.save(f'./new_data/{_file}/AF_{_file}.npy', np.array(AF_LIST))
    np.save(f'./new_data/{_file}/EU_{_file}.npy', np.array(EU_LIST))
    np.save(f'./new_data/{_file}/AS_{_file}.npy', np.array(AS_LIST))
    np.save(f'./new_data/{_file}/OA_{_file}.npy', np.array(OA_LIST))
    np.save(f'./new_data/{_file}/NON_NA_{_file}.npy', np.array(NON_NA_LIST))

    print(f'done with {_file}')
    print(f'Total: { len(OVERALL_LIST) }')
    print(f'NA Total: { len(NA_LIST) }')
    print(f'Non_NA Total: { len(NON_NA_LIST) }')

    plot_list = [len(NA_LIST), len(SA_LIST), len(AF_LIST), len(EU_LIST), len(AS_LIST), len(OA_LIST)]
    plt.bar(np.arange(6), plot_list)
    plt.xticks(np.arange(6), ('North America', 'South America', 'Africa', 'Europe', 'Asia', 'Oceania'))
    plt.ylabel('Total Doodles')
    plt.title(f'{_file}')
    plt.show()


    # print(f"Total {_file} doodles: " + str(len(OVERALL_LIST)) + "\n")
    #
    # print("North America total: \n" + str(len(NA_LIST)) + "\n")
    #
    # print("Non North America total: " + str(len(NON_NA_LIST)) + "\n")
    #
    # print("-"*20)


print('done :)')
