# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetReplicaReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partitions': 'list[ResetReplicaReqPartitions]'
    }

    attribute_map = {
        'partitions': 'partitions'
    }

    def __init__(self, partitions=None):
        r"""ResetReplicaReq

        The model defined in huaweicloud sdk

        :param partitions: 期望调整的分区副本分配情况。
        :type partitions: list[:class:`huaweicloudsdkkafka.v2.ResetReplicaReqPartitions`]
        """
        
        

        self._partitions = None
        self.discriminator = None

        if partitions is not None:
            self.partitions = partitions

    @property
    def partitions(self):
        r"""Gets the partitions of this ResetReplicaReq.

        期望调整的分区副本分配情况。

        :return: The partitions of this ResetReplicaReq.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ResetReplicaReqPartitions`]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        r"""Sets the partitions of this ResetReplicaReq.

        期望调整的分区副本分配情况。

        :param partitions: The partitions of this ResetReplicaReq.
        :type partitions: list[:class:`huaweicloudsdkkafka.v2.ResetReplicaReqPartitions`]
        """
        self._partitions = partitions

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
        if not isinstance(other, ResetReplicaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
