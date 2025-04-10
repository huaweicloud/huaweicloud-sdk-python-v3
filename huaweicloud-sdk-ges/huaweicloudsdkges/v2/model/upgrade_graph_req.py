# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeGraphReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_version': 'str',
        'force_upgrade': 'bool'
    }

    attribute_map = {
        'upgrade_version': 'upgrade_version',
        'force_upgrade': 'force_upgrade'
    }

    def __init__(self, upgrade_version=None, force_upgrade=None):
        r"""UpgradeGraphReq

        The model defined in huaweicloud sdk

        :param upgrade_version: 升级到的版本，必须大于当前图版本。
        :type upgrade_version: str
        :param force_upgrade: 是否强制升级。取值为true或false，默认为false。  - true：强制升级，会中断升级时已经在处理的任务，比如运行算法长任务，可能会造成少量请求失败。 - false：非强制升级，会等待已经运行的业务，升级过程可能较慢。
        :type force_upgrade: bool
        """
        
        

        self._upgrade_version = None
        self._force_upgrade = None
        self.discriminator = None

        self.upgrade_version = upgrade_version
        if force_upgrade is not None:
            self.force_upgrade = force_upgrade

    @property
    def upgrade_version(self):
        r"""Gets the upgrade_version of this UpgradeGraphReq.

        升级到的版本，必须大于当前图版本。

        :return: The upgrade_version of this UpgradeGraphReq.
        :rtype: str
        """
        return self._upgrade_version

    @upgrade_version.setter
    def upgrade_version(self, upgrade_version):
        r"""Sets the upgrade_version of this UpgradeGraphReq.

        升级到的版本，必须大于当前图版本。

        :param upgrade_version: The upgrade_version of this UpgradeGraphReq.
        :type upgrade_version: str
        """
        self._upgrade_version = upgrade_version

    @property
    def force_upgrade(self):
        r"""Gets the force_upgrade of this UpgradeGraphReq.

        是否强制升级。取值为true或false，默认为false。  - true：强制升级，会中断升级时已经在处理的任务，比如运行算法长任务，可能会造成少量请求失败。 - false：非强制升级，会等待已经运行的业务，升级过程可能较慢。

        :return: The force_upgrade of this UpgradeGraphReq.
        :rtype: bool
        """
        return self._force_upgrade

    @force_upgrade.setter
    def force_upgrade(self, force_upgrade):
        r"""Sets the force_upgrade of this UpgradeGraphReq.

        是否强制升级。取值为true或false，默认为false。  - true：强制升级，会中断升级时已经在处理的任务，比如运行算法长任务，可能会造成少量请求失败。 - false：非强制升级，会等待已经运行的业务，升级过程可能较慢。

        :param force_upgrade: The force_upgrade of this UpgradeGraphReq.
        :type force_upgrade: bool
        """
        self._force_upgrade = force_upgrade

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
        if not isinstance(other, UpgradeGraphReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
