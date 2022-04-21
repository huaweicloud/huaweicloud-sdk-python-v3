# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFunctionTriggerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'trigger_type_code': 'str',
        'trigger_id': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'trigger_type_code': 'trigger_type_code',
        'trigger_id': 'trigger_id'
    }

    def __init__(self, function_urn=None, trigger_type_code=None, trigger_id=None):
        """DeleteFunctionTriggerRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param trigger_type_code: 触发器类型代码。
        :type trigger_type_code: str
        :param trigger_id: 触发器编码。
        :type trigger_id: str
        """
        
        

        self._function_urn = None
        self._trigger_type_code = None
        self._trigger_id = None
        self.discriminator = None

        self.function_urn = function_urn
        self.trigger_type_code = trigger_type_code
        self.trigger_id = trigger_id

    @property
    def function_urn(self):
        """Gets the function_urn of this DeleteFunctionTriggerRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this DeleteFunctionTriggerRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this DeleteFunctionTriggerRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this DeleteFunctionTriggerRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def trigger_type_code(self):
        """Gets the trigger_type_code of this DeleteFunctionTriggerRequest.

        触发器类型代码。

        :return: The trigger_type_code of this DeleteFunctionTriggerRequest.
        :rtype: str
        """
        return self._trigger_type_code

    @trigger_type_code.setter
    def trigger_type_code(self, trigger_type_code):
        """Sets the trigger_type_code of this DeleteFunctionTriggerRequest.

        触发器类型代码。

        :param trigger_type_code: The trigger_type_code of this DeleteFunctionTriggerRequest.
        :type trigger_type_code: str
        """
        self._trigger_type_code = trigger_type_code

    @property
    def trigger_id(self):
        """Gets the trigger_id of this DeleteFunctionTriggerRequest.

        触发器编码。

        :return: The trigger_id of this DeleteFunctionTriggerRequest.
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this DeleteFunctionTriggerRequest.

        触发器编码。

        :param trigger_id: The trigger_id of this DeleteFunctionTriggerRequest.
        :type trigger_id: str
        """
        self._trigger_id = trigger_id

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
        if not isinstance(other, DeleteFunctionTriggerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
