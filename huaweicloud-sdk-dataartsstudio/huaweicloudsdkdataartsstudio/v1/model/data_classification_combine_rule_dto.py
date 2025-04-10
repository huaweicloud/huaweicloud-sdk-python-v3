# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationCombineRuleDTO:

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
        'secrecy_level_id': 'str',
        'combine_expression': 'str',
        'description': 'str',
        'category_id': 'str',
        'enable': 'bool',
        'single_expressions': 'list[DataClassificationSingleRuleDTO]'
    }

    attribute_map = {
        'name': 'name',
        'secrecy_level_id': 'secrecy_level_id',
        'combine_expression': 'combine_expression',
        'description': 'description',
        'category_id': 'category_id',
        'enable': 'enable',
        'single_expressions': 'single_expressions'
    }

    def __init__(self, name=None, secrecy_level_id=None, combine_expression=None, description=None, category_id=None, enable=None, single_expressions=None):
        r"""DataClassificationCombineRuleDTO

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param secrecy_level_id: 密级ID
        :type secrecy_level_id: str
        :param combine_expression: 条件表达式
        :type combine_expression: str
        :param description: 规则描述
        :type description: str
        :param category_id: 分类ID
        :type category_id: str
        :param enable: 使能状态。
        :type enable: bool
        :param single_expressions: 条件单规则
        :type single_expressions: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationSingleRuleDTO`]
        """
        
        

        self._name = None
        self._secrecy_level_id = None
        self._combine_expression = None
        self._description = None
        self._category_id = None
        self._enable = None
        self._single_expressions = None
        self.discriminator = None

        self.name = name
        self.secrecy_level_id = secrecy_level_id
        self.combine_expression = combine_expression
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if enable is not None:
            self.enable = enable
        self.single_expressions = single_expressions

    @property
    def name(self):
        r"""Gets the name of this DataClassificationCombineRuleDTO.

        规则名称

        :return: The name of this DataClassificationCombineRuleDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataClassificationCombineRuleDTO.

        规则名称

        :param name: The name of this DataClassificationCombineRuleDTO.
        :type name: str
        """
        self._name = name

    @property
    def secrecy_level_id(self):
        r"""Gets the secrecy_level_id of this DataClassificationCombineRuleDTO.

        密级ID

        :return: The secrecy_level_id of this DataClassificationCombineRuleDTO.
        :rtype: str
        """
        return self._secrecy_level_id

    @secrecy_level_id.setter
    def secrecy_level_id(self, secrecy_level_id):
        r"""Sets the secrecy_level_id of this DataClassificationCombineRuleDTO.

        密级ID

        :param secrecy_level_id: The secrecy_level_id of this DataClassificationCombineRuleDTO.
        :type secrecy_level_id: str
        """
        self._secrecy_level_id = secrecy_level_id

    @property
    def combine_expression(self):
        r"""Gets the combine_expression of this DataClassificationCombineRuleDTO.

        条件表达式

        :return: The combine_expression of this DataClassificationCombineRuleDTO.
        :rtype: str
        """
        return self._combine_expression

    @combine_expression.setter
    def combine_expression(self, combine_expression):
        r"""Sets the combine_expression of this DataClassificationCombineRuleDTO.

        条件表达式

        :param combine_expression: The combine_expression of this DataClassificationCombineRuleDTO.
        :type combine_expression: str
        """
        self._combine_expression = combine_expression

    @property
    def description(self):
        r"""Gets the description of this DataClassificationCombineRuleDTO.

        规则描述

        :return: The description of this DataClassificationCombineRuleDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataClassificationCombineRuleDTO.

        规则描述

        :param description: The description of this DataClassificationCombineRuleDTO.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        r"""Gets the category_id of this DataClassificationCombineRuleDTO.

        分类ID

        :return: The category_id of this DataClassificationCombineRuleDTO.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this DataClassificationCombineRuleDTO.

        分类ID

        :param category_id: The category_id of this DataClassificationCombineRuleDTO.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def enable(self):
        r"""Gets the enable of this DataClassificationCombineRuleDTO.

        使能状态。

        :return: The enable of this DataClassificationCombineRuleDTO.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this DataClassificationCombineRuleDTO.

        使能状态。

        :param enable: The enable of this DataClassificationCombineRuleDTO.
        :type enable: bool
        """
        self._enable = enable

    @property
    def single_expressions(self):
        r"""Gets the single_expressions of this DataClassificationCombineRuleDTO.

        条件单规则

        :return: The single_expressions of this DataClassificationCombineRuleDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationSingleRuleDTO`]
        """
        return self._single_expressions

    @single_expressions.setter
    def single_expressions(self, single_expressions):
        r"""Sets the single_expressions of this DataClassificationCombineRuleDTO.

        条件单规则

        :param single_expressions: The single_expressions of this DataClassificationCombineRuleDTO.
        :type single_expressions: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationSingleRuleDTO`]
        """
        self._single_expressions = single_expressions

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
        if not isinstance(other, DataClassificationCombineRuleDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
