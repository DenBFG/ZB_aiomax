import aiomax

#----------------------------------------------------------------------------------------------------------------------
# Ответы на частозадаваемы вопросы
#----------------------------------------------------------------------------------------------------------------------

def ans_keyboard():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Регистрация рождения','reg_birth'))
    kb.row(aiomax.buttons.CallbackButton('Установление отцовства','reg_dad'))
    kb.row(aiomax.buttons.CallbackButton('Заключение брака','reg_marry'))
    kb.row(aiomax.buttons.CallbackButton('Расторжение брака','reg_divorce'))
    kb.row(aiomax.buttons.CallbackButton('Регистрация усыновления\удочерения','reg_adopt'))
    kb.row(aiomax.buttons.CallbackButton('Перемена имени','reg_nchange'))
    kb.row(aiomax.buttons.CallbackButton('Регистрация смерти','reg_death'))
    kb.row(aiomax.buttons.CallbackButton('Получение повторного свидетельства','reg_renew'))
    kb.row(aiomax.buttons.CallbackButton('Внесение исправлений и изменений','reg_change'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb

#----------------------------------------------------------------------------------------------------------------------
# Регистрация рождения
#----------------------------------------------------------------------------------------------------------------------

def birth_keyboard():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Родители, состоящие в браке','par_mar'))
    kb.row(aiomax.buttons.CallbackButton('Мать, не состоящая в браке с отцом ребенка','mother_unmar'))
    kb.row(aiomax.buttons.CallbackButton('Родители, не состоящие в браке с установлением отцовства','par_unmar'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню','to_main'))
    return kb

#----------------------------------------------------------------------------------------------------------------------
# Установление отцовства
#----------------------------------------------------------------------------------------------------------------------

def dad_keyboard():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Совместное заявления родителей, не состоящих в браке на момент рождения ребенка', 'dad_sov'))
    kb.row(aiomax.buttons.CallbackButton('Заявление отца ребенка, не состоящего в браке с матерью ребенка', 'dad_unmarry'))
    kb.row(aiomax.buttons.CallbackButton('На основании решения суда', 'dad_judge'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb

#----------------------------------------------------------------------------------------------------------------------
# Заключение брака
#----------------------------------------------------------------------------------------------------------------------

def marry_keyboard():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Заключение брака гражданами РФ', 'marry_rf'))
    kb.row(aiomax.buttons.CallbackButton('Заключение брака с участием иностранного гражданина', 'marry_nonrf'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb

#----------------------------------------------------------------------------------------------------------------------
# Расторжение брака
#----------------------------------------------------------------------------------------------------------------------

def devorce_keyboard():
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Совместное заявление супругов, не имеющих несовершеннолетних детей', 'dev_unchild'))
    kb.row(aiomax.buttons.CallbackButton('На основании решения суда', 'dev_judge'))
    kb.row(aiomax.buttons.CallbackButton('Заявление одного из супругов', 'dev_one'))
    kb.row(aiomax.buttons.CallbackButton('Главное меню', 'to_main'))
    return kb
