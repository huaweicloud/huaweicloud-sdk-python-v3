# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeActionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_action': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'upgrade_action': 'upgrade_action',
        'enable': 'enable'
    }

    def __init__(self, upgrade_action=None, enable=None):
        """UpgradeActionInfo

        The model defined in huaweicloud sdk

        :param upgrade_action: 升级操作,upgrade&#x3D;升级,upgradeAutoCommit&#x3D;升级自动提交,commit&#x3D;提交,rollback&#x3D;回滚
        :type upgrade_action: str
        :param enable: 可用，不可用
        :type enable: bool
        """
        
        

        self._upgrade_action = None
        self._enable = None
        self.discriminator = None

        if upgrade_action is not None:
            self.upgrade_action = upgrade_action
        if enable is not None:
            self.enable = enable

    @property
    def upgrade_action(self):
        """Gets the upgrade_action of this UpgradeActionInfo.

        升级操作,upgrade=升级,upgradeAutoCommit=升级自动提交,commit=提交,rollback=回滚

        :return: The upgrade_action of this UpgradeActionInfo.
        :rtype: str
        """
        return self._upgrade_action

    @upgrade_action.setter
    def upgrade_action(self, upgrade_action):
        """Sets the upgrade_action of this UpgradeActionInfo.

        升级操作,upgrade=升级,upgradeAutoCommit=升级自动提交,commit=提交,rollback=回滚

        :param upgrade_action: The upgrade_action of this UpgradeActionInfo.
        :type upgrade_action: str
        """
        self._upgrade_action = upgrade_action

    @property
    def enable(self):
        """Gets the enable of this UpgradeActionInfo.

        可用，不可用

        :return: The enable of this UpgradeActionInfo.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpgradeActionInfo.

        可用，不可用

        :param enable: The enable of this UpgradeActionInfo.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, UpgradeActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
