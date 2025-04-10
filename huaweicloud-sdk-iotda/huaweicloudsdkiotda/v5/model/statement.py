# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Statement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'effect': 'str',
        'actions': 'list[str]',
        'resources': 'list[str]'
    }

    attribute_map = {
        'effect': 'effect',
        'actions': 'actions',
        'resources': 'resources'
    }

    def __init__(self, effect=None, actions=None, resources=None):
        r"""Statement

        The model defined in huaweicloud sdk

        :param effect: 指定是允许还是拒绝该操作。既有允许（ALLOW）又有拒绝（DENY）的授权语句时，遵循拒绝（DENY）优先的原则。 - ALLOW：允许。 - DENY：拒绝。 
        :type effect: str
        :param actions: 用于指定策略允许或拒绝的操作。格式为：服务名:资源:操作。当前支持的操作类型如下： - iotda:devices:publish：设备使用MQTT协议发布消息。 - iotda:devices:subscribe：设备使用MQTT协议订阅消息。 
        :type actions: list[str]
        :param resources: 用于指定允许或拒绝对其执行操作的资源。格式为：资源类型:资源名称。如设备订阅的资源为：topic:/v1/${devices.deviceId}/test/hello。  **取值范围**：资源列表长度最小为1，最大为10，列表中的资源取值范围：仅支持字母，数字，以及/{}$&#x3D;+#?*:._-组合。 
        :type resources: list[str]
        """
        
        

        self._effect = None
        self._actions = None
        self._resources = None
        self.discriminator = None

        self.effect = effect
        self.actions = actions
        self.resources = resources

    @property
    def effect(self):
        r"""Gets the effect of this Statement.

        指定是允许还是拒绝该操作。既有允许（ALLOW）又有拒绝（DENY）的授权语句时，遵循拒绝（DENY）优先的原则。 - ALLOW：允许。 - DENY：拒绝。 

        :return: The effect of this Statement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this Statement.

        指定是允许还是拒绝该操作。既有允许（ALLOW）又有拒绝（DENY）的授权语句时，遵循拒绝（DENY）优先的原则。 - ALLOW：允许。 - DENY：拒绝。 

        :param effect: The effect of this Statement.
        :type effect: str
        """
        self._effect = effect

    @property
    def actions(self):
        r"""Gets the actions of this Statement.

        用于指定策略允许或拒绝的操作。格式为：服务名:资源:操作。当前支持的操作类型如下： - iotda:devices:publish：设备使用MQTT协议发布消息。 - iotda:devices:subscribe：设备使用MQTT协议订阅消息。 

        :return: The actions of this Statement.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this Statement.

        用于指定策略允许或拒绝的操作。格式为：服务名:资源:操作。当前支持的操作类型如下： - iotda:devices:publish：设备使用MQTT协议发布消息。 - iotda:devices:subscribe：设备使用MQTT协议订阅消息。 

        :param actions: The actions of this Statement.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def resources(self):
        r"""Gets the resources of this Statement.

        用于指定允许或拒绝对其执行操作的资源。格式为：资源类型:资源名称。如设备订阅的资源为：topic:/v1/${devices.deviceId}/test/hello。  **取值范围**：资源列表长度最小为1，最大为10，列表中的资源取值范围：仅支持字母，数字，以及/{}$=+#?*:._-组合。 

        :return: The resources of this Statement.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this Statement.

        用于指定允许或拒绝对其执行操作的资源。格式为：资源类型:资源名称。如设备订阅的资源为：topic:/v1/${devices.deviceId}/test/hello。  **取值范围**：资源列表长度最小为1，最大为10，列表中的资源取值范围：仅支持字母，数字，以及/{}$=+#?*:._-组合。 

        :param resources: The resources of this Statement.
        :type resources: list[str]
        """
        self._resources = resources

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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
