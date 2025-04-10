# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DynamicMaskingPolicySet:

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
        'table_name': 'str',
        'user_groups': 'str',
        'users': 'str',
        'sync_status': 'str',
        'sync_time': 'int',
        'sync_msg': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int',
        'update_user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'datasource_type': 'datasource_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'user_groups': 'user_groups',
        'users': 'users',
        'sync_status': 'sync_status',
        'sync_time': 'sync_time',
        'sync_msg': 'sync_msg',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, id=None, name=None, datasource_type=None, cluster_id=None, cluster_name=None, database_name=None, table_name=None, user_groups=None, users=None, sync_status=None, sync_time=None, sync_msg=None, create_time=None, create_user=None, update_time=None, update_user=None):
        r"""DynamicMaskingPolicySet

        The model defined in huaweicloud sdk

        :param id: 动态脱敏策略id。
        :type id: str
        :param name: 动态脱敏策略名称。英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符。
        :type name: str
        :param datasource_type: 数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)
        :type datasource_type: str
        :param cluster_id: 集群id。请于集群管理页面查看集群ID信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。
        :type cluster_id: str
        :param cluster_name: 集群名称。请于集群管理页面查看集群名称信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。
        :type cluster_name: str
        :param database_name: 数据库名称。获取方法请参见[获取数据源中的表](getDataTables.html)。
        :type database_name: str
        :param table_name: 数据表名称, 获取方法请参见[获取数据源中的表](getDataTables.html)。
        :type table_name: str
        :param user_groups: 用户组列表，用户组名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置）。例如：\&quot;userGroup1,userGroup2\&quot;。
        :type user_groups: str
        :param users: 用户列表，用户名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置），例如：\&quot;user1,user2\&quot;。
        :type users: str
        :param sync_status: 同步状态： - UNKNOWN 未知状态 - NOT_SYNC 未同步 - SYNCING 同步中 - SYNC_SUCCESS 同步成功 - SYNC_FAIL 同步失败 - SYNC_PARTIAL_FAIL 存在失败 - DELETE_FAIL 删除失败 - DELETING 删除中 - UPDATING 更新中 - DATA_UPDATED 数据存在更新
        :type sync_status: str
        :param sync_time: 策略同步时间。
        :type sync_time: int
        :param sync_msg: 策略同步日志。
        :type sync_msg: str
        :param create_time: 策略创建时间。
        :type create_time: int
        :param create_user: 策略创建者。
        :type create_user: str
        :param update_time: 策略更新时间。
        :type update_time: int
        :param update_user: 策略更新者。
        :type update_user: str
        """
        
        

        self._id = None
        self._name = None
        self._datasource_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._database_name = None
        self._table_name = None
        self._user_groups = None
        self._users = None
        self._sync_status = None
        self._sync_time = None
        self._sync_msg = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
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
        if table_name is not None:
            self.table_name = table_name
        if user_groups is not None:
            self.user_groups = user_groups
        if users is not None:
            self.users = users
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_time is not None:
            self.sync_time = sync_time
        if sync_msg is not None:
            self.sync_msg = sync_msg
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def id(self):
        r"""Gets the id of this DynamicMaskingPolicySet.

        动态脱敏策略id。

        :return: The id of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DynamicMaskingPolicySet.

        动态脱敏策略id。

        :param id: The id of this DynamicMaskingPolicySet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DynamicMaskingPolicySet.

        动态脱敏策略名称。英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符。

        :return: The name of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DynamicMaskingPolicySet.

        动态脱敏策略名称。英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符。

        :param name: The name of this DynamicMaskingPolicySet.
        :type name: str
        """
        self._name = name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this DynamicMaskingPolicySet.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :return: The datasource_type of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this DynamicMaskingPolicySet.

        数据源类型 - HIVE数据源 - DWS数据源 - [DLI数据源](tag:nohcs)

        :param datasource_type: The datasource_type of this DynamicMaskingPolicySet.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this DynamicMaskingPolicySet.

        集群id。请于集群管理页面查看集群ID信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :return: The cluster_id of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this DynamicMaskingPolicySet.

        集群id。请于集群管理页面查看集群ID信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :param cluster_id: The cluster_id of this DynamicMaskingPolicySet.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this DynamicMaskingPolicySet.

        集群名称。请于集群管理页面查看集群名称信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :return: The cluster_name of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this DynamicMaskingPolicySet.

        集群名称。请于集群管理页面查看集群名称信息。[当数据源类型为DLI时，该参数需要填写为DLI](tag:nohcs)。

        :param cluster_name: The cluster_name of this DynamicMaskingPolicySet.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database_name(self):
        r"""Gets the database_name of this DynamicMaskingPolicySet.

        数据库名称。获取方法请参见[获取数据源中的表](getDataTables.html)。

        :return: The database_name of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DynamicMaskingPolicySet.

        数据库名称。获取方法请参见[获取数据源中的表](getDataTables.html)。

        :param database_name: The database_name of this DynamicMaskingPolicySet.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this DynamicMaskingPolicySet.

        数据表名称, 获取方法请参见[获取数据源中的表](getDataTables.html)。

        :return: The table_name of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DynamicMaskingPolicySet.

        数据表名称, 获取方法请参见[获取数据源中的表](getDataTables.html)。

        :param table_name: The table_name of this DynamicMaskingPolicySet.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def user_groups(self):
        r"""Gets the user_groups of this DynamicMaskingPolicySet.

        用户组列表，用户组名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置）。例如：\"userGroup1,userGroup2\"。

        :return: The user_groups of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        r"""Sets the user_groups of this DynamicMaskingPolicySet.

        用户组列表，用户组名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置）。例如：\"userGroup1,userGroup2\"。

        :param user_groups: The user_groups of this DynamicMaskingPolicySet.
        :type user_groups: str
        """
        self._user_groups = user_groups

    @property
    def users(self):
        r"""Gets the users of this DynamicMaskingPolicySet.

        用户列表，用户名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置），例如：\"user1,user2\"。

        :return: The users of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this DynamicMaskingPolicySet.

        用户列表，用户名称逗号分隔（非必填项，但用户、用户组必须二选其一进行配置），例如：\"user1,user2\"。

        :param users: The users of this DynamicMaskingPolicySet.
        :type users: str
        """
        self._users = users

    @property
    def sync_status(self):
        r"""Gets the sync_status of this DynamicMaskingPolicySet.

        同步状态： - UNKNOWN 未知状态 - NOT_SYNC 未同步 - SYNCING 同步中 - SYNC_SUCCESS 同步成功 - SYNC_FAIL 同步失败 - SYNC_PARTIAL_FAIL 存在失败 - DELETE_FAIL 删除失败 - DELETING 删除中 - UPDATING 更新中 - DATA_UPDATED 数据存在更新

        :return: The sync_status of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this DynamicMaskingPolicySet.

        同步状态： - UNKNOWN 未知状态 - NOT_SYNC 未同步 - SYNCING 同步中 - SYNC_SUCCESS 同步成功 - SYNC_FAIL 同步失败 - SYNC_PARTIAL_FAIL 存在失败 - DELETE_FAIL 删除失败 - DELETING 删除中 - UPDATING 更新中 - DATA_UPDATED 数据存在更新

        :param sync_status: The sync_status of this DynamicMaskingPolicySet.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def sync_time(self):
        r"""Gets the sync_time of this DynamicMaskingPolicySet.

        策略同步时间。

        :return: The sync_time of this DynamicMaskingPolicySet.
        :rtype: int
        """
        return self._sync_time

    @sync_time.setter
    def sync_time(self, sync_time):
        r"""Sets the sync_time of this DynamicMaskingPolicySet.

        策略同步时间。

        :param sync_time: The sync_time of this DynamicMaskingPolicySet.
        :type sync_time: int
        """
        self._sync_time = sync_time

    @property
    def sync_msg(self):
        r"""Gets the sync_msg of this DynamicMaskingPolicySet.

        策略同步日志。

        :return: The sync_msg of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._sync_msg

    @sync_msg.setter
    def sync_msg(self, sync_msg):
        r"""Sets the sync_msg of this DynamicMaskingPolicySet.

        策略同步日志。

        :param sync_msg: The sync_msg of this DynamicMaskingPolicySet.
        :type sync_msg: str
        """
        self._sync_msg = sync_msg

    @property
    def create_time(self):
        r"""Gets the create_time of this DynamicMaskingPolicySet.

        策略创建时间。

        :return: The create_time of this DynamicMaskingPolicySet.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DynamicMaskingPolicySet.

        策略创建时间。

        :param create_time: The create_time of this DynamicMaskingPolicySet.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this DynamicMaskingPolicySet.

        策略创建者。

        :return: The create_user of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this DynamicMaskingPolicySet.

        策略创建者。

        :param create_user: The create_user of this DynamicMaskingPolicySet.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this DynamicMaskingPolicySet.

        策略更新时间。

        :return: The update_time of this DynamicMaskingPolicySet.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DynamicMaskingPolicySet.

        策略更新时间。

        :param update_time: The update_time of this DynamicMaskingPolicySet.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this DynamicMaskingPolicySet.

        策略更新者。

        :return: The update_user of this DynamicMaskingPolicySet.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this DynamicMaskingPolicySet.

        策略更新者。

        :param update_user: The update_user of this DynamicMaskingPolicySet.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, DynamicMaskingPolicySet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
