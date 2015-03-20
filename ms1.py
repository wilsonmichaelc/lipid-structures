import itertools

f=open('ms1.csv', 'w')

# Core of the Lipid -- ??
_backbone = [340.1482]

# Loose ends
_one = [0, 79.9663, 143.9377, 161.0688353, 241.0351387, 321.0014353, 162.0528353, 242.0191353, 321.9854353, 131.0582432, 211.0245353, 290.9909353, 123.0085353, 202.9748353]
_fourPrime = [0, 79.9663, 143.9377, 161.0688353, 241.0351387, 321.0014353, 162.0528353, 242.0191353, 321.9854353, 131.0582432, 211.0245353, 290.9909353, 123.0085353, 202.9748353]

_two = [0, 170.1306, 198.1619, 226.1932, 254.2245, 282.2558, 310.2871, 338.3184]
_twoB = [0, 154.1357652, 182.1670653, 210.1983655, 238.2296656, 266.2609657, 294.2922658]

_three = [0, 170.1306, 198.1619, 226.1932, 254.2245, 282.2558, 310.2871, 338.3184]
_threeB = [0, 154.1357652, 182.1670653, 210.1983655, 238.2296656, 266.2609657, 294.2922658]

_twoPrime = [0, 170.1306, 198.1619, 226.1932, 254.2245, 282.2558, 310.2871, 338.3184]
_twoPrimeB = [0, 154.1358, 182.1671, 210.1984, 238.2297, 266.2610, 294.2923]

_threePrime = [0, 170.1306, 198.1619, 226.1932, 254.2245, 282.2558, 310.2871, 338.3184, 208.1827]
_threePrimeB = [0, 154.1358, 182.1671, 210.1984, 238.2297, 266.2610, 294.2923]


f.write('Backbone, One, Two, TwoB, Three, ThreeB, TwoPrime, TwoPrimeB, ThreePrime, ThreePrimeB, FourPrime, Total\n')

for backbone, one, fourPrime, two, twoB, three, threeB, twoPrime, twoPrimeB, threePrime, threePrimeB in itertools.product(_backbone, _one, _fourPrime, _two, _twoB, _three, _threeB, _twoPrime, _twoPrimeB, _threePrime, _threePrimeB):
	#print onepp, op, dp, threep, threepp, twobp, threebpp, twobp
	total = backbone + one + fourPrime + two + twoB + three + threeB + twoPrime + twoPrimeB + threePrime + threePrimeB - 1.0078
	f.write("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % (backbone, one, fourPrime, two, twoB, three, threeB, twoPrime, twoPrimeB, threePrime, threePrimeB, total))
f.close()