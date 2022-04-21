# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Auditlog:

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
        'size': 'int',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'size': 'size',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, name=None, size=None, begin_time=None, end_time=None):
        """Auditlog

        The model defined in huaweicloud sdk

        :param id: 审计日志ID。
        :type id: str
        :param name: 审计日志文件名。
        :type name: str
        :param size: 审计日志大小，单位：KB。
        :type size: int
        :param begin_time: 审计日志开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type begin_time: str
        :param end_time: 审计日志结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        """
        
        

        self._id = None
        self._name = None
        self._size = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this Auditlog.

        审计日志ID。

        :return: The id of this Auditlog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Auditlog.

        审计日志ID。

        :param id: The id of this Auditlog.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Auditlog.

        审计日志文件名。

        :return: The name of this Auditlog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Auditlog.

        审计日志文件名。

        :param name: The name of this Auditlog.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this Auditlog.

        审计日志大小，单位：KB。

        :return: The size of this Auditlog.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Auditlog.

        审计日志大小，单位：KB。

        :param size: The size of this Auditlog.
        :type size: int
        """
        self._size = size

    @property
    def begin_time(self):
        """Gets the begin_time of this Auditlog.

        审计日志开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The begin_time of this Auditlog.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this Auditlog.

        审计日志开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param begin_time: The begin_time of this Auditlog.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this Auditlog.

        审计日志结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this Auditlog.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Auditlog.

        审计日志结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this Auditlog.
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
        if not isinstance(other, Auditlog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
