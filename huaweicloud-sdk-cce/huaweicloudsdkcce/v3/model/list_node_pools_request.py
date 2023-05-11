# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodePoolsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'show_default_node_pool': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'show_default_node_pool': 'showDefaultNodePool'
    }

    def __init__(self, cluster_id=None, show_default_node_pool=None):
        """ListNodePoolsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param show_default_node_pool: 是否展示默认节点池。默认不展示，指定为“true”时展示默认节点池。
        :type show_default_node_pool: str
        """
        
        

        self._cluster_id = None
        self._show_default_node_pool = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if show_default_node_pool is not None:
            self.show_default_node_pool = show_default_node_pool

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListNodePoolsRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ListNodePoolsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListNodePoolsRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ListNodePoolsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def show_default_node_pool(self):
        """Gets the show_default_node_pool of this ListNodePoolsRequest.

        是否展示默认节点池。默认不展示，指定为“true”时展示默认节点池。

        :return: The show_default_node_pool of this ListNodePoolsRequest.
        :rtype: str
        """
        return self._show_default_node_pool

    @show_default_node_pool.setter
    def show_default_node_pool(self, show_default_node_pool):
        """Sets the show_default_node_pool of this ListNodePoolsRequest.

        是否展示默认节点池。默认不展示，指定为“true”时展示默认节点池。

        :param show_default_node_pool: The show_default_node_pool of this ListNodePoolsRequest.
        :type show_default_node_pool: str
        """
        self._show_default_node_pool = show_default_node_pool

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
        if not isinstance(other, ListNodePoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
