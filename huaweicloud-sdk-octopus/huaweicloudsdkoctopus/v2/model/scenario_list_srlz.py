# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScenarioListSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'labels': 'list[LabelBriefSrlz]',
        'gen_scenario': 'str',
        'road_scenario': 'str',
        'simulator': 'str',
        'version': 'ScenarioVersionEnum',
        'filename': 'str',
        'map_filename': 'str',
        'model_filename': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'name': 'str',
        'priority': 'PriorityEnum',
        'status': 'ScenarioStatusEnum',
        'map': 'str',
        'model': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'labels': 'labels',
        'gen_scenario': 'gen_scenario',
        'road_scenario': 'road_scenario',
        'simulator': 'simulator',
        'version': 'version',
        'filename': 'filename',
        'map_filename': 'map_filename',
        'model_filename': 'model_filename',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'name': 'name',
        'priority': 'priority',
        'status': 'status',
        'map': 'map',
        'model': 'model'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, labels=None, gen_scenario=None, road_scenario=None, simulator=None, version=None, filename=None, map_filename=None, model_filename=None, user_id=None, user_name=None, name=None, priority=None, status=None, map=None, model=None):
        r"""ScenarioListSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param labels: 
        :type labels: list[:class:`huaweicloudsdkoctopus.v2.LabelBriefSrlz`]
        :param gen_scenario: 
        :type gen_scenario: str
        :param road_scenario: 
        :type road_scenario: str
        :param simulator: 仿真器名称,取值范围:A,B,C,D,E
        :type simulator: str
        :param version: 
        :type version: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        :param filename: 
        :type filename: str
        :param map_filename: 
        :type map_filename: str
        :param model_filename: 
        :type model_filename: str
        :param user_id: 
        :type user_id: str
        :param user_name: 
        :type user_name: str
        :param name: 
        :type name: str
        :param priority: 
        :type priority: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        :param status: 
        :type status: :class:`huaweicloudsdkoctopus.v2.ScenarioStatusEnum`
        :param map: 
        :type map: str
        :param model: 
        :type model: str
        """
        
        

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._labels = None
        self._gen_scenario = None
        self._road_scenario = None
        self._simulator = None
        self._version = None
        self._filename = None
        self._map_filename = None
        self._model_filename = None
        self._user_id = None
        self._user_name = None
        self._name = None
        self._priority = None
        self._status = None
        self._map = None
        self._model = None
        self.discriminator = None

        self.url = url
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.labels = labels
        self.gen_scenario = gen_scenario
        self.road_scenario = road_scenario
        self.simulator = simulator
        self.version = version
        self.filename = filename
        self.map_filename = map_filename
        self.model_filename = model_filename
        self.user_id = user_id
        self.user_name = user_name
        self.name = name
        if priority is not None:
            self.priority = priority
        if status is not None:
            self.status = status
        self.map = map
        self.model = model

    @property
    def url(self):
        r"""Gets the url of this ScenarioListSrlz.

        :return: The url of this ScenarioListSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ScenarioListSrlz.

        :param url: The url of this ScenarioListSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this ScenarioListSrlz.

        :return: The id of this ScenarioListSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScenarioListSrlz.

        :param id: The id of this ScenarioListSrlz.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ScenarioListSrlz.

        :return: The created_at of this ScenarioListSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ScenarioListSrlz.

        :param created_at: The created_at of this ScenarioListSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ScenarioListSrlz.

        :return: The updated_at of this ScenarioListSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ScenarioListSrlz.

        :param updated_at: The updated_at of this ScenarioListSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def labels(self):
        r"""Gets the labels of this ScenarioListSrlz.

        :return: The labels of this ScenarioListSrlz.
        :rtype: list[:class:`huaweicloudsdkoctopus.v2.LabelBriefSrlz`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ScenarioListSrlz.

        :param labels: The labels of this ScenarioListSrlz.
        :type labels: list[:class:`huaweicloudsdkoctopus.v2.LabelBriefSrlz`]
        """
        self._labels = labels

    @property
    def gen_scenario(self):
        r"""Gets the gen_scenario of this ScenarioListSrlz.

        :return: The gen_scenario of this ScenarioListSrlz.
        :rtype: str
        """
        return self._gen_scenario

    @gen_scenario.setter
    def gen_scenario(self, gen_scenario):
        r"""Sets the gen_scenario of this ScenarioListSrlz.

        :param gen_scenario: The gen_scenario of this ScenarioListSrlz.
        :type gen_scenario: str
        """
        self._gen_scenario = gen_scenario

    @property
    def road_scenario(self):
        r"""Gets the road_scenario of this ScenarioListSrlz.

        :return: The road_scenario of this ScenarioListSrlz.
        :rtype: str
        """
        return self._road_scenario

    @road_scenario.setter
    def road_scenario(self, road_scenario):
        r"""Sets the road_scenario of this ScenarioListSrlz.

        :param road_scenario: The road_scenario of this ScenarioListSrlz.
        :type road_scenario: str
        """
        self._road_scenario = road_scenario

    @property
    def simulator(self):
        r"""Gets the simulator of this ScenarioListSrlz.

        仿真器名称,取值范围:A,B,C,D,E

        :return: The simulator of this ScenarioListSrlz.
        :rtype: str
        """
        return self._simulator

    @simulator.setter
    def simulator(self, simulator):
        r"""Sets the simulator of this ScenarioListSrlz.

        仿真器名称,取值范围:A,B,C,D,E

        :param simulator: The simulator of this ScenarioListSrlz.
        :type simulator: str
        """
        self._simulator = simulator

    @property
    def version(self):
        r"""Gets the version of this ScenarioListSrlz.

        :return: The version of this ScenarioListSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ScenarioListSrlz.

        :param version: The version of this ScenarioListSrlz.
        :type version: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        """
        self._version = version

    @property
    def filename(self):
        r"""Gets the filename of this ScenarioListSrlz.

        :return: The filename of this ScenarioListSrlz.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this ScenarioListSrlz.

        :param filename: The filename of this ScenarioListSrlz.
        :type filename: str
        """
        self._filename = filename

    @property
    def map_filename(self):
        r"""Gets the map_filename of this ScenarioListSrlz.

        :return: The map_filename of this ScenarioListSrlz.
        :rtype: str
        """
        return self._map_filename

    @map_filename.setter
    def map_filename(self, map_filename):
        r"""Sets the map_filename of this ScenarioListSrlz.

        :param map_filename: The map_filename of this ScenarioListSrlz.
        :type map_filename: str
        """
        self._map_filename = map_filename

    @property
    def model_filename(self):
        r"""Gets the model_filename of this ScenarioListSrlz.

        :return: The model_filename of this ScenarioListSrlz.
        :rtype: str
        """
        return self._model_filename

    @model_filename.setter
    def model_filename(self, model_filename):
        r"""Sets the model_filename of this ScenarioListSrlz.

        :param model_filename: The model_filename of this ScenarioListSrlz.
        :type model_filename: str
        """
        self._model_filename = model_filename

    @property
    def user_id(self):
        r"""Gets the user_id of this ScenarioListSrlz.

        :return: The user_id of this ScenarioListSrlz.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ScenarioListSrlz.

        :param user_id: The user_id of this ScenarioListSrlz.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ScenarioListSrlz.

        :return: The user_name of this ScenarioListSrlz.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ScenarioListSrlz.

        :param user_name: The user_name of this ScenarioListSrlz.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def name(self):
        r"""Gets the name of this ScenarioListSrlz.

        :return: The name of this ScenarioListSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScenarioListSrlz.

        :param name: The name of this ScenarioListSrlz.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        r"""Gets the priority of this ScenarioListSrlz.

        :return: The priority of this ScenarioListSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ScenarioListSrlz.

        :param priority: The priority of this ScenarioListSrlz.
        :type priority: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        self._priority = priority

    @property
    def status(self):
        r"""Gets the status of this ScenarioListSrlz.

        :return: The status of this ScenarioListSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.ScenarioStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScenarioListSrlz.

        :param status: The status of this ScenarioListSrlz.
        :type status: :class:`huaweicloudsdkoctopus.v2.ScenarioStatusEnum`
        """
        self._status = status

    @property
    def map(self):
        r"""Gets the map of this ScenarioListSrlz.

        :return: The map of this ScenarioListSrlz.
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        r"""Sets the map of this ScenarioListSrlz.

        :param map: The map of this ScenarioListSrlz.
        :type map: str
        """
        self._map = map

    @property
    def model(self):
        r"""Gets the model of this ScenarioListSrlz.

        :return: The model of this ScenarioListSrlz.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this ScenarioListSrlz.

        :param model: The model of this ScenarioListSrlz.
        :type model: str
        """
        self._model = model

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScenarioListSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
