# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleInstanceV3:

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
        'ha_mode': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'pay_model': 'str',
        'create_at': 'int',
        'deleted_at': 'int',
        'volume_type': 'str',
        'volume_size': 'str',
        'data_vip': 'str',
        'data_vip_ipv6': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'backup_level': 'str',
        'recycle_backup_id': 'str',
        'recycle_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ha_mode': 'ha_mode',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'pay_model': 'pay_model',
        'create_at': 'create_at',
        'deleted_at': 'deleted_at',
        'volume_type': 'volume_type',
        'volume_size': 'volume_size',
        'data_vip': 'data_vip',
        'data_vip_ipv6': 'data_vip_ipv6',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'backup_level': 'backup_level',
        'recycle_backup_id': 'recycle_backup_id',
        'recycle_status': 'recycle_status'
    }

    def __init__(self, id=None, name=None, ha_mode=None, engine_name=None, engine_version=None, pay_model=None, create_at=None, deleted_at=None, volume_type=None, volume_size=None, data_vip=None, data_vip_ipv6=None, enterprise_project_id=None, enterprise_project_name=None, backup_level=None, recycle_backup_id=None, recycle_status=None):
        r"""RecycleInstanceV3

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param ha_mode: 实例类型。
        :type ha_mode: str
        :param engine_name: 引擎名称。
        :type engine_name: str
        :param engine_version: 引擎版本。
        :type engine_version: str
        :param pay_model: 计费模式。
        :type pay_model: str
        :param create_at: 创建时间。
        :type create_at: int
        :param deleted_at: 删除时间。
        :type deleted_at: int
        :param volume_type: 磁盘类型。
        :type volume_type: str
        :param volume_size: 磁盘大小。
        :type volume_size: str
        :param data_vip: 数据面VIP。
        :type data_vip: str
        :param data_vip_ipv6: 数据面IPV6。
        :type data_vip_ipv6: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param backup_level: 备份级别。
        :type backup_level: str
        :param recycle_backup_id: 备份ID。
        :type recycle_backup_id: str
        :param recycle_status: 回收状态。
        :type recycle_status: str
        """
        
        

        self._id = None
        self._name = None
        self._ha_mode = None
        self._engine_name = None
        self._engine_version = None
        self._pay_model = None
        self._create_at = None
        self._deleted_at = None
        self._volume_type = None
        self._volume_size = None
        self._data_vip = None
        self._data_vip_ipv6 = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._backup_level = None
        self._recycle_backup_id = None
        self._recycle_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ha_mode is not None:
            self.ha_mode = ha_mode
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if pay_model is not None:
            self.pay_model = pay_model
        if create_at is not None:
            self.create_at = create_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if volume_type is not None:
            self.volume_type = volume_type
        if volume_size is not None:
            self.volume_size = volume_size
        if data_vip is not None:
            self.data_vip = data_vip
        if data_vip_ipv6 is not None:
            self.data_vip_ipv6 = data_vip_ipv6
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if backup_level is not None:
            self.backup_level = backup_level
        if recycle_backup_id is not None:
            self.recycle_backup_id = recycle_backup_id
        if recycle_status is not None:
            self.recycle_status = recycle_status

    @property
    def id(self):
        r"""Gets the id of this RecycleInstanceV3.

        实例ID。

        :return: The id of this RecycleInstanceV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecycleInstanceV3.

        实例ID。

        :param id: The id of this RecycleInstanceV3.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RecycleInstanceV3.

        实例名称。

        :return: The name of this RecycleInstanceV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecycleInstanceV3.

        实例名称。

        :param name: The name of this RecycleInstanceV3.
        :type name: str
        """
        self._name = name

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this RecycleInstanceV3.

        实例类型。

        :return: The ha_mode of this RecycleInstanceV3.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this RecycleInstanceV3.

        实例类型。

        :param ha_mode: The ha_mode of this RecycleInstanceV3.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def engine_name(self):
        r"""Gets the engine_name of this RecycleInstanceV3.

        引擎名称。

        :return: The engine_name of this RecycleInstanceV3.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this RecycleInstanceV3.

        引擎名称。

        :param engine_name: The engine_name of this RecycleInstanceV3.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this RecycleInstanceV3.

        引擎版本。

        :return: The engine_version of this RecycleInstanceV3.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this RecycleInstanceV3.

        引擎版本。

        :param engine_version: The engine_version of this RecycleInstanceV3.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def pay_model(self):
        r"""Gets the pay_model of this RecycleInstanceV3.

        计费模式。

        :return: The pay_model of this RecycleInstanceV3.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this RecycleInstanceV3.

        计费模式。

        :param pay_model: The pay_model of this RecycleInstanceV3.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def create_at(self):
        r"""Gets the create_at of this RecycleInstanceV3.

        创建时间。

        :return: The create_at of this RecycleInstanceV3.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this RecycleInstanceV3.

        创建时间。

        :param create_at: The create_at of this RecycleInstanceV3.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def deleted_at(self):
        r"""Gets the deleted_at of this RecycleInstanceV3.

        删除时间。

        :return: The deleted_at of this RecycleInstanceV3.
        :rtype: int
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        r"""Sets the deleted_at of this RecycleInstanceV3.

        删除时间。

        :param deleted_at: The deleted_at of this RecycleInstanceV3.
        :type deleted_at: int
        """
        self._deleted_at = deleted_at

    @property
    def volume_type(self):
        r"""Gets the volume_type of this RecycleInstanceV3.

        磁盘类型。

        :return: The volume_type of this RecycleInstanceV3.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this RecycleInstanceV3.

        磁盘类型。

        :param volume_type: The volume_type of this RecycleInstanceV3.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_size(self):
        r"""Gets the volume_size of this RecycleInstanceV3.

        磁盘大小。

        :return: The volume_size of this RecycleInstanceV3.
        :rtype: str
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this RecycleInstanceV3.

        磁盘大小。

        :param volume_size: The volume_size of this RecycleInstanceV3.
        :type volume_size: str
        """
        self._volume_size = volume_size

    @property
    def data_vip(self):
        r"""Gets the data_vip of this RecycleInstanceV3.

        数据面VIP。

        :return: The data_vip of this RecycleInstanceV3.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        r"""Sets the data_vip of this RecycleInstanceV3.

        数据面VIP。

        :param data_vip: The data_vip of this RecycleInstanceV3.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def data_vip_ipv6(self):
        r"""Gets the data_vip_ipv6 of this RecycleInstanceV3.

        数据面IPV6。

        :return: The data_vip_ipv6 of this RecycleInstanceV3.
        :rtype: str
        """
        return self._data_vip_ipv6

    @data_vip_ipv6.setter
    def data_vip_ipv6(self, data_vip_ipv6):
        r"""Sets the data_vip_ipv6 of this RecycleInstanceV3.

        数据面IPV6。

        :param data_vip_ipv6: The data_vip_ipv6 of this RecycleInstanceV3.
        :type data_vip_ipv6: str
        """
        self._data_vip_ipv6 = data_vip_ipv6

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RecycleInstanceV3.

        企业项目ID。

        :return: The enterprise_project_id of this RecycleInstanceV3.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RecycleInstanceV3.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this RecycleInstanceV3.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this RecycleInstanceV3.

        企业项目名称。

        :return: The enterprise_project_name of this RecycleInstanceV3.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this RecycleInstanceV3.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this RecycleInstanceV3.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def backup_level(self):
        r"""Gets the backup_level of this RecycleInstanceV3.

        备份级别。

        :return: The backup_level of this RecycleInstanceV3.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        r"""Sets the backup_level of this RecycleInstanceV3.

        备份级别。

        :param backup_level: The backup_level of this RecycleInstanceV3.
        :type backup_level: str
        """
        self._backup_level = backup_level

    @property
    def recycle_backup_id(self):
        r"""Gets the recycle_backup_id of this RecycleInstanceV3.

        备份ID。

        :return: The recycle_backup_id of this RecycleInstanceV3.
        :rtype: str
        """
        return self._recycle_backup_id

    @recycle_backup_id.setter
    def recycle_backup_id(self, recycle_backup_id):
        r"""Sets the recycle_backup_id of this RecycleInstanceV3.

        备份ID。

        :param recycle_backup_id: The recycle_backup_id of this RecycleInstanceV3.
        :type recycle_backup_id: str
        """
        self._recycle_backup_id = recycle_backup_id

    @property
    def recycle_status(self):
        r"""Gets the recycle_status of this RecycleInstanceV3.

        回收状态。

        :return: The recycle_status of this RecycleInstanceV3.
        :rtype: str
        """
        return self._recycle_status

    @recycle_status.setter
    def recycle_status(self, recycle_status):
        r"""Sets the recycle_status of this RecycleInstanceV3.

        回收状态。

        :param recycle_status: The recycle_status of this RecycleInstanceV3.
        :type recycle_status: str
        """
        self._recycle_status = recycle_status

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
        if not isinstance(other, RecycleInstanceV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
