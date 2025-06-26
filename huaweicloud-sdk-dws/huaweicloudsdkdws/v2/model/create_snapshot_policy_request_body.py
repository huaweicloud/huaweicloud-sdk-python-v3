# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSnapshotPolicyRequestBody:

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
        'backup_strategies': 'list[BackupStrategyRequest]',
        'device_name': 'str',
        'server_port': 'str',
        'backup_param': 'str',
        'server_ips': 'list[str]'
    }

    attribute_map = {
        'keep_day': 'keep_day',
        'backup_strategies': 'backup_strategies',
        'device_name': 'device_name',
        'server_port': 'server_port',
        'backup_param': 'backup_param',
        'server_ips': 'server_ips'
    }

    def __init__(self, keep_day=None, backup_strategies=None, device_name=None, server_port=None, backup_param=None, server_ips=None):
        r"""CreateSnapshotPolicyRequestBody

        The model defined in huaweicloud sdk

        :param keep_day: **参数解释**： 保留天数。 **取值范围**： 输入值必须在1-31之间。
        :type keep_day: int
        :param backup_strategies: **参数解释**： 策略列表信息。当需要添加策略时该参数为必选。 **取值范围**： 不涉及。
        :type backup_strategies: list[:class:`huaweicloudsdkdws.v2.BackupStrategyRequest`]
        :param device_name: **参数解释**： 备份设备。支持OBS、NBU和NFS。 **取值范围**： 不涉及。
        :type device_name: str
        :param server_port: **参数解释**： NBU备份介质端口。备份介质为NBU时该字段必填。 **取值范围**： 不涉及。
        :type server_port: str
        :param backup_param: **参数解释**： NBU备份参数。备份介质为NBU时该字段必选。 **取值范围**： 不涉及。
        :type backup_param: str
        :param server_ips: **参数解释**： 备份介质服务IP。备份介质为NBU和NFS时该字段必填。备份介质为NBU时表示NBU服务器地址，备份介质为NFS时表示NFS服务器地址。 **取值范围**： 不涉及。
        :type server_ips: list[str]
        """
        
        

        self._keep_day = None
        self._backup_strategies = None
        self._device_name = None
        self._server_port = None
        self._backup_param = None
        self._server_ips = None
        self.discriminator = None

        if keep_day is not None:
            self.keep_day = keep_day
        if backup_strategies is not None:
            self.backup_strategies = backup_strategies
        if device_name is not None:
            self.device_name = device_name
        if server_port is not None:
            self.server_port = server_port
        if backup_param is not None:
            self.backup_param = backup_param
        if server_ips is not None:
            self.server_ips = server_ips

    @property
    def keep_day(self):
        r"""Gets the keep_day of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 保留天数。 **取值范围**： 输入值必须在1-31之间。

        :return: The keep_day of this CreateSnapshotPolicyRequestBody.
        :rtype: int
        """
        return self._keep_day

    @keep_day.setter
    def keep_day(self, keep_day):
        r"""Sets the keep_day of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 保留天数。 **取值范围**： 输入值必须在1-31之间。

        :param keep_day: The keep_day of this CreateSnapshotPolicyRequestBody.
        :type keep_day: int
        """
        self._keep_day = keep_day

    @property
    def backup_strategies(self):
        r"""Gets the backup_strategies of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 策略列表信息。当需要添加策略时该参数为必选。 **取值范围**： 不涉及。

        :return: The backup_strategies of this CreateSnapshotPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkdws.v2.BackupStrategyRequest`]
        """
        return self._backup_strategies

    @backup_strategies.setter
    def backup_strategies(self, backup_strategies):
        r"""Sets the backup_strategies of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 策略列表信息。当需要添加策略时该参数为必选。 **取值范围**： 不涉及。

        :param backup_strategies: The backup_strategies of this CreateSnapshotPolicyRequestBody.
        :type backup_strategies: list[:class:`huaweicloudsdkdws.v2.BackupStrategyRequest`]
        """
        self._backup_strategies = backup_strategies

    @property
    def device_name(self):
        r"""Gets the device_name of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 备份设备。支持OBS、NBU和NFS。 **取值范围**： 不涉及。

        :return: The device_name of this CreateSnapshotPolicyRequestBody.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 备份设备。支持OBS、NBU和NFS。 **取值范围**： 不涉及。

        :param device_name: The device_name of this CreateSnapshotPolicyRequestBody.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def server_port(self):
        r"""Gets the server_port of this CreateSnapshotPolicyRequestBody.

        **参数解释**： NBU备份介质端口。备份介质为NBU时该字段必填。 **取值范围**： 不涉及。

        :return: The server_port of this CreateSnapshotPolicyRequestBody.
        :rtype: str
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        r"""Sets the server_port of this CreateSnapshotPolicyRequestBody.

        **参数解释**： NBU备份介质端口。备份介质为NBU时该字段必填。 **取值范围**： 不涉及。

        :param server_port: The server_port of this CreateSnapshotPolicyRequestBody.
        :type server_port: str
        """
        self._server_port = server_port

    @property
    def backup_param(self):
        r"""Gets the backup_param of this CreateSnapshotPolicyRequestBody.

        **参数解释**： NBU备份参数。备份介质为NBU时该字段必选。 **取值范围**： 不涉及。

        :return: The backup_param of this CreateSnapshotPolicyRequestBody.
        :rtype: str
        """
        return self._backup_param

    @backup_param.setter
    def backup_param(self, backup_param):
        r"""Sets the backup_param of this CreateSnapshotPolicyRequestBody.

        **参数解释**： NBU备份参数。备份介质为NBU时该字段必选。 **取值范围**： 不涉及。

        :param backup_param: The backup_param of this CreateSnapshotPolicyRequestBody.
        :type backup_param: str
        """
        self._backup_param = backup_param

    @property
    def server_ips(self):
        r"""Gets the server_ips of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 备份介质服务IP。备份介质为NBU和NFS时该字段必填。备份介质为NBU时表示NBU服务器地址，备份介质为NFS时表示NFS服务器地址。 **取值范围**： 不涉及。

        :return: The server_ips of this CreateSnapshotPolicyRequestBody.
        :rtype: list[str]
        """
        return self._server_ips

    @server_ips.setter
    def server_ips(self, server_ips):
        r"""Sets the server_ips of this CreateSnapshotPolicyRequestBody.

        **参数解释**： 备份介质服务IP。备份介质为NBU和NFS时该字段必填。备份介质为NBU时表示NBU服务器地址，备份介质为NFS时表示NFS服务器地址。 **取值范围**： 不涉及。

        :param server_ips: The server_ips of this CreateSnapshotPolicyRequestBody.
        :type server_ips: list[str]
        """
        self._server_ips = server_ips

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
        if not isinstance(other, CreateSnapshotPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
