from collections import defaultdict, namedtuple
from enum import Enum
from typing import Mapping, Tuple, TypeVar

from dbcog.models.enum_types import AwokenSkills, MonsterType

K = TypeVar('K')
V = TypeVar('V')


def inverse_map(token_map: Mapping[K, Tuple[V]]) -> Mapping[V, Tuple[K]]:
    ret = defaultdict(tuple)
    for k, vs in token_map.items():
        for v in vs:
            ret[v] += (k,)
    return ret


TYPE_MAP = {
    MonsterType.Evolve: ('evolve',),
    MonsterType.Balanced: ('balanced', 'bal', 'balance'),
    MonsterType.Physical: ('physical', 'phys'),
    MonsterType.Healer: ('healer',),
    MonsterType.Dragon: ('dragon', 'dra'),
    MonsterType.God: ('god',),
    MonsterType.Attacker: ('attacker', 'atk'),
    MonsterType.Devil: ('devil', 'dv'),
    MonsterType.Machine: ('machine', 'mech'),
    MonsterType.Awoken: ('awokentype', 'awotype'),
    MonsterType.Enhance: ('enhance', 'fodder', 'enh'),
    MonsterType.Vendor: ('vendor', 'redeemable'),
}


class EvoTypes(Enum):
    BASE = 'Base'
    EVO = 'Evolved'
    UVO = 'Ulimate'
    UUVO = 'Super Ultimate'
    EQUIP = 'Equip'
    BASETRANS = 'Base Transform'
    TRANS = 'Transform'
    AWOKEN = 'Awoken'
    MEGA = 'Mega Awoken'
    REVO = 'Reincarnated'
    SREVO = 'Super Reincarnated'
    PIXEL = 'Pixel'
    NONPIXEL = 'Nonpixel'
    CHIBI = 'Chibi'


EVO_MAP = {
    EvoTypes.BASE: ('base',),
    EvoTypes.EVO: ('evo', 'evolved'),
    EvoTypes.UVO: ('uvo', 'ult', 'ultimate', 'uevo'),
    EvoTypes.UUVO: ('uuvo', 'uult', 'uultimate', 'uuevo', 'suvo'),
    EvoTypes.EQUIP: ('equip', 'assist', 'eq'),
    EvoTypes.BASETRANS: ('transformbase', 'transbase'),
    EvoTypes.TRANS: ('transform', 'trans', 'transformed', 'xf', 'xform', 'tf'),
    EvoTypes.AWOKEN: ('awoken', 'awo', 'a'),
    EvoTypes.MEGA: ('mega', 'mawoken', 'mawo', 'ma', 'megaawoken'),
    EvoTypes.REVO: ('revo', 'reincarnated', 'rv'),
    EvoTypes.SREVO: ('srevo', 'super', 'sr', 'superreincarnated'),
    EvoTypes.PIXEL: ('pixel', 'p', 'dot', 'px'),
    EvoTypes.NONPIXEL: ('nonpixel', 'np'),
    EvoTypes.CHIBI: ('chibi', 'mini'),
}


class MiscModifiers(Enum):
    STORY = 'Story'
    FARMABLE = 'Farmable'
    TRADEABLE = 'Tradeable'
    REM = 'In REM'
    PEM = 'In PEM'
    ADPEM = 'In AdPEM'
    INADPEM = 'This evo is in AdPEM'
    MP = 'MP'
    INJP = 'In JP Server'
    ONLYJP = 'Only in JP Server'
    INNA = 'In NA Server'
    ONLYNA = 'Only in NA Server'
    REGULAR = 'Metaseries: REGULAR'
    EVENT = 'Metaseries: Event'
    SEASONAL = 'Metaseries: Seasonal'
    COLLAB = 'Metaseries: Collab'
    NEW = 'Newest monster in series'
    ORBSKIN = 'Grants an orb skin'
    BGM = 'Grants a BGM'
    MEDIA = 'Grants a form of media'  # orb skin or BGM
    ANIMATED = 'Animated monster'
    MEDAL_EXC = 'Exchangable for vendor mats'
    BLACK_MEDAL = 'Exchangable for black medals'
    CURRENT_EXCHANGE_JP = 'Currently exchangable in JP'
    CURRENT_EXCHANGE_NA = 'Currently exchangable in NA'
    CURRENT_EXCHANGE_KR = 'Currently exchangable in KR'
    PERMANENT_EXCHANGE = 'Permanently exchangable'
    TEMP_EXCHANGE = 'Temporarily exchangable at some point in time'
    HAS_GEM = 'Has an evo gem'
    GFESHOP = 'GFE exchangable'
    GFESHOP6S = '6* GFE exchangable'
    GFESHOP7S = '7* GFE exchangable'
    NONULLATTR = 'Has no null attributes'


MISC_MAP = {
    MiscModifiers.STORY: ('story',),
    MiscModifiers.FARMABLE: ('farmable',),
    MiscModifiers.TRADEABLE: ('tradeable', 'tradable'),
    MiscModifiers.REM: ('rem',),
    MiscModifiers.PEM: ('pem',),
    MiscModifiers.ADPEM: ('adpem', 'adpem'),
    MiscModifiers.INADPEM: ('invem', 'inadpem'),
    MiscModifiers.MP: ('mp',),
    MiscModifiers.INJP: ('injp',),
    MiscModifiers.INNA: ('inna',),
    MiscModifiers.ONLYJP: ('jp',),
    MiscModifiers.ONLYNA: ('na',),
    MiscModifiers.REGULAR: ('regular',),
    MiscModifiers.EVENT: ('event',),
    MiscModifiers.SEASONAL: ('seasonal',),
    MiscModifiers.COLLAB: ('collab',),
    MiscModifiers.NEW: ('new',),
    MiscModifiers.ORBSKIN: ('orbskin',),
    MiscModifiers.BGM: ('bgm',),
    MiscModifiers.MEDIA: ('media',),
    MiscModifiers.ANIMATED: ('animated',),
    MiscModifiers.MEDAL_EXC: ('medal', 'shop'),
    MiscModifiers.BLACK_MEDAL: ('blackmedal',),
    MiscModifiers.CURRENT_EXCHANGE_JP: ('nowshopjp', 'shopnowjp'),
    MiscModifiers.CURRENT_EXCHANGE_NA: ('nowshopna', 'shopnowna'),
    MiscModifiers.CURRENT_EXCHANGE_KR: ('nowshopkr', 'shopnowkr'),
    MiscModifiers.PERMANENT_EXCHANGE: ('permshop', 'shopperm'),
    MiscModifiers.TEMP_EXCHANGE: ('tempshop', 'shoptemp'),
    MiscModifiers.HAS_GEM: ('hasgem',),
    MiscModifiers.GFESHOP: ('gfeshop',),
    MiscModifiers.GFESHOP6S: ('6*gfeshop', 'gfeshop6*'),
    MiscModifiers.GFESHOP7S: ('7*gfeshop', 'gfeshop7*'),
    MiscModifiers.NONULLATTR: ('3ping', '!!!'),
}

MULTI_WORD_TOKENS = {tuple(ts.split()) for ts in {
    'super reincarnated',
    'mega awoken',
    'orb skin',
    'black medal',
}}

ALL_TOKEN_DICTS = {
    *TYPE_MAP.values(),
    *EVO_MAP.values(),
    *MISC_MAP.values(),
}

KNOWN_MODIFIERS = {v for vs in ALL_TOKEN_DICTS for v in vs}

EVO_TOKENS = {*sum(EVO_MAP.values(), ())}
TYPE_TOKENS = {*sum(TYPE_MAP.values(), ())}

OTHER_HIDDEN_TOKENS = set() \
    .union(EVO_TOKENS) \
    .union(TYPE_TOKENS)

LEGAL_END_TOKENS = {
    "equip",
    "assist",
    "eq",
}

# These tokens have been found to be harmful and will only be added to monsters explicitly.
HAZARDOUS_IN_NAME_MODS = {
    "reincarnated",
    "awoken",
    "equip",
}

PROBLEMATIC_SERIES_TOKENS = {
    "sonia",
    "odin",
    "metatron",
    "kali",
    "fenrir",
    "sherias",
}

# This probably doesn't belong in here
EquivalentAwakeningData = namedtuple("EquivalentAwakeningData", "awoken_skill value")
EQUIVALENT_AWOKENSKILL_MAP = {
    AwokenSkills.UNBINDABLE: EquivalentAwakeningData(AwokenSkills.BINDRES, 2),
    AwokenSkills.EXTMOVEPLUS: EquivalentAwakeningData(AwokenSkills.EXTMOVE, 2),
    AwokenSkills.SKILLBOOSTPLUS: EquivalentAwakeningData(AwokenSkills.SKILLBOOST, 2),
    AwokenSkills.SKILLCHARGEPLUS: EquivalentAwakeningData(AwokenSkills.SKILLCHARGE, 2),
    AwokenSkills.AUTOHEAL: EquivalentAwakeningData(AwokenSkills.AUTOHEAL, 2),
    AwokenSkills.ENHANCEDREDPLUS: EquivalentAwakeningData(AwokenSkills.ENHANCEDRED, 2),
    AwokenSkills.ENHANCEDBLUEPLUS: EquivalentAwakeningData(AwokenSkills.ENHANCEDBLUE, 2),
    AwokenSkills.ENHANCEDGREENPLUS: EquivalentAwakeningData(AwokenSkills.ENHANCEDGREEN, 2),
    AwokenSkills.ENHANCEDLIGHTPLUS: EquivalentAwakeningData(AwokenSkills.ENHANCEDLIGHT, 2),
    AwokenSkills.ENHANCEDDARKPLUS: EquivalentAwakeningData(AwokenSkills.ENHANCEDDARK, 2),
    AwokenSkills.ENHCOMBO7CPLUS: EquivalentAwakeningData(AwokenSkills.ENHCOMBO7C, 2),
    AwokenSkills.VDPPLUS: EquivalentAwakeningData(AwokenSkills.VDP, 2),
    AwokenSkills.CROSSATTACKPLUS: EquivalentAwakeningData(AwokenSkills.CROSSATTACK, 2),
    AwokenSkills.ENHCOMBO10CPLUS: EquivalentAwakeningData(AwokenSkills.ENHCOMBO10C, 2),
    AwokenSkills.ATTR3BOOSTPLUS: EquivalentAwakeningData(AwokenSkills.ATTR3BOOST, 2),
    AwokenSkills.ATTR4BOOSTPLUS: EquivalentAwakeningData(AwokenSkills.ATTR4BOOST, 2),
    AwokenSkills.ATTR5BOOSTPLUS: EquivalentAwakeningData(AwokenSkills.ATTR5BOOST, 2),
    AwokenSkills.BINDRESPLUS: EquivalentAwakeningData(AwokenSkills.BINDRES, 2),
    AwokenSkills.REDROWX3: EquivalentAwakeningData(AwokenSkills.REDROW, 3),
    AwokenSkills.BLUEROWX3: EquivalentAwakeningData(AwokenSkills.BLUEROW, 3),
    AwokenSkills.GREENROWX3: EquivalentAwakeningData(AwokenSkills.GREENROW, 3),
    AwokenSkills.LIGHTROWX3: EquivalentAwakeningData(AwokenSkills.LIGHTROW, 3),
    AwokenSkills.DARKROWX3: EquivalentAwakeningData(AwokenSkills.DARKROW, 3),
    AwokenSkills.REDCOMBOCOUNTPLUS: EquivalentAwakeningData(AwokenSkills.REDCOMBOCOUNT, 2),
    AwokenSkills.BLUECOMBOCOUNTPLUS: EquivalentAwakeningData(AwokenSkills.BLUECOMBOCOUNT, 2),
    AwokenSkills.GREENCOMBOCOUNTPLUS: EquivalentAwakeningData(AwokenSkills.GREENCOMBOCOUNT, 2),
    AwokenSkills.LIGHTCOMBOCOUNTPLUS: EquivalentAwakeningData(AwokenSkills.LIGHTCOMBOCOUNT, 2),
    AwokenSkills.DARKCOMBOCOUNTPLUS: EquivalentAwakeningData(AwokenSkills.DARKCOMBOCOUNT, 2),
}

NUMERIC_MONSTER_ATTRIBUTE_ALIASES = {
    (('monster_no',),): ('monsterid', 'monsterno', 'monster#'),
    (('base_evo_id',),): ('baseid',),
    (('superawakening_count',),): ('sacount',),
    (('leader_skill', 'leader_skill_id'),): ('lsid',),
    (('active_skill', 'active_skill_id'),): ('asid',),
    (('series', 'series_id'),): ('sid', 'seriesid'),
    (('rarity',),): ('rarity', 'rare'),
    (('series_id',),): ('seriesid', 'series#'),
    (('rcv_min',),): ('minrcv',),
    (('buy_mp',),): ('buymp',),
    (('sell_mp',),): ('sellmp',),
    (('sell_gold',),): ('gold', 'coins'),
    (('cost',),): ('cost', 'teamcost'),
    (('exp',),): ('exp', 'exptomax', 'xptomax'),
    (('fodder_exp',),): ('fodderexp',),
    (('level',),): ('maxlvl', 'maxlevel'),
    (('latent_slots',),): ('latentslots',),
    (('hp_max',),): ('hp', 'maxhp'),
    (('atk_max',),): ('atk', 'maxatk'),
    (('rcv_max',),): ('rcv', 'maxrcv'),
    (('hp_min',),): ('minhp',),
    (('atk_min',),): ('minatk',),
    (('rcv_min',),): ('minrcv',),
}
NUMERIC_MONSTER_ATTRIBUTE_NAMES = {*sum(NUMERIC_MONSTER_ATTRIBUTE_ALIASES.values(), ())}

STRING_MONSTER_ATTRIBUTE_ALIASES = {
    (('name_en',),
     ('name_ja',)): ('monstername', 'cardname'),
    (('leader_skill', 'name_en'),
     ('leader_skill', 'name_ja'),
     ('active_skill', 'name_en'),
     ('active_skill', 'name_ja')): ('skillname',),
    (('leader_skill', 'desc_en'),
     ('leader_skill', 'desc_ja'),
     ('active_skill', 'desc_en'),
     ('active_skill', 'desc_ja')): ('skilltext',),
    (('leader_skill', 'name_en'),
     ('leader_skill', 'name_ja')): ('lsname',),
    (('leader_skill', 'desc_en'),
     ('leader_skill', 'desc_ja')): ('lsdesc',),
    (('active_skill', 'name_en'),
     ('active_skill', 'name_ja')): ('asname',),
    (('active_skill', 'desc_en'),
     ('active_skill', 'desc_ja')): ('asdesc',),
    (('series', 'name_en'),): ('seriesname',),
    (('history_us',),): ('regdate', 'dateadded'),
}
STRING_MONSTER_ATTRIBUTE_NAMES = {*sum(STRING_MONSTER_ATTRIBUTE_ALIASES.values(), ())}

BOOL_MONSTER_ATTRIBUTE_ALIASES = {}
BOOL_MONSTER_ATTRIBUTE_NAMES = {*sum(BOOL_MONSTER_ATTRIBUTE_ALIASES.values(), ())}

MONSTER_CLASS_ATTRIBUTES = {
    *sum(NUMERIC_MONSTER_ATTRIBUTE_ALIASES, ()),
    *sum(STRING_MONSTER_ATTRIBUTE_ALIASES, ()),
    *sum(BOOL_MONSTER_ATTRIBUTE_NAMES, ()),
}
MONSTER_ATTR_ALIAS_TO_ATTR_MAP = {v: k for k, vs in {
    **NUMERIC_MONSTER_ATTRIBUTE_ALIASES,
    **STRING_MONSTER_ATTRIBUTE_ALIASES,
    **BOOL_MONSTER_ATTRIBUTE_ALIASES,
}.items() for v in vs}
