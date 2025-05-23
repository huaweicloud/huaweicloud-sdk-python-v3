# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopJobActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_force_stop': 'bool'
    }

    attribute_map = {
        'is_force_stop': 'is_force_stop'
    }

    def __init__(self, is_force_stop=None):
        r"""StopJobActionReq

        The model defined in huaweicloud sdk

        :param is_force_stop: 强制结束任务时取值true，默认false。
        :type is_force_stop: bool
        """
        
        

        self._is_force_stop = None
        self.discriminator = None

        if is_force_stop is not None:
            self.is_force_stop = is_force_stop

    @property
    def is_force_stop(self):
        r"""Gets the is_force_stop of this StopJobActionReq.

        强制结束任务时取值true，默认false。

        :return: The is_force_stop of this StopJobActionReq.
        :rtype: bool
        """
        return self._is_force_stop

    @is_force_stop.setter
    def is_force_stop(self, is_force_stop):
        r"""Sets the is_force_stop of this StopJobActionReq.

        强制结束任务时取值true，默认false。

        :param is_force_stop: The is_force_stop of this StopJobActionReq.
        :type is_force_stop: bool
        """
        self._is_force_stop = is_force_stop

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
        if not isinstance(other, StopJobActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
