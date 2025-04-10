# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetActiveCodeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clean_auth_credential': 'bool'
    }

    attribute_map = {
        'clean_auth_credential': 'clean_auth_credential'
    }

    def __init__(self, clean_auth_credential=None):
        r"""ResetActiveCodeReq

        The model defined in huaweicloud sdk

        :param clean_auth_credential: 是否清除鉴权凭证。
        :type clean_auth_credential: bool
        """
        
        

        self._clean_auth_credential = None
        self.discriminator = None

        if clean_auth_credential is not None:
            self.clean_auth_credential = clean_auth_credential

    @property
    def clean_auth_credential(self):
        r"""Gets the clean_auth_credential of this ResetActiveCodeReq.

        是否清除鉴权凭证。

        :return: The clean_auth_credential of this ResetActiveCodeReq.
        :rtype: bool
        """
        return self._clean_auth_credential

    @clean_auth_credential.setter
    def clean_auth_credential(self, clean_auth_credential):
        r"""Sets the clean_auth_credential of this ResetActiveCodeReq.

        是否清除鉴权凭证。

        :param clean_auth_credential: The clean_auth_credential of this ResetActiveCodeReq.
        :type clean_auth_credential: bool
        """
        self._clean_auth_credential = clean_auth_credential

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
        if not isinstance(other, ResetActiveCodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
