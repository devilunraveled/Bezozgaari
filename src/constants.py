import pint

entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'maximum_weight_recommendation': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {
        'centilitre',
        'cubic foot',
        'cubic inch',
        'cup',
        'decilitre',
        'fluid ounce',
        'gallon',
        'imperial gallon',
        'litre',
        'microlitre',
        'millilitre',
        'pint',
        'quart'
    }
}

conversion_factor = {
    'centilitre' : {
        'centilitre' : 1,
        'cubic foot' : 0.000353146,
        'cubic inch' : 0.610237,
        'cup' : 0.00422675,
        'decilitre' : 0.1,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'cubic foot' :{
        'centilitre' : 28316.8,
        'cubic foot' : 1,
        'cubic inch' : 1728,
        'cup' : 119.688,
        'decilitre' : 2831.6,
        'fluid ounce' : 957.506,
        'gallon' : 7.48052,
        'imperial gallon' : 8.35592,
        'litre' : 28.3168,
        'microlitre' : 28_316_846.592,
        'millilitre' : 28_316.8466,
        'pint' : 8.47318,
        'quart' : 17.9464
    },
    'cubic inch' : {
        'centilitre' : 16.3871,
        'cubic foot' : 0.000578704,
        'cubic inch' : 1,
        'cup' : 0.236588,
        'decilitre' : 16.387,
        'fluid ounce' : 0.554112,
        'gallon' : 0.00454609,
        'imperial gallon' : 0.005195,
        'litre' : 0.016387,
        'microlitre' : 0.000016,
        'millilitre' : 0.0000163871,
        'pint' : 0.578704,
        'quart' : 1.15741
    },
    'cup' : {
        'centilitre' : 0.236588,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 1,
        'decilitre' : 0.2366,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'decilitre' : {
        'centilitre' : 10,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 1,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'fluid ounce' : {
        'centilitre' : 2.95735,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 29.574,
        'fluid ounce' : 1,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'gallon' : {
        'centilitre' : 29.5735,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 29.574,
        'fluid ounce' : 1,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'imperial gallon' : {
        'centilitre' : 29.5735,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 29.574,
        'fluid ounce' : 1,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'litre' : {
        'centilitre' : 1000,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 10000,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 1,
        'microlitre' : 0.000001,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'microlitre' : {
        'centilitre' : 1000000,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 10000000,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.001,
        'microlitre' : 1,
        'millilitre' : 0.001,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'millilitre' : {
        'centilitre' : 1000,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 10000,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 1,
        'microlitre' : 0.000001,
        'millilitre' : 1,
        'pint' : 0.473176,
        'quart' : 0.946353
    },
    'pint' : {
        'centilitre' : 473.176,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 4731.76,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 1,
        'quart' : 2
    },
    'quart' : {
        'centilitre' : 946.353,
        'cubic foot' : 0.0283168,
        'cubic inch' : 0.0163871,
        'cup' : 0.236588,
        'decilitre' : 9463.53,
        'fluid ounce' : 0.0295735,
        'gallon' : 0.00378541,
        'imperial gallon' : 0.00454609,
        'litre' : 0.01,
        'microlitre' : 0.00001,
        'millilitre' : 0.001,
        'pint' : 2,
        'quart' : 1
    },
    'kilovolt' :{
        'kilovolt' : 1,
        'millivolt' : 1000000,
        'volt' : 0.001
    },
    'millivolt' : {
        'kilovolt' : 0.000001,
        'millivolt' : 1,
        'volt' : 0.001
    },
    'volt' : {
        'kilovolt' : 0.001,
        'millivolt' : 1000,
        'volt' : 1
    },
    'gram' : {
        'gram' : 1,
        'kilogram' : 0.001,
        'microgram' : 0.000001,
        'milligram' : 0.001,
        'ounce' : 0.035274,
        'pound' : 0.00220462,
        'ton' : 0.000001
    },
    'kilogram' : {
        'gram' : 1000,
        'kilogram' : 1,
        'microgram' : 0.000001,
        'milligram' : 1000,
        'ounce' : 35.274,
        'pound' : 2.20462,
        'ton' : 0.001
    },
    'microgram' : {
        'gram' : 0.000001,
        'kilogram' : 0.000000001,
        'microgram' : 1,
        'milligram' : 0.000001,
        'ounce' : 0.000035274,
        'pound' : 0.00000220462,
        'ton' : 0.000000001
    },
    'milligram' : {
        'gram' : 0.001,
        'kilogram' : 0.000001,
        'microgram' : 0.000000001,
        'milligram' : 1,
        'ounce' : 0.035274,
        'pound' : 0.00220462,
        'ton' : 0.000001
    },
    'ounce' : {
        'gram' : 28.3495,
        'kilogram' : 0.0283495,
        'microgram' : 0.0000283495,
        'milligram' : 28.3495,
        'ounce' : 1,
        'pound' : 0.0625,
        'ton' : 0.0000283495
    },
    'pound' : {
        'gram' : 453.592,
        'kilogram' : 0.453592,
        'microgram' : 0.000453592,
        'milligram' : 453.592,
        'ounce' : 16,
        'pound' : 1,
        'ton' : 0.000453592
    },
    'ton' : {
        'gram' : 1000000,
        'kilogram' : 1000,
        'microgram' : 0.000001,
        'milligram' : 1000000,
        'ounce' : 35274,
        'pound' : 2204.62,
        'ton' : 1
    },
    'centimetre' : {
        'centimetre' : 1,
        'foot' : 0.0328084,
        'inch' : 0.393701,
        'metre' : 0.01,
        'millimetre' : 10,
        'yard' : 0.0109361
    },
    'foot' : {
        'centimetre' : 30.48,
        'foot' : 1,
        'inch' : 12,
        'metre' : 0.3048,
        'millimetre' : 304.8,
        'yard' : 0.9144
    },
    'inch' : {
        'centimetre' : 2.54,
        'foot' : 0.0833333,
        'inch' : 1,
        'metre' : 0.0254,
        'millimetre' : 25.4,
        'yard' : 0.0277778
    },
    'metre' : {
        'centimetre' : 100,
        'foot' : 3.28084,
        'inch' : 39.3701,
        'metre' : 1,
        'millimetre' : 1000,
        'yard' : 1.09361
    },
    'millimetre' : {
        'centimetre' : 0.1,
        'foot' : 0.00328084,
        'inch' : 0.0393701,
        'metre' : 0.001,
        'millimetre' : 1,
        'yard' : 0.00109361
    },
    'yard' : {
        'centimetre' : 91.44,
        'foot' : 3,
        'inch' : 36,
        'metre' : 0.9144,
        'millimetre' : 914.4,
        'yard' : 1
    }
}

aliases = {
    'centimetre' : {
        'centimeter',
        'centi',
        'cm',
    },
    'foot' : {
        'foot',
        'feet',
        "'",
        'ft',
    },
    'inch' : {
        'inch',
        'inches',
        "''",
        'in',
    },
    'metre' : {
        'meter',
        'metres',
        'm',
    },
    'millimetre' : {
        'millimetre',
        'millimeter',
        'milli',
        'mm',
    },
    'yard' : {
        'yard',
        'yards',
        'yd',
    },
    'gram' : {
        'gram',
        'grams',
        'g',
    },
    'kilogram' : {
        'kilogram',
        'kilograms',
        'kg',
    },
    'microgram' : {
        'microgram',
        'micrograms',
        'ug',
    },
    'milligram' : {
        'milligram',
        'milligrams',
        'mg',
    },
    'ounce' : {
        'ounce',
        'ounces',
        'oz',
    },
    'pound' : {
        'pound',
        'pounds',
        'lb',
    },
    'ton' : {
        'ton',
        'tons',
    },
    'kilowatt' : {
        'kilowatt',
        'kw',
    },
    'watt' : {
        'watt',
        'watts',
        'w',
    },
    'kilovolt' : {
        'kilovolt',
        'kv',
    },
    'millivolt' : {
        'millivolt',
        'mv',
    },
    'volt' : {
        'volt',
        'volts',
        'v',
    },
    'centilitre' : {
        'centilitre',
        'centilitres',
        'cl',
    },
    'cubic foot' : {
        'cubic foot',
        'cubic feet',
        'cf',
        'c3',
    },
    'cubic inch' : {
        'cubic inch',
        'cubic inches',
        'ci',
        'c3',
    },
    'cup' : {
        'cup',
        'cups',
        'c',
    },
    'decilitre' : {
        'decilitre',
        'decilitres',
        'dl',
    },
    'fluid ounce' : {
        'fluid ounce',
        'fluid ounces',
        'fl oz',
        'fl',
        'oz'
    },
    'gallon' : {
        'gallon',
        'gallons',
        'gal',
    },
    'imperial gallon' : {
        'imperial gallon',
        'imperial gallons',
    },
    'litre' : {
        'litre',
        'litres',
        'l',
    },
    'microlitre' : {
        'microlitre',
        'microlitres',
        'ul',
    },
    'millilitre' : {
        'millilitre',
        'millilitres',
        'ml',
    },
    'pint' : {
        'pint',
        'pints',
        'pt',
    },
    'quart' : {
        'quart',
        'quarts',
        'qt',
    },
}

allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}
