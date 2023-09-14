# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CorsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_cors': 'bool'
    }

    attribute_map = {
        'is_cors': 'is_cors'
    }

    def __init__(self, is_cors=None):
        """CorsConfig

        The model defined in huaweicloud sdk

        :param is_cors: 是否支持跨域
        :type is_cors: bool
        """
        
        

        self._is_cors = None
        self.discriminator = None

        if is_cors is not None:
            self.is_cors = is_cors

    @property
    def is_cors(self):
        """Gets the is_cors of this CorsConfig.

        是否支持跨域

        :return: The is_cors of this CorsConfig.
        :rtype: bool
        """
        return self._is_cors

    @is_cors.setter
    def is_cors(self, is_cors):
        """Sets the is_cors of this CorsConfig.

        是否支持跨域

        :param is_cors: The is_cors of this CorsConfig.
        :type is_cors: bool
        """
        self._is_cors = is_cors

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
        if not isinstance(other, CorsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
