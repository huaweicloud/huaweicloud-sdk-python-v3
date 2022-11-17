# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterTagRequest:

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
        'resource_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, cluster_id=None, resource_type=None):
        """ShowClusterTagRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 指定待查询的集群ID。
        :type cluster_id: str
        :param resource_type: 资源类型，当前固定值为“css-cluster”，表示是集群类型。
        :type resource_type: str
        """
        
        

        self._cluster_id = None
        self._resource_type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.resource_type = resource_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowClusterTagRequest.

        指定待查询的集群ID。

        :return: The cluster_id of this ShowClusterTagRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowClusterTagRequest.

        指定待查询的集群ID。

        :param cluster_id: The cluster_id of this ShowClusterTagRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ShowClusterTagRequest.

        资源类型，当前固定值为“css-cluster”，表示是集群类型。

        :return: The resource_type of this ShowClusterTagRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ShowClusterTagRequest.

        资源类型，当前固定值为“css-cluster”，表示是集群类型。

        :param resource_type: The resource_type of this ShowClusterTagRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ShowClusterTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
