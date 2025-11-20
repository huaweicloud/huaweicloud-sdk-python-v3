# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantServiceConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_shared_config': 'ServiceSharedConfig',
        'tenant_log_config': 'TenantLogConfig',
        'sub_account_control_config': 'SubAccountControlConfig',
        'is_ai_mark_on': 'bool',
        'tenant_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'service_shared_config': 'service_shared_config',
        'tenant_log_config': 'tenant_log_config',
        'sub_account_control_config': 'sub_account_control_config',
        'is_ai_mark_on': 'is_ai_mark_on',
        'tenant_id': 'tenant_id',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, service_shared_config=None, tenant_log_config=None, sub_account_control_config=None, is_ai_mark_on=None, tenant_id=None, x_request_id=None):
        r"""UpdateTenantServiceConfigsResponse

        The model defined in huaweicloud sdk

        :param service_shared_config: 
        :type service_shared_config: :class:`huaweicloudsdkmetastudio.v1.ServiceSharedConfig`
        :param tenant_log_config: 
        :type tenant_log_config: :class:`huaweicloudsdkmetastudio.v1.TenantLogConfig`
        :param sub_account_control_config: 
        :type sub_account_control_config: :class:`huaweicloudsdkmetastudio.v1.SubAccountControlConfig`
        :param is_ai_mark_on: AI标识开关
        :type is_ai_mark_on: bool
        :param tenant_id: 租户project ID
        :type tenant_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._service_shared_config = None
        self._tenant_log_config = None
        self._sub_account_control_config = None
        self._is_ai_mark_on = None
        self._tenant_id = None
        self._x_request_id = None
        self.discriminator = None

        if service_shared_config is not None:
            self.service_shared_config = service_shared_config
        if tenant_log_config is not None:
            self.tenant_log_config = tenant_log_config
        if sub_account_control_config is not None:
            self.sub_account_control_config = sub_account_control_config
        if is_ai_mark_on is not None:
            self.is_ai_mark_on = is_ai_mark_on
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def service_shared_config(self):
        r"""Gets the service_shared_config of this UpdateTenantServiceConfigsResponse.

        :return: The service_shared_config of this UpdateTenantServiceConfigsResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ServiceSharedConfig`
        """
        return self._service_shared_config

    @service_shared_config.setter
    def service_shared_config(self, service_shared_config):
        r"""Sets the service_shared_config of this UpdateTenantServiceConfigsResponse.

        :param service_shared_config: The service_shared_config of this UpdateTenantServiceConfigsResponse.
        :type service_shared_config: :class:`huaweicloudsdkmetastudio.v1.ServiceSharedConfig`
        """
        self._service_shared_config = service_shared_config

    @property
    def tenant_log_config(self):
        r"""Gets the tenant_log_config of this UpdateTenantServiceConfigsResponse.

        :return: The tenant_log_config of this UpdateTenantServiceConfigsResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TenantLogConfig`
        """
        return self._tenant_log_config

    @tenant_log_config.setter
    def tenant_log_config(self, tenant_log_config):
        r"""Sets the tenant_log_config of this UpdateTenantServiceConfigsResponse.

        :param tenant_log_config: The tenant_log_config of this UpdateTenantServiceConfigsResponse.
        :type tenant_log_config: :class:`huaweicloudsdkmetastudio.v1.TenantLogConfig`
        """
        self._tenant_log_config = tenant_log_config

    @property
    def sub_account_control_config(self):
        r"""Gets the sub_account_control_config of this UpdateTenantServiceConfigsResponse.

        :return: The sub_account_control_config of this UpdateTenantServiceConfigsResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SubAccountControlConfig`
        """
        return self._sub_account_control_config

    @sub_account_control_config.setter
    def sub_account_control_config(self, sub_account_control_config):
        r"""Sets the sub_account_control_config of this UpdateTenantServiceConfigsResponse.

        :param sub_account_control_config: The sub_account_control_config of this UpdateTenantServiceConfigsResponse.
        :type sub_account_control_config: :class:`huaweicloudsdkmetastudio.v1.SubAccountControlConfig`
        """
        self._sub_account_control_config = sub_account_control_config

    @property
    def is_ai_mark_on(self):
        r"""Gets the is_ai_mark_on of this UpdateTenantServiceConfigsResponse.

        AI标识开关

        :return: The is_ai_mark_on of this UpdateTenantServiceConfigsResponse.
        :rtype: bool
        """
        return self._is_ai_mark_on

    @is_ai_mark_on.setter
    def is_ai_mark_on(self, is_ai_mark_on):
        r"""Sets the is_ai_mark_on of this UpdateTenantServiceConfigsResponse.

        AI标识开关

        :param is_ai_mark_on: The is_ai_mark_on of this UpdateTenantServiceConfigsResponse.
        :type is_ai_mark_on: bool
        """
        self._is_ai_mark_on = is_ai_mark_on

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this UpdateTenantServiceConfigsResponse.

        租户project ID

        :return: The tenant_id of this UpdateTenantServiceConfigsResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this UpdateTenantServiceConfigsResponse.

        租户project ID

        :param tenant_id: The tenant_id of this UpdateTenantServiceConfigsResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateTenantServiceConfigsResponse.

        :return: The x_request_id of this UpdateTenantServiceConfigsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateTenantServiceConfigsResponse.

        :param x_request_id: The x_request_id of this UpdateTenantServiceConfigsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("UpdateTenantServiceConfigsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateTenantServiceConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
