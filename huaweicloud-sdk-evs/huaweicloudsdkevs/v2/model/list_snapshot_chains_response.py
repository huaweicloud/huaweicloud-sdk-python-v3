# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotChainsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_chains': 'list[ListSnapshotChainsResponseBodySnapshotChains]'
    }

    attribute_map = {
        'snapshot_chains': 'snapshot_chains'
    }

    def __init__(self, snapshot_chains=None):
        r"""ListSnapshotChainsResponse

        The model defined in huaweicloud sdk

        :param snapshot_chains: **参数解释** 快照链列表。 **取值范围** 不涉及
        :type snapshot_chains: list[:class:`huaweicloudsdkevs.v2.ListSnapshotChainsResponseBodySnapshotChains`]
        """
        
        super().__init__()

        self._snapshot_chains = None
        self.discriminator = None

        if snapshot_chains is not None:
            self.snapshot_chains = snapshot_chains

    @property
    def snapshot_chains(self):
        r"""Gets the snapshot_chains of this ListSnapshotChainsResponse.

        **参数解释** 快照链列表。 **取值范围** 不涉及

        :return: The snapshot_chains of this ListSnapshotChainsResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.ListSnapshotChainsResponseBodySnapshotChains`]
        """
        return self._snapshot_chains

    @snapshot_chains.setter
    def snapshot_chains(self, snapshot_chains):
        r"""Sets the snapshot_chains of this ListSnapshotChainsResponse.

        **参数解释** 快照链列表。 **取值范围** 不涉及

        :param snapshot_chains: The snapshot_chains of this ListSnapshotChainsResponse.
        :type snapshot_chains: list[:class:`huaweicloudsdkevs.v2.ListSnapshotChainsResponseBodySnapshotChains`]
        """
        self._snapshot_chains = snapshot_chains

    def to_dict(self):
        import warnings
        warnings.warn("ListSnapshotChainsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSnapshotChainsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
