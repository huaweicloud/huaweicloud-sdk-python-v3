# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityDynamicMaskingPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'datasource_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'database_name': 'str',
        'table_id': 'str',
        'table_name': 'str',
        'user_groups': 'str',
        'users': 'str',
        'conn_name': 'str',
        'conn_id': 'str',
        'sync_status': 'str',
        'sync_msg': 'str',
        'sync_log': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int',
        'update_user': 'str',
        'schema_name': 'str',
        'policy_list': 'list[DynamicMaskingPolicy]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'datasource_type': 'datasource_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'database_name': 'database_name',
        'table_id': 'table_id',
        'table_name': 'table_name',
        'user_groups': 'user_groups',
        'users': 'users',
        'conn_name': 'conn_name',
        'conn_id': 'conn_id',
        'sync_status': 'sync_status',
        'sync_msg': 'sync_msg',
        'sync_log': 'sync_log',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'schema_name': 'schema_name',
        'policy_list': 'policy_list'
    }

    def __init__(self, id=None, name=None, datasource_type=None, cluster_id=None, cluster_name=None, database_name=None, table_id=None, table_name=None, user_groups=None, users=None, conn_name=None, conn_id=None, sync_status=None, sync_msg=None, sync_log=None, create_time=None, create_user=None, update_time=None, update_user=None, schema_name=None, policy_list=None):
        r"""UpdateSecurityDynamicMaskingPolicyResponse

        The model defined in huaweicloud sdk

        :param id: 策略id。
        :type id: str
        :param name: 策略名称。英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符。
        :type name: str
        :param datasource_type: 数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)
        :type datasource_type: str
        :param cluster_id: 集群id。请于集群管理页面查看集群ID信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。
        :type cluster_id: str
        :param cluster_name: 集群名称。请于集群管理页面查看集群名称信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。
        :type cluster_name: str
        :param database_name: 数据库名称。获取方法请参见[获取数据源中的表](getDataTables.html)。
        :type database_name: str
        :param table_id: 数据表id，获取方法请参见[获取数据源中的表](getDataTables.html)。
        :type table_id: str
        :param table_name: 数据表名称, 获取方法请参见[获取数据源中的表](getDataTables.html)。
        :type table_name: str
        :param user_groups: 用户组列表，用户组名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置）。例如：\&quot;userGroup1,userGroup2\&quot;。
        :type user_groups: str
        :param users: 用户列表，用户名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置），例如：\&quot;user1,user2\&quot;。
        :type users: str
        :param conn_name: 数据连接名称，获取方法请参见[查询数据连接列表](ListDataconnections.html)。
        :type conn_name: str
        :param conn_id: 数据连接id，获取方法请参见[查询数据连接列表](ListDataconnections.html)。
        :type conn_id: str
        :param sync_status: 同步状态： - UNKNOWN 未知状态 - NOT_SYNC 未同步 - SYNCING 同步中 - SYNC_SUCCESS 同步成功 - SYNC_FAIL 同步失败 - SYNC_PARTIAL_FAIL 存在失败 - DELETE_FAIL 删除失败 - DELETING 删除中 - UPDATING 更新中 - DATA_UPDATED 数据存在更新
        :type sync_status: str
        :param sync_msg: 策略同步信息。
        :type sync_msg: str
        :param sync_log: 同步运行日志, 格式为 字段同步信息+换行符。
        :type sync_log: str
        :param create_time: 策略创建时间。
        :type create_time: int
        :param create_user: 策略创建者。
        :type create_user: str
        :param update_time: 策略更新时间。
        :type update_time: int
        :param update_user: 策略更新者。
        :type update_user: str
        :param schema_name: DWS数据源的模式名称。
        :type schema_name: str
        :param policy_list: 动态数据脱敏策略列表。
        :type policy_list: list[:class:`huaweicloudsdkdataartsstudio.v1.DynamicMaskingPolicy`]
        """
        
        super(UpdateSecurityDynamicMaskingPolicyResponse, self).__init__()

        self._id = None
        self._name = None
        self._datasource_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._database_name = None
        self._table_id = None
        self._table_name = None
        self._user_groups = None
        self._users = None
        self._conn_name = None
        self._conn_id = None
        self._sync_status = None
        self._sync_msg = None
        self._sync_log = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self._schema_name = None
        self._policy_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if database_name is not None:
            self.database_name = database_name
        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if user_groups is not None:
            self.user_groups = user_groups
        if users is not None:
            self.users = users
        if conn_name is not None:
            self.conn_name = conn_name
        if conn_id is not None:
            self.conn_id = conn_id
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_msg is not None:
            self.sync_msg = sync_msg
        if sync_log is not None:
            self.sync_log = sync_log
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if schema_name is not None:
            self.schema_name = schema_name
        if policy_list is not None:
            self.policy_list = policy_list

    @property
    def id(self):
        r"""Gets the id of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略id。

        :return: The id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略id。

        :param id: The id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略名称。英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符。

        :return: The name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略名称。英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符。

        :param name: The name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :return: The datasource_type of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :param datasource_type: The datasource_type of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateSecurityDynamicMaskingPolicyResponse.

        集群id。请于集群管理页面查看集群ID信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :return: The cluster_id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateSecurityDynamicMaskingPolicyResponse.

        集群id。请于集群管理页面查看集群ID信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :param cluster_id: The cluster_id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        集群名称。请于集群管理页面查看集群名称信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :return: The cluster_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        集群名称。请于集群管理页面查看集群名称信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :param cluster_name: The cluster_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database_name(self):
        r"""Gets the database_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据库名称。获取方法请参见[获取数据源中的表](getDataTables.html)。

        :return: The database_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据库名称。获取方法请参见[获取数据源中的表](getDataTables.html)。

        :param database_name: The database_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_id(self):
        r"""Gets the table_id of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据表id，获取方法请参见[获取数据源中的表](getDataTables.html)。

        :return: The table_id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据表id，获取方法请参见[获取数据源中的表](getDataTables.html)。

        :param table_id: The table_id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name(self):
        r"""Gets the table_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据表名称, 获取方法请参见[获取数据源中的表](getDataTables.html)。

        :return: The table_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据表名称, 获取方法请参见[获取数据源中的表](getDataTables.html)。

        :param table_name: The table_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def user_groups(self):
        r"""Gets the user_groups of this UpdateSecurityDynamicMaskingPolicyResponse.

        用户组列表，用户组名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置）。例如：\"userGroup1,userGroup2\"。

        :return: The user_groups of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        r"""Sets the user_groups of this UpdateSecurityDynamicMaskingPolicyResponse.

        用户组列表，用户组名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置）。例如：\"userGroup1,userGroup2\"。

        :param user_groups: The user_groups of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type user_groups: str
        """
        self._user_groups = user_groups

    @property
    def users(self):
        r"""Gets the users of this UpdateSecurityDynamicMaskingPolicyResponse.

        用户列表，用户名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置），例如：\"user1,user2\"。

        :return: The users of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this UpdateSecurityDynamicMaskingPolicyResponse.

        用户列表，用户名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置），例如：\"user1,user2\"。

        :param users: The users of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type users: str
        """
        self._users = users

    @property
    def conn_name(self):
        r"""Gets the conn_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据连接名称，获取方法请参见[查询数据连接列表](ListDataconnections.html)。

        :return: The conn_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._conn_name

    @conn_name.setter
    def conn_name(self, conn_name):
        r"""Sets the conn_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据连接名称，获取方法请参见[查询数据连接列表](ListDataconnections.html)。

        :param conn_name: The conn_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type conn_name: str
        """
        self._conn_name = conn_name

    @property
    def conn_id(self):
        r"""Gets the conn_id of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据连接id，获取方法请参见[查询数据连接列表](ListDataconnections.html)。

        :return: The conn_id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._conn_id

    @conn_id.setter
    def conn_id(self, conn_id):
        r"""Sets the conn_id of this UpdateSecurityDynamicMaskingPolicyResponse.

        数据连接id，获取方法请参见[查询数据连接列表](ListDataconnections.html)。

        :param conn_id: The conn_id of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type conn_id: str
        """
        self._conn_id = conn_id

    @property
    def sync_status(self):
        r"""Gets the sync_status of this UpdateSecurityDynamicMaskingPolicyResponse.

        同步状态： - UNKNOWN 未知状态 - NOT_SYNC 未同步 - SYNCING 同步中 - SYNC_SUCCESS 同步成功 - SYNC_FAIL 同步失败 - SYNC_PARTIAL_FAIL 存在失败 - DELETE_FAIL 删除失败 - DELETING 删除中 - UPDATING 更新中 - DATA_UPDATED 数据存在更新

        :return: The sync_status of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this UpdateSecurityDynamicMaskingPolicyResponse.

        同步状态： - UNKNOWN 未知状态 - NOT_SYNC 未同步 - SYNCING 同步中 - SYNC_SUCCESS 同步成功 - SYNC_FAIL 同步失败 - SYNC_PARTIAL_FAIL 存在失败 - DELETE_FAIL 删除失败 - DELETING 删除中 - UPDATING 更新中 - DATA_UPDATED 数据存在更新

        :param sync_status: The sync_status of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def sync_msg(self):
        r"""Gets the sync_msg of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略同步信息。

        :return: The sync_msg of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._sync_msg

    @sync_msg.setter
    def sync_msg(self, sync_msg):
        r"""Sets the sync_msg of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略同步信息。

        :param sync_msg: The sync_msg of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type sync_msg: str
        """
        self._sync_msg = sync_msg

    @property
    def sync_log(self):
        r"""Gets the sync_log of this UpdateSecurityDynamicMaskingPolicyResponse.

        同步运行日志, 格式为 字段同步信息+换行符。

        :return: The sync_log of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._sync_log

    @sync_log.setter
    def sync_log(self, sync_log):
        r"""Sets the sync_log of this UpdateSecurityDynamicMaskingPolicyResponse.

        同步运行日志, 格式为 字段同步信息+换行符。

        :param sync_log: The sync_log of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type sync_log: str
        """
        self._sync_log = sync_log

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略创建时间。

        :return: The create_time of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略创建时间。

        :param create_time: The create_time of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略创建者。

        :return: The create_user of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略创建者。

        :param create_user: The create_user of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略更新时间。

        :return: The update_time of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略更新时间。

        :param update_time: The update_time of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略更新者。

        :return: The update_user of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this UpdateSecurityDynamicMaskingPolicyResponse.

        策略更新者。

        :param update_user: The update_user of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def schema_name(self):
        r"""Gets the schema_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        DWS数据源的模式名称。

        :return: The schema_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this UpdateSecurityDynamicMaskingPolicyResponse.

        DWS数据源的模式名称。

        :param schema_name: The schema_name of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def policy_list(self):
        r"""Gets the policy_list of this UpdateSecurityDynamicMaskingPolicyResponse.

        动态数据脱敏策略列表。

        :return: The policy_list of this UpdateSecurityDynamicMaskingPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DynamicMaskingPolicy`]
        """
        return self._policy_list

    @policy_list.setter
    def policy_list(self, policy_list):
        r"""Sets the policy_list of this UpdateSecurityDynamicMaskingPolicyResponse.

        动态数据脱敏策略列表。

        :param policy_list: The policy_list of this UpdateSecurityDynamicMaskingPolicyResponse.
        :type policy_list: list[:class:`huaweicloudsdkdataartsstudio.v1.DynamicMaskingPolicy`]
        """
        self._policy_list = policy_list

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
        if not isinstance(other, UpdateSecurityDynamicMaskingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
