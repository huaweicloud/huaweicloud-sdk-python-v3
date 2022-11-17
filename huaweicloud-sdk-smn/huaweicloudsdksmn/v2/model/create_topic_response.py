# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTopicResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'topic_urn': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, request_id=None, topic_urn=None):
        """CreateTopicResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param topic_urn: Topic的唯一的资源标识，可通过查询主题列表获取该标识。
        :type topic_urn: str
        """
        
        super(CreateTopicResponse, self).__init__()

        self._request_id = None
        self._topic_urn = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if topic_urn is not None:
            self.topic_urn = topic_urn

    @property
    def request_id(self):
        """Gets the request_id of this CreateTopicResponse.

        请求的唯一标识ID。

        :return: The request_id of this CreateTopicResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateTopicResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this CreateTopicResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def topic_urn(self):
        """Gets the topic_urn of this CreateTopicResponse.

        Topic的唯一的资源标识，可通过查询主题列表获取该标识。

        :return: The topic_urn of this CreateTopicResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this CreateTopicResponse.

        Topic的唯一的资源标识，可通过查询主题列表获取该标识。

        :param topic_urn: The topic_urn of this CreateTopicResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, CreateTopicResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
