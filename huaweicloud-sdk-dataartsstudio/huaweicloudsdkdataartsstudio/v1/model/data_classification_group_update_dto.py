# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationGroupUpdateDTO:

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
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'rule_ids': 'rule_ids',
        'description': 'description'
    }

    def __init__(self, name=None, rule_ids=None, description=None):
        r"""DataClassificationGroupUpdateDTO

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param rule_ids: 规则id列表
        :type rule_ids: list[str]
        :param description: 规则组描述
        :type description: str
        """
        
        

        self._name = None
        self._rule_ids = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.rule_ids = rule_ids
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this DataClassificationGroupUpdateDTO.

        规则名称

        :return: The name of this DataClassificationGroupUpdateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataClassificationGroupUpdateDTO.

        规则名称

        :param name: The name of this DataClassificationGroupUpdateDTO.
        :type name: str
        """
        self._name = name

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this DataClassificationGroupUpdateDTO.

        规则id列表

        :return: The rule_ids of this DataClassificationGroupUpdateDTO.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this DataClassificationGroupUpdateDTO.

        规则id列表

        :param rule_ids: The rule_ids of this DataClassificationGroupUpdateDTO.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

    @property
    def description(self):
        r"""Gets the description of this DataClassificationGroupUpdateDTO.

        规则组描述

        :return: The description of this DataClassificationGroupUpdateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataClassificationGroupUpdateDTO.

        规则组描述

        :param description: The description of this DataClassificationGroupUpdateDTO.
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
        if not isinstance(other, DataClassificationGroupUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
