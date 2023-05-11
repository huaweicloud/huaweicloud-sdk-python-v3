# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateConnectionQueueReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queues': 'list[str]',
        'elastic_resource_pools': 'list[str]'
    }

    attribute_map = {
        'queues': 'queues',
        'elastic_resource_pools': 'elastic_resource_pools'
    }

    def __init__(self, queues=None, elastic_resource_pools=None):
        """AssociateConnectionQueueReq

        The model defined in huaweicloud sdk

        :param queues: 需要使用跨源的队列名列表。
        :type queues: list[str]
        :param elastic_resource_pools: 需要使用跨源的弹性资源池名列表。
        :type elastic_resource_pools: list[str]
        """
        
        

        self._queues = None
        self._elastic_resource_pools = None
        self.discriminator = None

        if queues is not None:
            self.queues = queues
        if elastic_resource_pools is not None:
            self.elastic_resource_pools = elastic_resource_pools

    @property
    def queues(self):
        """Gets the queues of this AssociateConnectionQueueReq.

        需要使用跨源的队列名列表。

        :return: The queues of this AssociateConnectionQueueReq.
        :rtype: list[str]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this AssociateConnectionQueueReq.

        需要使用跨源的队列名列表。

        :param queues: The queues of this AssociateConnectionQueueReq.
        :type queues: list[str]
        """
        self._queues = queues

    @property
    def elastic_resource_pools(self):
        """Gets the elastic_resource_pools of this AssociateConnectionQueueReq.

        需要使用跨源的弹性资源池名列表。

        :return: The elastic_resource_pools of this AssociateConnectionQueueReq.
        :rtype: list[str]
        """
        return self._elastic_resource_pools

    @elastic_resource_pools.setter
    def elastic_resource_pools(self, elastic_resource_pools):
        """Sets the elastic_resource_pools of this AssociateConnectionQueueReq.

        需要使用跨源的弹性资源池名列表。

        :param elastic_resource_pools: The elastic_resource_pools of this AssociateConnectionQueueReq.
        :type elastic_resource_pools: list[str]
        """
        self._elastic_resource_pools = elastic_resource_pools

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
        if not isinstance(other, AssociateConnectionQueueReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
