# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeAgencyForPodIdentityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assumed_agency': 'AssumedAgency',
        'audience': 'str',
        'credentials': 'Credentials',
        'pod_identity_association_id': 'str',
        'subject': 'PodIdentitySubject'
    }

    attribute_map = {
        'assumed_agency': 'assumedAgency',
        'audience': 'audience',
        'credentials': 'credentials',
        'pod_identity_association_id': 'podIdentityAssociationId',
        'subject': 'subject'
    }

    def __init__(self, assumed_agency=None, audience=None, credentials=None, pod_identity_association_id=None, subject=None):
        r"""AssumeAgencyForPodIdentityResponse

        The model defined in huaweicloud sdk

        :param assumed_agency: 
        :type assumed_agency: :class:`huaweicloudsdkcce.v3.AssumedAgency`
        :param audience: **参数解释：** 凭据签发时传入的audience属性，通过pod-identity关联获取委托凭据的场景下，该值固定为 service.cce.pods。 该属性只在pod-identity关联绑定信任委托时返回 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type audience: str
        :param credentials: 
        :type credentials: :class:`huaweicloudsdkcce.v3.Credentials`
        :param pod_identity_association_id: **参数解释：** 委托凭据所属的pod-identity关联id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type pod_identity_association_id: str
        :param subject: 
        :type subject: :class:`huaweicloudsdkcce.v3.PodIdentitySubject`
        """
        
        super().__init__()

        self._assumed_agency = None
        self._audience = None
        self._credentials = None
        self._pod_identity_association_id = None
        self._subject = None
        self.discriminator = None

        if assumed_agency is not None:
            self.assumed_agency = assumed_agency
        if audience is not None:
            self.audience = audience
        if credentials is not None:
            self.credentials = credentials
        if pod_identity_association_id is not None:
            self.pod_identity_association_id = pod_identity_association_id
        if subject is not None:
            self.subject = subject

    @property
    def assumed_agency(self):
        r"""Gets the assumed_agency of this AssumeAgencyForPodIdentityResponse.

        :return: The assumed_agency of this AssumeAgencyForPodIdentityResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.AssumedAgency`
        """
        return self._assumed_agency

    @assumed_agency.setter
    def assumed_agency(self, assumed_agency):
        r"""Sets the assumed_agency of this AssumeAgencyForPodIdentityResponse.

        :param assumed_agency: The assumed_agency of this AssumeAgencyForPodIdentityResponse.
        :type assumed_agency: :class:`huaweicloudsdkcce.v3.AssumedAgency`
        """
        self._assumed_agency = assumed_agency

    @property
    def audience(self):
        r"""Gets the audience of this AssumeAgencyForPodIdentityResponse.

        **参数解释：** 凭据签发时传入的audience属性，通过pod-identity关联获取委托凭据的场景下，该值固定为 service.cce.pods。 该属性只在pod-identity关联绑定信任委托时返回 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The audience of this AssumeAgencyForPodIdentityResponse.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        r"""Sets the audience of this AssumeAgencyForPodIdentityResponse.

        **参数解释：** 凭据签发时传入的audience属性，通过pod-identity关联获取委托凭据的场景下，该值固定为 service.cce.pods。 该属性只在pod-identity关联绑定信任委托时返回 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param audience: The audience of this AssumeAgencyForPodIdentityResponse.
        :type audience: str
        """
        self._audience = audience

    @property
    def credentials(self):
        r"""Gets the credentials of this AssumeAgencyForPodIdentityResponse.

        :return: The credentials of this AssumeAgencyForPodIdentityResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.Credentials`
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        r"""Sets the credentials of this AssumeAgencyForPodIdentityResponse.

        :param credentials: The credentials of this AssumeAgencyForPodIdentityResponse.
        :type credentials: :class:`huaweicloudsdkcce.v3.Credentials`
        """
        self._credentials = credentials

    @property
    def pod_identity_association_id(self):
        r"""Gets the pod_identity_association_id of this AssumeAgencyForPodIdentityResponse.

        **参数解释：** 委托凭据所属的pod-identity关联id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The pod_identity_association_id of this AssumeAgencyForPodIdentityResponse.
        :rtype: str
        """
        return self._pod_identity_association_id

    @pod_identity_association_id.setter
    def pod_identity_association_id(self, pod_identity_association_id):
        r"""Sets the pod_identity_association_id of this AssumeAgencyForPodIdentityResponse.

        **参数解释：** 委托凭据所属的pod-identity关联id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param pod_identity_association_id: The pod_identity_association_id of this AssumeAgencyForPodIdentityResponse.
        :type pod_identity_association_id: str
        """
        self._pod_identity_association_id = pod_identity_association_id

    @property
    def subject(self):
        r"""Gets the subject of this AssumeAgencyForPodIdentityResponse.

        :return: The subject of this AssumeAgencyForPodIdentityResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.PodIdentitySubject`
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this AssumeAgencyForPodIdentityResponse.

        :param subject: The subject of this AssumeAgencyForPodIdentityResponse.
        :type subject: :class:`huaweicloudsdkcce.v3.PodIdentitySubject`
        """
        self._subject = subject

    def to_dict(self):
        import warnings
        warnings.warn("AssumeAgencyForPodIdentityResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AssumeAgencyForPodIdentityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
