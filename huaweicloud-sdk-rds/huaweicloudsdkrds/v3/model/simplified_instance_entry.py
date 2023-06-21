# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimplifiedInstanceEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'instance_status': 'str',
        'frozen': 'bool',
        'type': 'str',
        'pay_model': 'str',
        'spec_code': 'str',
        'availability_zone_ids': 'list[str]',
        'read_only_instances': 'list[str]',
        'current_actions': 'list[str]',
        'volume_type': 'str',
        'volume_size': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'instance_status': 'instance_status',
        'frozen': 'frozen',
        'type': 'type',
        'pay_model': 'pay_model',
        'spec_code': 'spec_code',
        'availability_zone_ids': 'availability_zone_ids',
        'read_only_instances': 'read_only_instances',
        'current_actions': 'current_actions',
        'volume_type': 'volume_type',
        'volume_size': 'volume_size',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, engine_name=None, engine_version=None, instance_status=None, frozen=None, type=None, pay_model=None, spec_code=None, availability_zone_ids=None, read_only_instances=None, current_actions=None, volume_type=None, volume_size=None, enterprise_project_id=None):
        """SimplifiedInstanceEntry

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param name: 创建的实例名称
        :type name: str
        :param engine_name: 引擎名字
        :type engine_name: str
        :param engine_version: 引擎版本
        :type engine_version: str
        :param instance_status: 实例状态。 normal,表示正常 abnormal,表示异常 creating,表示创建中 createfail,表示创建失败 data_disk_full,表示磁盘满 deleted,表示删除 shutdown,表示关机
        :type instance_status: str
        :param frozen: 是否冻结
        :type frozen: bool
        :param type: 按照实例类型查询。取值Single、Ha、Replica、Enterprise，分别对应于单实例、主备实例和只读实例、分布式实例（企业版）。
        :type type: str
        :param pay_model: 按需还是包周期
        :type pay_model: str
        :param spec_code: 规格码
        :type spec_code: str
        :param availability_zone_ids: 可用区集合
        :type availability_zone_ids: list[str]
        :param read_only_instances: 只读实例id集合
        :type read_only_instances: list[str]
        :param current_actions: 当前实例操作动作集合
        :type current_actions: list[str]
        :param volume_type: 磁盘类型。
        :type volume_type: str
        :param volume_size: 磁盘大小(单位:G)。
        :type volume_size: int
        :param enterprise_project_id: 企业项目标签ID。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._engine_name = None
        self._engine_version = None
        self._instance_status = None
        self._frozen = None
        self._type = None
        self._pay_model = None
        self._spec_code = None
        self._availability_zone_ids = None
        self._read_only_instances = None
        self._current_actions = None
        self._volume_type = None
        self._volume_size = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.engine_name = engine_name
        self.engine_version = engine_version
        self.instance_status = instance_status
        self.frozen = frozen
        self.type = type
        self.pay_model = pay_model
        self.spec_code = spec_code
        self.availability_zone_ids = availability_zone_ids
        self.read_only_instances = read_only_instances
        self.current_actions = current_actions
        self.volume_type = volume_type
        self.volume_size = volume_size
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this SimplifiedInstanceEntry.

        实例id

        :return: The id of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimplifiedInstanceEntry.

        实例id

        :param id: The id of this SimplifiedInstanceEntry.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SimplifiedInstanceEntry.

        创建的实例名称

        :return: The name of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimplifiedInstanceEntry.

        创建的实例名称

        :param name: The name of this SimplifiedInstanceEntry.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        """Gets the engine_name of this SimplifiedInstanceEntry.

        引擎名字

        :return: The engine_name of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this SimplifiedInstanceEntry.

        引擎名字

        :param engine_name: The engine_name of this SimplifiedInstanceEntry.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        """Gets the engine_version of this SimplifiedInstanceEntry.

        引擎版本

        :return: The engine_version of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this SimplifiedInstanceEntry.

        引擎版本

        :param engine_version: The engine_version of this SimplifiedInstanceEntry.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def instance_status(self):
        """Gets the instance_status of this SimplifiedInstanceEntry.

        实例状态。 normal,表示正常 abnormal,表示异常 creating,表示创建中 createfail,表示创建失败 data_disk_full,表示磁盘满 deleted,表示删除 shutdown,表示关机

        :return: The instance_status of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this SimplifiedInstanceEntry.

        实例状态。 normal,表示正常 abnormal,表示异常 creating,表示创建中 createfail,表示创建失败 data_disk_full,表示磁盘满 deleted,表示删除 shutdown,表示关机

        :param instance_status: The instance_status of this SimplifiedInstanceEntry.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def frozen(self):
        """Gets the frozen of this SimplifiedInstanceEntry.

        是否冻结

        :return: The frozen of this SimplifiedInstanceEntry.
        :rtype: bool
        """
        return self._frozen

    @frozen.setter
    def frozen(self, frozen):
        """Sets the frozen of this SimplifiedInstanceEntry.

        是否冻结

        :param frozen: The frozen of this SimplifiedInstanceEntry.
        :type frozen: bool
        """
        self._frozen = frozen

    @property
    def type(self):
        """Gets the type of this SimplifiedInstanceEntry.

        按照实例类型查询。取值Single、Ha、Replica、Enterprise，分别对应于单实例、主备实例和只读实例、分布式实例（企业版）。

        :return: The type of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimplifiedInstanceEntry.

        按照实例类型查询。取值Single、Ha、Replica、Enterprise，分别对应于单实例、主备实例和只读实例、分布式实例（企业版）。

        :param type: The type of this SimplifiedInstanceEntry.
        :type type: str
        """
        self._type = type

    @property
    def pay_model(self):
        """Gets the pay_model of this SimplifiedInstanceEntry.

        按需还是包周期

        :return: The pay_model of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        """Sets the pay_model of this SimplifiedInstanceEntry.

        按需还是包周期

        :param pay_model: The pay_model of this SimplifiedInstanceEntry.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def spec_code(self):
        """Gets the spec_code of this SimplifiedInstanceEntry.

        规格码

        :return: The spec_code of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this SimplifiedInstanceEntry.

        规格码

        :param spec_code: The spec_code of this SimplifiedInstanceEntry.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this SimplifiedInstanceEntry.

        可用区集合

        :return: The availability_zone_ids of this SimplifiedInstanceEntry.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this SimplifiedInstanceEntry.

        可用区集合

        :param availability_zone_ids: The availability_zone_ids of this SimplifiedInstanceEntry.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def read_only_instances(self):
        """Gets the read_only_instances of this SimplifiedInstanceEntry.

        只读实例id集合

        :return: The read_only_instances of this SimplifiedInstanceEntry.
        :rtype: list[str]
        """
        return self._read_only_instances

    @read_only_instances.setter
    def read_only_instances(self, read_only_instances):
        """Sets the read_only_instances of this SimplifiedInstanceEntry.

        只读实例id集合

        :param read_only_instances: The read_only_instances of this SimplifiedInstanceEntry.
        :type read_only_instances: list[str]
        """
        self._read_only_instances = read_only_instances

    @property
    def current_actions(self):
        """Gets the current_actions of this SimplifiedInstanceEntry.

        当前实例操作动作集合

        :return: The current_actions of this SimplifiedInstanceEntry.
        :rtype: list[str]
        """
        return self._current_actions

    @current_actions.setter
    def current_actions(self, current_actions):
        """Sets the current_actions of this SimplifiedInstanceEntry.

        当前实例操作动作集合

        :param current_actions: The current_actions of this SimplifiedInstanceEntry.
        :type current_actions: list[str]
        """
        self._current_actions = current_actions

    @property
    def volume_type(self):
        """Gets the volume_type of this SimplifiedInstanceEntry.

        磁盘类型。

        :return: The volume_type of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this SimplifiedInstanceEntry.

        磁盘类型。

        :param volume_type: The volume_type of this SimplifiedInstanceEntry.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_size(self):
        """Gets the volume_size of this SimplifiedInstanceEntry.

        磁盘大小(单位:G)。

        :return: The volume_size of this SimplifiedInstanceEntry.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this SimplifiedInstanceEntry.

        磁盘大小(单位:G)。

        :param volume_size: The volume_size of this SimplifiedInstanceEntry.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SimplifiedInstanceEntry.

        企业项目标签ID。

        :return: The enterprise_project_id of this SimplifiedInstanceEntry.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SimplifiedInstanceEntry.

        企业项目标签ID。

        :param enterprise_project_id: The enterprise_project_id of this SimplifiedInstanceEntry.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, SimplifiedInstanceEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
