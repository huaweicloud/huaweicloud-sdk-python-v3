# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorSample:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'count': 'int',
        'msg': 'str'
    }

    attribute_map = {
        'source': 'source',
        'count': 'count',
        'msg': 'msg'
    }

    def __init__(self, source=None, count=None, msg=None):
        """ErrorSample

        The model defined in huaweicloud sdk

        :param source: 检测源描述。
        :type source: str
        :param count: 此错误共计次数。
        :type count: int
        :param msg: 错误数据和错误提示消息。
        :type msg: str
        """
        
        

        self._source = None
        self._count = None
        self._msg = None
        self.discriminator = None

        self.source = source
        if count is not None:
            self.count = count
        if msg is not None:
            self.msg = msg

    @property
    def source(self):
        """Gets the source of this ErrorSample.

        检测源描述。

        :return: The source of this ErrorSample.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ErrorSample.

        检测源描述。

        :param source: The source of this ErrorSample.
        :type source: str
        """
        self._source = source

    @property
    def count(self):
        """Gets the count of this ErrorSample.

        此错误共计次数。

        :return: The count of this ErrorSample.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ErrorSample.

        此错误共计次数。

        :param count: The count of this ErrorSample.
        :type count: int
        """
        self._count = count

    @property
    def msg(self):
        """Gets the msg of this ErrorSample.

        错误数据和错误提示消息。

        :return: The msg of this ErrorSample.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this ErrorSample.

        错误数据和错误提示消息。

        :param msg: The msg of this ErrorSample.
        :type msg: str
        """
        self._msg = msg

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
        if not isinstance(other, ErrorSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
