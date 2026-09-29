# -*- coding: utf-8 -*-
"""
All site copy lives here, split by language.
Add a language by copying one whole dict and translating the values;
the templates just look up TRANSLATIONS[lang][...] so nothing else needs to change.
"""

TRANSLATIONS = {

    "en": {
        "lang_label": "EN",
        "nav": {
            "concept": "Concept", "route": "Route", "itinerary": "Itinerary",
            "villages": "Villages", "practical": "Practical",
            "enquire": "Enquire", "register_host": "Register as a host family",
        },
        "hero": {
            "eyebrow": "Mangystau Region, Kazakhstan · 4 days / 3 nights",
            "title_1": "Cross a fossil sea.",
            "title_2_pre": "Sleep in ", "title_2_em": "living", "title_2_post": " villages.",
            "sub": "A small-group journey through Mangystau's Mars-like canyons and out to the aouls "
                   "where the steppe is still home — not a stage. Bozzhyra, Sherkala, the underground "
                   "shrine of Beket-Ata, and three nights hosted by the families who actually live here.",
            "meta": [
                ("4 days", "Aktau to Aktau, looped"),
                ("3 nights", "Yurt · desert camp · homestay"),
                ("6–10", "Guests per departure"),
                ("Mar–Jun / Sep–Oct", "Best seasons"),
            ],
        },
        "concept": {
            "p1": "Most Mangystau tours sell you the same six viewpoints — Bozzhyra at sunset, the "
                  "underground mosques, a jeep, a photo. Ata Joly is built around the part nobody else "
                  "stops for: the aouls along the way, where Kazakh nomadic life hasn't been repackaged "
                  "for visitors.",
            "p2": "You still get Bozzhyra. You still get the salt canyons and the shell-white plains of "
                  "an ocean that dried up five million years ago. But two of your three nights are spent "
                  "with families, not in a hotel — eating what they cook, hearing what they know, and "
                  "paying them directly for it.",
            "points": [
                ("Not a spectacle", "No staged \u201cnomad shows.\u201d Homestays are arranged directly "
                                     "with families who choose to host, at rates they set."),
                ("Small groups only", "Six to ten guests, two vehicles. Villages absorb a handful of "
                                        "visitors far better than a busload."),
                ("Guided by locals", "Your route guide is Mangystau-born. English-speaking, and the one "
                                      "translating between you and your hosts."),
            ],
        },
        "route": {
            "heading": "Four days, one loop",
            "sub": "Out from Aktau along the northern escarpment, across the Ustyurt plateau to "
                   "Bozzhyra, back through the shrine route, home along the coast.",
            "stops": [
                ("Day 1", "Shetpe \u2192 Kogez", "Karagie depression, Sherkala, ethno-aoul"),
                ("Day 2", "Bozzhyra", "Airakty canyons, Torysh sphere field, desert camp"),
                ("Day 3", "Beket-Ata \u2192 aoul", "Shopan-Ata, underground shrine, family homestay"),
                ("Day 4", "Tuzbair \u2192 Aktau", "Caspian chalk cliffs, coast, return"),
            ],
        },
        "itinerary": {
            "heading": "Day by day",
            "sub": "Times are approximate and adjust to light, weather and the group's pace.",
            "days": [
                {
                    "num": "01", "title": "Shetpe & the ethno-aoul of Kogez",
                    "tag": "Karagie depression · Sherkala · yurt night",
                    "gradient": "grad-1",
                    "schedule": [
                        ("08:00", "Depart Aktau by 4x4."),
                        ("09:30", "Stop at the <strong>Karagie depression</strong>, one of the deepest dry basins on Earth."),
                        ("12:00", "Lunch in Shetpe, a local kitchen, not a tourist buffet."),
                        ("14:00", "Walk the base of <strong>Sherkala</strong>, the lone \u201cheart-shaped\u201d mountain."),
                        ("17:00", "Arrive at the Kogez ethno-aoul. Settle into yurts."),
                        ("18:30", "Hands-on: raising a yurt frame, felt-making basics."),
                        ("20:00", "Dinner and an evening of dombra music and steppe stories."),
                    ],
                    "overnight": None,
                },
                {
                    "num": "02", "title": "Into the Ustyurt \u2014 Bozzhyra",
                    "tag": "Airakty canyons · Torysh spheres · night sky",
                    "gradient": "grad-2",
                    "schedule": [
                        ("07:00", "Breakfast, depart early to beat the heat."),
                        ("09:00", "Hike the <strong>Airakty-Shomanay</strong> canyons \u2014 carved rock and ancient geoglyphs."),
                        ("11:30", "<strong>Torysh</strong>, the valley of stone spheres."),
                        ("13:00", "Packed lunch on the road."),
                        ("16:00", "Arrive Bozzhyra, set up desert camp."),
                        ("18:00", "Climb to the viewpoint for sunset over the \u201cfangs\u201d of Bozzhyra."),
                        ("21:00", "Campfire dinner; a short guided look at the night sky."),
                    ],
                    "overnight": "Overnight: tents / desert camp at Bozzhyra.",
                },
                {
                    "num": "03", "title": "Shopan-Ata, Beket-Ata & a family aoul",
                    "tag": "Underground shrines · homestay · home-cooked dinner",
                    "gradient": "grad-3",
                    "schedule": [
                        ("06:00", "Sunrise at Bozzhyra."),
                        ("08:00", "Breakfast, break camp."),
                        ("11:00", "Visit the underground mosque of <strong>Shopan-Ata</strong>."),
                        ("14:00", "Visit <strong>Beket-Ata</strong> at Oglandy, the region's most sacred underground shrine."),
                        ("17:00", "Arrive at a nearby aoul. Check into a real family guesthouse."),
                        ("19:00", "Dinner cooked by your hosts \u2014 beshbarmak, kurt, kumys or shubat."),
                        ("20:30", "Open conversation over tea \u2014 ask your hosts about daily life, no script."),
                    ],
                    "overnight": "Overnight: family homestay, paid directly to the household.",
                },
                {
                    "num": "04", "title": "Tuzbair & the Caspian coast",
                    "tag": "Chalk cliffs · beach · return to Aktau",
                    "gradient": "grad-4",
                    "schedule": [
                        ("08:00", "Breakfast with the family, farewells."),
                        ("09:30", "Stop at <strong>Tuzbair</strong> \u2014 white chalk cliffs meeting the Caspian Sea."),
                        ("13:00", "Lunch on the coast."),
                        ("15:00", "Free time on the beach."),
                        ("17:00", "Drive back to Aktau."),
                        ("19:00", "Arrive Aktau. Tour ends."),
                    ],
                    "overnight": None,
                },
            ],
        },
        "villages": {
            "heading": "Where the money actually goes",
            "sub": "Two of three nights are spent in aouls. Here's the split for those nights, per guest.",
            "cards": [
                ("45%", "To the host family", "Covers the room, the meals they cook, and their time — paid directly, not through a middleman."),
                ("20%", "Community fund", "Pooled across all Ata Joly guests and put toward something the aoul chooses."),
                ("35%", "Guide, vehicles, permits", "Driver-guides, 4x4 upkeep and fuel, reserve entry permits, and camp equipment."),
            ],
        },
        "highlights": {
            "heading": "What you'll see",
            "sub": "A handful of the moments the route is built around.",
            "cards": [
                ("grad-h1", "Bozzhyra's fangs at sunset"),
                ("grad-h2", "Sherkala at dusk"),
                ("grad-h3", "Ustyurt night sky"),
                ("grad-h4", "Torysh sphere field"),
            ],
        },
        "practical": {
            "heading": "Before you go",
            "rows": [
                ("Fitness", "Moderate. Uneven terrain, one steep climb at Bozzhyra, no technical climbing."),
                ("Facilities", "Basic. Camp night has a field toilet; aoul homestays have simple but real facilities."),
                ("Language", "Your route guide speaks English. Kazakh and Russian are the local languages in the aouls."),
                ("Weather", "Spring and autumn only. Summer heat exceeds 40°C on the plateau."),
            ],
        },
        "cta": {
            "heading": "Four days. Two families. One landscape nobody else shows you like this.",
            "button": "Enquire about dates",
        },
        "footer": {
            "left": "Ata Joly · Mangystau Region, Kazakhstan",
            "right": "School project concept · not an operating booking service",
        },
        "register": {
            "eyebrow": "For aoul families",
            "heading": "Host travellers in your home",
            "sub": "Ata Joly pays host families directly for a room, home-cooked meals and an evening "
                   "of conversation. Fill in the form below and our route guide will contact you before "
                   "adding your household to the route.",
            "field_family_name": "Family / host name",
            "field_aoul": "Aoul (village) name",
            "field_phone": "Phone number",
            "field_guests": "How many guests can you host at once?",
            "field_rooms": "Describe the room(s) you can offer",
            "field_meals": "What meals can you cook for guests?",
            "field_extra": "Anything else worth knowing (crafts, animals, activities)?",
            "field_consent": "I agree to be contacted about hosting Ata Joly guests.",
            "submit": "Submit registration",
            "success": "Thank you — your registration was received. Our route guide will call you soon.",
            "back_home": "Back to the tour page",
            "view_list": "View registered host families",
        },
        "booking": {
            "eyebrow": "Book your spot",
            "heading": "Apply for the tour",
            "sub": "Leave your details and our route guide will confirm the exact departure "
                   "date with you. This is a request to join, not an automatic payment.",
            "price_per_day": "55,000 ₸",
            "price_per_day_label": "per person, per day",
            "price_total": "220,000 ₸",
            "price_total_label": "per person, full 4-day tour",
            "price_note": "Covers accommodation, meals, guiding, transport and the interactive "
                           "activities. See the cost breakdown for where the money goes.",
            "capacity_label": "Group size for the next departure",
            "spots_left": "{left} of {total} spots left",
            "spots_full": "This departure is full — you can still apply and we'll offer you the next one.",
            "field_name": "Full name",
            "field_contact": "Phone or email",
            "field_people": "Number of people",
            "field_date": "Preferred departure date",
            "field_message": "Anything we should know (dietary needs, language, etc.)",
            "submit": "Send application",
            "success": "Thank you — your application was received. We'll contact you to confirm dates and payment.",
            "back_home": "Back to the tour page",
        },
        "dates": {
            "eyebrow": "Upcoming journeys",
            "heading": "Planned tour dates",
            "intro": "Proposed four-day departures in spring and autumn. Pick a date to send an application.",
            "planned": "Planned · subject to confirmation",
            "duration": "4 days · Aktau to Aktau",
            "apply": "Apply for this date",
            "note": "These departures are proposals, not confirmed tours. We are not showing a guest count until applications can be stored reliably.",
            "empty": "No upcoming dates are available yet. Please check back later.",
            "choose": "Select a departure",
            "back": "All planned dates",
            "invalid_error": "Please enter your name, contact, group size and one of the available dates.",
        },
    },

    "ru": {
        "lang_label": "RU",
        "nav": {
            "concept": "Концепция", "route": "Маршрут", "itinerary": "По дням",
            "villages": "Аулы", "practical": "Важное",
            "enquire": "Записаться", "register_host": "Регистрация семьи-хозяина",
        },
        "hero": {
            "eyebrow": "Мангистауская область, Казахстан · 4 дня / 3 ночи",
            "title_1": "Пересеки древнее морское дно.",
            "title_2_pre": "Переночуй в ", "title_2_em": "настоящих", "title_2_post": " аулах.",
            "sub": "Групповое путешествие небольшой группой через марсианские каньоны Мангистау и в аулы, "
                   "где степной быт до сих пор жив, а не разыгран для гостей. Бозжыра, Шеркала, подземная "
                   "мечеть Бекет-ата и три ночи в гостях у семей, которые здесь действительно живут.",
            "meta": [
                ("4 дня", "Маршрут из Актау в Актау"),
                ("3 ночи", "Юрта · лагерь в пустыне · гостевой дом"),
                ("6–10", "гостей на группу"),
                ("март–июнь / сен–окт", "лучшие сезоны"),
            ],
        },
        "concept": {
            "p1": "Большинство туров по Мангистау продают одни и те же шесть точек — закат на Бозжыре, "
                  "подземные мечети, джип, фото. Ata Joly построен вокруг того, что никто не показывает: "
                  "аулы по пути, где кочевой быт казахов не превращён в шоу для туристов.",
            "p2": "Бозжыра всё ещё есть. Солевые каньоны и белые как ракушки равнины древнего океана, "
                  "высохшего пять миллионов лет назад, — тоже. Но две из трёх ночей вы проведёте у семей, "
                  "а не в отеле — едите то, что готовят они, слушаете то, что знают они, и платите им "
                  "напрямую.",
            "points": [
                ("Не спектакль", "Никаких постановочных «шоу кочевников». Ночлег организуется напрямую с "
                                  "семьями, которые сами решили принимать гостей, по своим расценкам."),
                ("Только маленькие группы", "От шести до десяти гостей, два внедорожника. Аул выдерживает "
                                             "горстку туристов куда лучше, чем автобус."),
                ("Гид — местный", "Ваш гид родился в Мангистау. Говорит по-английски и переводит между "
                                   "вами и хозяевами."),
            ],
        },
        "route": {
            "heading": "Четыре дня, одно кольцо",
            "sub": "Из Актау вдоль северного чинка, через плато Устюрт к Бозжыре, обратно через "
                   "маршрут святынь, домой вдоль побережья.",
            "stops": [
                ("День 1", "Шетпе \u2192 Когез", "Впадина Карагие, Шеркала, этноаул"),
                ("День 2", "Бозжыра", "Каньоны Айракты, поле шаров Торыш, лагерь в пустыне"),
                ("День 3", "Бекет-ата \u2192 аул", "Шопан-ата, подземная мечеть, гостевой дом"),
                ("День 4", "Тузбаир \u2192 Актау", "Меловые скалы Каспия, побережье, возвращение"),
            ],
        },
        "itinerary": {
            "heading": "По дням",
            "sub": "Время примерное и подстраивается под свет, погоду и темп группы.",
            "days": [
                {
                    "num": "01", "title": "Шетпе и этноаул Когез",
                    "tag": "Впадина Карагие · Шеркала · ночь в юрте",
                    "gradient": "grad-1",
                    "schedule": [
                        ("08:00", "Выезд из Актау на внедорожниках."),
                        ("09:30", "Остановка у <strong>впадины Карагие</strong> — одной из самых глубоких сухих впадин на Земле."),
                        ("12:00", "Обед в Шетпе, в местной кухне, а не в туристической столовой."),
                        ("14:00", "Прогулка у подножья <strong>Шеркалы</strong> — горы в форме сердца."),
                        ("17:00", "Прибытие в этноаул Когез. Заселение в юрты."),
                        ("18:30", "Мастер-класс: установка каркаса юрты, основы валяния войлока."),
                        ("20:00", "Ужин и вечер с домброй и степными легендами."),
                    ],
                    "overnight": None,
                },
                {
                    "num": "02", "title": "На Устюрт \u2014 Бозжыра",
                    "tag": "Каньоны Айракты · шары Торыш · ночное небо",
                    "gradient": "grad-2",
                    "schedule": [
                        ("07:00", "Завтрак, ранний выезд, пока не жарко."),
                        ("09:00", "Каньоны <strong>Айракты-Шоманай</strong> — резной рельеф и древние геоглифы."),
                        ("11:30", "<strong>Торыш</strong>, долина каменных шаров."),
                        ("13:00", "Обед в пути."),
                        ("16:00", "Прибытие в район Бозжыры, разбивка лагеря."),
                        ("18:00", "Подъём на смотровую к закату над «клыками» Бозжыры."),
                        ("21:00", "Ужин у костра; короткий рассказ о ночном небе."),
                    ],
                    "overnight": "Ночёвка: палатки / лагерь в пустыне у Бозжыры.",
                },
                {
                    "num": "03", "title": "Шопан-ата, Бекет-ата и аул",
                    "tag": "Подземные мечети · гостевой дом · домашний ужин",
                    "gradient": "grad-3",
                    "schedule": [
                        ("06:00", "Рассвет на Бозжыре."),
                        ("08:00", "Завтрак, сбор лагеря."),
                        ("11:00", "Подземная мечеть <strong>Шопан-ата</strong>."),
                        ("14:00", "<strong>Бекет-ата</strong> в Огланды — главная святыня региона."),
                        ("17:00", "Прибытие в ближайший аул. Заселение в настоящий гостевой дом."),
                        ("19:00", "Ужин от хозяев — бешбармак, курт, кумыс или шубат."),
                        ("20:30", "Свободный разговор за чаем — вопросы о быте, без сценария."),
                    ],
                    "overnight": "Ночёвка: гостевой дом, оплата напрямую семье.",
                },
                {
                    "num": "04", "title": "Тузбаир и побережье Каспия",
                    "tag": "Меловые скалы · пляж · возвращение в Актау",
                    "gradient": "grad-4",
                    "schedule": [
                        ("08:00", "Завтрак с семьёй, прощание."),
                        ("09:30", "Остановка у <strong>Тузбаира</strong> — белые меловые скалы у Каспия."),
                        ("13:00", "Обед на побережье."),
                        ("15:00", "Свободное время на пляже."),
                        ("17:00", "Выезд в Актау."),
                        ("19:00", "Прибытие в Актау. Конец тура."),
                    ],
                    "overnight": None,
                },
            ],
        },
        "villages": {
            "heading": "Куда реально идут деньги",
            "sub": "Две из трёх ночей — в аулах. Вот распределение за эти ночи, с одного гостя.",
            "cards": [
                ("45%", "Семье-хозяину", "Комната, домашняя еда и время хозяев — оплата напрямую, без посредников."),
                ("20%", "Общий фонд аула", "Собирается со всех гостей Ata Joly и идёт на то, что выберет сам аул."),
                ("35%", "Гид, транспорт, разрешения", "Гиды-водители, обслуживание и топливо внедорожников, пропуска, снаряжение лагеря."),
            ],
        },
        "highlights": {
            "heading": "Что вы увидите",
            "sub": "Несколько моментов, вокруг которых построен маршрут.",
            "cards": [
                ("grad-h1", "Клыки Бозжыры на закате"),
                ("grad-h2", "Шеркала в сумерках"),
                ("grad-h3", "Ночное небо Устюрта"),
                ("grad-h4", "Поле шаров Торыш"),
            ],
        },
        "practical": {
            "heading": "Перед поездкой",
            "rows": [
                ("Физподготовка", "Умеренная. Неровный рельеф, один крутой подъём на Бозжыре, без техническего лазания."),
                ("Условия", "Базовые. В лагере — полевой туалет; в аулах — простые, но настоящие удобства."),
                ("Язык", "Гид говорит по-английски. В аулах говорят на казахском и русском."),
                ("Погода", "Только весна и осень. Летом на плато жара выше 40°C."),
            ],
        },
        "cta": {
            "heading": "Четыре дня. Две семьи. Пейзаж, который никто не показывает так, как мы.",
            "button": "Узнать даты",
        },
        "footer": {
            "left": "Ata Joly · Мангистауская область, Казахстан",
            "right": "Концепция школьного проекта · не является действующим сервисом бронирования",
        },
        "register": {
            "eyebrow": "Для семей из аулов",
            "heading": "Принимайте туристов у себя дома",
            "sub": "Ata Joly платит семьям-хозяевам напрямую за комнату, домашнюю еду и вечер общения. "
                   "Заполните форму — наш гид свяжется с вами перед тем, как добавить ваш дом в маршрут.",
            "field_family_name": "Имя семьи / хозяина",
            "field_aoul": "Название аула",
            "field_phone": "Номер телефона",
            "field_guests": "Сколько гостей можете принять одновременно?",
            "field_rooms": "Опишите комнату(ы), которые можете предложить",
            "field_meals": "Какие блюда можете готовить для гостей?",
            "field_extra": "Что ещё стоит знать (ремёсла, животные, занятия)?",
            "field_consent": "Согласен(на), чтобы со мной связались по поводу приёма гостей Ata Joly.",
            "submit": "Отправить заявку",
            "success": "Спасибо — заявка принята. Наш гид скоро вам позвонит.",
            "back_home": "Вернуться на страницу тура",
            "view_list": "Посмотреть зарегистрированные семьи",
        },
        "booking": {
            "eyebrow": "Забронировать место",
            "heading": "Оставить заявку на тур",
            "sub": "Оставьте контакты — наш гид свяжется с вами и подтвердит точную дату "
                   "выезда. Это заявка на участие, а не автоматическая оплата.",
            "price_per_day": "55 000 ₸",
            "price_per_day_label": "с человека, за один день",
            "price_total": "220 000 ₸",
            "price_total_label": "с человека, весь тур (4 дня)",
            "price_note": "Включает проживание, питание, гида, транспорт и интерактивные "
                           "активности. Подробное распределение — на слайде «Стоимость».",
            "capacity_label": "Размер группы на ближайший выезд",
            "spots_left": "Осталось мест: {left} из {total}",
            "spots_full": "На этот выезд мест нет — можно подать заявку на следующую дату.",
            "field_name": "Имя и фамилия",
            "field_contact": "Телефон или email",
            "field_people": "Количество человек",
            "field_date": "Предпочитаемая дата выезда",
            "field_message": "Что нам стоит знать (диета, язык и т.д.)",
            "submit": "Отправить заявку",
            "success": "Спасибо — заявка принята. Мы свяжемся с вами для подтверждения дат и оплаты.",
            "back_home": "Вернуться на страницу тура",
        },
        "dates": {
            "eyebrow": "Ближайшие поездки",
            "heading": "Планируемые даты туров",
            "intro": "Предлагаем четырёхдневные выезды весной и осенью. Выберите дату, чтобы оставить заявку.",
            "planned": "Планируется · дата требует подтверждения",
            "duration": "4 дня · из Актау и обратно",
            "apply": "Оставить заявку",
            "note": "Это планируемые, а не подтверждённые туры. Число участников пока не показываем: сначала нужно обеспечить надёжное хранение заявок.",
            "empty": "Предстоящих дат пока нет. Загляните позже.",
            "choose": "Выберите дату выезда",
            "back": "Все планируемые даты",
            "invalid_error": "Укажите имя, контакт, число участников и одну из доступных дат.",
        },
    },

    "kk": {
        "lang_label": "KZ",
        "nav": {
            "concept": "Тұжырымдама", "route": "Бағыт", "itinerary": "Күн сайын",
            "villages": "Ауылдар", "practical": "Маңызды ақпарат",
            "enquire": "Жазылу", "register_host": "Отбасы тіркеу",
        },
        "hero": {
            "eyebrow": "Маңғыстау облысы, Қазақстан · 4 күн / 3 түн",
            "title_1": "Ежелгі теңіз түбін кесіп өт.",
            "title_2_pre": "", "title_2_em": "Өмір сүріп жатқан", "title_2_post": " ауылдарда түнеп шық.",
            "sub": "Маңғыстаудың марсқа ұқсас каньондары арқылы және дала өмірі әлі де шынайы сақталған "
                   "ауылдарға баратын шағын топтық сапар. Бозжыра, Шеркала, Бекет-ата жерасты мешіті "
                   "және осында тұратын отбасылардың қонағында өтетін үш түн.",
            "meta": [
                ("4 күн", "Ақтаудан Ақтауға дейін"),
                ("3 түн", "Киіз үй · шөл лагері · қонақ үй"),
                ("6–10", "топтағы қонақ саны"),
                ("наурыз–маусым / қыркүйек–қазан", "ең қолайлы мезгіл"),
            ],
        },
        "concept": {
            "p1": "Маңғыстау бойынша турлардың көбі бір-біріне ұқсас алты нүктені сатады — Бозжырадағы "
                  "күн батысы, жерасты мешіттер, джип, фото. Ata Joly ешкім тоқтамайтын бөлікке "
                  "негізделген: жол бойындағы ауылдарға, мұнда қазақтың көшпелі өмірі туристерге "
                  "арнап қайта құрылмаған.",
            "p2": "Бозжыра да бар. Тұзды каньондар мен бес миллион жыл бұрын кепкен теңіздің ақ "
                  "жазықтары да бар. Бірақ үш түннің екеуін сіз қонақ үйде емес, отбасыларда өткізесіз — "
                  "олар пісірген тағамды жеп, олардың білетінін тыңдап, ақыны тікелей соларға төлейсіз.",
            "points": [
                ("Ойын-сауық емес", "Қойылған «көшпенді шоулары» жоқ. Түнеу қонуды өздері шешкен "
                                     "отбасылармен, солар белгілеген бағамен тікелей келісеміз."),
                ("Тек шағын топтар", "Алты-он қонақ, екі көлік. Ауыл автобус толы туристен гөрі "
                                      "аз топты әлдеқайда жақсы қабылдайды."),
                ("Жергілікті гид", "Сіздің гидіңіз — Маңғыстауда туған адам. Ағылшынша сөйлейді және "
                                    "сізбен үй иелерінің арасында аудармашы болады."),
            ],
        },
        "route": {
            "heading": "Төрт күн, бір шеңбер",
            "sub": "Ақтаудан солтүстік шыңқыр бойымен, Үстірт үстіртінен Бозжыраға дейін, содан "
                   "кейін киелі орындар бағытымен, жағалау бойымен үйге қарай.",
            "stops": [
                ("1-күн", "Шетпе \u2192 Көгез", "Қарағия ойпаты, Шеркала, этноауыл"),
                ("2-күн", "Бозжыра", "Айрақты каньондары, Торыш шарлары, шөл лагері"),
                ("3-күн", "Бекет-ата \u2192 ауыл", "Шопан-ата, жерасты мешіті, қонақ үй"),
                ("4-күн", "Тұзбайыр \u2192 Ақтау", "Каспий бор жарлары, жағалау, қайту"),
            ],
        },
        "itinerary": {
            "heading": "Күн сайынғы жоспар",
            "sub": "Уақыт болжамды және жарыққа, ауа-райына, топтың қарқынына қарай өзгереді.",
            "days": [
                {
                    "num": "01", "title": "Шетпе және Көгез этноауылы",
                    "tag": "Қарағия ойпаты · Шеркала · киіз үйде түн",
                    "gradient": "grad-1",
                    "schedule": [
                        ("08:00", "Ақтаудан жол-көлікпен шығу."),
                        ("09:30", "<strong>Қарағия ойпаты</strong> — жердегі ең терең құрғақ ойпаттардың бірі."),
                        ("12:00", "Шетпеде түскі ас, жергілікті асхана."),
                        ("14:00", "<strong>Шеркала</strong> табанында серуен — жүрек тәрізді тау."),
                        ("17:00", "Көгез этноауылына келу. Киіз үйге орналасу."),
                        ("18:30", "Шеберлік сабағы: киіз үй қаңқасын құрастыру, ұйықты басу негіздері."),
                        ("20:00", "Кешкі ас, домбыра және дала әңгімелерімен кеш."),
                    ],
                    "overnight": None,
                },
                {
                    "num": "02", "title": "Үстіртке \u2014 Бозжыраға",
                    "tag": "Айрақты каньондары · Торыш шарлары · түнгі аспан",
                    "gradient": "grad-2",
                    "schedule": [
                        ("07:00", "Таңғы ас, ыстықтан бұрын ерте шығу."),
                        ("09:00", "<strong>Айрақты-Шоманай</strong> каньондары — ежелгі геоглифтер."),
                        ("11:30", "<strong>Торыш</strong> — тас шарлар аңғары."),
                        ("13:00", "Жолда түскі ас."),
                        ("16:00", "Бозжыраға келу, шөл лагерін құру."),
                        ("18:00", "Бозжыраның «азу тістеріне» күн батысын көру үшін көру алаңына көтерілу."),
                        ("21:00", "От басында кешкі ас; түнгі аспан туралы қысқа әңгіме."),
                    ],
                    "overnight": "Түнеу: шатыр / Бозжырадағы шөл лагері.",
                },
                {
                    "num": "03", "title": "Шопан-ата, Бекет-ата және ауыл",
                    "tag": "Жерасты мешіттер · қонақ үй · үй тағамы",
                    "gradient": "grad-3",
                    "schedule": [
                        ("06:00", "Бозжырада күннің шығуы."),
                        ("08:00", "Таңғы ас, лагерді жинау."),
                        ("11:00", "<strong>Шопан-ата</strong> жерасты мешітіне бару."),
                        ("14:00", "Оғланды жеріндегі <strong>Бекет-ата</strong> — өңірдің басты киелі орны."),
                        ("17:00", "Жақын маңдағы ауылға келу. Нағыз отбасылық қонақ үйге орналасу."),
                        ("19:00", "Үй иелері дайындаған кешкі ас — бешбармақ, құрт, қымыз немесе шұбат."),
                        ("20:30", "Шай үстінде еркін әңгіме — күнделікті өмір туралы сұрақтар."),
                    ],
                    "overnight": "Түнеу: отбасылық қонақ үй, ақы тікелей отбасыға төленеді.",
                },
                {
                    "num": "04", "title": "Тұзбайыр және Каспий жағалауы",
                    "tag": "Бор жарлары · жағажай · Ақтауға қайту",
                    "gradient": "grad-4",
                    "schedule": [
                        ("08:00", "Отбасымен таңғы ас, қоштасу."),
                        ("09:30", "<strong>Тұзбайырда</strong> аялдама — Каспиймен түйісетін ақ бор жарлары."),
                        ("13:00", "Жағалауда түскі ас."),
                        ("15:00", "Жағажайда бос уақыт."),
                        ("17:00", "Ақтауға қарай жол."),
                        ("19:00", "Ақтауға келу. Тур аяқталады."),
                    ],
                    "overnight": None,
                },
            ],
        },
        "villages": {
            "heading": "Ақша нақты қайда кетеді",
            "sub": "Үш түннің екеуі ауылдарда өтеді. Осы түндер үшін бір қонаққа бөліну осылай.",
            "cards": [
                ("45%", "Үй иесі отбасына", "Бөлме, олар дайындаған тағам және уақыттары үшін — делдалсыз, тікелей төлем."),
                ("20%", "Ауылдық қор", "Барлық Ata Joly қонақтарынан жиналып, ауыл өзі таңдаған нәрсеге жұмсалады."),
                ("35%", "Гид, көлік, рұқсаттар", "Гид-жүргізушілер, көлікті ұстау және жанармай, қорық рұқсаттары, лагерь жабдығы."),
            ],
        },
        "highlights": {
            "heading": "Сіз не көресіз",
            "sub": "Бағыт құрылған бірнеше сәттер.",
            "cards": [
                ("grad-h1", "Күн батыстағы Бозжыра азу тістері"),
                ("grad-h2", "Кешкі Шеркала"),
                ("grad-h3", "Үстірттің түнгі аспаны"),
                ("grad-h4", "Торыш шарлар аңғары"),
            ],
        },
        "practical": {
            "heading": "Жолға шықпас бұрын",
            "rows": [
                ("Дене дайындығы", "Орташа. Тегіс емес жер, Бозжырада бір тік көтерілу, техникалық альпинизм жоқ."),
                ("Жағдайлар", "Қарапайым. Лагерде далалық дәретхана; ауылдарда қарапайым, бірақ нақты жағдайлар."),
                ("Тіл", "Гид ағылшынша сөйлейді. Ауылдарда қазақ және орыс тілдері қолданылады."),
                ("Ауа-райы", "Тек көктем мен күз. Жазда үстіртте ыстық 40°C-тан асады."),
            ],
        },
        "cta": {
            "heading": "Төрт күн. Екі отбасы. Ешкім бұлай көрсетпейтін пейзаж.",
            "button": "Күндерді сұрау",
        },
        "footer": {
            "left": "Ata Joly · Маңғыстау облысы, Қазақстан",
            "right": "Мектеп жобасының тұжырымдамасы · нақты брондау қызметі емес",
        },
        "register": {
            "eyebrow": "Ауыл отбасыларына арналған",
            "heading": "Туристерді үйіңізде қабылдаңыз",
            "sub": "Ata Joly үй иесі отбасыларына бөлме, үй тағамы және кешкі әңгіме үшін тікелей "
                   "төлейді. Төмендегі форманы толтырыңыз — гидіміз үйіңізді бағытқа қосар алдында "
                   "сізбен байланысады.",
            "field_family_name": "Отбасы / үй иесінің аты",
            "field_aoul": "Ауыл атауы",
            "field_phone": "Телефон нөірі",
            "field_guests": "Бір уақытта неше қонақ қабылдай аласыз?",
            "field_rooms": "Ұсына алатын бөлме(лер)ді сипаттаңыз",
            "field_meals": "Қонақтарға қандай тағам дайындай аласыз?",
            "field_extra": "Тағы білу керек нәрсе бар ма (қолөнер, малдар, шаралар)?",
            "field_consent": "Ata Joly қонақтарын қабылдау туралы менімен байланысуға келісемін.",
            "submit": "Өтінішті жіберу",
            "success": "Рахмет — өтінішіңіз қабылданды. Гидіміз жақында қоңырау шалады.",
            "back_home": "Тур бетіне оралу",
            "view_list": "Тіркелген отбасыларды көру",
        },
        "booking": {
            "eyebrow": "Орын брондау",
            "heading": "Турға өтінім қалдыру",
            "sub": "Байланысыңызды қалдырыңыз — гидіміз хабарласып, нақты шығу күнін "
                   "растайды. Бұл қатысуға өтінім, автоматты төлем емес.",
            "price_per_day": "55 000 ₸",
            "price_per_day_label": "бір адамға, бір күнге",
            "price_total": "220 000 ₸",
            "price_total_label": "бір адамға, толық тур (4 күн)",
            "price_note": "Тұру, тамақтану, гид, көлік және интерактивті шаралар кіреді.",
            "capacity_label": "Жақын шығу үшін топ саны",
            "spots_left": "Қалған орын: {total} ішінен {left}",
            "spots_full": "Бұл шығуға орын жоқ — келесі күнге өтінім қалдыра аласыз.",
            "field_name": "Аты-жөні",
            "field_contact": "Телефон немесе email",
            "field_people": "Адам саны",
            "field_date": "Қалаған шығу күні",
            "field_message": "Білуіміз керек нәрсе (диета, тіл және т.б.)",
            "submit": "Өтінішті жіберу",
            "success": "Рахмет — өтінішіңіз қабылданды. Күндер мен төлемді растау үшін хабарласамыз.",
            "back_home": "Тур бетіне оралу",
        },
        "dates": {
            "eyebrow": "Алдағы сапарлар",
            "heading": "Жоспарланған тур күндері",
            "intro": "Көктем мен күзде төрт күндік сапарлар жоспарлап отырмыз. Өтінім жіберу үшін күнді таңдаңыз.",
            "planned": "Жоспарланған · күн әлі расталмаған",
            "duration": "4 күн · Ақтаудан Ақтауға",
            "apply": "Өтінім беру",
            "note": "Бұл расталған турлар емес, тек жоспар. Өтінімдерді сенімді сақтау жолға қойылғанша қатысушылар санын көрсетпейміз.",
            "empty": "Әзірге алдағы сапар күндері жоқ. Кейінірек қайта қараңыз.",
            "choose": "Шығу күнін таңдаңыз",
            "back": "Барлық жоспарланған күндер",
            "invalid_error": "Аты-жөніңізді, байланысыңызды, адам санын және қолжетімді күнді көрсетіңіз.",
        },
    },
}

LANGUAGES = ["en", "ru", "kk"]
DEFAULT_LANG = "en"
