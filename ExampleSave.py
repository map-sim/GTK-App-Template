#!/usr/bin/python3


example_library = {
    "terrains": {
        "steppe-0": {
            "desc": "flat steppe",
            "color": (1, 0.95, 0.8),
            "cover-level": 0,
            "water-level": 0,
            "land-level": 0
        },
        "highland-1": {
            "desc": "flat highland",
            "color": (1, 0.9, 0.75),
            "cover-level": 0,
            "water-level": 0,
            "land-level": 1
        },
        "highland-2": {
            "desc": "flat highland",
            "color": (1, 0.85, 0.7),
            "cover-level": 0,
            "water-level": 0,
            "land-level": 2
        },
        "forest-0": {
            "desc": "flat forest",
            "color": (0.7, 0.95, 0.85),
            "cover-level": 2,
            "water-level": 0,
            "land-level": 0
        },
        "water-0": {
            "desc": "shallow water",
            "color": (0.5, 0.85, 1.0),
            "cover-level": 0,
            "water-level": 1,
            "land-level": 0           
        },
        "water-1": {
            "desc": "shallow water",
            "color": (0.45, 0.8, 0.95),
            "cover-level": 0,
            "water-level": 2,
            "land-level": 0           
        }
    },
    "infrastructure": {
        "building-0": {
            "desc": "small building",
            "color": (0.3, 0.3, 0.3),
            "size": (100, 100),
            "construction": 100,
            "cover-level": 1,
        },
        "fortress-0": {
            "desc": "small fortress",
            "color": (0.3, 0.3, 0.3),
            "size": (100, 100),
            "construction": 200,
            "cover-level": 1,
        },
        "bridge-0": {
            "desc": "small bridge",
            "color": (0.3, 0.3, 0.3),
            "size": (120, 60),
            "construction": 30,
            "cover-level": 0,
        },
        "bridge-1": {
            "desc": "small bridge",
            "color": (0.3, 0.3, 0.3),
            "size": (60, 120),
            "construction": 30,
            "cover-level": 0,
        },
        "route-0": {
            "desc": "small route",
            "color": (0.3, 0.3, 0.3),
            "size": (28, 200),
            "construction": 10,
            "cover-level": 0,
        },
        "route-1": {
            "desc": "small route",
            "color": (0.3, 0.3, 0.3),
            "size": (200, 28),
            "construction": 10,
            "cover-level": 0,
        },
        "route-2": {
            "desc": "small route",
            "color": (0.3, 0.3, 0.3),
            "size": (200, 28),
            "construction": 10,
            "cover-level": 0,
        },
        "route-3": {
            "desc": "small route",
            "color": (0.3, 0.3, 0.3),
            "size": (200, 28),
            "construction": 10,
            "cover-level": 0,
        },
        "seeport-0": {
            "desc": "small see port",
            "color": (0.3, 0.3, 0.3),
            "size": (150, 150),
            "construction": 100,
            "cover-level": 10,
        }
    },
}

example_config = {
    "window-title": "navi window",
    "window-size": (1600, 1000),
    "window-offset": (200, 100),
    "window-zoom": 0.5,
    "move-sensitive": 50,
    "battle-field": {
        "infrastructure": [
            ("building-0", 1618, 810),
            ("building-0", 1618, 905),
            ("building-0", 1570, 1005),
            ("building-0", 1670, 1005),
            ("building-0", 1620, 1105),
            ("building-0", 1720, 1105),

            ("route-2", -1890, -300),
            ("route-2", -2031, -441),
            ("route-2", -2172, -582),
            ("route-2", -2313, -723),
            ("route-0", -2313, -923),
            ("route-0", -2313, -1123),
            ("route-0", -2313, -1323),
            ("route-0", -2313, -1523),
            ("building-0", -2363, -1623),

            
            
            ("building-0", 550, 1100),
            ("building-0", 550, 1000),
            ("building-0", -1750, -200),

            ("fortress-0", 50, 625),
            ("fortress-0", 150, 575),
            ("fortress-0", -550, 450),
            
            ("bridge-0", 650, 1030),
            ("bridge-1", -1725, 100),
            ("bridge-1", -1725, 220),

            ("route-0", -1695, -100),
            ("route-0", -1695, 340),
            ("route-0", -1695, 540),
            
            ("route-1", 770, 1060),
            ("route-1", 970, 1060),
            ("route-1", 1170, 1060),
            ("route-1", 1370, 1060),
            
            ("route-2", -1695, 740),
            ("route-2", -1551, 883),
            ("route-0", -1410, 1028),
            ("route-0", -1410, 1228),
            ("route-2", -1410, 1428),
            ("route-2", -1267, 1571),
            ("route-2", -1124, 1712),
            ("route-2", -983, 1855),
            ("route-0", -841, 1999),
            ("route-0", -841, 2199),
            
            ("route-1", -1410, 1027),
            ("route-1", -1215, 1027),
            ("route-1", -1020, 1027),
            ("route-1", -825, 1027),
            ("route-1", -630, 1027),
            ("route-1", -435, 1027),
            ("route-1", -240, 1027),
            ("route-1", -45, 1027),
            ("route-1", 150, 1027),
            ("route-1", 345, 1027),

            ("route-0", 600, 1200),
            ("route-0", 600, 1400),
            ("route-3", 600, 1600),
            ("route-0", 457, 1741),
            ("route-0", 457, 1941),
            ("route-0", 457, 2141),
            ("route-0", 457, 2341),
            ("route-0", 457, 2541),
            ("route-3", 457, 2741),
            ("route-0", 316, 2881),
            ("route-0", 316, 3081),
            ("route-0", 316, 3281),
            ("route-0", 316, 3481),

            ("building-0", -908, 2399),
            ("building-0", -908, 2499),
            ("building-0", -1008, 2450),
            ("route-1", -1208, 2490),
            ("route-1", -1408, 2490),
            ("route-1", -1608, 2490),
            ("route-1", -1808, 2490),
            ("route-1", -2008, 2490),
            ("route-1", -2208, 2490),
            ("route-1", -2408, 2490),
            ("route-1", -2608, 2490),
            ("route-3", -2608, 2490),
            ("route-1", -2949, 2631),
            ("route-1", -3149, 2631),
            ("building-0", -3249, 2591),
            
            ("route-1", -810, 2430),
            ("route-1", -610, 2430),
            ("route-1", -410, 2430),

            ("building-0", -210, 2380),

            ("route-2", 175, 2740),
            ("route-2", 32, 2597),
            ("route-2", -110, 2456),

            ("building-0", 240, 3680),
            ("building-0", 340, 3680),
            ("building-0", 290, 3780),

            ("seeport-0", 3950, 1100),
            ("seeport-0", 3950, 1250),
            ("building-0", 3850, 1285),

            ("route-1", 1770, 1050),
            ("route-1", 1970, 1050),
            ("route-1", 2170, 1050),
            ("route-1", 2370, 1050),
            ("route-1", 2570, 1050),
            ("route-1", 2770, 1050),
            ("route-1", 2970, 1050),
            ("route-2", 3170, 1050),
            ("route-2", 3310, 1190),
            ("route-1", 3452, 1332),
            ("route-1", 3652, 1332),
            
            ("route-0", 340, 3882),
            ("route-3", 340, 4082),
            ("route-3", 200, 4222),
            ("route-3", 60, 4362),
            ("route-1", -284, 4504),
            ("route-1", -484, 4504),
            ("route-3", -484, 4504),
            ("route-3", -624, 4644),
            ("route-1", -968, 4785),
            ("route-1", -1168, 4785),
            ("route-3", -1168, 4785),
            ("route-3", -1309, 4926),
            ("route-3", -1450, 5067),
            ("route-3", -1591, 5208),
            ("route-3", -1732, 5349),
            ("route-3", -1873, 5490),
            ("route-3", -2014, 5631),
            ("route-3", -2155, 5772),
            ("route-3", -2296, 5913),
            ("route-1", -2637, 6054),
            ("route-1", -2837, 6054),
            
            ("building-0", -2937, 6034),
            ("building-0", -3037, 6034),
            ("building-0", -2987, 6134),

            ("route-3", -3037, 6120),
            ("route-1", -3378, 6261),
            ("route-1", -3578, 6261),
            ("route-3", -3578, 6261),
            ("route-3", -3719, 6402),
            ("route-1", -4060, 6543),
            ("route-3", -4060, 6543),
            ("route-3", -4201, 6684),
            ("route-1", -4542, 6825),
            ("route-3", -4542, 6825),
            ("route-3", -4683, 6966),
            ("route-1", -5024, 7107),
            ("route-1", -5224, 7107),
            ("route-1", -5424, 7107),
            ("route-3", -5424, 7107),
            ("route-1", -5765, 7248),
            ("route-1", -5965, 7248),

            ("fortress-0", -5300, 6700),
            ("fortress-0", -5200, 6675),

            ("route-2", -6106, 7107),
            ("route-2", -6247, 6966),
            ("building-0", -6347, 6914),
            ("building-0", -6447, 6914),

            ("route-2", -6588, 6825),
            ("route-2", -6728, 6684),
            ("route-0", -6728, 6484),
            ("route-0", -6728, 6284),
            ("route-0", -6728, 6084),
            ("route-0", -6728, 5884),
            ("building-0", -6778, 5784),

            ("route-3", -5965, 7248),
            ("route-3", -6106, 7389),
            ("route-1", -6447, 7530),
            ("route-1", -6647, 7530),
            ("route-3", -6647, 7530),
            ("route-3", -6788, 7671),
            ("route-3", -6927, 7812),
            ("route-3", -7068, 7953),

            ("building-0", -7309, 8053),
            ("airport-0", -7459, 8038),

            ("route-1", -1650, -160),
            ("route-1", -1450, -160),
            ("route-1", -1250, -160),
            ("route-3", -909, -301),
            ("route-1", -909, -301),
            ("route-1", -709, -301),
            ("route-1", -509, -301),
            ("route-1", -309, -301),
            ("route-2", -109, -301),
            ("route-1", 31, -160),
            ("route-1", 231, -160),
            ("route-1", 431, -160),
            ("route-2", 631, -160),
            ("route-2", 772, -19),
            ("route-2", 913, 122),
            ("route-2", 1054, 263),
            ("route-2", 1195, 404),
            ("route-2", 1336, 545),
            ("route-2", 1477, 686),
        ],
        "terrains": [
            ("base", "water-1"),
            ("polygon", "water-0",
             (-50.38, -6197.8),
             (-8089.69, -5000.45),
             (-11318.24, -3247.2),
             (-15017.18, 686.93),
             (-15337.9, 3808.58),
             (-12323.16, 9260.77),
             (-8324.88, 11719.6),
             (-4497.66, 11206.46),
             (227.58, 8769.01),
             ),
            ("polygon", "water-0",
             (-57.7, -6168.3),
             (3350.66, -4606.13),
             (4025.24, -2972.96),
             (2027.86, 6988.89),
             (239.43, 8777.33),
             (-1862.77, 1451.02),
            ),
            ("polygon", "steppe-0",
             (-9000, -2000),
             (-7000, -3700),
             (0, -5200),
             (5000, -3000),
             (7000, -1000),
             (7000, 6000),
             (2000, 7000),
             (-10000, 5000)
            ),
            ("polygon", "steppe-0",
             (-9974.91, 4990.79),
             (-9272.81, 9773.08),
             (-8196.26, 10631.2),
             (-4872.98, 10428.37),
             (-1471.69, 6368.6),
            ),
            ("polygon", "highland-1",
             (1423.8, 2257.5),
             (1517.21, 2771.29),
             (2229.51, 3366.82),
             (2895.09, 3355.14),
             (3175.34, 3004.83),
             (2918.45, 2432.66),
             (2311.25, 2117.38),
             (1622.31, 2035.64),
            ),
            ("polygon", "highland-1",
             (-4755.15, -3208.67),
             (-3755.15, -3908.67),
             (-144.92, -4560.37),
             (244.92, -4560.37),
             (3248.12, -2905.23),
             (3992.93, -1525.95),
             (4048.11, -891.48),
             (2227.45, -367.35),
             (-503.53, -615.62),
             (-3620.71, -1663.88),
             (-4668.96, -2519.03),
            ),
            ("polygon", "highland-1",
             (-4741.03, -3198.57),
             (-6322.9, -3225.69),
             (-7452.81, -2466.39),
             (-7949.97, -1716.13),
             (-7624.55, -1146.65),
             (-7118.36, -902.59),
             (-5943.25, -812.2),
             (-4623.52, -1191.85),
             (-3945.57, -1996.34),
            ),
            ("polygon", "highland-1",
             (-6440.48, 5243.98),
             (-5907.93, 5297.24),
             (-4949.32, 6504.37),
             (-5499.63, 8031.03),
             (-7044.05, 7977.77),
             (-7399.08, 6167.08),
            ),
            ("polygon", "highland-1",
             (-8193.82, 2421.1),
             (-7593.82, 2421.1),
             (-6698.83, 3904.22),
             (-6481.47, 5374.56),
             (-7184.68, 6729.83),
             (-8527.16, 6653.12),
             (-9128.08, 5182.78),
             (-8782.87, 4134.36),
            ),
            ("polygon", "highland-1",
             (-5930.73, 5401.01),
             (-5778.46, 4525.48),
             (-4433.45, 3573.82),
             (-2060.65, 2596.78),
             (-1197.81, 2901.31),
             (-753.7, 3662.64),
             (-1426.21, 4436.66),
             (-3799.01, 5933.93),
             (-5170.91, 6249.64),
            ),
            ("polygon", "highland-1",
             (-5713.15, 6406.36),
             (-5167.72, 5726.97),
             (-3980.83, 5573.86),
             (-3713.25, 6827.39),
             (-5416.52, 7746.01),
            ),
            ("polygon", "highland-1",
             (-8055.13, -350.2),
             (-7750.91, -308.24),
             (-7404.72, 310.7),
             (-7604.72, 810.7),
             (-8348.87, 1076.51),
             (-8548.19, 572.96),
             (-8506.22, 205.8),
             ),
            ("polygon", "highland-1",
             (-8510.62, 6464.2),
             (-8836.47, 7876.24),
             (-8743.37, 8884.84),
             (-8091.66, 9629.65),
             (-7176.16, 9272.76),
             (-6307.21, 8000.38),
             (-6369.28, 7271.08),
             (-7362.36, 6619.37),
            ),
            ("polygon", "highland-1",
             (-760.83, 413.13),
             (-454.18, 248.45),
             (312.45, 430.17),
             (443.06, 540.28),
             (391.96, 710.64),
             (113.7, 812.86),
             (-403.07, 722.0),
             (-712.5, 562.59),
            ),
            ("polygon", "highland-1",
             (5152.02, 5067.89),
             (4615.89, 4649.83),
             (3621.57, 4525.54),
             (2243.08, 4604.63),
             (1158.37, 4887.11),
             (1192.27, 5565.05),
             (2197.89, 6220.4),
             (3904.05, 6118.71),
             (4887.07, 5610.25),
            ),
            ("polygon", "highland-2",
             (-2277.57, -3615.92),
             (-815.31, -3844.95),
             (329.83, -3668.77),
             (1774.46, -2964.07),
             (2126.82, -2488.4),
             (1933.02, -2100.81),
             (417.92, -2118.43),
             (-1167.66, -2329.84),
             (-2189.48, -2858.37),
            ),
            ("polygon", "highland-2",
             (2118.66, -2489.12),
             (1622.28, -2520.15),
             (1079.37, -2434.83),
             (1312.05, -1628.22),
             (1909.25, -1162.86),
             (2335.83, -1310.22),
             (2661.58, -1884.16),
             (2312.56, -2310.74),
            ),
            ("polygon", "highland-2",
             (-2047.09, 3076.89),
             (-1576.57, 3393.14),
             (-1476.29, 3855.95),
             (-2772.16, 4920.42),
             (-4214.59, 5390.94),
             (-4908.81, 5336.95),
             (-5294.48, 5074.69),
             (-4062.25, 3811.05),
            ),
            ("polygon", "highland-2",
             (-5291.98, 5070.5),
             (-4604.89, 5076.09),
             (-4213.86, 5372.15),
             (-4252.96, 6076.0),
             (-5085.29, 6919.5),
             (-5582.45, 6908.33),
             (-5917.62, 6511.72),
             (-5783.55, 5869.31),
            ),
            ("polygon", "highland-2",
             (-8379.99, 4068.01),
             (-7793.56, 3754.34),
             (-7316.24, 4095.29),
             (-6907.1, 5213.6),
             (-7234.41, 5827.3),
             (-8052.68, 6031.87),
             (-8611.84, 5309.06),
             (-8666.39, 4899.92),
            ),
            ("polygon", "steppe-0",
             (-2813.8, -1068.57),
             (-2047.67, -1445.47),
             (-1261.56, -1531.62),
             (-217.01, -1305.48),
             (227.58, -842.43),
             (449.12, -444.0),
             (-1013.89, -271.7),
             (-1789.22, -467.05),
            ),
            ("polygon", "water-1",
             (4000, 2000),
             (4000, 1000),
             (7500, 1000),
             (7500, 5000),
             (5000, 4000),
             ),
                        ("polygon", "forest-0",
             (2738.12, 1283.34),
             (3297.37, 1571.98),
             (3522.88, 2059.07),
             (3721.32, 2717.55),
             (3577.0, 2915.99),
             (3297.37, 2753.63),
             (2801.26, 2221.44),
             (2539.68, 1590.02),
            ),
            ("polygon", "forest-0",
             (-1893.34, 430.35),
             (-1376.36, 420.53),
             (-1022.99, 525.24),
             (-771.04, 816.45),
             (-787.4, 1078.21),
             (-1032.8, 1349.79),
             (-1487.61, 1523.2),
             (-1962.06, 1444.68),
             (-2351.43, 1094.57),
             (-2328.52, 773.91),
             ),
            ("polygon", "forest-0",
             (-1195.09, 1216.23),
             (-849.99, 1111.98),
             (-353.92, 1302.5),
             (-274.83, 1590.08),
             (-404.24, 1881.26),
             (-681.04, 1913.61),
             (-965.02, 1802.17),
             (-1177.12, 1518.19),
             (-1234.63, 1403.15),
            ),
            ("polygon", "forest-0",
             (-6877.43, 308.43),
             (-5593.61, -441.41),
             (-4457.49, -680.0),
             (-3525.87, -236.91),
             (-3025.98, 547.01),
             (-2969.17, 1489.99),
             (-3707.65, 2648.84),
             (-4764.24, 3114.65),
             (-6002.62, 2762.45),
             (-7104.65, 1955.8),
            ),
            ("polygon", "forest-0",
             (-3571.91, 232.81),
             (-2518.38, -114.95),
             (-1843.3, 478.3),
             (-2058.1, 1337.49),
             (-3193.46, 1756.85),
             ),
            ("polygon", "forest-0",             
             (-3937.34, -449.46),
             (-3069.57, -492.84),
             (-2516.37, -113.2),
             (-2836.36, 548.48),
             (-3731.25, 483.4),
            ),
            ("polygon", "forest-0",
             (2080.65, 434.9),
             (2485.7, 216.49),
             (2835.15, 256.2),
             (3140.92, 561.97),
             (3045.61, 1173.51),
             (2803.38, 1439.57),
             (2799.41, 1443.54),
             (2223.61, 1102.03),
             (2132.28, 832.0),
            ),
            ("polygon", "forest-0",
             (2223.61, 1099.66),
             (3042.78, 1150.57),
             (3288.07, 1571.73),
             (2552.2, 1562.47),
             (2214.35, 1395.86),
            ),
            ("polygon", "forest-0",
             (-1510.82, 4984.31),
             (-1541.69, 4710.84),
             (-1140.31, 4344.74),
             (-668.35, 4335.92),
             (-438.99, 4706.43),
             (-527.21, 5037.24),
             (-968.29, 5218.08),
            ),
            ("polygon", "water-0",
             (4750, 3500),
             (5050, 3600),
             (5000, 4000),
             (4000, 4000),
             (4000, 3700),
            ),
            ("polygon", "water-0",
             (4003, 4000),
             (2100, 3900),
             (2100, 3700),
             (4003, 3700),
            ),
            ("polygon", "water-0",
             (2103, 3900),
             (1000, 3000),
             (1200, 3000),
             (2103, 3700),
            ),
            ("polygon", "water-0",
             (1004, 3005),
             (1196, 3002),
             (761, 1063),
             (663, 1060),
            ),
            ("polygon", "water-0",
             (664.34, 1061.52),
             (759.26, 1064.67),
             (791.65, 550.22),
             (652.19, 548.87),
             ),
            ("polygon", "water-0",            
             (651.76, 550.95),
             (791.8, 550.8),
             (551.7, 110.93),
             (492.65, 266.76),
             ),
            ("polygon", "water-0",
             (515.49, 273),
             (-448.9, 76.5),
             (-460.53, -71.78),
             (555.38, 115.41),
             ),
            ("polygon", "water-0",
             (-446.54, 76.71),
             (-1694.96, 301.77),
             (-1686.92, 166.63),
             (-457.8, -72.64),
             ),
            ("polygon", "water-0",
             (-1679.59, 168.24),
             (-1689.02, 299.5),
             (-3568.04, 412.9),
             (-3568.04, 284.07),
             ),
            ("polygon", "water-0",
             (-3551.33, 299.74),
             (-4214.69, -85.94),
             (-5171.16, -31.95),
             (-5772.82, 1194.5),
             (-5618.55, 2336.1),
             (-4924.33, 2945.4),
             (-3913.86, 2505.8),
             (-3413.86, 1505.8),
             (-3359.04, 707.72),
             ),
            ("polygon", "water-0",
             (-5119.6, 2763.4),
             (-4915.3, 2921.37),
             (-6084.36, 4360.48),
             (-6316.2, 4305.93),
            ),
            ("polygon", "water-0",
             (-6305.4, 4306.7),
             (-6090.99, 4351.2),
             (-6188.08, 5823.74),
             (-6264.94, 5827.79),
            ),
        ]
    }
}
