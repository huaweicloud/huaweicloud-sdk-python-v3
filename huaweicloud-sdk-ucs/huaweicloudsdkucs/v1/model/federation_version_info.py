# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FederationVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_version': 'FederationVersionSpec',
        'target_versions': 'list[FederationVersionSpec]'
    }

    attribute_map = {
        'current_version': 'currentVersion',
        'target_versions': 'targetVersions'
    }

    def __init__(self, current_version=None, target_versions=None):
        r"""FederationVersionInfo

        The model defined in huaweicloud sdk

        :param current_version: 
        :type current_version: :class:`huaweicloudsdkucs.v1.FederationVersionSpec`
        :param target_versions: 目标联邦版本列表
        :type target_versions: list[:class:`huaweicloudsdkucs.v1.FederationVersionSpec`]
        """
        
        

        self._current_version = None
        self._target_versions = None
        self.discriminator = None

        if current_version is not None:
            self.current_version = current_version
        if target_versions is not None:
            self.target_versions = target_versions

    @property
    def current_version(self):
        r"""Gets the current_version of this FederationVersionInfo.

        :return: The current_version of this FederationVersionInfo.
        :rtype: :class:`huaweicloudsdkucs.v1.FederationVersionSpec`
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this FederationVersionInfo.

        :param current_version: The current_version of this FederationVersionInfo.
        :type current_version: :class:`huaweicloudsdkucs.v1.FederationVersionSpec`
        """
        self._current_version = current_version

    @property
    def target_versions(self):
        r"""Gets the target_versions of this FederationVersionInfo.

        目标联邦版本列表

        :return: The target_versions of this FederationVersionInfo.
        :rtype: list[:class:`huaweicloudsdkucs.v1.FederationVersionSpec`]
        """
        return self._target_versions

    @target_versions.setter
    def target_versions(self, target_versions):
        r"""Sets the target_versions of this FederationVersionInfo.

        目标联邦版本列表

        :param target_versions: The target_versions of this FederationVersionInfo.
        :type target_versions: list[:class:`huaweicloudsdkucs.v1.FederationVersionSpec`]
        """
        self._target_versions = target_versions

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
        if not isinstance(other, FederationVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
