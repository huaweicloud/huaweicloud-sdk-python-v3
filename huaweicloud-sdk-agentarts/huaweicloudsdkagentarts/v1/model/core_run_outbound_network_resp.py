# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunOutboundNetworkResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_mode': 'str',
        'vpc_config': 'CoreRunVpcConfigResp'
    }

    attribute_map = {
        'network_mode': 'network_mode',
        'vpc_config': 'vpc_config'
    }

    def __init__(self, network_mode=None, vpc_config=None):
        r"""CoreRunOutboundNetworkResp

        The model defined in huaweicloud sdk

        :param network_mode: **参数解释**: 出站网络类型。 **取值范围**: - PUBLIC: 表示公网出口。 - VPC: 表示虚拟私有云出口。 
        :type network_mode: str
        :param vpc_config: 
        :type vpc_config: :class:`huaweicloudsdkagentarts.v1.CoreRunVpcConfigResp`
        """
        
        

        self._network_mode = None
        self._vpc_config = None
        self.discriminator = None

        self.network_mode = network_mode
        if vpc_config is not None:
            self.vpc_config = vpc_config

    @property
    def network_mode(self):
        r"""Gets the network_mode of this CoreRunOutboundNetworkResp.

        **参数解释**: 出站网络类型。 **取值范围**: - PUBLIC: 表示公网出口。 - VPC: 表示虚拟私有云出口。 

        :return: The network_mode of this CoreRunOutboundNetworkResp.
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        r"""Sets the network_mode of this CoreRunOutboundNetworkResp.

        **参数解释**: 出站网络类型。 **取值范围**: - PUBLIC: 表示公网出口。 - VPC: 表示虚拟私有云出口。 

        :param network_mode: The network_mode of this CoreRunOutboundNetworkResp.
        :type network_mode: str
        """
        self._network_mode = network_mode

    @property
    def vpc_config(self):
        r"""Gets the vpc_config of this CoreRunOutboundNetworkResp.

        :return: The vpc_config of this CoreRunOutboundNetworkResp.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunVpcConfigResp`
        """
        return self._vpc_config

    @vpc_config.setter
    def vpc_config(self, vpc_config):
        r"""Sets the vpc_config of this CoreRunOutboundNetworkResp.

        :param vpc_config: The vpc_config of this CoreRunOutboundNetworkResp.
        :type vpc_config: :class:`huaweicloudsdkagentarts.v1.CoreRunVpcConfigResp`
        """
        self._vpc_config = vpc_config

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
        if not isinstance(other, CoreRunOutboundNetworkResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
