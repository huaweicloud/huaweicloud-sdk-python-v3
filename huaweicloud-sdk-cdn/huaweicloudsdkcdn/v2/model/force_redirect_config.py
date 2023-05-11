# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForceRedirectConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'type': 'str',
        'redirect_code': 'int'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'redirect_code': 'redirect_code'
    }

    def __init__(self, status=None, type=None, redirect_code=None):
        """ForceRedirectConfig

        The model defined in huaweicloud sdk

        :param status: 强制跳转开关（on：打开，off：关闭）。
        :type status: str
        :param type: 强制跳转类型（http：强制跳转HTTP，https：强制跳转HTTPS）。
        :type type: str
        :param redirect_code: 重定向跳转码301,302。
        :type redirect_code: int
        """
        
        

        self._status = None
        self._type = None
        self._redirect_code = None
        self.discriminator = None

        self.status = status
        if type is not None:
            self.type = type
        if redirect_code is not None:
            self.redirect_code = redirect_code

    @property
    def status(self):
        """Gets the status of this ForceRedirectConfig.

        强制跳转开关（on：打开，off：关闭）。

        :return: The status of this ForceRedirectConfig.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ForceRedirectConfig.

        强制跳转开关（on：打开，off：关闭）。

        :param status: The status of this ForceRedirectConfig.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ForceRedirectConfig.

        强制跳转类型（http：强制跳转HTTP，https：强制跳转HTTPS）。

        :return: The type of this ForceRedirectConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ForceRedirectConfig.

        强制跳转类型（http：强制跳转HTTP，https：强制跳转HTTPS）。

        :param type: The type of this ForceRedirectConfig.
        :type type: str
        """
        self._type = type

    @property
    def redirect_code(self):
        """Gets the redirect_code of this ForceRedirectConfig.

        重定向跳转码301,302。

        :return: The redirect_code of this ForceRedirectConfig.
        :rtype: int
        """
        return self._redirect_code

    @redirect_code.setter
    def redirect_code(self, redirect_code):
        """Sets the redirect_code of this ForceRedirectConfig.

        重定向跳转码301,302。

        :param redirect_code: The redirect_code of this ForceRedirectConfig.
        :type redirect_code: int
        """
        self._redirect_code = redirect_code

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
        if not isinstance(other, ForceRedirectConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
