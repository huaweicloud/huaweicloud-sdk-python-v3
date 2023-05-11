# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneValidateTokenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_subject_token')

    openapi_types = {
        'x_subject_token': 'str',
        'nocatalog': 'str'
    }

    attribute_map = {
        'x_subject_token': 'X-Subject-Token',
        'nocatalog': 'nocatalog'
    }

    def __init__(self, x_subject_token=None, nocatalog=None):
        """KeystoneValidateTokenRequest

        The model defined in huaweicloud sdk

        :param x_subject_token: 待校验的token。
        :type x_subject_token: str
        :param nocatalog: 如果设置该参数，返回的响应体中将不显示catalog信息。任何非空字符串都将解释为true，并使该字段生效。
        :type nocatalog: str
        """
        
        

        self._x_subject_token = None
        self._nocatalog = None
        self.discriminator = None

        self.x_subject_token = x_subject_token
        if nocatalog is not None:
            self.nocatalog = nocatalog

    @property
    def x_subject_token(self):
        """Gets the x_subject_token of this KeystoneValidateTokenRequest.

        待校验的token。

        :return: The x_subject_token of this KeystoneValidateTokenRequest.
        :rtype: str
        """
        return self._x_subject_token

    @x_subject_token.setter
    def x_subject_token(self, x_subject_token):
        """Sets the x_subject_token of this KeystoneValidateTokenRequest.

        待校验的token。

        :param x_subject_token: The x_subject_token of this KeystoneValidateTokenRequest.
        :type x_subject_token: str
        """
        self._x_subject_token = x_subject_token

    @property
    def nocatalog(self):
        """Gets the nocatalog of this KeystoneValidateTokenRequest.

        如果设置该参数，返回的响应体中将不显示catalog信息。任何非空字符串都将解释为true，并使该字段生效。

        :return: The nocatalog of this KeystoneValidateTokenRequest.
        :rtype: str
        """
        return self._nocatalog

    @nocatalog.setter
    def nocatalog(self, nocatalog):
        """Sets the nocatalog of this KeystoneValidateTokenRequest.

        如果设置该参数，返回的响应体中将不显示catalog信息。任何非空字符串都将解释为true，并使该字段生效。

        :param nocatalog: The nocatalog of this KeystoneValidateTokenRequest.
        :type nocatalog: str
        """
        self._nocatalog = nocatalog

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
        if not isinstance(other, KeystoneValidateTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
