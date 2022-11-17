# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutorPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'executor': 'str'
    }

    attribute_map = {
        'executor': 'executor'
    }

    def __init__(self, executor=None):
        """ExecutorPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param executor: 执行操作者的名字，将用做未来的审计工作
        :type executor: str
        """
        
        

        self._executor = None
        self.discriminator = None

        if executor is not None:
            self.executor = executor

    @property
    def executor(self):
        """Gets the executor of this ExecutorPrimitiveTypeHolder.

        执行操作者的名字，将用做未来的审计工作

        :return: The executor of this ExecutorPrimitiveTypeHolder.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this ExecutorPrimitiveTypeHolder.

        执行操作者的名字，将用做未来的审计工作

        :param executor: The executor of this ExecutorPrimitiveTypeHolder.
        :type executor: str
        """
        self._executor = executor

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
        if not isinstance(other, ExecutorPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
