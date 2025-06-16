import os, time, sys
import fn
import calc

if os.name == 'nt':  # Windows
    import msvcrt
else:  # Linux / macOS
    import tty
    import termios

def getch():
    while True:
        char = ''
        if os.name == 'nt':
            char_bytes = msvcrt.getch()
            try:
                char = char_bytes.decode('cp949') 
            except UnicodeDecodeError:
                try:
                    char = char_bytes.decode('mbcs')
                except UnicodeDecodeError:
                    char = char_bytes.decode('utf-8', errors='ignore')
        else:  # Linux / macOS
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                char = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        if char.isdigit():
            return char

def display_run():
    fn.clear_terminal()
    print("=== 환율 애플리케이션 실행 ===")
    print("|                            |")
    print("|                            |")
    print("| 애플리케이션을 실행합니다. |")
    print("|                            |")
    print("|                            |")
    print("|                            |")
    print("==============================")

def display_welcome():
    fn.clear_terminal()
    print("=== 환율 애플리케이션 실행 ===")
    print("|                            |")
    print("|                            |")
    print("|        어서오십시오.       |")
    print("|                            |")
    print("|                            |")
    print("|                            |")
    print("==============================")

def display_main_menu():
    fn.clear_terminal()
    print("=== 환율 애플리케이션 메뉴 ===")
    print("|                            |")
    print("|  1. 환율 조회              |")
    print("|  2. 환율 계산기            |")
    print("|  3. 국가 목록 보기         |")
    print("|  0. 종료                   |")
    print("|                            |")
    print("==============================")

def display_stop():
    fn.clear_terminal()
    print("=== 환율 애플리케이션 종료 ===")
    print("|                            |")
    print("|                            |")
    print("| 애플리케이션을 종료합니다. |")
    print("|                            |")
    print("|                            |")
    print("|                            |")
    print("==============================")

def display_thanks():
    fn.clear_terminal()
    print("=== 환율 애플리케이션 종료 ===")
    print("|                            |")
    print("|                            |")
    print("|  이용해 주셔서 감사합니다. |")
    print("|                            |")
    print("|                            |")
    print("|                            |")
    print("==============================")

def main():
    fn.load_user_setting()
    fn.load_favorites()
    while True:
        display_run()
        time.sleep(1)
        display_welcome()
        time.sleep(0.125)
        print("\n계속하려면 아무 숫자 키나 누르세요.")
        char = getch()
        display_main_menu()
        print("\n메뉴를 선택하세요.(번호 입력)")
        char = getch()
        if char.lower() == '1':
            fn.lookup_exchange_rate()
        elif char.lower() == '2':
            calc.currency_calculator_menu()
        elif char.lower() == '3':
            fn.display_country_info()
        elif char.lower() == '0':
            display_stop()
            time.sleep(1)
            display_thanks()
            time.sleep(0.125)
            break
        else:
            display_main_menu()
            print("\n❗ 잘못된 선택입니다. 1 ~ 3 또는 0 중 하나를 선택하세요.")
            start_time = time.time()
            re_input_char = None
            while time.time() - start_time < 2:
                if os.name == 'nt' and msvcrt.kbhit(): # Windows
                    re_input_char = msvcrt.getch().decode('utf-8')
                    break
                elif os.name != 'nt': # Linux/macOS
                    fd = sys.stdin.fileno()
                    old_settings = termios.tcgetattr(fd)
                    try:
                        tty.setraw(sys.stdin.fileno())
                        if sys.stdin in sys.stdin.select([sys.stdin], [], [], 0.01)[0]:
                            re_input_char = sys.stdin.read(1)
                            break
                    finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                time.sleep(0.05)
            if re_input_char:
                if re_input_char.lower() == '1':
                    fn.lookup_exchange_rate()
                elif re_input_char.lower() == '2':
                    calc.currency_calculator_menu()
                elif re_input_char.lower() == '3':
                    fn.display_country_info()
                elif re_input_char.lower() == '0':
                    display_stop()
                    time.sleep(1)
                    display_thanks()
                    time.sleep(0.125)
                    break
                else:
                    continue
            else:
                fn.clear_terminal()

if __name__ == "__main__":
    main()