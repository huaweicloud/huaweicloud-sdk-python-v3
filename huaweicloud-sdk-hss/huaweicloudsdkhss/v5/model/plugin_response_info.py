# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'os_type': 'str',
        'plugin_name': 'str',
        'plugin_version': 'str',
        'plugin_status': 'str',
        'upgrade_status': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'os_type': 'os_type',
        'plugin_name': 'plugin_name',
        'plugin_version': 'plugin_version',
        'plugin_status': 'plugin_status',
        'upgrade_status': 'upgrade_status'
    }

    def __init__(self, host_name=None, host_id=None, private_ip=None, public_ip=None, os_type=None, plugin_name=None, plugin_version=None, plugin_status=None, upgrade_status=None):
        r"""PluginResponseInfo

        The model defined in huaweicloud sdk

        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param private_ip: 私有IP地址
        :type private_ip: str
        :param public_ip: 公有IP地址
        :type public_ip: str
        :param os_type: 系统类型
        :type os_type: str
        :param plugin_name: 插件名称
        :type plugin_name: str
        :param plugin_version: 插件版本
        :type plugin_version: str
        :param plugin_status: 插件状态
        :type plugin_status: str
        :param upgrade_status: 插件升级状态
        :type upgrade_status: str
        """
        
        

        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._os_type = None
        self._plugin_name = None
        self._plugin_version = None
        self._plugin_status = None
        self._upgrade_status = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if os_type is not None:
            self.os_type = os_type
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if plugin_status is not None:
            self.plugin_status = plugin_status
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status

    @property
    def host_name(self):
        r"""Gets the host_name of this PluginResponseInfo.

        服务器名称

        :return: The host_name of this PluginResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this PluginResponseInfo.

        服务器名称

        :param host_name: The host_name of this PluginResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this PluginResponseInfo.

        服务器ID

        :return: The host_id of this PluginResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this PluginResponseInfo.

        服务器ID

        :param host_id: The host_id of this PluginResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this PluginResponseInfo.

        私有IP地址

        :return: The private_ip of this PluginResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this PluginResponseInfo.

        私有IP地址

        :param private_ip: The private_ip of this PluginResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this PluginResponseInfo.

        公有IP地址

        :return: The public_ip of this PluginResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this PluginResponseInfo.

        公有IP地址

        :param public_ip: The public_ip of this PluginResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def os_type(self):
        r"""Gets the os_type of this PluginResponseInfo.

        系统类型

        :return: The os_type of this PluginResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this PluginResponseInfo.

        系统类型

        :param os_type: The os_type of this PluginResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this PluginResponseInfo.

        插件名称

        :return: The plugin_name of this PluginResponseInfo.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this PluginResponseInfo.

        插件名称

        :param plugin_name: The plugin_name of this PluginResponseInfo.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this PluginResponseInfo.

        插件版本

        :return: The plugin_version of this PluginResponseInfo.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this PluginResponseInfo.

        插件版本

        :param plugin_version: The plugin_version of this PluginResponseInfo.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def plugin_status(self):
        r"""Gets the plugin_status of this PluginResponseInfo.

        插件状态

        :return: The plugin_status of this PluginResponseInfo.
        :rtype: str
        """
        return self._plugin_status

    @plugin_status.setter
    def plugin_status(self, plugin_status):
        r"""Sets the plugin_status of this PluginResponseInfo.

        插件状态

        :param plugin_status: The plugin_status of this PluginResponseInfo.
        :type plugin_status: str
        """
        self._plugin_status = plugin_status

    @property
    def upgrade_status(self):
        r"""Gets the upgrade_status of this PluginResponseInfo.

        插件升级状态

        :return: The upgrade_status of this PluginResponseInfo.
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        r"""Sets the upgrade_status of this PluginResponseInfo.

        插件升级状态

        :param upgrade_status: The upgrade_status of this PluginResponseInfo.
        :type upgrade_status: str
        """
        self._upgrade_status = upgrade_status

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
        if not isinstance(other, PluginResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
