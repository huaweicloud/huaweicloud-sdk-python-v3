# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteMqsInstanceTopicResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics': 'list[DeleteMqsInstanceTopicRespTopics]'
    }

    attribute_map = {
        'topics': 'topics'
    }

    def __init__(self, topics=None):
        """DeleteMqsInstanceTopicResponse

        The model defined in huaweicloud sdk

        :param topics: Topic列表。
        :type topics: list[:class:`huaweicloudsdkroma.v2.DeleteMqsInstanceTopicRespTopics`]
        """
        
        super(DeleteMqsInstanceTopicResponse, self).__init__()

        self._topics = None
        self.discriminator = None

        if topics is not None:
            self.topics = topics

    @property
    def topics(self):
        """Gets the topics of this DeleteMqsInstanceTopicResponse.

        Topic列表。

        :return: The topics of this DeleteMqsInstanceTopicResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.DeleteMqsInstanceTopicRespTopics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this DeleteMqsInstanceTopicResponse.

        Topic列表。

        :param topics: The topics of this DeleteMqsInstanceTopicResponse.
        :type topics: list[:class:`huaweicloudsdkroma.v2.DeleteMqsInstanceTopicRespTopics`]
        """
        self._topics = topics

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
        if not isinstance(other, DeleteMqsInstanceTopicResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
