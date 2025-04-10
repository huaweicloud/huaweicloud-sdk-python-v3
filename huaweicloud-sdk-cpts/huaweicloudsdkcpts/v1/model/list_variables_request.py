# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVariablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'variable_type': 'int',
        'test_suite_id': 'int'
    }

    attribute_map = {
        'variable_type': 'variable_type',
        'test_suite_id': 'test_suite_id'
    }

    def __init__(self, variable_type=None, test_suite_id=None):
        r"""ListVariablesRequest

        The model defined in huaweicloud sdk

        :param variable_type: 变量类型
        :type variable_type: int
        :param test_suite_id: 测试工程id
        :type test_suite_id: int
        """
        
        

        self._variable_type = None
        self._test_suite_id = None
        self.discriminator = None

        self.variable_type = variable_type
        self.test_suite_id = test_suite_id

    @property
    def variable_type(self):
        r"""Gets the variable_type of this ListVariablesRequest.

        变量类型

        :return: The variable_type of this ListVariablesRequest.
        :rtype: int
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        r"""Sets the variable_type of this ListVariablesRequest.

        变量类型

        :param variable_type: The variable_type of this ListVariablesRequest.
        :type variable_type: int
        """
        self._variable_type = variable_type

    @property
    def test_suite_id(self):
        r"""Gets the test_suite_id of this ListVariablesRequest.

        测试工程id

        :return: The test_suite_id of this ListVariablesRequest.
        :rtype: int
        """
        return self._test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        r"""Sets the test_suite_id of this ListVariablesRequest.

        测试工程id

        :param test_suite_id: The test_suite_id of this ListVariablesRequest.
        :type test_suite_id: int
        """
        self._test_suite_id = test_suite_id

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
        if not isinstance(other, ListVariablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
