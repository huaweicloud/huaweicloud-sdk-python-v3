# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerStatusPool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provisioning_status': 'str',
        'name': 'str',
        'healthmonitor': 'LoadBalancerStatusHealthMonitor',
        'members': 'list[LoadBalancerStatusMember]',
        'id': 'str',
        'operating_status': 'str'
    }

    attribute_map = {
        'provisioning_status': 'provisioning_status',
        'name': 'name',
        'healthmonitor': 'healthmonitor',
        'members': 'members',
        'id': 'id',
        'operating_status': 'operating_status'
    }

    def __init__(self, provisioning_status=None, name=None, healthmonitor=None, members=None, id=None, operating_status=None):
        """LoadBalancerStatusPool

        The model defined in huaweicloud sdk

        :param provisioning_status: 后端服务器组的配置状态。  取值： - ACTIVE：使用中。
        :type provisioning_status: str
        :param name: 后端服务器组名。
        :type name: str
        :param healthmonitor: 
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.LoadBalancerStatusHealthMonitor`
        :param members: 后端服务器状态信息。
        :type members: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusMember`]
        :param id: 后端服务器组ID。
        :type id: str
        :param operating_status: 后端服务器组的操作状态。  取值： - ONLINE：创建时默认状态，表后端服务器组正常。 - DEGRADED：该后端服务器组下存在member为的operating_status&#x3D;OFFLINE。 - DISABLED：负载均衡器或后端服务器组的admin_state_up&#x3D;false。  说明： DEGRADED和DISABLED仅在当前接口返回， 查询后端服务器组详情等其他接口返回的operating_status字段不存在这两个状态值。
        :type operating_status: str
        """
        
        

        self._provisioning_status = None
        self._name = None
        self._healthmonitor = None
        self._members = None
        self._id = None
        self._operating_status = None
        self.discriminator = None

        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if name is not None:
            self.name = name
        if healthmonitor is not None:
            self.healthmonitor = healthmonitor
        if members is not None:
            self.members = members
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusPool.

        后端服务器组的配置状态。  取值： - ACTIVE：使用中。

        :return: The provisioning_status of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusPool.

        后端服务器组的配置状态。  取值： - ACTIVE：使用中。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusPool.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def name(self):
        """Gets the name of this LoadBalancerStatusPool.

        后端服务器组名。

        :return: The name of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerStatusPool.

        后端服务器组名。

        :param name: The name of this LoadBalancerStatusPool.
        :type name: str
        """
        self._name = name

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this LoadBalancerStatusPool.

        :return: The healthmonitor of this LoadBalancerStatusPool.
        :rtype: :class:`huaweicloudsdkelb.v3.LoadBalancerStatusHealthMonitor`
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this LoadBalancerStatusPool.

        :param healthmonitor: The healthmonitor of this LoadBalancerStatusPool.
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.LoadBalancerStatusHealthMonitor`
        """
        self._healthmonitor = healthmonitor

    @property
    def members(self):
        """Gets the members of this LoadBalancerStatusPool.

        后端服务器状态信息。

        :return: The members of this LoadBalancerStatusPool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusMember`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this LoadBalancerStatusPool.

        后端服务器状态信息。

        :param members: The members of this LoadBalancerStatusPool.
        :type members: list[:class:`huaweicloudsdkelb.v3.LoadBalancerStatusMember`]
        """
        self._members = members

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusPool.

        后端服务器组ID。

        :return: The id of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusPool.

        后端服务器组ID。

        :param id: The id of this LoadBalancerStatusPool.
        :type id: str
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancerStatusPool.

        后端服务器组的操作状态。  取值： - ONLINE：创建时默认状态，表后端服务器组正常。 - DEGRADED：该后端服务器组下存在member为的operating_status=OFFLINE。 - DISABLED：负载均衡器或后端服务器组的admin_state_up=false。  说明： DEGRADED和DISABLED仅在当前接口返回， 查询后端服务器组详情等其他接口返回的operating_status字段不存在这两个状态值。

        :return: The operating_status of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancerStatusPool.

        后端服务器组的操作状态。  取值： - ONLINE：创建时默认状态，表后端服务器组正常。 - DEGRADED：该后端服务器组下存在member为的operating_status=OFFLINE。 - DISABLED：负载均衡器或后端服务器组的admin_state_up=false。  说明： DEGRADED和DISABLED仅在当前接口返回， 查询后端服务器组详情等其他接口返回的operating_status字段不存在这两个状态值。

        :param operating_status: The operating_status of this LoadBalancerStatusPool.
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
        if not isinstance(other, LoadBalancerStatusPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
