# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'name': 'str',
        'size': 'int',
        'link': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'name': 'name',
        'size': 'size',
        'link': 'link'
    }

    def __init__(self, domain_name=None, start_time=None, end_time=None, name=None, size=None, link=None):
        """LogObject

        The model defined in huaweicloud sdk

        :param domain_name: 域名名称。
        :type domain_name: str
        :param start_time: 查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type start_time: int
        :param end_time: 查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type end_time: int
        :param name: 日志文件名字。
        :type name: str
        :param size: 文件大小(Byte)。
        :type size: int
        :param link: 下载链接。
        :type link: str
        """
        
        

        self._domain_name = None
        self._start_time = None
        self._end_time = None
        self._name = None
        self._size = None
        self._link = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if link is not None:
            self.link = link

    @property
    def domain_name(self):
        """Gets the domain_name of this LogObject.

        域名名称。

        :return: The domain_name of this LogObject.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this LogObject.

        域名名称。

        :param domain_name: The domain_name of this LogObject.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def start_time(self):
        """Gets the start_time of this LogObject.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The start_time of this LogObject.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this LogObject.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param start_time: The start_time of this LogObject.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this LogObject.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The end_time of this LogObject.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this LogObject.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param end_time: The end_time of this LogObject.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def name(self):
        """Gets the name of this LogObject.

        日志文件名字。

        :return: The name of this LogObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LogObject.

        日志文件名字。

        :param name: The name of this LogObject.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this LogObject.

        文件大小(Byte)。

        :return: The size of this LogObject.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LogObject.

        文件大小(Byte)。

        :param size: The size of this LogObject.
        :type size: int
        """
        self._size = size

    @property
    def link(self):
        """Gets the link of this LogObject.

        下载链接。

        :return: The link of this LogObject.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this LogObject.

        下载链接。

        :param link: The link of this LogObject.
        :type link: str
        """
        self._link = link

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
        if not isinstance(other, LogObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
