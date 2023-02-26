import asyncio
import bleak

async def macaddress_find_connected(name, repeat):
    for i in range(repeat):
        devices = await bleak.discover()
        for d in devices:
            if d.name == name:
                return d.address


async def macaddress_findby_name(name, repeat):
    for i in range(repeat):
        devices = await bleak.BleakScanner.discover(timeout=5)
        for d in devices:
            if d.name == name:
                return d.address


async def read_mapped_key(address):
    async with bleak.BleakClient(address) as client:
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                for t in characteristic.properties:
                    if t == "write":
                        read_data = await client.read_gatt_char(characteristic.uuid)
                        return read_data





async def write_key_mapping(address,keymap):
    async with bleak.BleakClient(address) as client:
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                for t in characteristic.properties:
                    if t == "write":
                        translated_keymap = translate(keymap)
                        print(translated_keymap)
                        await client.write_gatt_char(characteristic, bytes(translated_keymap))


def get_key_from_device(name):
    try:
        if asyncio.get_event_loop().run_until_complete(macaddress_find_connected(name, 1)):
            address = asyncio.get_event_loop().run_until_complete(macaddress_find_connected(name, 1))
        else:
            address = asyncio.get_event_loop().run_until_complete(macaddress_findby_name(name, 1))
        data = asyncio.get_event_loop().run_until_complete(read_mapped_key(address))
        print(list(data))
    except Exception as e:
        print(e)



def write_key(name,key_list):
    if asyncio.get_event_loop().run_until_complete(macaddress_find_connected(name, 1)):
        address = asyncio.get_event_loop().run_until_complete(macaddress_find_connected(name, 1))
    else:
        address = asyncio.get_event_loop().run_until_complete(macaddress_findby_name(name, 1))
    asyncio.get_event_loop().run_until_complete(write_key_mapping(address,key_list))

def translate(list):
    key_dictionary = {"KC_NO":0,"KC_0":48,"KC_1":49,"KC_2":50,"KC_3":51,"KC_4":52,"KC_5":53,"KC_6":54,"KC_7":55,"KC_8":56,"KC_9":57,"KC_A":65,"KC_B":66,"KC_C":67,"KC_D":68,"KC_E":69,"KC_F":70,"KC_G":71,"KC_H":72,"KC_I":73,"KC_J":74,"KC_K":75,"KC_L":76,"KC_M":77,"KC_N":78,"KC_O":79,"KC_P":80,"KC_Q":81,"KC_R":82,"KC_S":83,"KC_T":84,"KC_U":85,"KC_V":86,"KC_W":87,"KC_X":88,"KC_Y":89,"KC_Z":90,"KC_ENT":176,"KC_ESC":177,"KC_BSPC":178,"KC_TAB":179,"KC_SPC":32,"KC_MINS":45,"KC_EQL":61,"KC_LBRC":91,"KC_RBRC":93,"KC_BSLS":92,"KC_SCLN":59,"KC_QUOT":39,"KC_GRV":96,"KC_COMM":44,"KC_DOT":46,"KC_SLSH":47,"KC_CAPS":193,"KC_F1":194,"KC_F2":195,"KC_F3":196,"KC_F4":197,"KC_F5":198,"KC_F6":199,"KC_F7":200,"KC_F8":201,"KC_F9":202,"KC_F10":203,"KC_F11":204,"KC_F12":205,"KC_F13":240,"KC_F14":241,"KC_F15":242,"KC_F16":243,"KC_F17":244,"KC_F18":245,"KC_F19":246,"KC_F20":247,"KC_F21":248,"KC_F22":249,"KC_F23":250,"KC_F24":251,"KC_PSCR":206,"KC_SCRL":207,"KC_PAUS":208,"KC_INS":209,"KC_HOME":210,"KC_PGUP":211,"KC_DEL":212,"KC_END":213,"KC_PGDN":214,"KC_RGHT":218,"KC_LEFT":216,"KC_DOWN":217,"KC_UP":218,"KC_NUM":219,"KC_PSLS":220,"KC_PAST":221,"KC_PMNS":222,"KC_PPLS":223,"KC_PENT":224,"KC_P1":225,"KC_P2":226,"KC_P3":227,"KC_P4":228,"KC_P5":229,"KC_P6":230,"KC_P7":231,"KC_P8":232,"KC_P9":233,"KC_P0":234,"KC_PDOT":235,"KC_APP":237,"KC_PEQL":61,"KC_INT3":92,"KC_LCTL":128,"KC_LSFT":129,"KC_LALT":130,"KC_LOPT":130,"KC_LGUI":131,"KC_LCMD":131,"KC_LWIN":131,"KC_RCTL":132,"KC_RSFT":133,"KC_RALT":134,"KC_ROPT":134,"KC_ALGR":134,"KC_LNG1":134,"KC_RGUI":135,"KC_RCMD":135,"KC_RWIN":135,"KC_INT1":45,"KC_NUBS":92,"KC_INT5":132,"KC_INT5":132,"KC_INT2":132,"KC_LNG2":132,"KC_TILD":126,"KC_EXLM":33,"KC_AT":64,"KC_HASH":35,"KC_DLR":36,"KC_PERC":37,"KC_CIRC":94,"KC_AMPR":38,"KC_ASTR":42,"KC_LPRN":40,"KC_RPRN":41,"KC_UNDS":95,"KC_PLUS":43,"KC_LCBR":123,"KC_RCBR":125,"KC_PIPE":124,"KC_COLN":58,"KC_DQUO":34,"KC_DQT":34,"KC_LABK":60,"KC_LT":60,"KC_RABK":62,"KC_GT":62,"KC_QUES":63}
    translated = []
    for i in list:
        translated.append(key_dictionary[i])
    return translated


# write_key("ESP32",['KC_F7', 'KC_F8', 'KC_F9', 'KC_F10', 'KC_F11', 'KC_F12', 'KC_6', 'KC_7', 'KC_8', 'KC_9', 'KC_0', 'KC_BSPC', 'KC_Y', 'KC_U', 'KC_I', 'KC_O', 'KC_P', 'KC_PAST', 'KC_H', 'KC_J', 'KC_K', 'KC_L', 'KC_SCLN', 'KC_QUOT', 'KC_B', 'KC_N', 'KC_M', 'KC_UP', 'KC_RGHT', 'KC_BSLS', 'KC_LEFT', 'KC_DOWN', 'KC_LNG1', 'KC_ENT', 'KC_COMM', 'KC_DOT', 'KC_EQL', 'KC_MINS'])
# get_key_from_device("ble_left")


#test


async def run(address):    
    async with bleak.BleakClient(address) as client:
        print('connected')
        services = await client.get_services()        
        # 서비스내에 있는 캐릭터리스틱 정보 보기
        for service in services:
            print('Service :', service)                
            print('\tuuid:', service.uuid)
            print('\tcharacteristic list:')
            for characteristic in service.characteristics:
                print('\t\t', characteristic)
                print('\t\tuuid:', characteristic.uuid)
                print('\t\tdescription :', characteristic.description)
                # ['write-without-response', 'write', 'read', 'notify']
                print('\t\tproperties :', characteristic.properties)

def get_characters(name):
    try:
        if asyncio.get_event_loop().run_until_complete(macaddress_find_connected(name, 1)):
            address = asyncio.get_event_loop().run_until_complete(macaddress_find_connected(name, 1))
        else:
            address = asyncio.get_event_loop().run_until_complete(macaddress_findby_name(name, 1))
        asyncio.get_event_loop().run_until_complete(run(address))
    except Exception as e:
        print(e)



get_characters("ble_left")

# print(asyncio.get_event_loop().run_until_complete(macaddress_findby_name("ble_left", 1)))