"""
Надёжные URL обложек и баннеров (Steam CDN + проверенные прямые ссылки).
Вертикальная обложка — library_600x900, горизонтальный баннер — header / library_hero.
"""

STEAM_CDN = 'https://cdn.akamai.steamstatic.com/steam/apps/{appid}'


def _steam(appid: int) -> dict:
    base = STEAM_CDN.format(appid=appid)
    return {
        'cover': f'{base}/library_600x900_2x.jpg',
        'banner': f'{base}/library_hero_2x.jpg',
    }


#
# slug → данные обложек. Для большинства игр используем Steam CDN
# через _steam(appid). Для нестабильных или не-стимовых игр
# задаём прямые URL вручную.
#
COVER_BY_SLUG: dict[str, dict] = {
    'witcher-3': _steam(292030),
    'elden-ring': _steam(1245620),
    'red-dead-redemption-2': _steam(1174180),
    'the-last-of-us-part-1': _steam(1888930),
    'half-life-alyx': _steam(546560),
    'hades': _steam(1145360),
    'spiderman-2': _steam(2651280),
    'starfield': _steam(1716740),
    'gow-ragnarok': _steam(1593500),
    'hollow-knight': _steam(367520),
    'ghost-of-tsushima': _steam(2215430),
    'portal-2': _steam(620),
    'civilization-vi': _steam(289070),
    'dead-space': _steam(1693980),
    'dragon-age-inquisition': _steam(1237320),
    'monster-hunter-rise': _steam(1446780),
    'crusader-kings-iii': _steam(1158310),
    'cyberpunk-2077': _steam(1091500),
    'baldurs-gate-3': _steam(1086940),
    'metro-exodus': _steam(412020),
    'horizon-forbidden-west': _steam(2420110),
    'sekiro-shadows-die-twice': _steam(814380),
    'dark-souls-iii': _steam(374320),
    'resident-evil-4': _steam(2050650),
    'control': _steam(870780),
    'disco-elysium': _steam(632470),
    'persona-5-royal': _steam(1687950),
    'final-fantasy-xvi': _steam(2515020),
    'doom-eternal': _steam(782330),
    'forza-horizon-5': _steam(1551360),
    'street-fighter-6': _steam(1364780),
    'tekken-8': _steam(1778820),
    'stardew-valley': _steam(413150),
    'celeste': _steam(504230),
    'undertale': _steam(391540),
    'half-life-2': _steam(220),
    'bioshock-infinite': _steam(8870),
    'mass-effect-legendary-edition': _steam(1328670),
    'fallout-4': _steam(377160),
    'skyrim': _steam(489830),
    'assassins-creed-valhalla': _steam(2208920),
    'far-cry-6': _steam(2369390),
    'watch-dogs-legion': _steam(2239550),
    'zelda-totk': {
        'cover': 'https://assets.nintendo.com/image/upload/c_fill,w_400/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/switch/t/the-legend-of-zelda-tears-of-the-kingdom-switch/hero',
        'banner': 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/switch/t/the-legend-of-zelda-tears-of-the-kingdom-switch/hero',
    },
    'bloodborne': {
        'cover': 'https://image.api.playstation.com/vulcan/ap/rnd/202010/0121/AXD2aa3V5vDLS9eF6m1Hk9z0.png',
        'banner': 'https://image.api.playstation.com/games/images/tachyon/000/001/360/0000013600.jpg',
    },
    'gran-turismo-7': {
        'cover': 'https://image.api.playstation.com/vulcan/ap/rnd/202202/2501/L2p2xDevKnZPsOj3X0Q2m1z.png',
        'banner': 'https://gmedia.playstation.com/is/image/SIEPDC/gran-turismo-7-screenshot-01-en-27jan22?$2400px--t$',
    },
    # S.T.A.L.K.E.R. 2 — ручные ссылки, чтобы не было путаницы с Fallout
    'stalker-2': {
        'cover': 'https://cdn.akamai.steamstatic.com/steam/apps/1151340/library_600x900_2x.jpg',
        'banner': 'https://cdn.akamai.steamstatic.com/steam/apps/1151340/library_hero_2x.jpg',
    },
    'fifa-24': _steam(2195250),
    'nba-2k24': _steam(2338770),
    'total-war-warhammer-iii': _steam(1142710),
    # Alan Wake 2 — Epic/console, берём проверенные картинки
    'alan-wake-2': {
        'cover': 'https://image.api.playstation.com/vulcan/ap/rnd/202308/0221/3Wvywgq6Z9eruqbWtaXDpK0N.png',
        'banner': 'https://image.api.playstation.com/vulcan/ap/rnd/202310/1919/6l0RRqtD9h5pz50jdK5Zk90k.png',
    },
}

# Заголовок (lower) → slug в COVER_BY_SLUG
TITLE_ALIASES: dict[str, str] = {
    'metro exodus': 'metro-exodus',
    'сталкер 2: сердце чернобыля': 'stalker-2',
    "baldur's gate 3": 'baldurs-gate-3',
    'cyberpunk 2077': 'cyberpunk-2077',
    'horizon forbidden west': 'horizon-forbidden-west',
    'sekiro: shadows die twice': 'sekiro-shadows-die-twice',
    'dark souls iii': 'dark-souls-iii',
    'resident evil 4': 'resident-evil-4',
    'alan wake 2': 'alan-wake-2',
    'fifa 24': 'fifa-24',
    'nba 2k24': 'nba-2k24',
}


def _normalize_title(title: str) -> str:
    return title.strip().lower()


def resolve_slug(slug: str | None = None, title: str | None = None) -> str | None:
    if slug and slug in COVER_BY_SLUG:
        return slug
    if title:
        key = _normalize_title(title)
        if key in TITLE_ALIASES:
            alias = TITLE_ALIASES[key]
            if isinstance(alias, str):
                return alias if alias in COVER_BY_SLUG else None
        # попытка по slug из title
        from pytils.translit import slugify
        generated = slugify(title)
        if generated in COVER_BY_SLUG:
            return generated
    return slug if slug in COVER_BY_SLUG else None


def get_urls(slug: str | None = None, title: str | None = None) -> dict:
    """Возвращает {'cover': url, 'banner': url} или пустой dict."""
    resolved = resolve_slug(slug, title)
    if not resolved:
        return {}
    data = COVER_BY_SLUG.get(resolved, {})
    return {
        'cover': data.get('cover'),
        'banner': data.get('banner'),
    }


def get_cover_url(slug: str | None = None, title: str | None = None) -> str | None:
    return get_urls(slug, title).get('cover')


def get_banner_url(slug: str | None = None, title: str | None = None) -> str | None:
    urls = get_urls(slug, title)
    return urls.get('banner') or urls.get('cover')
