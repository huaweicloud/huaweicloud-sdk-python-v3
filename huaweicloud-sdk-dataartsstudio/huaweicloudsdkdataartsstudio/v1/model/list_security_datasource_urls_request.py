# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDatasourceUrlsRequest:

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
        'cluster_id': 'str',
        'datasource_type': 'str',
        'parent_permission_set_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'cluster_id': 'cluster_id',
        'datasource_type': 'datasource_type',
        'parent_permission_set_id': 'parent_permission_set_id'
    }

    def __init__(self, workspace=None, cluster_id=None, datasource_type=None, parent_permission_set_id=None):
        r"""ListSecurityDatasourceUrlsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param datasource_type: 数据源类型,HIVE
        :type datasource_type: str
        :param parent_permission_set_id: 父权限集ID。获取方法请参见[查询权限集列表](ListSecurityPermissionSets.xml) 注意： * 当该值为父权限集ID时，则基于父权限集中的权限查询
        :type parent_permission_set_id: str
        """
        
        

        self._workspace = None
        self._cluster_id = None
        self._datasource_type = None
        self._parent_permission_set_id = None
        self.discriminator = None

        self.workspace = workspace
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if parent_permission_set_id is not None:
            self.parent_permission_set_id = parent_permission_set_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityDatasourceUrlsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityDatasourceUrlsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityDatasourceUrlsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityDatasourceUrlsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListSecurityDatasourceUrlsRequest.

        集群id

        :return: The cluster_id of this ListSecurityDatasourceUrlsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListSecurityDatasourceUrlsRequest.

        集群id

        :param cluster_id: The cluster_id of this ListSecurityDatasourceUrlsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ListSecurityDatasourceUrlsRequest.

        数据源类型,HIVE

        :return: The datasource_type of this ListSecurityDatasourceUrlsRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ListSecurityDatasourceUrlsRequest.

        数据源类型,HIVE

        :param datasource_type: The datasource_type of this ListSecurityDatasourceUrlsRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def parent_permission_set_id(self):
        r"""Gets the parent_permission_set_id of this ListSecurityDatasourceUrlsRequest.

        父权限集ID。获取方法请参见[查询权限集列表](ListSecurityPermissionSets.xml) 注意： * 当该值为父权限集ID时，则基于父权限集中的权限查询

        :return: The parent_permission_set_id of this ListSecurityDatasourceUrlsRequest.
        :rtype: str
        """
        return self._parent_permission_set_id

    @parent_permission_set_id.setter
    def parent_permission_set_id(self, parent_permission_set_id):
        r"""Sets the parent_permission_set_id of this ListSecurityDatasourceUrlsRequest.

        父权限集ID。获取方法请参见[查询权限集列表](ListSecurityPermissionSets.xml) 注意： * 当该值为父权限集ID时，则基于父权限集中的权限查询

        :param parent_permission_set_id: The parent_permission_set_id of this ListSecurityDatasourceUrlsRequest.
        :type parent_permission_set_id: str
        """
        self._parent_permission_set_id = parent_permission_set_id

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
        if not isinstance(other, ListSecurityDatasourceUrlsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
