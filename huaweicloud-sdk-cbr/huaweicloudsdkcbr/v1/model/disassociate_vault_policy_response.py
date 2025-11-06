# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateVaultPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dissociate_policy': 'VaultPolicyResp'
    }

    attribute_map = {
        'dissociate_policy': 'dissociate_policy'
    }

    def __init__(self, dissociate_policy=None):
        r"""DisassociateVaultPolicyResponse

        The model defined in huaweicloud sdk

        :param dissociate_policy: 
        :type dissociate_policy: :class:`huaweicloudsdkcbr.v1.VaultPolicyResp`
        """
        
        super().__init__()

        self._dissociate_policy = None
        self.discriminator = None

        if dissociate_policy is not None:
            self.dissociate_policy = dissociate_policy

    @property
    def dissociate_policy(self):
        r"""Gets the dissociate_policy of this DisassociateVaultPolicyResponse.

        :return: The dissociate_policy of this DisassociateVaultPolicyResponse.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultPolicyResp`
        """
        return self._dissociate_policy

    @dissociate_policy.setter
    def dissociate_policy(self, dissociate_policy):
        r"""Sets the dissociate_policy of this DisassociateVaultPolicyResponse.

        :param dissociate_policy: The dissociate_policy of this DisassociateVaultPolicyResponse.
        :type dissociate_policy: :class:`huaweicloudsdkcbr.v1.VaultPolicyResp`
        """
        self._dissociate_policy = dissociate_policy

    def to_dict(self):
        import warnings
        warnings.warn("DisassociateVaultPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DisassociateVaultPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
