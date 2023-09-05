olimlar = {
    'Abu Abdulloh':{'familiya':'ibn Ismoil',
                    'yil': 810,
                    'tjoy': 'Buxoro',
                    'yashagan':60},
    'Abdulla'     :{'familiya':'Qodiriy',
                    'yil':1894,
                    'tjoy':'Toshkent',
                    'yashagan':44 },
    'Erkin'        :{'familiya':'Vohidov',
                     'yil':1936,
                     'tjoy':'Fargona',
                     'yashagan':80 },
    'Alisher'      :{'familiya':'Navoiy',
                    'yil': 1441,
                    'tjoy': 'Hirot',
                    'yashagan':60}
}                  
for ism , info in olimlar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['yil']}-yilda {info['tjoy']}da tug'ilgan."
          f"{info['yashagan']}yil umr ko'rgan")
    