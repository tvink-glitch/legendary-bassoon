from weather import get_weather


def main():
    print("Програма отримання поточної погоди в Україні")
    city = input("Введіть назву міста: ").strip()

    if not city:
        print("Місто не введено.")
        return

    try:
        weather = get_weather(city)
        print("\nПоточна погода:")
        print(f"Місто: {weather['city']}")
        print(f"Температура: {weather['temperature']} °C")
        print(f"Опис: {weather['description']}")
        print(f"Вологість: {weather['humidity']} %")
        print(f"Швидкість вітру: {weather['wind_speed']} м/с")
    except Exception as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()
