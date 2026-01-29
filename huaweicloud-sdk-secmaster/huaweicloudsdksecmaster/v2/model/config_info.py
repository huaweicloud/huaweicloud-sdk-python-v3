# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accounts': 'list[str]',
        'action': 'str',
        'alert': 'bool',
        'all_accounts': 'bool',
        'csvc': 'str',
        'csvc_display': 'str',
        'enable': 'int',
        'new_account_auto_access': 'bool',
        'shards': 'int',
        'source_display': 'str',
        'source_id': 'int',
        'source_name': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'accounts': 'accounts',
        'action': 'action',
        'alert': 'alert',
        'all_accounts': 'all_accounts',
        'csvc': 'csvc',
        'csvc_display': 'csvc_display',
        'enable': 'enable',
        'new_account_auto_access': 'new_account_auto_access',
        'shards': 'shards',
        'source_display': 'source_display',
        'source_id': 'source_id',
        'source_name': 'source_name',
        'ttl': 'ttl'
    }

    def __init__(self, accounts=None, action=None, alert=None, all_accounts=None, csvc=None, csvc_display=None, enable=None, new_account_auto_access=None, shards=None, source_display=None, source_id=None, source_name=None, ttl=None):
        r"""ConfigInfo

        The model defined in huaweicloud sdk

        :param accounts: 纳管账号列表(非跨账号场景不传递)
        :type accounts: list[str]
        :param action: 操作
        :type action: str
        :param alert: 自动转告警的开关
        :type alert: bool
        :param all_accounts: 是否接入已纳管的全量账号
        :type all_accounts: bool
        :param csvc: 云产品
        :type csvc: str
        :param csvc_display: 云服务描述
        :type csvc_display: str
        :param enable: 启用状态：0未启用；1启用
        :type enable: int
        :param new_account_auto_access: 新账号自动同步的开关
        :type new_account_auto_access: bool
        :param shards: 所需分区数
        :type shards: int
        :param source_display: 数据源描述
        :type source_display: str
        :param source_id: 数据源ID
        :type source_id: int
        :param source_name: 日志名称
        :type source_name: str
        :param ttl: 数据生命周期
        :type ttl: int
        """
        
        

        self._accounts = None
        self._action = None
        self._alert = None
        self._all_accounts = None
        self._csvc = None
        self._csvc_display = None
        self._enable = None
        self._new_account_auto_access = None
        self._shards = None
        self._source_display = None
        self._source_id = None
        self._source_name = None
        self._ttl = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if action is not None:
            self.action = action
        if alert is not None:
            self.alert = alert
        if all_accounts is not None:
            self.all_accounts = all_accounts
        if csvc is not None:
            self.csvc = csvc
        self.csvc_display = csvc_display
        self.enable = enable
        if new_account_auto_access is not None:
            self.new_account_auto_access = new_account_auto_access
        self.shards = shards
        self.source_display = source_display
        self.source_id = source_id
        if source_name is not None:
            self.source_name = source_name
        self.ttl = ttl

    @property
    def accounts(self):
        r"""Gets the accounts of this ConfigInfo.

        纳管账号列表(非跨账号场景不传递)

        :return: The accounts of this ConfigInfo.
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        r"""Sets the accounts of this ConfigInfo.

        纳管账号列表(非跨账号场景不传递)

        :param accounts: The accounts of this ConfigInfo.
        :type accounts: list[str]
        """
        self._accounts = accounts

    @property
    def action(self):
        r"""Gets the action of this ConfigInfo.

        操作

        :return: The action of this ConfigInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ConfigInfo.

        操作

        :param action: The action of this ConfigInfo.
        :type action: str
        """
        self._action = action

    @property
    def alert(self):
        r"""Gets the alert of this ConfigInfo.

        自动转告警的开关

        :return: The alert of this ConfigInfo.
        :rtype: bool
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        r"""Sets the alert of this ConfigInfo.

        自动转告警的开关

        :param alert: The alert of this ConfigInfo.
        :type alert: bool
        """
        self._alert = alert

    @property
    def all_accounts(self):
        r"""Gets the all_accounts of this ConfigInfo.

        是否接入已纳管的全量账号

        :return: The all_accounts of this ConfigInfo.
        :rtype: bool
        """
        return self._all_accounts

    @all_accounts.setter
    def all_accounts(self, all_accounts):
        r"""Sets the all_accounts of this ConfigInfo.

        是否接入已纳管的全量账号

        :param all_accounts: The all_accounts of this ConfigInfo.
        :type all_accounts: bool
        """
        self._all_accounts = all_accounts

    @property
    def csvc(self):
        r"""Gets the csvc of this ConfigInfo.

        云产品

        :return: The csvc of this ConfigInfo.
        :rtype: str
        """
        return self._csvc

    @csvc.setter
    def csvc(self, csvc):
        r"""Sets the csvc of this ConfigInfo.

        云产品

        :param csvc: The csvc of this ConfigInfo.
        :type csvc: str
        """
        self._csvc = csvc

    @property
    def csvc_display(self):
        r"""Gets the csvc_display of this ConfigInfo.

        云服务描述

        :return: The csvc_display of this ConfigInfo.
        :rtype: str
        """
        return self._csvc_display

    @csvc_display.setter
    def csvc_display(self, csvc_display):
        r"""Sets the csvc_display of this ConfigInfo.

        云服务描述

        :param csvc_display: The csvc_display of this ConfigInfo.
        :type csvc_display: str
        """
        self._csvc_display = csvc_display

    @property
    def enable(self):
        r"""Gets the enable of this ConfigInfo.

        启用状态：0未启用；1启用

        :return: The enable of this ConfigInfo.
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ConfigInfo.

        启用状态：0未启用；1启用

        :param enable: The enable of this ConfigInfo.
        :type enable: int
        """
        self._enable = enable

    @property
    def new_account_auto_access(self):
        r"""Gets the new_account_auto_access of this ConfigInfo.

        新账号自动同步的开关

        :return: The new_account_auto_access of this ConfigInfo.
        :rtype: bool
        """
        return self._new_account_auto_access

    @new_account_auto_access.setter
    def new_account_auto_access(self, new_account_auto_access):
        r"""Sets the new_account_auto_access of this ConfigInfo.

        新账号自动同步的开关

        :param new_account_auto_access: The new_account_auto_access of this ConfigInfo.
        :type new_account_auto_access: bool
        """
        self._new_account_auto_access = new_account_auto_access

    @property
    def shards(self):
        r"""Gets the shards of this ConfigInfo.

        所需分区数

        :return: The shards of this ConfigInfo.
        :rtype: int
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this ConfigInfo.

        所需分区数

        :param shards: The shards of this ConfigInfo.
        :type shards: int
        """
        self._shards = shards

    @property
    def source_display(self):
        r"""Gets the source_display of this ConfigInfo.

        数据源描述

        :return: The source_display of this ConfigInfo.
        :rtype: str
        """
        return self._source_display

    @source_display.setter
    def source_display(self, source_display):
        r"""Sets the source_display of this ConfigInfo.

        数据源描述

        :param source_display: The source_display of this ConfigInfo.
        :type source_display: str
        """
        self._source_display = source_display

    @property
    def source_id(self):
        r"""Gets the source_id of this ConfigInfo.

        数据源ID

        :return: The source_id of this ConfigInfo.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ConfigInfo.

        数据源ID

        :param source_id: The source_id of this ConfigInfo.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def source_name(self):
        r"""Gets the source_name of this ConfigInfo.

        日志名称

        :return: The source_name of this ConfigInfo.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this ConfigInfo.

        日志名称

        :param source_name: The source_name of this ConfigInfo.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def ttl(self):
        r"""Gets the ttl of this ConfigInfo.

        数据生命周期

        :return: The ttl of this ConfigInfo.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this ConfigInfo.

        数据生命周期

        :param ttl: The ttl of this ConfigInfo.
        :type ttl: int
        """
        self._ttl = ttl

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
        if not isinstance(other, ConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
