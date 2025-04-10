# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeInfoSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_upgrade_info': 'UpgradeInfoStatus',
        'version_info': 'UpgradeVersionInfo',
        'upgrade_feature_gates': 'UpgradeFeatureGates'
    }

    attribute_map = {
        'last_upgrade_info': 'lastUpgradeInfo',
        'version_info': 'versionInfo',
        'upgrade_feature_gates': 'upgradeFeatureGates'
    }

    def __init__(self, last_upgrade_info=None, version_info=None, upgrade_feature_gates=None):
        r"""UpgradeInfoSpec

        The model defined in huaweicloud sdk

        :param last_upgrade_info: 
        :type last_upgrade_info: :class:`huaweicloudsdkcce.v3.UpgradeInfoStatus`
        :param version_info: 
        :type version_info: :class:`huaweicloudsdkcce.v3.UpgradeVersionInfo`
        :param upgrade_feature_gates: 
        :type upgrade_feature_gates: :class:`huaweicloudsdkcce.v3.UpgradeFeatureGates`
        """
        
        

        self._last_upgrade_info = None
        self._version_info = None
        self._upgrade_feature_gates = None
        self.discriminator = None

        if last_upgrade_info is not None:
            self.last_upgrade_info = last_upgrade_info
        if version_info is not None:
            self.version_info = version_info
        if upgrade_feature_gates is not None:
            self.upgrade_feature_gates = upgrade_feature_gates

    @property
    def last_upgrade_info(self):
        r"""Gets the last_upgrade_info of this UpgradeInfoSpec.

        :return: The last_upgrade_info of this UpgradeInfoSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeInfoStatus`
        """
        return self._last_upgrade_info

    @last_upgrade_info.setter
    def last_upgrade_info(self, last_upgrade_info):
        r"""Sets the last_upgrade_info of this UpgradeInfoSpec.

        :param last_upgrade_info: The last_upgrade_info of this UpgradeInfoSpec.
        :type last_upgrade_info: :class:`huaweicloudsdkcce.v3.UpgradeInfoStatus`
        """
        self._last_upgrade_info = last_upgrade_info

    @property
    def version_info(self):
        r"""Gets the version_info of this UpgradeInfoSpec.

        :return: The version_info of this UpgradeInfoSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeVersionInfo`
        """
        return self._version_info

    @version_info.setter
    def version_info(self, version_info):
        r"""Sets the version_info of this UpgradeInfoSpec.

        :param version_info: The version_info of this UpgradeInfoSpec.
        :type version_info: :class:`huaweicloudsdkcce.v3.UpgradeVersionInfo`
        """
        self._version_info = version_info

    @property
    def upgrade_feature_gates(self):
        r"""Gets the upgrade_feature_gates of this UpgradeInfoSpec.

        :return: The upgrade_feature_gates of this UpgradeInfoSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeFeatureGates`
        """
        return self._upgrade_feature_gates

    @upgrade_feature_gates.setter
    def upgrade_feature_gates(self, upgrade_feature_gates):
        r"""Sets the upgrade_feature_gates of this UpgradeInfoSpec.

        :param upgrade_feature_gates: The upgrade_feature_gates of this UpgradeInfoSpec.
        :type upgrade_feature_gates: :class:`huaweicloudsdkcce.v3.UpgradeFeatureGates`
        """
        self._upgrade_feature_gates = upgrade_feature_gates

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
        if not isinstance(other, UpgradeInfoSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
