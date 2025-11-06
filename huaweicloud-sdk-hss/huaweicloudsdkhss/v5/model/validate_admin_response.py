# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateAdminResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_admin_account': 'bool'
    }

    attribute_map = {
        'is_admin_account': 'is_admin_account'
    }

    def __init__(self, is_admin_account=None):
        r"""ValidateAdminResponse

        The model defined in huaweicloud sdk

        :param is_admin_account: 是否是管理员账号
        :type is_admin_account: bool
        """
        
        super().__init__()

        self._is_admin_account = None
        self.discriminator = None

        if is_admin_account is not None:
            self.is_admin_account = is_admin_account

    @property
    def is_admin_account(self):
        r"""Gets the is_admin_account of this ValidateAdminResponse.

        是否是管理员账号

        :return: The is_admin_account of this ValidateAdminResponse.
        :rtype: bool
        """
        return self._is_admin_account

    @is_admin_account.setter
    def is_admin_account(self, is_admin_account):
        r"""Sets the is_admin_account of this ValidateAdminResponse.

        是否是管理员账号

        :param is_admin_account: The is_admin_account of this ValidateAdminResponse.
        :type is_admin_account: bool
        """
        self._is_admin_account = is_admin_account

    def to_dict(self):
        import warnings
        warnings.warn("ValidateAdminResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValidateAdminResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
