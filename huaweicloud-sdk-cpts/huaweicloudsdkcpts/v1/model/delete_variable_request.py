# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteVariableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'variable_id': 'int',
        'test_suite_id': 'int'
    }

    attribute_map = {
        'variable_id': 'variable_id',
        'test_suite_id': 'test_suite_id'
    }

    def __init__(self, variable_id=None, test_suite_id=None):
        """DeleteVariableRequest

        The model defined in huaweicloud sdk

        :param variable_id: 全局变量id
        :type variable_id: int
        :param test_suite_id: 工程id
        :type test_suite_id: int
        """
        
        

        self._variable_id = None
        self._test_suite_id = None
        self.discriminator = None

        self.variable_id = variable_id
        self.test_suite_id = test_suite_id

    @property
    def variable_id(self):
        """Gets the variable_id of this DeleteVariableRequest.

        全局变量id

        :return: The variable_id of this DeleteVariableRequest.
        :rtype: int
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id):
        """Sets the variable_id of this DeleteVariableRequest.

        全局变量id

        :param variable_id: The variable_id of this DeleteVariableRequest.
        :type variable_id: int
        """
        self._variable_id = variable_id

    @property
    def test_suite_id(self):
        """Gets the test_suite_id of this DeleteVariableRequest.

        工程id

        :return: The test_suite_id of this DeleteVariableRequest.
        :rtype: int
        """
        return self._test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        """Sets the test_suite_id of this DeleteVariableRequest.

        工程id

        :param test_suite_id: The test_suite_id of this DeleteVariableRequest.
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
        if not isinstance(other, DeleteVariableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
