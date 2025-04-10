# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAuthorizationSchemaV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_code': 'str'
    }

    attribute_map = {
        'service_code': 'service_code'
    }

    def __init__(self, service_code=None):
        r"""GetAuthorizationSchemaV5Request

        The model defined in huaweicloud sdk

        :param service_code: 服务名称缩写，长度为1到56个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type service_code: str
        """
        
        

        self._service_code = None
        self.discriminator = None

        self.service_code = service_code

    @property
    def service_code(self):
        r"""Gets the service_code of this GetAuthorizationSchemaV5Request.

        服务名称缩写，长度为1到56个字符，只包含字母、数字和\"-\"的字符串。

        :return: The service_code of this GetAuthorizationSchemaV5Request.
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        r"""Sets the service_code of this GetAuthorizationSchemaV5Request.

        服务名称缩写，长度为1到56个字符，只包含字母、数字和\"-\"的字符串。

        :param service_code: The service_code of this GetAuthorizationSchemaV5Request.
        :type service_code: str
        """
        self._service_code = service_code

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
        if not isinstance(other, GetAuthorizationSchemaV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
