# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupsRequest:

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
        'backup_id': 'str',
        'backup_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'begin_time': 'str',
        'end_time': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'backup_id': 'backup_id',
        'backup_type': 'backup_type',
        'offset': 'offset',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'mode': 'mode'
    }

    def __init__(self, instance_id=None, backup_id=None, backup_type=None, offset=None, limit=None, begin_time=None, end_time=None, mode=None):
        r"""ListBackupsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param backup_id: 备份ID。 - 当该字段传入的备份ID归属为自动增量备份时，实例ID必传。
        :type backup_id: str
        :param backup_type: 备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。 - 当该字段未传入值时，默认只查询所有的全量备份，包括自动全备备份和手动全量备份。当该字段取值为“Incremental”时，实例ID必传。
        :type backup_type: str
        :param offset: 索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。
        :type offset: int
        :param limit: 查询备份个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。
        :type limit: int
        :param begin_time: 查询开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 “end_time”有值时，“begin_time”必选。
        :type begin_time: str
        :param end_time: 查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 “begin_time”有值时，“end_time”必选。
        :type end_time: str
        :param mode: 实例模式。 取值： - Sharding - ReplicaSet - Single
        :type mode: str
        """
        
        

        self._instance_id = None
        self._backup_id = None
        self._backup_type = None
        self._offset = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self._mode = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_type is not None:
            self.backup_type = backup_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if mode is not None:
            self.mode = mode

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListBackupsRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListBackupsRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ListBackupsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ListBackupsRequest.

        备份ID。 - 当该字段传入的备份ID归属为自动增量备份时，实例ID必传。

        :return: The backup_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ListBackupsRequest.

        备份ID。 - 当该字段传入的备份ID归属为自动增量备份时，实例ID必传。

        :param backup_id: The backup_id of this ListBackupsRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_type(self):
        r"""Gets the backup_type of this ListBackupsRequest.

        备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。 - 当该字段未传入值时，默认只查询所有的全量备份，包括自动全备备份和手动全量备份。当该字段取值为“Incremental”时，实例ID必传。

        :return: The backup_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this ListBackupsRequest.

        备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。 - 当该字段未传入值时，默认只查询所有的全量备份，包括自动全备备份和手动全量备份。当该字段取值为“Incremental”时，实例ID必传。

        :param backup_type: The backup_type of this ListBackupsRequest.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def offset(self):
        r"""Gets the offset of this ListBackupsRequest.

        索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。

        :return: The offset of this ListBackupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBackupsRequest.

        索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。

        :param offset: The offset of this ListBackupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBackupsRequest.

        查询备份个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :return: The limit of this ListBackupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackupsRequest.

        查询备份个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :param limit: The limit of this ListBackupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListBackupsRequest.

        查询开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 “end_time”有值时，“begin_time”必选。

        :return: The begin_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListBackupsRequest.

        查询开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 “end_time”有值时，“begin_time”必选。

        :param begin_time: The begin_time of this ListBackupsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBackupsRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 “begin_time”有值时，“end_time”必选。

        :return: The end_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBackupsRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 “begin_time”有值时，“end_time”必选。

        :param end_time: The end_time of this ListBackupsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def mode(self):
        r"""Gets the mode of this ListBackupsRequest.

        实例模式。 取值： - Sharding - ReplicaSet - Single

        :return: The mode of this ListBackupsRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListBackupsRequest.

        实例模式。 取值： - Sharding - ReplicaSet - Single

        :param mode: The mode of this ListBackupsRequest.
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
        if not isinstance(other, ListBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
