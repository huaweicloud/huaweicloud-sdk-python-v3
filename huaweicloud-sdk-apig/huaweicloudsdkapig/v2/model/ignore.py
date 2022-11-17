# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Ignore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'method': 'str',
        'path': 'str'
    }

    attribute_map = {
        'method': 'method',
        'path': 'path'
    }

    def __init__(self, method=None, path=None):
        """Ignore

        The model defined in huaweicloud sdk

        :param method: API请求方法
        :type method: str
        :param path: API请求路径
        :type path: str
        """
        
        

        self._method = None
        self._path = None
        self.discriminator = None

        if method is not None:
            self.method = method
        if path is not None:
            self.path = path

    @property
    def method(self):
        """Gets the method of this Ignore.

        API请求方法

        :return: The method of this Ignore.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Ignore.

        API请求方法

        :param method: The method of this Ignore.
        :type method: str
        """
        self._method = method

    @property
    def path(self):
        """Gets the path of this Ignore.

        API请求路径

        :return: The path of this Ignore.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Ignore.

        API请求路径

        :param path: The path of this Ignore.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, Ignore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
