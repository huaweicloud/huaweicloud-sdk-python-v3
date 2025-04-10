# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRestoreSnapshotReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_ids': 'list[str]'
    }

    attribute_map = {
        'snapshot_ids': 'snapshot_ids'
    }

    def __init__(self, snapshot_ids=None):
        r"""BatchRestoreSnapshotReq

        The model defined in huaweicloud sdk

        :param snapshot_ids: 桌面快照记录id数组，最多支持100。
        :type snapshot_ids: list[str]
        """
        
        

        self._snapshot_ids = None
        self.discriminator = None

        if snapshot_ids is not None:
            self.snapshot_ids = snapshot_ids

    @property
    def snapshot_ids(self):
        r"""Gets the snapshot_ids of this BatchRestoreSnapshotReq.

        桌面快照记录id数组，最多支持100。

        :return: The snapshot_ids of this BatchRestoreSnapshotReq.
        :rtype: list[str]
        """
        return self._snapshot_ids

    @snapshot_ids.setter
    def snapshot_ids(self, snapshot_ids):
        r"""Sets the snapshot_ids of this BatchRestoreSnapshotReq.

        桌面快照记录id数组，最多支持100。

        :param snapshot_ids: The snapshot_ids of this BatchRestoreSnapshotReq.
        :type snapshot_ids: list[str]
        """
        self._snapshot_ids = snapshot_ids

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
        if not isinstance(other, BatchRestoreSnapshotReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
