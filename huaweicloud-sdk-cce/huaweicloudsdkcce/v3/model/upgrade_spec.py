# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_upgrade_action': 'ClusterUpgradeAction'
    }

    attribute_map = {
        'cluster_upgrade_action': 'clusterUpgradeAction'
    }

    def __init__(self, cluster_upgrade_action=None):
        r"""UpgradeSpec

        The model defined in huaweicloud sdk

        :param cluster_upgrade_action: 
        :type cluster_upgrade_action: :class:`huaweicloudsdkcce.v3.ClusterUpgradeAction`
        """
        
        

        self._cluster_upgrade_action = None
        self.discriminator = None

        if cluster_upgrade_action is not None:
            self.cluster_upgrade_action = cluster_upgrade_action

    @property
    def cluster_upgrade_action(self):
        r"""Gets the cluster_upgrade_action of this UpgradeSpec.

        :return: The cluster_upgrade_action of this UpgradeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterUpgradeAction`
        """
        return self._cluster_upgrade_action

    @cluster_upgrade_action.setter
    def cluster_upgrade_action(self, cluster_upgrade_action):
        r"""Sets the cluster_upgrade_action of this UpgradeSpec.

        :param cluster_upgrade_action: The cluster_upgrade_action of this UpgradeSpec.
        :type cluster_upgrade_action: :class:`huaweicloudsdkcce.v3.ClusterUpgradeAction`
        """
        self._cluster_upgrade_action = cluster_upgrade_action

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
        if not isinstance(other, UpgradeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
