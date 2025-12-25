# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyDatasets:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_all_num': 'float',
        'account_successful_num': 'float',
        'accounts': 'list[ListCollectConfigResponseBodyAccounts]',
        'alert': 'bool',
        'all_accounts': 'bool',
        'allow_alert': 'bool',
        'dataspace_id': 'str',
        'dataspace_name': 'str',
        'enable': 'str',
        'last_active_time': 'float',
        'limit': 'str',
        'new_account_auto_access': 'bool',
        'process_status': 'str',
        'reference': 'ListCollectConfigResponseBodyReference',
        'region_id': 'str',
        'sink_msg': 'str',
        'source_id': 'float',
        'source_name': 'str',
        'target': 'ListCollectConfigResponseBodyTarget',
        'type': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'account_all_num': 'account_all_num',
        'account_successful_num': 'account_successful_num',
        'accounts': 'accounts',
        'alert': 'alert',
        'all_accounts': 'all_accounts',
        'allow_alert': 'allow_alert',
        'dataspace_id': 'dataspace_id',
        'dataspace_name': 'dataspace_name',
        'enable': 'enable',
        'last_active_time': 'last_active_time',
        'limit': 'limit',
        'new_account_auto_access': 'new_account_auto_access',
        'process_status': 'process_status',
        'reference': 'reference',
        'region_id': 'region_id',
        'sink_msg': 'sink_msg',
        'source_id': 'source_id',
        'source_name': 'source_name',
        'target': 'target',
        'type': 'type',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, account_all_num=None, account_successful_num=None, accounts=None, alert=None, all_accounts=None, allow_alert=None, dataspace_id=None, dataspace_name=None, enable=None, last_active_time=None, limit=None, new_account_auto_access=None, process_status=None, reference=None, region_id=None, sink_msg=None, source_id=None, source_name=None, target=None, type=None, workspace_id=None):
        r"""ListCollectConfigResponseBodyDatasets

        The model defined in huaweicloud sdk

        :param account_all_num: 接入账号总数量
        :type account_all_num: float
        :param account_successful_num: 成功接入账号数量
        :type account_successful_num: float
        :param accounts: 账号列表
        :type accounts: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyAccounts`]
        :param alert: 自动转告警开关
        :type alert: bool
        :param all_accounts: 是否接入已纳管的全量账号
        :type all_accounts: bool
        :param allow_alert: 能否开自动转告警
        :type allow_alert: bool
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param enable: 开启状态
        :type enable: str
        :param last_active_time: 上次活跃时间
        :type last_active_time: float
        :param limit: 限制
        :type limit: str
        :param new_account_auto_access: 新账号自动接入开关
        :type new_account_auto_access: bool
        :param process_status: 日志的接入状态,可能的值为FAIL,DEFAULT,CREATING,SUCCESS,FAIL表示失败,DEFAULT表示待接入,CREATING表示接入中,SUCCESS表示成功
        :type process_status: str
        :param reference: 
        :type reference: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyReference`
        :param region_id: 所属区域
        :type region_id: str
        :param sink_msg: 错误信息
        :type sink_msg: str
        :param source_id: 日志ID
        :type source_id: float
        :param source_name: 日志名称
        :type source_name: str
        :param target: 
        :type target: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyTarget`
        :param type: 类型
        :type type: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        """
        
        

        self._account_all_num = None
        self._account_successful_num = None
        self._accounts = None
        self._alert = None
        self._all_accounts = None
        self._allow_alert = None
        self._dataspace_id = None
        self._dataspace_name = None
        self._enable = None
        self._last_active_time = None
        self._limit = None
        self._new_account_auto_access = None
        self._process_status = None
        self._reference = None
        self._region_id = None
        self._sink_msg = None
        self._source_id = None
        self._source_name = None
        self._target = None
        self._type = None
        self._workspace_id = None
        self.discriminator = None

        if account_all_num is not None:
            self.account_all_num = account_all_num
        if account_successful_num is not None:
            self.account_successful_num = account_successful_num
        if accounts is not None:
            self.accounts = accounts
        if alert is not None:
            self.alert = alert
        if all_accounts is not None:
            self.all_accounts = all_accounts
        if allow_alert is not None:
            self.allow_alert = allow_alert
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if dataspace_name is not None:
            self.dataspace_name = dataspace_name
        if enable is not None:
            self.enable = enable
        if last_active_time is not None:
            self.last_active_time = last_active_time
        if limit is not None:
            self.limit = limit
        if new_account_auto_access is not None:
            self.new_account_auto_access = new_account_auto_access
        if process_status is not None:
            self.process_status = process_status
        if reference is not None:
            self.reference = reference
        if region_id is not None:
            self.region_id = region_id
        if sink_msg is not None:
            self.sink_msg = sink_msg
        if source_id is not None:
            self.source_id = source_id
        if source_name is not None:
            self.source_name = source_name
        if target is not None:
            self.target = target
        if type is not None:
            self.type = type
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def account_all_num(self):
        r"""Gets the account_all_num of this ListCollectConfigResponseBodyDatasets.

        接入账号总数量

        :return: The account_all_num of this ListCollectConfigResponseBodyDatasets.
        :rtype: float
        """
        return self._account_all_num

    @account_all_num.setter
    def account_all_num(self, account_all_num):
        r"""Sets the account_all_num of this ListCollectConfigResponseBodyDatasets.

        接入账号总数量

        :param account_all_num: The account_all_num of this ListCollectConfigResponseBodyDatasets.
        :type account_all_num: float
        """
        self._account_all_num = account_all_num

    @property
    def account_successful_num(self):
        r"""Gets the account_successful_num of this ListCollectConfigResponseBodyDatasets.

        成功接入账号数量

        :return: The account_successful_num of this ListCollectConfigResponseBodyDatasets.
        :rtype: float
        """
        return self._account_successful_num

    @account_successful_num.setter
    def account_successful_num(self, account_successful_num):
        r"""Sets the account_successful_num of this ListCollectConfigResponseBodyDatasets.

        成功接入账号数量

        :param account_successful_num: The account_successful_num of this ListCollectConfigResponseBodyDatasets.
        :type account_successful_num: float
        """
        self._account_successful_num = account_successful_num

    @property
    def accounts(self):
        r"""Gets the accounts of this ListCollectConfigResponseBodyDatasets.

        账号列表

        :return: The accounts of this ListCollectConfigResponseBodyDatasets.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyAccounts`]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        r"""Sets the accounts of this ListCollectConfigResponseBodyDatasets.

        账号列表

        :param accounts: The accounts of this ListCollectConfigResponseBodyDatasets.
        :type accounts: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyAccounts`]
        """
        self._accounts = accounts

    @property
    def alert(self):
        r"""Gets the alert of this ListCollectConfigResponseBodyDatasets.

        自动转告警开关

        :return: The alert of this ListCollectConfigResponseBodyDatasets.
        :rtype: bool
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        r"""Sets the alert of this ListCollectConfigResponseBodyDatasets.

        自动转告警开关

        :param alert: The alert of this ListCollectConfigResponseBodyDatasets.
        :type alert: bool
        """
        self._alert = alert

    @property
    def all_accounts(self):
        r"""Gets the all_accounts of this ListCollectConfigResponseBodyDatasets.

        是否接入已纳管的全量账号

        :return: The all_accounts of this ListCollectConfigResponseBodyDatasets.
        :rtype: bool
        """
        return self._all_accounts

    @all_accounts.setter
    def all_accounts(self, all_accounts):
        r"""Sets the all_accounts of this ListCollectConfigResponseBodyDatasets.

        是否接入已纳管的全量账号

        :param all_accounts: The all_accounts of this ListCollectConfigResponseBodyDatasets.
        :type all_accounts: bool
        """
        self._all_accounts = all_accounts

    @property
    def allow_alert(self):
        r"""Gets the allow_alert of this ListCollectConfigResponseBodyDatasets.

        能否开自动转告警

        :return: The allow_alert of this ListCollectConfigResponseBodyDatasets.
        :rtype: bool
        """
        return self._allow_alert

    @allow_alert.setter
    def allow_alert(self, allow_alert):
        r"""Sets the allow_alert of this ListCollectConfigResponseBodyDatasets.

        能否开自动转告警

        :param allow_alert: The allow_alert of this ListCollectConfigResponseBodyDatasets.
        :type allow_alert: bool
        """
        self._allow_alert = allow_alert

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this ListCollectConfigResponseBodyDatasets.

        数据空间ID

        :return: The dataspace_id of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this ListCollectConfigResponseBodyDatasets.

        数据空间ID

        :param dataspace_id: The dataspace_id of this ListCollectConfigResponseBodyDatasets.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this ListCollectConfigResponseBodyDatasets.

        数据空间名称

        :return: The dataspace_name of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this ListCollectConfigResponseBodyDatasets.

        数据空间名称

        :param dataspace_name: The dataspace_name of this ListCollectConfigResponseBodyDatasets.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def enable(self):
        r"""Gets the enable of this ListCollectConfigResponseBodyDatasets.

        开启状态

        :return: The enable of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ListCollectConfigResponseBodyDatasets.

        开启状态

        :param enable: The enable of this ListCollectConfigResponseBodyDatasets.
        :type enable: str
        """
        self._enable = enable

    @property
    def last_active_time(self):
        r"""Gets the last_active_time of this ListCollectConfigResponseBodyDatasets.

        上次活跃时间

        :return: The last_active_time of this ListCollectConfigResponseBodyDatasets.
        :rtype: float
        """
        return self._last_active_time

    @last_active_time.setter
    def last_active_time(self, last_active_time):
        r"""Sets the last_active_time of this ListCollectConfigResponseBodyDatasets.

        上次活跃时间

        :param last_active_time: The last_active_time of this ListCollectConfigResponseBodyDatasets.
        :type last_active_time: float
        """
        self._last_active_time = last_active_time

    @property
    def limit(self):
        r"""Gets the limit of this ListCollectConfigResponseBodyDatasets.

        限制

        :return: The limit of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCollectConfigResponseBodyDatasets.

        限制

        :param limit: The limit of this ListCollectConfigResponseBodyDatasets.
        :type limit: str
        """
        self._limit = limit

    @property
    def new_account_auto_access(self):
        r"""Gets the new_account_auto_access of this ListCollectConfigResponseBodyDatasets.

        新账号自动接入开关

        :return: The new_account_auto_access of this ListCollectConfigResponseBodyDatasets.
        :rtype: bool
        """
        return self._new_account_auto_access

    @new_account_auto_access.setter
    def new_account_auto_access(self, new_account_auto_access):
        r"""Sets the new_account_auto_access of this ListCollectConfigResponseBodyDatasets.

        新账号自动接入开关

        :param new_account_auto_access: The new_account_auto_access of this ListCollectConfigResponseBodyDatasets.
        :type new_account_auto_access: bool
        """
        self._new_account_auto_access = new_account_auto_access

    @property
    def process_status(self):
        r"""Gets the process_status of this ListCollectConfigResponseBodyDatasets.

        日志的接入状态,可能的值为FAIL,DEFAULT,CREATING,SUCCESS,FAIL表示失败,DEFAULT表示待接入,CREATING表示接入中,SUCCESS表示成功

        :return: The process_status of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this ListCollectConfigResponseBodyDatasets.

        日志的接入状态,可能的值为FAIL,DEFAULT,CREATING,SUCCESS,FAIL表示失败,DEFAULT表示待接入,CREATING表示接入中,SUCCESS表示成功

        :param process_status: The process_status of this ListCollectConfigResponseBodyDatasets.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def reference(self):
        r"""Gets the reference of this ListCollectConfigResponseBodyDatasets.

        :return: The reference of this ListCollectConfigResponseBodyDatasets.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyReference`
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this ListCollectConfigResponseBodyDatasets.

        :param reference: The reference of this ListCollectConfigResponseBodyDatasets.
        :type reference: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyReference`
        """
        self._reference = reference

    @property
    def region_id(self):
        r"""Gets the region_id of this ListCollectConfigResponseBodyDatasets.

        所属区域

        :return: The region_id of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListCollectConfigResponseBodyDatasets.

        所属区域

        :param region_id: The region_id of this ListCollectConfigResponseBodyDatasets.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def sink_msg(self):
        r"""Gets the sink_msg of this ListCollectConfigResponseBodyDatasets.

        错误信息

        :return: The sink_msg of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._sink_msg

    @sink_msg.setter
    def sink_msg(self, sink_msg):
        r"""Sets the sink_msg of this ListCollectConfigResponseBodyDatasets.

        错误信息

        :param sink_msg: The sink_msg of this ListCollectConfigResponseBodyDatasets.
        :type sink_msg: str
        """
        self._sink_msg = sink_msg

    @property
    def source_id(self):
        r"""Gets the source_id of this ListCollectConfigResponseBodyDatasets.

        日志ID

        :return: The source_id of this ListCollectConfigResponseBodyDatasets.
        :rtype: float
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ListCollectConfigResponseBodyDatasets.

        日志ID

        :param source_id: The source_id of this ListCollectConfigResponseBodyDatasets.
        :type source_id: float
        """
        self._source_id = source_id

    @property
    def source_name(self):
        r"""Gets the source_name of this ListCollectConfigResponseBodyDatasets.

        日志名称

        :return: The source_name of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this ListCollectConfigResponseBodyDatasets.

        日志名称

        :param source_name: The source_name of this ListCollectConfigResponseBodyDatasets.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def target(self):
        r"""Gets the target of this ListCollectConfigResponseBodyDatasets.

        :return: The target of this ListCollectConfigResponseBodyDatasets.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyTarget`
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this ListCollectConfigResponseBodyDatasets.

        :param target: The target of this ListCollectConfigResponseBodyDatasets.
        :type target: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyTarget`
        """
        self._target = target

    @property
    def type(self):
        r"""Gets the type of this ListCollectConfigResponseBodyDatasets.

        类型

        :return: The type of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCollectConfigResponseBodyDatasets.

        类型

        :param type: The type of this ListCollectConfigResponseBodyDatasets.
        :type type: str
        """
        self._type = type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListCollectConfigResponseBodyDatasets.

        工作空间ID

        :return: The workspace_id of this ListCollectConfigResponseBodyDatasets.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListCollectConfigResponseBodyDatasets.

        工作空间ID

        :param workspace_id: The workspace_id of this ListCollectConfigResponseBodyDatasets.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ListCollectConfigResponseBodyDatasets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
