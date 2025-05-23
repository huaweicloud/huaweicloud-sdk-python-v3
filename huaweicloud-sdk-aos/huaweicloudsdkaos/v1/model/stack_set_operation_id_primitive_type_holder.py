# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackSetOperationIdPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_set_operation_id': 'str'
    }

    attribute_map = {
        'stack_set_operation_id': 'stack_set_operation_id'
    }

    def __init__(self, stack_set_operation_id=None):
        r"""StackSetOperationIdPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param stack_set_operation_id: 资源栈集操作（stack_set_operation）的唯一Id。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。
        :type stack_set_operation_id: str
        """
        
        

        self._stack_set_operation_id = None
        self.discriminator = None

        if stack_set_operation_id is not None:
            self.stack_set_operation_id = stack_set_operation_id

    @property
    def stack_set_operation_id(self):
        r"""Gets the stack_set_operation_id of this StackSetOperationIdPrimitiveTypeHolder.

        资源栈集操作（stack_set_operation）的唯一Id。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :return: The stack_set_operation_id of this StackSetOperationIdPrimitiveTypeHolder.
        :rtype: str
        """
        return self._stack_set_operation_id

    @stack_set_operation_id.setter
    def stack_set_operation_id(self, stack_set_operation_id):
        r"""Sets the stack_set_operation_id of this StackSetOperationIdPrimitiveTypeHolder.

        资源栈集操作（stack_set_operation）的唯一Id。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :param stack_set_operation_id: The stack_set_operation_id of this StackSetOperationIdPrimitiveTypeHolder.
        :type stack_set_operation_id: str
        """
        self._stack_set_operation_id = stack_set_operation_id

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
        if not isinstance(other, StackSetOperationIdPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
