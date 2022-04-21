# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListFirewallGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'ingress_firewall_policy_id': 'str',
        'egress_firewall_policy_id': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'ingress_firewall_policy_id': 'ingress_firewall_policy_id',
        'egress_firewall_policy_id': 'egress_firewall_policy_id'
    }

    def __init__(self, marker=None, limit=None, id=None, name=None, description=None, ingress_firewall_policy_id=None, egress_firewall_policy_id=None):
        """NeutronListFirewallGroupsRequest

        The model defined in huaweicloud sdk

        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param limit: 每页返回的个数
        :type limit: int
        :param id: 使用id过滤网络ACL组
        :type id: list[str]
        :param name: 使用name过滤ACL组
        :type name: list[str]
        :param description: 使用description过滤ACL组
        :type description: list[str]
        :param ingress_firewall_policy_id: 使用入方向的网络ACL策略ID过滤网络ACL组
        :type ingress_firewall_policy_id: str
        :param egress_firewall_policy_id: 使用出方向的网络ACL策略过滤查询网络ACL组
        :type egress_firewall_policy_id: str
        """
        
        

        self._marker = None
        self._limit = None
        self._id = None
        self._name = None
        self._description = None
        self._ingress_firewall_policy_id = None
        self._egress_firewall_policy_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ingress_firewall_policy_id is not None:
            self.ingress_firewall_policy_id = ingress_firewall_policy_id
        if egress_firewall_policy_id is not None:
            self.egress_firewall_policy_id = egress_firewall_policy_id

    @property
    def marker(self):
        """Gets the marker of this NeutronListFirewallGroupsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this NeutronListFirewallGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListFirewallGroupsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this NeutronListFirewallGroupsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this NeutronListFirewallGroupsRequest.

        每页返回的个数

        :return: The limit of this NeutronListFirewallGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListFirewallGroupsRequest.

        每页返回的个数

        :param limit: The limit of this NeutronListFirewallGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        """Gets the id of this NeutronListFirewallGroupsRequest.

        使用id过滤网络ACL组

        :return: The id of this NeutronListFirewallGroupsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListFirewallGroupsRequest.

        使用id过滤网络ACL组

        :param id: The id of this NeutronListFirewallGroupsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronListFirewallGroupsRequest.

        使用name过滤ACL组

        :return: The name of this NeutronListFirewallGroupsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListFirewallGroupsRequest.

        使用name过滤ACL组

        :param name: The name of this NeutronListFirewallGroupsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronListFirewallGroupsRequest.

        使用description过滤ACL组

        :return: The description of this NeutronListFirewallGroupsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronListFirewallGroupsRequest.

        使用description过滤ACL组

        :param description: The description of this NeutronListFirewallGroupsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def ingress_firewall_policy_id(self):
        """Gets the ingress_firewall_policy_id of this NeutronListFirewallGroupsRequest.

        使用入方向的网络ACL策略ID过滤网络ACL组

        :return: The ingress_firewall_policy_id of this NeutronListFirewallGroupsRequest.
        :rtype: str
        """
        return self._ingress_firewall_policy_id

    @ingress_firewall_policy_id.setter
    def ingress_firewall_policy_id(self, ingress_firewall_policy_id):
        """Sets the ingress_firewall_policy_id of this NeutronListFirewallGroupsRequest.

        使用入方向的网络ACL策略ID过滤网络ACL组

        :param ingress_firewall_policy_id: The ingress_firewall_policy_id of this NeutronListFirewallGroupsRequest.
        :type ingress_firewall_policy_id: str
        """
        self._ingress_firewall_policy_id = ingress_firewall_policy_id

    @property
    def egress_firewall_policy_id(self):
        """Gets the egress_firewall_policy_id of this NeutronListFirewallGroupsRequest.

        使用出方向的网络ACL策略过滤查询网络ACL组

        :return: The egress_firewall_policy_id of this NeutronListFirewallGroupsRequest.
        :rtype: str
        """
        return self._egress_firewall_policy_id

    @egress_firewall_policy_id.setter
    def egress_firewall_policy_id(self, egress_firewall_policy_id):
        """Sets the egress_firewall_policy_id of this NeutronListFirewallGroupsRequest.

        使用出方向的网络ACL策略过滤查询网络ACL组

        :param egress_firewall_policy_id: The egress_firewall_policy_id of this NeutronListFirewallGroupsRequest.
        :type egress_firewall_policy_id: str
        """
        self._egress_firewall_policy_id = egress_firewall_policy_id

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
        if not isinstance(other, NeutronListFirewallGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
