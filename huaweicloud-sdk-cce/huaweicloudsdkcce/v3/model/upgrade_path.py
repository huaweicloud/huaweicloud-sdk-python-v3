# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradePath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'platform_version': 'str',
        'target_versions': 'list[str]'
    }

    attribute_map = {
        'version': 'version',
        'platform_version': 'platformVersion',
        'target_versions': 'targetVersions'
    }

    def __init__(self, version=None, platform_version=None, target_versions=None):
        r"""UpgradePath

        The model defined in huaweicloud sdk

        :param version: 集群版本，v1.19及以下集群形如v1.19.16-r20，v1.21及以上形如v1.21,v1.23，详细请参考CCE集群版本号说明。
        :type version: str
        :param platform_version: CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。   platformVersion格式为：cce.X.Y   - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。  - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。
        :type platform_version: str
        :param target_versions: 可升级的目标版本集合
        :type target_versions: list[str]
        """
        
        

        self._version = None
        self._platform_version = None
        self._target_versions = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if platform_version is not None:
            self.platform_version = platform_version
        if target_versions is not None:
            self.target_versions = target_versions

    @property
    def version(self):
        r"""Gets the version of this UpgradePath.

        集群版本，v1.19及以下集群形如v1.19.16-r20，v1.21及以上形如v1.21,v1.23，详细请参考CCE集群版本号说明。

        :return: The version of this UpgradePath.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpgradePath.

        集群版本，v1.19及以下集群形如v1.19.16-r20，v1.21及以上形如v1.21,v1.23，详细请参考CCE集群版本号说明。

        :param version: The version of this UpgradePath.
        :type version: str
        """
        self._version = version

    @property
    def platform_version(self):
        r"""Gets the platform_version of this UpgradePath.

        CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。   platformVersion格式为：cce.X.Y   - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。  - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。

        :return: The platform_version of this UpgradePath.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        r"""Sets the platform_version of this UpgradePath.

        CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。   platformVersion格式为：cce.X.Y   - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。  - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。

        :param platform_version: The platform_version of this UpgradePath.
        :type platform_version: str
        """
        self._platform_version = platform_version

    @property
    def target_versions(self):
        r"""Gets the target_versions of this UpgradePath.

        可升级的目标版本集合

        :return: The target_versions of this UpgradePath.
        :rtype: list[str]
        """
        return self._target_versions

    @target_versions.setter
    def target_versions(self, target_versions):
        r"""Sets the target_versions of this UpgradePath.

        可升级的目标版本集合

        :param target_versions: The target_versions of this UpgradePath.
        :type target_versions: list[str]
        """
        self._target_versions = target_versions

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
        if not isinstance(other, UpgradePath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
