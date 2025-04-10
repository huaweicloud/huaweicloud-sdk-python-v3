# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationGroupCreateDTO:

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
        'rule_ids': 'list[str]',
        'description': 'str',
        'create_rules': 'list[DataClassificationGroupCombineRuleDTO]'
    }

    attribute_map = {
        'name': 'name',
        'rule_ids': 'rule_ids',
        'description': 'description',
        'create_rules': 'create_rules'
    }

    def __init__(self, name=None, rule_ids=None, description=None, create_rules=None):
        r"""DataClassificationGroupCreateDTO

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param rule_ids: 规则id列表
        :type rule_ids: list[str]
        :param description: 规则组描述
        :type description: str
        :param create_rules: 需要创建的规则
        :type create_rules: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationGroupCombineRuleDTO`]
        """
        
        

        self._name = None
        self._rule_ids = None
        self._description = None
        self._create_rules = None
        self.discriminator = None

        self.name = name
        self.rule_ids = rule_ids
        if description is not None:
            self.description = description
        if create_rules is not None:
            self.create_rules = create_rules

    @property
    def name(self):
        r"""Gets the name of this DataClassificationGroupCreateDTO.

        规则名称

        :return: The name of this DataClassificationGroupCreateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataClassificationGroupCreateDTO.

        规则名称

        :param name: The name of this DataClassificationGroupCreateDTO.
        :type name: str
        """
        self._name = name

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this DataClassificationGroupCreateDTO.

        规则id列表

        :return: The rule_ids of this DataClassificationGroupCreateDTO.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this DataClassificationGroupCreateDTO.

        规则id列表

        :param rule_ids: The rule_ids of this DataClassificationGroupCreateDTO.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

    @property
    def description(self):
        r"""Gets the description of this DataClassificationGroupCreateDTO.

        规则组描述

        :return: The description of this DataClassificationGroupCreateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataClassificationGroupCreateDTO.

        规则组描述

        :param description: The description of this DataClassificationGroupCreateDTO.
        :type description: str
        """
        self._description = description

    @property
    def create_rules(self):
        r"""Gets the create_rules of this DataClassificationGroupCreateDTO.

        需要创建的规则

        :return: The create_rules of this DataClassificationGroupCreateDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationGroupCombineRuleDTO`]
        """
        return self._create_rules

    @create_rules.setter
    def create_rules(self, create_rules):
        r"""Sets the create_rules of this DataClassificationGroupCreateDTO.

        需要创建的规则

        :param create_rules: The create_rules of this DataClassificationGroupCreateDTO.
        :type create_rules: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationGroupCombineRuleDTO`]
        """
        self._create_rules = create_rules

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
        if not isinstance(other, DataClassificationGroupCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
