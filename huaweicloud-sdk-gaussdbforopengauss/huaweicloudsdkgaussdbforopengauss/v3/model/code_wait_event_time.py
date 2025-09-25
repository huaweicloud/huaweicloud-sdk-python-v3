# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeWaitEventTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_time': 'int',
        'code_wait_event_time_details': 'EventTimeInfo'
    }

    attribute_map = {
        'all_time': 'all_time',
        'code_wait_event_time_details': 'code_wait_event_time_details'
    }

    def __init__(self, all_time=None, code_wait_event_time_details=None):
        r"""CodeWaitEventTime

        The model defined in huaweicloud sdk

        :param all_time: **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type all_time: int
        :param code_wait_event_time_details: 
        :type code_wait_event_time_details: :class:`huaweicloudsdkgaussdbforopengauss.v3.EventTimeInfo`
        """
        
        

        self._all_time = None
        self._code_wait_event_time_details = None
        self.discriminator = None

        self.all_time = all_time
        self.code_wait_event_time_details = code_wait_event_time_details

    @property
    def all_time(self):
        r"""Gets the all_time of this CodeWaitEventTime.

        **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The all_time of this CodeWaitEventTime.
        :rtype: int
        """
        return self._all_time

    @all_time.setter
    def all_time(self, all_time):
        r"""Sets the all_time of this CodeWaitEventTime.

        **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param all_time: The all_time of this CodeWaitEventTime.
        :type all_time: int
        """
        self._all_time = all_time

    @property
    def code_wait_event_time_details(self):
        r"""Gets the code_wait_event_time_details of this CodeWaitEventTime.

        :return: The code_wait_event_time_details of this CodeWaitEventTime.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.EventTimeInfo`
        """
        return self._code_wait_event_time_details

    @code_wait_event_time_details.setter
    def code_wait_event_time_details(self, code_wait_event_time_details):
        r"""Sets the code_wait_event_time_details of this CodeWaitEventTime.

        :param code_wait_event_time_details: The code_wait_event_time_details of this CodeWaitEventTime.
        :type code_wait_event_time_details: :class:`huaweicloudsdkgaussdbforopengauss.v3.EventTimeInfo`
        """
        self._code_wait_event_time_details = code_wait_event_time_details

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
        if not isinstance(other, CodeWaitEventTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
