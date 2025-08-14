# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationTemplateDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application': 'ApplicationTemplateDisplayDto',
        'response_config': 'ResponseConfigDto',
        'response_schema_config': 'ResponseSchemaConfigDto',
        'sso_protocol': 'str',
        'security_config': 'SecurityConfigDto',
        'service_provider_config': 'ServiceProviderConfigDto',
        'template_id': 'str',
        'template_version': 'str'
    }

    attribute_map = {
        'application': 'application',
        'response_config': 'response_config',
        'response_schema_config': 'response_schema_config',
        'sso_protocol': 'sso_protocol',
        'security_config': 'security_config',
        'service_provider_config': 'service_provider_config',
        'template_id': 'template_id',
        'template_version': 'template_version'
    }

    def __init__(self, application=None, response_config=None, response_schema_config=None, sso_protocol=None, security_config=None, service_provider_config=None, template_id=None, template_version=None):
        r"""ApplicationTemplateDto

        The model defined in huaweicloud sdk

        :param application: 
        :type application: :class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDisplayDto`
        :param response_config: 
        :type response_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseConfigDto`
        :param response_schema_config: 
        :type response_schema_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        :param sso_protocol: 支持的协议
        :type sso_protocol: str
        :param security_config: 
        :type security_config: :class:`huaweicloudsdkidentitycenter.v1.SecurityConfigDto`
        :param service_provider_config: 
        :type service_provider_config: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        :param template_id: 应用程序模板唯一标识ID
        :type template_id: str
        :param template_version: 应用程序模板版本
        :type template_version: str
        """
        
        

        self._application = None
        self._response_config = None
        self._response_schema_config = None
        self._sso_protocol = None
        self._security_config = None
        self._service_provider_config = None
        self._template_id = None
        self._template_version = None
        self.discriminator = None

        self.application = application
        self.response_config = response_config
        self.response_schema_config = response_schema_config
        self.sso_protocol = sso_protocol
        self.security_config = security_config
        self.service_provider_config = service_provider_config
        self.template_id = template_id
        self.template_version = template_version

    @property
    def application(self):
        r"""Gets the application of this ApplicationTemplateDto.

        :return: The application of this ApplicationTemplateDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDisplayDto`
        """
        return self._application

    @application.setter
    def application(self, application):
        r"""Sets the application of this ApplicationTemplateDto.

        :param application: The application of this ApplicationTemplateDto.
        :type application: :class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDisplayDto`
        """
        self._application = application

    @property
    def response_config(self):
        r"""Gets the response_config of this ApplicationTemplateDto.

        :return: The response_config of this ApplicationTemplateDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ResponseConfigDto`
        """
        return self._response_config

    @response_config.setter
    def response_config(self, response_config):
        r"""Sets the response_config of this ApplicationTemplateDto.

        :param response_config: The response_config of this ApplicationTemplateDto.
        :type response_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseConfigDto`
        """
        self._response_config = response_config

    @property
    def response_schema_config(self):
        r"""Gets the response_schema_config of this ApplicationTemplateDto.

        :return: The response_schema_config of this ApplicationTemplateDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        """
        return self._response_schema_config

    @response_schema_config.setter
    def response_schema_config(self, response_schema_config):
        r"""Sets the response_schema_config of this ApplicationTemplateDto.

        :param response_schema_config: The response_schema_config of this ApplicationTemplateDto.
        :type response_schema_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        """
        self._response_schema_config = response_schema_config

    @property
    def sso_protocol(self):
        r"""Gets the sso_protocol of this ApplicationTemplateDto.

        支持的协议

        :return: The sso_protocol of this ApplicationTemplateDto.
        :rtype: str
        """
        return self._sso_protocol

    @sso_protocol.setter
    def sso_protocol(self, sso_protocol):
        r"""Sets the sso_protocol of this ApplicationTemplateDto.

        支持的协议

        :param sso_protocol: The sso_protocol of this ApplicationTemplateDto.
        :type sso_protocol: str
        """
        self._sso_protocol = sso_protocol

    @property
    def security_config(self):
        r"""Gets the security_config of this ApplicationTemplateDto.

        :return: The security_config of this ApplicationTemplateDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.SecurityConfigDto`
        """
        return self._security_config

    @security_config.setter
    def security_config(self, security_config):
        r"""Sets the security_config of this ApplicationTemplateDto.

        :param security_config: The security_config of this ApplicationTemplateDto.
        :type security_config: :class:`huaweicloudsdkidentitycenter.v1.SecurityConfigDto`
        """
        self._security_config = security_config

    @property
    def service_provider_config(self):
        r"""Gets the service_provider_config of this ApplicationTemplateDto.

        :return: The service_provider_config of this ApplicationTemplateDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        """
        return self._service_provider_config

    @service_provider_config.setter
    def service_provider_config(self, service_provider_config):
        r"""Sets the service_provider_config of this ApplicationTemplateDto.

        :param service_provider_config: The service_provider_config of this ApplicationTemplateDto.
        :type service_provider_config: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        """
        self._service_provider_config = service_provider_config

    @property
    def template_id(self):
        r"""Gets the template_id of this ApplicationTemplateDto.

        应用程序模板唯一标识ID

        :return: The template_id of this ApplicationTemplateDto.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ApplicationTemplateDto.

        应用程序模板唯一标识ID

        :param template_id: The template_id of this ApplicationTemplateDto.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_version(self):
        r"""Gets the template_version of this ApplicationTemplateDto.

        应用程序模板版本

        :return: The template_version of this ApplicationTemplateDto.
        :rtype: str
        """
        return self._template_version

    @template_version.setter
    def template_version(self, template_version):
        r"""Sets the template_version of this ApplicationTemplateDto.

        应用程序模板版本

        :param template_version: The template_version of this ApplicationTemplateDto.
        :type template_version: str
        """
        self._template_version = template_version

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
        if not isinstance(other, ApplicationTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
