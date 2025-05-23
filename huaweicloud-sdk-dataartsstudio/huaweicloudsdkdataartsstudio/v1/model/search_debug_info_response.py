# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDebugInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'publish_messages': 'list[ApiPublishDTO]'
    }

    attribute_map = {
        'total': 'total',
        'publish_messages': 'publish_messages'
    }

    def __init__(self, total=None, publish_messages=None):
        r"""SearchDebugInfoResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param publish_messages: 发布信息列表
        :type publish_messages: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiPublishDTO`]
        """
        
        super(SearchDebugInfoResponse, self).__init__()

        self._total = None
        self._publish_messages = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if publish_messages is not None:
            self.publish_messages = publish_messages

    @property
    def total(self):
        r"""Gets the total of this SearchDebugInfoResponse.

        总数

        :return: The total of this SearchDebugInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SearchDebugInfoResponse.

        总数

        :param total: The total of this SearchDebugInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def publish_messages(self):
        r"""Gets the publish_messages of this SearchDebugInfoResponse.

        发布信息列表

        :return: The publish_messages of this SearchDebugInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiPublishDTO`]
        """
        return self._publish_messages

    @publish_messages.setter
    def publish_messages(self, publish_messages):
        r"""Sets the publish_messages of this SearchDebugInfoResponse.

        发布信息列表

        :param publish_messages: The publish_messages of this SearchDebugInfoResponse.
        :type publish_messages: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiPublishDTO`]
        """
        self._publish_messages = publish_messages

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
        if not isinstance(other, SearchDebugInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
