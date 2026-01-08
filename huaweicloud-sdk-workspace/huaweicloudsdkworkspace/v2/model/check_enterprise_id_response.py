# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckEnterpriseIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_used': 'bool',
        'enterprise_id': 'str'
    }

    attribute_map = {
        'is_used': 'is_used',
        'enterprise_id': 'enterprise_id'
    }

    def __init__(self, is_used=None, enterprise_id=None):
        r"""CheckEnterpriseIdResponse

        The model defined in huaweicloud sdk

        :param is_used: 企业ID是否已被使用。
        :type is_used: bool
        :param enterprise_id: 企业ID。
        :type enterprise_id: str
        """
        
        super().__init__()

        self._is_used = None
        self._enterprise_id = None
        self.discriminator = None

        if is_used is not None:
            self.is_used = is_used
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id

    @property
    def is_used(self):
        r"""Gets the is_used of this CheckEnterpriseIdResponse.

        企业ID是否已被使用。

        :return: The is_used of this CheckEnterpriseIdResponse.
        :rtype: bool
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        r"""Sets the is_used of this CheckEnterpriseIdResponse.

        企业ID是否已被使用。

        :param is_used: The is_used of this CheckEnterpriseIdResponse.
        :type is_used: bool
        """
        self._is_used = is_used

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this CheckEnterpriseIdResponse.

        企业ID。

        :return: The enterprise_id of this CheckEnterpriseIdResponse.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this CheckEnterpriseIdResponse.

        企业ID。

        :param enterprise_id: The enterprise_id of this CheckEnterpriseIdResponse.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    def to_dict(self):
        import warnings
        warnings.warn("CheckEnterpriseIdResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckEnterpriseIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
