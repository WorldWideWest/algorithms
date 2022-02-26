array = [1320, 1503, 2067, 1116, 533, 1400, 2608, 2020, 2179, 2432, 1125, 2250, 2376, 242, 1353, 1456, 1316, 2005, 1445, 1031, 1536, 1094, 435, 991, 2143, 2161, 1385, 716, 589, 2796, 2210, 2289, 198, 2457, 283, 2867, 2955, 1268, 335, 509, 2303, 2146, 2166, 1329, 589, 1132, 581, 691, 2958, 2132, 1814, 1774, 2122, 2503, 2558, 2645, 592, 386, 538, 178, 710, 194, 2004, 431, 2199, 1088, 2450, 697, 1451, 101, 2564, 2838, 2464, 2500, 0, 1738, 448, 1543, 2054, 1242, 505, 238, 678, 1310, 2504, 221, 1898, 591, 997, 1844, 911, 2658, 2660, 2759, 1925, 2565, 669, 2346, 1366, 2489, 894, 1699, 1594, 771, 2224, 823, 775, 2843, 1603, 595, 1217, 1565, 910, 289, 333, 2190, 904, 355, 514, 276, 1579, 1410, 2997, 967, 1141, 1507, 764, 754, 1287, 2775, 2766, 1969, 1610, 1887, 1419, 1637, 1793, 2092, 244, 1062, 2518, 2201, 791, 2918, 895, 2374, 1095, 2941, 2578, 1912, 1735, 911, 316, 1257, 2908, 722, 859, 1082, 885, 1567, 2749, 474, 769, 2265, 1687, 718, 22, 2778, 549, 2025, 2606, 2068, 2044, 1293, 334, 334, 2567, 1906, 960, 1256, 1180, 676, 1435, 1678, 2411, 1740, 1671, 2182, 2713, 707, 913, 2615, 2611, 675, 2382, 1531, 350, 432, 2961, 1580, 2930, 828, 717, 557, 2954, 1570, 2461, 1421, 1910, 2286, 208, 153, 1350, 2815, 2416, 1806, 2195, 1250, 2175, 2303, 2994, 2125, 10, 2536, 846, 447, 2820, 1519, 488, 1547, 1324, 734, 885, 1622, 769, 1573, 2748, 862, 275, 2716, 2874, 1051, 458, 1095, 2830, 488, 2190, 1793, 1266, 650, 2377, 1901, 1870, 718, 976, 2489, 797, 341, 2236, 342, 643, 627, 2385, 2767, 161, 1693, 1818, 2063, 144, 291, 1958, 715, 2043, 2861, 2734, 6, 1770, 1961, 1323, 2954, 810, 2300, 1090, 656, 1481, 2184, 2571, 1458, 78, 1942, 944, 306, 195, 1081, 2339, 80, 1922, 1501, 125, 1161]

### PSEUDO CODE ###

# for i in range(1, array:length)
#   j = i
#   while j > 0  and  array[j - 1] > array[j]
#       swap array[j - 1], array[j]
#       j -= 1


def sort(array:list) -> list:

    for i in range(1, len(array)):

        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array

print(sort(array))