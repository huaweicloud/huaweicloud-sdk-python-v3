# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVulInfoAppList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_version': 'str',
        'upgrade_version': 'str',
        'app_path': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_version': 'app_version',
        'upgrade_version': 'upgrade_version',
        'app_path': 'app_path'
    }

    def __init__(self, app_name=None, app_version=None, upgrade_version=None, app_path=None):
        """HostVulInfoAppList

        The model defined in huaweicloud sdk

        :param app_name: 软件名称
        :type app_name: str
        :param app_version: 软件版本
        :type app_version: str
        :param upgrade_version: 修复漏洞软件需要升级到的版本
        :type upgrade_version: str
        :param app_path: 应用软件的路径（只有应用漏洞有该字段）
        :type app_path: str
        """
        
        

        self._app_name = None
        self._app_version = None
        self._upgrade_version = None
        self._app_path = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if upgrade_version is not None:
            self.upgrade_version = upgrade_version
        if app_path is not None:
            self.app_path = app_path

    @property
    def app_name(self):
        """Gets the app_name of this HostVulInfoAppList.

        软件名称

        :return: The app_name of this HostVulInfoAppList.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this HostVulInfoAppList.

        软件名称

        :param app_name: The app_name of this HostVulInfoAppList.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        """Gets the app_version of this HostVulInfoAppList.

        软件版本

        :return: The app_version of this HostVulInfoAppList.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this HostVulInfoAppList.

        软件版本

        :param app_version: The app_version of this HostVulInfoAppList.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def upgrade_version(self):
        """Gets the upgrade_version of this HostVulInfoAppList.

        修复漏洞软件需要升级到的版本

        :return: The upgrade_version of this HostVulInfoAppList.
        :rtype: str
        """
        return self._upgrade_version

    @upgrade_version.setter
    def upgrade_version(self, upgrade_version):
        """Sets the upgrade_version of this HostVulInfoAppList.

        修复漏洞软件需要升级到的版本

        :param upgrade_version: The upgrade_version of this HostVulInfoAppList.
        :type upgrade_version: str
        """
        self._upgrade_version = upgrade_version

    @property
    def app_path(self):
        """Gets the app_path of this HostVulInfoAppList.

        应用软件的路径（只有应用漏洞有该字段）

        :return: The app_path of this HostVulInfoAppList.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        """Sets the app_path of this HostVulInfoAppList.

        应用软件的路径（只有应用漏洞有该字段）

        :param app_path: The app_path of this HostVulInfoAppList.
        :type app_path: str
        """
        self._app_path = app_path

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
        if not isinstance(other, HostVulInfoAppList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
