# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StateDataFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'str',
        'output': 'str'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output'
    }

    def __init__(self, input=None, output=None):
        """StateDataFilter

        The model defined in huaweicloud sdk

        :param input: 输入过滤表达式（JsonPath）
        :type input: str
        :param output: 输出过滤表达式（JsonPath）
        :type output: str
        """
        
        

        self._input = None
        self._output = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if output is not None:
            self.output = output

    @property
    def input(self):
        """Gets the input of this StateDataFilter.

        输入过滤表达式（JsonPath）

        :return: The input of this StateDataFilter.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this StateDataFilter.

        输入过滤表达式（JsonPath）

        :param input: The input of this StateDataFilter.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this StateDataFilter.

        输出过滤表达式（JsonPath）

        :return: The output of this StateDataFilter.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this StateDataFilter.

        输出过滤表达式（JsonPath）

        :param output: The output of this StateDataFilter.
        :type output: str
        """
        self._output = output

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
        if not isinstance(other, StateDataFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
