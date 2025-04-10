# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationCombineRuleCheckDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expression': 'str',
        'combine_input_data': 'DataClassificationCombineRuleCheckDTOCombineInputData',
        'combine': 'bool',
        'single_rule_check_list': 'list[DataClassificationSingleRuleDTO]'
    }

    attribute_map = {
        'expression': 'expression',
        'combine_input_data': 'combine_input_data',
        'combine': 'combine',
        'single_rule_check_list': 'single_rule_check_list'
    }

    def __init__(self, expression=None, combine_input_data=None, combine=None, single_rule_check_list=None):
        r"""DataClassificationCombineRuleCheckDTO

        The model defined in huaweicloud sdk

        :param expression: 条件表达式
        :type expression: str
        :param combine_input_data: 
        :type combine_input_data: :class:`huaweicloudsdkdataartsstudio.v1.DataClassificationCombineRuleCheckDTOCombineInputData`
        :param combine: 分类ID
        :type combine: bool
        :param single_rule_check_list: 条件单规则列表
        :type single_rule_check_list: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationSingleRuleDTO`]
        """
        
        

        self._expression = None
        self._combine_input_data = None
        self._combine = None
        self._single_rule_check_list = None
        self.discriminator = None

        if expression is not None:
            self.expression = expression
        if combine_input_data is not None:
            self.combine_input_data = combine_input_data
        if combine is not None:
            self.combine = combine
        if single_rule_check_list is not None:
            self.single_rule_check_list = single_rule_check_list

    @property
    def expression(self):
        r"""Gets the expression of this DataClassificationCombineRuleCheckDTO.

        条件表达式

        :return: The expression of this DataClassificationCombineRuleCheckDTO.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this DataClassificationCombineRuleCheckDTO.

        条件表达式

        :param expression: The expression of this DataClassificationCombineRuleCheckDTO.
        :type expression: str
        """
        self._expression = expression

    @property
    def combine_input_data(self):
        r"""Gets the combine_input_data of this DataClassificationCombineRuleCheckDTO.

        :return: The combine_input_data of this DataClassificationCombineRuleCheckDTO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataClassificationCombineRuleCheckDTOCombineInputData`
        """
        return self._combine_input_data

    @combine_input_data.setter
    def combine_input_data(self, combine_input_data):
        r"""Sets the combine_input_data of this DataClassificationCombineRuleCheckDTO.

        :param combine_input_data: The combine_input_data of this DataClassificationCombineRuleCheckDTO.
        :type combine_input_data: :class:`huaweicloudsdkdataartsstudio.v1.DataClassificationCombineRuleCheckDTOCombineInputData`
        """
        self._combine_input_data = combine_input_data

    @property
    def combine(self):
        r"""Gets the combine of this DataClassificationCombineRuleCheckDTO.

        分类ID

        :return: The combine of this DataClassificationCombineRuleCheckDTO.
        :rtype: bool
        """
        return self._combine

    @combine.setter
    def combine(self, combine):
        r"""Sets the combine of this DataClassificationCombineRuleCheckDTO.

        分类ID

        :param combine: The combine of this DataClassificationCombineRuleCheckDTO.
        :type combine: bool
        """
        self._combine = combine

    @property
    def single_rule_check_list(self):
        r"""Gets the single_rule_check_list of this DataClassificationCombineRuleCheckDTO.

        条件单规则列表

        :return: The single_rule_check_list of this DataClassificationCombineRuleCheckDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationSingleRuleDTO`]
        """
        return self._single_rule_check_list

    @single_rule_check_list.setter
    def single_rule_check_list(self, single_rule_check_list):
        r"""Sets the single_rule_check_list of this DataClassificationCombineRuleCheckDTO.

        条件单规则列表

        :param single_rule_check_list: The single_rule_check_list of this DataClassificationCombineRuleCheckDTO.
        :type single_rule_check_list: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationSingleRuleDTO`]
        """
        self._single_rule_check_list = single_rule_check_list

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
        if not isinstance(other, DataClassificationCombineRuleCheckDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
