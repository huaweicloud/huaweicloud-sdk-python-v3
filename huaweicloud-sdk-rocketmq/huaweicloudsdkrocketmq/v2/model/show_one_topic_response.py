# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOneTopicResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_read_queue_num': 'float',
        'total_write_queue_num': 'float',
        'permission': 'str',
        'brokers': 'list[TopicBrokers]'
    }

    attribute_map = {
        'total_read_queue_num': 'total_read_queue_num',
        'total_write_queue_num': 'total_write_queue_num',
        'permission': 'permission',
        'brokers': 'brokers'
    }

    def __init__(self, total_read_queue_num=None, total_write_queue_num=None, permission=None, brokers=None):
        """ShowOneTopicResponse

        The model defined in huaweicloud sdk

        :param total_read_queue_num: 总读队列个数。
        :type total_read_queue_num: float
        :param total_write_queue_num: 总写队列个数。
        :type total_write_queue_num: float
        :param permission: 权限。
        :type permission: str
        :param brokers: 关联的代理。
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.TopicBrokers`]
        """
        
        super(ShowOneTopicResponse, self).__init__()

        self._total_read_queue_num = None
        self._total_write_queue_num = None
        self._permission = None
        self._brokers = None
        self.discriminator = None

        if total_read_queue_num is not None:
            self.total_read_queue_num = total_read_queue_num
        if total_write_queue_num is not None:
            self.total_write_queue_num = total_write_queue_num
        if permission is not None:
            self.permission = permission
        if brokers is not None:
            self.brokers = brokers

    @property
    def total_read_queue_num(self):
        """Gets the total_read_queue_num of this ShowOneTopicResponse.

        总读队列个数。

        :return: The total_read_queue_num of this ShowOneTopicResponse.
        :rtype: float
        """
        return self._total_read_queue_num

    @total_read_queue_num.setter
    def total_read_queue_num(self, total_read_queue_num):
        """Sets the total_read_queue_num of this ShowOneTopicResponse.

        总读队列个数。

        :param total_read_queue_num: The total_read_queue_num of this ShowOneTopicResponse.
        :type total_read_queue_num: float
        """
        self._total_read_queue_num = total_read_queue_num

    @property
    def total_write_queue_num(self):
        """Gets the total_write_queue_num of this ShowOneTopicResponse.

        总写队列个数。

        :return: The total_write_queue_num of this ShowOneTopicResponse.
        :rtype: float
        """
        return self._total_write_queue_num

    @total_write_queue_num.setter
    def total_write_queue_num(self, total_write_queue_num):
        """Sets the total_write_queue_num of this ShowOneTopicResponse.

        总写队列个数。

        :param total_write_queue_num: The total_write_queue_num of this ShowOneTopicResponse.
        :type total_write_queue_num: float
        """
        self._total_write_queue_num = total_write_queue_num

    @property
    def permission(self):
        """Gets the permission of this ShowOneTopicResponse.

        权限。

        :return: The permission of this ShowOneTopicResponse.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ShowOneTopicResponse.

        权限。

        :param permission: The permission of this ShowOneTopicResponse.
        :type permission: str
        """
        self._permission = permission

    @property
    def brokers(self):
        """Gets the brokers of this ShowOneTopicResponse.

        关联的代理。

        :return: The brokers of this ShowOneTopicResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.TopicBrokers`]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this ShowOneTopicResponse.

        关联的代理。

        :param brokers: The brokers of this ShowOneTopicResponse.
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.TopicBrokers`]
        """
        self._brokers = brokers

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
        if not isinstance(other, ShowOneTopicResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
