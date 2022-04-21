# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSnapshotRequest:

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
        """DeleteSnapshotRequest

        The model defined in huaweicloud sdk

        :param snapshot_id: 快照ID。
        :type snapshot_id: str
        """
        
        

        self._snapshot_id = None
        self.discriminator = None

        self.snapshot_id = snapshot_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this DeleteSnapshotRequest.

        快照ID。

        :return: The snapshot_id of this DeleteSnapshotRequest.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this DeleteSnapshotRequest.

        快照ID。

        :param snapshot_id: The snapshot_id of this DeleteSnapshotRequest.
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
        if not isinstance(other, DeleteSnapshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
