# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddHarmonySoftBusDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bus_name': 'str',
        'group_id': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'bus_name': 'bus_name',
        'group_id': 'group_id',
        'app_id': 'app_id'
    }

    def __init__(self, bus_name=None, group_id=None, app_id=None):
        r"""AddHarmonySoftBusDTO

        The model defined in huaweicloud sdk

        :param bus_name: **参数说明**：鸿蒙软总线组名称，单个资源空间下不可重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? &#39;#().,&amp;%@!-等字符的组合。
        :type bus_name: str
        :param group_id: **参数说明**：设备组ID，用于唯一标识一个设备组，在创建设备组时由物联网平台分配。
        :type group_id: str
        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        """
        
        

        self._bus_name = None
        self._group_id = None
        self._app_id = None
        self.discriminator = None

        if bus_name is not None:
            self.bus_name = bus_name
        if group_id is not None:
            self.group_id = group_id
        if app_id is not None:
            self.app_id = app_id

    @property
    def bus_name(self):
        r"""Gets the bus_name of this AddHarmonySoftBusDTO.

        **参数说明**：鸿蒙软总线组名称，单个资源空间下不可重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :return: The bus_name of this AddHarmonySoftBusDTO.
        :rtype: str
        """
        return self._bus_name

    @bus_name.setter
    def bus_name(self, bus_name):
        r"""Sets the bus_name of this AddHarmonySoftBusDTO.

        **参数说明**：鸿蒙软总线组名称，单个资源空间下不可重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :param bus_name: The bus_name of this AddHarmonySoftBusDTO.
        :type bus_name: str
        """
        self._bus_name = bus_name

    @property
    def group_id(self):
        r"""Gets the group_id of this AddHarmonySoftBusDTO.

        **参数说明**：设备组ID，用于唯一标识一个设备组，在创建设备组时由物联网平台分配。

        :return: The group_id of this AddHarmonySoftBusDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AddHarmonySoftBusDTO.

        **参数说明**：设备组ID，用于唯一标识一个设备组，在创建设备组时由物联网平台分配。

        :param group_id: The group_id of this AddHarmonySoftBusDTO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def app_id(self):
        r"""Gets the app_id of this AddHarmonySoftBusDTO.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this AddHarmonySoftBusDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AddHarmonySoftBusDTO.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this AddHarmonySoftBusDTO.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, AddHarmonySoftBusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
