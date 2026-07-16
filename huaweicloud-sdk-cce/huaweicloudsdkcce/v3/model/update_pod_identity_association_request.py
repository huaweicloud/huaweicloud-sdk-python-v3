# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePodIdentityAssociationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'association_id': 'str',
        'body': 'PodIdentityAssociationUpdate'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'association_id': 'association_id',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, association_id=None, body=None):
        r"""UpdatePodIdentityAssociationRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param association_id: **参数解释**： Pod-identity关联ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type association_id: str
        :param body: Body of the UpdatePodIdentityAssociationRequest
        :type body: :class:`huaweicloudsdkcce.v3.PodIdentityAssociationUpdate`
        """
        
        

        self._cluster_id = None
        self._association_id = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.association_id = association_id
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdatePodIdentityAssociationRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this UpdatePodIdentityAssociationRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdatePodIdentityAssociationRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this UpdatePodIdentityAssociationRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def association_id(self):
        r"""Gets the association_id of this UpdatePodIdentityAssociationRequest.

        **参数解释**： Pod-identity关联ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The association_id of this UpdatePodIdentityAssociationRequest.
        :rtype: str
        """
        return self._association_id

    @association_id.setter
    def association_id(self, association_id):
        r"""Sets the association_id of this UpdatePodIdentityAssociationRequest.

        **参数解释**： Pod-identity关联ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param association_id: The association_id of this UpdatePodIdentityAssociationRequest.
        :type association_id: str
        """
        self._association_id = association_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePodIdentityAssociationRequest.

        :return: The body of this UpdatePodIdentityAssociationRequest.
        :rtype: :class:`huaweicloudsdkcce.v3.PodIdentityAssociationUpdate`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePodIdentityAssociationRequest.

        :param body: The body of this UpdatePodIdentityAssociationRequest.
        :type body: :class:`huaweicloudsdkcce.v3.PodIdentityAssociationUpdate`
        """
        self._body = body

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
        if not isinstance(other, UpdatePodIdentityAssociationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
