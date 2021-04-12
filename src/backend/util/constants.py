from enum import Enum


class RouteType(Enum):
    LightRail = 0
    HeavyRail = 1
    CommuterRail = 2
    Bus = 3
    Ferry = 4


class ClientHeaderKeys(Enum):
    Api = 'x-api-key'
    UserAgent = 'user-agent'


class ResponseKeys(Enum):
    Data = 'data'
    Attributes = 'attributes'
    Relationships = 'relationships'
    Id = 'id'


class RequestKeys(Enum):
    pass


class RouteKeys(Enum):
    DirectionDestination = 'direction_destinations'
    DirectionName = 'direction_names'
    Type = 'type'
    Name = 'long_name'
    Line = 'line'


class StopKeys(Enum):
    Name = 'name'


class PredictionKeys(Enum):
    ArrivalTime = 'arrival_time'
    ScheduleRelationShips = 'schedule_relationships'
    DirectionId = 'direction_id'
