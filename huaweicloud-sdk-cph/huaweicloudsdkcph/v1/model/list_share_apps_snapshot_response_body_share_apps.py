# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareAppsSnapshotResponseBodyShareApps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_name': 'str',
        'versions': 'list[str]'
    }

    attribute_map = {
        'package_name': 'package_name',
        'versions': 'versions'
    }

    def __init__(self, package_name=None, versions=None):
        r"""ListShareAppsSnapshotResponseBodyShareApps

        The model defined in huaweicloud sdk

        :param package_name: 应用包名
        :type package_name: str
        :param versions: 应用对应的版本号列表
        :type versions: list[str]
        """
        
        

        self._package_name = None
        self._versions = None
        self.discriminator = None

        if package_name is not None:
            self.package_name = package_name
        if versions is not None:
            self.versions = versions

    @property
    def package_name(self):
        r"""Gets the package_name of this ListShareAppsSnapshotResponseBodyShareApps.

        应用包名

        :return: The package_name of this ListShareAppsSnapshotResponseBodyShareApps.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this ListShareAppsSnapshotResponseBodyShareApps.

        应用包名

        :param package_name: The package_name of this ListShareAppsSnapshotResponseBodyShareApps.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def versions(self):
        r"""Gets the versions of this ListShareAppsSnapshotResponseBodyShareApps.

        应用对应的版本号列表

        :return: The versions of this ListShareAppsSnapshotResponseBodyShareApps.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ListShareAppsSnapshotResponseBodyShareApps.

        应用对应的版本号列表

        :param versions: The versions of this ListShareAppsSnapshotResponseBodyShareApps.
        :type versions: list[str]
        """
        self._versions = versions

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
        if not isinstance(other, ListShareAppsSnapshotResponseBodyShareApps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
