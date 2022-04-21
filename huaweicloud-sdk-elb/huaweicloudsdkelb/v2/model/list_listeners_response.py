# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListListenersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'listeners': 'list[ListenerResp]'
    }

    attribute_map = {
        'listeners': 'listeners'
    }

    def __init__(self, listeners=None):
        """ListListenersResponse

        The model defined in huaweicloud sdk

        :param listeners: 监听器对象列表
        :type listeners: list[:class:`huaweicloudsdkelb.v2.ListenerResp`]
        """
        
        super(ListListenersResponse, self).__init__()

        self._listeners = None
        self.discriminator = None

        if listeners is not None:
            self.listeners = listeners

    @property
    def listeners(self):
        """Gets the listeners of this ListListenersResponse.

        监听器对象列表

        :return: The listeners of this ListListenersResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v2.ListenerResp`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this ListListenersResponse.

        监听器对象列表

        :param listeners: The listeners of this ListListenersResponse.
        :type listeners: list[:class:`huaweicloudsdkelb.v2.ListenerResp`]
        """
        self._listeners = listeners

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
        if not isinstance(other, ListListenersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
