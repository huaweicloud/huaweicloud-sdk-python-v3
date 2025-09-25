# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceWaitEventTime:

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
        'resource_wait_event_time_details': 'ResourceWaitEvenTimeDetails',
        'other_time': 'int'
    }

    attribute_map = {
        'all_time': 'all_time',
        'resource_wait_event_time_details': 'resource_wait_event_time_details',
        'other_time': 'other_time'
    }

    def __init__(self, all_time=None, resource_wait_event_time_details=None, other_time=None):
        r"""ResourceWaitEventTime

        The model defined in huaweicloud sdk

        :param all_time: **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type all_time: int
        :param resource_wait_event_time_details: 
        :type resource_wait_event_time_details: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceWaitEvenTimeDetails`
        :param other_time: **参数解释**: 资源类等待事件外耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type other_time: int
        """
        
        

        self._all_time = None
        self._resource_wait_event_time_details = None
        self._other_time = None
        self.discriminator = None

        self.all_time = all_time
        self.resource_wait_event_time_details = resource_wait_event_time_details
        if other_time is not None:
            self.other_time = other_time

    @property
    def all_time(self):
        r"""Gets the all_time of this ResourceWaitEventTime.

        **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The all_time of this ResourceWaitEventTime.
        :rtype: int
        """
        return self._all_time

    @all_time.setter
    def all_time(self, all_time):
        r"""Sets the all_time of this ResourceWaitEventTime.

        **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param all_time: The all_time of this ResourceWaitEventTime.
        :type all_time: int
        """
        self._all_time = all_time

    @property
    def resource_wait_event_time_details(self):
        r"""Gets the resource_wait_event_time_details of this ResourceWaitEventTime.

        :return: The resource_wait_event_time_details of this ResourceWaitEventTime.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceWaitEvenTimeDetails`
        """
        return self._resource_wait_event_time_details

    @resource_wait_event_time_details.setter
    def resource_wait_event_time_details(self, resource_wait_event_time_details):
        r"""Sets the resource_wait_event_time_details of this ResourceWaitEventTime.

        :param resource_wait_event_time_details: The resource_wait_event_time_details of this ResourceWaitEventTime.
        :type resource_wait_event_time_details: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceWaitEvenTimeDetails`
        """
        self._resource_wait_event_time_details = resource_wait_event_time_details

    @property
    def other_time(self):
        r"""Gets the other_time of this ResourceWaitEventTime.

        **参数解释**: 资源类等待事件外耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The other_time of this ResourceWaitEventTime.
        :rtype: int
        """
        return self._other_time

    @other_time.setter
    def other_time(self, other_time):
        r"""Sets the other_time of this ResourceWaitEventTime.

        **参数解释**: 资源类等待事件外耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param other_time: The other_time of this ResourceWaitEventTime.
        :type other_time: int
        """
        self._other_time = other_time

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
        if not isinstance(other, ResourceWaitEventTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
