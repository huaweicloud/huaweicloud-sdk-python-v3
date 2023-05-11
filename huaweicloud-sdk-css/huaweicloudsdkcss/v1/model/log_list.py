# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'date': 'str',
        'level': 'str'
    }

    attribute_map = {
        'content': 'content',
        'date': 'date',
        'level': 'level'
    }

    def __init__(self, content=None, date=None, level=None):
        """LogList

        The model defined in huaweicloud sdk

        :param content: 日志内容。
        :type content: str
        :param date: 日期。
        :type date: str
        :param level: 日志级别。
        :type level: str
        """
        
        

        self._content = None
        self._date = None
        self._level = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if date is not None:
            self.date = date
        if level is not None:
            self.level = level

    @property
    def content(self):
        """Gets the content of this LogList.

        日志内容。

        :return: The content of this LogList.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this LogList.

        日志内容。

        :param content: The content of this LogList.
        :type content: str
        """
        self._content = content

    @property
    def date(self):
        """Gets the date of this LogList.

        日期。

        :return: The date of this LogList.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this LogList.

        日期。

        :param date: The date of this LogList.
        :type date: str
        """
        self._date = date

    @property
    def level(self):
        """Gets the level of this LogList.

        日志级别。

        :return: The level of this LogList.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this LogList.

        日志级别。

        :param level: The level of this LogList.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, LogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
