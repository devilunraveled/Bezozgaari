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
    'item_volume': {'centilitre',
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
        'quart'}
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
        "''",
        'ft',
    },
    'inch' : {
        'inch',
        'inches',
        "'",
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
