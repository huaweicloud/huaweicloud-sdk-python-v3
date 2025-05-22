# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeManagement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group_reference': 'str'
    }

    attribute_map = {
        'server_group_reference': 'serverGroupReference'
    }

    def __init__(self, server_group_reference=None):
        r"""NodeManagement

        The model defined in huaweicloud sdk

        :param server_group_reference: **参数解释**： 云服务器组ID，指定后将绑定云服务器组，节点池中所有节点将创建在该云服务器组下。绑定云服务器组后节点池中的节点数量不允许超出云服务器组可添加的云服务器数量，否则将导致节点池无法扩容。 &gt; - 绑定云服务器组后，云服务器将严格按照亲和策略分布，同时也会限制节点池中节点个数上限。由于ECS创建云服务器时本身具有一定反亲和能力，如果仅需云服务器分散的创建在不同主机上以提高业务的可靠性，又不希望节点个数受到云服务器组的限制，请勿绑定云服务器组。 &gt; - 云服务组支持解绑，解绑后存量节点仍属于原云服务器组，新建节点将不再绑定云服务器组。 当节点池中不存在节点时支持绑定新的云服务器组或者切换绑定的云服务器组  **约束限制**： 指定云服务器组时节点池中的节点数量不允许超出云服务器组的配额限制。 **取值范围**： - 不指定或者指定空字符串：表示解绑云服务器组 - 云服务器组ID：表示切换节点池绑定的云服务组  **默认取值**： 不涉及
        :type server_group_reference: str
        """
        
        

        self._server_group_reference = None
        self.discriminator = None

        if server_group_reference is not None:
            self.server_group_reference = server_group_reference

    @property
    def server_group_reference(self):
        r"""Gets the server_group_reference of this NodeManagement.

        **参数解释**： 云服务器组ID，指定后将绑定云服务器组，节点池中所有节点将创建在该云服务器组下。绑定云服务器组后节点池中的节点数量不允许超出云服务器组可添加的云服务器数量，否则将导致节点池无法扩容。 > - 绑定云服务器组后，云服务器将严格按照亲和策略分布，同时也会限制节点池中节点个数上限。由于ECS创建云服务器时本身具有一定反亲和能力，如果仅需云服务器分散的创建在不同主机上以提高业务的可靠性，又不希望节点个数受到云服务器组的限制，请勿绑定云服务器组。 > - 云服务组支持解绑，解绑后存量节点仍属于原云服务器组，新建节点将不再绑定云服务器组。 当节点池中不存在节点时支持绑定新的云服务器组或者切换绑定的云服务器组  **约束限制**： 指定云服务器组时节点池中的节点数量不允许超出云服务器组的配额限制。 **取值范围**： - 不指定或者指定空字符串：表示解绑云服务器组 - 云服务器组ID：表示切换节点池绑定的云服务组  **默认取值**： 不涉及

        :return: The server_group_reference of this NodeManagement.
        :rtype: str
        """
        return self._server_group_reference

    @server_group_reference.setter
    def server_group_reference(self, server_group_reference):
        r"""Sets the server_group_reference of this NodeManagement.

        **参数解释**： 云服务器组ID，指定后将绑定云服务器组，节点池中所有节点将创建在该云服务器组下。绑定云服务器组后节点池中的节点数量不允许超出云服务器组可添加的云服务器数量，否则将导致节点池无法扩容。 > - 绑定云服务器组后，云服务器将严格按照亲和策略分布，同时也会限制节点池中节点个数上限。由于ECS创建云服务器时本身具有一定反亲和能力，如果仅需云服务器分散的创建在不同主机上以提高业务的可靠性，又不希望节点个数受到云服务器组的限制，请勿绑定云服务器组。 > - 云服务组支持解绑，解绑后存量节点仍属于原云服务器组，新建节点将不再绑定云服务器组。 当节点池中不存在节点时支持绑定新的云服务器组或者切换绑定的云服务器组  **约束限制**： 指定云服务器组时节点池中的节点数量不允许超出云服务器组的配额限制。 **取值范围**： - 不指定或者指定空字符串：表示解绑云服务器组 - 云服务器组ID：表示切换节点池绑定的云服务组  **默认取值**： 不涉及

        :param server_group_reference: The server_group_reference of this NodeManagement.
        :type server_group_reference: str
        """
        self._server_group_reference = server_group_reference

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
        if not isinstance(other, NodeManagement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
