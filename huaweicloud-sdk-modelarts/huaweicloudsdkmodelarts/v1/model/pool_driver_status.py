# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolDriverStatus:

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
        'state': 'str'
    }

    attribute_map = {
        'version': 'version',
        'state': 'state'
    }

    def __init__(self, version=None, state=None):
        r"""PoolDriverStatus

        The model defined in huaweicloud sdk

        :param version: **参数解释**：资源池当前驱动版本。 **取值范围**：不涉及。
        :type version: str
        :param state: **参数解释**：资源池当前驱动状态。 **取值范围**：可选值如下： - Creating：驱动安装中。 - Upgrading：驱动升级中。 - Running：驱动运行中。 - Abnormal：驱动异常。
        :type state: str
        """
        
        

        self._version = None
        self._state = None
        self.discriminator = None

        self.version = version
        self.state = state

    @property
    def version(self):
        r"""Gets the version of this PoolDriverStatus.

        **参数解释**：资源池当前驱动版本。 **取值范围**：不涉及。

        :return: The version of this PoolDriverStatus.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PoolDriverStatus.

        **参数解释**：资源池当前驱动版本。 **取值范围**：不涉及。

        :param version: The version of this PoolDriverStatus.
        :type version: str
        """
        self._version = version

    @property
    def state(self):
        r"""Gets the state of this PoolDriverStatus.

        **参数解释**：资源池当前驱动状态。 **取值范围**：可选值如下： - Creating：驱动安装中。 - Upgrading：驱动升级中。 - Running：驱动运行中。 - Abnormal：驱动异常。

        :return: The state of this PoolDriverStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this PoolDriverStatus.

        **参数解释**：资源池当前驱动状态。 **取值范围**：可选值如下： - Creating：驱动安装中。 - Upgrading：驱动升级中。 - Running：驱动运行中。 - Abnormal：驱动异常。

        :param state: The state of this PoolDriverStatus.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, PoolDriverStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
