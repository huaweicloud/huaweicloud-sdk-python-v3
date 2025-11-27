# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'ready_num': 'int'
    }

    attribute_map = {
        'total_num': 'totalNum',
        'ready_num': 'readyNum'
    }

    def __init__(self, total_num=None, ready_num=None):
        r"""NodeSummary

        The model defined in huaweicloud sdk

        :param total_num: 集群中所有节点的个数。
        :type total_num: int
        :param ready_num: 集群中已就绪节点的数量。
        :type ready_num: int
        """
        
        

        self._total_num = None
        self._ready_num = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if ready_num is not None:
            self.ready_num = ready_num

    @property
    def total_num(self):
        r"""Gets the total_num of this NodeSummary.

        集群中所有节点的个数。

        :return: The total_num of this NodeSummary.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this NodeSummary.

        集群中所有节点的个数。

        :param total_num: The total_num of this NodeSummary.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def ready_num(self):
        r"""Gets the ready_num of this NodeSummary.

        集群中已就绪节点的数量。

        :return: The ready_num of this NodeSummary.
        :rtype: int
        """
        return self._ready_num

    @ready_num.setter
    def ready_num(self, ready_num):
        r"""Sets the ready_num of this NodeSummary.

        集群中已就绪节点的数量。

        :param ready_num: The ready_num of this NodeSummary.
        :type ready_num: int
        """
        self._ready_num = ready_num

    def to_dict(self):
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
        if not isinstance(other, NodeSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
