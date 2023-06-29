# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoLogoutOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sbc_logout_waiting_time': 'int'
    }

    attribute_map = {
        'sbc_logout_waiting_time': 'sbc_logout_waiting_time'
    }

    def __init__(self, sbc_logout_waiting_time=None):
        """AutoLogoutOptions

        The model defined in huaweicloud sdk

        :param sbc_logout_waiting_time: 会话断连保留时长（分钟）
        :type sbc_logout_waiting_time: int
        """
        
        

        self._sbc_logout_waiting_time = None
        self.discriminator = None

        if sbc_logout_waiting_time is not None:
            self.sbc_logout_waiting_time = sbc_logout_waiting_time

    @property
    def sbc_logout_waiting_time(self):
        """Gets the sbc_logout_waiting_time of this AutoLogoutOptions.

        会话断连保留时长（分钟）

        :return: The sbc_logout_waiting_time of this AutoLogoutOptions.
        :rtype: int
        """
        return self._sbc_logout_waiting_time

    @sbc_logout_waiting_time.setter
    def sbc_logout_waiting_time(self, sbc_logout_waiting_time):
        """Sets the sbc_logout_waiting_time of this AutoLogoutOptions.

        会话断连保留时长（分钟）

        :param sbc_logout_waiting_time: The sbc_logout_waiting_time of this AutoLogoutOptions.
        :type sbc_logout_waiting_time: int
        """
        self._sbc_logout_waiting_time = sbc_logout_waiting_time

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
        if not isinstance(other, AutoLogoutOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
