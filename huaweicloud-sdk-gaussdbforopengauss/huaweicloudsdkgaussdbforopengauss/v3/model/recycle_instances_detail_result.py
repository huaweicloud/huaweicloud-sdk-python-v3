# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleInstancesDetailResult:

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
        'engine_version': 'str',
        'pay_model': 'str',
        'created_at': 'str',
        'deleted_at': 'str',
        'volume_type': 'str',
        'data_vip': 'str',
        'enterprise_project_id': 'str',
        'recycle_backup_id': 'str',
        'recycle_status': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ha_mode': 'ha_mode',
        'engine_version': 'engine_version',
        'pay_model': 'pay_model',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'volume_type': 'volume_type',
        'data_vip': 'data_vip',
        'enterprise_project_id': 'enterprise_project_id',
        'recycle_backup_id': 'recycle_backup_id',
        'recycle_status': 'recycle_status',
        'mode': 'mode'
    }

    def __init__(self, id=None, name=None, ha_mode=None, engine_version=None, pay_model=None, created_at=None, deleted_at=None, volume_type=None, data_vip=None, enterprise_project_id=None, recycle_backup_id=None, recycle_status=None, mode=None):
        """RecycleInstancesDetailResult

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param ha_mode: 部署形态。
        :type ha_mode: str
        :param engine_version: 引擎版本号。
        :type engine_version: str
        :param pay_model: 计费模式（0：按需计费；1：包年/包月）。
        :type pay_model: str
        :param created_at: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created_at: str
        :param deleted_at: 删除时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type deleted_at: str
        :param volume_type: 磁盘类型。（SAS：high；SSD：ultrahigh；ESSD：essd）。
        :type volume_type: str
        :param data_vip: 数据vip。
        :type data_vip: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param recycle_backup_id: 备份ID。（指删除实例时产生备份信息中的备份ID）。
        :type recycle_backup_id: str
        :param recycle_status: 回收站备份状态。（Running：运行中；Active：有效的）。
        :type recycle_status: str
        :param mode: 实例类型（basic：基础版；standard：标准版；enterprise：企业版）。
        :type mode: str
        """
        
        

        self._id = None
        self._name = None
        self._ha_mode = None
        self._engine_version = None
        self._pay_model = None
        self._created_at = None
        self._deleted_at = None
        self._volume_type = None
        self._data_vip = None
        self._enterprise_project_id = None
        self._recycle_backup_id = None
        self._recycle_status = None
        self._mode = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.ha_mode = ha_mode
        self.engine_version = engine_version
        self.pay_model = pay_model
        self.created_at = created_at
        self.deleted_at = deleted_at
        self.volume_type = volume_type
        self.data_vip = data_vip
        self.enterprise_project_id = enterprise_project_id
        self.recycle_backup_id = recycle_backup_id
        self.recycle_status = recycle_status
        self.mode = mode

    @property
    def id(self):
        """Gets the id of this RecycleInstancesDetailResult.

        实例ID。

        :return: The id of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecycleInstancesDetailResult.

        实例ID。

        :param id: The id of this RecycleInstancesDetailResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RecycleInstancesDetailResult.

        实例名称。

        :return: The name of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecycleInstancesDetailResult.

        实例名称。

        :param name: The name of this RecycleInstancesDetailResult.
        :type name: str
        """
        self._name = name

    @property
    def ha_mode(self):
        """Gets the ha_mode of this RecycleInstancesDetailResult.

        部署形态。

        :return: The ha_mode of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this RecycleInstancesDetailResult.

        部署形态。

        :param ha_mode: The ha_mode of this RecycleInstancesDetailResult.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def engine_version(self):
        """Gets the engine_version of this RecycleInstancesDetailResult.

        引擎版本号。

        :return: The engine_version of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this RecycleInstancesDetailResult.

        引擎版本号。

        :param engine_version: The engine_version of this RecycleInstancesDetailResult.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def pay_model(self):
        """Gets the pay_model of this RecycleInstancesDetailResult.

        计费模式（0：按需计费；1：包年/包月）。

        :return: The pay_model of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        """Sets the pay_model of this RecycleInstancesDetailResult.

        计费模式（0：按需计费；1：包年/包月）。

        :param pay_model: The pay_model of this RecycleInstancesDetailResult.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def created_at(self):
        """Gets the created_at of this RecycleInstancesDetailResult.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created_at of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RecycleInstancesDetailResult.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created_at: The created_at of this RecycleInstancesDetailResult.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this RecycleInstancesDetailResult.

        删除时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The deleted_at of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this RecycleInstancesDetailResult.

        删除时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param deleted_at: The deleted_at of this RecycleInstancesDetailResult.
        :type deleted_at: str
        """
        self._deleted_at = deleted_at

    @property
    def volume_type(self):
        """Gets the volume_type of this RecycleInstancesDetailResult.

        磁盘类型。（SAS：high；SSD：ultrahigh；ESSD：essd）。

        :return: The volume_type of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this RecycleInstancesDetailResult.

        磁盘类型。（SAS：high；SSD：ultrahigh；ESSD：essd）。

        :param volume_type: The volume_type of this RecycleInstancesDetailResult.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def data_vip(self):
        """Gets the data_vip of this RecycleInstancesDetailResult.

        数据vip。

        :return: The data_vip of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        """Sets the data_vip of this RecycleInstancesDetailResult.

        数据vip。

        :param data_vip: The data_vip of this RecycleInstancesDetailResult.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this RecycleInstancesDetailResult.

        企业项目ID。

        :return: The enterprise_project_id of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this RecycleInstancesDetailResult.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this RecycleInstancesDetailResult.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def recycle_backup_id(self):
        """Gets the recycle_backup_id of this RecycleInstancesDetailResult.

        备份ID。（指删除实例时产生备份信息中的备份ID）。

        :return: The recycle_backup_id of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._recycle_backup_id

    @recycle_backup_id.setter
    def recycle_backup_id(self, recycle_backup_id):
        """Sets the recycle_backup_id of this RecycleInstancesDetailResult.

        备份ID。（指删除实例时产生备份信息中的备份ID）。

        :param recycle_backup_id: The recycle_backup_id of this RecycleInstancesDetailResult.
        :type recycle_backup_id: str
        """
        self._recycle_backup_id = recycle_backup_id

    @property
    def recycle_status(self):
        """Gets the recycle_status of this RecycleInstancesDetailResult.

        回收站备份状态。（Running：运行中；Active：有效的）。

        :return: The recycle_status of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._recycle_status

    @recycle_status.setter
    def recycle_status(self, recycle_status):
        """Sets the recycle_status of this RecycleInstancesDetailResult.

        回收站备份状态。（Running：运行中；Active：有效的）。

        :param recycle_status: The recycle_status of this RecycleInstancesDetailResult.
        :type recycle_status: str
        """
        self._recycle_status = recycle_status

    @property
    def mode(self):
        """Gets the mode of this RecycleInstancesDetailResult.

        实例类型（basic：基础版；standard：标准版；enterprise：企业版）。

        :return: The mode of this RecycleInstancesDetailResult.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this RecycleInstancesDetailResult.

        实例类型（basic：基础版；standard：标准版；enterprise：企业版）。

        :param mode: The mode of this RecycleInstancesDetailResult.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, RecycleInstancesDetailResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
