# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionReassignRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reassignments': 'list[PartitionReassignEntity]',
        'throttle': 'int'
    }

    attribute_map = {
        'reassignments': 'reassignments',
        'throttle': 'throttle'
    }

    def __init__(self, reassignments=None, throttle=None):
        """PartitionReassignRequest

        The model defined in huaweicloud sdk

        :param reassignments: 重平衡分配方案。
        :type reassignments: list[:class:`huaweicloudsdkkafka.v2.PartitionReassignEntity`]
        :param throttle: 重平衡门限值。
        :type throttle: int
        """
        
        

        self._reassignments = None
        self._throttle = None
        self.discriminator = None

        self.reassignments = reassignments
        if throttle is not None:
            self.throttle = throttle

    @property
    def reassignments(self):
        """Gets the reassignments of this PartitionReassignRequest.

        重平衡分配方案。

        :return: The reassignments of this PartitionReassignRequest.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.PartitionReassignEntity`]
        """
        return self._reassignments

    @reassignments.setter
    def reassignments(self, reassignments):
        """Sets the reassignments of this PartitionReassignRequest.

        重平衡分配方案。

        :param reassignments: The reassignments of this PartitionReassignRequest.
        :type reassignments: list[:class:`huaweicloudsdkkafka.v2.PartitionReassignEntity`]
        """
        self._reassignments = reassignments

    @property
    def throttle(self):
        """Gets the throttle of this PartitionReassignRequest.

        重平衡门限值。

        :return: The throttle of this PartitionReassignRequest.
        :rtype: int
        """
        return self._throttle

    @throttle.setter
    def throttle(self, throttle):
        """Sets the throttle of this PartitionReassignRequest.

        重平衡门限值。

        :param throttle: The throttle of this PartitionReassignRequest.
        :type throttle: int
        """
        self._throttle = throttle

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
        if not isinstance(other, PartitionReassignRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
