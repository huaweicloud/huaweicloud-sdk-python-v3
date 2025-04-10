# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncrementalBackups:

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
        'begin_time': 'str',
        'end_time': 'str',
        'size': 'float',
        'instance_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'size': 'size',
        'instance_id': 'instance_id'
    }

    def __init__(self, id=None, name=None, begin_time=None, end_time=None, size=None, instance_id=None):
        r"""IncrementalBackups

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param begin_time: 备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type begin_time: str
        :param end_time: 备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        :param size: 备份大小，(单位：KB)。
        :type size: float
        :param instance_id: 实例ID。
        :type instance_id: str
        """
        
        

        self._id = None
        self._name = None
        self._begin_time = None
        self._end_time = None
        self._size = None
        self._instance_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if size is not None:
            self.size = size
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def id(self):
        r"""Gets the id of this IncrementalBackups.

        备份ID。

        :return: The id of this IncrementalBackups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IncrementalBackups.

        备份ID。

        :param id: The id of this IncrementalBackups.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this IncrementalBackups.

        备份名称。

        :return: The name of this IncrementalBackups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IncrementalBackups.

        备份名称。

        :param name: The name of this IncrementalBackups.
        :type name: str
        """
        self._name = name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this IncrementalBackups.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The begin_time of this IncrementalBackups.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this IncrementalBackups.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param begin_time: The begin_time of this IncrementalBackups.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this IncrementalBackups.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this IncrementalBackups.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this IncrementalBackups.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this IncrementalBackups.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def size(self):
        r"""Gets the size of this IncrementalBackups.

        备份大小，(单位：KB)。

        :return: The size of this IncrementalBackups.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this IncrementalBackups.

        备份大小，(单位：KB)。

        :param size: The size of this IncrementalBackups.
        :type size: float
        """
        self._size = size

    @property
    def instance_id(self):
        r"""Gets the instance_id of this IncrementalBackups.

        实例ID。

        :return: The instance_id of this IncrementalBackups.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this IncrementalBackups.

        实例ID。

        :param instance_id: The instance_id of this IncrementalBackups.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, IncrementalBackups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
