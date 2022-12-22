# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterSnapshotsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, cluster_id=None, limit=None, offset=None, sort_key=None, sort_dir=None):
        """ListClusterSnapshotsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param limit: 查询条数
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param sort_key: 排序字段
        :type sort_key: str
        :param sort_dir: 排序规则
        :type sort_dir: str
        """
        
        

        self._cluster_id = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListClusterSnapshotsRequest.

        集群ID

        :return: The cluster_id of this ListClusterSnapshotsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListClusterSnapshotsRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListClusterSnapshotsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def limit(self):
        """Gets the limit of this ListClusterSnapshotsRequest.

        查询条数

        :return: The limit of this ListClusterSnapshotsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListClusterSnapshotsRequest.

        查询条数

        :param limit: The limit of this ListClusterSnapshotsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListClusterSnapshotsRequest.

        偏移量

        :return: The offset of this ListClusterSnapshotsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListClusterSnapshotsRequest.

        偏移量

        :param offset: The offset of this ListClusterSnapshotsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        """Gets the sort_key of this ListClusterSnapshotsRequest.

        排序字段

        :return: The sort_key of this ListClusterSnapshotsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListClusterSnapshotsRequest.

        排序字段

        :param sort_key: The sort_key of this ListClusterSnapshotsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListClusterSnapshotsRequest.

        排序规则

        :return: The sort_dir of this ListClusterSnapshotsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListClusterSnapshotsRequest.

        排序规则

        :param sort_dir: The sort_dir of this ListClusterSnapshotsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListClusterSnapshotsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
