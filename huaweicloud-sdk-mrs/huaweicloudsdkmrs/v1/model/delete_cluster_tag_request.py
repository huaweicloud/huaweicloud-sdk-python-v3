# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteClusterTagRequest:

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
        'key': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'key': 'key'
    }

    def __init__(self, cluster_id=None, key=None):
        """DeleteClusterTagRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param key: 键。标签的key值
        :type key: str
        """
        
        

        self._cluster_id = None
        self._key = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.key = key

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteClusterTagRequest.

        集群ID。

        :return: The cluster_id of this DeleteClusterTagRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteClusterTagRequest.

        集群ID。

        :param cluster_id: The cluster_id of this DeleteClusterTagRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def key(self):
        """Gets the key of this DeleteClusterTagRequest.

        键。标签的key值

        :return: The key of this DeleteClusterTagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteClusterTagRequest.

        键。标签的key值

        :param key: The key of this DeleteClusterTagRequest.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, DeleteClusterTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
