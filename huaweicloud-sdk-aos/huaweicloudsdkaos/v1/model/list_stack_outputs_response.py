# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStackOutputsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'outputs': 'list[StackOutput]',
        'next_marker': 'str'
    }

    attribute_map = {
        'outputs': 'outputs',
        'next_marker': 'next_marker'
    }

    def __init__(self, outputs=None, next_marker=None):
        """ListStackOutputsResponse

        The model defined in huaweicloud sdk

        :param outputs: 堆栈输出
        :type outputs: list[:class:`huaweicloudsdkaos.v1.StackOutput`]
        :param next_marker: 下一页的标记信息
        :type next_marker: str
        """
        
        super(ListStackOutputsResponse, self).__init__()

        self._outputs = None
        self._next_marker = None
        self.discriminator = None

        if outputs is not None:
            self.outputs = outputs
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def outputs(self):
        """Gets the outputs of this ListStackOutputsResponse.

        堆栈输出

        :return: The outputs of this ListStackOutputsResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.StackOutput`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ListStackOutputsResponse.

        堆栈输出

        :param outputs: The outputs of this ListStackOutputsResponse.
        :type outputs: list[:class:`huaweicloudsdkaos.v1.StackOutput`]
        """
        self._outputs = outputs

    @property
    def next_marker(self):
        """Gets the next_marker of this ListStackOutputsResponse.

        下一页的标记信息

        :return: The next_marker of this ListStackOutputsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListStackOutputsResponse.

        下一页的标记信息

        :param next_marker: The next_marker of this ListStackOutputsResponse.
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
        if not isinstance(other, ListStackOutputsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
