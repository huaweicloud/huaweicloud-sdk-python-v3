# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStacksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack': 'StacksTags',
        'status': 'str'
    }

    attribute_map = {
        'stack': 'stack',
        'status': 'status'
    }

    def __init__(self, stack=None, status=None):
        """ListStacksResponse

        The model defined in huaweicloud sdk

        :param stack: 
        :type stack: :class:`huaweicloudsdkcloudide.v2.StacksTags`
        :param status: 状态
        :type status: str
        """
        
        super(ListStacksResponse, self).__init__()

        self._stack = None
        self._status = None
        self.discriminator = None

        if stack is not None:
            self.stack = stack
        if status is not None:
            self.status = status

    @property
    def stack(self):
        """Gets the stack of this ListStacksResponse.

        :return: The stack of this ListStacksResponse.
        :rtype: :class:`huaweicloudsdkcloudide.v2.StacksTags`
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        """Sets the stack of this ListStacksResponse.

        :param stack: The stack of this ListStacksResponse.
        :type stack: :class:`huaweicloudsdkcloudide.v2.StacksTags`
        """
        self._stack = stack

    @property
    def status(self):
        """Gets the status of this ListStacksResponse.

        状态

        :return: The status of this ListStacksResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListStacksResponse.

        状态

        :param status: The status of this ListStacksResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListStacksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
