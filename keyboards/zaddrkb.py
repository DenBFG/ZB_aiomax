import aiomax

def zaddr_main():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Красноярск','addr_krsk'))
    kb.row(aiomax.buttons.CallbackButton('Центральные районы','addr_centr'))
    kb.row(aiomax.buttons.CallbackButton('Западные раойны', 'addr_zapad'))
    kb.row(aiomax.buttons.CallbackButton('Южные районы', 'addr_uzhn'))
    kb.row(aiomax.buttons.CallbackButton('Восточные районы', 'addr_vost'))
    kb.row(aiomax.buttons.CallbackButton('Северные районы', 'addr_sever'))
    kb.row(aiomax.buttons.CallbackButton('Приангарье', 'addr_priang'))
    kb.row(aiomax.buttons.CallbackButton('Арктические районы', 'addr_arkt'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb

def krsk_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Дворец бракосочетания','krsk_dvor'))
    kb.row(aiomax.buttons.CallbackButton('Дом семейных торжеств','krsk_dom'))
    kb.row(aiomax.buttons.CallbackButton('Центральный и Железнодорожный районы', 'krsk_centr_zhd'))
    kb.row(aiomax.buttons.CallbackButton('Кировский и Свердловский районы', 'krsk_kir_sverd'))
    kb.row(aiomax.buttons.CallbackButton('Ленинский район', 'krsk_len'))
    kb.row(aiomax.buttons.CallbackButton('Советский район', 'krsk_sov'))
    kb.row(aiomax.buttons.CallbackButton('Октябрьский район', 'krsk_okt'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb

def centr_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Балахта','centr_bal'))
    kb.row(aiomax.buttons.CallbackButton('Берёзовка','centr_berez'))
    kb.row(aiomax.buttons.CallbackButton('Дивногорск', 'centr_divn'))
    kb.row(aiomax.buttons.CallbackButton('Емельяново', 'centr_emel'))
    kb.row(aiomax.buttons.CallbackButton('Железногорск', 'centr_zhel'))
    kb.row(aiomax.buttons.CallbackButton('Шалинское', 'centr_shal'))
    kb.row(aiomax.buttons.CallbackButton('Сосновоборск', 'centr_sosn'))
    kb.row(aiomax.buttons.CallbackButton('Сухобузимо', 'centr_suh'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb

def zapad_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Ачинск','zap_ach'))
    kb.row(aiomax.buttons.CallbackButton('Новобирилюссы','zap_nbiril'))
    kb.row(aiomax.buttons.CallbackButton('Боготол','zap_bogot'))
    kb.row(aiomax.buttons.CallbackButton('Большой улуй','zap_buluy'))
    kb.row(aiomax.buttons.CallbackButton('Козулька','zap_koz'))
    kb.row(aiomax.buttons.CallbackButton('Назарово','zap_nazar'))
    kb.row(aiomax.buttons.CallbackButton('Новоселево','zap_novos'))
    kb.row(aiomax.buttons.CallbackButton('Тюхтет','zap_tuht'))
    kb.row(aiomax.buttons.CallbackButton('Ужур','zap_uzhur'))
    kb.row(aiomax.buttons.CallbackButton('Шарыпово','zap_shar'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb

def uzhn_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Ермаковское','u_ermak'))
    kb.row(aiomax.buttons.CallbackButton('Идринское','u_idr'))
    kb.row(aiomax.buttons.CallbackButton('Каратузское','u_karat'))
    kb.row(aiomax.buttons.CallbackButton('Краснотуранск', 'u_krasn'))
    kb.row(aiomax.buttons.CallbackButton('Курагино', 'u_kurag'))
    kb.row(aiomax.buttons.CallbackButton('Минусинск', 'u_minus'))
    kb.row(aiomax.buttons.CallbackButton('Шушенское', 'u_shush'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb

def vost_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Абан','v_aban'))
    kb.row(aiomax.buttons.CallbackButton('Дзержинское','v_dzer'))
    kb.row(aiomax.buttons.CallbackButton('Иланский', 'v_ilan'))
    kb.row(aiomax.buttons.CallbackButton('Ирбейское', 'v_irb'))
    kb.row(aiomax.buttons.CallbackButton('Нижний ингаш', 'v_nii'))
    kb.row(aiomax.buttons.CallbackButton('Партизанское', 'v_part'))
    kb.row(aiomax.buttons.CallbackButton('Заозерный', 'v_zaoz'))
    kb.row(aiomax.buttons.CallbackButton('Агинское', 'v_agin'))
    kb.row(aiomax.buttons.CallbackButton('Тасеево', 'v_taseev'))
    kb.row(aiomax.buttons.CallbackButton('Уяр', 'v_uyar'))
    kb.row(aiomax.buttons.CallbackButton('Канск', 'v_kansk'))
    kb.row(aiomax.buttons.CallbackButton('Зеленогорск', 'v_zelen'))
    kb.row(aiomax.buttons.CallbackButton('Бородино', 'v_borod'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb

def sev_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Енисейск','sev_enisk'))
    kb.row(aiomax.buttons.CallbackButton('Казачинское','sev_kazach'))
    kb.row(aiomax.buttons.CallbackButton('Лесосибирск','sev_les'))
    kb.row(aiomax.buttons.CallbackButton('Пировское','sev_pir'))
    kb.row(aiomax.buttons.CallbackButton('Северо-Енисейский','sev_senisk'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb

def priang_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Мотыгино','p_mot'))
    kb.row(aiomax.buttons.CallbackButton('Кодинск','p_kod'))
    kb.row(aiomax.buttons.CallbackButton('Богучаны','p_bog'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb

def ark_kb():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Норильск','ark_nor'))
    kb.row(aiomax.buttons.CallbackButton('Район Кайеркан','ark_kayer'))
    kb.row(aiomax.buttons.CallbackButton('Район Талнах','ark_taln'))
    kb.row(aiomax.buttons.CallbackButton('Туруханский район','ark_tur'))
    kb.row(aiomax.buttons.CallbackButton('Эвенкийский район','ark_evenk'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb
