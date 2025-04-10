# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionsByTopicRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'offset': 'int',
        'limit': 'int',
        'fuzzy_remark': 'str'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'offset': 'offset',
        'limit': 'limit',
        'fuzzy_remark': 'fuzzy_remark'
    }

    def __init__(self, topic_urn=None, offset=None, limit=None, fuzzy_remark=None):
        r"""ListSubscriptionsByTopicRequest

        The model defined in huaweicloud sdk

        :param topic_urn: Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。
        :type topic_urn: str
        :param offset: 偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit: 查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        :param fuzzy_remark: 检索的订阅备注字段，模糊匹配。最大长度限制为128字节。
        :type fuzzy_remark: str
        """
        
        

        self._topic_urn = None
        self._offset = None
        self._limit = None
        self._fuzzy_remark = None
        self.discriminator = None

        self.topic_urn = topic_urn
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if fuzzy_remark is not None:
            self.fuzzy_remark = fuzzy_remark

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ListSubscriptionsByTopicRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :return: The topic_urn of this ListSubscriptionsByTopicRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ListSubscriptionsByTopicRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :param topic_urn: The topic_urn of this ListSubscriptionsByTopicRequest.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def offset(self):
        r"""Gets the offset of this ListSubscriptionsByTopicRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListSubscriptionsByTopicRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubscriptionsByTopicRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListSubscriptionsByTopicRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubscriptionsByTopicRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListSubscriptionsByTopicRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubscriptionsByTopicRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListSubscriptionsByTopicRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fuzzy_remark(self):
        r"""Gets the fuzzy_remark of this ListSubscriptionsByTopicRequest.

        检索的订阅备注字段，模糊匹配。最大长度限制为128字节。

        :return: The fuzzy_remark of this ListSubscriptionsByTopicRequest.
        :rtype: str
        """
        return self._fuzzy_remark

    @fuzzy_remark.setter
    def fuzzy_remark(self, fuzzy_remark):
        r"""Sets the fuzzy_remark of this ListSubscriptionsByTopicRequest.

        检索的订阅备注字段，模糊匹配。最大长度限制为128字节。

        :param fuzzy_remark: The fuzzy_remark of this ListSubscriptionsByTopicRequest.
        :type fuzzy_remark: str
        """
        self._fuzzy_remark = fuzzy_remark

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
        if not isinstance(other, ListSubscriptionsByTopicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
