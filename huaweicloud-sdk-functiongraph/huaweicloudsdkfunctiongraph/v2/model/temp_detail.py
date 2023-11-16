# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TempDetail:

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
        'output': 'str',
        'warning': 'str'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'warning': 'warning'
    }

    def __init__(self, input=None, output=None, warning=None):
        """TempDetail

        The model defined in huaweicloud sdk

        :param input: 模板输入
        :type input: str
        :param output: 模板输出
        :type output: str
        :param warning: 警告信息
        :type warning: str
        """
        
        

        self._input = None
        self._output = None
        self._warning = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if warning is not None:
            self.warning = warning

    @property
    def input(self):
        """Gets the input of this TempDetail.

        模板输入

        :return: The input of this TempDetail.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this TempDetail.

        模板输入

        :param input: The input of this TempDetail.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this TempDetail.

        模板输出

        :return: The output of this TempDetail.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TempDetail.

        模板输出

        :param output: The output of this TempDetail.
        :type output: str
        """
        self._output = output

    @property
    def warning(self):
        """Gets the warning of this TempDetail.

        警告信息

        :return: The warning of this TempDetail.
        :rtype: str
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this TempDetail.

        警告信息

        :param warning: The warning of this TempDetail.
        :type warning: str
        """
        self._warning = warning

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
        if not isinstance(other, TempDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
