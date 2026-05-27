"""
Каталог игр для seed_data: названия, метаданные и осмысленные описания на русском.
"""

GENRES = [
    {
        'name': 'Экшен', 'slug': 'action', 'icon': '⚔️',
        'description': 'Динамичные игры с боем, погонями и быстрыми решениями в моменте.',
    },
    {
        'name': 'РПГ', 'slug': 'rpg', 'icon': '🧙',
        'description': 'Ролевые игры с прокачкой персонажа, выбором и разветвлённым сюжетом.',
    },
    {
        'name': 'Стратегия', 'slug': 'strategy', 'icon': '♟️',
        'description': 'Тактика, управление ресурсами и планирование на несколько шагов вперёд.',
    },
    {
        'name': 'Шутер', 'slug': 'shooter', 'icon': '🔫',
        'description': 'Стрельба от первого или третьего лица, упор на реакцию и точность.',
    },
    {
        'name': 'Приключения', 'slug': 'adventure', 'icon': '🗺️',
        'description': 'Исследование миров, головоломки и история, которую вы проживаете сами.',
    },
    {
        'name': 'Спорт', 'slug': 'sports', 'icon': '⚽',
        'description': 'Симуляторы и аркады про футбол, баскетбол и другие виды спорта.',
    },
    {
        'name': 'Гонки', 'slug': 'racing', 'icon': '🏎️',
        'description': 'Гонки на машинах, мотоциклах и другом транспорте — от симулятора до аркады.',
    },
    {
        'name': 'Инди', 'slug': 'indie', 'icon': '🌱',
        'description': 'Авторские проекты небольших студий с необычными идеями и механиками.',
    },
    {
        'name': 'Хоррор', 'slug': 'horror', 'icon': '👻',
        'description': 'Атмосфера страха, напряжение и выживание в опасных условиях.',
    },
    {
        'name': 'Файтинг', 'slug': 'fighting', 'icon': '🥊',
        'description': 'Поединки один на один, комбо и соревновательные дуэли.',
    },
]

PLATFORMS = [
    {'name': 'PC (Windows)', 'short_name': 'PC'},
    {'name': 'PlayStation 5', 'short_name': 'PS5'},
    {'name': 'PlayStation 4', 'short_name': 'PS4'},
    {'name': 'Xbox Series X', 'short_name': 'XSX'},
    {'name': 'Xbox One', 'short_name': 'XBO'},
    {'name': 'Nintendo Switch', 'short_name': 'NSW'},
    {'name': 'macOS', 'short_name': 'Mac'},
    {'name': 'iOS', 'short_name': 'iOS'},
    {'name': 'Android', 'short_name': 'And'},
]

DEVELOPERS = [
    {'name': 'CD Projekt Red', 'country': 'Польша', 'founded_year': 1994},
    {'name': 'FromSoftware', 'country': 'Япония', 'founded_year': 1986},
    {'name': 'Rockstar Games', 'country': 'США', 'founded_year': 1998},
    {'name': 'Naughty Dog', 'country': 'США', 'founded_year': 1984},
    {'name': 'Nintendo EPD', 'country': 'Япония', 'founded_year': 2015},
    {'name': 'Valve Corporation', 'country': 'США', 'founded_year': 1996},
    {'name': 'Supergiant Games', 'country': 'США', 'founded_year': 2009},
    {'name': 'Insomniac Games', 'country': 'США', 'founded_year': 1994},
    {'name': 'Bethesda Game Studios', 'country': 'США', 'founded_year': 2001},
    {'name': 'Santa Monica Studio', 'country': 'США', 'founded_year': 1999},
]

# slug → short_description + description
GAME_TEXT = {
    'witcher-3': {
        'short_description': 'Открытый мир, моральный выбор и охота на монстров в роли Геральта из Ривии.',
        'description': (
            'The Witcher 3: Wild Hunt — культовая RPG в огромном фэнтезийном мире. '
            'Вы играете за Геральта, который ищет приёмную дочь Цири, убегающую от таинственной '
            'Дикой Охоты. Сюжетные квесты запоминаются на годы, а решения игрока меняют судьбы '
            'персонажей и целых регионов.\n\n'
            'Боевая система сочетает мечи, знаки и алchemy. Карта полна побочных историй, '
            'контрактов на монстров и секретов — от этого проекта ожидают сотни часов контента.'
        ),
    },
    'elden-ring': {
        'short_description': 'Тёмное фэнтези FromSoftware в огромном открытом мире Земель Между.',
        'description': (
            'Elden Ring — масштабная action-RPG от создателей Dark Souls в соавторстве с '
            'Джорджем Р. Р. Мартином. Вы — изгой без благословения, который должен собрать '
            'осколки Элденского кольца и стать новым Повелителем.\n\n'
            'Игра славится сложными боссами, свободой исследования и множеством билдов. '
            'Каждый регион Земель Между полон опасностей, скрытых подземелий и легендарного лута.'
        ),
    },
    'red-dead-redemption-2': {
        'short_description': 'Эпос о банде на закате эпохи Дикого Запада и цене верности.',
        'description': (
            'Red Dead Redemption 2 — история Артура Моргана и банды Ван der Linde в 1899 году, '
            'когда цивилизация вытесняет вольную жизнь на границе. Это не просто стрельба и '
            'погони — игра глубоко прорабатывает отношения в банде и личную честь героя.\n\n'
            'Мир невероятно детализирован: животные, погода, NPC и быт создают ощущение '
            'настоящего проживания эпохи. Охота, рыбалка, покер и сюжетные миссии сливаются '
            'в единый иммерсивный опыт.'
        ),
    },
    'the-last-of-us-part-1': {
        'short_description': 'Постапокалиптическая история о выживании, потере и человечности.',
        'description': (
            'The Last of Us Part I — переиздание легендарной истории Джоэла и Элли. '
            'Мир разрушен грибковой инфекцией, и вместе герои пересекают опасную Америку, '
            'полную заражённых и враждебных людей.\n\n'
            'Игра сочетает напряжённый стелс, ресурсы на грани и сильный эмоциональный '
            'нарратив. Это история не о монстрах, а о том, что люди готовы сделать ради выживания.'
        ),
    },
    'zelda-totk': {
        'short_description': 'Продолжение Breath of the Wild с небом, подземельями и новыми способностями.',
        'description': (
            'The Legend of Zelda: Tears of the Kingdom расширяет Хайрул вертикально: '
            'небо, поверхность и глубины под землёй. Линк получает новые силы — Ультраруку, '
            'Соединение, Возврат и Скольжение — которые превращают строительство в ключ к победе.\n\n'
            'Сотни святынь, побочные квесты и свобода исследования делают игру одной из '
            'самых масштабных приключенческих RPG на Nintendo Switch.'
        ),
    },
    'half-life-alyx': {
        'short_description': 'VR-приключение во вселенной Half-Life между первой и второй частями.',
        'description': (
            'Half-Life: Alyx — полноценная VR-игра от Valve, показавшая, каким может быть '
            'AAA-проект в виртуальной реальности. Аликс Вэнс сражается с силами Альянса в '
            'City 17, используя физику, интерактивность и атмосферный хоррор.\n\n'
            'Головоломки, перестрелки и сюжет тесно связаны с лore серии. Для фанатов '
            'Half-Life это обязательный опыт, а для VR — эталон качества.'
        ),
    },
    'hades': {
        'short_description': 'Roguelike про побег из Аида с живым диалогом и идеальной боёвкой.',
        'description': (
            'Hades — roguelike от Supergiant Games, где вы играете за Загрея, сына Аида. '
            'Каждый забег уникален: случайные комнаты, боги Олимпа дарят способности, '
            'а после смерти история всё равно движется вперёд.\n\n'
            'Персонажи запоминаются, диалоги меняются, а боевая система остаётся '
            'отзывчивой и глубокой. Игра доказала, что roguelike может быть и сюжетной, '
            'и эмоциональной.'
        ),
    },
    'spiderman-2': {
        'short_description': 'Питер Паркер и Майлз Моралес против Венома в раскрытом Нью-Йорке.',
        'description': (
            'Marvel\'s Spider-Man 2 продолжает историю Insomniac про Человека-Паука. '
            'Два героя, один город и угроза симбиота, который меняет всё. Полёт на паутине '
            'стал ещё быстрее, а бои — зрелищнее.\n\n'
            'Нью-Йорк больше и живее, сюжет держит темп, а побочные активности не ощущаются '
            'наполнителем. Отличный эксклюзив для PlayStation 5.'
        ),
    },
    'starfield': {
        'short_description': 'Космическая RPG Bethesda — исследование галактики и собственная история.',
        'description': (
            'Starfield — первая новая вселенная Bethesda за 25 лет. Вы член организации '
            'Созвездие, исследующей космос в поисках ответа: одни ли мы во вселенной. '
            'Сотни планет, кастомизация корабля и персонажа, фракции и моральный выбор.\n\n'
            'Игра сочетает масштаб Skyrim с научной фантастикой: высадки на планеты, '
            'космические бои и сюжетные линии на десятки часов.'
        ),
    },
    'gow-ragnarok': {
        'short_description': 'Кратос и Атрей перед лицом Рагнарёка в финале норвежской саги.',
        'description': (
            'God of War Ragnarök завершает историю Кратоса и Атрея в скандинавской мифологии. '
            'Девять миров, боги, судьба и семья — всё сходится к надвигающемуся Рагнарёку. '
            'Бои стали разнообразнее, а эмоциональные сцены — сильнее.\n\n'
            'Игра балансирует между эпическим экшеном и личной драмой отца и сына. '
            'Один из лучших эксклюзивов PlayStation.'
        ),
    },
    'metro-exodus': {
        'short_description': 'Постапокалиптическое путешествие по России на поезде «Аврора».',
        'description': (
            'Metro Exodus отправляет Артёма и его отряд из московского метро в путешествие '
            'по просторам России. Каждый регион — новая атмосфера, от зимних лесов до пустыни.\n\n'
            'Сочетание стелса, выживания и сюжетных миссий с выбором, влияющим на концовку. '
            'Мрачная, но надежда не исчезает полностью.'
        ),
    },
    'stalker-2': {
        'short_description': 'Долгожданное продолжение S.T.A.L.K.E.R. в Зоне отчуждения.',
        'description': (
            'S.T.A.L.K.E.R. 2: Heart of Chornobyl возвращает в Зону — опасную территорию '
            'с аномалиями, мутантами и artefактами. Исследуйте открытый мир, выполняйте '
            'контракты и выживайте среди других сталкеров.\n\n'
            'Атмосфера напряжения, непредсказуемые встречи и свобода действий — '
            'дух оригинальной серии в современной графике.'
        ),
    },
    'baldurs-gate-3': {
        'short_description': 'Глубокая партийная RPG по D&D с выбором, романами и тактическими боями.',
        'description': (
            'Baldur\'s Gate 3 от Larian Studios — RPG, где каждый диалог и бой имеют вес. '
            'Создайте отряд, исследуйте Фаerun, раскройте тайну паразита в вашей голове '
            'и решите судьбу мира.\n\n'
            'Система D&D 5e, реактивный мир и множество концовок. Один из лучших RPG-релизов '
            'последних лет по отзывам игроков и критиков.'
        ),
    },
    'cyberpunk-2077': {
        'short_description': 'Киберпанк-RPG в Night City — стиль, импланты и корпоративные интриги.',
        'description': (
            'Cyberpunk 2077 переносит в мегаполис Night City, где технологии и жадность '
            'правят улицами. Вы — V, наёмник с амбициями, чья жизнь переплетается с '
            'легендой Джонни Сильверхенда.\n\n'
            'Открытый мир, кастомизация билдов, сюжетные линии и обновление Phantom Liberty '
            'сделали игру одним из главных киберпанк-опытов в индустрии.'
        ),
    },
    'horizon-forbidden-west': {
        'short_description': 'Элой исследует Запретный Запад и раскрывает тайну гибели цивилизации.',
        'description': (
            'Horizon Forbidden West продолжает историю Элой. Новые биомы, механические '
            'существа и древние технологии ждут в Западе. Элой ищет ответ, как спасти '
            'мир от экологической катастрофы.\n\n'
            'Красивый открытый мир, тактические бои с роботами и сильный сюжет о наследии '
            'прошлого и ответственности будущего.'
        ),
    },
    'ghost-of-tsushima': {
        'short_description': 'Самурай на осаждённом острове Цусима — честь, стелс и красота Японии.',
        'description': (
            'Ghost of Tsushima — приключение о монголо-японской войне XIII века. Джин Сакай '
            'должен защитить остров, выбирая между кодексом самурая и методами «призрака».\n\n'
            'Пейзажи вдохновлены классическим японским кино, бои — зрелищны, а история '
            'о цене войны и идентичности остаётся с вами после финала.'
        ),
    },
    'sekiro-shadows-die-twice': {
        'short_description': 'Сложный экшен про синоби с акцентом на парирование и вертикальность.',
        'description': (
            'Sekiro: Shadows Die Twice — action от FromSoftware про одорогого воина в '
            'феодальной Японии. Главная механика — идеальное парирование и система '
            'стойкости вместо классической выносливости.\n\n'
            'Игра требует терпения и практики, но награждает ощущением мастерства. '
            'Сюжет о преданности, мести и искуплении.'
        ),
    },
    'dark-souls-iii': {
        'short_description': 'Классика soulslike: тёмное фэнтези, сложные боссы и атмосфера отчаяния.',
        'description': (
            'Dark Souls III завершает трилогию FromSoftware. Королевство Лотрик угасает, '
            'Пепло идёт на трон, а вы — Незапятнанный, призванный связать огонь или '
            'погасить его навсегда.\n\n'
            'Мастерски спроектированные локации, запоминающиеся боссы и минималистичный '
            'сторителлинг через окружение — основа жанра soulslike.'
        ),
    },
    'bloodborne': {
        'short_description': 'Готический хорror-action в Ярнаме, где безумие опаснее монстров.',
        'description': (
            'Bloodborne переносит в викторианский Ярнам, охваченный кровавой чумой. '
            'Быстрый, агрессивный бой, пистолеты для парирования и кошмарные существа '
            'создают уникальную атмосферу.\n\n'
            'Игра награждает смелость и наказует осторожность. Сюжет о культах, '
            'космическом ужасе и цене знания скрыт в деталях мира.'
        ),
    },
    'resident-evil-4': {
        'short_description': 'Ремейк культового survival horror про спасение дочери президента.',
        'description': (
            'Resident Evil 4 (2023) — современная версия классики. Леон Кеннedy отправляется '
            'в европейскую деревню, чтобы спасти Эшли, и попадает в ловушку культа и паразитов.\n\n'
            'Напряжённая стрельба, управление ресурсами и кинематографичная подача. '
            'Ремейк сохранил дух оригинала и улучшил управление и графику.'
        ),
    },
    'dead-space': {
        'short_description': 'Sci-fi horror на космическом корабле «Ишимура» — некроморфы и изоляция.',
        'description': (
            'Dead Space (2023) — ремейк хорror-классики. Инженер Айзек Кларк прибывает '
            'на «Ишимуру» и обнаруживает корабль, заражённый некроморфами. Разрезание '
            'конечностей — не жестокость, а необходимость для выживания.\n\n'
            'Клаустрофобные коридоры, звук и свет создают постоянное напряжение. '
            'Один из лучших sci-fi horror опытов.'
        ),
    },
    'alan-wake-2': {
        'short_description': 'Психологический хорror о писателе, реальности и тёмной силе.',
        'description': (
            'Alan Wake 2 продолжает историю писателя, чьи слова меняют реальность. '
            'Два протагониста, детектив Сага и сам Алан, раскрывают мистику вокруг '
            'Dark Place — измерения, где история пожирает людей.\n\n'
            'Сюрреалистичная атмосфера, сильный сценарий и напряжённые перестрелки с '
            'фонариком. Игра от Remedy для любителей авторского хорror.'
        ),
    },
    'control': {
        'short_description': 'Странный экшен в здании ФБК — телекинез, оружие и паранormal.',
        'description': (
            'Control от Remedy — игра про директорa Федерального бюро контроля Джesse Faden. '
            'Здание Oldest House — бесконечный лабиринт, где нарушены законы физики. '
            'Телекинез, трансформируемое оружие и стильный дизайн 70-х.\n\n'
            'Сюжет о силах, которые нельзя понять, и бюрократии, пытающейся их сдержать.'
        ),
    },
    'disco-elysium': {
        'short_description': 'Детективная RPG без боёв — диалоги, навыки и политика в вашей голове.',
        'description': (
            'Disco Elysium — уникальная RPG, где главное оружие — слова. Вы — детектив '
            'с амнезией, расследующий убийство в городе Revachol. 24 внутренних «навыка» '
            'спорят в вашей голове и влияют на каждый выбор.\n\n'
            'Нет классических боёв, зато есть философия, политика, юмор и десятки '
            'концовок. История о том, как прошлое формирует личность.'
        ),
    },
    'persona-5-royal': {
        'short_description': 'Стильная JRPG: школа днём, Phantom Thieves ночью, социальные связи.',
        'description': (
            'Persona 5 Royal — расширенная версия культовой JRPG. Студент по дню, '
            'вор-фантом ночью: вы меняете сердца корrupt чиновников в Metaverse. '
            'Параллельно строите отношения с друзьями и улучшаете Persona.\n\n'
            'Стильный UI, саундтрек, тактические бои и сотни часов контента. '
            'Один из самых харизматичных RPG-релизов.'
        ),
    },
    'final-fantasy-xvi': {
        'short_description': 'Мрачное фэнтези Final Fantasy с акцентом на экшен и политику королевств.',
        'description': (
            'Final Fantasy XVI — более взрослая и мрачная часть серии. Клайв Rosfield '
            'ищет месть в мире, где люди используют силу Eikon. Бои стали динамичнее, '
            'сюжет — кинематографичнее.\n\n'
            'Эпические сражения богов, политические интриги и личная драма. '
            'Эксклюзив PlayStation 5 с масштабом, ожидаемым от FF.'
        ),
    },
    'monster-hunter-rise': {
        'short_description': 'Охота на гигантских монстров в команде — лут, крафт и Wirebug.',
        'description': (
            'Monster Hunter Rise отправляет охотников в деревню Камура. Используйте '
            'Wirebug для мобильности и новых атак, выслеживайте огромных монстров '
            'и создавайте броню из их частей.\n\n'
            'Кооператив на 4 игроков, глубокая система крафта и бои, где каждый '
            'монстр — отдельный экзамен на терпение и тактику.'
        ),
    },
    'doom-eternal': {
        'short_description': 'Бескомпромиссный шутер — Doom Slayer против демонов на Mars и Земле.',
        'description': (
            'DOOM Eternal ускоряет формулу 2016 года: больше демонов, больше движения, '
            'больше насилия над ада. Glory kills восстанавливают ресурсы, арсенал '
            'разнообразен, а саундтрек Mick Gordon подгоняет темп.\n\n'
            'Игра не про сюжет — про flow-state и доминирование. '
            'Идеальный выбор для любителей fast-paced шутеров.'
        ),
    },
    'forza-horizon-5': {
        'short_description': 'Открытые гонки в Мексике — сотни машин, сезоны и онлайн-фестиваль.',
        'description': (
            'Forza Horizon 5 — аркадные гонки в живописной Мексике. Сотни лицензированных '
            'автомобилей, смена сезонов меняет карту, а фестиваль Horizon объединяет '
            'одиночку и онлайн.\n\n'
            'Доступные настройка помощи и глубокая симуляция для хардкора. '
            'Один из лучших racing sandbox на рынке.'
        ),
    },
    'gran-turismo-7': {
        'short_description': 'Реалистичный гоночный симулятор с легендарными трассами и машинами.',
        'description': (
            'Gran Turismo 7 возвращает серию к корням: лицензии, физика, культовые '
            'трассы и режим карьеры. Сочетание симуляции и доступности для новичков '
            'через помощники и обучение.\n\n'
            'Для фанатов motorsport и коллекционеров виртуальных автомобилей — '
            'флагман PlayStation.'
        ),
    },
    'fifa-24': {
        'short_description': 'Футбольный симулятор EA Sports — карьера, Ultimate Team и онлайн.',
        'description': (
            'EA Sports FC 24 (FIFA) — ежегодный футбольный симулятор с актуальными '
            'составами, лигами и режимами. Карьера игрока или менеджера, Ultimate Team '
            'и онлайн-матчи с друзьями.\n\n'
            'HyperMotion и улучшенная физика делают матчи ближе к реальному футболу. '
            'Главный выбор для фанатов спорта.'
        ),
    },
    'nba-2k24': {
        'short_description': 'Баскетбольный симулятор — MyCareer, парк и NBA сезон.',
        'description': (
            'NBA 2K24 — симулятор баскетбола с режимом MyCareer, где вы строите карьеру '
            'от новичка до звезды NBA. The City для онлайн-игры, управление клубом '
            'и актуальные составы лиги.\n\n'
            'Реалистичная анимация, кастомизация и соревновательный онлайн — '
            'стандарт жанра sports sim.'
        ),
    },
    'street-fighter-6': {
        'short_description': 'Легендарный fighting с World Tour, онлайном и новой системой Drive.',
        'description': (
            'Street Fighter 6 обновляет формулу серии: режим World Tour с обучением, '
            'Battle Hub для онлайна и система Drive для глубины боёв. Ryu, Chun-Li '
            'и новые бойцы с уникальными стилями.\n\n'
            'Отличный вход для новичков и поле для соревновательных игроков. '
            'Визуальный стиль и отзывчивость на высоте.'
        ),
    },
    'tekken-8': {
        'short_description': '3D-файтинг с динамичными боями и сюжетом Mishima-клана.',
        'description': (
            'Tekken 8 продолжает вековую вражду семьи Mishima. Новая система Heat, '
            'разрушаемые арены и кинематографичный режим истории. Каждый персонаж '
            'имеет глубокий набор приёмов.\n\n'
            'Один из главных competitive 3D-файтингов с loyal community и '
            'регулярными турнирами.'
        ),
    },
    'civilization-vi': {
        'short_description': 'Постройте империю от древности до космоса — «ещё один ход» на десятки часов.',
        'description': (
            'Sid Meier\'s Civilization VI — пошаговая стратегия, где вы ведёте цивилизацию '
            'от каменного века до будущего. Города на сетке, районы, дипломатия, война '
            'и культурная победа — пути разные.\n\n'
            '«Just one more turn» — главная опасность. Глубокая, но понятная стратегия '
            'для одиночной игры и мультиплеера.'
        ),
    },
    'total-war-warhammer-iii': {
        'short_description': 'Эпические сражения Total War во вселенной Warhammer Fantasy.',
        'description': (
            'Total War: Warhammer III завершает трилогию Creative Assembly. Огромные '
            'армии, легендарные фракции Chaos, Kislev и Cathay, кампания на карте '
            'мира и тактические битвы в реальном времени.\n\n'
            'Для фанатов Warhammer и стратегий — масштаб, который редко встретишь '
            'в других играх.'
        ),
    },
    'crusader-kings-iii': {
        'short_description': 'Династическая стратегия — интриги, браки, войны и roleplay средневековья.',
        'description': (
            'Crusader Kings III от Paradox — grand strategy про династии, а не страны. '
            'Вы управляете персонажем со своими чертами, амбициями и врагами. '
            'Браки, заговоры, holy wars и абсurdные истории рождаются сами.\n\n'
            'Sandbox средневековой политики с бесконечным replayability.'
        ),
    },
    'stardew-valley': {
        'short_description': 'Уютная ферма, соседи и спокойный ритм — antidote к стрессу.',
        'description': (
            'Stardew Valley — indie-хит про наследованную ферму. Пашите землю, '
            'разводите животных, дружите с жителями Pelican Town и исследуйте '
            'пещеры. Каждый сезон приносит новые культуры и события.\n\n'
            'Тёплая атмосфера, кооператив и сотни часов спокойного геймплея. '
            'Игра, к которой возвращаются годами.'
        ),
    },
    'hollow-knight': {
        'short_description': 'Metroidvania в мрачном подземном королевстве насекомых.',
        'description': (
            'Hollow Knight — 2D metroidvania с ручной отрисовкой и атмосферой Hallownest. '
            'Рыцарь исследует глубины, сражается с боссами и открывает способности '
            'для новых регионов.\n\n'
            'Сложные бои, красивая музыка и молчаливый сторителлинг через мир. '
            'Эталон indie metroidvania.'
        ),
    },
    'celeste': {
        'short_description': 'Платформер про покорение горы и преодоление тревоги.',
        'description': (
            'Celeste — precision platformer, где Madeline поднимается на гору Celeste. '
            'Жёсткие уровни требуют практики, но история о тревоге и принятии себя '
            'идёт параллельно с геймплеем.\n\n'
            'Отличный саундтрек Lena Raine, assist mode для доступности и '
            'одна из самых эмоциональных indie-историй.'
        ),
    },
    'undertale': {
        'short_description': 'RPG, где можно пройти без единого убийства — выбор определяет всё.',
        'description': (
            'Undertale от Toby Fox ломает ожидания от RPG. Каждый враг можно пощадить, '
            'диалоги запоминают ваши прошлые прохождения, а саундтрек стал культовым.\n\n'
            'Короткая по часам, но бесконечная по обсуждениям. Игра о mercy, '
            'последствиях и авторском видении.'
        ),
    },
    'portal-2': {
        'short_description': 'Головоломки с портальной пушкой и саркастичным AI GLaDOS.',
        'description': (
            'Portal 2 — эталон головоломок от Valve. Портальная пушка, физика, '
            'кооператив и сюжет с GLaDOS и Уheatley. Уровни умные, смешные '
            'и постепенно усложняются.\n\n'
            'Одна из лучших игр всех времён по дизайну уровней и юмору.'
        ),
    },
    'half-life-2': {
        'short_description': 'Легендарный шутер — Гordon Freeman против Альянса в City 17.',
        'description': (
            'Half-Life 2 (2004) до сих пор учит индустрию. Физика, повествование '
            'без кат-сцен и атмосфера оккупированного City 17. Гравипушка, '
            'враги и сюжетные повороты на каждом шагу.\n\n'
            'Обязательна к прохождению для любого любителя игр.'
        ),
    },
    'bioshock-infinite': {
        'short_description': 'Стимпанк-шутер в летающем городе Columbia и история Booker и Elizabeth.',
        'description': (
            'BioShock Infinite переносит в небесный Columbia — город идеологии и '
            'насилия. Booker DeWitt ищет девушку Elizabeth, и их путешествие '
            'ломает ожидания о времени и реальности.\n\n'
            'Стрельба, vigors и один из самых обсуждаемых финалов в играх.'
        ),
    },
    'mass-effect-legendary-edition': {
        'short_description': 'Трилогия Mass Effect в одном издании — космическая opera и выборы.',
        'description': (
            'Mass Effect Legendary Edition объединяет три части saga о Commander Shepard. '
            'Исследуйте галактику, собирайте отряд, принимайте решения, которые '
            'переходят между играми.\n\n'
            'Отношения с напарниками, моральные дilemmas и эпический финал против Reapers.'
        ),
    },
    'dragon-age-inquisition': {
        'short_description': 'Fantasy RPG — Inquisitor против хаоса и Breach в Thedas.',
        'description': (
            'Dragon Age: Inquisition — open-world RPG от BioWare. После катастрофы '
            'вы становитесь Inquisitor и объединяете фракции Thedas против новой угрозы.\n\n'
            'Большой мир, тактические бои с паузой и глубокие отношения с компаньонами.'
        ),
    },
    'fallout-4': {
        'short_description': 'Post-apocalypse Boston — стройте, стреляйте и ищите сына в wasteland.',
        'description': (
            'Fallout 4 отправляет в Commonwealth после ядерной войны. Отец ищет сына, '
            'строит поселения, модифицирует оружие и исследует руины Бостона.\n\n'
            'Свобода билдов, VATS и атмосфера retro-future USA в разрухе.'
        ),
    },
    'skyrim': {
        'short_description': 'Открытый мир Skyrim — драконы, гильдии и бесконечные приключения.',
        'description': (
            'The Elder Scrolls V: Skyrim — sandbox RPG, который пережил десятилетие. '
            'Вы Dragonborn в провинции Skyrim: гильдии, даedric квесты, моддинг '
            'и свобода «куда угодно, когда угодно».\n\n'
            'Игра, которую до сих пор проходят впервые каждый год.'
        ),
    },
    'assassins-creed-valhalla': {
        'short_description': 'Викинги в Англии — рейды, settlement и скрытый клинок.',
        'description': (
            'Assassin\'s Creed Valhalla — история викинга Eivor в Англии IX века. '
            'Рейды, строительство settlement, мифология и конфликт с орденом тамplars '
            'в формате open world Ubisoft.\n\n'
            'Масштаб, кастомизация и смесь истории с фэнтези AC.'
        ),
    },
    'far-cry-6': {
        'short_description': 'Революция на острове Yara против диктатора Anton Castillo.',
        'description': (
            'Far Cry 6 — open-world шутер на вымышленном карибском острове Yara. '
            'Guerrilla war против Anton Castillo, кастомное оружие «Resolver» '
            'и типичный хаос серии Far Cry.\n\n'
            'Для тех, кто любит взрывы, захват outposts и сатиру на тиранию.'
        ),
    },
    'watch-dogs-legion': {
        'short_description': 'Хакерская London — играйте за любого NPC из толпы.',
        'description': (
            'Watch Dogs: Legion уникален тем, что каждый житель London может стать '
            'игровым персонажем. Хакерство, дроны, DedSec против authoritarian '
            'режима Albion.\n\n'
            'Процедурный отряд и исследование near-future UK в стиле Ubisoft.'
        ),
    },
}

# Полные записи игр для seed (основные + дополнительные)
GAMES = [
    {
        'title': 'The Witcher 3: Wild Hunt', 'slug': 'witcher-3',
        'developer': 'CD Projekt Red', 'genres': ['rpg', 'action', 'adventure'],
        'platforms': ['PC', 'PS5', 'PS4', 'XSX', 'XBO', 'NSW'],
        'release_year': 2015, 'release_date': '2015-05-19', 'age_rating': '18+',
        'metacritic_score': 93, 'is_featured': True,
    },
    {
        'title': 'Elden Ring', 'slug': 'elden-ring',
        'developer': 'FromSoftware', 'genres': ['action', 'rpg'],
        'platforms': ['PC', 'PS5', 'PS4', 'XSX', 'XBO'],
        'release_year': 2022, 'release_date': '2022-02-25', 'age_rating': '16+',
        'metacritic_score': 96, 'is_featured': True,
    },
    {
        'title': 'Red Dead Redemption 2', 'slug': 'red-dead-redemption-2',
        'developer': 'Rockstar Games', 'genres': ['action', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO'],
        'release_year': 2018, 'release_date': '2018-10-26', 'age_rating': '18+',
        'metacritic_score': 97, 'is_featured': True,
    },
    {
        'title': 'The Last of Us Part I', 'slug': 'the-last-of-us-part-1',
        'developer': 'Naughty Dog', 'genres': ['action', 'adventure', 'horror'],
        'platforms': ['PC', 'PS5'],
        'release_year': 2022, 'release_date': '2022-09-02', 'age_rating': '18+',
        'metacritic_score': 89, 'is_featured': True,
    },
    {
        'title': 'The Legend of Zelda: Tears of the Kingdom', 'slug': 'zelda-totk',
        'developer': 'Nintendo EPD', 'genres': ['action', 'adventure', 'rpg'],
        'platforms': ['NSW'],
        'release_year': 2023, 'release_date': '2023-05-12', 'age_rating': '12+',
        'metacritic_score': 96, 'is_featured': True,
    },
    {
        'title': 'Half-Life: Alyx', 'slug': 'half-life-alyx',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'adventure', 'horror'],
        'platforms': ['PC'],
        'release_year': 2020, 'release_date': '2020-03-23', 'age_rating': '16+',
        'metacritic_score': 93, 'is_featured': False,
    },
    {
        'title': 'Hades', 'slug': 'hades',
        'developer': 'Supergiant Games', 'genres': ['action', 'rpg', 'indie'],
        'platforms': ['PC', 'NSW', 'PS5', 'PS4', 'XSX', 'XBO'],
        'release_year': 2020, 'release_date': '2020-09-17', 'age_rating': '12+',
        'metacritic_score': 93, 'is_featured': False,
    },
    {
        'title': 'Marvel\'s Spider-Man 2', 'slug': 'spiderman-2',
        'developer': 'Insomniac Games', 'genres': ['action', 'adventure'],
        'platforms': ['PS5'],
        'release_year': 2023, 'release_date': '2023-10-20', 'age_rating': '16+',
        'metacritic_score': 90, 'is_featured': False,
    },
    {
        'title': 'Starfield', 'slug': 'starfield',
        'developer': 'Bethesda Game Studios', 'genres': ['rpg', 'action', 'adventure'],
        'platforms': ['PC', 'XSX'],
        'release_year': 2023, 'release_date': '2023-09-06', 'age_rating': '16+',
        'metacritic_score': 83, 'is_featured': False,
    },
    {
        'title': 'God of War Ragnarök', 'slug': 'gow-ragnarok',
        'developer': 'Santa Monica Studio', 'genres': ['action', 'adventure', 'rpg'],
        'platforms': ['PS5', 'PS4'],
        'release_year': 2022, 'release_date': '2022-11-09', 'age_rating': '18+',
        'metacritic_score': 94, 'is_featured': False,
    },
    {
        'title': 'Metro Exodus', 'slug': 'metro-exodus',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'adventure', 'horror'],
        'platforms': ['PC', 'PS5', 'PS4', 'XSX', 'XBO'],
        'release_year': 2019, 'release_date': '2019-02-15', 'age_rating': '18+',
        'metacritic_score': 82, 'is_featured': False,
    },
    {
        'title': 'Сталкер 2: Сердце Чернобыля', 'slug': 'stalker-2',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'horror', 'adventure'],
        'platforms': ['PC', 'XSX'],
        'release_year': 2024, 'release_date': '2024-11-20', 'age_rating': '18+',
        'metacritic_score': 73, 'is_featured': False,
    },
    {
        'title': 'Baldur\'s Gate 3', 'slug': 'baldurs-gate-3',
        'developer': 'CD Projekt Red', 'genres': ['rpg', 'adventure'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2023, 'release_date': '2023-08-03', 'age_rating': '18+',
        'metacritic_score': 96, 'is_featured': True,
    },
    {
        'title': 'Cyberpunk 2077', 'slug': 'cyberpunk-2077',
        'developer': 'CD Projekt Red', 'genres': ['rpg', 'action'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2020, 'release_date': '2020-12-10', 'age_rating': '18+',
        'metacritic_score': 86, 'is_featured': True,
    },
    {
        'title': 'Horizon Forbidden West', 'slug': 'horizon-forbidden-west',
        'developer': 'Insomniac Games', 'genres': ['action', 'rpg', 'adventure'],
        'platforms': ['PS5', 'PS4', 'PC'],
        'release_year': 2022, 'release_date': '2022-02-18', 'age_rating': '16+',
        'metacritic_score': 88, 'is_featured': False,
    },
    {
        'title': 'Ghost of Tsushima', 'slug': 'ghost-of-tsushima',
        'developer': 'Insomniac Games', 'genres': ['action', 'adventure'],
        'platforms': ['PS5', 'PS4', 'PC'],
        'release_year': 2020, 'release_date': '2020-07-17', 'age_rating': '18+',
        'metacritic_score': 83, 'is_featured': False,
    },
    {
        'title': 'Sekiro: Shadows Die Twice', 'slug': 'sekiro-shadows-die-twice',
        'developer': 'FromSoftware', 'genres': ['action', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO'],
        'release_year': 2019, 'release_date': '2019-03-22', 'age_rating': '18+',
        'metacritic_score': 90, 'is_featured': False,
    },
    {
        'title': 'Dark Souls III', 'slug': 'dark-souls-iii',
        'developer': 'FromSoftware', 'genres': ['action', 'rpg'],
        'platforms': ['PC', 'PS4', 'XBO'],
        'release_year': 2016, 'release_date': '2016-04-12', 'age_rating': '16+',
        'metacritic_score': 89, 'is_featured': False,
    },
    {
        'title': 'Bloodborne', 'slug': 'bloodborne',
        'developer': 'FromSoftware', 'genres': ['action', 'horror'],
        'platforms': ['PS4', 'PS5'],
        'release_year': 2015, 'release_date': '2015-03-24', 'age_rating': '18+',
        'metacritic_score': 92, 'is_featured': False,
    },
    {
        'title': 'Resident Evil 4', 'slug': 'resident-evil-4',
        'developer': 'Valve Corporation', 'genres': ['horror', 'shooter', 'action'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2023, 'release_date': '2023-03-24', 'age_rating': '18+',
        'metacritic_score': 93, 'is_featured': False,
    },
    {
        'title': 'Dead Space', 'slug': 'dead-space',
        'developer': 'Valve Corporation', 'genres': ['horror', 'shooter'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2023, 'release_date': '2023-01-27', 'age_rating': '18+',
        'metacritic_score': 89, 'is_featured': False,
    },
    {
        'title': 'Alan Wake 2', 'slug': 'alan-wake-2',
        'developer': 'Valve Corporation', 'genres': ['horror', 'shooter', 'adventure'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2023, 'release_date': '2023-10-27', 'age_rating': '18+',
        'metacritic_score': 89, 'is_featured': False,
    },
    {
        'title': 'Control', 'slug': 'control',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'action', 'adventure'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2019, 'release_date': '2019-08-27', 'age_rating': '16+',
        'metacritic_score': 82, 'is_featured': False,
    },
    {
        'title': 'Disco Elysium', 'slug': 'disco-elysium',
        'developer': 'Supergiant Games', 'genres': ['rpg', 'adventure', 'indie'],
        'platforms': ['PC', 'PS5', 'XSX', 'NSW'],
        'release_year': 2019, 'release_date': '2019-10-15', 'age_rating': '18+',
        'metacritic_score': 91, 'is_featured': False,
    },
    {
        'title': 'Persona 5 Royal', 'slug': 'persona-5-royal',
        'developer': 'FromSoftware', 'genres': ['rpg', 'adventure'],
        'platforms': ['PC', 'PS5', 'XSX', 'NSW'],
        'release_year': 2022, 'release_date': '2022-10-21', 'age_rating': '16+',
        'metacritic_score': 95, 'is_featured': False,
    },
    {
        'title': 'Final Fantasy XVI', 'slug': 'final-fantasy-xvi',
        'developer': 'FromSoftware', 'genres': ['rpg', 'action'],
        'platforms': ['PS5', 'PC'],
        'release_year': 2023, 'release_date': '2023-06-22', 'age_rating': '18+',
        'metacritic_score': 87, 'is_featured': False,
    },
    {
        'title': 'Monster Hunter Rise', 'slug': 'monster-hunter-rise',
        'developer': 'FromSoftware', 'genres': ['action', 'rpg'],
        'platforms': ['PC', 'PS5', 'XSX', 'NSW'],
        'release_year': 2021, 'release_date': '2021-03-26', 'age_rating': '16+',
        'metacritic_score': 88, 'is_featured': False,
    },
    {
        'title': 'Doom Eternal', 'slug': 'doom-eternal',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'action'],
        'platforms': ['PC', 'PS5', 'XSX', 'NSW'],
        'release_year': 2020, 'release_date': '2020-03-20', 'age_rating': '18+',
        'metacritic_score': 88, 'is_featured': False,
    },
    {
        'title': 'Forza Horizon 5', 'slug': 'forza-horizon-5',
        'developer': 'Valve Corporation', 'genres': ['racing'],
        'platforms': ['PC', 'XSX'],
        'release_year': 2021, 'release_date': '2021-11-09', 'age_rating': '6+',
        'metacritic_score': 92, 'is_featured': False,
    },
    {
        'title': 'Gran Turismo 7', 'slug': 'gran-turismo-7',
        'developer': 'Insomniac Games', 'genres': ['racing'],
        'platforms': ['PS5', 'PS4'],
        'release_year': 2022, 'release_date': '2022-03-04', 'age_rating': '6+',
        'metacritic_score': 87, 'is_featured': False,
    },
    {
        'title': 'FIFA 24', 'slug': 'fifa-24',
        'developer': 'Valve Corporation', 'genres': ['sports'],
        'platforms': ['PC', 'PS5', 'XSX', 'NSW'],
        'release_year': 2023, 'release_date': '2023-09-29', 'age_rating': '6+',
        'metacritic_score': 74, 'is_featured': False,
    },
    {
        'title': 'NBA 2K24', 'slug': 'nba-2k24',
        'developer': 'Valve Corporation', 'genres': ['sports'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2023, 'release_date': '2023-09-08', 'age_rating': '6+',
        'metacritic_score': 72, 'is_featured': False,
    },
    {
        'title': 'Street Fighter 6', 'slug': 'street-fighter-6',
        'developer': 'FromSoftware', 'genres': ['fighting', 'action'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2023, 'release_date': '2023-06-02', 'age_rating': '12+',
        'metacritic_score': 92, 'is_featured': False,
    },
    {
        'title': 'Tekken 8', 'slug': 'tekken-8',
        'developer': 'FromSoftware', 'genres': ['fighting', 'action'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2024, 'release_date': '2024-01-26', 'age_rating': '16+',
        'metacritic_score': 90, 'is_featured': False,
    },
    {
        'title': 'Civilization VI', 'slug': 'civilization-vi',
        'developer': 'Valve Corporation', 'genres': ['strategy'],
        'platforms': ['PC', 'PS4', 'XBO', 'NSW'],
        'release_year': 2016, 'release_date': '2016-10-21', 'age_rating': '12+',
        'metacritic_score': 88, 'is_featured': False,
    },
    {
        'title': 'Total War: Warhammer III', 'slug': 'total-war-warhammer-iii',
        'developer': 'Valve Corporation', 'genres': ['strategy', 'action'],
        'platforms': ['PC'],
        'release_year': 2022, 'release_date': '2022-02-17', 'age_rating': '16+',
        'metacritic_score': 86, 'is_featured': False,
    },
    {
        'title': 'Crusader Kings III', 'slug': 'crusader-kings-iii',
        'developer': 'Valve Corporation', 'genres': ['strategy', 'rpg'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2020, 'release_date': '2020-09-01', 'age_rating': '16+',
        'metacritic_score': 91, 'is_featured': False,
    },
    {
        'title': 'Stardew Valley', 'slug': 'stardew-valley',
        'developer': 'Supergiant Games', 'genres': ['indie', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO', 'NSW', 'And', 'iOS'],
        'release_year': 2016, 'release_date': '2016-02-26', 'age_rating': '6+',
        'metacritic_score': 89, 'is_featured': False,
    },
    {
        'title': 'Hollow Knight', 'slug': 'hollow-knight',
        'developer': 'Supergiant Games', 'genres': ['indie', 'action', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO', 'NSW'],
        'release_year': 2017, 'release_date': '2017-02-24', 'age_rating': '6+',
        'metacritic_score': 90, 'is_featured': False,
    },
    {
        'title': 'Celeste', 'slug': 'celeste',
        'developer': 'Supergiant Games', 'genres': ['indie', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO', 'NSW'],
        'release_year': 2018, 'release_date': '2018-01-25', 'age_rating': '6+',
        'metacritic_score': 94, 'is_featured': False,
    },
    {
        'title': 'Undertale', 'slug': 'undertale',
        'developer': 'Supergiant Games', 'genres': ['indie', 'rpg'],
        'platforms': ['PC', 'PS4', 'XBO', 'NSW'],
        'release_year': 2015, 'release_date': '2015-09-15', 'age_rating': '12+',
        'metacritic_score': 92, 'is_featured': False,
    },
    {
        'title': 'Portal 2', 'slug': 'portal-2',
        'developer': 'Valve Corporation', 'genres': ['adventure', 'action'],
        'platforms': ['PC', 'PS3', 'XBO'],
        'release_year': 2011, 'release_date': '2011-04-19', 'age_rating': '12+',
        'metacritic_score': 95, 'is_featured': False,
    },
    {
        'title': 'Half-Life 2', 'slug': 'half-life-2',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'action'],
        'platforms': ['PC'],
        'release_year': 2004, 'release_date': '2004-11-16', 'age_rating': '16+',
        'metacritic_score': 96, 'is_featured': False,
    },
    {
        'title': 'BioShock Infinite', 'slug': 'bioshock-infinite',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'action', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO', 'NSW'],
        'release_year': 2013, 'release_date': '2013-03-26', 'age_rating': '18+',
        'metacritic_score': 94, 'is_featured': False,
    },
    {
        'title': 'Mass Effect Legendary Edition', 'slug': 'mass-effect-legendary-edition',
        'developer': 'Valve Corporation', 'genres': ['rpg', 'shooter', 'action'],
        'platforms': ['PC', 'PS4', 'XBO'],
        'release_year': 2021, 'release_date': '2021-05-14', 'age_rating': '18+',
        'metacritic_score': 87, 'is_featured': False,
    },
    {
        'title': 'Dragon Age: Inquisition', 'slug': 'dragon-age-inquisition',
        'developer': 'Valve Corporation', 'genres': ['rpg', 'action'],
        'platforms': ['PC', 'PS4', 'XBO'],
        'release_year': 2014, 'release_date': '2014-11-18', 'age_rating': '18+',
        'metacritic_score': 85, 'is_featured': False,
    },
    {
        'title': 'Fallout 4', 'slug': 'fallout-4',
        'developer': 'Bethesda Game Studios', 'genres': ['rpg', 'action', 'shooter'],
        'platforms': ['PC', 'PS4', 'XBO'],
        'release_year': 2015, 'release_date': '2015-11-10', 'age_rating': '18+',
        'metacritic_score': 84, 'is_featured': False,
    },
    {
        'title': 'The Elder Scrolls V: Skyrim', 'slug': 'skyrim',
        'developer': 'Bethesda Game Studios', 'genres': ['rpg', 'action', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO', 'NSW'],
        'release_year': 2011, 'release_date': '2011-11-11', 'age_rating': '18+',
        'metacritic_score': 94, 'is_featured': True,
    },
    {
        'title': 'Assassin\'s Creed Valhalla', 'slug': 'assassins-creed-valhalla',
        'developer': 'Valve Corporation', 'genres': ['action', 'adventure', 'rpg'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2020, 'release_date': '2020-11-10', 'age_rating': '18+',
        'metacritic_score': 84, 'is_featured': False,
    },
    {
        'title': 'Far Cry 6', 'slug': 'far-cry-6',
        'developer': 'Valve Corporation', 'genres': ['shooter', 'action', 'adventure'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2021, 'release_date': '2021-10-07', 'age_rating': '18+',
        'metacritic_score': 75, 'is_featured': False,
    },
    {
        'title': 'Watch Dogs: Legion', 'slug': 'watch-dogs-legion',
        'developer': 'Valve Corporation', 'genres': ['action', 'adventure'],
        'platforms': ['PC', 'PS5', 'XSX'],
        'release_year': 2020, 'release_date': '2020-10-29', 'age_rating': '18+',
        'metacritic_score': 76, 'is_featured': False,
    },
]


def get_game_text(slug: str) -> dict:
    """Тексты игры по slug; fallback если slug не найден."""
    if slug in GAME_TEXT:
        return GAME_TEXT[slug]
    return {
        'short_description': 'Популярная игра из каталога GameLib.',
        'description': (
            'Подробное описание для этой игры скоро появится в каталоге. '
            'Пока вы можете посмотреть жанры, платформы и рейтинг на карточке.'
        ),
    }
