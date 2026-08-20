# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityMemberPermissionsByUserIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'user_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'datasource_type': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'account_type': 'str',
        'expire_status': 'str',
        'start_expire_time': 'int',
        'end_expire_time': 'int',
        'workspace': 'str',
        'order_by': 'str',
        'order_by_asc': 'bool'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'limit': 'limit',
        'offset': 'offset',
        'datasource_type': 'datasource_type',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'account_type': 'account_type',
        'expire_status': 'expire_status',
        'start_expire_time': 'start_expire_time',
        'end_expire_time': 'end_expire_time',
        'workspace': 'workspace',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc'
    }

    def __init__(self, user_id=None, user_name=None, limit=None, offset=None, datasource_type=None, database_name=None, schema_name=None, table_name=None, account_type=None, expire_status=None, start_expire_time=None, end_expire_time=None, workspace=None, order_by=None, order_by_asc=None):
        r"""ListSecurityMemberPermissionsByUserIdRequest

        The model defined in huaweicloud sdk

        :param user_id: IAM用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param datasource_type: 数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)
        :type datasource_type: str
        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: Schema名，正向模糊匹配
        :type schema_name: str
        :param table_name: 表名称
        :type table_name: str
        :param account_type: 权限账号类型 * SELF_ACCOUNT 个人账号权限 * WORKSPACE_ACCOUNT 空间调度账号权限
        :type account_type: str
        :param expire_status: 权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON
        :type expire_status: str
        :param start_expire_time: 过期时间开始时间戳，毫秒。
        :type start_expire_time: int
        :param end_expire_time: 过期时间结束时间戳，毫秒。
        :type end_expire_time: int
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param order_by: 排序参数,EXPIRE_TIME
        :type order_by: str
        :param order_by_asc: 升序/降序。true升序，false降序
        :type order_by_asc: bool
        """
        
        

        self._user_id = None
        self._user_name = None
        self._limit = None
        self._offset = None
        self._datasource_type = None
        self._database_name = None
        self._schema_name = None
        self._table_name = None
        self._account_type = None
        self._expire_status = None
        self._start_expire_time = None
        self._end_expire_time = None
        self._workspace = None
        self._order_by = None
        self._order_by_asc = None
        self.discriminator = None

        self.user_id = user_id
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
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if account_type is not None:
            self.account_type = account_type
        if expire_status is not None:
            self.expire_status = expire_status
        if start_expire_time is not None:
            self.start_expire_time = start_expire_time
        if end_expire_time is not None:
            self.end_expire_time = end_expire_time
        self.workspace = workspace
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc

    @property
    def user_id(self):
        r"""Gets the user_id of this ListSecurityMemberPermissionsByUserIdRequest.

        IAM用户id

        :return: The user_id of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListSecurityMemberPermissionsByUserIdRequest.

        IAM用户id

        :param user_id: The user_id of this ListSecurityMemberPermissionsByUserIdRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ListSecurityMemberPermissionsByUserIdRequest.

        用户名

        :return: The user_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListSecurityMemberPermissionsByUserIdRequest.

        用户名

        :param user_name: The user_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityMemberPermissionsByUserIdRequest.

        limit

        :return: The limit of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityMemberPermissionsByUserIdRequest.

        limit

        :param limit: The limit of this ListSecurityMemberPermissionsByUserIdRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityMemberPermissionsByUserIdRequest.

        offset

        :return: The offset of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityMemberPermissionsByUserIdRequest.

        offset

        :param offset: The offset of this ListSecurityMemberPermissionsByUserIdRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ListSecurityMemberPermissionsByUserIdRequest.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :return: The datasource_type of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ListSecurityMemberPermissionsByUserIdRequest.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :param datasource_type: The datasource_type of this ListSecurityMemberPermissionsByUserIdRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSecurityMemberPermissionsByUserIdRequest.

        数据库名称

        :return: The database_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSecurityMemberPermissionsByUserIdRequest.

        数据库名称

        :param database_name: The database_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListSecurityMemberPermissionsByUserIdRequest.

        Schema名，正向模糊匹配

        :return: The schema_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListSecurityMemberPermissionsByUserIdRequest.

        Schema名，正向模糊匹配

        :param schema_name: The schema_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListSecurityMemberPermissionsByUserIdRequest.

        表名称

        :return: The table_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListSecurityMemberPermissionsByUserIdRequest.

        表名称

        :param table_name: The table_name of this ListSecurityMemberPermissionsByUserIdRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def account_type(self):
        r"""Gets the account_type of this ListSecurityMemberPermissionsByUserIdRequest.

        权限账号类型 * SELF_ACCOUNT 个人账号权限 * WORKSPACE_ACCOUNT 空间调度账号权限

        :return: The account_type of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this ListSecurityMemberPermissionsByUserIdRequest.

        权限账号类型 * SELF_ACCOUNT 个人账号权限 * WORKSPACE_ACCOUNT 空间调度账号权限

        :param account_type: The account_type of this ListSecurityMemberPermissionsByUserIdRequest.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def expire_status(self):
        r"""Gets the expire_status of this ListSecurityMemberPermissionsByUserIdRequest.

        权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON

        :return: The expire_status of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._expire_status

    @expire_status.setter
    def expire_status(self, expire_status):
        r"""Sets the expire_status of this ListSecurityMemberPermissionsByUserIdRequest.

        权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON

        :param expire_status: The expire_status of this ListSecurityMemberPermissionsByUserIdRequest.
        :type expire_status: str
        """
        self._expire_status = expire_status

    @property
    def start_expire_time(self):
        r"""Gets the start_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.

        过期时间开始时间戳，毫秒。

        :return: The start_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: int
        """
        return self._start_expire_time

    @start_expire_time.setter
    def start_expire_time(self, start_expire_time):
        r"""Sets the start_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.

        过期时间开始时间戳，毫秒。

        :param start_expire_time: The start_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.
        :type start_expire_time: int
        """
        self._start_expire_time = start_expire_time

    @property
    def end_expire_time(self):
        r"""Gets the end_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.

        过期时间结束时间戳，毫秒。

        :return: The end_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: int
        """
        return self._end_expire_time

    @end_expire_time.setter
    def end_expire_time(self, end_expire_time):
        r"""Sets the end_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.

        过期时间结束时间戳，毫秒。

        :param end_expire_time: The end_expire_time of this ListSecurityMemberPermissionsByUserIdRequest.
        :type end_expire_time: int
        """
        self._end_expire_time = end_expire_time

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityMemberPermissionsByUserIdRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityMemberPermissionsByUserIdRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityMemberPermissionsByUserIdRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityMemberPermissionsByUserIdRequest.

        排序参数,EXPIRE_TIME

        :return: The order_by of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityMemberPermissionsByUserIdRequest.

        排序参数,EXPIRE_TIME

        :param order_by: The order_by of this ListSecurityMemberPermissionsByUserIdRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecurityMemberPermissionsByUserIdRequest.

        升序/降序。true升序，false降序

        :return: The order_by_asc of this ListSecurityMemberPermissionsByUserIdRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecurityMemberPermissionsByUserIdRequest.

        升序/降序。true升序，false降序

        :param order_by_asc: The order_by_asc of this ListSecurityMemberPermissionsByUserIdRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSecurityMemberPermissionsByUserIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
