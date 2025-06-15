import time
import fn
import calc

def main():
    fn.load_user_setting()
    fn.load_favorites()
    while True:
        fn.display_main_menu()
        print("\n메뉴를 선택하세요.(번호 입력)")
        time.sleep(0.25)
        choice = input("\n> ").strip()
        if choice == '1':
            fn.lookup_exchange_rate()
        elif choice == '2':
            calc.currency_calculator_menu()
        elif choice == '3':
            fn.display_country_info()
        elif choice == '0':
            fn.display_break()
            time.sleep(0.5)
            break
        else:
            fn.display_main_menu()
            print("\n❗ 잘못된 선택입니다. 1 ~ 5 또는 0 중 하나를 입력하세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            fn.clear_terminal()

if __name__ == "__main__":
    main()