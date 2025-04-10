# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppRule:

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
        'description': 'str',
        'rule': 'Rule',
        'rule_source': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'rule': 'rule',
        'rule_source': 'rule_source',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, rule=None, rule_source=None, create_time=None, update_time=None):
        r"""AppRule

        The model defined in huaweicloud sdk

        :param id: 规则ID。
        :type id: str
        :param name: 规则名称。
        :type name: str
        :param description: 规则描述。
        :type description: str
        :param rule: 
        :type rule: :class:`huaweicloudsdkworkspace.v2.Rule`
        :param rule_source: 规则来源。
        :type rule_source: str
        :param create_time: 创建时间。
        :type create_time: datetime
        :param update_time: 更新时间。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._rule = None
        self._rule_source = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if rule is not None:
            self.rule = rule
        if rule_source is not None:
            self.rule_source = rule_source
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this AppRule.

        规则ID。

        :return: The id of this AppRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AppRule.

        规则ID。

        :param id: The id of this AppRule.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AppRule.

        规则名称。

        :return: The name of this AppRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AppRule.

        规则名称。

        :param name: The name of this AppRule.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AppRule.

        规则描述。

        :return: The description of this AppRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AppRule.

        规则描述。

        :param description: The description of this AppRule.
        :type description: str
        """
        self._description = description

    @property
    def rule(self):
        r"""Gets the rule of this AppRule.

        :return: The rule of this AppRule.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Rule`
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this AppRule.

        :param rule: The rule of this AppRule.
        :type rule: :class:`huaweicloudsdkworkspace.v2.Rule`
        """
        self._rule = rule

    @property
    def rule_source(self):
        r"""Gets the rule_source of this AppRule.

        规则来源。

        :return: The rule_source of this AppRule.
        :rtype: str
        """
        return self._rule_source

    @rule_source.setter
    def rule_source(self, rule_source):
        r"""Sets the rule_source of this AppRule.

        规则来源。

        :param rule_source: The rule_source of this AppRule.
        :type rule_source: str
        """
        self._rule_source = rule_source

    @property
    def create_time(self):
        r"""Gets the create_time of this AppRule.

        创建时间。

        :return: The create_time of this AppRule.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AppRule.

        创建时间。

        :param create_time: The create_time of this AppRule.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AppRule.

        更新时间。

        :return: The update_time of this AppRule.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AppRule.

        更新时间。

        :param update_time: The update_time of this AppRule.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, AppRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
