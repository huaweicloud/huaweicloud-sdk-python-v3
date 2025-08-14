# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerHdaUpgradeRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'machine_name': 'str',
        'server_name': 'str',
        'server_group_name': 'str',
        'sid': 'str',
        'current_version': 'str',
        'target_version': 'str',
        'upgrade_status': 'str',
        'upgrade_time': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'machine_name': 'machine_name',
        'server_name': 'server_name',
        'server_group_name': 'server_group_name',
        'sid': 'sid',
        'current_version': 'current_version',
        'target_version': 'target_version',
        'upgrade_status': 'upgrade_status',
        'upgrade_time': 'upgrade_time'
    }

    def __init__(self, server_id=None, machine_name=None, server_name=None, server_group_name=None, sid=None, current_version=None, target_version=None, upgrade_status=None, upgrade_time=None):
        r"""ServerHdaUpgradeRecord

        The model defined in huaweicloud sdk

        :param server_id: 服务器id。
        :type server_id: str
        :param machine_name: 机器名称。
        :type machine_name: str
        :param server_name: 服务器名称。
        :type server_name: str
        :param server_group_name: 服务器组名称。
        :type server_group_name: str
        :param sid: 服务器的sid。
        :type sid: str
        :param current_version: 当前的accessAgent版本。
        :type current_version: str
        :param target_version: 目标的accessAgent版本。
        :type target_version: str
        :param upgrade_status: HDA升级状态。
        :type upgrade_status: str
        :param upgrade_time: 更新时间。
        :type upgrade_time: str
        """
        
        

        self._server_id = None
        self._machine_name = None
        self._server_name = None
        self._server_group_name = None
        self._sid = None
        self._current_version = None
        self._target_version = None
        self._upgrade_status = None
        self._upgrade_time = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if machine_name is not None:
            self.machine_name = machine_name
        if server_name is not None:
            self.server_name = server_name
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if sid is not None:
            self.sid = sid
        if current_version is not None:
            self.current_version = current_version
        if target_version is not None:
            self.target_version = target_version
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status
        if upgrade_time is not None:
            self.upgrade_time = upgrade_time

    @property
    def server_id(self):
        r"""Gets the server_id of this ServerHdaUpgradeRecord.

        服务器id。

        :return: The server_id of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ServerHdaUpgradeRecord.

        服务器id。

        :param server_id: The server_id of this ServerHdaUpgradeRecord.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def machine_name(self):
        r"""Gets the machine_name of this ServerHdaUpgradeRecord.

        机器名称。

        :return: The machine_name of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        r"""Sets the machine_name of this ServerHdaUpgradeRecord.

        机器名称。

        :param machine_name: The machine_name of this ServerHdaUpgradeRecord.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def server_name(self):
        r"""Gets the server_name of this ServerHdaUpgradeRecord.

        服务器名称。

        :return: The server_name of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ServerHdaUpgradeRecord.

        服务器名称。

        :param server_name: The server_name of this ServerHdaUpgradeRecord.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_group_name(self):
        r"""Gets the server_group_name of this ServerHdaUpgradeRecord.

        服务器组名称。

        :return: The server_group_name of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        r"""Sets the server_group_name of this ServerHdaUpgradeRecord.

        服务器组名称。

        :param server_group_name: The server_group_name of this ServerHdaUpgradeRecord.
        :type server_group_name: str
        """
        self._server_group_name = server_group_name

    @property
    def sid(self):
        r"""Gets the sid of this ServerHdaUpgradeRecord.

        服务器的sid。

        :return: The sid of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this ServerHdaUpgradeRecord.

        服务器的sid。

        :param sid: The sid of this ServerHdaUpgradeRecord.
        :type sid: str
        """
        self._sid = sid

    @property
    def current_version(self):
        r"""Gets the current_version of this ServerHdaUpgradeRecord.

        当前的accessAgent版本。

        :return: The current_version of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this ServerHdaUpgradeRecord.

        当前的accessAgent版本。

        :param current_version: The current_version of this ServerHdaUpgradeRecord.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def target_version(self):
        r"""Gets the target_version of this ServerHdaUpgradeRecord.

        目标的accessAgent版本。

        :return: The target_version of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ServerHdaUpgradeRecord.

        目标的accessAgent版本。

        :param target_version: The target_version of this ServerHdaUpgradeRecord.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def upgrade_status(self):
        r"""Gets the upgrade_status of this ServerHdaUpgradeRecord.

        HDA升级状态。

        :return: The upgrade_status of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        r"""Sets the upgrade_status of this ServerHdaUpgradeRecord.

        HDA升级状态。

        :param upgrade_status: The upgrade_status of this ServerHdaUpgradeRecord.
        :type upgrade_status: str
        """
        self._upgrade_status = upgrade_status

    @property
    def upgrade_time(self):
        r"""Gets the upgrade_time of this ServerHdaUpgradeRecord.

        更新时间。

        :return: The upgrade_time of this ServerHdaUpgradeRecord.
        :rtype: str
        """
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, upgrade_time):
        r"""Sets the upgrade_time of this ServerHdaUpgradeRecord.

        更新时间。

        :param upgrade_time: The upgrade_time of this ServerHdaUpgradeRecord.
        :type upgrade_time: str
        """
        self._upgrade_time = upgrade_time

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
        if not isinstance(other, ServerHdaUpgradeRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
