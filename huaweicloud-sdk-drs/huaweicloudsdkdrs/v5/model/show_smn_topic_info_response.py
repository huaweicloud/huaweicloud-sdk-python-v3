# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmnTopicInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics': 'list[SmnTopicInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'topics': 'topics',
        'total_count': 'total_count'
    }

    def __init__(self, topics=None, total_count=None):
        r"""ShowSmnTopicInfoResponse

        The model defined in huaweicloud sdk

        :param topics: 主题信息
        :type topics: list[:class:`huaweicloudsdkdrs.v5.SmnTopicInfo`]
        :param total_count: 主题总数
        :type total_count: int
        """
        
        super().__init__()

        self._topics = None
        self._total_count = None
        self.discriminator = None

        if topics is not None:
            self.topics = topics
        if total_count is not None:
            self.total_count = total_count

    @property
    def topics(self):
        r"""Gets the topics of this ShowSmnTopicInfoResponse.

        主题信息

        :return: The topics of this ShowSmnTopicInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.SmnTopicInfo`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ShowSmnTopicInfoResponse.

        主题信息

        :param topics: The topics of this ShowSmnTopicInfoResponse.
        :type topics: list[:class:`huaweicloudsdkdrs.v5.SmnTopicInfo`]
        """
        self._topics = topics

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowSmnTopicInfoResponse.

        主题总数

        :return: The total_count of this ShowSmnTopicInfoResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowSmnTopicInfoResponse.

        主题总数

        :param total_count: The total_count of this ShowSmnTopicInfoResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowSmnTopicInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSmnTopicInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
