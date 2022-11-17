# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDatabaseResponseBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'created': 'str',
        'status': 'str',
        'updated': 'str',
        'databases': 'list[GetDatabases]',
        'shard_mode': 'str',
        'shard_number': 'int',
        'shard_unit': 'int',
        'data_vips': 'list[str]',
        'used_rds': 'list[GetDatabaseUsedRds]'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'status': 'status',
        'updated': 'updated',
        'databases': 'databases',
        'shard_mode': 'shard_mode',
        'shard_number': 'shard_number',
        'shard_unit': 'shard_unit',
        'data_vips': 'dataVips',
        'used_rds': 'used_rds'
    }

    def __init__(self, name=None, created=None, status=None, updated=None, databases=None, shard_mode=None, shard_number=None, shard_unit=None, data_vips=None, used_rds=None):
        """GetDatabaseResponseBean

        The model defined in huaweicloud sdk

        :param name: 逻辑库名称。
        :type name: str
        :param created: 逻辑库的创建时间。
        :type created: str
        :param status: 状态。
        :type status: str
        :param updated: DDM实例最后更新时间。
        :type updated: str
        :param databases: 逻辑库分片的详细信息。
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetDatabases`]
        :param shard_mode: 逻辑库的工作模式。  - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。
        :type shard_mode: str
        :param shard_number: 同一种工作模式下逻辑库分片的数量。
        :type shard_number: int
        :param shard_unit: 单个RDS上的逻辑库分片数。
        :type shard_unit: int
        :param data_vips: 连接逻辑库使用的IP:端口。
        :type data_vips: list[str]
        :param used_rds: 关联RDS
        :type used_rds: list[:class:`huaweicloudsdkddm.v1.GetDatabaseUsedRds`]
        """
        
        

        self._name = None
        self._created = None
        self._status = None
        self._updated = None
        self._databases = None
        self._shard_mode = None
        self._shard_number = None
        self._shard_unit = None
        self._data_vips = None
        self._used_rds = None
        self.discriminator = None

        self.name = name
        self.created = created
        self.status = status
        self.updated = updated
        self.databases = databases
        self.shard_mode = shard_mode
        self.shard_number = shard_number
        self.shard_unit = shard_unit
        self.data_vips = data_vips
        self.used_rds = used_rds

    @property
    def name(self):
        """Gets the name of this GetDatabaseResponseBean.

        逻辑库名称。

        :return: The name of this GetDatabaseResponseBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetDatabaseResponseBean.

        逻辑库名称。

        :param name: The name of this GetDatabaseResponseBean.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this GetDatabaseResponseBean.

        逻辑库的创建时间。

        :return: The created of this GetDatabaseResponseBean.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetDatabaseResponseBean.

        逻辑库的创建时间。

        :param created: The created of this GetDatabaseResponseBean.
        :type created: str
        """
        self._created = created

    @property
    def status(self):
        """Gets the status of this GetDatabaseResponseBean.

        状态。

        :return: The status of this GetDatabaseResponseBean.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetDatabaseResponseBean.

        状态。

        :param status: The status of this GetDatabaseResponseBean.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this GetDatabaseResponseBean.

        DDM实例最后更新时间。

        :return: The updated of this GetDatabaseResponseBean.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetDatabaseResponseBean.

        DDM实例最后更新时间。

        :param updated: The updated of this GetDatabaseResponseBean.
        :type updated: str
        """
        self._updated = updated

    @property
    def databases(self):
        """Gets the databases of this GetDatabaseResponseBean.

        逻辑库分片的详细信息。

        :return: The databases of this GetDatabaseResponseBean.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetDatabases`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this GetDatabaseResponseBean.

        逻辑库分片的详细信息。

        :param databases: The databases of this GetDatabaseResponseBean.
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetDatabases`]
        """
        self._databases = databases

    @property
    def shard_mode(self):
        """Gets the shard_mode of this GetDatabaseResponseBean.

        逻辑库的工作模式。  - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。

        :return: The shard_mode of this GetDatabaseResponseBean.
        :rtype: str
        """
        return self._shard_mode

    @shard_mode.setter
    def shard_mode(self, shard_mode):
        """Sets the shard_mode of this GetDatabaseResponseBean.

        逻辑库的工作模式。  - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。

        :param shard_mode: The shard_mode of this GetDatabaseResponseBean.
        :type shard_mode: str
        """
        self._shard_mode = shard_mode

    @property
    def shard_number(self):
        """Gets the shard_number of this GetDatabaseResponseBean.

        同一种工作模式下逻辑库分片的数量。

        :return: The shard_number of this GetDatabaseResponseBean.
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this GetDatabaseResponseBean.

        同一种工作模式下逻辑库分片的数量。

        :param shard_number: The shard_number of this GetDatabaseResponseBean.
        :type shard_number: int
        """
        self._shard_number = shard_number

    @property
    def shard_unit(self):
        """Gets the shard_unit of this GetDatabaseResponseBean.

        单个RDS上的逻辑库分片数。

        :return: The shard_unit of this GetDatabaseResponseBean.
        :rtype: int
        """
        return self._shard_unit

    @shard_unit.setter
    def shard_unit(self, shard_unit):
        """Sets the shard_unit of this GetDatabaseResponseBean.

        单个RDS上的逻辑库分片数。

        :param shard_unit: The shard_unit of this GetDatabaseResponseBean.
        :type shard_unit: int
        """
        self._shard_unit = shard_unit

    @property
    def data_vips(self):
        """Gets the data_vips of this GetDatabaseResponseBean.

        连接逻辑库使用的IP:端口。

        :return: The data_vips of this GetDatabaseResponseBean.
        :rtype: list[str]
        """
        return self._data_vips

    @data_vips.setter
    def data_vips(self, data_vips):
        """Sets the data_vips of this GetDatabaseResponseBean.

        连接逻辑库使用的IP:端口。

        :param data_vips: The data_vips of this GetDatabaseResponseBean.
        :type data_vips: list[str]
        """
        self._data_vips = data_vips

    @property
    def used_rds(self):
        """Gets the used_rds of this GetDatabaseResponseBean.

        关联RDS

        :return: The used_rds of this GetDatabaseResponseBean.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetDatabaseUsedRds`]
        """
        return self._used_rds

    @used_rds.setter
    def used_rds(self, used_rds):
        """Sets the used_rds of this GetDatabaseResponseBean.

        关联RDS

        :param used_rds: The used_rds of this GetDatabaseResponseBean.
        :type used_rds: list[:class:`huaweicloudsdkddm.v1.GetDatabaseUsedRds`]
        """
        self._used_rds = used_rds

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
        if not isinstance(other, GetDatabaseResponseBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
