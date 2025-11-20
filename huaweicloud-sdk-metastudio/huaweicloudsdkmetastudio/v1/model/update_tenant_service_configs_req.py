# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantServiceConfigsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_account_control_config': 'SubAccountControlConfig',
        'is_ai_mark_on': 'bool'
    }

    attribute_map = {
        'sub_account_control_config': 'sub_account_control_config',
        'is_ai_mark_on': 'is_ai_mark_on'
    }

    def __init__(self, sub_account_control_config=None, is_ai_mark_on=None):
        r"""UpdateTenantServiceConfigsReq

        The model defined in huaweicloud sdk

        :param sub_account_control_config: 
        :type sub_account_control_config: :class:`huaweicloudsdkmetastudio.v1.SubAccountControlConfig`
        :param is_ai_mark_on: AI标识开关
        :type is_ai_mark_on: bool
        """
        
        

        self._sub_account_control_config = None
        self._is_ai_mark_on = None
        self.discriminator = None

        if sub_account_control_config is not None:
            self.sub_account_control_config = sub_account_control_config
        if is_ai_mark_on is not None:
            self.is_ai_mark_on = is_ai_mark_on

    @property
    def sub_account_control_config(self):
        r"""Gets the sub_account_control_config of this UpdateTenantServiceConfigsReq.

        :return: The sub_account_control_config of this UpdateTenantServiceConfigsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SubAccountControlConfig`
        """
        return self._sub_account_control_config

    @sub_account_control_config.setter
    def sub_account_control_config(self, sub_account_control_config):
        r"""Sets the sub_account_control_config of this UpdateTenantServiceConfigsReq.

        :param sub_account_control_config: The sub_account_control_config of this UpdateTenantServiceConfigsReq.
        :type sub_account_control_config: :class:`huaweicloudsdkmetastudio.v1.SubAccountControlConfig`
        """
        self._sub_account_control_config = sub_account_control_config

    @property
    def is_ai_mark_on(self):
        r"""Gets the is_ai_mark_on of this UpdateTenantServiceConfigsReq.

        AI标识开关

        :return: The is_ai_mark_on of this UpdateTenantServiceConfigsReq.
        :rtype: bool
        """
        return self._is_ai_mark_on

    @is_ai_mark_on.setter
    def is_ai_mark_on(self, is_ai_mark_on):
        r"""Sets the is_ai_mark_on of this UpdateTenantServiceConfigsReq.

        AI标识开关

        :param is_ai_mark_on: The is_ai_mark_on of this UpdateTenantServiceConfigsReq.
        :type is_ai_mark_on: bool
        """
        self._is_ai_mark_on = is_ai_mark_on

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
        if not isinstance(other, UpdateTenantServiceConfigsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
