#import aiomax
from keyboards.KBmain import *
from keyboards.questkb import *
from keyboards.serviceskb import *
from keyboards.zaddrkb import *
from DB.ansvars import *
from DB.zaddrvars import *
from DB.mfcaddr import *
from decorators import track_activity

router = aiomax.Router()

@router.on_bot_start()
@track_activity
async def start_bot(ctx: aiomax.BotStartPayload):
    welcome_text = "Вас привествует агентство ЗАГС Красноярского края!\nВыберите интересующий вас вопрос:"
    await ctx.send(welcome_text, keyboard=main_keyboard())

@router.on_command('start')
@track_activity
async def start_command(ctx: aiomax.CommandContext):
    welcome_text = "Вас привествует агентство ЗАГС Красноярского края!\nВыберите интересующий вас вопрос:"
    await ctx.reply(welcome_text, keyboard=main_keyboard())
#----------------------------------------------------------------------------------------------------------------------
# Клавиатура главного меню
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'quest_button')
@track_activity
async def main_quest(cd: aiomax.Callback):
    await cd.answer(
        text="Выберите пункт:",
        keyboard=ans_keyboard()
    )
@router.on_button_callback(lambda data: data.payload == 'el_button')
@track_activity
async def main_el(cd: aiomax.Callback):
    await cd.answer(keyboard=el_services_keyboard())

@router.on_button_callback(lambda data: data.payload == 'zags_addr')
@track_activity
async def main_addr(cd: aiomax.Callback):
    await cd.answer(keyboard=zaddr_main())

@router.on_button_callback(lambda data: data.payload == 'mfc_addr')
@track_activity
async def main_mfc(cd: aiomax.Callback):
    await cd.answer(text=f"{maddr}")

@router.on_button_callback(lambda data: data.payload == 'about')
@track_activity
async def main_about(cd: aiomax.Callback):
    await cd.answer(text='Сайт Агентства ЗАГС:\nzags.krskstate.ru\n\nВконтакте:\nvk.com/zags24\n\nКанал в MAX:\nhttps://max.ru/id2465095400_gos\n\nГорячая линия:\n8-800-200-72-84')

#----------------------------------------------------------------------------------------------------------------------
# Ответы на частозадаваемые вопросы
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'reg_birth')
@track_activity
async def ans_birth(cd: aiomax.Callback):
    await cd.answer(keyboard=birth_keyboard())

@router.on_button_callback(lambda data: data.payload == 'reg_dad')
@track_activity
async def ans_dad(cd: aiomax.Callback):
    await cd.answer(keyboard=dad_keyboard())

@router.on_button_callback(lambda data: data.payload == 'reg_marry')
@track_activity
async def ans_marry(cd: aiomax.Callback):
    await cd.answer(keyboard=marry_keyboard())

@router.on_button_callback(lambda data: data.payload == 'reg_divorce')
@track_activity
async def ans_divorce(cd: aiomax.Callback):
    await cd.answer(keyboard=devorce_keyboard())

@router.on_button_callback(lambda data: data.payload == 'reg_adopt')
@track_activity
async def ans_adopt(cd: aiomax.Callback):
    await cd.answer(text=f"{adopt}")

@router.on_button_callback(lambda data: data.payload == 'reg_nchange')
@track_activity
async def ans_nchange(cd: aiomax.Callback):
    await cd.answer(text=f"{nchange}")

@router.on_button_callback(lambda data: data.payload == 'reg_death')
@track_activity
async def ans_death(cd: aiomax.Callback):
    await cd.answer(text=f"{death}")

@router.on_button_callback(lambda data: data.payload == 'reg_renew')
@track_activity
async def ans_renew(cd: aiomax.Callback):
    await cd.answer(text=f"{povt}")

@router.on_button_callback(lambda data: data.payload == 'reg_change')
@track_activity
async def ans_change(cd: aiomax.Callback):
    await cd.answer(text=f"{isprav}")

#----------------------------------------------------------------------------------------------------------------------
# Регистрация рождения
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'par_mar')
@track_activity
async def par_mar(cd: aiomax.Callback):
    await cd.answer(text=f"{birth_1_1}")

@router.on_button_callback(lambda data: data.payload == 'mother_unmar')
@track_activity
async def mother_unmar(cd: aiomax.Callback):
    await cd.answer(text=f"{birth_1_2}")

@router.on_button_callback(lambda data: data.payload == 'par_unmar')
@track_activity
async def par_unmar(cd: aiomax.Callback):
    await cd.answer(text=f"{birth_1_3}")

#----------------------------------------------------------------------------------------------------------------------
# Установление отцовства
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'dad_sov')
@track_activity
async def dad_sov(cd: aiomax.Callback):
    await cd.answer(text=f"{pat_1_1}")

@router.on_button_callback(lambda data: data.payload == 'dad_unmarry')
@track_activity
async def dad_unmarry(cd: aiomax.Callback):
    await cd.answer(text=f"{pat_1_2}")

@router.on_button_callback(lambda data: data.payload == 'dad_judge')
@track_activity
async def dad_judge(cd: aiomax.Callback):
    await cd.answer(text=f"{pat_1_3}")

#----------------------------------------------------------------------------------------------------------------------
# Заключение брака
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'marry_1_1')
@track_activity
async def marry_rf(cd: aiomax.Callback):
    await cd.answer(text=f"{marry_rf}")

@router.on_button_callback(lambda data: data.payload == 'marry_1_2')
@track_activity
async def marry_nonrf(cd: aiomax.Callback):
    await cd.answer(text=f"{marry_nonrf}")

#----------------------------------------------------------------------------------------------------------------------
# Расторжение брака
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'dev_unchild')
@track_activity
async def dev_unchild(cd: aiomax.Callback):
    await cd.answer(text=f"{devo_1_1}")

@router.on_button_callback(lambda data: data.payload == 'dev_judge')
@track_activity
async def dev_judge(cd: aiomax.Callback):
    await cd.answer(text=f"{devo_1_2}")

@router.on_button_callback(lambda data: data.payload == 'dev_one')
@track_activity
async def dev_one(cd: aiomax.Callback):
    await cd.answer(text=f"{devo_1_3}")

#----------------------------------------------------------------------------------------------------------------------
# Электронные сервисы
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'reg_birth_stat')
@track_activity
async def reg_birth_stat(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка на Госуслуги:\n\nhttps://www.gosuslugi.ru/600370/1/form")

@router.on_button_callback(lambda data: data.payload == 'reg_marry_stat')
@track_activity
async def reg_marry_stat(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка на Госуслуги:\n\nhttps://www.gosuslugi.ru/600105/1/form")

@router.on_button_callback(lambda data: data.payload == 'reg_dad_stat')
@track_activity
async def reg_dad_stat(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка на Госуслуги:\n\nhttps://www.gosuslugi.ru/600678/1/form")

@router.on_button_callback(lambda data: data.payload == 'reg_adopt_stat')
@track_activity
async def reg_adopt_stat(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка на Госуслуги:\n\nhttps://www.gosuslugi.ru/614502/1/form")

@router.on_button_callback(lambda data: data.payload == 'reg_devorce_stat')
@track_activity
async def reg_devorce_stat(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка на Госуслуги:\n\nhttps://www.gosuslugi.ru/600706/1/form")

@router.on_button_callback(lambda data: data.payload == 'reg_death_stat')
@track_activity
async def reg_death_stat(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка на Госуслуги:\n\nhttps://www.gosuslugi.ru/630944/1/form")

@router.on_button_callback(lambda data: data.payload == 'reg_renew_stat')
@track_activity
async def reg_renew_stat(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка на Госуслуги:\n\nhttps://www.gosuslugi.ru/600408/1/form")

@router.on_button_callback(lambda data: data.payload == 'reg_apost')
@track_activity
async def reg_apost(cd: aiomax.Callback):
    await cd.answer(text=f"Запись на апостилирование документов:\n\nhttps://gosuslugi.krskstate.ru/#/shortCard/123456789")

@router.on_button_callback(lambda data: data.payload == 'reg_anniv')
@track_activity
async def reg_anniv(cd: aiomax.Callback):
    await cd.answer(text=f"Запись на чествование юбиляров:\n\nhttps://forms.yandex.ru/cloud/6785e8074936394aad494692")

@router.on_button_callback(lambda data: data.payload == 'reg_consult')
@track_activity
async def reg_consult(cd: aiomax.Callback):
    await cd.answer(text=f"Запись на консультацию:\n\nhttps://gosuslugi.krskstate.ru/#/shortCard/12345678")

@router.on_button_callback(lambda data: data.payload == 'reg_priem')
@track_activity
async def reg_priem(cd: aiomax.Callback):
    await cd.answer(text=f"Запись на прием к...",keyboard=el_zapis_priem())

@router.on_button_callback(lambda data: data.payload == 'ruk_zags')
@track_activity
async def ruk_zags(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка для записи на прием:\n\nhttps://gosuslugi.krskstate.ru/#/shortCard/123456")

@router.on_button_callback(lambda data: data.payload == 'zam_zags')
@track_activity
async def zam_zags(cd: aiomax.Callback):
    await cd.answer(text=f"Ссылка для записи на прием:\n\nhttps://gosuslugi.krskstate.ru/#/shortCard/1234567")

#----------------------------------------------------------------------------------------------------------------------
# Адреса органов ЗАГС
#----------------------------------------------------------------------------------------------------------------------
# Красноярск
#----------------------------------------------------------------------------------------------------------------------
@router.on_button_callback(lambda data: data.payload == 'addr_krsk')
@track_activity
async def addr_krsk(cd: aiomax.Callback):
    await cd.answer(keyboard=krsk_kb())

@router.on_button_callback(lambda data: data.payload == 'krsk_dvor')
@track_activity
async def addr_dvor(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_55}")

@router.on_button_callback(lambda data: data.payload == 'krsk_dom')
@track_activity
async def krsk_dom(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_65}")

@router.on_button_callback(lambda data: data.payload == 'krsk_centr_zhd')
@track_activity
async def krsk_centr_zhd(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_62}")

@router.on_button_callback(lambda data: data.payload == 'krsk_kir_sverd')
@track_activity
async def krsk_kir_sverd(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_57}")

@router.on_button_callback(lambda data: data.payload == 'krsk_len')
@track_activity
async def krsk_len(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_58}")

@router.on_button_callback(lambda data: data.payload == 'krsk_sov')
@track_activity
async def krsk_sov(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_61}")

@router.on_button_callback(lambda data: data.payload == 'krsk_okt')
@track_activity
async def krsk_okt(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_59}")

#----------------------------------------------------------------------------------------------------------------------
# Центральные районы
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'addr_centr')
@track_activity
async def addr_centr(cd: aiomax.Callback):
    await cd.answer(keyboard=centr_kb())

@router.on_button_callback(lambda data: data.payload == 'centr_bal')
@track_activity
async def centr_bal(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_4}")

@router.on_button_callback(lambda data: data.payload == 'centr_berez')
@track_activity
async def centr_berez(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_2}")

@router.on_button_callback(lambda data: data.payload == 'centr_divn')
@track_activity
async def centr_divn(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_12}")

@router.on_button_callback(lambda data: data.payload == 'centr_emel')
@track_activity
async def centr_emel(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_13}")

@router.on_button_callback(lambda data: data.payload == 'centr_zhel')
@track_activity
async def centr_zhel(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_15}")

@router.on_button_callback(lambda data: data.payload == 'centr_shal')
@track_activity
async def centr_shal(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_30}")

@router.on_button_callback(lambda data: data.payload == 'centr_sosn')
@track_activity
async def centr_sosn(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_44}")

@router.on_button_callback(lambda data: data.payload == 'centr_suh')
@track_activity
async def centr_suh(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_45}")

#----------------------------------------------------------------------------------------------------------------------
# Западные районы
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'addr_zapad')
@track_activity
async def addr_zapad(cd: aiomax.Callback):
    await cd.answer(keyboard=zapad_kb())

@router.on_button_callback(lambda data: data.payload == 'zap_ach')
@track_activity
async def zap_ach(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_3}")

@router.on_button_callback(lambda data: data.payload == 'zap_nbiril')
@track_activity
async def zap_nbiril(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_6}")

@router.on_button_callback(lambda data: data.payload == 'zap_bogot')
@track_activity
async def zap_bogot(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_5}")

@router.on_button_callback(lambda data: data.payload == 'zap_buluy')
@track_activity
async def zap_buluy(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_10}")

@router.on_button_callback(lambda data: data.payload == 'zap_koz')
@track_activity
async def zap_koz(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_27}")

@router.on_button_callback(lambda data: data.payload == 'zap_nazar')
@track_activity
async def zap_nazar(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_36}")

@router.on_button_callback(lambda data: data.payload == 'zap_novos')
@track_activity
async def zap_novos(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_35}")

@router.on_button_callback(lambda data: data.payload == 'zap_tuht')
@track_activity
async def zap_tuht(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_48}")

@router.on_button_callback(lambda data: data.payload == 'zap_uzhur')
@track_activity
async def zap_uzhur(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_50}")

@router.on_button_callback(lambda data: data.payload == 'zap_shar')
@track_activity
async def zap_shar(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_52}")

#----------------------------------------------------------------------------------------------------------------------
# Южный район
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'addr_uzhn')
@track_activity
async def zap_shar(cd: aiomax.Callback):
    await cd.answer(keyboard=uzhn_kb())

@router.on_button_callback(lambda data: data.payload == 'u_ermak')
@track_activity
async def u_ermak(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_16}")

@router.on_button_callback(lambda data: data.payload == 'u_idr')
@track_activity
async def u_idr(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_20}")

@router.on_button_callback(lambda data: data.payload == 'u_karat')
@track_activity
async def u_karat(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_24}")

@router.on_button_callback(lambda data: data.payload == 'u_krasn')
@track_activity
async def u_krasn(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_28}")

@router.on_button_callback(lambda data: data.payload == 'u_kurag')
@track_activity
async def u_kurag(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_29}")

@router.on_button_callback(lambda data: data.payload == 'u_minus')
@track_activity
async def u_minus(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_34}")

@router.on_button_callback(lambda data: data.payload == 'u_shush')
@track_activity
async def u_shush(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_51}")

#----------------------------------------------------------------------------------------------------------------------
# Восточный район
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'addr_vost')
@track_activity
async def addr_vost(cd: aiomax.Callback):
    await cd.answer(keyboard=vost_kb())

@router.on_button_callback(lambda data: data.payload == 'v_aban')
@track_activity
async def v_aban(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_1}")

@router.on_button_callback(lambda data: data.payload == 'v_dzer')
@track_activity
async def v_dzer(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_11}")

@router.on_button_callback(lambda data: data.payload == 'v_ilan')
@track_activity
async def v_ilan(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_22}")

@router.on_button_callback(lambda data: data.payload == 'v_irb')
@track_activity
async def v_irb(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_21}")

@router.on_button_callback(lambda data: data.payload == 'v_nii')
@track_activity
async def v_nii(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_33}")

@router.on_button_callback(lambda data: data.payload == 'v_part')
@track_activity
async def v_part(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_40}")

@router.on_button_callback(lambda data: data.payload == 'v_zaoz')
@track_activity
async def v_zaoz(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_17}")

@router.on_button_callback(lambda data: data.payload == 'v_agin')
@track_activity
async def v_agin(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_42}")

@router.on_button_callback(lambda data: data.payload == 'v_taseev')
@track_activity
async def v_taseev(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_46}")

@router.on_button_callback(lambda data: data.payload == 'v_uyar')
@track_activity
async def v_uyar(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_49}")

@router.on_button_callback(lambda data: data.payload == 'v_kansk')
@track_activity
async def v_kansk(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_26}")

@router.on_button_callback(lambda data: data.payload == 'v_zelen')
@track_activity
async def v_zelen(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_18}")

@router.on_button_callback(lambda data: data.payload == 'v_borod')
@track_activity
async def v_borod(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_7}")
#----------------------------------------------------------------------------------------------------------------------
# Северные районы
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'addr_sever')
@track_activity
async def addr_sever(cd: aiomax.Callback):
    await cd.answer(keyboard=sev_kb())

@router.on_button_callback(lambda data: data.payload == 'sev_enisk')
@track_activity
async def sev_enisk(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_14}")

@router.on_button_callback(lambda data: data.payload == 'sev_kazach')
@track_activity
async def sev_kazach(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_23}")

@router.on_button_callback(lambda data: data.payload == 'sev_les')
@track_activity
async def sev_les(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_32}")

@router.on_button_callback(lambda data: data.payload == 'sev_pir')
@track_activity
async def sev_pir(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_41}")

@router.on_button_callback(lambda data: data.payload == 'sev_senisk')
@track_activity
async def sev_senisk(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_43}")

#----------------------------------------------------------------------------------------------------------------------
# Приангарье
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'addr_priang')
@track_activity
async def addr_priang(cd: aiomax.Callback):
    await cd.answer(keyboard=priang_kb())

@router.on_button_callback(lambda data: data.payload == 'p_mot')
@track_activity
async def p_mot(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_31}")

@router.on_button_callback(lambda data: data.payload == 'p_kod')
@track_activity
async def p_kod(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_25}")

@router.on_button_callback(lambda data: data.payload == 'p_bog')
@track_activity
async def p_bog(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_5}")

#----------------------------------------------------------------------------------------------------------------------
# Арктические районы
#----------------------------------------------------------------------------------------------------------------------

@router.on_button_callback(lambda data: data.payload == 'addr_arkt')
@track_activity
async def addr_arkt(cd: aiomax.Callback):
    await cd.answer(keyboard=ark_kb())

@router.on_button_callback(lambda data: data.payload == 'ark_nor')
@track_activity
async def ark_nor(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_38}")

@router.on_button_callback(lambda data: data.payload == 'ark_kayer')
@track_activity
async def ark_kayer(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_39}")

@router.on_button_callback(lambda data: data.payload == 'ark_taln')
@track_activity
async def ark_taln(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_37}")

@router.on_button_callback(lambda data: data.payload == 'ark_tur')
@track_activity
async def ark_tur(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_47}")

@router.on_button_callback(lambda data: data.payload == 'ark_evenk')
@track_activity
async def ark_evenk(cd: aiomax.Callback):
    await cd.answer(text=f"{zags_48}")

#----------------------------------------------------------------------------------------------------------------------
# Хэндлер главного меню
#----------------------------------------------------------------------------------------------------------------------


@router.on_button_callback(lambda data: data.payload == 'to_main')
@track_activity
async def to_main(cd: aiomax.Callback):
    await cd.answer(keyboard=main_keyboard())