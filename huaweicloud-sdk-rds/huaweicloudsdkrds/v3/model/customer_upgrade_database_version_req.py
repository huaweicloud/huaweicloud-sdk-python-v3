# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerUpgradeDatabaseVersionReq:

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
        """CustomerUpgradeDatabaseVersionReq

        The model defined in huaweicloud sdk

        :param delay: 是否延迟至可维护时间段内升级。 取值范围： - true：延迟升级。表示实例将在设置的可维护时间段内升级。 - false：立即升级，默认该方式。
        :type delay: bool
        """
        
        

        self._delay = None
        self.discriminator = None

        if delay is not None:
            self.delay = delay

    @property
    def delay(self):
        """Gets the delay of this CustomerUpgradeDatabaseVersionReq.

        是否延迟至可维护时间段内升级。 取值范围： - true：延迟升级。表示实例将在设置的可维护时间段内升级。 - false：立即升级，默认该方式。

        :return: The delay of this CustomerUpgradeDatabaseVersionReq.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this CustomerUpgradeDatabaseVersionReq.

        是否延迟至可维护时间段内升级。 取值范围： - true：延迟升级。表示实例将在设置的可维护时间段内升级。 - false：立即升级，默认该方式。

        :param delay: The delay of this CustomerUpgradeDatabaseVersionReq.
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
        if not isinstance(other, CustomerUpgradeDatabaseVersionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
