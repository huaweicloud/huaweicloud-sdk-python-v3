# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagedOperation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_parallel_operation': 'bool'
    }

    attribute_map = {
        'enable_parallel_operation': 'enable_parallel_operation'
    }

    def __init__(self, enable_parallel_operation=None):
        r"""ManagedOperation

        The model defined in huaweicloud sdk

        :param enable_parallel_operation: 资源栈集（stack_set）是否可以并发地创建多个资源栈集操作。该参数作为资源栈集属性，可以通过创建资源栈集API（CreateStackSet）指定，通过更新资源栈集API（UpdateStackSet）更新该参数。  该参数默认为false，资源栈集只允许以串行的方式生成并执行资源栈集操作。同一时刻，资源栈集中只会存在一个处于运行态，即QUEUE_IN_PROGRESS或OPERATION_IN_PROGRESS状态的资源栈集操作，该操作执行完成后，下一个资源栈集操作才允许被创建。  该参数如果设定为true，资源栈集允许并发地生成多个资源栈集操作，执行非冲突操作，并将冲突操作进行排队处理。当冲突操作执行完毕，资源栈集按请求顺序继续执行排队操作。当前同一资源栈集下最多允许创建10个并发的资源栈集操作。  注：冲突操作指资源栈集允许多个操作同时执行的条件下，如果超过一个以上的操作包含了同一资源栈实例，此时在该资源栈实例上的多个操作被称为冲突操作。  当资源栈集状态为OPERATION_IN_PROGRESS时，不允许用户通过更新资源栈集（UpdateStackSet）来更新该参数。  * 当前，一个资源栈集下仅允许同时最多存在10个处于运行态的资源栈集操作*
        :type enable_parallel_operation: bool
        """
        
        

        self._enable_parallel_operation = None
        self.discriminator = None

        if enable_parallel_operation is not None:
            self.enable_parallel_operation = enable_parallel_operation

    @property
    def enable_parallel_operation(self):
        r"""Gets the enable_parallel_operation of this ManagedOperation.

        资源栈集（stack_set）是否可以并发地创建多个资源栈集操作。该参数作为资源栈集属性，可以通过创建资源栈集API（CreateStackSet）指定，通过更新资源栈集API（UpdateStackSet）更新该参数。  该参数默认为false，资源栈集只允许以串行的方式生成并执行资源栈集操作。同一时刻，资源栈集中只会存在一个处于运行态，即QUEUE_IN_PROGRESS或OPERATION_IN_PROGRESS状态的资源栈集操作，该操作执行完成后，下一个资源栈集操作才允许被创建。  该参数如果设定为true，资源栈集允许并发地生成多个资源栈集操作，执行非冲突操作，并将冲突操作进行排队处理。当冲突操作执行完毕，资源栈集按请求顺序继续执行排队操作。当前同一资源栈集下最多允许创建10个并发的资源栈集操作。  注：冲突操作指资源栈集允许多个操作同时执行的条件下，如果超过一个以上的操作包含了同一资源栈实例，此时在该资源栈实例上的多个操作被称为冲突操作。  当资源栈集状态为OPERATION_IN_PROGRESS时，不允许用户通过更新资源栈集（UpdateStackSet）来更新该参数。  * 当前，一个资源栈集下仅允许同时最多存在10个处于运行态的资源栈集操作*

        :return: The enable_parallel_operation of this ManagedOperation.
        :rtype: bool
        """
        return self._enable_parallel_operation

    @enable_parallel_operation.setter
    def enable_parallel_operation(self, enable_parallel_operation):
        r"""Sets the enable_parallel_operation of this ManagedOperation.

        资源栈集（stack_set）是否可以并发地创建多个资源栈集操作。该参数作为资源栈集属性，可以通过创建资源栈集API（CreateStackSet）指定，通过更新资源栈集API（UpdateStackSet）更新该参数。  该参数默认为false，资源栈集只允许以串行的方式生成并执行资源栈集操作。同一时刻，资源栈集中只会存在一个处于运行态，即QUEUE_IN_PROGRESS或OPERATION_IN_PROGRESS状态的资源栈集操作，该操作执行完成后，下一个资源栈集操作才允许被创建。  该参数如果设定为true，资源栈集允许并发地生成多个资源栈集操作，执行非冲突操作，并将冲突操作进行排队处理。当冲突操作执行完毕，资源栈集按请求顺序继续执行排队操作。当前同一资源栈集下最多允许创建10个并发的资源栈集操作。  注：冲突操作指资源栈集允许多个操作同时执行的条件下，如果超过一个以上的操作包含了同一资源栈实例，此时在该资源栈实例上的多个操作被称为冲突操作。  当资源栈集状态为OPERATION_IN_PROGRESS时，不允许用户通过更新资源栈集（UpdateStackSet）来更新该参数。  * 当前，一个资源栈集下仅允许同时最多存在10个处于运行态的资源栈集操作*

        :param enable_parallel_operation: The enable_parallel_operation of this ManagedOperation.
        :type enable_parallel_operation: bool
        """
        self._enable_parallel_operation = enable_parallel_operation

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
        if not isinstance(other, ManagedOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
