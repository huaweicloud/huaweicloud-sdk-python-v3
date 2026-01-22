# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateNetworkSegmentVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_id': 'str',
        'protect_network': 'str',
        'az_info': 'str',
        'subnet_name': 'str'
    }

    attribute_map = {
        'conf_id': 'conf_id',
        'protect_network': 'protect_network',
        'az_info': 'az_info',
        'subnet_name': 'subnet_name'
    }

    def __init__(self, conf_id=None, protect_network=None, az_info=None, subnet_name=None):
        r"""PrivateNetworkSegmentVO

        The model defined in huaweicloud sdk

        :param conf_id: **参数解释**： 私网网段ID，更新私网网段时需要 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type conf_id: str
        :param protect_network: **参数解释**： 私网网段，格式为：IP/Mask **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type protect_network: str
        :param az_info: **参数解释**： 私网网段的可用区信息，如AZ1 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type az_info: str
        :param subnet_name: **参数解释**： 子网名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type subnet_name: str
        """
        
        

        self._conf_id = None
        self._protect_network = None
        self._az_info = None
        self._subnet_name = None
        self.discriminator = None

        if conf_id is not None:
            self.conf_id = conf_id
        self.protect_network = protect_network
        if az_info is not None:
            self.az_info = az_info
        if subnet_name is not None:
            self.subnet_name = subnet_name

    @property
    def conf_id(self):
        r"""Gets the conf_id of this PrivateNetworkSegmentVO.

        **参数解释**： 私网网段ID，更新私网网段时需要 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The conf_id of this PrivateNetworkSegmentVO.
        :rtype: str
        """
        return self._conf_id

    @conf_id.setter
    def conf_id(self, conf_id):
        r"""Sets the conf_id of this PrivateNetworkSegmentVO.

        **参数解释**： 私网网段ID，更新私网网段时需要 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param conf_id: The conf_id of this PrivateNetworkSegmentVO.
        :type conf_id: str
        """
        self._conf_id = conf_id

    @property
    def protect_network(self):
        r"""Gets the protect_network of this PrivateNetworkSegmentVO.

        **参数解释**： 私网网段，格式为：IP/Mask **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The protect_network of this PrivateNetworkSegmentVO.
        :rtype: str
        """
        return self._protect_network

    @protect_network.setter
    def protect_network(self, protect_network):
        r"""Sets the protect_network of this PrivateNetworkSegmentVO.

        **参数解释**： 私网网段，格式为：IP/Mask **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param protect_network: The protect_network of this PrivateNetworkSegmentVO.
        :type protect_network: str
        """
        self._protect_network = protect_network

    @property
    def az_info(self):
        r"""Gets the az_info of this PrivateNetworkSegmentVO.

        **参数解释**： 私网网段的可用区信息，如AZ1 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The az_info of this PrivateNetworkSegmentVO.
        :rtype: str
        """
        return self._az_info

    @az_info.setter
    def az_info(self, az_info):
        r"""Sets the az_info of this PrivateNetworkSegmentVO.

        **参数解释**： 私网网段的可用区信息，如AZ1 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param az_info: The az_info of this PrivateNetworkSegmentVO.
        :type az_info: str
        """
        self._az_info = az_info

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this PrivateNetworkSegmentVO.

        **参数解释**： 子网名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The subnet_name of this PrivateNetworkSegmentVO.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this PrivateNetworkSegmentVO.

        **参数解释**： 子网名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param subnet_name: The subnet_name of this PrivateNetworkSegmentVO.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

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
        if not isinstance(other, PrivateNetworkSegmentVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
