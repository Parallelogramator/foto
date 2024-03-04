import serial, sqlite3, datetime


def update_db(length, diameter, l, e):
    strength = e*(3.14159265358979 * (diameter*10**-6)**2)*length/l
    conn = sqlite3.connect('data.db')  # Данное соединение создаст файл data.db, если таковой не существует
    c = conn.cursor()

    # Вставляем данные в таблицу
    c.execute('''
        INSERT INTO Logs (strength, length, pleasure, time)
        VALUES (?, ?, ?)
    ''', (strength, length, strength/(3.14159265358979 * (diameter*10**-6)**2), datetime.datetime.now()))

    # Сохраняем изменения
    conn.commit()

    # Закрываем соединение с базой данных
    conn.close()


def start(diameter, coefficient, length):
    # Configure the COM port
    port = "COM22"  # Replace with the appropriate COM port name
    baudrate = 9600

    try:
        # Open the COM port
        ser = serial.Serial(port, baudrate=baudrate)
        ser.write(b'start')
        # Read data from the Arduino
        while True:
            # Read a line of data from the serial port
            line = ser.readline().decode().strip()
            if line:
                update_db(int(line), diameter, length, coefficient)
                ser.close()
                return False

    except serial.SerialException as se:
        return ("Serial port error:", str(se))

    except KeyboardInterrupt:
        pass

