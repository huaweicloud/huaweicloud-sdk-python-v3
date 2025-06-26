# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSimSmScenariosResponse(SdkResponse):

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
        'description': 'MutableFileSrlz',
        'file': 'FileCreateSrlz',
        'simulator': 'str',
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
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'labels': 'labels',
        'gen_scenario': 'gen_scenario',
        'road_scenario': 'road_scenario',
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

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, labels=None, gen_scenario=None, road_scenario=None, description=None, file=None, simulator=None, version=None, map_filename=None, model_filename=None, user_id=None, user_name=None, name=None, priority=None, map=None, model=None):
        r"""CreateSimSmScenariosResponse

        The model defined in huaweicloud sdk

        :param url: 地址
        :type url: str
        :param id: ID
        :type id: int
        :param created_at: 创建时间
        :type created_at: float
        :param updated_at: 更新时间
        :type updated_at: float
        :param labels: 标签
        :type labels: list[:class:`huaweicloudsdkoctopus.v2.LabelBriefSrlz`]
        :param gen_scenario: 泛化场景
        :type gen_scenario: str
        :param road_scenario: 路采场景
        :type road_scenario: str
        :param description: 
        :type description: :class:`huaweicloudsdkoctopus.v2.MutableFileSrlz`
        :param file: 文件
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        :param simulator: 仿真器名称,取值范围:A,B,C,D,E
        :type simulator: str
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
        
        super(CreateSimSmScenariosResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._labels = None
        self._gen_scenario = None
        self._road_scenario = None
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

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if labels is not None:
            self.labels = labels
        self.gen_scenario = gen_scenario
        if road_scenario is not None:
            self.road_scenario = road_scenario
        if description is not None:
            self.description = description
        self.file = file
        if simulator is not None:
            self.simulator = simulator
        if version is not None:
            self.version = version
        self.map_filename = map_filename
        self.model_filename = model_filename
        self.user_id = user_id
        self.user_name = user_name
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        self.map = map
        self.model = model

    @property
    def url(self):
        r"""Gets the url of this CreateSimSmScenariosResponse.

        地址

        :return: The url of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateSimSmScenariosResponse.

        地址

        :param url: The url of this CreateSimSmScenariosResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this CreateSimSmScenariosResponse.

        ID

        :return: The id of this CreateSimSmScenariosResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSimSmScenariosResponse.

        ID

        :param id: The id of this CreateSimSmScenariosResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateSimSmScenariosResponse.

        创建时间

        :return: The created_at of this CreateSimSmScenariosResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateSimSmScenariosResponse.

        创建时间

        :param created_at: The created_at of this CreateSimSmScenariosResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateSimSmScenariosResponse.

        更新时间

        :return: The updated_at of this CreateSimSmScenariosResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateSimSmScenariosResponse.

        更新时间

        :param updated_at: The updated_at of this CreateSimSmScenariosResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def labels(self):
        r"""Gets the labels of this CreateSimSmScenariosResponse.

        标签

        :return: The labels of this CreateSimSmScenariosResponse.
        :rtype: list[:class:`huaweicloudsdkoctopus.v2.LabelBriefSrlz`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateSimSmScenariosResponse.

        标签

        :param labels: The labels of this CreateSimSmScenariosResponse.
        :type labels: list[:class:`huaweicloudsdkoctopus.v2.LabelBriefSrlz`]
        """
        self._labels = labels

    @property
    def gen_scenario(self):
        r"""Gets the gen_scenario of this CreateSimSmScenariosResponse.

        泛化场景

        :return: The gen_scenario of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._gen_scenario

    @gen_scenario.setter
    def gen_scenario(self, gen_scenario):
        r"""Sets the gen_scenario of this CreateSimSmScenariosResponse.

        泛化场景

        :param gen_scenario: The gen_scenario of this CreateSimSmScenariosResponse.
        :type gen_scenario: str
        """
        self._gen_scenario = gen_scenario

    @property
    def road_scenario(self):
        r"""Gets the road_scenario of this CreateSimSmScenariosResponse.

        路采场景

        :return: The road_scenario of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._road_scenario

    @road_scenario.setter
    def road_scenario(self, road_scenario):
        r"""Sets the road_scenario of this CreateSimSmScenariosResponse.

        路采场景

        :param road_scenario: The road_scenario of this CreateSimSmScenariosResponse.
        :type road_scenario: str
        """
        self._road_scenario = road_scenario

    @property
    def description(self):
        r"""Gets the description of this CreateSimSmScenariosResponse.

        :return: The description of this CreateSimSmScenariosResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.MutableFileSrlz`
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSimSmScenariosResponse.

        :param description: The description of this CreateSimSmScenariosResponse.
        :type description: :class:`huaweicloudsdkoctopus.v2.MutableFileSrlz`
        """
        self._description = description

    @property
    def file(self):
        r"""Gets the file of this CreateSimSmScenariosResponse.

        文件

        :return: The file of this CreateSimSmScenariosResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this CreateSimSmScenariosResponse.

        文件

        :param file: The file of this CreateSimSmScenariosResponse.
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        """
        self._file = file

    @property
    def simulator(self):
        r"""Gets the simulator of this CreateSimSmScenariosResponse.

        仿真器名称,取值范围:A,B,C,D,E

        :return: The simulator of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._simulator

    @simulator.setter
    def simulator(self, simulator):
        r"""Sets the simulator of this CreateSimSmScenariosResponse.

        仿真器名称,取值范围:A,B,C,D,E

        :param simulator: The simulator of this CreateSimSmScenariosResponse.
        :type simulator: str
        """
        self._simulator = simulator

    @property
    def version(self):
        r"""Gets the version of this CreateSimSmScenariosResponse.

        :return: The version of this CreateSimSmScenariosResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateSimSmScenariosResponse.

        :param version: The version of this CreateSimSmScenariosResponse.
        :type version: :class:`huaweicloudsdkoctopus.v2.ScenarioVersionEnum`
        """
        self._version = version

    @property
    def map_filename(self):
        r"""Gets the map_filename of this CreateSimSmScenariosResponse.

        地图文件名

        :return: The map_filename of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._map_filename

    @map_filename.setter
    def map_filename(self, map_filename):
        r"""Sets the map_filename of this CreateSimSmScenariosResponse.

        地图文件名

        :param map_filename: The map_filename of this CreateSimSmScenariosResponse.
        :type map_filename: str
        """
        self._map_filename = map_filename

    @property
    def model_filename(self):
        r"""Gets the model_filename of this CreateSimSmScenariosResponse.

        模型文件名

        :return: The model_filename of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._model_filename

    @model_filename.setter
    def model_filename(self, model_filename):
        r"""Sets the model_filename of this CreateSimSmScenariosResponse.

        模型文件名

        :param model_filename: The model_filename of this CreateSimSmScenariosResponse.
        :type model_filename: str
        """
        self._model_filename = model_filename

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateSimSmScenariosResponse.

        用户id

        :return: The user_id of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateSimSmScenariosResponse.

        用户id

        :param user_id: The user_id of this CreateSimSmScenariosResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateSimSmScenariosResponse.

        用户名

        :return: The user_name of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateSimSmScenariosResponse.

        用户名

        :param user_name: The user_name of this CreateSimSmScenariosResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def name(self):
        r"""Gets the name of this CreateSimSmScenariosResponse.

        名称

        :return: The name of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSimSmScenariosResponse.

        名称

        :param name: The name of this CreateSimSmScenariosResponse.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        r"""Gets the priority of this CreateSimSmScenariosResponse.

        :return: The priority of this CreateSimSmScenariosResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateSimSmScenariosResponse.

        :param priority: The priority of this CreateSimSmScenariosResponse.
        :type priority: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        self._priority = priority

    @property
    def map(self):
        r"""Gets the map of this CreateSimSmScenariosResponse.

        地图

        :return: The map of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        r"""Sets the map of this CreateSimSmScenariosResponse.

        地图

        :param map: The map of this CreateSimSmScenariosResponse.
        :type map: str
        """
        self._map = map

    @property
    def model(self):
        r"""Gets the model of this CreateSimSmScenariosResponse.

        模型

        :return: The model of this CreateSimSmScenariosResponse.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this CreateSimSmScenariosResponse.

        模型

        :param model: The model of this CreateSimSmScenariosResponse.
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
        if not isinstance(other, CreateSimSmScenariosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
