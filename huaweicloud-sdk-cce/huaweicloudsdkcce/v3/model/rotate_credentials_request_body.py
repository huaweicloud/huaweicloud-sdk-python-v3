# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RotateCredentialsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component': 'str',
        'certificate_expiration_time': 'int',
        'cert_content': 'AuthenticatingProxy'
    }

    attribute_map = {
        'component': 'component',
        'certificate_expiration_time': 'certificateExpirationTime',
        'cert_content': 'certContent'
    }

    def __init__(self, component=None, certificate_expiration_time=None, cert_content=None):
        r"""RotateCredentialsRequestBody

        The model defined in huaweicloud sdk

        :param component: **参数解释：**  需要轮转的组件名称。 **约束限制：** 不涉及 **取值范围：** - all：轮转CCE集群证书。 - service-account-controller：轮转ServiceAccount token相关证书。 - custom：轮转用户自有证书，指定此参数时，需同时指定certContent参数。  **默认取值：** 不涉及 
        :type component: str
        :param certificate_expiration_time: **参数解释：**  轮转证书后，用于验证ServiceAccount Token签名的旧证书保留时间。  为了保证基于旧证书签发的ServiceAccount Token在证书轮转后能验签通过，CCE会保留老证书一段时间，具体规则如下： - 首次轮转时，CCE会保留创建集群时生成的证书； - 从第二次轮转开始，CCE会保留老证书一段时间，默认24小时。用户可以通过当前参数配置保留的时间。  **约束限制：** 不涉及 **取值范围：** 0-8784（小时） **默认取值：** 24（小时） 
        :type certificate_expiration_time: int
        :param cert_content: 
        :type cert_content: :class:`huaweicloudsdkcce.v3.AuthenticatingProxy`
        """
        
        

        self._component = None
        self._certificate_expiration_time = None
        self._cert_content = None
        self.discriminator = None

        self.component = component
        if certificate_expiration_time is not None:
            self.certificate_expiration_time = certificate_expiration_time
        if cert_content is not None:
            self.cert_content = cert_content

    @property
    def component(self):
        r"""Gets the component of this RotateCredentialsRequestBody.

        **参数解释：**  需要轮转的组件名称。 **约束限制：** 不涉及 **取值范围：** - all：轮转CCE集群证书。 - service-account-controller：轮转ServiceAccount token相关证书。 - custom：轮转用户自有证书，指定此参数时，需同时指定certContent参数。  **默认取值：** 不涉及 

        :return: The component of this RotateCredentialsRequestBody.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        r"""Sets the component of this RotateCredentialsRequestBody.

        **参数解释：**  需要轮转的组件名称。 **约束限制：** 不涉及 **取值范围：** - all：轮转CCE集群证书。 - service-account-controller：轮转ServiceAccount token相关证书。 - custom：轮转用户自有证书，指定此参数时，需同时指定certContent参数。  **默认取值：** 不涉及 

        :param component: The component of this RotateCredentialsRequestBody.
        :type component: str
        """
        self._component = component

    @property
    def certificate_expiration_time(self):
        r"""Gets the certificate_expiration_time of this RotateCredentialsRequestBody.

        **参数解释：**  轮转证书后，用于验证ServiceAccount Token签名的旧证书保留时间。  为了保证基于旧证书签发的ServiceAccount Token在证书轮转后能验签通过，CCE会保留老证书一段时间，具体规则如下： - 首次轮转时，CCE会保留创建集群时生成的证书； - 从第二次轮转开始，CCE会保留老证书一段时间，默认24小时。用户可以通过当前参数配置保留的时间。  **约束限制：** 不涉及 **取值范围：** 0-8784（小时） **默认取值：** 24（小时） 

        :return: The certificate_expiration_time of this RotateCredentialsRequestBody.
        :rtype: int
        """
        return self._certificate_expiration_time

    @certificate_expiration_time.setter
    def certificate_expiration_time(self, certificate_expiration_time):
        r"""Sets the certificate_expiration_time of this RotateCredentialsRequestBody.

        **参数解释：**  轮转证书后，用于验证ServiceAccount Token签名的旧证书保留时间。  为了保证基于旧证书签发的ServiceAccount Token在证书轮转后能验签通过，CCE会保留老证书一段时间，具体规则如下： - 首次轮转时，CCE会保留创建集群时生成的证书； - 从第二次轮转开始，CCE会保留老证书一段时间，默认24小时。用户可以通过当前参数配置保留的时间。  **约束限制：** 不涉及 **取值范围：** 0-8784（小时） **默认取值：** 24（小时） 

        :param certificate_expiration_time: The certificate_expiration_time of this RotateCredentialsRequestBody.
        :type certificate_expiration_time: int
        """
        self._certificate_expiration_time = certificate_expiration_time

    @property
    def cert_content(self):
        r"""Gets the cert_content of this RotateCredentialsRequestBody.

        :return: The cert_content of this RotateCredentialsRequestBody.
        :rtype: :class:`huaweicloudsdkcce.v3.AuthenticatingProxy`
        """
        return self._cert_content

    @cert_content.setter
    def cert_content(self, cert_content):
        r"""Sets the cert_content of this RotateCredentialsRequestBody.

        :param cert_content: The cert_content of this RotateCredentialsRequestBody.
        :type cert_content: :class:`huaweicloudsdkcce.v3.AuthenticatingProxy`
        """
        self._cert_content = cert_content

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
        if not isinstance(other, RotateCredentialsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
