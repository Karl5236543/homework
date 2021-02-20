import json
import os
import pprint

class Ipv4_manager:
    """ предоставляет ф-ции для работы с ipv4 """
    _sep = '.'

    def __init__(self, ip_list):
        if all(self.__class__.is_ipv4(ip) for ip in ip_list):
            raise ValueError("не верный формат ip-адреса")
        self._ip_list = ip_list

    @property
    def ip_list(self):
        return self._ip_list

    def get_ip_reversed(self):
        """ возвращает перевёрнутые ip-адресов"""
        return [self.__class__._sep.join(ip.split(self.__class__._sep)[::-1]) for ip in self.ip_list]

    def get_without_last_actets(self):
        """ возвращает последние 3 актета"""
        return [ip.rsplit(self.__class__._sep, 1)[0] for ip in self.ip_list]

    def get_lst_actets(self):
        """ возвращает первый актет """
        return [ip.rsplit(self.__class__._sep, 1)[1] for ip in self.ip_list]

    @staticmethod
    def is_ipv4(ip):
        """ проверяет соотвецтвует ли ip нужному формату """

        if not isinstance(ip, str):
            raise TypeError("ip-адресс должен быть строкой")
        actet_list = ip.split(Ipv4_manager._sep)
        if len(actet_list) != 4:
            return False
        if not all(isinstance(actet, int) for actet in actet_list):
            return False
        parsed_actet_list = [int(actet) for actet in actet_list]
        if not all(0 <= actet <= 255 for actet in parsed_actet_list):
            return False
        return True


class JSON_manager:
    @staticmethod
    def dump(path, data):
        with open(path, 'w') as f:
            json.dump(data, f)
    
    @staticmethod
    def load(path):
        if not os.path.exists(path):
            raise FileNotFoundError("файл не найден")
        with open(path) as f:
            return json.load(f)

    @staticmethod
    def concatenate(input_path_list, output_path):
        output_data = []
        for path in input_path_list:
            if not os.path.exists(path):
                raise FileNotFoundError("файл не найден")
            with open(path) as f:
                output_data.append(json.load(f))
        with open(output_path, 'w') as f:
            json.dump(output_data, f)

    @staticmethod
    def get_relative_path(project_path, file_path):
        return os.path.relpath(file_path, start=project_path)

    @staticmethod
    def get_absolute_path(project_path, relative_path):
        return os.path.join(project_path, relative_path)
        

class Swithc_connector:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name
    
    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value
    
    @property
    def mac_address(self):
        return self._mac_address
    
    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value
    
    @property
    def ip_address(self):
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, value):
        self._login = value
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value


def test_Ipv4_manager():
    ip_m = Ipv4_manager(["192.168.0.1", "192.168.0.10", "192.168.0.231"])
    print(f'ip_m.ip_list: {ip_m.ip_list}')
    print(ip_m.get_ip_reversed())
    print(ip_m.get_lst_actets())
    print(ip_m.get_without_last_actets())


def test_JSON_manager():
    project_path = r'c:/Users/valen/Desktop/tests/python_test/hillel/homework'
    json_data_path = os.path.join(project_path, 'homework6_data')
    file1_path = os.path.join(json_data_path, 'example_json_1.json')
    file2_path = os.path.join(json_data_path, 'example_json_2.json')

    js_manager = JSON_manager()
    rel_path = js_manager.get_relative_path(project_path, file1_path)
    print(f'project path:\t\t{project_path}')
    print(f'file1 path:\t\t{file1_path}')
    print(f'file1 relation path:\t{rel_path}')
    print('---------------------------------------------------------------------------------------------')

    abs_path = js_manager.get_absolute_path(project_path, rel_path)
    print(f'project path:\t\t{project_path}')
    print(f'file1 absolute path:\t{rel_path}')
    print(f'absolute file1 path:\t{abs_path}')
    print('---------------------------------------------------------------------------------------------')

    data = js_manager.load(file1_path)
    pprint.pprint(f'{file1_path} data:\n{data}')
    print('---------------------------------------------------------------------------------------------')

    output_file_path = os.path.join(json_data_path, 'test1.json')
    js_manager.dump(output_file_path, data)
    print('---------------------------------------------------------------------------------------------')

    input_file_path = os.path.join(json_data_path, 'concatenated_data.json')
    js_manager.concatenate([file1_path, file2_path], input_file_path)
    concatenated_data = js_manager.load(input_file_path)
    pprint.pprint(f'concatenated data:\n{concatenated_data}')


def test_swithc_connector():
    sw_connector = Swithc_connector('switch1', '48:df:37:33:fc:20', '192.168.0.27', 'admin', 'admin')
    print(sw_connector.unit_name)
    sw_connector.unit_name = 'swith2'

    print(sw_connector.ip_address)
    sw_connector.ip_address = '192.168.0.28'

    print(sw_connector.mac_address)
    sw_connector.mac_address = '46:df:37:34:fc:21'

    print(sw_connector.login)
    sw_connector.login = 'admin2'

    print(sw_connector.password)
    sw_connector.password = '111'

    


if __name__ == '__main__':
    test_Ipv4_manager()
    test_JSON_manager()
    test_swithc_connector()
    