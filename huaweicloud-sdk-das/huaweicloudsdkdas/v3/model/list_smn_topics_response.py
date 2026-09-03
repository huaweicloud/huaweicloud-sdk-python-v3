# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmnTopicsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'request_id': 'str',
        'topic_count': 'int',
        'topics': 'list[SmnTopicInfo]'
    }

    attribute_map = {
        'success': 'success',
        'request_id': 'request_id',
        'topic_count': 'topic_count',
        'topics': 'topics'
    }

    def __init__(self, success=None, request_id=None, topic_count=None, topics=None):
        r"""ListSmnTopicsResponse

        The model defined in huaweicloud sdk

        :param success: 是否成功
        :type success: bool
        :param request_id: 请求的唯一标识ID
        :type request_id: str
        :param topic_count: 返回的Topic个数
        :type topic_count: int
        :param topics: 主题列表
        :type topics: list[:class:`huaweicloudsdkdas.v3.SmnTopicInfo`]
        """
        
        super().__init__()

        self._success = None
        self._request_id = None
        self._topic_count = None
        self._topics = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if request_id is not None:
            self.request_id = request_id
        if topic_count is not None:
            self.topic_count = topic_count
        if topics is not None:
            self.topics = topics

    @property
    def success(self):
        r"""Gets the success of this ListSmnTopicsResponse.

        是否成功

        :return: The success of this ListSmnTopicsResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListSmnTopicsResponse.

        是否成功

        :param success: The success of this ListSmnTopicsResponse.
        :type success: bool
        """
        self._success = success

    @property
    def request_id(self):
        r"""Gets the request_id of this ListSmnTopicsResponse.

        请求的唯一标识ID

        :return: The request_id of this ListSmnTopicsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListSmnTopicsResponse.

        请求的唯一标识ID

        :param request_id: The request_id of this ListSmnTopicsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def topic_count(self):
        r"""Gets the topic_count of this ListSmnTopicsResponse.

        返回的Topic个数

        :return: The topic_count of this ListSmnTopicsResponse.
        :rtype: int
        """
        return self._topic_count

    @topic_count.setter
    def topic_count(self, topic_count):
        r"""Sets the topic_count of this ListSmnTopicsResponse.

        返回的Topic个数

        :param topic_count: The topic_count of this ListSmnTopicsResponse.
        :type topic_count: int
        """
        self._topic_count = topic_count

    @property
    def topics(self):
        r"""Gets the topics of this ListSmnTopicsResponse.

        主题列表

        :return: The topics of this ListSmnTopicsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SmnTopicInfo`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ListSmnTopicsResponse.

        主题列表

        :param topics: The topics of this ListSmnTopicsResponse.
        :type topics: list[:class:`huaweicloudsdkdas.v3.SmnTopicInfo`]
        """
        self._topics = topics

    def to_dict(self):
        import warnings
        warnings.warn("ListSmnTopicsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSmnTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
