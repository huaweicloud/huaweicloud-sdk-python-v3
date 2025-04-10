# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityMemberPermissionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'datasource_type': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'account_type': 'str',
        'expire_status': 'str',
        'workspace': 'str',
        'order_by': 'str',
        'order_by_asc': 'bool'
    }

    attribute_map = {
        'user_name': 'user_name',
        'limit': 'limit',
        'offset': 'offset',
        'datasource_type': 'datasource_type',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'account_type': 'account_type',
        'expire_status': 'expire_status',
        'workspace': 'workspace',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc'
    }

    def __init__(self, user_name=None, limit=None, offset=None, datasource_type=None, database_name=None, table_name=None, account_type=None, expire_status=None, workspace=None, order_by=None, order_by_asc=None):
        r"""ListSecurityMemberPermissionRequest

        The model defined in huaweicloud sdk

        :param user_name: 用户名
        :type user_name: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param datasource_type: 数据源类型,HIVE
        :type datasource_type: str
        :param database_name: 数据库名称
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param account_type: 权限账号类型 * SELF_ACCOUNT 个人账号权限 * WORKSPACE_ACCOUNT 空间调度账号权限
        :type account_type: str
        :param expire_status: 权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON
        :type expire_status: str
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param order_by: 排序参数,EXPIRE_TIME
        :type order_by: str
        :param order_by_asc: 升序/降序。true升序，fasle降序
        :type order_by_asc: bool
        """
        
        

        self._user_name = None
        self._limit = None
        self._offset = None
        self._datasource_type = None
        self._database_name = None
        self._table_name = None
        self._account_type = None
        self._expire_status = None
        self._workspace = None
        self._order_by = None
        self._order_by_asc = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if account_type is not None:
            self.account_type = account_type
        if expire_status is not None:
            self.expire_status = expire_status
        self.workspace = workspace
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc

    @property
    def user_name(self):
        r"""Gets the user_name of this ListSecurityMemberPermissionRequest.

        用户名

        :return: The user_name of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListSecurityMemberPermissionRequest.

        用户名

        :param user_name: The user_name of this ListSecurityMemberPermissionRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityMemberPermissionRequest.

        limit

        :return: The limit of this ListSecurityMemberPermissionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityMemberPermissionRequest.

        limit

        :param limit: The limit of this ListSecurityMemberPermissionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityMemberPermissionRequest.

        offset

        :return: The offset of this ListSecurityMemberPermissionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityMemberPermissionRequest.

        offset

        :param offset: The offset of this ListSecurityMemberPermissionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ListSecurityMemberPermissionRequest.

        数据源类型,HIVE

        :return: The datasource_type of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ListSecurityMemberPermissionRequest.

        数据源类型,HIVE

        :param datasource_type: The datasource_type of this ListSecurityMemberPermissionRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSecurityMemberPermissionRequest.

        数据库名称

        :return: The database_name of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSecurityMemberPermissionRequest.

        数据库名称

        :param database_name: The database_name of this ListSecurityMemberPermissionRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListSecurityMemberPermissionRequest.

        表名称

        :return: The table_name of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListSecurityMemberPermissionRequest.

        表名称

        :param table_name: The table_name of this ListSecurityMemberPermissionRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def account_type(self):
        r"""Gets the account_type of this ListSecurityMemberPermissionRequest.

        权限账号类型 * SELF_ACCOUNT 个人账号权限 * WORKSPACE_ACCOUNT 空间调度账号权限

        :return: The account_type of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this ListSecurityMemberPermissionRequest.

        权限账号类型 * SELF_ACCOUNT 个人账号权限 * WORKSPACE_ACCOUNT 空间调度账号权限

        :param account_type: The account_type of this ListSecurityMemberPermissionRequest.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def expire_status(self):
        r"""Gets the expire_status of this ListSecurityMemberPermissionRequest.

        权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON

        :return: The expire_status of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._expire_status

    @expire_status.setter
    def expire_status(self, expire_status):
        r"""Sets the expire_status of this ListSecurityMemberPermissionRequest.

        权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON

        :param expire_status: The expire_status of this ListSecurityMemberPermissionRequest.
        :type expire_status: str
        """
        self._expire_status = expire_status

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityMemberPermissionRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityMemberPermissionRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityMemberPermissionRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityMemberPermissionRequest.

        排序参数,EXPIRE_TIME

        :return: The order_by of this ListSecurityMemberPermissionRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityMemberPermissionRequest.

        排序参数,EXPIRE_TIME

        :param order_by: The order_by of this ListSecurityMemberPermissionRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecurityMemberPermissionRequest.

        升序/降序。true升序，fasle降序

        :return: The order_by_asc of this ListSecurityMemberPermissionRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecurityMemberPermissionRequest.

        升序/降序。true升序，fasle降序

        :param order_by_asc: The order_by_asc of this ListSecurityMemberPermissionRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

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
        if not isinstance(other, ListSecurityMemberPermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
