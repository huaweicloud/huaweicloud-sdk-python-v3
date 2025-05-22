# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretsConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checking_secret_strength': 'bool'
    }

    attribute_map = {
        'checking_secret_strength': 'checking_secret_strength'
    }

    def __init__(self, checking_secret_strength=None):
        r"""UpdateSecretsConfigRequestBody

        The model defined in huaweicloud sdk

        :param checking_secret_strength: 凭据强度检测配置是否打开。
        :type checking_secret_strength: bool
        """
        
        

        self._checking_secret_strength = None
        self.discriminator = None

        if checking_secret_strength is not None:
            self.checking_secret_strength = checking_secret_strength

    @property
    def checking_secret_strength(self):
        r"""Gets the checking_secret_strength of this UpdateSecretsConfigRequestBody.

        凭据强度检测配置是否打开。

        :return: The checking_secret_strength of this UpdateSecretsConfigRequestBody.
        :rtype: bool
        """
        return self._checking_secret_strength

    @checking_secret_strength.setter
    def checking_secret_strength(self, checking_secret_strength):
        r"""Sets the checking_secret_strength of this UpdateSecretsConfigRequestBody.

        凭据强度检测配置是否打开。

        :param checking_secret_strength: The checking_secret_strength of this UpdateSecretsConfigRequestBody.
        :type checking_secret_strength: bool
        """
        self._checking_secret_strength = checking_secret_strength

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
        if not isinstance(other, UpdateSecretsConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
