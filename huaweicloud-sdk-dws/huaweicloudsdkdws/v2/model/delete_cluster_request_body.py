# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_last_manual_snapshot': 'int'
    }

    attribute_map = {
        'keep_last_manual_snapshot': 'keep_last_manual_snapshot'
    }

    def __init__(self, keep_last_manual_snapshot=None):
        r"""DeleteClusterRequestBody

        The model defined in huaweicloud sdk

        :param keep_last_manual_snapshot: **参数解释**： 集群需要保留的快照数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type keep_last_manual_snapshot: int
        """
        
        

        self._keep_last_manual_snapshot = None
        self.discriminator = None

        self.keep_last_manual_snapshot = keep_last_manual_snapshot

    @property
    def keep_last_manual_snapshot(self):
        r"""Gets the keep_last_manual_snapshot of this DeleteClusterRequestBody.

        **参数解释**： 集群需要保留的快照数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The keep_last_manual_snapshot of this DeleteClusterRequestBody.
        :rtype: int
        """
        return self._keep_last_manual_snapshot

    @keep_last_manual_snapshot.setter
    def keep_last_manual_snapshot(self, keep_last_manual_snapshot):
        r"""Sets the keep_last_manual_snapshot of this DeleteClusterRequestBody.

        **参数解释**： 集群需要保留的快照数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param keep_last_manual_snapshot: The keep_last_manual_snapshot of this DeleteClusterRequestBody.
        :type keep_last_manual_snapshot: int
        """
        self._keep_last_manual_snapshot = keep_last_manual_snapshot

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
        if not isinstance(other, DeleteClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
