# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Curve:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_in': 'float',
        'out': 'float',
        'time': 'int'
    }

    attribute_map = {
        '_in': 'in',
        'out': 'out',
        'time': 'time'
    }

    def __init__(self, _in=None, out=None, time=None):
        r"""Curve

        The model defined in huaweicloud sdk

        :param _in: 入带宽
        :type _in: float
        :param out: 出带宽
        :type out: float
        :param time: 时间戳
        :type time: int
        """
        
        

        self.__in = None
        self._out = None
        self._time = None
        self.discriminator = None

        if _in is not None:
            self._in = _in
        if out is not None:
            self.out = out
        if time is not None:
            self.time = time

    @property
    def _in(self):
        r"""Gets the _in of this Curve.

        入带宽

        :return: The _in of this Curve.
        :rtype: float
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        r"""Sets the _in of this Curve.

        入带宽

        :param _in: The _in of this Curve.
        :type _in: float
        """
        self.__in = _in

    @property
    def out(self):
        r"""Gets the out of this Curve.

        出带宽

        :return: The out of this Curve.
        :rtype: float
        """
        return self._out

    @out.setter
    def out(self, out):
        r"""Sets the out of this Curve.

        出带宽

        :param out: The out of this Curve.
        :type out: float
        """
        self._out = out

    @property
    def time(self):
        r"""Gets the time of this Curve.

        时间戳

        :return: The time of this Curve.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Curve.

        时间戳

        :param time: The time of this Curve.
        :type time: int
        """
        self._time = time

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
        if not isinstance(other, Curve):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
