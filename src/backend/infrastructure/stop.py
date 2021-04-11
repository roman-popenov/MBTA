from src.backend.util.constants import StopKeys


class Stop(object):
    """ This class represents a stop. """

    all_resources_path = 'stops'
    resource_name = 'stop'

    def __init__(self, id, attributes, relationships):
        self.id = id
        self.attributes = attributes
        self.relationships = relationships

    @property
    def name(self):
        """ Stop friendly name. """

        return self.attributes[StopKeys.Name.value]
