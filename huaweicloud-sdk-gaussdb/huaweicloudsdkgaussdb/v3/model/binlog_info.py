# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BinlogInfo:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'size': 'int',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'size': 'size',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, name=None, instance_id=None, instance_name=None, size=None, begin_time=None, end_time=None):
        r"""BinlogInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  Binlog日志文件ID。   **取值范围**：  不涉及。
        :type id: str
        :param name: **参数解释**：  Binlog日志文件名字。   **取值范围**：  不涉及。
        :type name: str
        :param instance_id: **参数解释**：  Binlog日志对应的实例ID。   **取值范围**：  不涉及。
        :type instance_id: str
        :param instance_name: **参数解释**：  Binlog日志对应的实例名称。   **取值范围**：  不涉及。
        :type instance_name: str
        :param size: **参数解释**：  Binlog日志文件大小，单位是KB。   **取值范围**：  不涉及。
        :type size: int
        :param begin_time: **参数解释**：  Binlog日志文件中上一轮任务的最后一个事务的提交时间。   **取值范围**：  不涉及。
        :type begin_time: str
        :param end_time: **参数解释**：  Binlog日志文件中最后一个事务的提交时间。   **取值范围**：  不涉及。
        :type end_time: str
        """
        
        

        self._id = None
        self._name = None
        self._instance_id = None
        self._instance_name = None
        self._size = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if size is not None:
            self.size = size
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        r"""Gets the id of this BinlogInfo.

        **参数解释**：  Binlog日志文件ID。   **取值范围**：  不涉及。

        :return: The id of this BinlogInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BinlogInfo.

        **参数解释**：  Binlog日志文件ID。   **取值范围**：  不涉及。

        :param id: The id of this BinlogInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BinlogInfo.

        **参数解释**：  Binlog日志文件名字。   **取值范围**：  不涉及。

        :return: The name of this BinlogInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BinlogInfo.

        **参数解释**：  Binlog日志文件名字。   **取值范围**：  不涉及。

        :param name: The name of this BinlogInfo.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BinlogInfo.

        **参数解释**：  Binlog日志对应的实例ID。   **取值范围**：  不涉及。

        :return: The instance_id of this BinlogInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BinlogInfo.

        **参数解释**：  Binlog日志对应的实例ID。   **取值范围**：  不涉及。

        :param instance_id: The instance_id of this BinlogInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this BinlogInfo.

        **参数解释**：  Binlog日志对应的实例名称。   **取值范围**：  不涉及。

        :return: The instance_name of this BinlogInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this BinlogInfo.

        **参数解释**：  Binlog日志对应的实例名称。   **取值范围**：  不涉及。

        :param instance_name: The instance_name of this BinlogInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def size(self):
        r"""Gets the size of this BinlogInfo.

        **参数解释**：  Binlog日志文件大小，单位是KB。   **取值范围**：  不涉及。

        :return: The size of this BinlogInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BinlogInfo.

        **参数解释**：  Binlog日志文件大小，单位是KB。   **取值范围**：  不涉及。

        :param size: The size of this BinlogInfo.
        :type size: int
        """
        self._size = size

    @property
    def begin_time(self):
        r"""Gets the begin_time of this BinlogInfo.

        **参数解释**：  Binlog日志文件中上一轮任务的最后一个事务的提交时间。   **取值范围**：  不涉及。

        :return: The begin_time of this BinlogInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this BinlogInfo.

        **参数解释**：  Binlog日志文件中上一轮任务的最后一个事务的提交时间。   **取值范围**：  不涉及。

        :param begin_time: The begin_time of this BinlogInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BinlogInfo.

        **参数解释**：  Binlog日志文件中最后一个事务的提交时间。   **取值范围**：  不涉及。

        :return: The end_time of this BinlogInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BinlogInfo.

        **参数解释**：  Binlog日志文件中最后一个事务的提交时间。   **取值范围**：  不涉及。

        :param end_time: The end_time of this BinlogInfo.
        :type end_time: str
        """
        self._end_time = end_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BinlogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
