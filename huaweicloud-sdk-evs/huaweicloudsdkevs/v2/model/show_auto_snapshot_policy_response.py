# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoSnapshotPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_policy': 'GetSnapshotPolicy'
    }

    attribute_map = {
        'snapshot_policy': 'snapshot_policy'
    }

    def __init__(self, snapshot_policy=None):
        r"""ShowAutoSnapshotPolicyResponse

        The model defined in huaweicloud sdk

        :param snapshot_policy: 
        :type snapshot_policy: :class:`huaweicloudsdkevs.v2.GetSnapshotPolicy`
        """
        
        super().__init__()

        self._snapshot_policy = None
        self.discriminator = None

        if snapshot_policy is not None:
            self.snapshot_policy = snapshot_policy

    @property
    def snapshot_policy(self):
        r"""Gets the snapshot_policy of this ShowAutoSnapshotPolicyResponse.

        :return: The snapshot_policy of this ShowAutoSnapshotPolicyResponse.
        :rtype: :class:`huaweicloudsdkevs.v2.GetSnapshotPolicy`
        """
        return self._snapshot_policy

    @snapshot_policy.setter
    def snapshot_policy(self, snapshot_policy):
        r"""Sets the snapshot_policy of this ShowAutoSnapshotPolicyResponse.

        :param snapshot_policy: The snapshot_policy of this ShowAutoSnapshotPolicyResponse.
        :type snapshot_policy: :class:`huaweicloudsdkevs.v2.GetSnapshotPolicy`
        """
        self._snapshot_policy = snapshot_policy

    def to_dict(self):
        import warnings
        warnings.warn("ShowAutoSnapshotPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAutoSnapshotPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
