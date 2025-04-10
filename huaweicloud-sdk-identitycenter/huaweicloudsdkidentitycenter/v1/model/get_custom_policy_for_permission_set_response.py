# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetCustomPolicyForPermissionSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_policy': 'str'
    }

    attribute_map = {
        'custom_policy': 'custom_policy'
    }

    def __init__(self, custom_policy=None):
        r"""GetCustomPolicyForPermissionSetResponse

        The model defined in huaweicloud sdk

        :param custom_policy: 附加到权限集的自定义身份策略
        :type custom_policy: str
        """
        
        super(GetCustomPolicyForPermissionSetResponse, self).__init__()

        self._custom_policy = None
        self.discriminator = None

        if custom_policy is not None:
            self.custom_policy = custom_policy

    @property
    def custom_policy(self):
        r"""Gets the custom_policy of this GetCustomPolicyForPermissionSetResponse.

        附加到权限集的自定义身份策略

        :return: The custom_policy of this GetCustomPolicyForPermissionSetResponse.
        :rtype: str
        """
        return self._custom_policy

    @custom_policy.setter
    def custom_policy(self, custom_policy):
        r"""Sets the custom_policy of this GetCustomPolicyForPermissionSetResponse.

        附加到权限集的自定义身份策略

        :param custom_policy: The custom_policy of this GetCustomPolicyForPermissionSetResponse.
        :type custom_policy: str
        """
        self._custom_policy = custom_policy

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
        if not isinstance(other, GetCustomPolicyForPermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
