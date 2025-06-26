# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadQueueItem:

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
        'logical_cluster_name': 'str',
        'short_query_optimize': 'str',
        'short_query_concurrency_num': 'int',
        'resource_item_list': 'list[WorkloadResourceItem]'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'logical_cluster_name': 'logical_cluster_name',
        'short_query_optimize': 'short_query_optimize',
        'short_query_concurrency_num': 'short_query_concurrency_num',
        'resource_item_list': 'resource_item_list'
    }

    def __init__(self, queue_name=None, logical_cluster_name=None, short_query_optimize=None, short_query_concurrency_num=None, resource_item_list=None):
        r"""WorkloadQueueItem

        The model defined in huaweicloud sdk

        :param queue_name: **参数解释**： 资源池名称。 **取值范围**： 不涉及。
        :type queue_name: str
        :param logical_cluster_name: **参数解释**： 逻辑集群名称。 **取值范围**： 不涉及。
        :type logical_cluster_name: str
        :param short_query_optimize: **参数解释**： 资源池短查询加速开关。 **取值范围**： 不涉及。
        :type short_query_optimize: str
        :param short_query_concurrency_num: **参数解释**： 资源池短查询并发数。 **取值范围**： 不涉及。
        :type short_query_concurrency_num: int
        :param resource_item_list: **参数解释**： 资源配置队列。 **取值范围**： 不涉及。
        :type resource_item_list: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        
        

        self._queue_name = None
        self._logical_cluster_name = None
        self._short_query_optimize = None
        self._short_query_concurrency_num = None
        self._resource_item_list = None
        self.discriminator = None

        self.queue_name = queue_name
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if short_query_optimize is not None:
            self.short_query_optimize = short_query_optimize
        if short_query_concurrency_num is not None:
            self.short_query_concurrency_num = short_query_concurrency_num
        self.resource_item_list = resource_item_list

    @property
    def queue_name(self):
        r"""Gets the queue_name of this WorkloadQueueItem.

        **参数解释**： 资源池名称。 **取值范围**： 不涉及。

        :return: The queue_name of this WorkloadQueueItem.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this WorkloadQueueItem.

        **参数解释**： 资源池名称。 **取值范围**： 不涉及。

        :param queue_name: The queue_name of this WorkloadQueueItem.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this WorkloadQueueItem.

        **参数解释**： 逻辑集群名称。 **取值范围**： 不涉及。

        :return: The logical_cluster_name of this WorkloadQueueItem.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this WorkloadQueueItem.

        **参数解释**： 逻辑集群名称。 **取值范围**： 不涉及。

        :param logical_cluster_name: The logical_cluster_name of this WorkloadQueueItem.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def short_query_optimize(self):
        r"""Gets the short_query_optimize of this WorkloadQueueItem.

        **参数解释**： 资源池短查询加速开关。 **取值范围**： 不涉及。

        :return: The short_query_optimize of this WorkloadQueueItem.
        :rtype: str
        """
        return self._short_query_optimize

    @short_query_optimize.setter
    def short_query_optimize(self, short_query_optimize):
        r"""Sets the short_query_optimize of this WorkloadQueueItem.

        **参数解释**： 资源池短查询加速开关。 **取值范围**： 不涉及。

        :param short_query_optimize: The short_query_optimize of this WorkloadQueueItem.
        :type short_query_optimize: str
        """
        self._short_query_optimize = short_query_optimize

    @property
    def short_query_concurrency_num(self):
        r"""Gets the short_query_concurrency_num of this WorkloadQueueItem.

        **参数解释**： 资源池短查询并发数。 **取值范围**： 不涉及。

        :return: The short_query_concurrency_num of this WorkloadQueueItem.
        :rtype: int
        """
        return self._short_query_concurrency_num

    @short_query_concurrency_num.setter
    def short_query_concurrency_num(self, short_query_concurrency_num):
        r"""Sets the short_query_concurrency_num of this WorkloadQueueItem.

        **参数解释**： 资源池短查询并发数。 **取值范围**： 不涉及。

        :param short_query_concurrency_num: The short_query_concurrency_num of this WorkloadQueueItem.
        :type short_query_concurrency_num: int
        """
        self._short_query_concurrency_num = short_query_concurrency_num

    @property
    def resource_item_list(self):
        r"""Gets the resource_item_list of this WorkloadQueueItem.

        **参数解释**： 资源配置队列。 **取值范围**： 不涉及。

        :return: The resource_item_list of this WorkloadQueueItem.
        :rtype: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        return self._resource_item_list

    @resource_item_list.setter
    def resource_item_list(self, resource_item_list):
        r"""Sets the resource_item_list of this WorkloadQueueItem.

        **参数解释**： 资源配置队列。 **取值范围**： 不涉及。

        :param resource_item_list: The resource_item_list of this WorkloadQueueItem.
        :type resource_item_list: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        self._resource_item_list = resource_item_list

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
        if not isinstance(other, WorkloadQueueItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
