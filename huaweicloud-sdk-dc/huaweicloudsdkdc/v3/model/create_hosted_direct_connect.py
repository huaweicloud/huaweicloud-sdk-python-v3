# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHostedDirectConnect:

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
        'description': 'str',
        'bandwidth': 'int',
        'hosting_id': 'str',
        'vlan': 'int',
        'resource_tenant_id': 'str',
        'peer_location': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'bandwidth': 'bandwidth',
        'hosting_id': 'hosting_id',
        'vlan': 'vlan',
        'resource_tenant_id': 'resource_tenant_id',
        'peer_location': 'peer_location'
    }

    def __init__(self, name=None, description=None, bandwidth=None, hosting_id=None, vlan=None, resource_tenant_id=None, peer_location=None):
        """CreateHostedDirectConnect

        The model defined in huaweicloud sdk

        :param name: 托管物理专线的名字。
        :type name: str
        :param description: 托管专线的描述信息
        :type description: str
        :param bandwidth: 指定托管专线接入带宽,单位Mbps
        :type bandwidth: int
        :param hosting_id: hosted物理专线对应的hosting物理专线的ID
        :type hosting_id: str
        :param vlan: 指定托管(hosted)专线预分配的vlan
        :type vlan: int
        :param resource_tenant_id: 为其他租户创建托管专线，指定对应的租户ID
        :type resource_tenant_id: str
        :param peer_location: 物理专线对端所在的物理位置，省/市/街道或IDC名字。
        :type peer_location: str
        """
        
        

        self._name = None
        self._description = None
        self._bandwidth = None
        self._hosting_id = None
        self._vlan = None
        self._resource_tenant_id = None
        self._peer_location = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bandwidth is not None:
            self.bandwidth = bandwidth
        self.hosting_id = hosting_id
        self.vlan = vlan
        self.resource_tenant_id = resource_tenant_id
        if peer_location is not None:
            self.peer_location = peer_location

    @property
    def name(self):
        """Gets the name of this CreateHostedDirectConnect.

        托管物理专线的名字。

        :return: The name of this CreateHostedDirectConnect.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHostedDirectConnect.

        托管物理专线的名字。

        :param name: The name of this CreateHostedDirectConnect.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateHostedDirectConnect.

        托管专线的描述信息

        :return: The description of this CreateHostedDirectConnect.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateHostedDirectConnect.

        托管专线的描述信息

        :param description: The description of this CreateHostedDirectConnect.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateHostedDirectConnect.

        指定托管专线接入带宽,单位Mbps

        :return: The bandwidth of this CreateHostedDirectConnect.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateHostedDirectConnect.

        指定托管专线接入带宽,单位Mbps

        :param bandwidth: The bandwidth of this CreateHostedDirectConnect.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def hosting_id(self):
        """Gets the hosting_id of this CreateHostedDirectConnect.

        hosted物理专线对应的hosting物理专线的ID

        :return: The hosting_id of this CreateHostedDirectConnect.
        :rtype: str
        """
        return self._hosting_id

    @hosting_id.setter
    def hosting_id(self, hosting_id):
        """Sets the hosting_id of this CreateHostedDirectConnect.

        hosted物理专线对应的hosting物理专线的ID

        :param hosting_id: The hosting_id of this CreateHostedDirectConnect.
        :type hosting_id: str
        """
        self._hosting_id = hosting_id

    @property
    def vlan(self):
        """Gets the vlan of this CreateHostedDirectConnect.

        指定托管(hosted)专线预分配的vlan

        :return: The vlan of this CreateHostedDirectConnect.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this CreateHostedDirectConnect.

        指定托管(hosted)专线预分配的vlan

        :param vlan: The vlan of this CreateHostedDirectConnect.
        :type vlan: int
        """
        self._vlan = vlan

    @property
    def resource_tenant_id(self):
        """Gets the resource_tenant_id of this CreateHostedDirectConnect.

        为其他租户创建托管专线，指定对应的租户ID

        :return: The resource_tenant_id of this CreateHostedDirectConnect.
        :rtype: str
        """
        return self._resource_tenant_id

    @resource_tenant_id.setter
    def resource_tenant_id(self, resource_tenant_id):
        """Sets the resource_tenant_id of this CreateHostedDirectConnect.

        为其他租户创建托管专线，指定对应的租户ID

        :param resource_tenant_id: The resource_tenant_id of this CreateHostedDirectConnect.
        :type resource_tenant_id: str
        """
        self._resource_tenant_id = resource_tenant_id

    @property
    def peer_location(self):
        """Gets the peer_location of this CreateHostedDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字。

        :return: The peer_location of this CreateHostedDirectConnect.
        :rtype: str
        """
        return self._peer_location

    @peer_location.setter
    def peer_location(self, peer_location):
        """Sets the peer_location of this CreateHostedDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字。

        :param peer_location: The peer_location of this CreateHostedDirectConnect.
        :type peer_location: str
        """
        self._peer_location = peer_location

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
        if not isinstance(other, CreateHostedDirectConnect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
