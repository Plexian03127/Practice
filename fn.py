import os, json, time
import requests

from assign import USER_SETTINGS_FILE, FAVORITES_FILE
from assign import API_BASE_URL
from assign import user_country_setting, currency_favorites
from assign import COMMAND_LIST, COMMAND_BACK
from assign import COUNTRIES, _OLD_CURRENCY_UNITS_REFERENCE, CURRENCY_UNITS, CURRENCY_NAMES

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_country_by_input(country_input_lower):
    for continent, countries_in_continent in COUNTRIES.items():
        for country_korean_name, country_info in countries_in_continent.items():
            if country_korean_name.lower() == country_input_lower:
                return {'display_name': country_korean_name, 'currency_code': country_info['통화코드']}
            if any(region.lower() == country_input_lower for region in country_info['유통지역']):
                return {'display_name': country_korean_name, 'currency_code': country_info['통화코드']}
            if country_info['통화코드'].lower() == country_input_lower:
                return {'display_name': country_korean_name, 'currency_code': country_info['통화코드']}
    return None

def get_exchange_rate(base_currency, target_currency):
    try:
        response = requests.get(f"{API_BASE_URL}{base_currency}")
        response.raise_for_status()
        data = response.json()
        if data and data['result'] == 'success':
            rates = data['rates']
            if target_currency in rates:
                return rates[target_currency]
            else:
                return None
        else:
            error_message = data.get('error', {}).get('message', '알 수 없는 오류')
            print(f"\n⚠️ API 응답 오류: {error_message}")
            time.sleep(1)
            return None
    except requests.exceptions.RequestException as e:
        print(f"\n⚠️ 네트워크 오류가 발생했습니다. 인터넷 연결을 확인해 주세요.({e})")
        time.sleep(1)
        return None
    except ValueError:
        print("\n⚠️ API 응답을 JSON으로 파싱할 수 없습니다. 응답 형식을 확인해 주세요.")
        time.sleep(1)
        return None

def load_user_setting():
    global user_country_setting
    if os.path.exists(USER_SETTINGS_FILE):
        with open(USER_SETTINGS_FILE, 'r', encoding='utf-8') as f:
            try:
                user_country_setting = json.load(f)
            except json.JSONDecodeError:
                user_country_setting = None
    else:
        user_country_setting = None

def save_user_setting():
    with open(USER_SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_country_setting, f, ensure_ascii=False, indent=4)

def load_favorites():
    global currency_favorites
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, 'r', encoding='utf-8') as f:
            try:
                currency_favorites = json.load(f)
            except json.JSONDecodeError:
                currency_favorites = []
    else:
        currency_favorites = []

def save_favorites():
    with open(FAVORITES_FILE, 'w', encoding='utf-8') as f:
        json.dump(currency_favorites, f, ensure_ascii=False, indent=4)

def display_main_menu():
    clear_terminal()
    print("=== 환율 애플리케이션 메뉴 ===")
    print("|                            |")
    print("|  1. 환율 조회              |")
    print("|  2. 환율 계산기            |")
    print("|  3. 국가 목록 보기         |")
    print("|  0. 종료                   |")
    print("|                            |")
    print("==============================")

def display_exchange_rate_menu():
    clear_terminal()
    print("====== 실시간 환율 조회 ======")
    print("|                            |")
    print("|  1. 직접 검색하여 조회     |")
    print("|  2. 즐겨찾기 통화 조회     |")
    print("|  3. 즐겨찾기 관리          |")
    print("|  4. 사용자 통화 설정       |")
    print("|  0. 뒤로 가기              |")
    print("|                            |")
    print("==============================")

def display_break():
    clear_terminal()
    print("=== 환율 애플리케이션 종료 ===")
    print("|                            |")
    print("| 애플리케이션을 종료합니다. |")
    print("|                            |")
    print("==============================")

def display_currency_setting_menu(title, current_setting):
    clear_terminal()
    print(f"======== {title} ========")
    if current_setting:
        current_currency_name = CURRENCY_NAMES.get(current_setting['currency_code'], "알 수 없는 통화")
        print(f"\n현재 설정: {current_currency_name}({current_setting['display_name']}/{current_setting['currency_code']})")
    else:
        print("\n현재 설정된 통화가 없습니다.")
    print("\n============================")

def display_individual_exchange_rate_menu(user_base_currency_name, user_country_setting, user_base_currency):
    clear_terminal()
    print("======= 개별 환율 조회 =======")
    print(f"\n현재 사용자 통화: {user_base_currency_name}({user_country_setting['display_name']}/{user_base_currency})")
    print("\n==============================")

def display_favorites_management_menu():
    clear_terminal()
    print("======= 즐겨찾기  관리 =======")
    print("|                            |")
    print("|  1. 즐겨찾기 추가          |")
    print("|  2. 즐겨찾기 삭제          |")
    print("|  0. 뒤로 가기              |")
    print("|                            |")
    print("==============================")

def display_add_favorite_menu(print_favorites_list_func):
    clear_terminal()
    print("======= 즐겨찾기  추가 =======")
    print_favorites_list_func()

def display_delete_favorite_menu(print_favorites_list_func):
    clear_terminal()
    print("======= 즐겨찾기  삭제 =======")
    print_favorites_list_func()

def display_country_info():
    clear_terminal()
    print("=== 전체 국가 및 통화 정보 ===")
    time.sleep(0.125)
    for continent, countries_in_continent in COUNTRIES.items():
        print(f"\n### {continent} ###\n")
        time.sleep(0.0625)
        print(f"발행국가 | 통화이름 | 통화코드")
        time.sleep(0.03125)
        counter = 1
        for country_korean_name, country_info in countries_in_continent.items():
            currency_code = country_info['통화코드']
            currency_name = CURRENCY_NAMES.get(currency_code, "알 수 없는 통화")
            print(f"{counter}. {country_korean_name} | {currency_name} | {currency_code}")
            time.sleep(0.015625)
            counter += 1
        print()
        time.sleep(0.125)
    print("==============================")
    time.sleep(0.5)
    input("\n> 확인(Enter)")

def print_favorites_list(title="현재 즐겨찾기에 등록된 통화"):
    print(f"\n# {title} #\n")
    for i, fav in enumerate(currency_favorites):
        currency_name = CURRENCY_NAMES.get(fav['currency_code'], "알 수 없는 통화")
        print(f"{i+1}. {fav['display_name']}({currency_name}/{fav['currency_code']})")
    print("\n==============================")

def set_user_country():
    global user_country_setting
    while True:
        clear_terminal()
        print("====== 사용자 통화 설정 ======")
        if user_country_setting:
            current_currency_name = CURRENCY_NAMES.get(user_country_setting['currency_code'], "알 수 없는 통화")
            print(f"\n현재 설정된 통화: {current_currency_name}({user_country_setting['display_name']}/{user_country_setting['currency_code']})")
        else:
            print("\n현재 설정된 통화가 없습니다.")
        print("\n==============================")
        print("\n발행 국가 이름, 유통 지역 또는 통화 코드를 입력하세요.")
        print(f"(국가 목록 보기: '{COMMAND_LIST[0]}' 또는 '{COMMAND_LIST[1]}' 입력 | 뒤로 가기: '{COMMAND_BACK[0]}' 또는 '{COMMAND_BACK[1]}' 입력)")
        time.sleep(0.25)
        country_input = input("\n> ").strip()
        if country_input.lower() in COMMAND_LIST:
            display_country_info()
            continue
        elif country_input.lower() in COMMAND_BACK:
            return
        found_country_info = find_country_by_input(country_input.lower())
        clear_terminal()
        print("====== 사용자 통화 설정 ======")
        if user_country_setting:
            current_currency_name = CURRENCY_NAMES.get(user_country_setting['currency_code'], "알 수 없는 통화")
            print(f"\n현재 설정된 통화: {current_currency_name}({user_country_setting['display_name']}/{user_country_setting['currency_code']})")
        else:
            print("\n현재 설정된 통화가 없습니다.")
        print("\n==============================")
        if found_country_info:
            user_currency_name = CURRENCY_NAMES.get(found_country_info['currency_code'], "알 수 없는 통화")
            user_country_setting = found_country_info
            save_user_setting()
            print(f"\n✅ 사용자 통화가 '{user_currency_name}'(으)로 설정되었습니다.({user_country_setting['display_name']}/{user_country_setting['currency_code']})")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            break
        else:
            print("\n❌ 해당 국가 또는 통화를 찾을 수 없습니다. 다시 입력해 주세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")

def manage_favorites():
    while True:
        display_favorites_management_menu()
        print("\n메뉴를 선택하세요.(번호 입력)")
        time.sleep(0.25)
        choice = input("\n> ").strip()
        if choice == '1':
            add_to_favorites()
        elif choice == '2':
            remove_from_favorites()
        elif choice in COMMAND_BACK or choice == '0':
            return
        else:
            display_favorites_management_menu()
            print("\n❗ 잘못된 선택입니다. 1, 2 또는 0('back' 또는 '/'도 가능) 중 하나를 입력하세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")

def add_to_favorites():
    while True:
        display_add_favorite_menu(print_favorites_list)
        print("\n즐겨찾기에 추가할 발행 국가 이름, 유통 지역 또는 통화 코드를 입력하세요.")
        print(f"(국가 목록 보기: '{COMMAND_LIST[0]}' 또는 '{COMMAND_LIST[1]}' 입력 | 뒤로 가기: '{COMMAND_BACK[0]}' 또는 '{COMMAND_BACK[1]}' 입력)")
        time.sleep(0.25)
        country_input = input("\n> ").strip()
        if country_input.lower() in COMMAND_LIST:
            display_country_info()
            continue
        elif country_input.lower() in COMMAND_BACK:
            return
        found_country_info = find_country_by_input(country_input.lower())
        display_add_favorite_menu(print_favorites_list)
        if found_country_info:
            if found_country_info not in currency_favorites:
                currency_favorites.append(found_country_info)
                save_favorites()
                currency_name = CURRENCY_NAMES.get(found_country_info['currency_code'], "알 수 없는 통화")
                print(f"\n✅ '{found_country_info['display_name']}'({currency_name}/{found_country_info['currency_code']})이(가) 즐겨찾기에 추가되었습니다.")
                time.sleep(0.5)
                input("\n> 확인(Enter)")
            else:
                currency_name = CURRENCY_NAMES.get(found_country_info['currency_code'], "알 수 없는 통화")
                print(f"\n❗ '{found_country_info['display_name']}'({currency_name}/{found_country_info['currency_code']})은(는) 이미 즐겨찾기에 있습니다.")
                time.sleep(0.5)
                input("\n> 확인(Enter)")
        else:
            print("\n❌ 해당 국가 또는 통화를 찾을 수 없습니다. 다시 입력해 주세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")

def remove_from_favorites():
    while True:
        clear_terminal()
        print("======= 즐겨찾기  삭제 =======")
        if not currency_favorites:
            print("\n삭제할 즐겨찾기 통화가 없습니다.")
            print("\n==============================")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            return
        print_favorites_list()
        print("\n삭제할 통화에 해당하는 번호를 입력하세요.")
        print(f"(뒤로 가기: '{COMMAND_BACK[0]}' 또는 '{COMMAND_BACK[1]}' 입력)")
        time.sleep(0.25)
        choice = input("\n> ").strip()
        if choice.lower() in COMMAND_BACK:
            return
        try:
            index_to_remove = int(choice) - 1
            if 0 <= index_to_remove < len(currency_favorites):
                removed_fav = currency_favorites.pop(index_to_remove)
                save_favorites()
                display_delete_favorite_menu(print_favorites_list)
                currency_name = CURRENCY_NAMES.get(removed_fav['currency_code'], "알 수 없는 통화")
                print(f"\n✅ '{removed_fav['display_name']}'({currency_name}/{removed_fav['currency_code']})이(가) 즐겨찾기에서 삭제되었습니다.")
                time.sleep(0.5)
                input("\n> 확인(Enter)")
            else:
                display_delete_favorite_menu(print_favorites_list)
                print("\n❗ 유효하지 않은 번호입니다. 다시 입력해 주세요.")
                time.sleep(0.5)
                input("\n> 확인(Enter)")
        except ValueError:
            display_delete_favorite_menu(print_favorites_list)
            print("\n❗ 유효하지 않은 입력입니다. 번호를 입력해 주세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")

def lookup_single_currency_rate(user_base_currency, user_base_currency_name):
    while True:
        display_individual_exchange_rate_menu(user_base_currency_name, user_country_setting, user_base_currency)
        print("\n조회할 발행 국가 이름, 유통 지역 또는 통화 코드를 입력하세요.")
        print(f"(국가 목록 보기: '{COMMAND_LIST[0]}' 또는 '{COMMAND_LIST[1]}' 입력 | 뒤로 가기: '{COMMAND_BACK[0]}' 또는 '{COMMAND_BACK[1]}' 입력)")
        time.sleep(0.25)
        target_country_input = input("\n> ").strip()
        if target_country_input.lower() in COMMAND_LIST:
            clear_terminal()
            display_country_info()
            continue
        elif target_country_input.lower() in COMMAND_BACK:
            clear_terminal()
            return
        found_target_country_info = find_country_by_input(target_country_input.lower())
        display_individual_exchange_rate_menu(user_base_currency_name, user_country_setting, user_base_currency)
        if found_target_country_info:
            target_currency = found_target_country_info['currency_code']
            target_country_display_name = found_target_country_info['display_name']
            target_currency_name = CURRENCY_NAMES.get(target_currency, "알 수 없는 통화")
            if target_currency == user_base_currency:
                print("\n❗ 동일한 통화는 조회할 수 없습니다.")
                time.sleep(0.5)
                input("\n> 확인(Enter)")
                continue
            rate_from_target_to_user = get_exchange_rate(target_currency, user_base_currency)
            if rate_from_target_to_user is not None:
                unit_target = CURRENCY_UNITS.get(target_currency, 1)
                display_value = rate_from_target_to_user * unit_target
                clear_terminal()
                print("======= 개별 환율 조회 =======")
                print(f"\n{unit_target} {target_currency_name}({target_country_display_name}/{target_currency}) = {display_value:.2f} {user_base_currency_name}({user_country_setting['display_name']}/{user_base_currency})")
            else:
                print(f"\n⚠️ '{target_country_display_name}'({target_currency})에서 '{user_country_setting['display_name']}'({user_base_currency})(으)로의 환율 정보를 가져올 수 없습니다. 통화 코드 또는 API 응답을 확인해 주세요.")
            print("\n==============================")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
        else:
            print("\n❌ 해당 국가 또는 통화를 찾을 수 없습니다. 다시 입력해 주세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")

def lookup_favorites_exchange_rates(user_base_currency, user_base_currency_name):
    while True:
        clear_terminal()
        print("===== 즐겨찾기 환율 조회 =====\n")
        if not currency_favorites:
            print(" 즐겨찾기에 등록된 통화가 없습니다.")
            print("'즐겨찾기 관리' 메뉴에서 추가해 주세요.")
            print("\n==============================")
            time.sleep(0.5)
            input("\n> 확인(Enter)")
            return
        print(f"기준 통화: {user_base_currency_name}({user_country_setting['display_name']}/{user_base_currency})\n")
        all_rates_fetched = True
        for fav in currency_favorites:
            target_currency = fav['currency_code']
            target_country_display_name = fav['display_name']
            target_currency_name = CURRENCY_NAMES.get(target_currency, "알 수 없는 통화")
            if target_currency == user_base_currency:
                print(f"{target_currency_name}({target_country_display_name}/{target_currency}) = 기준 통화와 동일")
                continue
            rate_from_target_to_user = get_exchange_rate(target_currency, user_base_currency)
            if rate_from_target_to_user is not None:
                unit_target = CURRENCY_UNITS.get(target_currency, 1)
                display_value = rate_from_target_to_user * unit_target
                print(f"{unit_target} {target_currency_name}({target_country_display_name}/{target_currency}) = {display_value:.2f} {user_base_currency_name}({user_country_setting['display_name']}/{user_base_currency})")
            else:
                print(f"⚠️ '{target_country_display_name}'({target_currency}) 환율 정보를 가져올 수 없습니다.")
                all_rates_fetched = False
        print("\n==============================")
        time.sleep(0.5)
        input("\n> 확인(Enter)")
        return

def lookup_exchange_rate():
    if user_country_setting is None:
        display_main_menu()
        print("\n❗ 사용자 통화를 먼저 설정해 주세요.")
        time.sleep(0.5)
        input("\n> 확인(Enter)")
        return
    user_base_currency = user_country_setting['currency_code']
    user_base_currency_name = CURRENCY_NAMES.get(user_base_currency, "알 수 없는 통화")
    while True:
        display_exchange_rate_menu()
        print("\n메뉴를 선택하세요.(번호 입력)")
        time.sleep(0.25)
        choice = input("\n> ").strip()
        if choice == '1':
            lookup_single_currency_rate(user_base_currency, user_base_currency_name)
        elif choice == '2':
            lookup_favorites_exchange_rates(user_base_currency, user_base_currency_name)
        elif choice == '3':
            manage_favorites()
        elif choice == '4':
            set_user_country()
        elif choice in COMMAND_BACK or choice == '0':
            return
        else:
            display_exchange_rate_menu()
            print("\n❗ 잘못된 선택입니다. 1~4 또는 0('back' 또는 '/'도 가능) 중 하나를 입력하세요.")
            time.sleep(0.5)
            input("\n> 확인(Enter)")