# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'release': 'str',
        'patch': 'str',
        'suggest_patch': 'str',
        'target_versions': 'list[str]'
    }

    attribute_map = {
        'release': 'release',
        'patch': 'patch',
        'suggest_patch': 'suggestPatch',
        'target_versions': 'targetVersions'
    }

    def __init__(self, release=None, patch=None, suggest_patch=None, target_versions=None):
        r"""UpgradeVersionInfo

        The model defined in huaweicloud sdk

        :param release: 正式版本号，如：v1.19.10
        :type release: str
        :param patch: 补丁版本号，如r0
        :type patch: str
        :param suggest_patch: 推荐升级的目标补丁版本号，如r0
        :type suggest_patch: str
        :param target_versions: 升级目标版本集合
        :type target_versions: list[str]
        """
        
        

        self._release = None
        self._patch = None
        self._suggest_patch = None
        self._target_versions = None
        self.discriminator = None

        if release is not None:
            self.release = release
        if patch is not None:
            self.patch = patch
        if suggest_patch is not None:
            self.suggest_patch = suggest_patch
        if target_versions is not None:
            self.target_versions = target_versions

    @property
    def release(self):
        r"""Gets the release of this UpgradeVersionInfo.

        正式版本号，如：v1.19.10

        :return: The release of this UpgradeVersionInfo.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        r"""Sets the release of this UpgradeVersionInfo.

        正式版本号，如：v1.19.10

        :param release: The release of this UpgradeVersionInfo.
        :type release: str
        """
        self._release = release

    @property
    def patch(self):
        r"""Gets the patch of this UpgradeVersionInfo.

        补丁版本号，如r0

        :return: The patch of this UpgradeVersionInfo.
        :rtype: str
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        r"""Sets the patch of this UpgradeVersionInfo.

        补丁版本号，如r0

        :param patch: The patch of this UpgradeVersionInfo.
        :type patch: str
        """
        self._patch = patch

    @property
    def suggest_patch(self):
        r"""Gets the suggest_patch of this UpgradeVersionInfo.

        推荐升级的目标补丁版本号，如r0

        :return: The suggest_patch of this UpgradeVersionInfo.
        :rtype: str
        """
        return self._suggest_patch

    @suggest_patch.setter
    def suggest_patch(self, suggest_patch):
        r"""Sets the suggest_patch of this UpgradeVersionInfo.

        推荐升级的目标补丁版本号，如r0

        :param suggest_patch: The suggest_patch of this UpgradeVersionInfo.
        :type suggest_patch: str
        """
        self._suggest_patch = suggest_patch

    @property
    def target_versions(self):
        r"""Gets the target_versions of this UpgradeVersionInfo.

        升级目标版本集合

        :return: The target_versions of this UpgradeVersionInfo.
        :rtype: list[str]
        """
        return self._target_versions

    @target_versions.setter
    def target_versions(self, target_versions):
        r"""Sets the target_versions of this UpgradeVersionInfo.

        升级目标版本集合

        :param target_versions: The target_versions of this UpgradeVersionInfo.
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
        if not isinstance(other, UpgradeVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
