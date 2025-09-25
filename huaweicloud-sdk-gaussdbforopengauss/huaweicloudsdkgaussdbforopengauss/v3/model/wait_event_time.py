# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WaitEventTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_wait_event_time': 'CodeWaitEventTime',
        'resource_wait_event_time': 'ResourceWaitEventTime'
    }

    attribute_map = {
        'code_wait_event_time': 'code_wait_event_time',
        'resource_wait_event_time': 'resource_wait_event_time'
    }

    def __init__(self, code_wait_event_time=None, resource_wait_event_time=None):
        r"""WaitEventTime

        The model defined in huaweicloud sdk

        :param code_wait_event_time: 
        :type code_wait_event_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.CodeWaitEventTime`
        :param resource_wait_event_time: 
        :type resource_wait_event_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceWaitEventTime`
        """
        
        

        self._code_wait_event_time = None
        self._resource_wait_event_time = None
        self.discriminator = None

        self.code_wait_event_time = code_wait_event_time
        self.resource_wait_event_time = resource_wait_event_time

    @property
    def code_wait_event_time(self):
        r"""Gets the code_wait_event_time of this WaitEventTime.

        :return: The code_wait_event_time of this WaitEventTime.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CodeWaitEventTime`
        """
        return self._code_wait_event_time

    @code_wait_event_time.setter
    def code_wait_event_time(self, code_wait_event_time):
        r"""Sets the code_wait_event_time of this WaitEventTime.

        :param code_wait_event_time: The code_wait_event_time of this WaitEventTime.
        :type code_wait_event_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.CodeWaitEventTime`
        """
        self._code_wait_event_time = code_wait_event_time

    @property
    def resource_wait_event_time(self):
        r"""Gets the resource_wait_event_time of this WaitEventTime.

        :return: The resource_wait_event_time of this WaitEventTime.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceWaitEventTime`
        """
        return self._resource_wait_event_time

    @resource_wait_event_time.setter
    def resource_wait_event_time(self, resource_wait_event_time):
        r"""Sets the resource_wait_event_time of this WaitEventTime.

        :param resource_wait_event_time: The resource_wait_event_time of this WaitEventTime.
        :type resource_wait_event_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceWaitEventTime`
        """
        self._resource_wait_event_time = resource_wait_event_time

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
        if not isinstance(other, WaitEventTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
