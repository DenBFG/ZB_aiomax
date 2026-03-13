import aiomax

def el_services_keyboard():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Регистрация рождения: заявление','reg_birth_stat'))
    kb.row(aiomax.buttons.CallbackButton('Заключения брака: заявление','reg_marry_stat'))
    kb.row(aiomax.buttons.CallbackButton('Установления отцовства: заявление','reg_dad_stat'))
    kb.row(aiomax.buttons.CallbackButton('Усыновление/Удочерение: заявление','reg_adopt_stat'))
    kb.row(aiomax.buttons.CallbackButton('Расторжения брака: заявление','reg_devorce_stat'))
    kb.row(aiomax.buttons.CallbackButton('Регистрация смерти: заявление','reg_death_stat'))
    kb.row(aiomax.buttons.CallbackButton('Повторные свидетельства: заявление','reg_renew_stat'))
    kb.row(aiomax.buttons.CallbackButton('Апостилирование документов','reg_apost'))
    kb.row(aiomax.buttons.CallbackButton('Чествование юбиляров','reg_anniv'))
    kb.row(aiomax.buttons.CallbackButton('Консультация/Юридическая помощь','reg_consult'))
    kb.row(aiomax.buttons.CallbackButton('Запись на личный прием','reg_priem'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb

def el_zapis_priem():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Руководителю агентства ЗАГС','ruk_zags'))
    kb.row(aiomax.buttons.CallbackButton('Заместителю руководителя агентства ЗАГС','zam_zags'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb