# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostAppsResponseInfoPaths:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_path': 'str',
        'app_version': 'str',
        'status': 'str'
    }

    attribute_map = {
        'app_path': 'app_path',
        'app_version': 'app_version',
        'status': 'status'
    }

    def __init__(self, app_path=None, app_version=None, status=None):
        r"""VulHostAppsResponseInfoPaths

        The model defined in huaweicloud sdk

        :param app_path: **参数解释**: 存在漏洞的软件路径 **取值范围**: 字符长度1-512位 
        :type app_path: str
        :param app_version: **参数解释**: 软件版本 **取值范围**: 字符长度1-64位 
        :type app_version: str
        :param status: **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复 
        :type status: str
        """
        
        

        self._app_path = None
        self._app_version = None
        self._status = None
        self.discriminator = None

        if app_path is not None:
            self.app_path = app_path
        if app_version is not None:
            self.app_version = app_version
        if status is not None:
            self.status = status

    @property
    def app_path(self):
        r"""Gets the app_path of this VulHostAppsResponseInfoPaths.

        **参数解释**: 存在漏洞的软件路径 **取值范围**: 字符长度1-512位 

        :return: The app_path of this VulHostAppsResponseInfoPaths.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this VulHostAppsResponseInfoPaths.

        **参数解释**: 存在漏洞的软件路径 **取值范围**: 字符长度1-512位 

        :param app_path: The app_path of this VulHostAppsResponseInfoPaths.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def app_version(self):
        r"""Gets the app_version of this VulHostAppsResponseInfoPaths.

        **参数解释**: 软件版本 **取值范围**: 字符长度1-64位 

        :return: The app_version of this VulHostAppsResponseInfoPaths.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this VulHostAppsResponseInfoPaths.

        **参数解释**: 软件版本 **取值范围**: 字符长度1-64位 

        :param app_version: The app_version of this VulHostAppsResponseInfoPaths.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def status(self):
        r"""Gets the status of this VulHostAppsResponseInfoPaths.

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复 

        :return: The status of this VulHostAppsResponseInfoPaths.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulHostAppsResponseInfoPaths.

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复 

        :param status: The status of this VulHostAppsResponseInfoPaths.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, VulHostAppsResponseInfoPaths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
