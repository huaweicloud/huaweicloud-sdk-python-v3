# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attribute': 'str',
        'operator': 'str',
        'value': 'object',
        'condition': 'str',
        'criterion': 'list[DataMapFilterCriteria]'
    }

    attribute_map = {
        'attribute': 'attribute',
        'operator': 'operator',
        'value': 'value',
        'condition': 'condition',
        'criterion': 'criterion'
    }

    def __init__(self, attribute=None, operator=None, value=None, condition=None, criterion=None):
        """ConditionInfo

        The model defined in huaweicloud sdk

        :param attribute: 属性
        :type attribute: str
        :param operator: 操作员，默认值EQ
        :type operator: str
        :param value: 值
        :type value: object
        :param condition: 条件拼接准则，取值范围 AND,OR
        :type condition: str
        :param criterion: 条件准则
        :type criterion: list[:class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`]
        """
        
        

        self._attribute = None
        self._operator = None
        self._value = None
        self._condition = None
        self._criterion = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value
        if condition is not None:
            self.condition = condition
        if criterion is not None:
            self.criterion = criterion

    @property
    def attribute(self):
        """Gets the attribute of this ConditionInfo.

        属性

        :return: The attribute of this ConditionInfo.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this ConditionInfo.

        属性

        :param attribute: The attribute of this ConditionInfo.
        :type attribute: str
        """
        self._attribute = attribute

    @property
    def operator(self):
        """Gets the operator of this ConditionInfo.

        操作员，默认值EQ

        :return: The operator of this ConditionInfo.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ConditionInfo.

        操作员，默认值EQ

        :param operator: The operator of this ConditionInfo.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        """Gets the value of this ConditionInfo.

        值

        :return: The value of this ConditionInfo.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConditionInfo.

        值

        :param value: The value of this ConditionInfo.
        :type value: object
        """
        self._value = value

    @property
    def condition(self):
        """Gets the condition of this ConditionInfo.

        条件拼接准则，取值范围 AND,OR

        :return: The condition of this ConditionInfo.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ConditionInfo.

        条件拼接准则，取值范围 AND,OR

        :param condition: The condition of this ConditionInfo.
        :type condition: str
        """
        self._condition = condition

    @property
    def criterion(self):
        """Gets the criterion of this ConditionInfo.

        条件准则

        :return: The criterion of this ConditionInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`]
        """
        return self._criterion

    @criterion.setter
    def criterion(self, criterion):
        """Sets the criterion of this ConditionInfo.

        条件准则

        :param criterion: The criterion of this ConditionInfo.
        :type criterion: list[:class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`]
        """
        self._criterion = criterion

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
        if not isinstance(other, ConditionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
