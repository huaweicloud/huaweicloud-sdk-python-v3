# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStackEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_events': 'list[StackEventResponse]',
        'next_marker': 'str'
    }

    attribute_map = {
        'stack_events': 'stack_events',
        'next_marker': 'next_marker'
    }

    def __init__(self, stack_events=None, next_marker=None):
        """ListStackEventsResponse

        The model defined in huaweicloud sdk

        :param stack_events: 栈的更新状态
        :type stack_events: list[:class:`huaweicloudsdkaos.v1.StackEventResponse`]
        :param next_marker: 当一页无法发回所有的细节，将返回next_marker，客户可以继续调用list-stack-events并给与next_marker来继续读取下页
        :type next_marker: str
        """
        
        super(ListStackEventsResponse, self).__init__()

        self._stack_events = None
        self._next_marker = None
        self.discriminator = None

        if stack_events is not None:
            self.stack_events = stack_events
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def stack_events(self):
        """Gets the stack_events of this ListStackEventsResponse.

        栈的更新状态

        :return: The stack_events of this ListStackEventsResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.StackEventResponse`]
        """
        return self._stack_events

    @stack_events.setter
    def stack_events(self, stack_events):
        """Sets the stack_events of this ListStackEventsResponse.

        栈的更新状态

        :param stack_events: The stack_events of this ListStackEventsResponse.
        :type stack_events: list[:class:`huaweicloudsdkaos.v1.StackEventResponse`]
        """
        self._stack_events = stack_events

    @property
    def next_marker(self):
        """Gets the next_marker of this ListStackEventsResponse.

        当一页无法发回所有的细节，将返回next_marker，客户可以继续调用list-stack-events并给与next_marker来继续读取下页

        :return: The next_marker of this ListStackEventsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListStackEventsResponse.

        当一页无法发回所有的细节，将返回next_marker，客户可以继续调用list-stack-events并给与next_marker来继续读取下页

        :param next_marker: The next_marker of this ListStackEventsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListStackEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
