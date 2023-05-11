# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MfaRsp:

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
        'info': 'str'
    }

    attribute_map = {
        'method': 'method',
        'info': 'info'
    }

    def __init__(self, method=None, info=None):
        """MfaRsp

        The model defined in huaweicloud sdk

        :param method: mfa方法
        :type method: str
        :param info: mfa信息
        :type info: str
        """
        
        

        self._method = None
        self._info = None
        self.discriminator = None

        if method is not None:
            self.method = method
        if info is not None:
            self.info = info

    @property
    def method(self):
        """Gets the method of this MfaRsp.

        mfa方法

        :return: The method of this MfaRsp.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this MfaRsp.

        mfa方法

        :param method: The method of this MfaRsp.
        :type method: str
        """
        self._method = method

    @property
    def info(self):
        """Gets the info of this MfaRsp.

        mfa信息

        :return: The info of this MfaRsp.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this MfaRsp.

        mfa信息

        :param info: The info of this MfaRsp.
        :type info: str
        """
        self._info = info

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
        if not isinstance(other, MfaRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
