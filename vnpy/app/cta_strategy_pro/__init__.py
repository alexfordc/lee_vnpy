from pathlib import Path

from vnpy.trader.app import BaseApp
from vnpy.app.cta_strategy_pro.base import APP_NAME, StopOrder

from vnpy.app.cta_strategy_pro.engine import CtaEngine

from vnpy.app.cta_strategy_pro.template import (
    Direction,
    Offset,
    Status,
    Color,
    TickData,
    BarData,
    TradeData,
    OrderData,
    CtaTemplate,
    CtaSignal,
    TargetPosTemplate,
    CtaProTemplate,
    CtaProFutureTemplate,
    CtaPosition,
    CtaPolicy,
    CtaGrid,
    CtaGridTrade)  # noqa
from vnpy.trader.utility import BarGenerator, ArrayManager  # noqa
from vnpy.app.cta_strategy_pro.cta_line_bar import CtaMinuteBar

from vnpy.app.cta_strategy_pro.template_spread import CtaSpreadTemplate


class CtaStrategyProApp(BaseApp):
    """"""

    app_name = APP_NAME
    app_module = __module__
    app_path = Path(__file__).parent
    display_name = "CTA策略PRO"
    engine_class = CtaEngine
    widget_name = "CtaManager"
    icon_name = "cta.ico"
