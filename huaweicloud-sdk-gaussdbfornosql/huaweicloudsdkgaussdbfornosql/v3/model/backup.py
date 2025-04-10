# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Backup:

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
        'description': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'datastore': 'Datastore',
        'name': 'str',
        'type': 'str',
        'size': 'float',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'database_tables': 'list[QueryDatabaseTableInfo]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'datastore': 'datastore',
        'name': 'name',
        'type': 'type',
        'size': 'size',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'database_tables': 'database_tables'
    }

    def __init__(self, id=None, description=None, instance_id=None, instance_name=None, datastore=None, name=None, type=None, size=None, status=None, begin_time=None, end_time=None, database_tables=None):
        r"""Backup

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param description: 备份描述信息。
        :type description: str
        :param instance_id: 备份所属的实例ID。
        :type instance_id: str
        :param instance_name: 备份所属的实例名称。
        :type instance_name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.Datastore`
        :param name: 备份名称。
        :type name: str
        :param type: - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。
        :type type: str
        :param size: 备份大小，单位：KB。
        :type size: float
        :param status: 备份状态。取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。
        :type status: str
        :param begin_time: 备份开始时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。
        :type begin_time: str
        :param end_time: 备份结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。
        :type end_time: str
        :param database_tables: 备份里的库表信息 - 实例级查询时该字段为空，可忽略 - 库表级查询时该字段非空（存在库表级备份的话）
        :type database_tables: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDatabaseTableInfo`]
        """
        
        

        self._id = None
        self._description = None
        self._instance_id = None
        self._instance_name = None
        self._datastore = None
        self._name = None
        self._type = None
        self._size = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._database_tables = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.datastore = datastore
        self.name = name
        self.type = type
        self.size = size
        self.status = status
        self.begin_time = begin_time
        self.end_time = end_time
        if database_tables is not None:
            self.database_tables = database_tables

    @property
    def id(self):
        r"""Gets the id of this Backup.

        备份ID。

        :return: The id of this Backup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Backup.

        备份ID。

        :param id: The id of this Backup.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this Backup.

        备份描述信息。

        :return: The description of this Backup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Backup.

        备份描述信息。

        :param description: The description of this Backup.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Backup.

        备份所属的实例ID。

        :return: The instance_id of this Backup.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Backup.

        备份所属的实例ID。

        :param instance_id: The instance_id of this Backup.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this Backup.

        备份所属的实例名称。

        :return: The instance_name of this Backup.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this Backup.

        备份所属的实例名称。

        :param instance_name: The instance_name of this Backup.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def datastore(self):
        r"""Gets the datastore of this Backup.

        :return: The datastore of this Backup.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this Backup.

        :param datastore: The datastore of this Backup.
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.Datastore`
        """
        self._datastore = datastore

    @property
    def name(self):
        r"""Gets the name of this Backup.

        备份名称。

        :return: The name of this Backup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Backup.

        备份名称。

        :param name: The name of this Backup.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this Backup.

        - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。

        :return: The type of this Backup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Backup.

        - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。

        :param type: The type of this Backup.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this Backup.

        备份大小，单位：KB。

        :return: The size of this Backup.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Backup.

        备份大小，单位：KB。

        :param size: The size of this Backup.
        :type size: float
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this Backup.

        备份状态。取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。

        :return: The status of this Backup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Backup.

        备份状态。取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。

        :param status: The status of this Backup.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this Backup.

        备份开始时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :return: The begin_time of this Backup.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this Backup.

        备份开始时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :param begin_time: The begin_time of this Backup.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this Backup.

        备份结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :return: The end_time of this Backup.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Backup.

        备份结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :param end_time: The end_time of this Backup.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def database_tables(self):
        r"""Gets the database_tables of this Backup.

        备份里的库表信息 - 实例级查询时该字段为空，可忽略 - 库表级查询时该字段非空（存在库表级备份的话）

        :return: The database_tables of this Backup.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDatabaseTableInfo`]
        """
        return self._database_tables

    @database_tables.setter
    def database_tables(self, database_tables):
        r"""Sets the database_tables of this Backup.

        备份里的库表信息 - 实例级查询时该字段为空，可忽略 - 库表级查询时该字段非空（存在库表级备份的话）

        :param database_tables: The database_tables of this Backup.
        :type database_tables: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDatabaseTableInfo`]
        """
        self._database_tables = database_tables

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
        if not isinstance(other, Backup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
