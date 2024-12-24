import json


str = '''{

    "Size & Fit": "5' 6",

    "Manufactured & Marketed By": {

        "Company Name": "FABINDIA LIMITED.",

        "Address": "Plot No. 10, Local Shopping Complex, Sector B, Pocket-7, Vasant Kunj, New Delhi- 110070",

        "Phone": "011-40692000",

        "Email": "mailus@fabindia.net"

    },

    "Care InstruCTIONS ": "Dry Clean Only",

    "Country Of Origin": "India",

    "Dimensions":"6.4M X1.16M (inclusive of blouse piece)", 

    "Material": "Silk"

}'''


print(json.loads(str))