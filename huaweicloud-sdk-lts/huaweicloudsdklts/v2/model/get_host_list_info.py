# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHostListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_ip': 'str',
        'host_name': 'str',
        'host_status': 'str',
        'host_type': 'str',
        'host_version': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'host_name': 'host_name',
        'host_status': 'host_status',
        'host_type': 'host_type',
        'host_version': 'host_version',
        'update_time': 'update_time'
    }

    def __init__(self, host_id=None, host_ip=None, host_name=None, host_status=None, host_type=None, host_version=None, update_time=None):
        """GetHostListInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机ID
        :type host_id: str
        :param host_ip: 主机IP
        :type host_ip: str
        :param host_name: 主机名称
        :type host_name: str
        :param host_status: 主机状态。 uninstall:未安装 running:运行 offline:离线 error:异常 plugin error:插件错误 installing:安装中 install-fail:安装失败 upgrading:升级中 upgrading-transient:升级中 upgrade failed:升级失败 upgrade-fail:升级失败 uninstalling:卸载中 uninstalling-transient:卸载中 authentication error:鉴权失败
        :type host_status: str
        :param host_type: 主机类型。linux:linux类型,windows:windows类型
        :type host_type: str
        :param host_version: 主机版本
        :type host_version: str
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._host_id = None
        self._host_ip = None
        self._host_name = None
        self._host_status = None
        self._host_type = None
        self._host_version = None
        self._update_time = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
        if host_name is not None:
            self.host_name = host_name
        if host_status is not None:
            self.host_status = host_status
        if host_type is not None:
            self.host_type = host_type
        if host_version is not None:
            self.host_version = host_version
        if update_time is not None:
            self.update_time = update_time

    @property
    def host_id(self):
        """Gets the host_id of this GetHostListInfo.

        主机ID

        :return: The host_id of this GetHostListInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this GetHostListInfo.

        主机ID

        :param host_id: The host_id of this GetHostListInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        """Gets the host_ip of this GetHostListInfo.

        主机IP

        :return: The host_ip of this GetHostListInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this GetHostListInfo.

        主机IP

        :param host_ip: The host_ip of this GetHostListInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_name(self):
        """Gets the host_name of this GetHostListInfo.

        主机名称

        :return: The host_name of this GetHostListInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this GetHostListInfo.

        主机名称

        :param host_name: The host_name of this GetHostListInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_status(self):
        """Gets the host_status of this GetHostListInfo.

        主机状态。 uninstall:未安装 running:运行 offline:离线 error:异常 plugin error:插件错误 installing:安装中 install-fail:安装失败 upgrading:升级中 upgrading-transient:升级中 upgrade failed:升级失败 upgrade-fail:升级失败 uninstalling:卸载中 uninstalling-transient:卸载中 authentication error:鉴权失败

        :return: The host_status of this GetHostListInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this GetHostListInfo.

        主机状态。 uninstall:未安装 running:运行 offline:离线 error:异常 plugin error:插件错误 installing:安装中 install-fail:安装失败 upgrading:升级中 upgrading-transient:升级中 upgrade failed:升级失败 upgrade-fail:升级失败 uninstalling:卸载中 uninstalling-transient:卸载中 authentication error:鉴权失败

        :param host_status: The host_status of this GetHostListInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def host_type(self):
        """Gets the host_type of this GetHostListInfo.

        主机类型。linux:linux类型,windows:windows类型

        :return: The host_type of this GetHostListInfo.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this GetHostListInfo.

        主机类型。linux:linux类型,windows:windows类型

        :param host_type: The host_type of this GetHostListInfo.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def host_version(self):
        """Gets the host_version of this GetHostListInfo.

        主机版本

        :return: The host_version of this GetHostListInfo.
        :rtype: str
        """
        return self._host_version

    @host_version.setter
    def host_version(self, host_version):
        """Sets the host_version of this GetHostListInfo.

        主机版本

        :param host_version: The host_version of this GetHostListInfo.
        :type host_version: str
        """
        self._host_version = host_version

    @property
    def update_time(self):
        """Gets the update_time of this GetHostListInfo.

        更新时间

        :return: The update_time of this GetHostListInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetHostListInfo.

        更新时间

        :param update_time: The update_time of this GetHostListInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, GetHostListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
