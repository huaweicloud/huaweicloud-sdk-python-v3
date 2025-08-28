# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'provisioning_status': 'str',
        'listeners': 'list[LoadBalancerStatusListener]',
        'pools': 'list[LoadBalancerStatusPool]',
        'id': 'str',
        'operating_status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'provisioning_status': 'provisioning_status',
        'listeners': 'listeners',
        'pools': 'pools',
        'id': 'id',
        'operating_status': 'operating_status'
    }

    def __init__(self, name=None, provisioning_status=None, listeners=None, pools=None, id=None, operating_status=None):
        r"""LoadBalancerStatus

        The model defined in huaweicloud sdk

        :param name: **参数解释**：负载均衡器名称。  **取值范围**：不涉及
        :type name: str
        :param provisioning_status: **参数解释**：负载均衡器的配置状态。  **取值范围**： - ACTIVE：使用中。 - PENDING_DELETE：删除中。
        :type provisioning_status: str
        :param listeners: **参数解释**：负载均衡器关联的所有监听器的状态信息。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusListener`]
        :param pools: **参数解释**：负载均衡器关联的所有后端服务器组的状态信息。
        :type pools: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusPool`]
        :param id: **参数解释**：负载均衡器ID。  **取值范围**：不涉及
        :type id: str
        :param operating_status: **参数解释**：负载均衡器的操作状态。  **取值范围**： - ONLINE：创建时默认状态，表示负载均衡器正常运行。 - FROZEN：已冻结。 - DEGRADED：负载均衡器下存在member的operating_status为OFFLINE时返回这个状态。 - DISABLED：负载均衡器的admin_state_up属性值为false。  &gt; DEGRADED和DISABLED状态仅在当前接口中返回，查询负载均衡器详情等其他接口不会返回这两个状态值。
        :type operating_status: str
        """
        
        

        self._name = None
        self._provisioning_status = None
        self._listeners = None
        self._pools = None
        self._id = None
        self._operating_status = None
        self.discriminator = None

        self.name = name
        self.provisioning_status = provisioning_status
        self.listeners = listeners
        self.pools = pools
        self.id = id
        self.operating_status = operating_status

    @property
    def name(self):
        r"""Gets the name of this LoadBalancerStatus.

        **参数解释**：负载均衡器名称。  **取值范围**：不涉及

        :return: The name of this LoadBalancerStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LoadBalancerStatus.

        **参数解释**：负载均衡器名称。  **取值范围**：不涉及

        :param name: The name of this LoadBalancerStatus.
        :type name: str
        """
        self._name = name

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this LoadBalancerStatus.

        **参数解释**：负载均衡器的配置状态。  **取值范围**： - ACTIVE：使用中。 - PENDING_DELETE：删除中。

        :return: The provisioning_status of this LoadBalancerStatus.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this LoadBalancerStatus.

        **参数解释**：负载均衡器的配置状态。  **取值范围**： - ACTIVE：使用中。 - PENDING_DELETE：删除中。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatus.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def listeners(self):
        r"""Gets the listeners of this LoadBalancerStatus.

        **参数解释**：负载均衡器关联的所有监听器的状态信息。

        :return: The listeners of this LoadBalancerStatus.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusListener`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this LoadBalancerStatus.

        **参数解释**：负载均衡器关联的所有监听器的状态信息。

        :param listeners: The listeners of this LoadBalancerStatus.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusListener`]
        """
        self._listeners = listeners

    @property
    def pools(self):
        r"""Gets the pools of this LoadBalancerStatus.

        **参数解释**：负载均衡器关联的所有后端服务器组的状态信息。

        :return: The pools of this LoadBalancerStatus.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusPool`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        r"""Sets the pools of this LoadBalancerStatus.

        **参数解释**：负载均衡器关联的所有后端服务器组的状态信息。

        :param pools: The pools of this LoadBalancerStatus.
        :type pools: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusPool`]
        """
        self._pools = pools

    @property
    def id(self):
        r"""Gets the id of this LoadBalancerStatus.

        **参数解释**：负载均衡器ID。  **取值范围**：不涉及

        :return: The id of this LoadBalancerStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LoadBalancerStatus.

        **参数解释**：负载均衡器ID。  **取值范围**：不涉及

        :param id: The id of this LoadBalancerStatus.
        :type id: str
        """
        self._id = id

    @property
    def operating_status(self):
        r"""Gets the operating_status of this LoadBalancerStatus.

        **参数解释**：负载均衡器的操作状态。  **取值范围**： - ONLINE：创建时默认状态，表示负载均衡器正常运行。 - FROZEN：已冻结。 - DEGRADED：负载均衡器下存在member的operating_status为OFFLINE时返回这个状态。 - DISABLED：负载均衡器的admin_state_up属性值为false。  > DEGRADED和DISABLED状态仅在当前接口中返回，查询负载均衡器详情等其他接口不会返回这两个状态值。

        :return: The operating_status of this LoadBalancerStatus.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this LoadBalancerStatus.

        **参数解释**：负载均衡器的操作状态。  **取值范围**： - ONLINE：创建时默认状态，表示负载均衡器正常运行。 - FROZEN：已冻结。 - DEGRADED：负载均衡器下存在member的operating_status为OFFLINE时返回这个状态。 - DISABLED：负载均衡器的admin_state_up属性值为false。  > DEGRADED和DISABLED状态仅在当前接口中返回，查询负载均衡器详情等其他接口不会返回这两个状态值。

        :param operating_status: The operating_status of this LoadBalancerStatus.
        :type operating_status: str
        """
        self._operating_status = operating_status

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
        if not isinstance(other, LoadBalancerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
