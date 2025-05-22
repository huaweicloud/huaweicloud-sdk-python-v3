# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_day': 'int',
        'backup_strategies': 'list[BackupStrategyDetail]',
        'device_name': 'str',
        'server_ips': 'list[str]',
        'server_port': 'str',
        'backup_param': 'str',
        'auto_backup': 'bool',
        'backup_strategy_cluster_type_limit_num': 'int',
        'backup_strategy_schema_type_limit_num': 'int'
    }

    attribute_map = {
        'keep_day': 'keep_day',
        'backup_strategies': 'backup_strategies',
        'device_name': 'device_name',
        'server_ips': 'server_ips',
        'server_port': 'server_port',
        'backup_param': 'backup_param',
        'auto_backup': 'auto_backup',
        'backup_strategy_cluster_type_limit_num': 'backup_strategy_cluster_type_limit_num',
        'backup_strategy_schema_type_limit_num': 'backup_strategy_schema_type_limit_num'
    }

    def __init__(self, keep_day=None, backup_strategies=None, device_name=None, server_ips=None, server_port=None, backup_param=None, auto_backup=None, backup_strategy_cluster_type_limit_num=None, backup_strategy_schema_type_limit_num=None):
        r"""ListSnapshotPolicyResponse

        The model defined in huaweicloud sdk

        :param keep_day: **参数解释**： 保留天数。 **取值范围**： 大于等于0。
        :type keep_day: int
        :param backup_strategies: **参数解释**： 备份策略列表。 **取值范围**： 不涉及。
        :type backup_strategies: list[:class:`huaweicloudsdkdws.v2.BackupStrategyDetail`]
        :param device_name: **参数解释**： 备份设备，一般为OBS。 **取值范围**： 不涉及。
        :type device_name: str
        :param server_ips: **参数解释**： 服务IP。 **取值范围**： 不涉及。
        :type server_ips: list[str]
        :param server_port: **参数解释**： 服务端口。 **取值范围**： 不涉及。
        :type server_port: str
        :param backup_param: **参数解释**： 备份参数。 **取值范围**： 不涉及。
        :type backup_param: str
        :param auto_backup: **参数解释**： 自动备份开关状态。 **取值范围**： true：已开启自动备份选项； false：已关闭自动备份选项；
        :type auto_backup: bool
        :param backup_strategy_cluster_type_limit_num: **参数解释**： 此策略下集群级快照最大数量。 **取值范围**： 大于等于0。
        :type backup_strategy_cluster_type_limit_num: int
        :param backup_strategy_schema_type_limit_num: **参数解释**： 此策略下schema级快照最大数量。 **取值范围**： 大于等于0。
        :type backup_strategy_schema_type_limit_num: int
        """
        
        super(ListSnapshotPolicyResponse, self).__init__()

        self._keep_day = None
        self._backup_strategies = None
        self._device_name = None
        self._server_ips = None
        self._server_port = None
        self._backup_param = None
        self._auto_backup = None
        self._backup_strategy_cluster_type_limit_num = None
        self._backup_strategy_schema_type_limit_num = None
        self.discriminator = None

        if keep_day is not None:
            self.keep_day = keep_day
        if backup_strategies is not None:
            self.backup_strategies = backup_strategies
        if device_name is not None:
            self.device_name = device_name
        if server_ips is not None:
            self.server_ips = server_ips
        if server_port is not None:
            self.server_port = server_port
        if backup_param is not None:
            self.backup_param = backup_param
        if auto_backup is not None:
            self.auto_backup = auto_backup
        if backup_strategy_cluster_type_limit_num is not None:
            self.backup_strategy_cluster_type_limit_num = backup_strategy_cluster_type_limit_num
        if backup_strategy_schema_type_limit_num is not None:
            self.backup_strategy_schema_type_limit_num = backup_strategy_schema_type_limit_num

    @property
    def keep_day(self):
        r"""Gets the keep_day of this ListSnapshotPolicyResponse.

        **参数解释**： 保留天数。 **取值范围**： 大于等于0。

        :return: The keep_day of this ListSnapshotPolicyResponse.
        :rtype: int
        """
        return self._keep_day

    @keep_day.setter
    def keep_day(self, keep_day):
        r"""Sets the keep_day of this ListSnapshotPolicyResponse.

        **参数解释**： 保留天数。 **取值范围**： 大于等于0。

        :param keep_day: The keep_day of this ListSnapshotPolicyResponse.
        :type keep_day: int
        """
        self._keep_day = keep_day

    @property
    def backup_strategies(self):
        r"""Gets the backup_strategies of this ListSnapshotPolicyResponse.

        **参数解释**： 备份策略列表。 **取值范围**： 不涉及。

        :return: The backup_strategies of this ListSnapshotPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.BackupStrategyDetail`]
        """
        return self._backup_strategies

    @backup_strategies.setter
    def backup_strategies(self, backup_strategies):
        r"""Sets the backup_strategies of this ListSnapshotPolicyResponse.

        **参数解释**： 备份策略列表。 **取值范围**： 不涉及。

        :param backup_strategies: The backup_strategies of this ListSnapshotPolicyResponse.
        :type backup_strategies: list[:class:`huaweicloudsdkdws.v2.BackupStrategyDetail`]
        """
        self._backup_strategies = backup_strategies

    @property
    def device_name(self):
        r"""Gets the device_name of this ListSnapshotPolicyResponse.

        **参数解释**： 备份设备，一般为OBS。 **取值范围**： 不涉及。

        :return: The device_name of this ListSnapshotPolicyResponse.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this ListSnapshotPolicyResponse.

        **参数解释**： 备份设备，一般为OBS。 **取值范围**： 不涉及。

        :param device_name: The device_name of this ListSnapshotPolicyResponse.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def server_ips(self):
        r"""Gets the server_ips of this ListSnapshotPolicyResponse.

        **参数解释**： 服务IP。 **取值范围**： 不涉及。

        :return: The server_ips of this ListSnapshotPolicyResponse.
        :rtype: list[str]
        """
        return self._server_ips

    @server_ips.setter
    def server_ips(self, server_ips):
        r"""Sets the server_ips of this ListSnapshotPolicyResponse.

        **参数解释**： 服务IP。 **取值范围**： 不涉及。

        :param server_ips: The server_ips of this ListSnapshotPolicyResponse.
        :type server_ips: list[str]
        """
        self._server_ips = server_ips

    @property
    def server_port(self):
        r"""Gets the server_port of this ListSnapshotPolicyResponse.

        **参数解释**： 服务端口。 **取值范围**： 不涉及。

        :return: The server_port of this ListSnapshotPolicyResponse.
        :rtype: str
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        r"""Sets the server_port of this ListSnapshotPolicyResponse.

        **参数解释**： 服务端口。 **取值范围**： 不涉及。

        :param server_port: The server_port of this ListSnapshotPolicyResponse.
        :type server_port: str
        """
        self._server_port = server_port

    @property
    def backup_param(self):
        r"""Gets the backup_param of this ListSnapshotPolicyResponse.

        **参数解释**： 备份参数。 **取值范围**： 不涉及。

        :return: The backup_param of this ListSnapshotPolicyResponse.
        :rtype: str
        """
        return self._backup_param

    @backup_param.setter
    def backup_param(self, backup_param):
        r"""Sets the backup_param of this ListSnapshotPolicyResponse.

        **参数解释**： 备份参数。 **取值范围**： 不涉及。

        :param backup_param: The backup_param of this ListSnapshotPolicyResponse.
        :type backup_param: str
        """
        self._backup_param = backup_param

    @property
    def auto_backup(self):
        r"""Gets the auto_backup of this ListSnapshotPolicyResponse.

        **参数解释**： 自动备份开关状态。 **取值范围**： true：已开启自动备份选项； false：已关闭自动备份选项；

        :return: The auto_backup of this ListSnapshotPolicyResponse.
        :rtype: bool
        """
        return self._auto_backup

    @auto_backup.setter
    def auto_backup(self, auto_backup):
        r"""Sets the auto_backup of this ListSnapshotPolicyResponse.

        **参数解释**： 自动备份开关状态。 **取值范围**： true：已开启自动备份选项； false：已关闭自动备份选项；

        :param auto_backup: The auto_backup of this ListSnapshotPolicyResponse.
        :type auto_backup: bool
        """
        self._auto_backup = auto_backup

    @property
    def backup_strategy_cluster_type_limit_num(self):
        r"""Gets the backup_strategy_cluster_type_limit_num of this ListSnapshotPolicyResponse.

        **参数解释**： 此策略下集群级快照最大数量。 **取值范围**： 大于等于0。

        :return: The backup_strategy_cluster_type_limit_num of this ListSnapshotPolicyResponse.
        :rtype: int
        """
        return self._backup_strategy_cluster_type_limit_num

    @backup_strategy_cluster_type_limit_num.setter
    def backup_strategy_cluster_type_limit_num(self, backup_strategy_cluster_type_limit_num):
        r"""Sets the backup_strategy_cluster_type_limit_num of this ListSnapshotPolicyResponse.

        **参数解释**： 此策略下集群级快照最大数量。 **取值范围**： 大于等于0。

        :param backup_strategy_cluster_type_limit_num: The backup_strategy_cluster_type_limit_num of this ListSnapshotPolicyResponse.
        :type backup_strategy_cluster_type_limit_num: int
        """
        self._backup_strategy_cluster_type_limit_num = backup_strategy_cluster_type_limit_num

    @property
    def backup_strategy_schema_type_limit_num(self):
        r"""Gets the backup_strategy_schema_type_limit_num of this ListSnapshotPolicyResponse.

        **参数解释**： 此策略下schema级快照最大数量。 **取值范围**： 大于等于0。

        :return: The backup_strategy_schema_type_limit_num of this ListSnapshotPolicyResponse.
        :rtype: int
        """
        return self._backup_strategy_schema_type_limit_num

    @backup_strategy_schema_type_limit_num.setter
    def backup_strategy_schema_type_limit_num(self, backup_strategy_schema_type_limit_num):
        r"""Sets the backup_strategy_schema_type_limit_num of this ListSnapshotPolicyResponse.

        **参数解释**： 此策略下schema级快照最大数量。 **取值范围**： 大于等于0。

        :param backup_strategy_schema_type_limit_num: The backup_strategy_schema_type_limit_num of this ListSnapshotPolicyResponse.
        :type backup_strategy_schema_type_limit_num: int
        """
        self._backup_strategy_schema_type_limit_num = backup_strategy_schema_type_limit_num

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
        if not isinstance(other, ListSnapshotPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
