# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityAssignedQueuesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'type': 'str',
        'cluster_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'type': 'type',
        'cluster_id': 'cluster_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, type=None, cluster_id=None, limit=None, offset=None):
        """ListSecurityAssignedQueuesRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param type: 队列类型，MRS、DLI。
        :type type: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        """
        
        

        self._workspace = None
        self._type = None
        self._cluster_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if type is not None:
            self.type = type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListSecurityAssignedQueuesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityAssignedQueuesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListSecurityAssignedQueuesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityAssignedQueuesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def type(self):
        """Gets the type of this ListSecurityAssignedQueuesRequest.

        队列类型，MRS、DLI。

        :return: The type of this ListSecurityAssignedQueuesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSecurityAssignedQueuesRequest.

        队列类型，MRS、DLI。

        :param type: The type of this ListSecurityAssignedQueuesRequest.
        :type type: str
        """
        self._type = type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListSecurityAssignedQueuesRequest.

        集群id

        :return: The cluster_id of this ListSecurityAssignedQueuesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListSecurityAssignedQueuesRequest.

        集群id

        :param cluster_id: The cluster_id of this ListSecurityAssignedQueuesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def limit(self):
        """Gets the limit of this ListSecurityAssignedQueuesRequest.

        limit

        :return: The limit of this ListSecurityAssignedQueuesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityAssignedQueuesRequest.

        limit

        :param limit: The limit of this ListSecurityAssignedQueuesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSecurityAssignedQueuesRequest.

        offset

        :return: The offset of this ListSecurityAssignedQueuesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSecurityAssignedQueuesRequest.

        offset

        :param offset: The offset of this ListSecurityAssignedQueuesRequest.
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
        if not isinstance(other, ListSecurityAssignedQueuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
