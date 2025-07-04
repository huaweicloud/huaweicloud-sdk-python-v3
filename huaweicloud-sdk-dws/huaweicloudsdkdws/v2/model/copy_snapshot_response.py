# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopySnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_id': 'str'
    }

    attribute_map = {
        'snapshot_id': 'snapshot_id'
    }

    def __init__(self, snapshot_id=None):
        r"""CopySnapshotResponse

        The model defined in huaweicloud sdk

        :param snapshot_id: **参数解释**： 快照ID。 **取值范围**： 不涉及。
        :type snapshot_id: str
        """
        
        super(CopySnapshotResponse, self).__init__()

        self._snapshot_id = None
        self.discriminator = None

        if snapshot_id is not None:
            self.snapshot_id = snapshot_id

    @property
    def snapshot_id(self):
        r"""Gets the snapshot_id of this CopySnapshotResponse.

        **参数解释**： 快照ID。 **取值范围**： 不涉及。

        :return: The snapshot_id of this CopySnapshotResponse.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        r"""Sets the snapshot_id of this CopySnapshotResponse.

        **参数解释**： 快照ID。 **取值范围**： 不涉及。

        :param snapshot_id: The snapshot_id of this CopySnapshotResponse.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

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
        if not isinstance(other, CopySnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
