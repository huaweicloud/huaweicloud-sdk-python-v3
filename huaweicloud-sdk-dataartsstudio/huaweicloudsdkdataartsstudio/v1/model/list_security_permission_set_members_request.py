# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityPermissionSetMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_set_id': 'str',
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'member_name': 'str',
        'member_type': 'str',
        'order_by_asc': 'bool',
        'order_by': 'str'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'member_name': 'member_name',
        'member_type': 'member_type',
        'order_by_asc': 'order_by_asc',
        'order_by': 'order_by'
    }

    def __init__(self, permission_set_id=None, workspace=None, limit=None, offset=None, member_name=None, member_type=None, order_by_asc=None, order_by=None):
        r"""ListSecurityPermissionSetMembersRequest

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param member_name: 成员名称
        :type member_name: str
        :param member_type: 成员类型,USER,USER_GROUP,WORKSPACE_ROLE
        :type member_type: str
        :param order_by_asc: 是否升序（仅指定排序参数时有效）
        :type order_by_asc: bool
        :param order_by: 排序参数, CREATE_TIME, MEMBER_NAME
        :type order_by: str
        """
        
        

        self._permission_set_id = None
        self._workspace = None
        self._limit = None
        self._offset = None
        self._member_name = None
        self._member_type = None
        self._order_by_asc = None
        self._order_by = None
        self.discriminator = None

        self.permission_set_id = permission_set_id
        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if member_name is not None:
            self.member_name = member_name
        if member_type is not None:
            self.member_type = member_type
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc
        if order_by is not None:
            self.order_by = order_by

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this ListSecurityPermissionSetMembersRequest.

        权限集id

        :return: The permission_set_id of this ListSecurityPermissionSetMembersRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this ListSecurityPermissionSetMembersRequest.

        权限集id

        :param permission_set_id: The permission_set_id of this ListSecurityPermissionSetMembersRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityPermissionSetMembersRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityPermissionSetMembersRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityPermissionSetMembersRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityPermissionSetMembersRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityPermissionSetMembersRequest.

        limit

        :return: The limit of this ListSecurityPermissionSetMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityPermissionSetMembersRequest.

        limit

        :param limit: The limit of this ListSecurityPermissionSetMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityPermissionSetMembersRequest.

        offset

        :return: The offset of this ListSecurityPermissionSetMembersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityPermissionSetMembersRequest.

        offset

        :param offset: The offset of this ListSecurityPermissionSetMembersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def member_name(self):
        r"""Gets the member_name of this ListSecurityPermissionSetMembersRequest.

        成员名称

        :return: The member_name of this ListSecurityPermissionSetMembersRequest.
        :rtype: str
        """
        return self._member_name

    @member_name.setter
    def member_name(self, member_name):
        r"""Sets the member_name of this ListSecurityPermissionSetMembersRequest.

        成员名称

        :param member_name: The member_name of this ListSecurityPermissionSetMembersRequest.
        :type member_name: str
        """
        self._member_name = member_name

    @property
    def member_type(self):
        r"""Gets the member_type of this ListSecurityPermissionSetMembersRequest.

        成员类型,USER,USER_GROUP,WORKSPACE_ROLE

        :return: The member_type of this ListSecurityPermissionSetMembersRequest.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        r"""Sets the member_type of this ListSecurityPermissionSetMembersRequest.

        成员类型,USER,USER_GROUP,WORKSPACE_ROLE

        :param member_type: The member_type of this ListSecurityPermissionSetMembersRequest.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecurityPermissionSetMembersRequest.

        是否升序（仅指定排序参数时有效）

        :return: The order_by_asc of this ListSecurityPermissionSetMembersRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecurityPermissionSetMembersRequest.

        是否升序（仅指定排序参数时有效）

        :param order_by_asc: The order_by_asc of this ListSecurityPermissionSetMembersRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityPermissionSetMembersRequest.

        排序参数, CREATE_TIME, MEMBER_NAME

        :return: The order_by of this ListSecurityPermissionSetMembersRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityPermissionSetMembersRequest.

        排序参数, CREATE_TIME, MEMBER_NAME

        :param order_by: The order_by of this ListSecurityPermissionSetMembersRequest.
        :type order_by: str
        """
        self._order_by = order_by

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
        if not isinstance(other, ListSecurityPermissionSetMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
