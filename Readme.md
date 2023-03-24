# English
## Installation instructions

1. Install Python 3.6 or higher.
2. Install the `cassandra-driver` package using the pip package manager:

```bash
pip install cassandra-driver
```
## Running instructions

1. Copy the file `export_collection.py` to your computer.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script, specifying the necessary parameters in the command line:

```bash
python export_collection.py <database_address> <database_port> <user_login> <user_password> [-d <number_of_days>]
```

where:
- `<database_address>` - the IP address of the Cassandra database server.
- `<database_port>` - the port on which the Cassandra database is running.
- `<user_login>` - the login of the Cassandra database user.
- `<user_password>` - the password of the Cassandra database user.
- `<number_of_days>` (optional parameter) - the number of days for which data should be exported. By default, it is set to 30 days.

## Description

When the script is run, it connects to the Cassandra database and exports data from the specified collection with a filter on the `date` field. The exported data is then converted to an object, after which a separate function is called to transform some fields of this object. After this, the object is saved in JSON format to a file with a name containing the current date and time.

# Russian
## Инструкция по установке

1. Установите Python версии 3.6 или выше.
2. Установите пакет `cassandra-driver` с помощью менеджера пакетов pip:
    
```bash
pip install cassandra-driver
```

## Инструкция по запуску

1. Скопируйте файл `export_collection.py` на свой компьютер.
2. Откройте терминал и перейдите в папку, где находится скрипт.
3. Запустите скрипт, указав необходимые параметры в командной строке:

```bash
python export_collection.py <адрес_базы_данных> <порт_базы_данных> <логин_пользователя> <пароль_пользователя> [-d <количество_дней>]
```

где:
- `<адрес_базы_данных>` - IP-адрес сервера базы данных Cassandra.
- `<порт_базы_данных>` - порт, на котором запущена база данных Cassandra.
- `<логин_пользователя>` - логин пользователя базы данных Cassandra.
- `<пароль_пользователя>` - пароль пользователя базы данных Cassandra.
- `<количество_дней>` (необязательный параметр) - количество дней, за которые нужно выгрузить данные. По умолчанию равно 30 дням.

## Описание работы скрипта

При запуске скрипта происходит подключение к базе данных Cassandra и выгрузка данных из указанной коллекции с фильтром по полю `date`. Затем происходит преобразование полученных данных в объект, после чего вызывается отдельная функция, в которой происходит преобразование некоторых полей этого объекта. После этого объект сохраняется в формате JSON в файл с именем, содержащим текущую дату и время.
