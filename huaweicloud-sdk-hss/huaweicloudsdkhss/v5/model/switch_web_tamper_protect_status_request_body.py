# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchWebTamperProtectStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'operate_type': 'str',
        'charging_mode': 'str',
        'protection_config_id_list': 'list[str]',
        'resource_id_list': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'operate_type': 'operate_type',
        'charging_mode': 'charging_mode',
        'protection_config_id_list': 'protection_config_id_list',
        'resource_id_list': 'resource_id_list'
    }

    def __init__(self, type=None, operate_type=None, charging_mode=None, protection_config_id_list=None, resource_id_list=None):
        r"""SwitchWebTamperProtectStatusRequestBody

        The model defined in huaweicloud sdk

        :param type: 防护类型
        :type type: str
        :param operate_type: 操作类型：（open 开启防护,close 关闭防护）
        :type operate_type: str
        :param charging_mode: 计费模式，开启防护时需要，容器网页防篡改固定传packet_cycle
        :type charging_mode: str
        :param protection_config_id_list: 操作的防护配置id列表
        :type protection_config_id_list: list[str]
        :param resource_id_list: 配额id列表，开启防护时需要（若开启防护时不传该列表，则随机绑定配额）
        :type resource_id_list: list[str]
        """
        
        

        self._type = None
        self._operate_type = None
        self._charging_mode = None
        self._protection_config_id_list = None
        self._resource_id_list = None
        self.discriminator = None

        self.type = type
        self.operate_type = operate_type
        self.charging_mode = charging_mode
        self.protection_config_id_list = protection_config_id_list
        if resource_id_list is not None:
            self.resource_id_list = resource_id_list

    @property
    def type(self):
        r"""Gets the type of this SwitchWebTamperProtectStatusRequestBody.

        防护类型

        :return: The type of this SwitchWebTamperProtectStatusRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SwitchWebTamperProtectStatusRequestBody.

        防护类型

        :param type: The type of this SwitchWebTamperProtectStatusRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def operate_type(self):
        r"""Gets the operate_type of this SwitchWebTamperProtectStatusRequestBody.

        操作类型：（open 开启防护,close 关闭防护）

        :return: The operate_type of this SwitchWebTamperProtectStatusRequestBody.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this SwitchWebTamperProtectStatusRequestBody.

        操作类型：（open 开启防护,close 关闭防护）

        :param operate_type: The operate_type of this SwitchWebTamperProtectStatusRequestBody.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this SwitchWebTamperProtectStatusRequestBody.

        计费模式，开启防护时需要，容器网页防篡改固定传packet_cycle

        :return: The charging_mode of this SwitchWebTamperProtectStatusRequestBody.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this SwitchWebTamperProtectStatusRequestBody.

        计费模式，开启防护时需要，容器网页防篡改固定传packet_cycle

        :param charging_mode: The charging_mode of this SwitchWebTamperProtectStatusRequestBody.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def protection_config_id_list(self):
        r"""Gets the protection_config_id_list of this SwitchWebTamperProtectStatusRequestBody.

        操作的防护配置id列表

        :return: The protection_config_id_list of this SwitchWebTamperProtectStatusRequestBody.
        :rtype: list[str]
        """
        return self._protection_config_id_list

    @protection_config_id_list.setter
    def protection_config_id_list(self, protection_config_id_list):
        r"""Sets the protection_config_id_list of this SwitchWebTamperProtectStatusRequestBody.

        操作的防护配置id列表

        :param protection_config_id_list: The protection_config_id_list of this SwitchWebTamperProtectStatusRequestBody.
        :type protection_config_id_list: list[str]
        """
        self._protection_config_id_list = protection_config_id_list

    @property
    def resource_id_list(self):
        r"""Gets the resource_id_list of this SwitchWebTamperProtectStatusRequestBody.

        配额id列表，开启防护时需要（若开启防护时不传该列表，则随机绑定配额）

        :return: The resource_id_list of this SwitchWebTamperProtectStatusRequestBody.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        r"""Sets the resource_id_list of this SwitchWebTamperProtectStatusRequestBody.

        配额id列表，开启防护时需要（若开启防护时不传该列表，则随机绑定配额）

        :param resource_id_list: The resource_id_list of this SwitchWebTamperProtectStatusRequestBody.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

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
        if not isinstance(other, SwitchWebTamperProtectStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
