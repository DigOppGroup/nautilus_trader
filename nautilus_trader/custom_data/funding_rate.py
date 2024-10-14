from nautilus_trader.core.data import Data
from nautilus_trader.model.custom import customdataclass
from nautilus_trader.model.identifiers import InstrumentId


@customdataclass
class FundingRateData(Data):
    instrument_id: InstrumentId
    funding_rate: str
    funding_time: str
    is_last: bool = False
