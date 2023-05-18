# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllInstancesBackupsNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'datastore_type': 'str',
        'backup_id': 'str',
        'backup_type': 'str',
        'type': 'str',
        'limit': 'int',
        'offset': 'int',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'datastore_type': 'datastore_type',
        'backup_id': 'backup_id',
        'backup_type': 'backup_type',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, datastore_type=None, backup_id=None, backup_type=None, type=None, limit=None, offset=None, begin_time=None, end_time=None):
        """ShowAllInstancesBackupsNewRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param datastore_type: 数据库类型。 - cassandra - redis - mongodb - influxdb
        :type datastore_type: str
        :param backup_id: 备份ID。
        :type backup_id: str
        :param backup_type: 备份类型，大小写敏感。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 当该字段未传入值时，默认只查询所有的全量备份(包含库表级)，包括自动全备备份和手动全量备份。
        :type backup_type: str
        :param type: 备份策略类型。可取值: - Instance 表示查询实例级备份 - DatabaseTable 表示查询库表级备份 - 默认取值 Instance
        :type type: str
        :param limit: 查询备份个数上限值。取值范围：1~100。不传该参数时，默认查询前100条实例信息。
        :type limit: int
        :param offset: 索引位置偏移量，表示从指定project ID下最新的备份创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的备份信息。取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的备份创建时间对应的备份开始查询。
        :type offset: int
        :param begin_time: 查询备份开始的时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量，默认为空。 - “end_time”有值时，“begin_time”必选。
        :type begin_time: str
        :param end_time: 查询备份开始的结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量，默认为空。 - “begin_time”有值时，“end_time”必选。
        :type end_time: str
        """
        
        

        self._instance_id = None
        self._datastore_type = None
        self._backup_id = None
        self._backup_type = None
        self._type = None
        self._limit = None
        self._offset = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_type is not None:
            self.backup_type = backup_type
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowAllInstancesBackupsNewRequest.

        实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ShowAllInstancesBackupsNewRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowAllInstancesBackupsNewRequest.

        实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ShowAllInstancesBackupsNewRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ShowAllInstancesBackupsNewRequest.

        数据库类型。 - cassandra - redis - mongodb - influxdb

        :return: The datastore_type of this ShowAllInstancesBackupsNewRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ShowAllInstancesBackupsNewRequest.

        数据库类型。 - cassandra - redis - mongodb - influxdb

        :param datastore_type: The datastore_type of this ShowAllInstancesBackupsNewRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def backup_id(self):
        """Gets the backup_id of this ShowAllInstancesBackupsNewRequest.

        备份ID。

        :return: The backup_id of this ShowAllInstancesBackupsNewRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this ShowAllInstancesBackupsNewRequest.

        备份ID。

        :param backup_id: The backup_id of this ShowAllInstancesBackupsNewRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_type(self):
        """Gets the backup_type of this ShowAllInstancesBackupsNewRequest.

        备份类型，大小写敏感。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 当该字段未传入值时，默认只查询所有的全量备份(包含库表级)，包括自动全备备份和手动全量备份。

        :return: The backup_type of this ShowAllInstancesBackupsNewRequest.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this ShowAllInstancesBackupsNewRequest.

        备份类型，大小写敏感。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 当该字段未传入值时，默认只查询所有的全量备份(包含库表级)，包括自动全备备份和手动全量备份。

        :param backup_type: The backup_type of this ShowAllInstancesBackupsNewRequest.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def type(self):
        """Gets the type of this ShowAllInstancesBackupsNewRequest.

        备份策略类型。可取值: - Instance 表示查询实例级备份 - DatabaseTable 表示查询库表级备份 - 默认取值 Instance

        :return: The type of this ShowAllInstancesBackupsNewRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowAllInstancesBackupsNewRequest.

        备份策略类型。可取值: - Instance 表示查询实例级备份 - DatabaseTable 表示查询库表级备份 - 默认取值 Instance

        :param type: The type of this ShowAllInstancesBackupsNewRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ShowAllInstancesBackupsNewRequest.

        查询备份个数上限值。取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :return: The limit of this ShowAllInstancesBackupsNewRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowAllInstancesBackupsNewRequest.

        查询备份个数上限值。取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :param limit: The limit of this ShowAllInstancesBackupsNewRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowAllInstancesBackupsNewRequest.

        索引位置偏移量，表示从指定project ID下最新的备份创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的备份信息。取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的备份创建时间对应的备份开始查询。

        :return: The offset of this ShowAllInstancesBackupsNewRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowAllInstancesBackupsNewRequest.

        索引位置偏移量，表示从指定project ID下最新的备份创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的备份信息。取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的备份创建时间对应的备份开始查询。

        :param offset: The offset of this ShowAllInstancesBackupsNewRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowAllInstancesBackupsNewRequest.

        查询备份开始的时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量，默认为空。 - “end_time”有值时，“begin_time”必选。

        :return: The begin_time of this ShowAllInstancesBackupsNewRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowAllInstancesBackupsNewRequest.

        查询备份开始的时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量，默认为空。 - “end_time”有值时，“begin_time”必选。

        :param begin_time: The begin_time of this ShowAllInstancesBackupsNewRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowAllInstancesBackupsNewRequest.

        查询备份开始的结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量，默认为空。 - “begin_time”有值时，“end_time”必选。

        :return: The end_time of this ShowAllInstancesBackupsNewRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowAllInstancesBackupsNewRequest.

        查询备份开始的结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量，默认为空。 - “begin_time”有值时，“end_time”必选。

        :param end_time: The end_time of this ShowAllInstancesBackupsNewRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowAllInstancesBackupsNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
