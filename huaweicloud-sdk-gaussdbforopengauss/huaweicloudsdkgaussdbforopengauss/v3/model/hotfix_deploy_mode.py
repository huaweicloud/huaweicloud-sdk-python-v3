# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotfixDeployMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_upgrade': 'bool',
        'update_time': 'int',
        'mode': 'str'
    }

    attribute_map = {
        'default_upgrade': 'default_upgrade',
        'update_time': 'update_time',
        'mode': 'mode'
    }

    def __init__(self, default_upgrade=None, update_time=None, mode=None):
        r"""HotfixDeployMode

        The model defined in huaweicloud sdk

        :param default_upgrade: **参数解释**： 补丁默认升级策略。 **取值范围**： - true：无需选择，默认升级该版本。 - false：用户可选，选择后升级该版本。
        :type default_upgrade: bool
        :param update_time: **参数解释**： 热补丁升级策略的修改时间，UNIX时间戳格式，单位是毫秒。 **取值范围**： 不涉及。
        :type update_time: int
        :param mode: **参数解释**： 可升级该补丁的实例部署形态。 **取值范围**： - distributed：包括独立部署，基础版混合部署。 - centralization_standard：包括主备版。
        :type mode: str
        """
        
        

        self._default_upgrade = None
        self._update_time = None
        self._mode = None
        self.discriminator = None

        if default_upgrade is not None:
            self.default_upgrade = default_upgrade
        if update_time is not None:
            self.update_time = update_time
        if mode is not None:
            self.mode = mode

    @property
    def default_upgrade(self):
        r"""Gets the default_upgrade of this HotfixDeployMode.

        **参数解释**： 补丁默认升级策略。 **取值范围**： - true：无需选择，默认升级该版本。 - false：用户可选，选择后升级该版本。

        :return: The default_upgrade of this HotfixDeployMode.
        :rtype: bool
        """
        return self._default_upgrade

    @default_upgrade.setter
    def default_upgrade(self, default_upgrade):
        r"""Sets the default_upgrade of this HotfixDeployMode.

        **参数解释**： 补丁默认升级策略。 **取值范围**： - true：无需选择，默认升级该版本。 - false：用户可选，选择后升级该版本。

        :param default_upgrade: The default_upgrade of this HotfixDeployMode.
        :type default_upgrade: bool
        """
        self._default_upgrade = default_upgrade

    @property
    def update_time(self):
        r"""Gets the update_time of this HotfixDeployMode.

        **参数解释**： 热补丁升级策略的修改时间，UNIX时间戳格式，单位是毫秒。 **取值范围**： 不涉及。

        :return: The update_time of this HotfixDeployMode.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this HotfixDeployMode.

        **参数解释**： 热补丁升级策略的修改时间，UNIX时间戳格式，单位是毫秒。 **取值范围**： 不涉及。

        :param update_time: The update_time of this HotfixDeployMode.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def mode(self):
        r"""Gets the mode of this HotfixDeployMode.

        **参数解释**： 可升级该补丁的实例部署形态。 **取值范围**： - distributed：包括独立部署，基础版混合部署。 - centralization_standard：包括主备版。

        :return: The mode of this HotfixDeployMode.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this HotfixDeployMode.

        **参数解释**： 可升级该补丁的实例部署形态。 **取值范围**： - distributed：包括独立部署，基础版混合部署。 - centralization_standard：包括主备版。

        :param mode: The mode of this HotfixDeployMode.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, HotfixDeployMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
