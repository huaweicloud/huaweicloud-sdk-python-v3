# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConsumerGroupOfTopicRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'topic': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic': 'topic',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, topic=None, limit=None, offset=None):
        r"""ListConsumerGroupOfTopicRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param topic: 主题名称。
        :type topic: str
        :param limit: 当次查询返回的最大个数，默认值为10，取值范围为1~50。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._topic = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListConsumerGroupOfTopicRequest.

        实例ID。

        :return: The instance_id of this ListConsumerGroupOfTopicRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListConsumerGroupOfTopicRequest.

        实例ID。

        :param instance_id: The instance_id of this ListConsumerGroupOfTopicRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        r"""Gets the topic of this ListConsumerGroupOfTopicRequest.

        主题名称。

        :return: The topic of this ListConsumerGroupOfTopicRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ListConsumerGroupOfTopicRequest.

        主题名称。

        :param topic: The topic of this ListConsumerGroupOfTopicRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def limit(self):
        r"""Gets the limit of this ListConsumerGroupOfTopicRequest.

        当次查询返回的最大个数，默认值为10，取值范围为1~50。

        :return: The limit of this ListConsumerGroupOfTopicRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConsumerGroupOfTopicRequest.

        当次查询返回的最大个数，默认值为10，取值范围为1~50。

        :param limit: The limit of this ListConsumerGroupOfTopicRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListConsumerGroupOfTopicRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListConsumerGroupOfTopicRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConsumerGroupOfTopicRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListConsumerGroupOfTopicRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListConsumerGroupOfTopicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
