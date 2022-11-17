# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Failure:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'error_msg': 'str',
        'method': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'path': 'path',
        'error_msg': 'error_msg',
        'method': 'method',
        'error_code': 'error_code'
    }

    def __init__(self, path=None, error_msg=None, method=None, error_code=None):
        """Failure

        The model defined in huaweicloud sdk

        :param path: API请求路径
        :type path: str
        :param error_msg: 导入失败的错误信息
        :type error_msg: str
        :param method: API请求方法
        :type method: str
        :param error_code: 导入失败的错误码
        :type error_code: str
        """
        
        

        self._path = None
        self._error_msg = None
        self._method = None
        self._error_code = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if error_msg is not None:
            self.error_msg = error_msg
        if method is not None:
            self.method = method
        if error_code is not None:
            self.error_code = error_code

    @property
    def path(self):
        """Gets the path of this Failure.

        API请求路径

        :return: The path of this Failure.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Failure.

        API请求路径

        :param path: The path of this Failure.
        :type path: str
        """
        self._path = path

    @property
    def error_msg(self):
        """Gets the error_msg of this Failure.

        导入失败的错误信息

        :return: The error_msg of this Failure.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this Failure.

        导入失败的错误信息

        :param error_msg: The error_msg of this Failure.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def method(self):
        """Gets the method of this Failure.

        API请求方法

        :return: The method of this Failure.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Failure.

        API请求方法

        :param method: The method of this Failure.
        :type method: str
        """
        self._method = method

    @property
    def error_code(self):
        """Gets the error_code of this Failure.

        导入失败的错误码

        :return: The error_code of this Failure.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Failure.

        导入失败的错误码

        :param error_code: The error_code of this Failure.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, Failure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
