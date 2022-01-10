"""Constants for the rademacher integration."""

DOMAIN = "rademacher"

COVER_TYPE = 0
ENV_SENSOR_TYPE = 1
SWITCH_ACTUATOR_TYPE = 2

## API Capability names
# Common
APICAP_PROT_ID_DEVICE_LOC = "PROT_ID_DEVICE_LOC"
APICAP_ID_DEVICE_LOC = "ID_DEVICE_LOC"
APICAP_NAME_DEVICE_LOC = "NAME_DEVICE_LOC"
APICAP_PROD_CODE_DEVICE_LOC = "PROD_CODE_DEVICE_LOC"
APICAP_VERSION_CFG = "VERSION_CFG"
APICAP_PING_CMD = "PING_CMD"
APICAP_REACHABILITY_EVT = "REACHABILITY_EVT"
# Cover
APICAP_GOTO_POS_CMD = "GOTO_POS_CMD"
APICAP_CURR_POS_CFG = "CURR_POS_CFG"
# Switch
APICAP_CURR_SWITCH_POS_CFG = "CURR_SWITCH_POS_CFG"
# Sensor
APICAP_SUN_DIRECTION_MEA = "SUN_DIRECTION_MEA"
APICAP_SUN_HEIGHT_DEG_MEA = "SUN_HEIGHT_DEG_MEA"
APICAP_LIGHT_VAL_LUX_MEA = "LIGHT_VAL_LUX_MEA"
APICAP_WIND_SPEED_MS_MEA = "WIND_SPEED_MS_MEA"
APICAP_TEMP_CURR_DEG_MEA = "TEMP_CURR_DEG_MEA"
APICAP_RAIN_DETECTION_MEA = "RAIN_DETECTION_MEA"

SUPPORTED_DEVICES = {
    "35001164": {"name": "DuoFern Switch actuator", "Type": SWITCH_ACTUATOR_TYPE},
    "35000262": {
        "name": "DuoFern Universal actuator 2-channel",
        "Type": SWITCH_ACTUATOR_TYPE,
    },
    "35000462": {"name": "DuoFern Universal dimming actuator", "Type": None},
    "36500572_A": {"name": "Troll Comfort DuoFern", "Type": None},
    "36500572_S": {"name": "Sun sensor Troll Comfort DuoFern", "Type": None},
    "36501512": {"name": "Troll Comfort DuoFern", "Type": None},
    "35002414": {"name": "Z-Wave Repeater with switching function", "Type": None},
    "35140462": {"name": "DuoFern Universal dimmer", "Type": None},
    "35003064": {"name": "DuoFern Radiator Actuator", "Type": None},
    "35003064_A": {"name": "DuoFern Radiator Actuator", "Type": None},
    "35003064_S": {
        "name": "Temperature sensor DuoFern Radiator Actuator",
        "Type": None,
    },
    "32501812_A": {"name": "DuoFern Room Thermostat", "Type": None},
    "32501812_S": {"name": "Temperature sensor DuoFern Room thermostat", "Type": None},
    "35002319": {"name": "Z-Wave radiator actuator", "Type": None},
    "35000662": {"name": "DuoFern tubular motor actuator", "Type": COVER_TYPE},
    "35000864": {"name": "DuoFern Connect actuator", "Type": None},
    "36500172": {"name": "Troll Basis DuoFern", "Type": None},
    "31500162": {"name": "DuoFern tubular motor control B50/B55", "Type": COVER_TYPE},
    "27601565": {"name": "DuoFern tubular motor", "Type": COVER_TYPE},
    "16234511_A": {"name": "RolloTron Comfort DuoFern", "Type": COVER_TYPE},
    "16234511_S": {"name": "Sun sensor RolloTron Comfort DuoFern", "Type": None},
    "14236011": {"name": "RolloTron radio beltwinder 60 kg", "Type": COVER_TYPE},
    "14234511": {"name": "RolloTron radio beltwinder", "Type": COVER_TYPE},
    "45059071": {"name": "RolloPort SX5 DuoFern", "Type": None},
    "32000064_A": {
        "name": "DuoFern tubular motor actuator environmental sensor",
        "Type": COVER_TYPE,
    },
    "32000064_S": {
        "name": "Sensor DuoFern Environmental sensor",
        "Type": ENV_SENSOR_TYPE,
    },
    "32501772_A": {"name": "Actuator DuoFern Motion detector (indoor)", "Type": None},
    "32501772_S": {"name": "Sensor DuoFern Motion detector (indoor)", "Type": None},
    "32000069": {"name": "DuoFern Sun Sensor", "Type": None},
    "32001664": {"name": "DuoFern Smoke Alarm Device", "Type": None},
    "32001464": {"name": "DuoFern Awning monitor", "Type": None},
    "32002119": {"name": "Z-Wave window/door contact", "Type": None},
    "32004219": {"name": "HomePilot\xae HD Camera (Indoor)", "Type": None},
    "32004329": {"name": "HomePilot\xae HD Camera (Outdoor)", "Type": None},
    "32004119": {"name": "IP Camera", "Type": None},
    "99999999": {"name": "Android Smartphone (GeoPilot)", "Type": None},
    "99999998": {"name": "iOS Smartphone (GeoPilot)", "Type": None},
    "32003164": {"name": "DuoFern Window/Door Contact", "Type": None},
    "32480366": {
        "name": "DuoFern Standard manual transmitter 6 groups 48 devices",
        "Type": None,
    },
    "32480361": {
        "name": "DuoFern Standard manual transmitter 1 group 48 devices",
        "Type": None,
    },
    "32010361": {
        "name": "DuoFern Standard manual transmitter 1 group 1 device",
        "Type": None,
    },
    "32060366": {
        "name": "DuoFern Standard manual transmitter 1 group 6 devices",
        "Type": None,
    },
    "32000062_S": {"name": "Sensor DuoFern Radio transmitter UP", "Type": None},
    "32000062": {"name": "DuoFern radio transmitter UP", "Type": None},
    "32501972_A": {
        "name": "Actuator DuoFern Multiple Wall Controller 230V",
        "Type": None,
    },
    "32501972_S": {
        "name": "Sensor DuoFern Multiple Wall Controller 230V",
        "Type": None,
    },
    "32501974": {"name": "DuoFern Multiple Wall Controller BAT", "Type": None},
    "32160211": {"name": "DuoFern Wall Controller", "Type": None},
    "34810060": {"name": "DuoFern Central Operating Unit", "Type": None},
    "32501371": {"name": "DuoFern HomeTimer", "Type": None},
    "35140662": {"name": "DuoFern tubular motor actuator", "Type": COVER_TYPE},
    "32501973": {"name": "DuoFern Wall Controller 1 channel", "Type": None},
    "23602075": {"name": "RolloTube S-line DuoFern", "Type": COVER_TYPE},
    "25782075": {"name": "RolloTube S-line Zip DuoFern", "Type": COVER_TYPE},
    "23782076": {"name": "RolloTube S-line Sun DuoFern", "Type": None},
    "35274001": {"name": "addZ White + Colour LED E27", "Type": None},
    "35144001": {"name": "addZ White + Colour LED E14", "Type": None},
    "35104001": {"name": "addZ White + Colour LED GU10", "Type": None},
    "99999973": {"name": "Zigbee White LED", "Type": None},
    "99999974": {"name": "Zigbee tuneable white LED", "Type": None},
    "99999975": {"name": "Zigbee RGBW LED", "Type": None},
    "99999976": {"name": "Zigbee RGB LED", "Type": None},
    "99999950": {"name": "ONVIF Camera", "Type": None},
    "32004464": {"name": "DuoFern Sun/Wind Sensor", "Type": None},
    "32320364": {"name": "DuoFern Standard manual transmitter 4 groups", "Type": None},
}
