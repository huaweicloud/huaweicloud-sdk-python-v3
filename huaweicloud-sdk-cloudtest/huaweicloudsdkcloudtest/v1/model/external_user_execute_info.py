# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalUserExecuteInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'executor': 'NameAndIdVo',
        'execute_count': 'int'
    }

    attribute_map = {
        'executor': 'executor',
        'execute_count': 'execute_count'
    }

    def __init__(self, executor=None, execute_count=None):
        r"""ExternalUserExecuteInfo

        The model defined in huaweicloud sdk

        :param executor: 
        :type executor: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param execute_count: 执行用例数
        :type execute_count: int
        """
        
        

        self._executor = None
        self._execute_count = None
        self.discriminator = None

        if executor is not None:
            self.executor = executor
        if execute_count is not None:
            self.execute_count = execute_count

    @property
    def executor(self):
        r"""Gets the executor of this ExternalUserExecuteInfo.

        :return: The executor of this ExternalUserExecuteInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this ExternalUserExecuteInfo.

        :param executor: The executor of this ExternalUserExecuteInfo.
        :type executor: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._executor = executor

    @property
    def execute_count(self):
        r"""Gets the execute_count of this ExternalUserExecuteInfo.

        执行用例数

        :return: The execute_count of this ExternalUserExecuteInfo.
        :rtype: int
        """
        return self._execute_count

    @execute_count.setter
    def execute_count(self, execute_count):
        r"""Sets the execute_count of this ExternalUserExecuteInfo.

        执行用例数

        :param execute_count: The execute_count of this ExternalUserExecuteInfo.
        :type execute_count: int
        """
        self._execute_count = execute_count

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
        if not isinstance(other, ExternalUserExecuteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
