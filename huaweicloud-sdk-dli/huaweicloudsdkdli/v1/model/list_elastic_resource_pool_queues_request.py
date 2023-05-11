# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListElasticResourcePoolQueuesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elastic_resource_pool_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'queue_name': 'str'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'limit': 'limit',
        'offset': 'offset',
        'queue_name': 'queue_name'
    }

    def __init__(self, elastic_resource_pool_name=None, limit=None, offset=None, queue_name=None):
        """ListElasticResourcePoolQueuesRequest

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 弹性资源池名称
        :type elastic_resource_pool_name: str
        :param limit: 默认为100
        :type limit: int
        :param offset: 默认为0
        :type offset: int
        :param queue_name: 可以根据queueName进行过滤
        :type queue_name: str
        """
        
        

        self._elastic_resource_pool_name = None
        self._limit = None
        self._offset = None
        self._queue_name = None
        self.discriminator = None

        self.elastic_resource_pool_name = elastic_resource_pool_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if queue_name is not None:
            self.queue_name = queue_name

    @property
    def elastic_resource_pool_name(self):
        """Gets the elastic_resource_pool_name of this ListElasticResourcePoolQueuesRequest.

        弹性资源池名称

        :return: The elastic_resource_pool_name of this ListElasticResourcePoolQueuesRequest.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        """Sets the elastic_resource_pool_name of this ListElasticResourcePoolQueuesRequest.

        弹性资源池名称

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this ListElasticResourcePoolQueuesRequest.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def limit(self):
        """Gets the limit of this ListElasticResourcePoolQueuesRequest.

        默认为100

        :return: The limit of this ListElasticResourcePoolQueuesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListElasticResourcePoolQueuesRequest.

        默认为100

        :param limit: The limit of this ListElasticResourcePoolQueuesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListElasticResourcePoolQueuesRequest.

        默认为0

        :return: The offset of this ListElasticResourcePoolQueuesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListElasticResourcePoolQueuesRequest.

        默认为0

        :param offset: The offset of this ListElasticResourcePoolQueuesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def queue_name(self):
        """Gets the queue_name of this ListElasticResourcePoolQueuesRequest.

        可以根据queueName进行过滤

        :return: The queue_name of this ListElasticResourcePoolQueuesRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListElasticResourcePoolQueuesRequest.

        可以根据queueName进行过滤

        :param queue_name: The queue_name of this ListElasticResourcePoolQueuesRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

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
        if not isinstance(other, ListElasticResourcePoolQueuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
