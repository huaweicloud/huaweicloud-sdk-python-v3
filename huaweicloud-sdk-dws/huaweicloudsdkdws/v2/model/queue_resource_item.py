# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueResourceItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'queue_resources': 'list[WorkloadResourceItem]'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'queue_resources': 'queue_resources'
    }

    def __init__(self, queue_name=None, queue_resources=None):
        """QueueResourceItem

        The model defined in huaweicloud sdk

        :param queue_name: 资源池名称。
        :type queue_name: str
        :param queue_resources: 资源配置队列。
        :type queue_resources: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        
        

        self._queue_name = None
        self._queue_resources = None
        self.discriminator = None

        self.queue_name = queue_name
        self.queue_resources = queue_resources

    @property
    def queue_name(self):
        """Gets the queue_name of this QueueResourceItem.

        资源池名称。

        :return: The queue_name of this QueueResourceItem.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this QueueResourceItem.

        资源池名称。

        :param queue_name: The queue_name of this QueueResourceItem.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def queue_resources(self):
        """Gets the queue_resources of this QueueResourceItem.

        资源配置队列。

        :return: The queue_resources of this QueueResourceItem.
        :rtype: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        return self._queue_resources

    @queue_resources.setter
    def queue_resources(self, queue_resources):
        """Sets the queue_resources of this QueueResourceItem.

        资源配置队列。

        :param queue_resources: The queue_resources of this QueueResourceItem.
        :type queue_resources: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        self._queue_resources = queue_resources

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
        if not isinstance(other, QueueResourceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
