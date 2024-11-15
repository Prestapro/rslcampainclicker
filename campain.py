import pyautogui
import time
import random

# Coordinates for one-time click
ONE_TIME_COORDINATES = (1113, 607)

# Coordinate for repeated clicks
REPEAT_COORDINATE = (1161, 612)

# Global click counters
one_time_click_counter = 0
repeat_click_counter = 0

# Function to click at specified coordinates and write to console log
def double_click_and_log(coordinates, counter_name):
    global one_time_click_counter, repeat_click_counter
    x, y = coordinates
    
    # Установить фокус перед кликом
    pyautogui.click(x, y)
    time.sleep(0.5)  # Подождать немного, чтобы установился фокус

    # Получить текущие координаты курсора для отладки
    current_x, current_y = pyautogui.position()
    print(f"Cursor moved to ({current_x}, {current_y}) before double click")

    # Выполнить двойной клик
    pyautogui.click(x, y)
    pyautogui.click(x, y)

    if counter_name == 'one_time':
        one_time_click_counter += 1
        print(f"Double clicked at coordinates: ({x}, {y}). One-time click count: {one_time_click_counter}")
    elif counter_name == 'repeat':
        repeat_click_counter += 1
        print(f"Double clicked at coordinates: ({x}, {y}). Repeat click count: {repeat_click_counter}")

# Function to scroll the window to the top
def scroll_to_top():
    start_x, start_y = 808, 177
    end_x, end_y = 639, 151
    
    # Установить фокус
    pyautogui.click(end_x, end_y)
    time.sleep(0.5)  # Подождать немного, чтобы установился фокус
    
    # Прокрутить несколько раз
    for _ in range(6):  # Прокрутить 6 раз
        scroll_vector = (start_x - end_x, start_y - end_y)
        pyautogui.scroll(scroll_vector[1])  # Прокрутка только по вертикали
        time.sleep(0.2)  # Добавить небольшую задержку между прокрутками
    print("Scrolled window to the top")

# Main function
def main():
    global one_time_click_counter, repeat_click_counter
    # Click at one-time coordinates
    double_click_and_log(ONE_TIME_COORDINATES, 'one_time')
    time.sleep(1)  # Задержка между кликами

    # Repeat clicking at the specified coordinates every 10 seconds
    while repeat_click_counter < 80:
        double_click_and_log(REPEAT_COORDINATE, 'repeat')
        time.sleep(random.uniform(2, 4))  # Random delay between 2 and 4 seconds
        
        time.sleep(15)

    # After 12 repetitions, perform additional actions
    if repeat_click_counter == 36:
        # Click at the specified coordinates
        pyautogui.click(850, 77)
        print("Clicked at coordinates: (850, 77)")
        # Scroll window to the top
        scroll_to_top()
        # Click at the specified coordinates
        pyautogui.click(853, 148)
        print("Clicked at coordinates: (853, 148)")

        # Repeat the initial actions 5 more times
        for _ in range(5):
            while repeat_click_counter < 100:
                double_click_and_log(REPEAT_COORDINATE, 'repeat')
                time.sleep(random.uniform(2, 4))  # Random delay between 2 and 4 seconds

            time.sleep(9)

if __name__ == "__main__":
    main()
