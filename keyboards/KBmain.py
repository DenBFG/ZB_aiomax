import aiomax

#----------------------------------------------------------------------------------------------------------------------
# Клавиатура главного меню
#----------------------------------------------------------------------------------------------------------------------

def main_keyboard():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Ответы на частозадаваемые вопросы', 'quest_button'))
    kb.row(aiomax.buttons.CallbackButton('Электронные сервисы', 'el_button'))
    kb.row(aiomax.buttons.CallbackButton('Адреса органов ЗАГС','zags_addr'))
    kb.row(aiomax.buttons.CallbackButton('Адреса МФЦ','mfc_addr'))
    kb.row(aiomax.buttons.CallbackButton('О нас', 'about'))
    return kb
