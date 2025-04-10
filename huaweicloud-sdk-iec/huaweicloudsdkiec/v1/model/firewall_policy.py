# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallPolicy:

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
        'firewall_rules': 'list[FirewallRule]',
        'insert_after': 'str',
        'insert_before': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'firewall_rules': 'firewall_rules',
        'insert_after': 'insert_after',
        'insert_before': 'insert_before'
    }

    def __init__(self, id=None, name=None, firewall_rules=None, insert_after=None, insert_before=None):
        r"""FirewallPolicy

        The model defined in huaweicloud sdk

        :param id: 网络ACL策略ID。
        :type id: str
        :param name: 网络ACL策略名称。
        :type name: str
        :param firewall_rules: 网络ACL规则列表对象。
        :type firewall_rules: list[:class:`huaweicloudsdkiec.v1.FirewallRule`]
        :param insert_after: ACL规则ID，表示在此ACL规则之后添加ACL规则
        :type insert_after: str
        :param insert_before: ACL规则ID，表示在此ACL规则之前添加ACL规则
        :type insert_before: str
        """
        
        

        self._id = None
        self._name = None
        self._firewall_rules = None
        self._insert_after = None
        self._insert_before = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        self.firewall_rules = firewall_rules
        if insert_after is not None:
            self.insert_after = insert_after
        if insert_before is not None:
            self.insert_before = insert_before

    @property
    def id(self):
        r"""Gets the id of this FirewallPolicy.

        网络ACL策略ID。

        :return: The id of this FirewallPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FirewallPolicy.

        网络ACL策略ID。

        :param id: The id of this FirewallPolicy.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this FirewallPolicy.

        网络ACL策略名称。

        :return: The name of this FirewallPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FirewallPolicy.

        网络ACL策略名称。

        :param name: The name of this FirewallPolicy.
        :type name: str
        """
        self._name = name

    @property
    def firewall_rules(self):
        r"""Gets the firewall_rules of this FirewallPolicy.

        网络ACL规则列表对象。

        :return: The firewall_rules of this FirewallPolicy.
        :rtype: list[:class:`huaweicloudsdkiec.v1.FirewallRule`]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        r"""Sets the firewall_rules of this FirewallPolicy.

        网络ACL规则列表对象。

        :param firewall_rules: The firewall_rules of this FirewallPolicy.
        :type firewall_rules: list[:class:`huaweicloudsdkiec.v1.FirewallRule`]
        """
        self._firewall_rules = firewall_rules

    @property
    def insert_after(self):
        r"""Gets the insert_after of this FirewallPolicy.

        ACL规则ID，表示在此ACL规则之后添加ACL规则

        :return: The insert_after of this FirewallPolicy.
        :rtype: str
        """
        return self._insert_after

    @insert_after.setter
    def insert_after(self, insert_after):
        r"""Sets the insert_after of this FirewallPolicy.

        ACL规则ID，表示在此ACL规则之后添加ACL规则

        :param insert_after: The insert_after of this FirewallPolicy.
        :type insert_after: str
        """
        self._insert_after = insert_after

    @property
    def insert_before(self):
        r"""Gets the insert_before of this FirewallPolicy.

        ACL规则ID，表示在此ACL规则之前添加ACL规则

        :return: The insert_before of this FirewallPolicy.
        :rtype: str
        """
        return self._insert_before

    @insert_before.setter
    def insert_before(self, insert_before):
        r"""Sets the insert_before of this FirewallPolicy.

        ACL规则ID，表示在此ACL规则之前添加ACL规则

        :param insert_before: The insert_before of this FirewallPolicy.
        :type insert_before: str
        """
        self._insert_before = insert_before

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
        if not isinstance(other, FirewallPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
