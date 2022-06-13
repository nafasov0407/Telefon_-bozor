from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup


til = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "🇺🇿Uzbekcha",callback_data = "uz"),InlineKeyboardButton(text = "🇷🇺Ruscha",callback_data = "ru")
		],
	],
)

tur = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Ipone",callback_data = "ipone"),InlineKeyboardButton(text = "Samsung",callback_data = "samsung")
		],
		[
				InlineKeyboardButton(text = "Redmi",callback_data = "redmi"),InlineKeyboardButton(text = "Vivo",callback_data = "vivo")
		],
		
	],
)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""IPONE"""""""'"""""""""""""""""""""""""""""""""""""""""'

ipon_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Ipone pro max",callback_data = "max")
		],
		[
				InlineKeyboardButton(text = "ipone pro",callback_data = "ort")
		],
		[
				InlineKeyboardButton(text = "ipone",callback_data = "kich")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad1")
		],
		
	],
)



promax_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "IPONE 13 PRO MAX",callback_data = "max13"),InlineKeyboardButton(text = "IPONE 12 PRO MAX",callback_data = "max12")
		],
		[
				InlineKeyboardButton(text = "IPONE 11 PRO MAX",callback_data = "max11"),InlineKeyboardButton(text = "IPONE XS MAX",callback_data = "maxs")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad2")
		],
		
	],
)

pro_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "IPONE 13 PRO",callback_data = "pro13"),InlineKeyboardButton(text = "IPONE 12 PRO",callback_data = "pro12")
		],
		[
				InlineKeyboardButton(text = "IPONE 11 PRO",callback_data = "pro11"),InlineKeyboardButton(text = "IPONE XS",callback_data = "proxs")
		],
		[
				InlineKeyboardButton(text = "IPONE XR",callback_data = "proxr")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad3")
		],
		
	],
)


min_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "IPONE 13",callback_data = "min13"),InlineKeyboardButton(text = "IPONE 12",callback_data = "min12")
		],
		[
				InlineKeyboardButton(text = "IPONE 11",callback_data = "min11"),InlineKeyboardButton(text = "IPONE X",callback_data = "minx")
		],
		[
				InlineKeyboardButton(text = "IPONE 8+",callback_data = "min8+"),InlineKeyboardButton(text = "IPONE 8",callback_data = "min8")
		],
		[
				InlineKeyboardButton(text = "IPONE 7+",callback_data = "min7+"),InlineKeyboardButton(text = "IPONE 7",callback_data = "min7")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad4")
		],
		
	],
)

#"""""""""""""""""""""""""""""""""""""""""""""""SAMSUNG"""""""""""""""""""""""""""""""""""""""""""""""""

sam_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Samsung galaxy s",callback_data = "s"),InlineKeyboardButton(text = "Samsung galaxy not",callback_data = "not")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy a",callback_data = "a"),InlineKeyboardButton(text = "Samsung galaxy z",callback_data = "z")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad5")
		],
		
	],
)

s_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Samsung galaxy S22 ULTRA",callback_data = "s22u"),InlineKeyboardButton(text = "Samsung galaxy S21 FE 5G",callback_data = "s21f")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy S20 FE",callback_data = "s20f"),InlineKeyboardButton(text = "Samsung galaxy S21 ULTRA 5G",callback_data = "s21u")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy S21+5G",callback_data = "s21+"),InlineKeyboardButton(text = "Samsung galaxy S21 5G",callback_data = "sam21")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy S20 ULTRA",callback_data = "s20u")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy S20",callback_data = "s20+"),InlineKeyboardButton(text = "Samsung galaxy S10",callback_data = "sam10")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad6")
		],
		
	],
)

not_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Samsung galaxy not 20 ULTRA",callback_data = "not20u"),InlineKeyboardButton(text = "Samsung galaxy not 20",callback_data = "not20")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy not 10",callback_data = "not10"),InlineKeyboardButton(text = "Samsung galaxy not 10+",callback_data = "not10+")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad7")
		],
		
	],
)

z_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Samsung galaxy Z fold3 5G",callback_data = "zfold3"),InlineKeyboardButton(text = "Samsung galaxy Z Flip3 5G",callback_data = "zflip3")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy Z Fold2",callback_data = "zfold"),InlineKeyboardButton(text = "Samsung galaxy Z Flip",callback_data = "zflip")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad8")
		],
		
	],
)


a_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Samsung galaxy A73 5G",callback_data = "a73"),InlineKeyboardButton(text = "Samsung galaxy A53 5G",callback_data = "a53")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy A33 5G",callback_data = "a33"),InlineKeyboardButton(text = "Samsung galaxy A22 5G",callback_data = "a22")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy A23",callback_data = "a23"),InlineKeyboardButton(text = "Samsung galaxy A13",callback_data = "a13")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy A72",callback_data = "a72"),InlineKeyboardButton(text = "Samsung galaxy A52",callback_data = "a52")
		],
		[
				InlineKeyboardButton(text = "Samsung galaxy A32 5G",callback_data = "a32"),InlineKeyboardButton(text = "Samsung galaxy A03s",callback_data = "a03")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad9")
		],
		
	],
)


# """""""""""""""""""""""""""""""""""""""""""""""REDMI"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

red_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Xiomi Mi 11",callback_data = "m11"),InlineKeyboardButton(text = "Xiomi Mi 10T Pro",callback_data = "m10")
		],
		[
				InlineKeyboardButton(text = "Xiomi Poco F3",callback_data = "f3"),InlineKeyboardButton(text = "Xiomi Mi 10T",callback_data = "t10")
		],
		[
				InlineKeyboardButton(text = "Xiomi Redmi not 10",callback_data = "not10"),InlineKeyboardButton(text = "Xiomi redmi not 10 pro",callback_data = "n0t9")
		],
		[
				InlineKeyboardButton(text = "Xiomi Poco x3",callback_data = "x3"),InlineKeyboardButton(text = "Xiomi Redmi 9T",callback_data = "9t")
		],
		[
				InlineKeyboardButton(text = "Xiomi Redmi not 9 Pro",callback_data = "9pro"),InlineKeyboardButton(text = "Xiomi Redmi not 9",callback_data = "r9")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad10")
		],
		
	],
)


vivo_menu = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = "vivo x60",callback_data = "x60"),InlineKeyboardButton(text = "vivo x50",callback_data = "x50")
		],
		[
				InlineKeyboardButton(text = "vivo v21",callback_data = "v21"),InlineKeyboardButton(text = "vivo v20",callback_data = "v20")
		],
		[
				InlineKeyboardButton(text = "vivo y30",callback_data = "y30"),InlineKeyboardButton(text = "vivo y20",callback_data = "y20")
		],
		[
				InlineKeyboardButton(text = "vivo y19",callback_data = "y19"),InlineKeyboardButton(text = "vivo y12s",callback_data = "y12s")
		],
		[
				InlineKeyboardButton(text = "Orqaga",callback_data = "nazad11")
		],
		
	],
)
# ipone
back = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "1Tb",callback_data = "a1"),InlineKeyboardButton(text = "512Gb",callback_data = "a2")
		],
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "a3"),InlineKeyboardButton(text = "128Gb",callback_data = "a4")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "nazad12")
		],
	],

)

back100 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "512Gb",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "a7"),InlineKeyboardButton(text = "128Gb",callback_data = "a8")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "orqa1")
		],
	],

)

back101 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "512Gb",callback_data = "a9"),InlineKeyboardButton(text = "256Gb",callback_data = "a10")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "a11"),InlineKeyboardButton(text = "64Gb",callback_data = "a12")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "orqa2")
		],
	],

)

back102 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "512Gb",callback_data = "a17"),InlineKeyboardButton(text = "256Gb",callback_data = "a18")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "a19"),InlineKeyboardButton(text = "64Gb",callback_data = "a20")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "orqa3")
		],
	],

)

iphone_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'r1'),InlineKeyboardButton(text = 'Silver',callback_data = 'r2')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'r3'),InlineKeyboardButton(text = 'Gray',callback_data = 'r4')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad21')
		],
	]

)

iphone_rangi1 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'r5'),InlineKeyboardButton(text = 'Silver',callback_data = 'r6')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'r7'),InlineKeyboardButton(text = 'Gray',callback_data = 'r8')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad22')
		],
	]

)

iphone_rangi2 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'r9'),InlineKeyboardButton(text = 'Silver',callback_data = 'r10')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'r11'),InlineKeyboardButton(text = 'Gray',callback_data = 'r12')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad23')
		],
	]

)
iphone_rangi3 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'r13'),InlineKeyboardButton(text = 'Silver',callback_data = 'r14')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'r15'),InlineKeyboardButton(text = 'Gray',callback_data = 'r16')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad24')
		],
	]

)

# iphone pro uchun"""""""""""""""""""""""""''''

back4 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1Tb",callback_data = "b1"),InlineKeyboardButton(text = "512Gb",callback_data = "b2")
		],
		[
			InlineKeyboardButton(text = "256Gb",callback_data = "b3"),InlineKeyboardButton(text = "128Gb",callback_data = "b4")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa4")
		],
	],

)


back400 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "512Gb",callback_data = "b5")
		],
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "b6"),InlineKeyboardButton(text = "128Gb",callback_data = "b7")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "orqa5")
		],
	],

)

back401 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "512Gb",callback_data = "b8"),InlineKeyboardButton(text = "256Gb",callback_data = "b9")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "b10"),InlineKeyboardButton(text = "64Gb",callback_data = "b11")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "orqa6")
		],
	],

)

back402 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "512Gb",callback_data = "b12"),InlineKeyboardButton(text = "256Gb",callback_data = "b13")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "b14"),InlineKeyboardButton(text = "64Gb",callback_data = "b15")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "orqa7")
		],
	],

)

back403 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "b17")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "b18"),InlineKeyboardButton(text = "64Gb",callback_data = "b19")
		],
		[
				InlineKeyboardButton(text = "orqaga",callback_data = "orqa8")
		],
	],

)


# iphone pro rangi""""""""""""""""""""""""""""""""""""""
iphone_rangi4 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'c1'),InlineKeyboardButton(text = 'Silver',callback_data = 'c2')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'c3'),InlineKeyboardButton(text = 'Gray',callback_data = 'c4')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad25')
		],
	]

)


iphone_rangi5 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'c5'),InlineKeyboardButton(text = 'Silver',callback_data = 'c6')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'c7'),InlineKeyboardButton(text = 'Gray',callback_data = 'c8')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad26')
		],
	]

)


iphone_rangi6 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'c9'),InlineKeyboardButton(text = 'Silver',callback_data = 'c10')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'c11'),InlineKeyboardButton(text = 'Gray',callback_data = 'c12')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad27')
		],
	]

)


iphone_rangi7 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'c13'),InlineKeyboardButton(text = 'Silver',callback_data = 'c14')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'c15'),InlineKeyboardButton(text = 'Gray',callback_data = 'c16')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad28')
		],
	]

)

iphone_rangi8 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'c17'),InlineKeyboardButton(text = 'Silver',callback_data = 'c18')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'c19'),InlineKeyboardButton(text = 'Gray',callback_data = 'c20')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad29')
		],
	]

)

# IPHONE min  uchun""""""""""""""""""""""""""""""""""""""""""

back5 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "512Gb",callback_data = "d1")
		],
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d2"),InlineKeyboardButton(text = "128Gb",callback_data = "d3")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad17")
		],
	],

)


back500 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d4")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "d5"),InlineKeyboardButton(text = "64Gb",callback_data = "d6")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa9")
		],
	],

)

back501 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d7")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "d8"),InlineKeyboardButton(text = "64Gb",callback_data = "d9")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa10")
		],
	],

)


back502 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d10")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "d11"),InlineKeyboardButton(text = "64Gb",callback_data = "d12")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa11")
		],
	],

)

back503 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d13")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "d14"),InlineKeyboardButton(text = "64Gb",callback_data = "d15")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa12")
		],
	],

)


back504 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d16")
		],
		[
				InlineKeyboardButton(text = "128Gb",callback_data = "d17"),InlineKeyboardButton(text = "64Gb",callback_data = "d18")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa13")
		],
	],

)

back505 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d19"),InlineKeyboardButton(text = "128Gb",callback_data = "d20")
		],
		[
				InlineKeyboardButton(text = "64Gb",callback_data = "d21"),InlineKeyboardButton(text = "32Gb",callback_data = "d22")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa14")
		],
	],

)

back506 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "256Gb",callback_data = "d23"),InlineKeyboardButton(text = "128Gb",callback_data = "d24")
		],
		[
				InlineKeyboardButton(text = "64Gb",callback_data = "d25"),InlineKeyboardButton(text = "32Gb",callback_data = "d26")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "orqa15")
		],
	],

)
# IPONE min rangi """"""""""""""""""""""""""""""""""""""''
ihone_min_rangi1 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g1'),InlineKeyboardButton(text = 'Silver',callback_data = 'g2')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g3'),InlineKeyboardButton(text = 'Gray',callback_data = 'g4')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad30')
		],
	]

)

ihone_min_rangi2 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g5'),InlineKeyboardButton(text = 'Silver',callback_data = 'g6')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g7'),InlineKeyboardButton(text = 'Gray',callback_data = 'g8')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad31')
		],
	]
)

ihone_min_rangi3 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g9'),InlineKeyboardButton(text = 'Silver',callback_data = 'g10')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g11'),InlineKeyboardButton(text = 'Gray',callback_data = 'g12')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad32')
		],
	]
)

ihone_min_rangi4 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g13'),InlineKeyboardButton(text = 'Silver',callback_data = 'g14')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g15'),InlineKeyboardButton(text = 'Gray',callback_data = 'g16')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad33')
		],
	]
)

ihone_min_rangi5 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g17'),InlineKeyboardButton(text = 'Silver',callback_data = 'g18')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g19'),InlineKeyboardButton(text = 'Gray',callback_data = 'g20')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad34')
		],
	]
)

ihone_min_rangi6 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g21'),InlineKeyboardButton(text = 'Silver',callback_data = 'g22')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g23'),InlineKeyboardButton(text = 'Gray',callback_data = 'g24')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad35')
		],
	]
)

ihone_min_rangi7 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g25'),InlineKeyboardButton(text = 'Silver',callback_data = 'g26')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g27'),InlineKeyboardButton(text = 'Gray',callback_data = 'g28')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad36')
		],
	]
)

ihone_min_rangi8 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Gold',callback_data = 'g29'),InlineKeyboardButton(text = 'Silver',callback_data = 'g30')
		],
		[
				InlineKeyboardButton(text = 'Space',callback_data = 'g31'),InlineKeyboardButton(text = 'Gray',callback_data = 'g32')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad37')
		],
	]
)
# samsung xotira uchun """"""""""""""""""""""""""""""""""""""""""""""
sam_back1 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "12/512Gb",callback_data = "s1")
		],
		[
				InlineKeyboardButton(text = "12/256Gb",callback_data = "s2"),InlineKeyboardButton(text = "8/128Gb",callback_data = "s3")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad13")
		],
	],

)

sam_back2 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/256Gb",callback_data = "s4"),InlineKeyboardButton(text = "6/128Gb",callback_data = "s5")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad38")
		],
	],

)

sam_back3 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/128Gb",callback_data = "s6"),InlineKeyboardButton(text = "6/128Gb",callback_data = "s7")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad39")
		],
	],

)

sam_back4 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "12/256Gb",callback_data = "s8"),InlineKeyboardButton(text = "12/128Gb",callback_data = "s9")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad40")
		],
	],

)

sam_back5 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/256Gb",callback_data = "s10"),InlineKeyboardButton(text = "8/128Gb",callback_data = "s11")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad41")
		],
	],

)

sam_back6 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/256Gb",callback_data = "s12"),InlineKeyboardButton(text = "8/128Gb",callback_data = "s13")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad42")
		],
	],

)


sam_back8 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/128Gb",callback_data = "s14")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad44")
		],
	],

)

sam_back9 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/128Gb",callback_data = "s15")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad45")
		],
	],

)

sam_back10 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/128Gb",callback_data = "s16")
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad46")
		],
	],

)
# samsung s ranglari >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

s22ultra_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'black',callback_data = 'e1'),InlineKeyboardButton(text = 'green',callback_data = 'e2')
		],
		[
				InlineKeyboardButton(text = 'burgundy',callback_data = 'e3'),InlineKeyboardButton(text = 'white',callback_data = 'e4')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad47')
		],
	]
)

s21fe_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'olive',callback_data = 'e5'),InlineKeyboardButton(text = 'gray',callback_data = 'e6')
		],
		[
				InlineKeyboardButton(text = 'purple',callback_data = 'e7'),InlineKeyboardButton(text = 'white',callback_data = 'e8')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad48')
		],
	]
)


s20fe_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'blue',callback_data = 'e9'),InlineKeyboardButton(text = 'mint',callback_data = 'e10')
		],
		[
				InlineKeyboardButton(text = 'red',callback_data = 'e11'),InlineKeyboardButton(text = 'lavender',callback_data = 'e12')
		],
		[
				InlineKeyboardButton(text = 'white',callback_data = 'e13')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad49')
		],
	]
)

s21ultra_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'black',callback_data = 'e14'),InlineKeyboardButton(text = 'silver',callback_data = 'e15')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad50')
		],
	]
)

s21plusG_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'black',callback_data = 'e16'),InlineKeyboardButton(text = 'silver',callback_data = 'e17')
		],
		[
				InlineKeyboardButton(text = 'purple',callback_data = 'e18')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad51')
		],
	]
)

s21g_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'purple',callback_data = 'e19'),InlineKeyboardButton(text = 'gray',callback_data = 'e20')
		],
		[
				InlineKeyboardButton(text = 'white',callback_data = 'e21'),InlineKeyboardButton(text = 'pink',callback_data = 'e22')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad52')
		],
	]
)

s20ultra_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'gray',callback_data = 'e23'),InlineKeyboardButton(text = 'black',callback_data = 'e24')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad53')
		],
	]
)

s20plus_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'gray',callback_data = 'e25'),InlineKeyboardButton(text = 'blue',callback_data = 'e26')
		],
		[
				InlineKeyboardButton(text = 'red',callback_data = 'e27')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad54')
		],
	]
)

s10_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'black',callback_data = 'e28'),InlineKeyboardButton(text = 'white',callback_data = 'e29')
		],
		[
				InlineKeyboardButton(text = 'blue',callback_data = 'e30'),InlineKeyboardButton(text = 'green',callback_data = 'e31')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad55')
		],
	]
)

samnot_back1 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "12/256Gb",callback_data = "s17"),InlineKeyboardButton(text = "12/128Gb",callback_data = "s18")
		],
		[
				InlineKeyboardButton(text = "8/256Gb",callback_data = "s19")	
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad56")
		],
	],

)

samnot_back2 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "12/256Gb",callback_data = "s20"),InlineKeyboardButton(text = "8/256Gb",callback_data = "s21")
		],	
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad57")
		],
	],

)

samnot_back3 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/256Gb",callback_data = "s22")
		],	
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad58")
		],
	],

)


samnot_back4 = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = "8/256Gb",callback_data = "s23")
		],	
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad59")
		],
	],

)


# samnot ranglari >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

not20_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'bronze',callback_data = 'f1')
		],
		[
				InlineKeyboardButton(text = 'graphite',callback_data = 'f2'),InlineKeyboardButton(text = 'mint',callback_data = 'f3')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad60')
		],
	]
)

not20ultra_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'bronze',callback_data = 'f4')
		],
		[
				InlineKeyboardButton(text = 'black',callback_data = 'f5'),InlineKeyboardButton(text = 'white',callback_data = 'f6')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad61')
		],
	]
)


not10_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'black',callback_data = 'f7')
		],
		[
				InlineKeyboardButton(text = 'aura',callback_data = 'f8'),InlineKeyboardButton(text = 'red',callback_data = 'f9')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad62')
		],
	]
)

not10plus_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'black',callback_data = 'f10')
		],
		[
				InlineKeyboardButton(text = 'aura',callback_data = 'f11'),InlineKeyboardButton(text = 'white',callback_data = 'f12')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad63')
		],
	]
)

zfold3_back = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = '12/512Gb',callback_data = 's24'),InlineKeyboardButton(text = '12/256Gb',callback_data = 's25')
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad64")
		],
	],

)

zflip3_back = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = '8/256Gb',callback_data = 's26'),InlineKeyboardButton(text = '8/256Gb',callback_data = 's25')
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad65")
		],
	],

)

zfold2_back = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = '8/256Gb',callback_data = 's28')
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad66")
		],
	],

)

zflip_back = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = '8/256Gb',callback_data = 's29')
		],
		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad71")
		],
	],

)

zfold3_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'black',callback_data = 'f13')
		],
		[
				InlineKeyboardButton(text = 'green',callback_data = 'f14'),InlineKeyboardButton(text = 'silver',callback_data = 'f15')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad67')
		],
	]
)


zflip3_rangi = InlineKeyboardMarkup(

	inline_keyboard = [

		[
				InlineKeyboardButton(text = 'Beige',callback_data = 'f16'),InlineKeyboardButton(text = 'black',callback_data = 'f17')
		],
		[
				InlineKeyboardButton(text = 'green',callback_data = 'f18'),InlineKeyboardButton(text = 'Violet',callback_data = 'f19')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad68')
		],
	]
)

zfold2_rangi = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = 'black',callback_data = 'f20'),InlineKeyboardButton(text = 'bronze',callback_data = 'f21')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad69')
		],
	]
)

zflip_rangi = InlineKeyboardMarkup(

	inline_keyboard = [
		[
				InlineKeyboardButton(text = 'black',callback_data = 'f22'),InlineKeyboardButton(text = 'purple',callback_data = 'f23')
		],
		[
				InlineKeyboardButton(text = 'orqaga',callback_data = 'nazad70')
		],
	]
)


back8 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad20")
		],
	],

)

back2 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad14")
		],
	],

)

back3 = InlineKeyboardMarkup(

	inline_keyboard = [

		[
			InlineKeyboardButton(text = "orqaga",callback_data = "nazad15")
		],
	],

)