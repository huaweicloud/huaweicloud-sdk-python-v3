# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutKvRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'condition_expression': 'ConditionExpression',
        'kv_doc': 'dict'
    }

    attribute_map = {
        'table_name': 'table_name',
        'condition_expression': 'condition_expression',
        'kv_doc': 'kv_doc'
    }

    def __init__(self, table_name=None, condition_expression=None, kv_doc=None):
        r"""PutKvRequestBody

        The model defined in huaweicloud sdk

        :param table_name: 表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type table_name: str
        :param condition_expression: 
        :type condition_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        :param kv_doc: 用户文档。
        :type kv_doc: dict
        """
        
        

        self._table_name = None
        self._condition_expression = None
        self._kv_doc = None
        self.discriminator = None

        self.table_name = table_name
        if condition_expression is not None:
            self.condition_expression = condition_expression
        if kv_doc is not None:
            self.kv_doc = kv_doc

    @property
    def table_name(self):
        r"""Gets the table_name of this PutKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The table_name of this PutKvRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this PutKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param table_name: The table_name of this PutKvRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this PutKvRequestBody.

        :return: The condition_expression of this PutKvRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this PutKvRequestBody.

        :param condition_expression: The condition_expression of this PutKvRequestBody.
        :type condition_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        self._condition_expression = condition_expression

    @property
    def kv_doc(self):
        r"""Gets the kv_doc of this PutKvRequestBody.

        用户文档。

        :return: The kv_doc of this PutKvRequestBody.
        :rtype: dict
        """
        return self._kv_doc

    @kv_doc.setter
    def kv_doc(self, kv_doc):
        r"""Sets the kv_doc of this PutKvRequestBody.

        用户文档。

        :param kv_doc: The kv_doc of this PutKvRequestBody.
        :type kv_doc: dict
        """
        self._kv_doc = kv_doc

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
        if not isinstance(other, PutKvRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
