# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterCondition:

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
        'status': 'str',
        'last_probe_time': 'str',
        'last_transit_time': 'str',
        'reason': 'str',
        'message': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'last_probe_time': 'lastProbeTime',
        'last_transit_time': 'lastTransitTime',
        'reason': 'reason',
        'message': 'message'
    }

    def __init__(self, type=None, status=None, last_probe_time=None, last_transit_time=None, reason=None, message=None):
        r"""ClusterCondition

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 状态类型。 **约束限制**： 不涉及 **取值范围**： - \&quot;AgencyAvailable\&quot;: CCE集群自定义委托的状态。 - \&quot;ClusterCertificate\&quot;: CCE集群证书的状态。 - \&quot;ClusterCustomCertificate\&quot;: CCE集群自有证书的状态。 - \&quot;CertificateRotation\&quot;: CCE集群证书更新的状态。 - \&quot;CustomCertificateRotation\&quot;: CCE集群自有证书更新的状态。 - \&quot;OpenIDConnectProcessing\&quot;: CCE集群开启OIDC特性处理中状态。 - \&quot;OpenIDConnectProcessSuccess\&quot;: CCE集群开启OIDC特性成功状态。 - \&quot;OpenIDConnectProcessFailed\&quot;: CCE集群开启OIDC特性失败状态。  **默认取值**： 不涉及
        :type type: str
        :param status: **参数解释**： Condition当前状态。 **约束限制**： 不涉及 **取值范围**： - \&quot;True\&quot; - \&quot;False\&quot;  **默认取值**： 不涉及
        :type status: str
        :param last_probe_time: **参数解释**： 上次状态检查时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type last_probe_time: str
        :param last_transit_time: **参数解释**： 上次状态变更时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type last_transit_time: str
        :param reason: **参数解释**： 上次状态变更原因。 **约束限制**： 不涉及 **取值范围**： - type为ClusterCertificate、ClusterCustomCertificate时取值范围：   - CertificateValid：证书状态正常   - CertificateExpiringWithin180Days：证书有效期低于180天   - CertificateExpiringWithin30Days：证书有效期低于30天   - CertificateExpired：证书已过期 - type为CertificateRotation、CustomCertificateRotation时取值范围：   - RotationInProgress：更新中   - RotationSucceeded：更新成功   - RotationFailed：更新失败  **默认取值**： 不涉及
        :type reason: str
        :param message: **参数解释**： Condition详细描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type message: str
        """
        
        

        self._type = None
        self._status = None
        self._last_probe_time = None
        self._last_transit_time = None
        self._reason = None
        self._message = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if last_probe_time is not None:
            self.last_probe_time = last_probe_time
        if last_transit_time is not None:
            self.last_transit_time = last_transit_time
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message

    @property
    def type(self):
        r"""Gets the type of this ClusterCondition.

        **参数解释**： 状态类型。 **约束限制**： 不涉及 **取值范围**： - \"AgencyAvailable\": CCE集群自定义委托的状态。 - \"ClusterCertificate\": CCE集群证书的状态。 - \"ClusterCustomCertificate\": CCE集群自有证书的状态。 - \"CertificateRotation\": CCE集群证书更新的状态。 - \"CustomCertificateRotation\": CCE集群自有证书更新的状态。 - \"OpenIDConnectProcessing\": CCE集群开启OIDC特性处理中状态。 - \"OpenIDConnectProcessSuccess\": CCE集群开启OIDC特性成功状态。 - \"OpenIDConnectProcessFailed\": CCE集群开启OIDC特性失败状态。  **默认取值**： 不涉及

        :return: The type of this ClusterCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterCondition.

        **参数解释**： 状态类型。 **约束限制**： 不涉及 **取值范围**： - \"AgencyAvailable\": CCE集群自定义委托的状态。 - \"ClusterCertificate\": CCE集群证书的状态。 - \"ClusterCustomCertificate\": CCE集群自有证书的状态。 - \"CertificateRotation\": CCE集群证书更新的状态。 - \"CustomCertificateRotation\": CCE集群自有证书更新的状态。 - \"OpenIDConnectProcessing\": CCE集群开启OIDC特性处理中状态。 - \"OpenIDConnectProcessSuccess\": CCE集群开启OIDC特性成功状态。 - \"OpenIDConnectProcessFailed\": CCE集群开启OIDC特性失败状态。  **默认取值**： 不涉及

        :param type: The type of this ClusterCondition.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ClusterCondition.

        **参数解释**： Condition当前状态。 **约束限制**： 不涉及 **取值范围**： - \"True\" - \"False\"  **默认取值**： 不涉及

        :return: The status of this ClusterCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterCondition.

        **参数解释**： Condition当前状态。 **约束限制**： 不涉及 **取值范围**： - \"True\" - \"False\"  **默认取值**： 不涉及

        :param status: The status of this ClusterCondition.
        :type status: str
        """
        self._status = status

    @property
    def last_probe_time(self):
        r"""Gets the last_probe_time of this ClusterCondition.

        **参数解释**： 上次状态检查时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The last_probe_time of this ClusterCondition.
        :rtype: str
        """
        return self._last_probe_time

    @last_probe_time.setter
    def last_probe_time(self, last_probe_time):
        r"""Sets the last_probe_time of this ClusterCondition.

        **参数解释**： 上次状态检查时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param last_probe_time: The last_probe_time of this ClusterCondition.
        :type last_probe_time: str
        """
        self._last_probe_time = last_probe_time

    @property
    def last_transit_time(self):
        r"""Gets the last_transit_time of this ClusterCondition.

        **参数解释**： 上次状态变更时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The last_transit_time of this ClusterCondition.
        :rtype: str
        """
        return self._last_transit_time

    @last_transit_time.setter
    def last_transit_time(self, last_transit_time):
        r"""Sets the last_transit_time of this ClusterCondition.

        **参数解释**： 上次状态变更时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param last_transit_time: The last_transit_time of this ClusterCondition.
        :type last_transit_time: str
        """
        self._last_transit_time = last_transit_time

    @property
    def reason(self):
        r"""Gets the reason of this ClusterCondition.

        **参数解释**： 上次状态变更原因。 **约束限制**： 不涉及 **取值范围**： - type为ClusterCertificate、ClusterCustomCertificate时取值范围：   - CertificateValid：证书状态正常   - CertificateExpiringWithin180Days：证书有效期低于180天   - CertificateExpiringWithin30Days：证书有效期低于30天   - CertificateExpired：证书已过期 - type为CertificateRotation、CustomCertificateRotation时取值范围：   - RotationInProgress：更新中   - RotationSucceeded：更新成功   - RotationFailed：更新失败  **默认取值**： 不涉及

        :return: The reason of this ClusterCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ClusterCondition.

        **参数解释**： 上次状态变更原因。 **约束限制**： 不涉及 **取值范围**： - type为ClusterCertificate、ClusterCustomCertificate时取值范围：   - CertificateValid：证书状态正常   - CertificateExpiringWithin180Days：证书有效期低于180天   - CertificateExpiringWithin30Days：证书有效期低于30天   - CertificateExpired：证书已过期 - type为CertificateRotation、CustomCertificateRotation时取值范围：   - RotationInProgress：更新中   - RotationSucceeded：更新成功   - RotationFailed：更新失败  **默认取值**： 不涉及

        :param reason: The reason of this ClusterCondition.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        r"""Gets the message of this ClusterCondition.

        **参数解释**： Condition详细描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The message of this ClusterCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ClusterCondition.

        **参数解释**： Condition详细描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param message: The message of this ClusterCondition.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ClusterCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
