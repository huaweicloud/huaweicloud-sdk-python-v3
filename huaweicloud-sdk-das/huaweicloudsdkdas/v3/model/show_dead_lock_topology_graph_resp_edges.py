# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockTopologyGraphRespEdges:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'target': 'str',
        'type': 'str'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target',
        'type': 'type'
    }

    def __init__(self, source=None, target=None, type=None):
        r"""ShowDeadLockTopologyGraphRespEdges

        The model defined in huaweicloud sdk

        :param source: 起始节点唯一标识
        :type source: str
        :param target: 终点节点唯一标识
        :type target: str
        :param type: 关系类型
        :type type: str
        """
        
        

        self._source = None
        self._target = None
        self._type = None
        self.discriminator = None

        self.source = source
        self.target = target
        self.type = type

    @property
    def source(self):
        r"""Gets the source of this ShowDeadLockTopologyGraphRespEdges.

        起始节点唯一标识

        :return: The source of this ShowDeadLockTopologyGraphRespEdges.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowDeadLockTopologyGraphRespEdges.

        起始节点唯一标识

        :param source: The source of this ShowDeadLockTopologyGraphRespEdges.
        :type source: str
        """
        self._source = source

    @property
    def target(self):
        r"""Gets the target of this ShowDeadLockTopologyGraphRespEdges.

        终点节点唯一标识

        :return: The target of this ShowDeadLockTopologyGraphRespEdges.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this ShowDeadLockTopologyGraphRespEdges.

        终点节点唯一标识

        :param target: The target of this ShowDeadLockTopologyGraphRespEdges.
        :type target: str
        """
        self._target = target

    @property
    def type(self):
        r"""Gets the type of this ShowDeadLockTopologyGraphRespEdges.

        关系类型

        :return: The type of this ShowDeadLockTopologyGraphRespEdges.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowDeadLockTopologyGraphRespEdges.

        关系类型

        :param type: The type of this ShowDeadLockTopologyGraphRespEdges.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowDeadLockTopologyGraphRespEdges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
