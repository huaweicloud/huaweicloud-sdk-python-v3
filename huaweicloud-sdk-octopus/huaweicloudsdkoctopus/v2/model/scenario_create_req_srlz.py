# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScenarioCreateReqSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gen_scenario': 'str',
        'description': 'MutableFileSrlz',
        'file': 'FileCreateReqSrlz',
        'simulator': 'SimulatorEnum',
        'version': 'ScenarioVersionEnum',
        'map_filename': 'str',
        'model_filename': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'name': 'str',
        'priority': 'PriorityEnum',
        'map': 'str',
        'model': 'str'
    }

    attribute_map = {
        'gen_scenario': 'gen_scenario',
        'description': 'description',
        'file': 'file',
        'simulator': 'simulator',
        'version': 'version',
        'map_filename': 'map_filename',
        'model_filename': 'model_filename',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'name': 'name',
        'priority': 'priority',
        'map': 'map',
        'model': 'model'
    }

    def __init__(self, gen_scenario=None, description=None, file=None, simulator=None, version=None, map_filename=None, model_filename=None, user_id=None, user_name=None, name=None, priority=None, map=None, model=None):
        """ScenarioCreateReqSrlz

        The model defined in huaweicloud sdk

        :param gen_scenario: 泛化场景
        :type gen_scenario: str
        :param description: 
        :type description: :class:`huaweicloudsdkoctopus.v2.MutableFileSrlz`
        :param file: 文件
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateReqSrlz`
        :param simulator: 
        :type simulator: :class:`huaweicloudsdkoctopus.v2.SimulatorEnum`
        :param version: 
        :type version: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        :param map_filename: 地图文件名
        :type map_filename: str
        :param model_filename: 模型文件名
        :type model_filename: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param name: 名称
        :type name: str
        :param priority: 
        :type priority: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        :param map: 地图
        :type map: str
        :param model: 模型
        :type model: str
        """
        
        

        self._gen_scenario = None
        self._description = None
        self._file = None
        self._simulator = None
        self._version = None
        self._map_filename = None
        self._model_filename = None
        self._user_id = None
        self._user_name = None
        self._name = None
        self._priority = None
        self._map = None
        self._model = None
        self.discriminator = None

        self.gen_scenario = gen_scenario
        self.description = description
        self.file = file
        self.simulator = simulator
        self.version = version
        self.map_filename = map_filename
        self.model_filename = model_filename
        self.user_id = user_id
        self.user_name = user_name
        self.name = name
        if priority is not None:
            self.priority = priority
        self.map = map
        self.model = model

    @property
    def gen_scenario(self):
        """Gets the gen_scenario of this ScenarioCreateReqSrlz.

        泛化场景

        :return: The gen_scenario of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._gen_scenario

    @gen_scenario.setter
    def gen_scenario(self, gen_scenario):
        """Sets the gen_scenario of this ScenarioCreateReqSrlz.

        泛化场景

        :param gen_scenario: The gen_scenario of this ScenarioCreateReqSrlz.
        :type gen_scenario: str
        """
        self._gen_scenario = gen_scenario

    @property
    def description(self):
        """Gets the description of this ScenarioCreateReqSrlz.

        :return: The description of this ScenarioCreateReqSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.MutableFileSrlz`
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScenarioCreateReqSrlz.

        :param description: The description of this ScenarioCreateReqSrlz.
        :type description: :class:`huaweicloudsdkoctopus.v2.MutableFileSrlz`
        """
        self._description = description

    @property
    def file(self):
        """Gets the file of this ScenarioCreateReqSrlz.

        文件

        :return: The file of this ScenarioCreateReqSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.FileCreateReqSrlz`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ScenarioCreateReqSrlz.

        文件

        :param file: The file of this ScenarioCreateReqSrlz.
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateReqSrlz`
        """
        self._file = file

    @property
    def simulator(self):
        """Gets the simulator of this ScenarioCreateReqSrlz.

        :return: The simulator of this ScenarioCreateReqSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.SimulatorEnum`
        """
        return self._simulator

    @simulator.setter
    def simulator(self, simulator):
        """Sets the simulator of this ScenarioCreateReqSrlz.

        :param simulator: The simulator of this ScenarioCreateReqSrlz.
        :type simulator: :class:`huaweicloudsdkoctopus.v2.SimulatorEnum`
        """
        self._simulator = simulator

    @property
    def version(self):
        """Gets the version of this ScenarioCreateReqSrlz.

        :return: The version of this ScenarioCreateReqSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ScenarioCreateReqSrlz.

        :param version: The version of this ScenarioCreateReqSrlz.
        :type version: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        """
        self._version = version

    @property
    def map_filename(self):
        """Gets the map_filename of this ScenarioCreateReqSrlz.

        地图文件名

        :return: The map_filename of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._map_filename

    @map_filename.setter
    def map_filename(self, map_filename):
        """Sets the map_filename of this ScenarioCreateReqSrlz.

        地图文件名

        :param map_filename: The map_filename of this ScenarioCreateReqSrlz.
        :type map_filename: str
        """
        self._map_filename = map_filename

    @property
    def model_filename(self):
        """Gets the model_filename of this ScenarioCreateReqSrlz.

        模型文件名

        :return: The model_filename of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._model_filename

    @model_filename.setter
    def model_filename(self, model_filename):
        """Sets the model_filename of this ScenarioCreateReqSrlz.

        模型文件名

        :param model_filename: The model_filename of this ScenarioCreateReqSrlz.
        :type model_filename: str
        """
        self._model_filename = model_filename

    @property
    def user_id(self):
        """Gets the user_id of this ScenarioCreateReqSrlz.

        用户id

        :return: The user_id of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ScenarioCreateReqSrlz.

        用户id

        :param user_id: The user_id of this ScenarioCreateReqSrlz.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this ScenarioCreateReqSrlz.

        用户名

        :return: The user_name of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ScenarioCreateReqSrlz.

        用户名

        :param user_name: The user_name of this ScenarioCreateReqSrlz.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def name(self):
        """Gets the name of this ScenarioCreateReqSrlz.

        名称

        :return: The name of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScenarioCreateReqSrlz.

        名称

        :param name: The name of this ScenarioCreateReqSrlz.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        """Gets the priority of this ScenarioCreateReqSrlz.

        :return: The priority of this ScenarioCreateReqSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ScenarioCreateReqSrlz.

        :param priority: The priority of this ScenarioCreateReqSrlz.
        :type priority: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        self._priority = priority

    @property
    def map(self):
        """Gets the map of this ScenarioCreateReqSrlz.

        地图

        :return: The map of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this ScenarioCreateReqSrlz.

        地图

        :param map: The map of this ScenarioCreateReqSrlz.
        :type map: str
        """
        self._map = map

    @property
    def model(self):
        """Gets the model of this ScenarioCreateReqSrlz.

        模型

        :return: The model of this ScenarioCreateReqSrlz.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ScenarioCreateReqSrlz.

        模型

        :param model: The model of this ScenarioCreateReqSrlz.
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
        if not isinstance(other, ScenarioCreateReqSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
