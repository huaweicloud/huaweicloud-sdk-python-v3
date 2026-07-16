# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCoreIngressNetworkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ingress_id': 'str',
        'vpc_ingress_network_id': 'str'
    }

    attribute_map = {
        'ingress_id': 'ingress_id',
        'vpc_ingress_network_id': 'vpc_ingress_network_id'
    }

    def __init__(self, ingress_id=None, vpc_ingress_network_id=None):
        r"""ShowCoreIngressNetworkRequest

        The model defined in huaweicloud sdk

        :param ingress_id: Ingress ID，用于唯一标识一个Ingress实例。
        :type ingress_id: str
        :param vpc_ingress_network_id: **参数解释**： 入站网络ID，用于唯一标识一个VPC入站网络实例。 **取值范围**： 匹配标准的UUID格式。
        :type vpc_ingress_network_id: str
        """
        
        

        self._ingress_id = None
        self._vpc_ingress_network_id = None
        self.discriminator = None

        self.ingress_id = ingress_id
        self.vpc_ingress_network_id = vpc_ingress_network_id

    @property
    def ingress_id(self):
        r"""Gets the ingress_id of this ShowCoreIngressNetworkRequest.

        Ingress ID，用于唯一标识一个Ingress实例。

        :return: The ingress_id of this ShowCoreIngressNetworkRequest.
        :rtype: str
        """
        return self._ingress_id

    @ingress_id.setter
    def ingress_id(self, ingress_id):
        r"""Sets the ingress_id of this ShowCoreIngressNetworkRequest.

        Ingress ID，用于唯一标识一个Ingress实例。

        :param ingress_id: The ingress_id of this ShowCoreIngressNetworkRequest.
        :type ingress_id: str
        """
        self._ingress_id = ingress_id

    @property
    def vpc_ingress_network_id(self):
        r"""Gets the vpc_ingress_network_id of this ShowCoreIngressNetworkRequest.

        **参数解释**： 入站网络ID，用于唯一标识一个VPC入站网络实例。 **取值范围**： 匹配标准的UUID格式。

        :return: The vpc_ingress_network_id of this ShowCoreIngressNetworkRequest.
        :rtype: str
        """
        return self._vpc_ingress_network_id

    @vpc_ingress_network_id.setter
    def vpc_ingress_network_id(self, vpc_ingress_network_id):
        r"""Sets the vpc_ingress_network_id of this ShowCoreIngressNetworkRequest.

        **参数解释**： 入站网络ID，用于唯一标识一个VPC入站网络实例。 **取值范围**： 匹配标准的UUID格式。

        :param vpc_ingress_network_id: The vpc_ingress_network_id of this ShowCoreIngressNetworkRequest.
        :type vpc_ingress_network_id: str
        """
        self._vpc_ingress_network_id = vpc_ingress_network_id

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
        if not isinstance(other, ShowCoreIngressNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
