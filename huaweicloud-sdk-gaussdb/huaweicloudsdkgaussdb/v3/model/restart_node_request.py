# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartNodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay': 'bool'
    }

    attribute_map = {
        'delay': 'delay'
    }

    def __init__(self, delay=None):
        r"""RestartNodeRequest

        The model defined in huaweicloud sdk

        :param delay: 实例节点是否延迟重启。默认false，立即重启。  - true: 延迟重启，实例节点将在运维时间窗内自动重启。 - false: 立即重启。
        :type delay: bool
        """
        
        

        self._delay = None
        self.discriminator = None

        if delay is not None:
            self.delay = delay

    @property
    def delay(self):
        r"""Gets the delay of this RestartNodeRequest.

        实例节点是否延迟重启。默认false，立即重启。  - true: 延迟重启，实例节点将在运维时间窗内自动重启。 - false: 立即重启。

        :return: The delay of this RestartNodeRequest.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this RestartNodeRequest.

        实例节点是否延迟重启。默认false，立即重启。  - true: 延迟重启，实例节点将在运维时间窗内自动重启。 - false: 立即重启。

        :param delay: The delay of this RestartNodeRequest.
        :type delay: bool
        """
        self._delay = delay

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
        if not isinstance(other, RestartNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
