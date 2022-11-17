# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'rule_id': 'int',
        'default_value': 'str',
        'option_value': 'str',
        'option_key': 'str',
        'option_name': 'str',
        'template_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rule_id': 'rule_id',
        'default_value': 'default_value',
        'option_value': 'option_value',
        'option_key': 'option_key',
        'option_name': 'option_name',
        'template_id': 'template_id',
        'description': 'description'
    }

    def __init__(self, id=None, rule_id=None, default_value=None, option_value=None, option_key=None, option_name=None, template_id=None, description=None):
        """RuleConfig

        The model defined in huaweicloud sdk

        :param id: 规则配置ID
        :type id: int
        :param rule_id: 规则ID
        :type rule_id: int
        :param default_value: 默认值
        :type default_value: str
        :param option_value: 当前
        :type option_value: str
        :param option_key: 当前规则配置项key
        :type option_key: str
        :param option_name: 当前规则配置项名称
        :type option_name: str
        :param template_id: 规则集id
        :type template_id: str
        :param description: 描述
        :type description: str
        """
        
        

        self._id = None
        self._rule_id = None
        self._default_value = None
        self._option_value = None
        self._option_key = None
        self._option_name = None
        self._template_id = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if rule_id is not None:
            self.rule_id = rule_id
        if default_value is not None:
            self.default_value = default_value
        if option_value is not None:
            self.option_value = option_value
        if option_key is not None:
            self.option_key = option_key
        if option_name is not None:
            self.option_name = option_name
        if template_id is not None:
            self.template_id = template_id
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this RuleConfig.

        规则配置ID

        :return: The id of this RuleConfig.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleConfig.

        规则配置ID

        :param id: The id of this RuleConfig.
        :type id: int
        """
        self._id = id

    @property
    def rule_id(self):
        """Gets the rule_id of this RuleConfig.

        规则ID

        :return: The rule_id of this RuleConfig.
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this RuleConfig.

        规则ID

        :param rule_id: The rule_id of this RuleConfig.
        :type rule_id: int
        """
        self._rule_id = rule_id

    @property
    def default_value(self):
        """Gets the default_value of this RuleConfig.

        默认值

        :return: The default_value of this RuleConfig.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this RuleConfig.

        默认值

        :param default_value: The default_value of this RuleConfig.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def option_value(self):
        """Gets the option_value of this RuleConfig.

        当前

        :return: The option_value of this RuleConfig.
        :rtype: str
        """
        return self._option_value

    @option_value.setter
    def option_value(self, option_value):
        """Sets the option_value of this RuleConfig.

        当前

        :param option_value: The option_value of this RuleConfig.
        :type option_value: str
        """
        self._option_value = option_value

    @property
    def option_key(self):
        """Gets the option_key of this RuleConfig.

        当前规则配置项key

        :return: The option_key of this RuleConfig.
        :rtype: str
        """
        return self._option_key

    @option_key.setter
    def option_key(self, option_key):
        """Sets the option_key of this RuleConfig.

        当前规则配置项key

        :param option_key: The option_key of this RuleConfig.
        :type option_key: str
        """
        self._option_key = option_key

    @property
    def option_name(self):
        """Gets the option_name of this RuleConfig.

        当前规则配置项名称

        :return: The option_name of this RuleConfig.
        :rtype: str
        """
        return self._option_name

    @option_name.setter
    def option_name(self, option_name):
        """Sets the option_name of this RuleConfig.

        当前规则配置项名称

        :param option_name: The option_name of this RuleConfig.
        :type option_name: str
        """
        self._option_name = option_name

    @property
    def template_id(self):
        """Gets the template_id of this RuleConfig.

        规则集id

        :return: The template_id of this RuleConfig.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this RuleConfig.

        规则集id

        :param template_id: The template_id of this RuleConfig.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def description(self):
        """Gets the description of this RuleConfig.

        描述

        :return: The description of this RuleConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleConfig.

        描述

        :param description: The description of this RuleConfig.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RuleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
