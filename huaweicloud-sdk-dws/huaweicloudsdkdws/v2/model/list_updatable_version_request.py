# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpdatableVersionRequest:

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
        'offset': 'int',
        'limit': 'int',
        'type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type'
    }

    def __init__(self, cluster_id=None, offset=None, limit=None, type=None):
        """ListUpdatableVersionRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 条目数
        :type limit: int
        :param type: 升级类型 cluster:集群升级 hotpatch:热补丁升级
        :type type: str
        """
        
        

        self._cluster_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListUpdatableVersionRequest.

        集群ID

        :return: The cluster_id of this ListUpdatableVersionRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListUpdatableVersionRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListUpdatableVersionRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def offset(self):
        """Gets the offset of this ListUpdatableVersionRequest.

        偏移量

        :return: The offset of this ListUpdatableVersionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUpdatableVersionRequest.

        偏移量

        :param offset: The offset of this ListUpdatableVersionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListUpdatableVersionRequest.

        条目数

        :return: The limit of this ListUpdatableVersionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUpdatableVersionRequest.

        条目数

        :param limit: The limit of this ListUpdatableVersionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ListUpdatableVersionRequest.

        升级类型 cluster:集群升级 hotpatch:热补丁升级

        :return: The type of this ListUpdatableVersionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListUpdatableVersionRequest.

        升级类型 cluster:集群升级 hotpatch:热补丁升级

        :param type: The type of this ListUpdatableVersionRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListUpdatableVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
