from typing import Any, Dict, Optional, TYPE_CHECKING

from discordmenu.embed.components import EmbedThumbnail
from tsutils.menu.pad_view import PadView, PadViewState
from tsutils.query_settings.query_settings import QuerySettings
from tsutils.tsubaki.links import MonsterImage, MonsterLink
from tsutils.tsubaki.monster_header import MonsterHeader

if TYPE_CHECKING:
    from dbcog.models.monster_model import MonsterModel


class PadinfoViewState(PadViewState):
    def __init__(self, original_author_id, menu_type, raw_query, query, qs: QuerySettings, monster: "MonsterModel",
                 extra_state):
        super().__init__(original_author_id, menu_type, raw_query, query, qs, extra_state)
        self.monster = monster

    def serialize(self) -> Dict[str, Any]:
        ret = super().serialize()
        ret.update({
            'resolved_monster_id': self.monster.monster_id,
        })
        return ret


class PadinfoView(PadView):
    @classmethod
    def embed_title(cls, state: PadinfoViewState) -> Optional[str]:
        m = state.monster
        return MonsterHeader.menu_title(m).to_markdown()

    @classmethod
    def embed_url(cls, state: PadinfoViewState):
        return MonsterLink.header_link(state.monster, state.qs)

    @classmethod
    def embed_thumbnail(cls, state: PadinfoViewState) -> Optional[EmbedThumbnail]:
        m = state.monster
        return EmbedThumbnail(MonsterImage.icon(m.monster_id, cachebreak=m.icon_cachebreak))
