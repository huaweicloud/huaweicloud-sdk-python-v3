# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLoadBalancerCascadeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unbounded_pool': 'bool',
        'public_ip': 'bool'
    }

    attribute_map = {
        'unbounded_pool': 'unbounded_pool',
        'public_ip': 'public_ip'
    }

    def __init__(self, unbounded_pool=None, public_ip=None):
        r"""DeleteLoadBalancerCascadeOption

        The model defined in huaweicloud sdk

        :param unbounded_pool: **参数解释**：是否删除关联的后端服务器组。  **约束限制**： - 共享型负载均衡器仅支持传参为true。 [- 若开启多挂特性，且后端服务器组关联了多个LB，则无论传入何值，都不会删除后端服务器组。](tag: hws,hws_hk)  **取值范围**： - true：删除该后端服务器组。 - false：仅解绑后端服务器组，不删除。  **默认取值**：true
        :type unbounded_pool: bool
        :param public_ip: **参数解释**：删除负载均衡器后是否删除关联的公网IP。  **约束限制**：不涉及          **取值范围**： - true：删除关联的EIP。 - false：仅解绑关联的EIP，不删除。  **默认取值**：false
        :type public_ip: bool
        """
        
        

        self._unbounded_pool = None
        self._public_ip = None
        self.discriminator = None

        if unbounded_pool is not None:
            self.unbounded_pool = unbounded_pool
        if public_ip is not None:
            self.public_ip = public_ip

    @property
    def unbounded_pool(self):
        r"""Gets the unbounded_pool of this DeleteLoadBalancerCascadeOption.

        **参数解释**：是否删除关联的后端服务器组。  **约束限制**： - 共享型负载均衡器仅支持传参为true。 [- 若开启多挂特性，且后端服务器组关联了多个LB，则无论传入何值，都不会删除后端服务器组。](tag: hws,hws_hk)  **取值范围**： - true：删除该后端服务器组。 - false：仅解绑后端服务器组，不删除。  **默认取值**：true

        :return: The unbounded_pool of this DeleteLoadBalancerCascadeOption.
        :rtype: bool
        """
        return self._unbounded_pool

    @unbounded_pool.setter
    def unbounded_pool(self, unbounded_pool):
        r"""Sets the unbounded_pool of this DeleteLoadBalancerCascadeOption.

        **参数解释**：是否删除关联的后端服务器组。  **约束限制**： - 共享型负载均衡器仅支持传参为true。 [- 若开启多挂特性，且后端服务器组关联了多个LB，则无论传入何值，都不会删除后端服务器组。](tag: hws,hws_hk)  **取值范围**： - true：删除该后端服务器组。 - false：仅解绑后端服务器组，不删除。  **默认取值**：true

        :param unbounded_pool: The unbounded_pool of this DeleteLoadBalancerCascadeOption.
        :type unbounded_pool: bool
        """
        self._unbounded_pool = unbounded_pool

    @property
    def public_ip(self):
        r"""Gets the public_ip of this DeleteLoadBalancerCascadeOption.

        **参数解释**：删除负载均衡器后是否删除关联的公网IP。  **约束限制**：不涉及          **取值范围**： - true：删除关联的EIP。 - false：仅解绑关联的EIP，不删除。  **默认取值**：false

        :return: The public_ip of this DeleteLoadBalancerCascadeOption.
        :rtype: bool
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this DeleteLoadBalancerCascadeOption.

        **参数解释**：删除负载均衡器后是否删除关联的公网IP。  **约束限制**：不涉及          **取值范围**： - true：删除关联的EIP。 - false：仅解绑关联的EIP，不删除。  **默认取值**：false

        :param public_ip: The public_ip of this DeleteLoadBalancerCascadeOption.
        :type public_ip: bool
        """
        self._public_ip = public_ip

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
        if not isinstance(other, DeleteLoadBalancerCascadeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
