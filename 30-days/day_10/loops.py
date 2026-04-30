# --------------------------- EXERCISE LEVEL 1 ---------------------------------
# # Count 1 - 10
# count = 1
# while count < 11:
#     print(count)
#     count += 1

# # Count 10 - 1
# for item in range(10, 1, -1):
#     print(item)

# #
# ##
# ###
# ####
# #####         Expected output
# ######
# ####### 

# result = "#"
# while len(result) < 8:
#     print(result)
#     result += "#"

# # # # # # # # # 
# # # # # # # # # 
# # # # # # # # # 
# # # # # # # # #  
# # # # # # # # #  Expected Output
# # # # # # # # # 
# # # # # # # # # 
# # # # # # # # # 

# for col in range(8):
#     for row in range(8):
#         print("#", end=" ")
#     print("")

# # Iterate through the list
# python_list = ["Python", "Flask", "Django", "FASTAPI", "Panda"]
# for item in python_list:
#     print(item, end=" ")

# # 0 - 100 only print even numbers
# for num in range(0, 101):
#     if num % 2 == 0:
#         print(num)

# # 0 - 100 only print odd numbers
# for num in range(0, 101):
#     if num % 2 != 0:
#         print(num)

# --------------------------- EXERCISE LEVEL 2 ---------------------------------
# Print the sum of all numbers from 0 - 100
# number = 0
# for num in range(101):
#     number += num

# print("The total number:", number)

# even = 0
# odd = 0
# for num in range(101):
#     if num % 2 == 0:
#         even += num
#     elif num % 2 != 0:
#         odd += num

# print("The total even:", even)
# print("The total odd:", odd)

# --------------------------- EXERCISE LEVEL 3 ---------------------------------
# Extract countries with "land" on it
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

land = []

for item in countries:
    if "land" in item:
        land.append(item)

print(land)

# Reverse the list
fruits = ["Banana", "Orange", "Grapes", "Tomato"]
reversed_fruits = []

for item in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[item])

print(reversed_fruits)

# Get the total number of languages in each country (without duplicates)
country = [
    {
        "name": "PH",
        "languages": [
            "Tagalog",
            "Bisaya"
        ]
    },
    {
        "name": "US",
        "languages": [
            "American",
            "Tagalog"
        ]
    }
]

languages = set()
for item in country:
    for lan in item["languages"]:
        languages.add(lan)
    
print("The total number of languages (without duplicates) is", len(languages))
    
    