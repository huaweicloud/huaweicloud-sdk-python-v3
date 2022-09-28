# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicePermissionsDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vpc_endpoint_service_id': 'str',
        'permission': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'vpc_endpoint_service_id': 'vpc_endpoint_service_id',
        'permission': 'permission',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, vpc_endpoint_service_id=None, permission=None, limit=None, offset=None, sort_key=None, sort_dir=None):
        """ListServicePermissionsDetailsRequest

        The model defined in huaweicloud sdk

        :param vpc_endpoint_service_id: 终端节点服务的ID。
        :type vpc_endpoint_service_id: str
        :param permission: 权限帐号ID，格式为“iam:domain::domain_id”。 其中“domain_id”为授权用户的帐号ID， 例如“iam:domain::6e9dfd51d1124e8d8498dce894923a0d”，支持模糊搜索。
        :type permission: str
        :param limit: 查询返回终端节点服务的白名单数量限制，即每页返回的个数。 取值范围：0~500，取值一般为10，20或者50，默认为10。
        :type limit: int
        :param offset: 偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。
        :type offset: int
        :param sort_key: 查询结果中白名单列表的排序字段，取值为create_at，表示白名单的添加时间。
        :type sort_key: str
        :param sort_dir: 查询结果中白名单列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。
        :type sort_dir: str
        """
        
        

        self._vpc_endpoint_service_id = None
        self._permission = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.vpc_endpoint_service_id = vpc_endpoint_service_id
        if permission is not None:
            self.permission = permission
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def vpc_endpoint_service_id(self):
        """Gets the vpc_endpoint_service_id of this ListServicePermissionsDetailsRequest.

        终端节点服务的ID。

        :return: The vpc_endpoint_service_id of this ListServicePermissionsDetailsRequest.
        :rtype: str
        """
        return self._vpc_endpoint_service_id

    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, vpc_endpoint_service_id):
        """Sets the vpc_endpoint_service_id of this ListServicePermissionsDetailsRequest.

        终端节点服务的ID。

        :param vpc_endpoint_service_id: The vpc_endpoint_service_id of this ListServicePermissionsDetailsRequest.
        :type vpc_endpoint_service_id: str
        """
        self._vpc_endpoint_service_id = vpc_endpoint_service_id

    @property
    def permission(self):
        """Gets the permission of this ListServicePermissionsDetailsRequest.

        权限帐号ID，格式为“iam:domain::domain_id”。 其中“domain_id”为授权用户的帐号ID， 例如“iam:domain::6e9dfd51d1124e8d8498dce894923a0d”，支持模糊搜索。

        :return: The permission of this ListServicePermissionsDetailsRequest.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ListServicePermissionsDetailsRequest.

        权限帐号ID，格式为“iam:domain::domain_id”。 其中“domain_id”为授权用户的帐号ID， 例如“iam:domain::6e9dfd51d1124e8d8498dce894923a0d”，支持模糊搜索。

        :param permission: The permission of this ListServicePermissionsDetailsRequest.
        :type permission: str
        """
        self._permission = permission

    @property
    def limit(self):
        """Gets the limit of this ListServicePermissionsDetailsRequest.

        查询返回终端节点服务的白名单数量限制，即每页返回的个数。 取值范围：0~500，取值一般为10，20或者50，默认为10。

        :return: The limit of this ListServicePermissionsDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServicePermissionsDetailsRequest.

        查询返回终端节点服务的白名单数量限制，即每页返回的个数。 取值范围：0~500，取值一般为10，20或者50，默认为10。

        :param limit: The limit of this ListServicePermissionsDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListServicePermissionsDetailsRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :return: The offset of this ListServicePermissionsDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServicePermissionsDetailsRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :param offset: The offset of this ListServicePermissionsDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        """Gets the sort_key of this ListServicePermissionsDetailsRequest.

        查询结果中白名单列表的排序字段，取值为create_at，表示白名单的添加时间。

        :return: The sort_key of this ListServicePermissionsDetailsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListServicePermissionsDetailsRequest.

        查询结果中白名单列表的排序字段，取值为create_at，表示白名单的添加时间。

        :param sort_key: The sort_key of this ListServicePermissionsDetailsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListServicePermissionsDetailsRequest.

        查询结果中白名单列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :return: The sort_dir of this ListServicePermissionsDetailsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListServicePermissionsDetailsRequest.

        查询结果中白名单列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :param sort_dir: The sort_dir of this ListServicePermissionsDetailsRequest.
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
        if not isinstance(other, ListServicePermissionsDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
