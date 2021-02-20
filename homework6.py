import json
import os

class Ipv4_manager:
    """ предоставляет ф-ции для работы с ipv4 """
    _sep = '.'

    def __init__(self, ip_list):
        if all(self.__class__.is_ipv4(ip) for ip in ip_list):
            raise ValueError("не верный формат ip-адресса")
        self.ip_list = ip_list

    def get_ip_list(self):
        return self.ip_list

    def get_ip_reversed(self):
        return [self.__class__._sep.join(ip.split(self.__class__._sep)[::-1]) for ip in self.ip_list]

    def get_without_last_actets(self):
        return [ip.rsplit(self.__class__._sep, 1)[0] for ip in self.ip_list]

    def get_lst_actets(self):
        return [ip.rsplit(self.__class__._sep, 1)[1] for ip in self.ip_list]

    @staticmethod
    def is_ipv4(ip):
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
        with open(output_path, 'w'):
            json.dump(output_data, f)

    @staticmethod
    def get_relative_path(project_path, file_path):
        return os.path.relpath(file_path, start=project_path)

    @staticmethod
    def get_absolute_path(project_path, relative_path):
        return os.path.join(project_path, relative_path)
        
    


if __name__ == '__main__':
    """ ip_coll = Ipv4_manager(["192.168.0.1", "192.168.0.10", "192.168.0.231"])
    print(ip_coll.get_ip_list())
    print(ip_coll.get_ip_reversed())
    print(ip_coll.get_lst_actets())
    print(ip_coll.get_without_last_actets()) """
    project_path = r'c:/Users/valen/Desktop/tests/python_test/hillel/homework'
    json_data_path = os.path.join(project_path, 'homework6_data')
    output_file_name = 'data.json'
    output_file_path = os.path.join(json_data_path, output_file_name)

    js_manager = JSON_manager()
    rel_path = js_manager.get_relative_path(project_path, output_file_path)
    print(project_path)
    print(output_file_path)
    print(rel_path)
    print('-----------------------------------------------------')
    abs_path = js_manager.get_absolute_path(project_path, rel_path)
    print(project_path)
    print(rel_path)
    print(abs_path)