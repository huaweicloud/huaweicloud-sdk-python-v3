# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkloadPlansRequest:

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
        'logical_cluster_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'logical_cluster_name': 'logical_cluster_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, logical_cluster_name=None, limit=None, offset=None):
        r"""ListWorkloadPlansRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param logical_cluster_name: 逻辑集群名称
        :type logical_cluster_name: str
        :param limit: 查询条数
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._logical_cluster_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListWorkloadPlansRequest.

        集群ID

        :return: The cluster_id of this ListWorkloadPlansRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListWorkloadPlansRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListWorkloadPlansRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this ListWorkloadPlansRequest.

        逻辑集群名称

        :return: The logical_cluster_name of this ListWorkloadPlansRequest.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this ListWorkloadPlansRequest.

        逻辑集群名称

        :param logical_cluster_name: The logical_cluster_name of this ListWorkloadPlansRequest.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkloadPlansRequest.

        查询条数

        :return: The limit of this ListWorkloadPlansRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkloadPlansRequest.

        查询条数

        :param limit: The limit of this ListWorkloadPlansRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkloadPlansRequest.

        偏移量

        :return: The offset of this ListWorkloadPlansRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkloadPlansRequest.

        偏移量

        :param offset: The offset of this ListWorkloadPlansRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListWorkloadPlansRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
