# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionApprovalDetailDTO:

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
        'cluster_name': 'str',
        'datasource_type': 'str',
        'expire_time': 'int',
        'permissions': 'list[PermissionApprovalDetailDTOPermissions]',
        'proposers': 'list[PermissionApprovalDetailDTOProposers]'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'datasource_type': 'datasource_type',
        'expire_time': 'expire_time',
        'permissions': 'permissions',
        'proposers': 'proposers'
    }

    def __init__(self, cluster_id=None, cluster_name=None, datasource_type=None, expire_time=None, permissions=None, proposers=None):
        r"""PermissionApprovalDetailDTO

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param datasource_type: 数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)
        :type datasource_type: str
        :param expire_time: 超时时间
        :type expire_time: int
        :param permissions: 申请权限详情列表
        :type permissions: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTOPermissions`]
        :param proposers: 申请人详情列表
        :type proposers: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTOProposers`]
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._datasource_type = None
        self._expire_time = None
        self._permissions = None
        self._proposers = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if expire_time is not None:
            self.expire_time = expire_time
        if permissions is not None:
            self.permissions = permissions
        if proposers is not None:
            self.proposers = proposers

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this PermissionApprovalDetailDTO.

        集群id

        :return: The cluster_id of this PermissionApprovalDetailDTO.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this PermissionApprovalDetailDTO.

        集群id

        :param cluster_id: The cluster_id of this PermissionApprovalDetailDTO.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this PermissionApprovalDetailDTO.

        集群名称

        :return: The cluster_name of this PermissionApprovalDetailDTO.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this PermissionApprovalDetailDTO.

        集群名称

        :param cluster_name: The cluster_name of this PermissionApprovalDetailDTO.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this PermissionApprovalDetailDTO.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :return: The datasource_type of this PermissionApprovalDetailDTO.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this PermissionApprovalDetailDTO.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :param datasource_type: The datasource_type of this PermissionApprovalDetailDTO.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def expire_time(self):
        r"""Gets the expire_time of this PermissionApprovalDetailDTO.

        超时时间

        :return: The expire_time of this PermissionApprovalDetailDTO.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this PermissionApprovalDetailDTO.

        超时时间

        :param expire_time: The expire_time of this PermissionApprovalDetailDTO.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def permissions(self):
        r"""Gets the permissions of this PermissionApprovalDetailDTO.

        申请权限详情列表

        :return: The permissions of this PermissionApprovalDetailDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTOPermissions`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this PermissionApprovalDetailDTO.

        申请权限详情列表

        :param permissions: The permissions of this PermissionApprovalDetailDTO.
        :type permissions: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTOPermissions`]
        """
        self._permissions = permissions

    @property
    def proposers(self):
        r"""Gets the proposers of this PermissionApprovalDetailDTO.

        申请人详情列表

        :return: The proposers of this PermissionApprovalDetailDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTOProposers`]
        """
        return self._proposers

    @proposers.setter
    def proposers(self, proposers):
        r"""Sets the proposers of this PermissionApprovalDetailDTO.

        申请人详情列表

        :param proposers: The proposers of this PermissionApprovalDetailDTO.
        :type proposers: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTOProposers`]
        """
        self._proposers = proposers

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
        if not isinstance(other, PermissionApprovalDetailDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
