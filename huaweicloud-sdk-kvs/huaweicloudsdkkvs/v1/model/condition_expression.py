# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionExpression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'single_field_expression': 'SingleFieldExpression',
        'multi_field_expression': 'MultiFieldExpression',
        'composed_expression': 'ComposedExpression',
        'single_kv_expression': 'SingleKvExpression'
    }

    attribute_map = {
        'single_field_expression': 'single_field_expression',
        'multi_field_expression': 'multi_field_expression',
        'composed_expression': 'composed_expression',
        'single_kv_expression': 'single_kv_expression'
    }

    def __init__(self, single_field_expression=None, multi_field_expression=None, composed_expression=None, single_kv_expression=None):
        r"""ConditionExpression

        The model defined in huaweicloud sdk

        :param single_field_expression: 
        :type single_field_expression: :class:`huaweicloudsdkkvs.v1.SingleFieldExpression`
        :param multi_field_expression: 
        :type multi_field_expression: :class:`huaweicloudsdkkvs.v1.MultiFieldExpression`
        :param composed_expression: 
        :type composed_expression: :class:`huaweicloudsdkkvs.v1.ComposedExpression`
        :param single_kv_expression: 
        :type single_kv_expression: :class:`huaweicloudsdkkvs.v1.SingleKvExpression`
        """
        
        

        self._single_field_expression = None
        self._multi_field_expression = None
        self._composed_expression = None
        self._single_kv_expression = None
        self.discriminator = None

        if single_field_expression is not None:
            self.single_field_expression = single_field_expression
        if multi_field_expression is not None:
            self.multi_field_expression = multi_field_expression
        if composed_expression is not None:
            self.composed_expression = composed_expression
        if single_kv_expression is not None:
            self.single_kv_expression = single_kv_expression

    @property
    def single_field_expression(self):
        r"""Gets the single_field_expression of this ConditionExpression.

        :return: The single_field_expression of this ConditionExpression.
        :rtype: :class:`huaweicloudsdkkvs.v1.SingleFieldExpression`
        """
        return self._single_field_expression

    @single_field_expression.setter
    def single_field_expression(self, single_field_expression):
        r"""Sets the single_field_expression of this ConditionExpression.

        :param single_field_expression: The single_field_expression of this ConditionExpression.
        :type single_field_expression: :class:`huaweicloudsdkkvs.v1.SingleFieldExpression`
        """
        self._single_field_expression = single_field_expression

    @property
    def multi_field_expression(self):
        r"""Gets the multi_field_expression of this ConditionExpression.

        :return: The multi_field_expression of this ConditionExpression.
        :rtype: :class:`huaweicloudsdkkvs.v1.MultiFieldExpression`
        """
        return self._multi_field_expression

    @multi_field_expression.setter
    def multi_field_expression(self, multi_field_expression):
        r"""Sets the multi_field_expression of this ConditionExpression.

        :param multi_field_expression: The multi_field_expression of this ConditionExpression.
        :type multi_field_expression: :class:`huaweicloudsdkkvs.v1.MultiFieldExpression`
        """
        self._multi_field_expression = multi_field_expression

    @property
    def composed_expression(self):
        r"""Gets the composed_expression of this ConditionExpression.

        :return: The composed_expression of this ConditionExpression.
        :rtype: :class:`huaweicloudsdkkvs.v1.ComposedExpression`
        """
        return self._composed_expression

    @composed_expression.setter
    def composed_expression(self, composed_expression):
        r"""Sets the composed_expression of this ConditionExpression.

        :param composed_expression: The composed_expression of this ConditionExpression.
        :type composed_expression: :class:`huaweicloudsdkkvs.v1.ComposedExpression`
        """
        self._composed_expression = composed_expression

    @property
    def single_kv_expression(self):
        r"""Gets the single_kv_expression of this ConditionExpression.

        :return: The single_kv_expression of this ConditionExpression.
        :rtype: :class:`huaweicloudsdkkvs.v1.SingleKvExpression`
        """
        return self._single_kv_expression

    @single_kv_expression.setter
    def single_kv_expression(self, single_kv_expression):
        r"""Sets the single_kv_expression of this ConditionExpression.

        :param single_kv_expression: The single_kv_expression of this ConditionExpression.
        :type single_kv_expression: :class:`huaweicloudsdkkvs.v1.SingleKvExpression`
        """
        self._single_kv_expression = single_kv_expression

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
        if not isinstance(other, ConditionExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
