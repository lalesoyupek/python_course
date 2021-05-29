from datetime import date
import os


personeller = [
    {
        "first": "Caesar",
        "last": "Ferry",
        "email": "Caesar.Ferry@nasir.com",
        "address": "67473 Reinhold Burg",
        "created": "October 14, 2013",
        "balance": "$1,980.53"
    },
    {
        "first": "Lance",
        "last": "Jacobson",
        "email": "magentasquirrel03@gmail.com",
        "address": "690 Shanahan Flats",
        "created": "March 4, 2012",
        "balance": "$5,531.59"
    },
    {
        "first": "Alfonzo",
        "last": "Daugherty",
        "email": "Alfonzo.Daugherty@deondre.info",
        "address": "81474 Justice Mountain",
        "created": "September 28, 2015",
        "balance": "$8,301.21"
    },
    {
        "first": "Ewald",
        "last": "Schimmel",
        "email": "azureturtle76@gmail.com",
        "address": "474 Dooley Common",
        "created": "September 16, 2011",
        "balance": "$3,784.60"
    },
    {
        "first": "Nicholas",
        "last": "Mertz",
        "email": "Nicholas.Mertz@frieda.name",
        "address": "34790 Zander Village",
        "created": "June 28, 2019",
        "balance": "$295.95"
    },
    {
        "first": "Maxine",
        "last": "Carroll",
        "email": "Maxine.Carroll@zetta.name",
        "address": "628 Omer Rapids",
        "created": "September 5, 2018",
        "balance": "$7,546.46"
    },
    {
        "first": "Cleveland",
        "last": "Dooley",
        "email": "Cleveland.Dooley@adeline.name",
        "address": "059 Lynch Field",
        "created": "June 24, 2012",
        "balance": "$1,714.94"
    },
    {
        "first": "Hassie",
        "last": "Bednar",
        "email": "azureturtle30@gmail.com",
        "address": "404 Lemke Shore",
        "created": "November 18, 2020",
        "balance": "$5,441.40"
    },
    {
        "first": "Brianne",
        "last": "Schaefer",
        "email": "fuchsiaturtle60@gmail.com",
        "address": "58525 Javonte Mall",
        "created": "June 9, 2013",
        "balance": "$8,674.37"
    },
    {
        "first": "Sage",
        "last": "Gerhold",
        "email": "whitefrog15@gmail.com",
        "address": "0217 Braun Gardens",
        "created": "July 21, 2016",
        "balance": "$7,380.90"
    },
    {
        "first": "Mariela",
        "last": "Nikolaus",
        "email": "Mariela.Nikolaus@crystel.com",
        "address": "3061 Pearlie Land",
        "created": "January 20, 2014",
        "balance": "$4,866.15"
    },
    {
        "first": "Damon",
        "last": "Bechtelar",
        "email": "turquoiserabbit15@gmail.com",
        "address": "695 Bechtelar Summit",
        "created": "December 25, 2018",
        "balance": "$2,497.65"
    },
    {
        "first": "Noemi",
        "last": "Parker",
        "email": "fuchsiawolf25@gmail.com",
        "address": "6265 Brakus Crossing",
        "created": "February 15, 2019",
        "balance": "$3,814.50"
    },
    {
        "first": "Hugh",
        "last": "Abernathy",
        "email": "Hugh.Abernathy@german.biz",
        "address": "2011 Edmund Park",
        "created": "September 27, 2017",
        "balance": "$6,008.43"
    },
    {
        "first": "Franz",
        "last": "Hahn",
        "email": "plumwolf57@gmail.com",
        "address": "169 Maeve Passage",
        "created": "April 1, 2016",
        "balance": "$6,986.46"
    },
    {
        "first": "Lawson",
        "last": "Abernathy",
        "email": "Lawson.Abernathy@bartholome.org",
        "address": "415 Shanon Throughway",
        "created": "May 1, 2014",
        "balance": "$8,687.18"
    },
    {
        "first": "Litzy",
        "last": "Leuschke",
        "email": "Litzy.Leuschke@jaycee.info",
        "address": "2123 Graham Parkways",
        "created": "March 15, 2013",
        "balance": "$8,299.22"
    },
    {
        "first": "Linnie",
        "last": "Gulgowski",
        "email": "Linnie.Gulgowski@waldo.biz",
        "address": "9229 Milton Ways",
        "created": "January 18, 2020",
        "balance": "$3,686.52"
    },
    {
        "first": "Malachi",
        "last": "Pagac",
        "email": "Malachi.Pagac@marcelle.org",
        "address": "781 Schultz Springs",
        "created": "January 23, 2012",
        "balance": "$3,684.91"
    },
    {
        "first": "Jeanette",
        "last": "Kertzmann",
        "email": "Jeanette.Kertzmann@priscilla.com",
        "address": "848 Rebeca Stream",
        "created": "February 16, 2016",
        "balance": "$7,291.15"
    },
    {
        "first": "Raquel",
        "last": "Gusikowski",
        "email": "Raquel.Gusikowski@celestino.org",
        "address": "66942 Rylee Isle",
        "created": "January 13, 2019",
        "balance": "$8,608.54"
    },
    {
        "first": "Antonio",
        "last": "Harris",
        "email": "Antonio.Harris@maeve.net",
        "address": "2819 Brandyn Plains",
        "created": "January 31, 2014",
        "balance": "$5,552.86"
    },
    {
        "first": "Tillman",
        "last": "Collins",
        "email": "Tillman.Collins@garrick.org",
        "address": "3301 Dario Canyon",
        "created": "October 9, 2020",
        "balance": "$380.85"
    },
    {
        "first": "Krystel",
        "last": "Kuhn",
        "email": "Krystel.Kuhn@shanny.org",
        "address": "5273 Timmothy Estate",
        "created": "September 21, 2014",
        "balance": "$2,675.14"
    },
    {
        "first": "Ransom",
        "last": "Stoltenberg",
        "email": "Ransom.Stoltenberg@dax.name",
        "address": "1249 Lesley Fords",
        "created": "March 28, 2018",
        "balance": "$6,969.18"
    },
    {
        "first": "Eleonore",
        "last": "Erdman",
        "email": "violetsquirrel85@gmail.com",
        "address": "40014 Vita Extensions",
        "created": "October 6, 2019",
        "balance": "$9,846.97"
    },
    {
        "first": "Daisy",
        "last": "Ziemann",
        "email": "Daisy.Ziemann@benton.info",
        "address": "6498 Daniella Ports",
        "created": "August 18, 2013",
        "balance": "$2,651.59"
    },
    {
        "first": "Mckenzie",
        "last": "Altenwerth",
        "email": "pinkwolf05@gmail.com",
        "address": "92840 Altenwerth Street",
        "created": "October 9, 2011",
        "balance": "$669.33"
    },
    {
        "first": "Vickie",
        "last": "Marvin",
        "email": "blackrabbit27@gmail.com",
        "address": "763 Breitenberg Coves",
        "created": "January 25, 2018",
        "balance": "$2,314.07"
    },
    {
        "first": "Pattie",
        "last": "Gottlieb",
        "email": "Pattie.Gottlieb@melvina.net",
        "address": "7263 Eldon Islands",
        "created": "June 4, 2020",
        "balance": "$9,599.78"
    },
    {
        "first": "Giovanny",
        "last": "Gulgowski",
        "email": "maroongiraffe29@gmail.com",
        "address": "7121 Shanelle Gateway",
        "created": "December 18, 2012",
        "balance": "$1,500.88"
    },
    {
        "first": "Cheyenne",
        "last": "Parisian",
        "email": "turquoisesquirrel67@gmail.com",
        "address": "5067 Harry Estate",
        "created": "January 8, 2020",
        "balance": "$3,103.38"
    },
    {
        "first": "Hollis",
        "last": "Ondricka",
        "email": "Hollis.Ondricka@irving.info",
        "address": "3209 Haven Junctions",
        "created": "August 26, 2017",
        "balance": "$7,083.91"
    },
    {
        "first": "Jevon",
        "last": "Botsford",
        "email": "maroonsquirrel01@gmail.com",
        "address": "24045 Herzog Passage",
        "created": "September 20, 2014",
        "balance": "$3,688.87"
    },
    {
        "first": "Emmalee",
        "last": "Ward",
        "email": "Emmalee.Ward@mary.biz",
        "address": "6620 Linda Land",
        "created": "April 1, 2019",
        "balance": "$3,597.65"
    },
    {
        "first": "Erika",
        "last": "Ledner",
        "email": "greenrabbit10@gmail.com",
        "address": "8093 Adams Lights",
        "created": "November 5, 2018",
        "balance": "$2,853.74"
    },
    {
        "first": "Adolf",
        "last": "Bergnaum",
        "email": "Adolf.Bergnaum@summer.info",
        "address": "20721 Heathcote Place",
        "created": "May 1, 2020",
        "balance": "$874.30"
    },
    {
        "first": "Dillan",
        "last": "Wisozk",
        "email": "silverwolf82@gmail.com",
        "address": "99175 Matilde Burg",
        "created": "February 23, 2021",
        "balance": "$7,585.61"
    },
    {
        "first": "Joyce",
        "last": "Batz",
        "email": "tealrabbit39@gmail.com",
        "address": "643 McLaughlin Keys",
        "created": "November 23, 2011",
        "balance": "$7,458.25"
    },
    {
        "first": "Yazmin",
        "last": "Rempel",
        "email": "Yazmin.Rempel@jess.com",
        "address": "35086 Parisian Fort",
        "created": "November 23, 2019",
        "balance": "$9,471.47"
    },
    {
        "first": "Nyah",
        "last": "Larkin",
        "email": "redturtle72@gmail.com",
        "address": "075 Lane Drive",
        "created": "September 17, 2014",
        "balance": "$7,084.00"
    },
    {
        "first": "Garland",
        "last": "Heaney",
        "email": "indigoturtle44@gmail.com",
        "address": "308 Colten Turnpike",
        "created": "October 16, 2016",
        "balance": "$1,493.52"
    },
    {
        "first": "Doris",
        "last": "McLaughlin",
        "email": "Doris.McLaughlin@jaclyn.name",
        "address": "617 Helena Estates",
        "created": "June 13, 2018",
        "balance": "$6,531.60"
    },
    {
        "first": "Michaela",
        "last": "Rolfson",
        "email": "Michaela.Rolfson@armando.org",
        "address": "237 Cassin Park",
        "created": "May 11, 2014",
        "balance": "$410.47"
    },
    {
        "first": "Green",
        "last": "Conroy",
        "email": "Green.Conroy@alessandra.biz",
        "address": "516 Price Brook",
        "created": "April 9, 2012",
        "balance": "$5,380.51"
    },
    {
        "first": "Jaylan",
        "last": "Moen",
        "email": "Jaylan.Moen@amos.net",
        "address": "28119 Collier Crest",
        "created": "January 12, 2021",
        "balance": "$535.31"
    },
    {
        "first": "Emely",
        "last": "Emard",
        "email": "blackrabbit81@gmail.com",
        "address": "665 Neil Lodge",
        "created": "October 1, 2014",
        "balance": "$5,109.07"
    },
    {
        "first": "Lorna",
        "last": "Price",
        "email": "Lorna.Price@abagail.info",
        "address": "28288 Callie Burg",
        "created": "July 17, 2013",
        "balance": "$886.01"
    },
    {
        "first": "Kristina",
        "last": "Hagenes",
        "email": "Kristina.Hagenes@nikki.name",
        "address": "0390 Doyle Garden",
        "created": "August 18, 2012",
        "balance": "$4,914.61"
    },
    {
        "first": "Erica",
        "last": "Barrows",
        "email": "Erica.Barrows@mohammad.org",
        "address": "11207 Rutherford Center",
        "created": "August 19, 2017",
        "balance": "$6,980.55"
    },
    {
        "first": "Jeromy",
        "last": "Boyer",
        "email": "ivorysquirrel26@gmail.com",
        "address": "6619 Shanelle Camp",
        "created": "January 2, 2015",
        "balance": "$6,732.44"
    },
    {
        "first": "Hosea",
        "last": "Hintz",
        "email": "greengiraffe22@gmail.com",
        "address": "38512 Hackett Fields",
        "created": "September 29, 2013",
        "balance": "$534.91"
    },
    {
        "first": "Bessie",
        "last": "Skiles",
        "email": "tealwolf15@gmail.com",
        "address": "28841 Dwight Plains",
        "created": "February 12, 2017",
        "balance": "$860.40"
    },
    {
        "first": "Dean",
        "last": "Wuckert",
        "email": "plumfrog48@gmail.com",
        "address": "922 Eugenia Port",
        "created": "July 18, 2019",
        "balance": "$6,787.88"
    },
    {
        "first": "Isabel",
        "last": "Haley",
        "email": "Isabel.Haley@iliana.name",
        "address": "1494 Rory Land",
        "created": "February 5, 2014",
        "balance": "$1,494.12"
    },
    {
        "first": "Derek",
        "last": "White",
        "email": "Derek.White@kimberly.biz",
        "address": "646 Chelsey Isle",
        "created": "January 11, 2020",
        "balance": "$261.32"
    },
    {
        "first": "Citlalli",
        "last": "Kihn",
        "email": "indigosquirrel29@gmail.com",
        "address": "981 Abshire Forks",
        "created": "March 13, 2018",
        "balance": "$0.75"
    },
    {
        "first": "Samantha",
        "last": "Botsford",
        "email": "Samantha.Botsford@makenna.info",
        "address": "190 Mosciski Point",
        "created": "September 28, 2020",
        "balance": "$9,333.33"
    },
    {
        "first": "Berenice",
        "last": "Volkman",
        "email": "ivoryrabbit54@gmail.com",
        "address": "8101 Schiller Cove",
        "created": "March 30, 2015",
        "balance": "$4,653.26"
    },
    {
        "first": "Gudrun",
        "last": "Hackett",
        "email": "Gudrun.Hackett@claire.info",
        "address": "761 Doris Drive",
        "created": "November 13, 2012",
        "balance": "$7,899.51"
    },
    {
        "first": "Chad",
        "last": "Dickens",
        "email": "lavendersquirrel95@gmail.com",
        "address": "2965 Murazik Divide",
        "created": "March 8, 2019",
        "balance": "$326.37"
    },
    {
        "first": "Philip",
        "last": "Gulgowski",
        "email": "silvergiraffe92@gmail.com",
        "address": "3864 Little Gateway",
        "created": "November 5, 2012",
        "balance": "$7,065.43"
    },
    {
        "first": "Claudia",
        "last": "Dicki",
        "email": "Claudia.Dicki@brock.net",
        "address": "7780 Howell Dale",
        "created": "February 3, 2015",
        "balance": "$6,789.46"
    },
    {
        "first": "Marcelino",
        "last": "Homenick",
        "email": "maroongiraffe45@gmail.com",
        "address": "50587 Lupe Fork",
        "created": "January 26, 2019",
        "balance": "$902.72"
    },
    {
        "first": "Peyton",
        "last": "McCullough",
        "email": "azuresquirrel64@gmail.com",
        "address": "917 Little Glens",
        "created": "March 31, 2018",
        "balance": "$8,130.35"
    },
    {
        "first": "Emery",
        "last": "Beahan",
        "email": "bluefrog97@gmail.com",
        "address": "924 Madie Dale",
        "created": "September 10, 2018",
        "balance": "$1,663.45"
    },
    {
        "first": "Elyse",
        "last": "Ritchie",
        "email": "orangerabbit48@gmail.com",
        "address": "4905 Considine Highway",
        "created": "January 29, 2017",
        "balance": "$6,517.47"
    },
    {
        "first": "Angela",
        "last": "Hane",
        "email": "olivewolf21@gmail.com",
        "address": "794 Conrad Land",
        "created": "February 25, 2013",
        "balance": "$4,860.33"
    },
    {
        "first": "Trycia",
        "last": "Considine",
        "email": "Trycia.Considine@gage.name",
        "address": "1540 Gretchen Trail",
        "created": "October 17, 2014",
        "balance": "$8,469.15"
    },
    {
        "first": "Tod",
        "last": "Rolfson",
        "email": "Tod.Rolfson@nola.net",
        "address": "786 Ericka Pine",
        "created": "February 7, 2012",
        "balance": "$6,195.25"
    },
    {
        "first": "Izaiah",
        "last": "Schiller",
        "email": "Izaiah.Schiller@cortez.name",
        "address": "0742 Upton Lodge",
        "created": "July 7, 2015",
        "balance": "$1,729.34"
    },
    {
        "first": "Miracle",
        "last": "Johns",
        "email": "Miracle.Johns@dallin.name",
        "address": "8973 Freddie Crossroad",
        "created": "December 20, 2016",
        "balance": "$2,162.78"
    },
    {
        "first": "Emely",
        "last": "Roberts",
        "email": "Emely.Roberts@godfrey.net",
        "address": "12561 Sipes Ports",
        "created": "January 26, 2017",
        "balance": "$5,798.72"
    },
    {
        "first": "Frederik",
        "last": "Swaniawski",
        "email": "Frederik.Swaniawski@alison.net",
        "address": "5004 Marlene Valleys",
        "created": "September 21, 2016",
        "balance": "$6,476.79"
    },
    {
        "first": "Abel",
        "last": "Feeney",
        "email": "Abel.Feeney@karson.biz",
        "address": "432 Rohan Springs",
        "created": "June 11, 2013",
        "balance": "$49.64"
    }
]


# print(personeller[0])
# print(personeller[0]["email"])

from datetime import date

try:
    first = input("personel ismini giriniz: ")
    last = input("personel soyismini giriniz: ")
    email = input("personel email giriniz: ")
    address = input("personel adres giriniz: ")
    #created = 
    balance = input("personel maaş giriniz: ")
except Exception as ex:
    print(ex) 
else: 
    # personeller.append(first)
    # personeller.append(last)
    # personeller.append(email)
    # personeller.append(address)
    # personeller.append(balance)

    personeller.append({
        "first" : first,
        "last" : last,
        "email": email,
        "address" : address,
        "created" : date.today().strftime('%B %d,%Y'),
        "balance" : balance
    })

print(personeller[len(personeller)-1])

###################################################

    # ,{
    #     "first": "Abel",
    #     "last": "Feeney",
    #     "email": "Abel.Feeney@karson.biz",
    #     "address": "432 Rohan Springs",
    #     "created": "June 11, 2013",
    #     "balance": "$49.64",
    #     "phones": [
    #         {
    #             "key": "Cell Phone",
    #             "value": "+90123457349",
    #             "description": "my cell phone"
    #         },
    #         {
    #             "key": "Home Phone",
    #             "value": "+90123457349",
    #             "description": "my home phone"
    #         },
    #     ]
    # }
]
 
 
# print(personeller[0])
# print(personeller[0]["email"])
# print(personeller[len(personeller) - 1])
# print(personeller[len(personeller) - 1]["phones"][0]["key"])
# print(personeller[len(personeller) - 1]["phones"][0])


# Dışarıdan aldığınız değerlere göre, yeni bir personel ekleyiniz.

os.system('cls')

_first = input("Lütfen adınızı giriniz : ")
_last = input("Lütfen soyadınızı giriniz : ")
_email = input("Lütfen mail adresinizi giriniz : ")
_address = input("Lütfen adresinizi giriniz : ")
_balance = input("Lütfen bakiye giriniz : ")
# _create = date.today().strftime('%d/%m/%Y')
_create = date.today().strftime('%B %d, %Y')


personeller.append({
    "first": _first,
    "last": _last,
    "email": _email,
    "address": _address,
    "created": _create,
    "balance": _balance
})

print(personeller[len(personeller) - 1])
