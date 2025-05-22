# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpecUpdateNodeNicSpecUpdatePrimaryNic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'subnet_list': 'list[str]'
    }

    attribute_map = {
        'subnet_id': 'subnetId',
        'subnet_list': 'subnetList'
    }

    def __init__(self, subnet_id=None, subnet_list=None):
        r"""NodeSpecUpdateNodeNicSpecUpdatePrimaryNic

        The model defined in huaweicloud sdk

        :param subnet_id: **参数解释**： 网卡所在子网的网络ID。 **约束限制**： 主网卡创建时若未指定subnetId,将使用集群子网。若节点池同时配置了subnetList，则节点池扩容子网以subnetList字段为准。扩展网卡创建时必须指定subnetId。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subnet_id: str
        :param subnet_list: **参数解释**： 网卡所在子网的网络ID列表，支持节点池配置多个子网。 **约束限制**： 最多支持配置20个子网。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subnet_list: list[str]
        """
        
        

        self._subnet_id = None
        self._subnet_list = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_list is not None:
            self.subnet_list = subnet_list

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.

        **参数解释**： 网卡所在子网的网络ID。 **约束限制**： 主网卡创建时若未指定subnetId,将使用集群子网。若节点池同时配置了subnetList，则节点池扩容子网以subnetList字段为准。扩展网卡创建时必须指定subnetId。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subnet_id of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.

        **参数解释**： 网卡所在子网的网络ID。 **约束限制**： 主网卡创建时若未指定subnetId,将使用集群子网。若节点池同时配置了subnetList，则节点池扩容子网以subnetList字段为准。扩展网卡创建时必须指定subnetId。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subnet_id: The subnet_id of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_list(self):
        r"""Gets the subnet_list of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.

        **参数解释**： 网卡所在子网的网络ID列表，支持节点池配置多个子网。 **约束限制**： 最多支持配置20个子网。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subnet_list of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.
        :rtype: list[str]
        """
        return self._subnet_list

    @subnet_list.setter
    def subnet_list(self, subnet_list):
        r"""Sets the subnet_list of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.

        **参数解释**： 网卡所在子网的网络ID列表，支持节点池配置多个子网。 **约束限制**： 最多支持配置20个子网。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subnet_list: The subnet_list of this NodeSpecUpdateNodeNicSpecUpdatePrimaryNic.
        :type subnet_list: list[str]
        """
        self._subnet_list = subnet_list

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
        if not isinstance(other, NodeSpecUpdateNodeNicSpecUpdatePrimaryNic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
