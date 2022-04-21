# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDeviceGroupDTO:

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
        'super_group_id': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'super_group_id': 'super_group_id',
        'app_id': 'app_id'
    }

    def __init__(self, name=None, description=None, super_group_id=None, app_id=None):
        """AddDeviceGroupDTO

        The model defined in huaweicloud sdk

        :param name: **参数说明**：设备组名称，单个资源空间下不可重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? &#39;#().,&amp;%@!-等字符的组合。
        :type name: str
        :param description: **参数说明**：设备组描述。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? &#39;#().,&amp;%@!-等字符的组合。
        :type description: str
        :param super_group_id: **参数说明**：父设备组ID，携带该参数时表示在该设备组下创建一个子设备组。 **取值范围**：长度不超过36，十六进制字符串和连接符（-）的组合。
        :type super_group_id: str
        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        """
        
        

        self._name = None
        self._description = None
        self._super_group_id = None
        self._app_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if super_group_id is not None:
            self.super_group_id = super_group_id
        if app_id is not None:
            self.app_id = app_id

    @property
    def name(self):
        """Gets the name of this AddDeviceGroupDTO.

        **参数说明**：设备组名称，单个资源空间下不可重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :return: The name of this AddDeviceGroupDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddDeviceGroupDTO.

        **参数说明**：设备组名称，单个资源空间下不可重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :param name: The name of this AddDeviceGroupDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AddDeviceGroupDTO.

        **参数说明**：设备组描述。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :return: The description of this AddDeviceGroupDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddDeviceGroupDTO.

        **参数说明**：设备组描述。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :param description: The description of this AddDeviceGroupDTO.
        :type description: str
        """
        self._description = description

    @property
    def super_group_id(self):
        """Gets the super_group_id of this AddDeviceGroupDTO.

        **参数说明**：父设备组ID，携带该参数时表示在该设备组下创建一个子设备组。 **取值范围**：长度不超过36，十六进制字符串和连接符（-）的组合。

        :return: The super_group_id of this AddDeviceGroupDTO.
        :rtype: str
        """
        return self._super_group_id

    @super_group_id.setter
    def super_group_id(self, super_group_id):
        """Sets the super_group_id of this AddDeviceGroupDTO.

        **参数说明**：父设备组ID，携带该参数时表示在该设备组下创建一个子设备组。 **取值范围**：长度不超过36，十六进制字符串和连接符（-）的组合。

        :param super_group_id: The super_group_id of this AddDeviceGroupDTO.
        :type super_group_id: str
        """
        self._super_group_id = super_group_id

    @property
    def app_id(self):
        """Gets the app_id of this AddDeviceGroupDTO.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this AddDeviceGroupDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddDeviceGroupDTO.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this AddDeviceGroupDTO.
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
        if not isinstance(other, AddDeviceGroupDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
