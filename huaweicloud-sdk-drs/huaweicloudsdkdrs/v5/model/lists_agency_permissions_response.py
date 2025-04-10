# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListsAgencyPermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'common_permissions': 'list[str]',
        'engine_permissions': 'list[str]'
    }

    attribute_map = {
        'common_permissions': 'common_permissions',
        'engine_permissions': 'engine_permissions'
    }

    def __init__(self, common_permissions=None, engine_permissions=None):
        r"""ListsAgencyPermissionsResponse

        The model defined in huaweicloud sdk

        :param common_permissions: - DRS FullAccess 数据复制服务所有权限
        :type common_permissions: list[str]
        :param engine_permissions: -  GaussDB ReadOnlyAccess 云数据库 GaussDB服务的只读访问权限 -  GeminiDB ReadOnlyAccess 分布式多模NoSQL数据库服务只读权限 -  GaussDBforMSQLReadOnlyAccess 云数据库HUAWEIGaussDBforMSQL服务的只读访问权限 -  DWS ReadOnlyAccess 数据仓库服务只读权限 -  DDM ReadOnlyAccess 分布式数据库中间件服务只读权限 -  DDS ReadOnlyPolicy 文档数据库服务资源只读权限 -  RDS ReadOnlyAccess 关系型数据库服务资源只读权限 -  MRS ReadOnlyAccess MapReduce服务只读权限,包括集群查询操作,基础服务弹性云服务器、裸金属服务器、云硬盘、虚拟私有云只读权限
        :type engine_permissions: list[str]
        """
        
        super(ListsAgencyPermissionsResponse, self).__init__()

        self._common_permissions = None
        self._engine_permissions = None
        self.discriminator = None

        if common_permissions is not None:
            self.common_permissions = common_permissions
        if engine_permissions is not None:
            self.engine_permissions = engine_permissions

    @property
    def common_permissions(self):
        r"""Gets the common_permissions of this ListsAgencyPermissionsResponse.

        - DRS FullAccess 数据复制服务所有权限

        :return: The common_permissions of this ListsAgencyPermissionsResponse.
        :rtype: list[str]
        """
        return self._common_permissions

    @common_permissions.setter
    def common_permissions(self, common_permissions):
        r"""Sets the common_permissions of this ListsAgencyPermissionsResponse.

        - DRS FullAccess 数据复制服务所有权限

        :param common_permissions: The common_permissions of this ListsAgencyPermissionsResponse.
        :type common_permissions: list[str]
        """
        self._common_permissions = common_permissions

    @property
    def engine_permissions(self):
        r"""Gets the engine_permissions of this ListsAgencyPermissionsResponse.

        -  GaussDB ReadOnlyAccess 云数据库 GaussDB服务的只读访问权限 -  GeminiDB ReadOnlyAccess 分布式多模NoSQL数据库服务只读权限 -  GaussDBforMSQLReadOnlyAccess 云数据库HUAWEIGaussDBforMSQL服务的只读访问权限 -  DWS ReadOnlyAccess 数据仓库服务只读权限 -  DDM ReadOnlyAccess 分布式数据库中间件服务只读权限 -  DDS ReadOnlyPolicy 文档数据库服务资源只读权限 -  RDS ReadOnlyAccess 关系型数据库服务资源只读权限 -  MRS ReadOnlyAccess MapReduce服务只读权限,包括集群查询操作,基础服务弹性云服务器、裸金属服务器、云硬盘、虚拟私有云只读权限

        :return: The engine_permissions of this ListsAgencyPermissionsResponse.
        :rtype: list[str]
        """
        return self._engine_permissions

    @engine_permissions.setter
    def engine_permissions(self, engine_permissions):
        r"""Sets the engine_permissions of this ListsAgencyPermissionsResponse.

        -  GaussDB ReadOnlyAccess 云数据库 GaussDB服务的只读访问权限 -  GeminiDB ReadOnlyAccess 分布式多模NoSQL数据库服务只读权限 -  GaussDBforMSQLReadOnlyAccess 云数据库HUAWEIGaussDBforMSQL服务的只读访问权限 -  DWS ReadOnlyAccess 数据仓库服务只读权限 -  DDM ReadOnlyAccess 分布式数据库中间件服务只读权限 -  DDS ReadOnlyPolicy 文档数据库服务资源只读权限 -  RDS ReadOnlyAccess 关系型数据库服务资源只读权限 -  MRS ReadOnlyAccess MapReduce服务只读权限,包括集群查询操作,基础服务弹性云服务器、裸金属服务器、云硬盘、虚拟私有云只读权限

        :param engine_permissions: The engine_permissions of this ListsAgencyPermissionsResponse.
        :type engine_permissions: list[str]
        """
        self._engine_permissions = engine_permissions

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
        if not isinstance(other, ListsAgencyPermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
