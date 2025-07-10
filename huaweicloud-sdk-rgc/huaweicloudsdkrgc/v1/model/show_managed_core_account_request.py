# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowManagedCoreAccountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_type': 'str'
    }

    attribute_map = {
        'account_type': 'account_type'
    }

    def __init__(self, account_type=None):
        r"""ShowManagedCoreAccountRequest

        The model defined in huaweicloud sdk

        :param account_type: 纳管账号类型。类型包括LOGGING，SECURITY和PRIMARY。
        :type account_type: str
        """
        
        

        self._account_type = None
        self.discriminator = None

        self.account_type = account_type

    @property
    def account_type(self):
        r"""Gets the account_type of this ShowManagedCoreAccountRequest.

        纳管账号类型。类型包括LOGGING，SECURITY和PRIMARY。

        :return: The account_type of this ShowManagedCoreAccountRequest.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this ShowManagedCoreAccountRequest.

        纳管账号类型。类型包括LOGGING，SECURITY和PRIMARY。

        :param account_type: The account_type of this ShowManagedCoreAccountRequest.
        :type account_type: str
        """
        self._account_type = account_type

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
        if not isinstance(other, ShowManagedCoreAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
