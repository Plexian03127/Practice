import os, json, time
import requests
import fn

from assign import HISTORY_FILE
from assign import calculator_base_currency_setting, calculator_target_currency_setting
from assign import COMMAND_LIST, COMMAND_BACK
from assign import CURRENCY_NAMES

calculator_base_currency_setting = fn.find_country_by_input('미국')
calculator_target_currency_setting = fn.find_country_by_input('한국')
calculation_history = []

def display_calculator_main_menu():
    fn.clear_terminal()
    print("======== 환율 계산기 =========")
    print("|                            |")
    print("|  1. 기준 통화 설정         |")
    print("|  2. 환산할 통화 설정       |")
    print("|  3. 환율 계산 하기         |")
    print("|  4. 계산 기록 보기         |")
    print("|  0. 뒤로 가기              |")
    print("|                            |")
    print("==============================")

def set_calculator_base_currency():
    global calculator_base_currency_setting, calculator_target_currency_setting
    previous_base = calculator_base_currency_setting
    while True:
        fn.clear_terminal()
        print("======= 기준 통화 설정 =======")
        if calculator_base_currency_setting:
            current_currency_name = CURRENCY_NAMES.get(calculator_base_currency_setting['currency_code'], "알 수 없는 통화")
            print(f"\n현재 설정: {current_currency_name}({calculator_base_currency_setting['display_name']}/{calculator_base_currency_setting['currency_code']})")
        else:
            print("\n현재 설정된 통화가 없습니다.")
        print("\n==============================")
        print("\n기준이 될 발행 국가 이름, 유통 지역 또는 통화 코드를 입력하세요.")
        print(f"(국가 목록 보기: '{COMMAND_LIST[0]}' 또는 '{COMMAND_LIST[1]}' 입력 | 뒤로 가기: '{COMMAND_BACK[0]}' 또는 '{COMMAND_BACK[1]}' 입력)")
        time.sleep(0.25)
        country_input = input("\n> ").strip()

        if country_input.lower() in COMMAND_LIST:
            fn.display_country_info()
            continue
        elif country_input.lower() in COMMAND_BACK:
            return

        found_country_info = fn.find_country_by_input(country_input.lower())

        fn.clear_terminal()
        print("======= 기준 통화 설정 =======")
        if calculator_base_currency_setting:
            current_currency_name = CURRENCY_NAMES.get(calculator_base_currency_setting['currency_code'], "알 수 없는 통화")
            print(f"\n현재 설정: {current_currency_name}({calculator_base_currency_setting['display_name']}/{calculator_base_currency_setting['currency_code']})")
        else:
            print("\n현재 설정된 통화가 없습니다.")
        print("\n==============================")

        if found_country_info:
            message = ""
            if (calculator_target_currency_setting and 
                found_country_info['currency_code'] == calculator_target_currency_setting['currency_code']):
                if previous_base is not None:
                    calculator_target_currency_setting = previous_base
                    changed_currency_name = CURRENCY_NAMES.get(calculator_target_currency_setting['currency_code'], "알 수 없는 통화")
                    message = f"\n💡 환산할 통화가 기준 통화와 같아 이전 기준 통화인 '{changed_currency_name}'(으)로 자동 변경되었습니다.({calculator_target_currency_setting['display_name']}/{calculator_target_currency_setting['currency_code']})"

            calculator_base_currency_setting = found_country_info
            currency_name = CURRENCY_NAMES.get(calculator_base_currency_setting['currency_code'], "알 수 없는 통화")
            print(f"\n✅ 기준 통화가 '{currency_name}'(으)로 설정되었습니다.({calculator_base_currency_setting['display_name']}/{calculator_base_currency_setting['currency_code']})")
            if message:
                print(message)
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            break
        else:
            print("\n❌ 해당 국가 또는 통화를 찾을 수 없습니다. 다시 입력해 주세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")

def set_calculator_target_currency():
    global calculator_base_currency_setting, calculator_target_currency_setting
    previous_target = calculator_target_currency_setting
    while True:
        fn.clear_terminal()
        print("====== 환산할 통화 설정 ======")
        if calculator_target_currency_setting:
            current_currency_name = CURRENCY_NAMES.get(calculator_target_currency_setting['currency_code'], "알 수 없는 통화")
            print(f"\n현재 설정: {current_currency_name}({calculator_target_currency_setting['display_name']}/{calculator_target_currency_setting['currency_code']})")
        else:
            print("\n현재 설정된 통화가 없습니다.")
        print("\n==============================")
        print("\n환산할 발행 국가 이름, 유통 지역 또는 통화 코드를 입력하세요.")
        print(f"(국가 목록 보기: '{COMMAND_LIST[0]}' 또는 '{COMMAND_LIST[1]}' 입력 | 뒤로 가기: '{COMMAND_BACK[0]}' 또는 '{COMMAND_BACK[1]}' 입력)")
        time.sleep(0.25)
        country_input = input("\n> ").strip()

        if country_input.lower() in COMMAND_LIST:
            fn.display_country_info()
            continue
        elif country_input.lower() in COMMAND_BACK:
            return

        found_country_info = fn.find_country_by_input(country_input.lower())

        fn.clear_terminal()
        print("====== 환산할 통화 설정 ======")
        if calculator_target_currency_setting:
            current_currency_name = CURRENCY_NAMES.get(calculator_target_currency_setting['currency_code'], "알 수 없는 통화")
            print(f"\n현재 설정: {current_currency_name}({calculator_target_currency_setting['display_name']}/{calculator_target_currency_setting['currency_code']})")
        else:
            print("\n현재 설정된 통화가 없습니다.")
        print("\n==============================")

        if found_country_info:
            message = ""
            if (calculator_base_currency_setting and
                found_country_info['currency_code'] == calculator_base_currency_setting['currency_code']):
                if previous_target is not None:
                    calculator_base_currency_setting = previous_target
                    changed_currency_name = CURRENCY_NAMES.get(calculator_base_currency_setting['currency_code'], "알 수 없는 통화")
                    message = f"\n💡 기준 통화가 환산 통화와 같아 이전 환산 통화 '{changed_currency_name}'(으)로 자동 변경되었습니다.({calculator_base_currency_setting['display_name']}/{calculator_base_currency_setting['currency_code']})"

            calculator_target_currency_setting = found_country_info
            currency_name = CURRENCY_NAMES.get(calculator_target_currency_setting['currency_code'], "알 수 없는 통화")
            print(f"\n✅ 환산할 통화가 '{currency_name}'(으)로 설정되었습니다.({calculator_target_currency_setting['display_name']}/{calculator_target_currency_setting['currency_code']})")
            if message:
                print(message)
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            break
        else:
            print("\n❌ 해당 국가 또는 통화를 찾을 수 없습니다. 다시 입력해 주세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")

def perform_currency_calculation():
    global calculation_history
    if calculator_base_currency_setting is None or calculator_target_currency_setting is None:
        fn.clear_terminal()
        display_calculator_main_menu()
        print("\n❗ 기준 통화와 환산할 통화를 먼저 설정해 주세요.")
        time.sleep(0.5)
        input("\n> 확인(Enter)")
        return

    base_currency_code = calculator_base_currency_setting['currency_code']
    target_currency_code = calculator_target_currency_setting['currency_code']

    base_currency_name = CURRENCY_NAMES.get(base_currency_code, "알 수 없는 통화")
    target_currency_name = CURRENCY_NAMES.get(target_currency_code, "알 수 없는 통화")

    while True:
        fn.clear_terminal()
        print("========= 환율  계산 =========")
        print(f"\n기준 통화: {base_currency_name}({calculator_base_currency_setting['display_name']}/{base_currency_code})")
        print(f"환산 통화: {target_currency_name}({calculator_target_currency_setting['display_name']}/{target_currency_code})")
        print("\n==============================")
        print("\n환산할 금액을 입력하세요.(뒤로 가기: 'back' 또는 '/' 입력)")
        time.sleep(0.25)
        amount_input = input("\n> ").strip()

        if amount_input.lower() in COMMAND_BACK:
            return

        try:
            amount = float(amount_input)
            if amount < 0:
                print("\n❗ 금액은 음수가 될 수 없습니다. 다시 입력해 주세요.")
                time.sleep(0.5)
                input("\n> 확인(Enter)")
                continue
        except ValueError:
            print("\n❗ 유효하지 않은 금액입니다. 숫자를 입력해 주세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            continue

        if base_currency_code == target_currency_code:
            fn.clear_terminal()
            print("========= 환율  계산 =========")
            print(f"\n기준 통화와 환산할 통화가 동일합니다: {amount:.2f} {base_currency_name}({base_currency_code})")
            print("\n==============================")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            continue

        exchange_rate = fn.get_exchange_rate(base_currency_code, target_currency_code)

        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            fn.clear_terminal()
            print("========= 환율  계산 =========")
            print(f"\n{amount:.2f} {base_currency_name}({calculator_base_currency_setting['display_name']}/{base_currency_code})")
            print(f"= {converted_amount:.2f} {target_currency_name}({calculator_target_currency_setting['display_name']}/{target_currency_code})")
            print("\n==============================")

            calculation_history.append({
                "base_currency_name": base_currency_name,
                "base_currency_display": calculator_base_currency_setting['display_name'],
                "base_currency_code": base_currency_code,
                "target_currency_name": target_currency_name,
                "target_currency_display": calculator_target_currency_setting['display_name'],
                "target_currency_code": target_currency_code,
                "input_amount": amount,
                "exchange_rate": exchange_rate,
                "converted_amount": converted_amount,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            })

        else:
            fn.clear_terminal()
            print("========= 환율  계산 =========")
            print(f"\n⚠️ '{base_currency_code}'에서 '{target_currency_code}'(으)로의 환율 정보를 가져올 수 없습니다.")
            print("\n==============================")
        time.sleep(0.5)
        input("\n> 확인(Enter)")

def display_calculation_history():
    fn.clear_terminal()
    print("======= 환율 계산 기록 =======")
    if not calculation_history:
        print("\n계산 기록이 없습니다.")
    else:
        for i, record in enumerate(calculation_history, start=1):
            print(f"\n[{i}] {record['timestamp']}")
            print(f"    {record['input_amount']:.2f} {record['base_currency_name']}({record['base_currency_display']}/{record['base_currency_code']})")
            print(f"  → {record['converted_amount']:.2f} {record['target_currency_name']}({record['target_currency_display']}/{record['target_currency_code']})")
            print(f"    (환율: {record['exchange_rate']:.6f})")
    print("\n==============================")
    input("\n> 확인(Enter)")

def currency_calculator_menu():
    while True:
        display_calculator_main_menu()
        print("\n메뉴를 선택하세요.(번호 입력)")
        time.sleep(0.25)
        choice = input("\n> ").strip()

        if choice == '1':
            set_calculator_base_currency()
        elif choice == '2':
            set_calculator_target_currency()
        elif choice == '3':
            perform_currency_calculation()
        elif choice == '4':
            display_calculation_history()
        elif choice in COMMAND_BACK or choice == '0':
            return
        else:
            display_calculator_main_menu()
            print("\n❗ 잘못된 선택입니다. 1-4 또는 0('back' 또는 '/'도 가능) 중 하나를 입력하세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            fn.clear_terminal()
        