# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeFeatureGates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_upgrade_page_v4': 'bool'
    }

    attribute_map = {
        'support_upgrade_page_v4': 'supportUpgradePageV4'
    }

    def __init__(self, support_upgrade_page_v4=None):
        """UpgradeFeatureGates

        The model defined in huaweicloud sdk

        :param support_upgrade_page_v4: 集群升级Console界面是否支持V4版本，该字段一般由CCE Console使用。
        :type support_upgrade_page_v4: bool
        """
        
        

        self._support_upgrade_page_v4 = None
        self.discriminator = None

        if support_upgrade_page_v4 is not None:
            self.support_upgrade_page_v4 = support_upgrade_page_v4

    @property
    def support_upgrade_page_v4(self):
        """Gets the support_upgrade_page_v4 of this UpgradeFeatureGates.

        集群升级Console界面是否支持V4版本，该字段一般由CCE Console使用。

        :return: The support_upgrade_page_v4 of this UpgradeFeatureGates.
        :rtype: bool
        """
        return self._support_upgrade_page_v4

    @support_upgrade_page_v4.setter
    def support_upgrade_page_v4(self, support_upgrade_page_v4):
        """Sets the support_upgrade_page_v4 of this UpgradeFeatureGates.

        集群升级Console界面是否支持V4版本，该字段一般由CCE Console使用。

        :param support_upgrade_page_v4: The support_upgrade_page_v4 of this UpgradeFeatureGates.
        :type support_upgrade_page_v4: bool
        """
        self._support_upgrade_page_v4 = support_upgrade_page_v4

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
        if not isinstance(other, UpgradeFeatureGates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
