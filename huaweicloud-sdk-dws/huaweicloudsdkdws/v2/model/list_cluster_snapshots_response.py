# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterSnapshotsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshots': 'list[ClusterSnapshots]',
        'project_id': 'str',
        'cluster_id': 'str',
        'count': 'int'
    }

    attribute_map = {
        'snapshots': 'snapshots',
        'project_id': 'project_id',
        'cluster_id': 'cluster_id',
        'count': 'count'
    }

    def __init__(self, snapshots=None, project_id=None, cluster_id=None, count=None):
        """ListClusterSnapshotsResponse

        The model defined in huaweicloud sdk

        :param snapshots: 快照对象列表。
        :type snapshots: list[:class:`huaweicloudsdkdws.v2.ClusterSnapshots`]
        :param project_id: 项目ID。
        :type project_id: str
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param count: 快照对象列表总数
        :type count: int
        """
        
        super(ListClusterSnapshotsResponse, self).__init__()

        self._snapshots = None
        self._project_id = None
        self._cluster_id = None
        self._count = None
        self.discriminator = None

        if snapshots is not None:
            self.snapshots = snapshots
        if project_id is not None:
            self.project_id = project_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if count is not None:
            self.count = count

    @property
    def snapshots(self):
        """Gets the snapshots of this ListClusterSnapshotsResponse.

        快照对象列表。

        :return: The snapshots of this ListClusterSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ClusterSnapshots`]
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this ListClusterSnapshotsResponse.

        快照对象列表。

        :param snapshots: The snapshots of this ListClusterSnapshotsResponse.
        :type snapshots: list[:class:`huaweicloudsdkdws.v2.ClusterSnapshots`]
        """
        self._snapshots = snapshots

    @property
    def project_id(self):
        """Gets the project_id of this ListClusterSnapshotsResponse.

        项目ID。

        :return: The project_id of this ListClusterSnapshotsResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListClusterSnapshotsResponse.

        项目ID。

        :param project_id: The project_id of this ListClusterSnapshotsResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListClusterSnapshotsResponse.

        集群ID。

        :return: The cluster_id of this ListClusterSnapshotsResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListClusterSnapshotsResponse.

        集群ID。

        :param cluster_id: The cluster_id of this ListClusterSnapshotsResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def count(self):
        """Gets the count of this ListClusterSnapshotsResponse.

        快照对象列表总数

        :return: The count of this ListClusterSnapshotsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListClusterSnapshotsResponse.

        快照对象列表总数

        :param count: The count of this ListClusterSnapshotsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListClusterSnapshotsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
