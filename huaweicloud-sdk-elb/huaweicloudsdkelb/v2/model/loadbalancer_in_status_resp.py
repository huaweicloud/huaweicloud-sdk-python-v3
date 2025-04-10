# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadbalancerInStatusResp:

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
        'id': 'str',
        'listeners': 'list[ListenersInStatusResp]',
        'pools': 'list[PoolsInStatusResp]',
        'operating_status': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'listeners': 'listeners',
        'pools': 'pools',
        'operating_status': 'operating_status',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, name=None, id=None, listeners=None, pools=None, operating_status=None, provisioning_status=None):
        r"""LoadbalancerInStatusResp

        The model defined in huaweicloud sdk

        :param name: 负载均衡器名称
        :type name: str
        :param id: 负载均衡器ID
        :type id: str
        :param listeners: 负载均衡器关联的监听器列表
        :type listeners: list[:class:`huaweicloudsdkelb.v2.ListenersInStatusResp`]
        :param pools: 负载均衡器关联的后端云服务器组列表
        :type pools: list[:class:`huaweicloudsdkelb.v2.PoolsInStatusResp`]
        :param operating_status: 负载均衡器的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。
        :type operating_status: str
        :param provisioning_status: 负载均衡器的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。
        :type provisioning_status: str
        """
        
        

        self._name = None
        self._id = None
        self._listeners = None
        self._pools = None
        self._operating_status = None
        self._provisioning_status = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.listeners = listeners
        self.pools = pools
        self.operating_status = operating_status
        self.provisioning_status = provisioning_status

    @property
    def name(self):
        r"""Gets the name of this LoadbalancerInStatusResp.

        负载均衡器名称

        :return: The name of this LoadbalancerInStatusResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LoadbalancerInStatusResp.

        负载均衡器名称

        :param name: The name of this LoadbalancerInStatusResp.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this LoadbalancerInStatusResp.

        负载均衡器ID

        :return: The id of this LoadbalancerInStatusResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LoadbalancerInStatusResp.

        负载均衡器ID

        :param id: The id of this LoadbalancerInStatusResp.
        :type id: str
        """
        self._id = id

    @property
    def listeners(self):
        r"""Gets the listeners of this LoadbalancerInStatusResp.

        负载均衡器关联的监听器列表

        :return: The listeners of this LoadbalancerInStatusResp.
        :rtype: list[:class:`huaweicloudsdkelb.v2.ListenersInStatusResp`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this LoadbalancerInStatusResp.

        负载均衡器关联的监听器列表

        :param listeners: The listeners of this LoadbalancerInStatusResp.
        :type listeners: list[:class:`huaweicloudsdkelb.v2.ListenersInStatusResp`]
        """
        self._listeners = listeners

    @property
    def pools(self):
        r"""Gets the pools of this LoadbalancerInStatusResp.

        负载均衡器关联的后端云服务器组列表

        :return: The pools of this LoadbalancerInStatusResp.
        :rtype: list[:class:`huaweicloudsdkelb.v2.PoolsInStatusResp`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        r"""Sets the pools of this LoadbalancerInStatusResp.

        负载均衡器关联的后端云服务器组列表

        :param pools: The pools of this LoadbalancerInStatusResp.
        :type pools: list[:class:`huaweicloudsdkelb.v2.PoolsInStatusResp`]
        """
        self._pools = pools

    @property
    def operating_status(self):
        r"""Gets the operating_status of this LoadbalancerInStatusResp.

        负载均衡器的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。

        :return: The operating_status of this LoadbalancerInStatusResp.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this LoadbalancerInStatusResp.

        负载均衡器的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。

        :param operating_status: The operating_status of this LoadbalancerInStatusResp.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this LoadbalancerInStatusResp.

        负载均衡器的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this LoadbalancerInStatusResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this LoadbalancerInStatusResp.

        负载均衡器的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this LoadbalancerInStatusResp.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, LoadbalancerInStatusResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
