# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateParamVariableValidation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'error_message': 'error_message'
    }

    def __init__(self, condition=None, error_message=None):
        r"""TemplateParamVariableValidation

        The model defined in huaweicloud sdk

        :param condition: 校验表达式。
        :type condition: str
        :param error_message: 校验失败后的错误信息。
        :type error_message: str
        """
        
        

        self._condition = None
        self._error_message = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if error_message is not None:
            self.error_message = error_message

    @property
    def condition(self):
        r"""Gets the condition of this TemplateParamVariableValidation.

        校验表达式。

        :return: The condition of this TemplateParamVariableValidation.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this TemplateParamVariableValidation.

        校验表达式。

        :param condition: The condition of this TemplateParamVariableValidation.
        :type condition: str
        """
        self._condition = condition

    @property
    def error_message(self):
        r"""Gets the error_message of this TemplateParamVariableValidation.

        校验失败后的错误信息。

        :return: The error_message of this TemplateParamVariableValidation.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this TemplateParamVariableValidation.

        校验失败后的错误信息。

        :param error_message: The error_message of this TemplateParamVariableValidation.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, TemplateParamVariableValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
