# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppCallbacks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'push_callback': 'AppCallbackUrl',
        'record_callback': 'AppCallbackUrl'
    }

    attribute_map = {
        'push_callback': 'push_callback',
        'record_callback': 'record_callback'
    }

    def __init__(self, push_callback=None, record_callback=None):
        r"""AppCallbacks

        The model defined in huaweicloud sdk

        :param push_callback: 
        :type push_callback: :class:`huaweicloudsdkcloudrtc.v2.AppCallbackUrl`
        :param record_callback: 
        :type record_callback: :class:`huaweicloudsdkcloudrtc.v2.AppCallbackUrl`
        """
        
        

        self._push_callback = None
        self._record_callback = None
        self.discriminator = None

        if push_callback is not None:
            self.push_callback = push_callback
        if record_callback is not None:
            self.record_callback = record_callback

    @property
    def push_callback(self):
        r"""Gets the push_callback of this AppCallbacks.

        :return: The push_callback of this AppCallbacks.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.AppCallbackUrl`
        """
        return self._push_callback

    @push_callback.setter
    def push_callback(self, push_callback):
        r"""Sets the push_callback of this AppCallbacks.

        :param push_callback: The push_callback of this AppCallbacks.
        :type push_callback: :class:`huaweicloudsdkcloudrtc.v2.AppCallbackUrl`
        """
        self._push_callback = push_callback

    @property
    def record_callback(self):
        r"""Gets the record_callback of this AppCallbacks.

        :return: The record_callback of this AppCallbacks.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.AppCallbackUrl`
        """
        return self._record_callback

    @record_callback.setter
    def record_callback(self, record_callback):
        r"""Sets the record_callback of this AppCallbacks.

        :param record_callback: The record_callback of this AppCallbacks.
        :type record_callback: :class:`huaweicloudsdkcloudrtc.v2.AppCallbackUrl`
        """
        self._record_callback = record_callback

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
        if not isinstance(other, AppCallbacks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
