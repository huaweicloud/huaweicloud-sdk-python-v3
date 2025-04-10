# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsParallelPortRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parallel_port_enable': 'bool'
    }

    attribute_map = {
        'parallel_port_enable': 'parallel_port_enable'
    }

    def __init__(self, parallel_port_enable=None):
        r"""PoliciesPeripheralsParallelPortRedirection

        The model defined in huaweicloud sdk

        :param parallel_port_enable: 是否开启并口重定向。取值为： false：表示关闭。 true：表示开启。
        :type parallel_port_enable: bool
        """
        
        

        self._parallel_port_enable = None
        self.discriminator = None

        if parallel_port_enable is not None:
            self.parallel_port_enable = parallel_port_enable

    @property
    def parallel_port_enable(self):
        r"""Gets the parallel_port_enable of this PoliciesPeripheralsParallelPortRedirection.

        是否开启并口重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The parallel_port_enable of this PoliciesPeripheralsParallelPortRedirection.
        :rtype: bool
        """
        return self._parallel_port_enable

    @parallel_port_enable.setter
    def parallel_port_enable(self, parallel_port_enable):
        r"""Sets the parallel_port_enable of this PoliciesPeripheralsParallelPortRedirection.

        是否开启并口重定向。取值为： false：表示关闭。 true：表示开启。

        :param parallel_port_enable: The parallel_port_enable of this PoliciesPeripheralsParallelPortRedirection.
        :type parallel_port_enable: bool
        """
        self._parallel_port_enable = parallel_port_enable

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
        if not isinstance(other, PoliciesPeripheralsParallelPortRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
