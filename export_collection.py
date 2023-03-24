import argparse
from datetime import datetime, timedelta
from cassandra.cluster import Cluster
import json


# функция для преобразования объекта
def transform_object(obj):
    # код для преобразования объекта

    return obj


# функция для выгрузки коллекции и преобразования объектов
def export_collection(host, port, login, password, days):
    # устанавливаем соединение с базой данных
    cluster = Cluster([host], port=port)
    session = cluster.connect()
    session.execute(f"USE keyspace_name")

    # получаем текущую дату и время
    now = datetime.now()

    # вычисляем дату начала периода
    start_date = now - timedelta(days=days)

    # выполняем запрос к базе данных
    result = session.execute(f"SELECT * FROM collection_name WHERE date >= '{start_date.isoformat()}' ALLOW FILTERING")

    # преобразуем объекты и записываем в список
    objects = []
    for row in result:
        obj = row._asdict()
        obj = transform_object(obj)
        objects.append(obj)

    # закрываем соединение с базой данных
    session.shutdown()
    cluster.shutdown()

    # записываем объекты в json файл
    file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    with open(file_name, "w") as file:
        json.dump(objects, file)

    print(f"Экспортировано {len(objects)} объектов в {file_name}")


if __name__ == "__main__":
    # определяем параметры командной строки
    parser = argparse.ArgumentParser(description="Экспорт коллекции из базы данных Apache Cassandra в файл json")
    parser.add_argument("host", help="IP-адрес сервера базы данных Cassandra")
    parser.add_argument("port", type=int, help="Номер порта сервера базы данных Cassandra")
    parser.add_argument("login", help="Имя пользователя для аутентификации в Cassandra")
    parser.add_argument("password", help="Пароль для аутентификации в Cassandra")
    parser.add_argument("-d", "--days", type=int, default=30, help="Количество дней для экспорта (по умолчанию 30)")
    args = parser.parse_args()

    # проверяем наличие всех необходимых параметров
    if not all([args.host, args.port, args.login, args.password]):
        parser.print_help()
        exit()

    # выполняем выгрузку коллекции
    export_collection(args.host, args.port, args.login, args.password, args.days)
