# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteQueueInfoRequest:

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
        'vhost': 'str',
        'queue': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vhost': 'vhost',
        'queue': 'queue'
    }

    def __init__(self, instance_id=None, vhost=None, queue=None):
        """DeleteQueueInfoRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param vhost: Vhost名称
        :type vhost: str
        :param queue: Queue名称
        :type queue: str
        """
        
        

        self._instance_id = None
        self._vhost = None
        self._queue = None
        self.discriminator = None

        self.instance_id = instance_id
        self.vhost = vhost
        self.queue = queue

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteQueueInfoRequest.

        实例ID

        :return: The instance_id of this DeleteQueueInfoRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteQueueInfoRequest.

        实例ID

        :param instance_id: The instance_id of this DeleteQueueInfoRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vhost(self):
        """Gets the vhost of this DeleteQueueInfoRequest.

        Vhost名称

        :return: The vhost of this DeleteQueueInfoRequest.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        """Sets the vhost of this DeleteQueueInfoRequest.

        Vhost名称

        :param vhost: The vhost of this DeleteQueueInfoRequest.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def queue(self):
        """Gets the queue of this DeleteQueueInfoRequest.

        Queue名称

        :return: The queue of this DeleteQueueInfoRequest.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this DeleteQueueInfoRequest.

        Queue名称

        :param queue: The queue of this DeleteQueueInfoRequest.
        :type queue: str
        """
        self._queue = queue

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
        if not isinstance(other, DeleteQueueInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
