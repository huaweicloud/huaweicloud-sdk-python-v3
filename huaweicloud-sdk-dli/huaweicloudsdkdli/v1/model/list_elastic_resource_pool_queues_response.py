# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListElasticResourcePoolQueuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'queues': 'list[QueueInfo]',
        'count': 'int'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'queues': 'queues',
        'count': 'count'
    }

    def __init__(self, is_success=None, message=None, queues=None, count=None):
        """ListElasticResourcePoolQueuesResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功
        :type is_success: bool
        :param message: 请求消息
        :type message: str
        :param queues: 该弹性资源池下所有queue信息及队列扩缩容策略信息。
        :type queues: list[:class:`huaweicloudsdkdli.v1.QueueInfo`]
        :param count: 该资源池下关联的队列数量
        :type count: int
        """
        
        super(ListElasticResourcePoolQueuesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._queues = None
        self._count = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if queues is not None:
            self.queues = queues
        if count is not None:
            self.count = count

    @property
    def is_success(self):
        """Gets the is_success of this ListElasticResourcePoolQueuesResponse.

        是否成功

        :return: The is_success of this ListElasticResourcePoolQueuesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListElasticResourcePoolQueuesResponse.

        是否成功

        :param is_success: The is_success of this ListElasticResourcePoolQueuesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListElasticResourcePoolQueuesResponse.

        请求消息

        :return: The message of this ListElasticResourcePoolQueuesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListElasticResourcePoolQueuesResponse.

        请求消息

        :param message: The message of this ListElasticResourcePoolQueuesResponse.
        :type message: str
        """
        self._message = message

    @property
    def queues(self):
        """Gets the queues of this ListElasticResourcePoolQueuesResponse.

        该弹性资源池下所有queue信息及队列扩缩容策略信息。

        :return: The queues of this ListElasticResourcePoolQueuesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.QueueInfo`]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this ListElasticResourcePoolQueuesResponse.

        该弹性资源池下所有queue信息及队列扩缩容策略信息。

        :param queues: The queues of this ListElasticResourcePoolQueuesResponse.
        :type queues: list[:class:`huaweicloudsdkdli.v1.QueueInfo`]
        """
        self._queues = queues

    @property
    def count(self):
        """Gets the count of this ListElasticResourcePoolQueuesResponse.

        该资源池下关联的队列数量

        :return: The count of this ListElasticResourcePoolQueuesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListElasticResourcePoolQueuesResponse.

        该资源池下关联的队列数量

        :param count: The count of this ListElasticResourcePoolQueuesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListElasticResourcePoolQueuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
