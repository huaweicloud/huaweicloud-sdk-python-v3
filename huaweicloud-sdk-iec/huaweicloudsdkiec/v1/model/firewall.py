# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Firewall:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'admin_state_up': 'bool',
        'status': 'str',
        'description': 'str',
        'domain_id': 'str',
        'egress_firewall_policy': 'FirewallPolicy',
        'egress_firewall_rule_count': 'int',
        'ingress_firewall_policy': 'FirewallPolicy',
        'ingress_firewall_rule_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'status': 'status',
        'description': 'description',
        'domain_id': 'domain_id',
        'egress_firewall_policy': 'egress_firewall_policy',
        'egress_firewall_rule_count': 'egress_firewall_rule_count',
        'ingress_firewall_policy': 'ingress_firewall_policy',
        'ingress_firewall_rule_count': 'ingress_firewall_rule_count'
    }

    def __init__(self, id=None, name=None, admin_state_up=None, status=None, description=None, domain_id=None, egress_firewall_policy=None, egress_firewall_rule_count=None, ingress_firewall_policy=None, ingress_firewall_rule_count=None):
        """Firewall

        The model defined in huaweicloud sdk

        :param id: 网络ACL ID
        :type id: str
        :param name: 网络ACL名称。
        :type name: str
        :param admin_state_up: 网络ACL使能开关。  取值范围：true（开启），false（关闭）。默认为true
        :type admin_state_up: bool
        :param status: 网络ACL状态。  取值范围：INACTIVE
        :type status: str
        :param description: 网络ACL描述。
        :type description: str
        :param domain_id: 租户domainID
        :type domain_id: str
        :param egress_firewall_policy: 
        :type egress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        :param egress_firewall_rule_count: 出方向网络ACL规则个数。
        :type egress_firewall_rule_count: int
        :param ingress_firewall_policy: 
        :type ingress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        :param ingress_firewall_rule_count: 入方向网络ACL规则个数。
        :type ingress_firewall_rule_count: int
        """
        
        

        self._id = None
        self._name = None
        self._admin_state_up = None
        self._status = None
        self._description = None
        self._domain_id = None
        self._egress_firewall_policy = None
        self._egress_firewall_rule_count = None
        self._ingress_firewall_policy = None
        self._ingress_firewall_rule_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if egress_firewall_policy is not None:
            self.egress_firewall_policy = egress_firewall_policy
        if egress_firewall_rule_count is not None:
            self.egress_firewall_rule_count = egress_firewall_rule_count
        if ingress_firewall_policy is not None:
            self.ingress_firewall_policy = ingress_firewall_policy
        if ingress_firewall_rule_count is not None:
            self.ingress_firewall_rule_count = ingress_firewall_rule_count

    @property
    def id(self):
        """Gets the id of this Firewall.

        网络ACL ID

        :return: The id of this Firewall.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Firewall.

        网络ACL ID

        :param id: The id of this Firewall.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Firewall.

        网络ACL名称。

        :return: The name of this Firewall.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Firewall.

        网络ACL名称。

        :param name: The name of this Firewall.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Firewall.

        网络ACL使能开关。  取值范围：true（开启），false（关闭）。默认为true

        :return: The admin_state_up of this Firewall.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Firewall.

        网络ACL使能开关。  取值范围：true（开启），false（关闭）。默认为true

        :param admin_state_up: The admin_state_up of this Firewall.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def status(self):
        """Gets the status of this Firewall.

        网络ACL状态。  取值范围：INACTIVE

        :return: The status of this Firewall.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Firewall.

        网络ACL状态。  取值范围：INACTIVE

        :param status: The status of this Firewall.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this Firewall.

        网络ACL描述。

        :return: The description of this Firewall.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Firewall.

        网络ACL描述。

        :param description: The description of this Firewall.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this Firewall.

        租户domainID

        :return: The domain_id of this Firewall.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Firewall.

        租户domainID

        :param domain_id: The domain_id of this Firewall.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def egress_firewall_policy(self):
        """Gets the egress_firewall_policy of this Firewall.


        :return: The egress_firewall_policy of this Firewall.
        :rtype: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        return self._egress_firewall_policy

    @egress_firewall_policy.setter
    def egress_firewall_policy(self, egress_firewall_policy):
        """Sets the egress_firewall_policy of this Firewall.


        :param egress_firewall_policy: The egress_firewall_policy of this Firewall.
        :type egress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        self._egress_firewall_policy = egress_firewall_policy

    @property
    def egress_firewall_rule_count(self):
        """Gets the egress_firewall_rule_count of this Firewall.

        出方向网络ACL规则个数。

        :return: The egress_firewall_rule_count of this Firewall.
        :rtype: int
        """
        return self._egress_firewall_rule_count

    @egress_firewall_rule_count.setter
    def egress_firewall_rule_count(self, egress_firewall_rule_count):
        """Sets the egress_firewall_rule_count of this Firewall.

        出方向网络ACL规则个数。

        :param egress_firewall_rule_count: The egress_firewall_rule_count of this Firewall.
        :type egress_firewall_rule_count: int
        """
        self._egress_firewall_rule_count = egress_firewall_rule_count

    @property
    def ingress_firewall_policy(self):
        """Gets the ingress_firewall_policy of this Firewall.


        :return: The ingress_firewall_policy of this Firewall.
        :rtype: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        return self._ingress_firewall_policy

    @ingress_firewall_policy.setter
    def ingress_firewall_policy(self, ingress_firewall_policy):
        """Sets the ingress_firewall_policy of this Firewall.


        :param ingress_firewall_policy: The ingress_firewall_policy of this Firewall.
        :type ingress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        self._ingress_firewall_policy = ingress_firewall_policy

    @property
    def ingress_firewall_rule_count(self):
        """Gets the ingress_firewall_rule_count of this Firewall.

        入方向网络ACL规则个数。

        :return: The ingress_firewall_rule_count of this Firewall.
        :rtype: int
        """
        return self._ingress_firewall_rule_count

    @ingress_firewall_rule_count.setter
    def ingress_firewall_rule_count(self, ingress_firewall_rule_count):
        """Sets the ingress_firewall_rule_count of this Firewall.

        入方向网络ACL规则个数。

        :param ingress_firewall_rule_count: The ingress_firewall_rule_count of this Firewall.
        :type ingress_firewall_rule_count: int
        """
        self._ingress_firewall_rule_count = ingress_firewall_rule_count

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
        if not isinstance(other, Firewall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
