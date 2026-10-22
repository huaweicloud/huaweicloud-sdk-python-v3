# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSnapshotGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_group': 'SnapshotGroupDetail'
    }

    attribute_map = {
        'snapshot_group': 'snapshot_group'
    }

    def __init__(self, snapshot_group=None):
        r"""UpdateSnapshotGroupResponse

        The model defined in huaweicloud sdk

        :param snapshot_group: 
        :type snapshot_group: :class:`huaweicloudsdkevs.v2.SnapshotGroupDetail`
        """
        
        super().__init__()

        self._snapshot_group = None
        self.discriminator = None

        if snapshot_group is not None:
            self.snapshot_group = snapshot_group

    @property
    def snapshot_group(self):
        r"""Gets the snapshot_group of this UpdateSnapshotGroupResponse.

        :return: The snapshot_group of this UpdateSnapshotGroupResponse.
        :rtype: :class:`huaweicloudsdkevs.v2.SnapshotGroupDetail`
        """
        return self._snapshot_group

    @snapshot_group.setter
    def snapshot_group(self, snapshot_group):
        r"""Sets the snapshot_group of this UpdateSnapshotGroupResponse.

        :param snapshot_group: The snapshot_group of this UpdateSnapshotGroupResponse.
        :type snapshot_group: :class:`huaweicloudsdkevs.v2.SnapshotGroupDetail`
        """
        self._snapshot_group = snapshot_group

    def to_dict(self):
        import warnings
        warnings.warn("UpdateSnapshotGroupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateSnapshotGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
