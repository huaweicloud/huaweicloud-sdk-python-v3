# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationInstanceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_certificate': 'CertificateDto',
        'display': 'DisplayDto',
        'identity_provider_config': 'IdentityProviderConfigDto',
        'application_instance_id': 'str',
        'name': 'str',
        'visible': 'bool',
        'response_config': 'ResponseConfigDto',
        'response_schema_config': 'ResponseSchemaConfigDto',
        'security_config': 'SecurityConfigDto',
        'status': 'str',
        'template': 'ApplicationTemplateDto',
        'service_provider_config': 'ServiceProviderConfigDto',
        'client_id': 'str',
        'end_user_visible': 'bool',
        'managed_account': 'str'
    }

    attribute_map = {
        'active_certificate': 'active_certificate',
        'display': 'display',
        'identity_provider_config': 'identity_provider_config',
        'application_instance_id': 'application_instance_id',
        'name': 'name',
        'visible': 'visible',
        'response_config': 'response_config',
        'response_schema_config': 'response_schema_config',
        'security_config': 'security_config',
        'status': 'status',
        'template': 'template',
        'service_provider_config': 'service_provider_config',
        'client_id': 'client_id',
        'end_user_visible': 'end_user_visible',
        'managed_account': 'managed_account'
    }

    def __init__(self, active_certificate=None, display=None, identity_provider_config=None, application_instance_id=None, name=None, visible=None, response_config=None, response_schema_config=None, security_config=None, status=None, template=None, service_provider_config=None, client_id=None, end_user_visible=None, managed_account=None):
        r"""ApplicationInstanceDto

        The model defined in huaweicloud sdk

        :param active_certificate: 
        :type active_certificate: :class:`huaweicloudsdkidentitycenter.v1.CertificateDto`
        :param display: 
        :type display: :class:`huaweicloudsdkidentitycenter.v1.DisplayDto`
        :param identity_provider_config: 
        :type identity_provider_config: :class:`huaweicloudsdkidentitycenter.v1.IdentityProviderConfigDto`
        :param application_instance_id: 应用程序实例唯一标识ID
        :type application_instance_id: str
        :param name: 应用程序UUID
        :type name: str
        :param visible: 应用程序在门户是否可见
        :type visible: bool
        :param response_config: 
        :type response_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseConfigDto`
        :param response_schema_config: 
        :type response_schema_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        :param security_config: 
        :type security_config: :class:`huaweicloudsdkidentitycenter.v1.SecurityConfigDto`
        :param status: 应用程序实例状态
        :type status: str
        :param template: 
        :type template: :class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDto`
        :param service_provider_config: 
        :type service_provider_config: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        :param client_id: OIDC Client ID
        :type client_id: str
        :param end_user_visible: 用户是否可见
        :type end_user_visible: bool
        :param managed_account: 组员所属账号ID
        :type managed_account: str
        """
        
        

        self._active_certificate = None
        self._display = None
        self._identity_provider_config = None
        self._application_instance_id = None
        self._name = None
        self._visible = None
        self._response_config = None
        self._response_schema_config = None
        self._security_config = None
        self._status = None
        self._template = None
        self._service_provider_config = None
        self._client_id = None
        self._end_user_visible = None
        self._managed_account = None
        self.discriminator = None

        self.active_certificate = active_certificate
        self.display = display
        self.identity_provider_config = identity_provider_config
        self.application_instance_id = application_instance_id
        self.name = name
        self.visible = visible
        self.response_config = response_config
        self.response_schema_config = response_schema_config
        self.security_config = security_config
        self.status = status
        self.template = template
        self.service_provider_config = service_provider_config
        if client_id is not None:
            self.client_id = client_id
        if end_user_visible is not None:
            self.end_user_visible = end_user_visible
        if managed_account is not None:
            self.managed_account = managed_account

    @property
    def active_certificate(self):
        r"""Gets the active_certificate of this ApplicationInstanceDto.

        :return: The active_certificate of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CertificateDto`
        """
        return self._active_certificate

    @active_certificate.setter
    def active_certificate(self, active_certificate):
        r"""Sets the active_certificate of this ApplicationInstanceDto.

        :param active_certificate: The active_certificate of this ApplicationInstanceDto.
        :type active_certificate: :class:`huaweicloudsdkidentitycenter.v1.CertificateDto`
        """
        self._active_certificate = active_certificate

    @property
    def display(self):
        r"""Gets the display of this ApplicationInstanceDto.

        :return: The display of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DisplayDto`
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this ApplicationInstanceDto.

        :param display: The display of this ApplicationInstanceDto.
        :type display: :class:`huaweicloudsdkidentitycenter.v1.DisplayDto`
        """
        self._display = display

    @property
    def identity_provider_config(self):
        r"""Gets the identity_provider_config of this ApplicationInstanceDto.

        :return: The identity_provider_config of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.IdentityProviderConfigDto`
        """
        return self._identity_provider_config

    @identity_provider_config.setter
    def identity_provider_config(self, identity_provider_config):
        r"""Sets the identity_provider_config of this ApplicationInstanceDto.

        :param identity_provider_config: The identity_provider_config of this ApplicationInstanceDto.
        :type identity_provider_config: :class:`huaweicloudsdkidentitycenter.v1.IdentityProviderConfigDto`
        """
        self._identity_provider_config = identity_provider_config

    @property
    def application_instance_id(self):
        r"""Gets the application_instance_id of this ApplicationInstanceDto.

        应用程序实例唯一标识ID

        :return: The application_instance_id of this ApplicationInstanceDto.
        :rtype: str
        """
        return self._application_instance_id

    @application_instance_id.setter
    def application_instance_id(self, application_instance_id):
        r"""Sets the application_instance_id of this ApplicationInstanceDto.

        应用程序实例唯一标识ID

        :param application_instance_id: The application_instance_id of this ApplicationInstanceDto.
        :type application_instance_id: str
        """
        self._application_instance_id = application_instance_id

    @property
    def name(self):
        r"""Gets the name of this ApplicationInstanceDto.

        应用程序UUID

        :return: The name of this ApplicationInstanceDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationInstanceDto.

        应用程序UUID

        :param name: The name of this ApplicationInstanceDto.
        :type name: str
        """
        self._name = name

    @property
    def visible(self):
        r"""Gets the visible of this ApplicationInstanceDto.

        应用程序在门户是否可见

        :return: The visible of this ApplicationInstanceDto.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this ApplicationInstanceDto.

        应用程序在门户是否可见

        :param visible: The visible of this ApplicationInstanceDto.
        :type visible: bool
        """
        self._visible = visible

    @property
    def response_config(self):
        r"""Gets the response_config of this ApplicationInstanceDto.

        :return: The response_config of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ResponseConfigDto`
        """
        return self._response_config

    @response_config.setter
    def response_config(self, response_config):
        r"""Sets the response_config of this ApplicationInstanceDto.

        :param response_config: The response_config of this ApplicationInstanceDto.
        :type response_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseConfigDto`
        """
        self._response_config = response_config

    @property
    def response_schema_config(self):
        r"""Gets the response_schema_config of this ApplicationInstanceDto.

        :return: The response_schema_config of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        """
        return self._response_schema_config

    @response_schema_config.setter
    def response_schema_config(self, response_schema_config):
        r"""Sets the response_schema_config of this ApplicationInstanceDto.

        :param response_schema_config: The response_schema_config of this ApplicationInstanceDto.
        :type response_schema_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        """
        self._response_schema_config = response_schema_config

    @property
    def security_config(self):
        r"""Gets the security_config of this ApplicationInstanceDto.

        :return: The security_config of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.SecurityConfigDto`
        """
        return self._security_config

    @security_config.setter
    def security_config(self, security_config):
        r"""Sets the security_config of this ApplicationInstanceDto.

        :param security_config: The security_config of this ApplicationInstanceDto.
        :type security_config: :class:`huaweicloudsdkidentitycenter.v1.SecurityConfigDto`
        """
        self._security_config = security_config

    @property
    def status(self):
        r"""Gets the status of this ApplicationInstanceDto.

        应用程序实例状态

        :return: The status of this ApplicationInstanceDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApplicationInstanceDto.

        应用程序实例状态

        :param status: The status of this ApplicationInstanceDto.
        :type status: str
        """
        self._status = status

    @property
    def template(self):
        r"""Gets the template of this ApplicationInstanceDto.

        :return: The template of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDto`
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this ApplicationInstanceDto.

        :param template: The template of this ApplicationInstanceDto.
        :type template: :class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDto`
        """
        self._template = template

    @property
    def service_provider_config(self):
        r"""Gets the service_provider_config of this ApplicationInstanceDto.

        :return: The service_provider_config of this ApplicationInstanceDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        """
        return self._service_provider_config

    @service_provider_config.setter
    def service_provider_config(self, service_provider_config):
        r"""Sets the service_provider_config of this ApplicationInstanceDto.

        :param service_provider_config: The service_provider_config of this ApplicationInstanceDto.
        :type service_provider_config: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        """
        self._service_provider_config = service_provider_config

    @property
    def client_id(self):
        r"""Gets the client_id of this ApplicationInstanceDto.

        OIDC Client ID

        :return: The client_id of this ApplicationInstanceDto.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ApplicationInstanceDto.

        OIDC Client ID

        :param client_id: The client_id of this ApplicationInstanceDto.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def end_user_visible(self):
        r"""Gets the end_user_visible of this ApplicationInstanceDto.

        用户是否可见

        :return: The end_user_visible of this ApplicationInstanceDto.
        :rtype: bool
        """
        return self._end_user_visible

    @end_user_visible.setter
    def end_user_visible(self, end_user_visible):
        r"""Sets the end_user_visible of this ApplicationInstanceDto.

        用户是否可见

        :param end_user_visible: The end_user_visible of this ApplicationInstanceDto.
        :type end_user_visible: bool
        """
        self._end_user_visible = end_user_visible

    @property
    def managed_account(self):
        r"""Gets the managed_account of this ApplicationInstanceDto.

        组员所属账号ID

        :return: The managed_account of this ApplicationInstanceDto.
        :rtype: str
        """
        return self._managed_account

    @managed_account.setter
    def managed_account(self, managed_account):
        r"""Sets the managed_account of this ApplicationInstanceDto.

        组员所属账号ID

        :param managed_account: The managed_account of this ApplicationInstanceDto.
        :type managed_account: str
        """
        self._managed_account = managed_account

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
        if not isinstance(other, ApplicationInstanceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
