# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentProbe:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'delay': 'int',
        'timeout': 'int',
        'parameters': 'ProbeParameter'
    }

    attribute_map = {
        'type': 'type',
        'delay': 'delay',
        'timeout': 'timeout',
        'parameters': 'parameters'
    }

    def __init__(self, type=None, delay=None, timeout=None, parameters=None):
        r"""ComponentProbe

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param delay: 表示启动后多久开始探测
        :type delay: int
        :param timeout: 表示探测超时时间
        :type timeout: int
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkservicestage.v2.ProbeParameter`
        """
        
        

        self._type = None
        self._delay = None
        self._timeout = None
        self._parameters = None
        self.discriminator = None

        self.type = type
        if delay is not None:
            self.delay = delay
        if timeout is not None:
            self.timeout = timeout
        self.parameters = parameters

    @property
    def type(self):
        r"""Gets the type of this ComponentProbe.

        :return: The type of this ComponentProbe.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ComponentProbe.

        :param type: The type of this ComponentProbe.
        :type type: str
        """
        self._type = type

    @property
    def delay(self):
        r"""Gets the delay of this ComponentProbe.

        表示启动后多久开始探测

        :return: The delay of this ComponentProbe.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this ComponentProbe.

        表示启动后多久开始探测

        :param delay: The delay of this ComponentProbe.
        :type delay: int
        """
        self._delay = delay

    @property
    def timeout(self):
        r"""Gets the timeout of this ComponentProbe.

        表示探测超时时间

        :return: The timeout of this ComponentProbe.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ComponentProbe.

        表示探测超时时间

        :param timeout: The timeout of this ComponentProbe.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def parameters(self):
        r"""Gets the parameters of this ComponentProbe.

        :return: The parameters of this ComponentProbe.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ProbeParameter`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ComponentProbe.

        :param parameters: The parameters of this ComponentProbe.
        :type parameters: :class:`huaweicloudsdkservicestage.v2.ProbeParameter`
        """
        self._parameters = parameters

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
        if not isinstance(other, ComponentProbe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
