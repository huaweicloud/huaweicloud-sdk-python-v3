# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceCapability:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'service_type': 'str',
        'properties': 'list[ServiceProperty]',
        'commands': 'list[ServiceCommand]',
        'events': 'list[ServiceEvent]',
        'description': 'str',
        'option': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'service_type': 'service_type',
        'properties': 'properties',
        'commands': 'commands',
        'events': 'events',
        'description': 'description',
        'option': 'option'
    }

    def __init__(self, service_id=None, service_type=None, properties=None, commands=None, events=None, description=None, option=None):
        """ServiceCapability

        The model defined in huaweicloud sdk

        :param service_id: **参数说明**：设备的服务ID。注：产品内不允许重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-$等字符的组合。
        :type service_id: str
        :param service_type: **参数说明**：设备的服务类型。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-$等字符的组合。
        :type service_type: str
        :param properties: **参数说明**：设备服务支持的属性列表。 **取值范围**：数组长度大小不超过500。
        :type properties: list[:class:`huaweicloudsdkiotda.v5.ServiceProperty`]
        :param commands: **参数说明**：设备服务支持的命令列表。 **取值范围**：数组长度大小不超过500。
        :type commands: list[:class:`huaweicloudsdkiotda.v5.ServiceCommand`]
        :param events: **参数说明**：设备服务支持的事件列表。 **取值范围**：数组长度大小不超过500。
        :type events: list[:class:`huaweicloudsdkiotda.v5.ServiceEvent`]
        :param description: **参数说明**：设备服务的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?&#39;#().,;&amp;%@!- ，、：；。/等字符的组合。
        :type description: str
        :param option: **参数说明**：指定设备服务是否必选。目前本字段为非功能性字段，仅起到标识作用。 **取值范围**： - Master：主服务 - Mandatory：必选服务 - Optional：可选服务 默认值为Optional。
        :type option: str
        """
        
        

        self._service_id = None
        self._service_type = None
        self._properties = None
        self._commands = None
        self._events = None
        self._description = None
        self._option = None
        self.discriminator = None

        self.service_id = service_id
        self.service_type = service_type
        if properties is not None:
            self.properties = properties
        if commands is not None:
            self.commands = commands
        if events is not None:
            self.events = events
        if description is not None:
            self.description = description
        if option is not None:
            self.option = option

    @property
    def service_id(self):
        """Gets the service_id of this ServiceCapability.

        **参数说明**：设备的服务ID。注：产品内不允许重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-$等字符的组合。

        :return: The service_id of this ServiceCapability.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ServiceCapability.

        **参数说明**：设备的服务ID。注：产品内不允许重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-$等字符的组合。

        :param service_id: The service_id of this ServiceCapability.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_type(self):
        """Gets the service_type of this ServiceCapability.

        **参数说明**：设备的服务类型。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-$等字符的组合。

        :return: The service_type of this ServiceCapability.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ServiceCapability.

        **参数说明**：设备的服务类型。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-$等字符的组合。

        :param service_type: The service_type of this ServiceCapability.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def properties(self):
        """Gets the properties of this ServiceCapability.

        **参数说明**：设备服务支持的属性列表。 **取值范围**：数组长度大小不超过500。

        :return: The properties of this ServiceCapability.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceProperty`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ServiceCapability.

        **参数说明**：设备服务支持的属性列表。 **取值范围**：数组长度大小不超过500。

        :param properties: The properties of this ServiceCapability.
        :type properties: list[:class:`huaweicloudsdkiotda.v5.ServiceProperty`]
        """
        self._properties = properties

    @property
    def commands(self):
        """Gets the commands of this ServiceCapability.

        **参数说明**：设备服务支持的命令列表。 **取值范围**：数组长度大小不超过500。

        :return: The commands of this ServiceCapability.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceCommand`]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this ServiceCapability.

        **参数说明**：设备服务支持的命令列表。 **取值范围**：数组长度大小不超过500。

        :param commands: The commands of this ServiceCapability.
        :type commands: list[:class:`huaweicloudsdkiotda.v5.ServiceCommand`]
        """
        self._commands = commands

    @property
    def events(self):
        """Gets the events of this ServiceCapability.

        **参数说明**：设备服务支持的事件列表。 **取值范围**：数组长度大小不超过500。

        :return: The events of this ServiceCapability.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceEvent`]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ServiceCapability.

        **参数说明**：设备服务支持的事件列表。 **取值范围**：数组长度大小不超过500。

        :param events: The events of this ServiceCapability.
        :type events: list[:class:`huaweicloudsdkiotda.v5.ServiceEvent`]
        """
        self._events = events

    @property
    def description(self):
        """Gets the description of this ServiceCapability.

        **参数说明**：设备服务的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :return: The description of this ServiceCapability.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceCapability.

        **参数说明**：设备服务的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :param description: The description of this ServiceCapability.
        :type description: str
        """
        self._description = description

    @property
    def option(self):
        """Gets the option of this ServiceCapability.

        **参数说明**：指定设备服务是否必选。目前本字段为非功能性字段，仅起到标识作用。 **取值范围**： - Master：主服务 - Mandatory：必选服务 - Optional：可选服务 默认值为Optional。

        :return: The option of this ServiceCapability.
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this ServiceCapability.

        **参数说明**：指定设备服务是否必选。目前本字段为非功能性字段，仅起到标识作用。 **取值范围**： - Master：主服务 - Mandatory：必选服务 - Optional：可选服务 默认值为Optional。

        :param option: The option of this ServiceCapability.
        :type option: str
        """
        self._option = option

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
        if not isinstance(other, ServiceCapability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
