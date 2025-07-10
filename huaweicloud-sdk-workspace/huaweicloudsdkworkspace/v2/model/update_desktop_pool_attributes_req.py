# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDesktopPoolAttributesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'ou_name': 'str',
        'tags': 'list[Tag]',
        'disconnected_retention_period': 'int',
        'enable_autoscale': 'bool',
        'autoscale_policy': 'AutoscalePolicy',
        'in_maintenance_mode': 'bool',
        'desktop_name_policy_id': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ou_name': 'ou_name',
        'tags': 'tags',
        'disconnected_retention_period': 'disconnected_retention_period',
        'enable_autoscale': 'enable_autoscale',
        'autoscale_policy': 'autoscale_policy',
        'in_maintenance_mode': 'in_maintenance_mode',
        'desktop_name_policy_id': 'desktop_name_policy_id',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, name=None, description=None, ou_name=None, tags=None, disconnected_retention_period=None, enable_autoscale=None, autoscale_policy=None, in_maintenance_mode=None, desktop_name_policy_id=None, availability_zone=None):
        r"""UpdateDesktopPoolAttributesReq

        The model defined in huaweicloud sdk

        :param name: 桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。
        :type name: str
        :param description: 桌面池描述。
        :type description: str
        :param ou_name: OU名称，在对接AD时使用，需提前在AD中创建OU。
        :type ou_name: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        :param disconnected_retention_period: 桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。
        :type disconnected_retention_period: int
        :param enable_autoscale: 桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。
        :type enable_autoscale: bool
        :param autoscale_policy: 
        :type autoscale_policy: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        :param in_maintenance_mode: 是否处于管理员维护模式。
        :type in_maintenance_mode: bool
        :param desktop_name_policy_id: 策略id，用于指定生成桌面名称策略。
        :type desktop_name_policy_id: str
        :param availability_zone: 桌面池的可用区。桌面池的可用区是边缘可用区时，不支持修改。
        :type availability_zone: str
        """
        
        

        self._name = None
        self._description = None
        self._ou_name = None
        self._tags = None
        self._disconnected_retention_period = None
        self._enable_autoscale = None
        self._autoscale_policy = None
        self._in_maintenance_mode = None
        self._desktop_name_policy_id = None
        self._availability_zone = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ou_name is not None:
            self.ou_name = ou_name
        if tags is not None:
            self.tags = tags
        if disconnected_retention_period is not None:
            self.disconnected_retention_period = disconnected_retention_period
        if enable_autoscale is not None:
            self.enable_autoscale = enable_autoscale
        if autoscale_policy is not None:
            self.autoscale_policy = autoscale_policy
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode
        if desktop_name_policy_id is not None:
            self.desktop_name_policy_id = desktop_name_policy_id
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def name(self):
        r"""Gets the name of this UpdateDesktopPoolAttributesReq.

        桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。

        :return: The name of this UpdateDesktopPoolAttributesReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateDesktopPoolAttributesReq.

        桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。

        :param name: The name of this UpdateDesktopPoolAttributesReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateDesktopPoolAttributesReq.

        桌面池描述。

        :return: The description of this UpdateDesktopPoolAttributesReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateDesktopPoolAttributesReq.

        桌面池描述。

        :param description: The description of this UpdateDesktopPoolAttributesReq.
        :type description: str
        """
        self._description = description

    @property
    def ou_name(self):
        r"""Gets the ou_name of this UpdateDesktopPoolAttributesReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :return: The ou_name of this UpdateDesktopPoolAttributesReq.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this UpdateDesktopPoolAttributesReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :param ou_name: The ou_name of this UpdateDesktopPoolAttributesReq.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def tags(self):
        r"""Gets the tags of this UpdateDesktopPoolAttributesReq.

        标签列表。

        :return: The tags of this UpdateDesktopPoolAttributesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateDesktopPoolAttributesReq.

        标签列表。

        :param tags: The tags of this UpdateDesktopPoolAttributesReq.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

    @property
    def disconnected_retention_period(self):
        r"""Gets the disconnected_retention_period of this UpdateDesktopPoolAttributesReq.

        桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。

        :return: The disconnected_retention_period of this UpdateDesktopPoolAttributesReq.
        :rtype: int
        """
        return self._disconnected_retention_period

    @disconnected_retention_period.setter
    def disconnected_retention_period(self, disconnected_retention_period):
        r"""Sets the disconnected_retention_period of this UpdateDesktopPoolAttributesReq.

        桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。

        :param disconnected_retention_period: The disconnected_retention_period of this UpdateDesktopPoolAttributesReq.
        :type disconnected_retention_period: int
        """
        self._disconnected_retention_period = disconnected_retention_period

    @property
    def enable_autoscale(self):
        r"""Gets the enable_autoscale of this UpdateDesktopPoolAttributesReq.

        桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。

        :return: The enable_autoscale of this UpdateDesktopPoolAttributesReq.
        :rtype: bool
        """
        return self._enable_autoscale

    @enable_autoscale.setter
    def enable_autoscale(self, enable_autoscale):
        r"""Sets the enable_autoscale of this UpdateDesktopPoolAttributesReq.

        桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。

        :param enable_autoscale: The enable_autoscale of this UpdateDesktopPoolAttributesReq.
        :type enable_autoscale: bool
        """
        self._enable_autoscale = enable_autoscale

    @property
    def autoscale_policy(self):
        r"""Gets the autoscale_policy of this UpdateDesktopPoolAttributesReq.

        :return: The autoscale_policy of this UpdateDesktopPoolAttributesReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        """
        return self._autoscale_policy

    @autoscale_policy.setter
    def autoscale_policy(self, autoscale_policy):
        r"""Sets the autoscale_policy of this UpdateDesktopPoolAttributesReq.

        :param autoscale_policy: The autoscale_policy of this UpdateDesktopPoolAttributesReq.
        :type autoscale_policy: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        """
        self._autoscale_policy = autoscale_policy

    @property
    def in_maintenance_mode(self):
        r"""Gets the in_maintenance_mode of this UpdateDesktopPoolAttributesReq.

        是否处于管理员维护模式。

        :return: The in_maintenance_mode of this UpdateDesktopPoolAttributesReq.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        r"""Sets the in_maintenance_mode of this UpdateDesktopPoolAttributesReq.

        是否处于管理员维护模式。

        :param in_maintenance_mode: The in_maintenance_mode of this UpdateDesktopPoolAttributesReq.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

    @property
    def desktop_name_policy_id(self):
        r"""Gets the desktop_name_policy_id of this UpdateDesktopPoolAttributesReq.

        策略id，用于指定生成桌面名称策略。

        :return: The desktop_name_policy_id of this UpdateDesktopPoolAttributesReq.
        :rtype: str
        """
        return self._desktop_name_policy_id

    @desktop_name_policy_id.setter
    def desktop_name_policy_id(self, desktop_name_policy_id):
        r"""Sets the desktop_name_policy_id of this UpdateDesktopPoolAttributesReq.

        策略id，用于指定生成桌面名称策略。

        :param desktop_name_policy_id: The desktop_name_policy_id of this UpdateDesktopPoolAttributesReq.
        :type desktop_name_policy_id: str
        """
        self._desktop_name_policy_id = desktop_name_policy_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this UpdateDesktopPoolAttributesReq.

        桌面池的可用区。桌面池的可用区是边缘可用区时，不支持修改。

        :return: The availability_zone of this UpdateDesktopPoolAttributesReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this UpdateDesktopPoolAttributesReq.

        桌面池的可用区。桌面池的可用区是边缘可用区时，不支持修改。

        :param availability_zone: The availability_zone of this UpdateDesktopPoolAttributesReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, UpdateDesktopPoolAttributesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
