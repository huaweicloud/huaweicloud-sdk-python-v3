# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'instance_info': 'InstanceInfoForRisk',
        'values': 'list[float]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'instance_info': 'instance_info',
        'values': 'values'
    }

    def __init__(self, node_id=None, instance_info=None, values=None):
        r"""RiskInfo

        The model defined in huaweicloud sdk

        :param node_id: 节点ID
        :type node_id: str
        :param instance_info: 
        :type instance_info: :class:`huaweicloudsdkdas.v3.InstanceInfoForRisk`
        :param values: 指标值
        :type values: list[float]
        """
        
        

        self._node_id = None
        self._instance_info = None
        self._values = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if instance_info is not None:
            self.instance_info = instance_info
        if values is not None:
            self.values = values

    @property
    def node_id(self):
        r"""Gets the node_id of this RiskInfo.

        节点ID

        :return: The node_id of this RiskInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this RiskInfo.

        节点ID

        :param node_id: The node_id of this RiskInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def instance_info(self):
        r"""Gets the instance_info of this RiskInfo.

        :return: The instance_info of this RiskInfo.
        :rtype: :class:`huaweicloudsdkdas.v3.InstanceInfoForRisk`
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        r"""Sets the instance_info of this RiskInfo.

        :param instance_info: The instance_info of this RiskInfo.
        :type instance_info: :class:`huaweicloudsdkdas.v3.InstanceInfoForRisk`
        """
        self._instance_info = instance_info

    @property
    def values(self):
        r"""Gets the values of this RiskInfo.

        指标值

        :return: The values of this RiskInfo.
        :rtype: list[float]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this RiskInfo.

        指标值

        :param values: The values of this RiskInfo.
        :type values: list[float]
        """
        self._values = values

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
        if not isinstance(other, RiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
