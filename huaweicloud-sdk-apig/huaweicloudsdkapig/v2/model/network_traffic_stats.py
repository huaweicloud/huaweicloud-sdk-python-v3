# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkTrafficStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output_throughput': 'int',
        'input_throughput': 'int'
    }

    attribute_map = {
        'output_throughput': 'output_throughput',
        'input_throughput': 'input_throughput'
    }

    def __init__(self, output_throughput=None, input_throughput=None):
        """NetworkTrafficStats

        The model defined in huaweicloud sdk

        :param output_throughput: 下行吞吐量（byte）
        :type output_throughput: int
        :param input_throughput: 上行吞吐量（byte）
        :type input_throughput: int
        """
        
        

        self._output_throughput = None
        self._input_throughput = None
        self.discriminator = None

        if output_throughput is not None:
            self.output_throughput = output_throughput
        if input_throughput is not None:
            self.input_throughput = input_throughput

    @property
    def output_throughput(self):
        """Gets the output_throughput of this NetworkTrafficStats.

        下行吞吐量（byte）

        :return: The output_throughput of this NetworkTrafficStats.
        :rtype: int
        """
        return self._output_throughput

    @output_throughput.setter
    def output_throughput(self, output_throughput):
        """Sets the output_throughput of this NetworkTrafficStats.

        下行吞吐量（byte）

        :param output_throughput: The output_throughput of this NetworkTrafficStats.
        :type output_throughput: int
        """
        self._output_throughput = output_throughput

    @property
    def input_throughput(self):
        """Gets the input_throughput of this NetworkTrafficStats.

        上行吞吐量（byte）

        :return: The input_throughput of this NetworkTrafficStats.
        :rtype: int
        """
        return self._input_throughput

    @input_throughput.setter
    def input_throughput(self, input_throughput):
        """Sets the input_throughput of this NetworkTrafficStats.

        上行吞吐量（byte）

        :param input_throughput: The input_throughput of this NetworkTrafficStats.
        :type input_throughput: int
        """
        self._input_throughput = input_throughput

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
        if not isinstance(other, NetworkTrafficStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
