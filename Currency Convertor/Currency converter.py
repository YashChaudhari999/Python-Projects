import requests

while True:
    # Function to get exchange rate from one currency to another
    def get_exchange_rate(from_currency, to_currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        exchange_rate = data["rates"][to_currency]
        return exchange_rate



    # Function to convert amount from one currency to another
    def convert_currency(amount, from_currency, to_currency):
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount


    # Function to print currency names
    def currencies():
        currency_names = ('United Arab Emirates dirham','Afghan afghani','Albanian lek','Armenian dram','Netherlands Antillean guilder','Angolan kwanza','Argentine peso','Australian dollar','Aruban florin','Azerbaijani manat','Bosnia and Herzegovina convertible mark','Barbados dollar','Bangladeshi taka','Bulgarian lev','Bahraini dinar','Burundian franc','Bermudian dollar','Brunei dollar','Boliviano','Bolivian Mvdol (funds code)','Brazilian real','Bahamian dollar','Bhutanese ngultrum','Botswana pula','Belarusian ruble','Belize dollar','Canadian dollar','Congolese franc','WIR euro (complementary currency)','Swiss franc','WIR franc (complementary currency)','Unidad de Fomento (funds code)','Chilean peso','Colombian peso','Unidad de Valor Real (UVR) (funds code)','Costa Rican colon','Cuban convertible peso','Cuban peso','Cape Verdean escudo','Czech koruna','Djiboutian franc','Danish krone','Dominican peso','Algerian dinar','Egyptian pound','Eritrean nakfa','Ethiopian birr','Euro','Fiji dollar','Falkland Islands pound','Pound sterling','Georgian lari','Ghanaian cedi','Gibraltar pound','Gambian dalasi','Guinean franc','Guatemalan quetzal','Guyanese dollar','Hong Kong dollar','Honduran lempira','Haitian gourde','Hungarian forint','Indonesian rupiah','Israeli new shekel','Indian rupee','Iraqi dinar','Iranian rial','Icelandic króna (plural: krónur)','Jamaican dollar','Jordanian dinar','Japanese yen','Kenyan shilling','Kyrgyzstani som','Cambodian riel','Comoro franc','North Korean won','South Korean won','Kuwaiti dinar','Cayman Islands dollar','Kazakhstani tenge','Lao kip','Lebanese pound','Sri Lankan rupee','Liberian dollar','Lesotho loti','Libyan dinar','Moroccan dirham','Moldovan leu','Malagasy ariary','Macedonian denar','Myanmar kyat','Mongolian tögrög','Macanese pataca','Mauritanian ouguiya','Mauritian rupee','Maldivian rufiyaa','Malawian kwacha','Mexican peso','Mexican Unidad de Inversion (UDI) (funds code)','Malaysian ringgit','ozambican metical','Namibian dollar','Nigerian naira','Nicaraguan córdoba','Norwegian krone','Nepalese rupee','New Zealand dollar','Omani rial','Panamanian balboa','Peruvian sol','Papua New Guinean kina','Philippine peso','Pakistani rupee','Polish złoty','Paraguayan guaraní','Qatari riyal','Romanian leu','Serbian dinar','Renminbi','Russian ruble','Rwandan franc','Saudi riyal','Solomon Islands dollar','Seychelles rupee','Sudanese pound','Swedish krona (plural: kronor)','Singapore dollar','Saint Helena pound','Sierra Leonean leone (new leone)','Sierra Leonean leone (old leone)','Somali shilling','Surinamese dollar','South Sudanese pound','São Tomé and Príncipe dobra','Salvadoran colón','Syrian pound','Swazi lilangeni','Thai baht','Tajikistani somoni','Turkmenistan manat','Tunisian dinar','Tongan paʻanga','Turkish lira','Trinidad and Tobago dollar','New Taiwan dollar','Tanzanian shilling','Ukrainian hryvnia','Ugandan shilling','United States dollar','United States dollar (next day) (funds code)','Uruguay Peso en Unidades Indexadas (URUIURUI) (funds code)','Uruguayan peso','Unidad previsional','Uzbekistan sum','Venezuelan digital bolívar','Venezuelan sovereign bolívar','Vietnamese đồng','Vanuatu vatu','Samoan tala','CFA franc BEAC','Silver (one troy ounce)','Gold (one troy ounce)','European Composite Unit (EURCO) (bond market unit)','European Monetary Unit (E.M.U.-6) (bond market unit)','European Unit of Account 9 (E.U.A.-9) (bond market unit)','European Unit of Account 17 (E.U.A.-17) (bond market unit)','East Caribbean dollar','Special drawing rights','CFA franc BCEAO','Palladium (one troy ounce)','CFP franc (franc Pacifique)','Platinum (one troy ounce)','SUCRE','ADB Unit of Account','Yemeni rial','South African rand','Zambian kwacha','Zimbabwean dollar (fifth)')

        for i in range(len(currency_names)):
            print(f"{i+1}. {currency_names[i]}")




    # Example usage


    print("Select Choice of 1st currency: ")
    currencies()
    ch1 = int(input("Enter the choice of 1st currency:"))

    amount = int(input("Enter the amount: "))

    print("Select choice of 2nd currency:")
    currencies()
    ch2 = int(input("Enter the choice of 2nd currency:"))

    currency_tu = (
    'null','AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD',
    'BND', 'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHE', 'CHF', 'CHW', 'CLF', 'CLP', 'COP',
    'COU', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP',
    'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK',
    'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL',
    'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD',
    'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'CNY',
    'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SVC', 'SYP',
    'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USN', 'UYI', 'UYU', 'UYW',
    'UZS', 'VED', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XBA', 'XBB', 'XBC', 'XBD', 'XCD', 'XDR', 'XOF', 'XPD',
    'XPF', 'XPT', 'XSU', 'XUA', 'YER', 'ZAR', 'ZMW', 'ZWL')



    from_currency = currency_tu[ch1]
    to_currency = currency_tu[ch2]
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    a = input()