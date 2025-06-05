# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInfoResponseDsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desired_num': 'int',
        'current_num': 'int',
        'ready_num': 'int'
    }

    attribute_map = {
        'desired_num': 'desired_num',
        'current_num': 'current_num',
        'ready_num': 'ready_num'
    }

    def __init__(self, desired_num=None, current_num=None, ready_num=None):
        r"""ClusterInfoResponseDsInfo

        The model defined in huaweicloud sdk

        :param desired_num: 目标数量
        :type desired_num: int
        :param current_num: 当前数量
        :type current_num: int
        :param ready_num: 就绪数量
        :type ready_num: int
        """
        
        

        self._desired_num = None
        self._current_num = None
        self._ready_num = None
        self.discriminator = None

        if desired_num is not None:
            self.desired_num = desired_num
        if current_num is not None:
            self.current_num = current_num
        if ready_num is not None:
            self.ready_num = ready_num

    @property
    def desired_num(self):
        r"""Gets the desired_num of this ClusterInfoResponseDsInfo.

        目标数量

        :return: The desired_num of this ClusterInfoResponseDsInfo.
        :rtype: int
        """
        return self._desired_num

    @desired_num.setter
    def desired_num(self, desired_num):
        r"""Sets the desired_num of this ClusterInfoResponseDsInfo.

        目标数量

        :param desired_num: The desired_num of this ClusterInfoResponseDsInfo.
        :type desired_num: int
        """
        self._desired_num = desired_num

    @property
    def current_num(self):
        r"""Gets the current_num of this ClusterInfoResponseDsInfo.

        当前数量

        :return: The current_num of this ClusterInfoResponseDsInfo.
        :rtype: int
        """
        return self._current_num

    @current_num.setter
    def current_num(self, current_num):
        r"""Sets the current_num of this ClusterInfoResponseDsInfo.

        当前数量

        :param current_num: The current_num of this ClusterInfoResponseDsInfo.
        :type current_num: int
        """
        self._current_num = current_num

    @property
    def ready_num(self):
        r"""Gets the ready_num of this ClusterInfoResponseDsInfo.

        就绪数量

        :return: The ready_num of this ClusterInfoResponseDsInfo.
        :rtype: int
        """
        return self._ready_num

    @ready_num.setter
    def ready_num(self, ready_num):
        r"""Sets the ready_num of this ClusterInfoResponseDsInfo.

        就绪数量

        :param ready_num: The ready_num of this ClusterInfoResponseDsInfo.
        :type ready_num: int
        """
        self._ready_num = ready_num

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
        if not isinstance(other, ClusterInfoResponseDsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
