# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleInstsanceV3:

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
        'created_at': 'str',
        'deleted_at': 'str',
        'volume_type': 'str',
        'volume_size': 'int',
        'data_vip': 'str',
        'data_vip_v6': 'str',
        'enterprise_project_id': 'str',
        'retained_until': 'str',
        'recycle_backup_id': 'str',
        'recycle_status': 'str',
        'is_serverless': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ha_mode': 'ha_mode',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'pay_model': 'pay_model',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'volume_type': 'volume_type',
        'volume_size': 'volume_size',
        'data_vip': 'data_vip',
        'data_vip_v6': 'data_vip_v6',
        'enterprise_project_id': 'enterprise_project_id',
        'retained_until': 'retained_until',
        'recycle_backup_id': 'recycle_backup_id',
        'recycle_status': 'recycle_status',
        'is_serverless': 'is_serverless'
    }

    def __init__(self, id=None, name=None, ha_mode=None, engine_name=None, engine_version=None, pay_model=None, created_at=None, deleted_at=None, volume_type=None, volume_size=None, data_vip=None, data_vip_v6=None, enterprise_project_id=None, retained_until=None, recycle_backup_id=None, recycle_status=None, is_serverless=None):
        r"""RecycleInstsanceV3

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param name: 实例名
        :type name: str
        :param ha_mode: 实例主备模式，取值：Ha（主备），不区分大小写。
        :type ha_mode: str
        :param engine_name: 引擎名
        :type engine_name: str
        :param engine_version: 数据库引擎版本
        :type engine_version: str
        :param pay_model: 计费方式
        :type pay_model: str
        :param created_at: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type created_at: str
        :param deleted_at: 删除时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type deleted_at: str
        :param volume_type: 磁盘类型。 取值范围如下，区分大小写： - COMMON，表示SATA。 - HIGH，表示SAS。 - ULTRAHIGH，表示SSD。 - ULTRAHIGHPRO，表示SSD尊享版，仅支持超高性能型尊享版（需申请权限）。 - CLOUDSSD，表示SSD云盘，仅支持通用型和独享型规格实例。 - LOCALSSD，表示本地SSD。
        :type volume_type: str
        :param volume_size: 磁盘大小，单位为GB。 取值范围：40GB~4000GB，必须为10的整数倍。  部分用户支持40GB~6000GB，如果您想创建存储空间最大为6000GB的数据库实例，或提高扩容上限到10000GB，请联系客服开通。  说明：对于只读实例，该参数无效，磁盘大小，默认和主实例相同。
        :type volume_size: int
        :param data_vip: 内网地址
        :type data_vip: str
        :param data_vip_v6: ipv6内网地址
        :type data_vip_v6: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param retained_until: 保留时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type retained_until: str
        :param recycle_backup_id: 备份id
        :type recycle_backup_id: str
        :param recycle_status: 备份状态 取值范围如下，区分大小写: - BUILDING 备份中，不能进行重建 - COMPLETED，标识备份完成，可以重建
        :type recycle_status: str
        :param is_serverless: 是否为serverless实例 - false 不是serverless实例 - true 是serverless实例
        :type is_serverless: bool
        """
        
        

        self._id = None
        self._name = None
        self._ha_mode = None
        self._engine_name = None
        self._engine_version = None
        self._pay_model = None
        self._created_at = None
        self._deleted_at = None
        self._volume_type = None
        self._volume_size = None
        self._data_vip = None
        self._data_vip_v6 = None
        self._enterprise_project_id = None
        self._retained_until = None
        self._recycle_backup_id = None
        self._recycle_status = None
        self._is_serverless = None
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
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if volume_type is not None:
            self.volume_type = volume_type
        if volume_size is not None:
            self.volume_size = volume_size
        if data_vip is not None:
            self.data_vip = data_vip
        if data_vip_v6 is not None:
            self.data_vip_v6 = data_vip_v6
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if retained_until is not None:
            self.retained_until = retained_until
        if recycle_backup_id is not None:
            self.recycle_backup_id = recycle_backup_id
        if recycle_status is not None:
            self.recycle_status = recycle_status
        if is_serverless is not None:
            self.is_serverless = is_serverless

    @property
    def id(self):
        r"""Gets the id of this RecycleInstsanceV3.

        实例id

        :return: The id of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecycleInstsanceV3.

        实例id

        :param id: The id of this RecycleInstsanceV3.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RecycleInstsanceV3.

        实例名

        :return: The name of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecycleInstsanceV3.

        实例名

        :param name: The name of this RecycleInstsanceV3.
        :type name: str
        """
        self._name = name

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this RecycleInstsanceV3.

        实例主备模式，取值：Ha（主备），不区分大小写。

        :return: The ha_mode of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this RecycleInstsanceV3.

        实例主备模式，取值：Ha（主备），不区分大小写。

        :param ha_mode: The ha_mode of this RecycleInstsanceV3.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def engine_name(self):
        r"""Gets the engine_name of this RecycleInstsanceV3.

        引擎名

        :return: The engine_name of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this RecycleInstsanceV3.

        引擎名

        :param engine_name: The engine_name of this RecycleInstsanceV3.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this RecycleInstsanceV3.

        数据库引擎版本

        :return: The engine_version of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this RecycleInstsanceV3.

        数据库引擎版本

        :param engine_version: The engine_version of this RecycleInstsanceV3.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def pay_model(self):
        r"""Gets the pay_model of this RecycleInstsanceV3.

        计费方式

        :return: The pay_model of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this RecycleInstsanceV3.

        计费方式

        :param pay_model: The pay_model of this RecycleInstsanceV3.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def created_at(self):
        r"""Gets the created_at of this RecycleInstsanceV3.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The created_at of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecycleInstsanceV3.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param created_at: The created_at of this RecycleInstsanceV3.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def deleted_at(self):
        r"""Gets the deleted_at of this RecycleInstsanceV3.

        删除时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The deleted_at of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        r"""Sets the deleted_at of this RecycleInstsanceV3.

        删除时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param deleted_at: The deleted_at of this RecycleInstsanceV3.
        :type deleted_at: str
        """
        self._deleted_at = deleted_at

    @property
    def volume_type(self):
        r"""Gets the volume_type of this RecycleInstsanceV3.

        磁盘类型。 取值范围如下，区分大小写： - COMMON，表示SATA。 - HIGH，表示SAS。 - ULTRAHIGH，表示SSD。 - ULTRAHIGHPRO，表示SSD尊享版，仅支持超高性能型尊享版（需申请权限）。 - CLOUDSSD，表示SSD云盘，仅支持通用型和独享型规格实例。 - LOCALSSD，表示本地SSD。

        :return: The volume_type of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this RecycleInstsanceV3.

        磁盘类型。 取值范围如下，区分大小写： - COMMON，表示SATA。 - HIGH，表示SAS。 - ULTRAHIGH，表示SSD。 - ULTRAHIGHPRO，表示SSD尊享版，仅支持超高性能型尊享版（需申请权限）。 - CLOUDSSD，表示SSD云盘，仅支持通用型和独享型规格实例。 - LOCALSSD，表示本地SSD。

        :param volume_type: The volume_type of this RecycleInstsanceV3.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_size(self):
        r"""Gets the volume_size of this RecycleInstsanceV3.

        磁盘大小，单位为GB。 取值范围：40GB~4000GB，必须为10的整数倍。  部分用户支持40GB~6000GB，如果您想创建存储空间最大为6000GB的数据库实例，或提高扩容上限到10000GB，请联系客服开通。  说明：对于只读实例，该参数无效，磁盘大小，默认和主实例相同。

        :return: The volume_size of this RecycleInstsanceV3.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this RecycleInstsanceV3.

        磁盘大小，单位为GB。 取值范围：40GB~4000GB，必须为10的整数倍。  部分用户支持40GB~6000GB，如果您想创建存储空间最大为6000GB的数据库实例，或提高扩容上限到10000GB，请联系客服开通。  说明：对于只读实例，该参数无效，磁盘大小，默认和主实例相同。

        :param volume_size: The volume_size of this RecycleInstsanceV3.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def data_vip(self):
        r"""Gets the data_vip of this RecycleInstsanceV3.

        内网地址

        :return: The data_vip of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        r"""Sets the data_vip of this RecycleInstsanceV3.

        内网地址

        :param data_vip: The data_vip of this RecycleInstsanceV3.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def data_vip_v6(self):
        r"""Gets the data_vip_v6 of this RecycleInstsanceV3.

        ipv6内网地址

        :return: The data_vip_v6 of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._data_vip_v6

    @data_vip_v6.setter
    def data_vip_v6(self, data_vip_v6):
        r"""Sets the data_vip_v6 of this RecycleInstsanceV3.

        ipv6内网地址

        :param data_vip_v6: The data_vip_v6 of this RecycleInstsanceV3.
        :type data_vip_v6: str
        """
        self._data_vip_v6 = data_vip_v6

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RecycleInstsanceV3.

        企业项目ID

        :return: The enterprise_project_id of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RecycleInstsanceV3.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this RecycleInstsanceV3.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def retained_until(self):
        r"""Gets the retained_until of this RecycleInstsanceV3.

        保留时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The retained_until of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._retained_until

    @retained_until.setter
    def retained_until(self, retained_until):
        r"""Sets the retained_until of this RecycleInstsanceV3.

        保留时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param retained_until: The retained_until of this RecycleInstsanceV3.
        :type retained_until: str
        """
        self._retained_until = retained_until

    @property
    def recycle_backup_id(self):
        r"""Gets the recycle_backup_id of this RecycleInstsanceV3.

        备份id

        :return: The recycle_backup_id of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._recycle_backup_id

    @recycle_backup_id.setter
    def recycle_backup_id(self, recycle_backup_id):
        r"""Sets the recycle_backup_id of this RecycleInstsanceV3.

        备份id

        :param recycle_backup_id: The recycle_backup_id of this RecycleInstsanceV3.
        :type recycle_backup_id: str
        """
        self._recycle_backup_id = recycle_backup_id

    @property
    def recycle_status(self):
        r"""Gets the recycle_status of this RecycleInstsanceV3.

        备份状态 取值范围如下，区分大小写: - BUILDING 备份中，不能进行重建 - COMPLETED，标识备份完成，可以重建

        :return: The recycle_status of this RecycleInstsanceV3.
        :rtype: str
        """
        return self._recycle_status

    @recycle_status.setter
    def recycle_status(self, recycle_status):
        r"""Sets the recycle_status of this RecycleInstsanceV3.

        备份状态 取值范围如下，区分大小写: - BUILDING 备份中，不能进行重建 - COMPLETED，标识备份完成，可以重建

        :param recycle_status: The recycle_status of this RecycleInstsanceV3.
        :type recycle_status: str
        """
        self._recycle_status = recycle_status

    @property
    def is_serverless(self):
        r"""Gets the is_serverless of this RecycleInstsanceV3.

        是否为serverless实例 - false 不是serverless实例 - true 是serverless实例

        :return: The is_serverless of this RecycleInstsanceV3.
        :rtype: bool
        """
        return self._is_serverless

    @is_serverless.setter
    def is_serverless(self, is_serverless):
        r"""Sets the is_serverless of this RecycleInstsanceV3.

        是否为serverless实例 - false 不是serverless实例 - true 是serverless实例

        :param is_serverless: The is_serverless of this RecycleInstsanceV3.
        :type is_serverless: bool
        """
        self._is_serverless = is_serverless

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
        if not isinstance(other, RecycleInstsanceV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
