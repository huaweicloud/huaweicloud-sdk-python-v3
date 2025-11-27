# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replicas': 'int',
        'strategy': 'NodeUpgradeStrategy'
    }

    attribute_map = {
        'replicas': 'replicas',
        'strategy': 'strategy'
    }

    def __init__(self, replicas=None, strategy=None):
        r"""WorkerConfig

        The model defined in huaweicloud sdk

        :param replicas: 节点个数
        :type replicas: int
        :param strategy: 
        :type strategy: :class:`huaweicloudsdkucs.v1.NodeUpgradeStrategy`
        """
        
        

        self._replicas = None
        self._strategy = None
        self.discriminator = None

        if replicas is not None:
            self.replicas = replicas
        if strategy is not None:
            self.strategy = strategy

    @property
    def replicas(self):
        r"""Gets the replicas of this WorkerConfig.

        节点个数

        :return: The replicas of this WorkerConfig.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        r"""Sets the replicas of this WorkerConfig.

        节点个数

        :param replicas: The replicas of this WorkerConfig.
        :type replicas: int
        """
        self._replicas = replicas

    @property
    def strategy(self):
        r"""Gets the strategy of this WorkerConfig.

        :return: The strategy of this WorkerConfig.
        :rtype: :class:`huaweicloudsdkucs.v1.NodeUpgradeStrategy`
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this WorkerConfig.

        :param strategy: The strategy of this WorkerConfig.
        :type strategy: :class:`huaweicloudsdkucs.v1.NodeUpgradeStrategy`
        """
        self._strategy = strategy

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
        if not isinstance(other, WorkerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
