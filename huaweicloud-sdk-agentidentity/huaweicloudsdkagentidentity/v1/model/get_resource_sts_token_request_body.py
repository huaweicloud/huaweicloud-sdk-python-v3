# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceStsTokenRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('workload_access_token')

    openapi_types = {
        'resource_credential_provider_name': 'str',
        'workload_access_token': 'str',
        'agency_session_name': 'str',
        'duration_seconds': 'int',
        'policy': 'str',
        'source_identity': 'str',
        'tags': 'list[StsTag]',
        'transitive_tag_keys': 'list[str]'
    }

    attribute_map = {
        'resource_credential_provider_name': 'resource_credential_provider_name',
        'workload_access_token': 'workload_access_token',
        'agency_session_name': 'agency_session_name',
        'duration_seconds': 'duration_seconds',
        'policy': 'policy',
        'source_identity': 'source_identity',
        'tags': 'tags',
        'transitive_tag_keys': 'transitive_tag_keys'
    }

    def __init__(self, resource_credential_provider_name=None, workload_access_token=None, agency_session_name=None, duration_seconds=None, policy=None, source_identity=None, tags=None, transitive_tag_keys=None):
        r"""GetResourceStsTokenRequestBody

        The model defined in huaweicloud sdk

        :param resource_credential_provider_name: Name of the STS credential provider to retrieve STS credentials from
        :type resource_credential_provider_name: str
        :param workload_access_token: Identity token of the workload requesting the STS token
        :type workload_access_token: str
        :param agency_session_name: An identifier for the assumed agency session
        :type agency_session_name: str
        :param duration_seconds: The duration, in seconds, of the agency session
        :type duration_seconds: int
        :param policy: An IAM policy in JSON format that you want to use as an inline session policy
        :type policy: str
        :param source_identity: The source identity specified by the principal that is calling the operation
        :type source_identity: str
        :param tags: A list of tags
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.StsTag`]
        :param transitive_tag_keys: A list of keys for session tags that you want to set as transitive
        :type transitive_tag_keys: list[str]
        """
        
        

        self._resource_credential_provider_name = None
        self._workload_access_token = None
        self._agency_session_name = None
        self._duration_seconds = None
        self._policy = None
        self._source_identity = None
        self._tags = None
        self._transitive_tag_keys = None
        self.discriminator = None

        self.resource_credential_provider_name = resource_credential_provider_name
        if workload_access_token is not None:
            self.workload_access_token = workload_access_token
        self.agency_session_name = agency_session_name
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds
        if policy is not None:
            self.policy = policy
        if source_identity is not None:
            self.source_identity = source_identity
        if tags is not None:
            self.tags = tags
        if transitive_tag_keys is not None:
            self.transitive_tag_keys = transitive_tag_keys

    @property
    def resource_credential_provider_name(self):
        r"""Gets the resource_credential_provider_name of this GetResourceStsTokenRequestBody.

        Name of the STS credential provider to retrieve STS credentials from

        :return: The resource_credential_provider_name of this GetResourceStsTokenRequestBody.
        :rtype: str
        """
        return self._resource_credential_provider_name

    @resource_credential_provider_name.setter
    def resource_credential_provider_name(self, resource_credential_provider_name):
        r"""Sets the resource_credential_provider_name of this GetResourceStsTokenRequestBody.

        Name of the STS credential provider to retrieve STS credentials from

        :param resource_credential_provider_name: The resource_credential_provider_name of this GetResourceStsTokenRequestBody.
        :type resource_credential_provider_name: str
        """
        self._resource_credential_provider_name = resource_credential_provider_name

    @property
    def workload_access_token(self):
        r"""Gets the workload_access_token of this GetResourceStsTokenRequestBody.

        Identity token of the workload requesting the STS token

        :return: The workload_access_token of this GetResourceStsTokenRequestBody.
        :rtype: str
        """
        return self._workload_access_token

    @workload_access_token.setter
    def workload_access_token(self, workload_access_token):
        r"""Sets the workload_access_token of this GetResourceStsTokenRequestBody.

        Identity token of the workload requesting the STS token

        :param workload_access_token: The workload_access_token of this GetResourceStsTokenRequestBody.
        :type workload_access_token: str
        """
        self._workload_access_token = workload_access_token

    @property
    def agency_session_name(self):
        r"""Gets the agency_session_name of this GetResourceStsTokenRequestBody.

        An identifier for the assumed agency session

        :return: The agency_session_name of this GetResourceStsTokenRequestBody.
        :rtype: str
        """
        return self._agency_session_name

    @agency_session_name.setter
    def agency_session_name(self, agency_session_name):
        r"""Sets the agency_session_name of this GetResourceStsTokenRequestBody.

        An identifier for the assumed agency session

        :param agency_session_name: The agency_session_name of this GetResourceStsTokenRequestBody.
        :type agency_session_name: str
        """
        self._agency_session_name = agency_session_name

    @property
    def duration_seconds(self):
        r"""Gets the duration_seconds of this GetResourceStsTokenRequestBody.

        The duration, in seconds, of the agency session

        :return: The duration_seconds of this GetResourceStsTokenRequestBody.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        r"""Sets the duration_seconds of this GetResourceStsTokenRequestBody.

        The duration, in seconds, of the agency session

        :param duration_seconds: The duration_seconds of this GetResourceStsTokenRequestBody.
        :type duration_seconds: int
        """
        self._duration_seconds = duration_seconds

    @property
    def policy(self):
        r"""Gets the policy of this GetResourceStsTokenRequestBody.

        An IAM policy in JSON format that you want to use as an inline session policy

        :return: The policy of this GetResourceStsTokenRequestBody.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this GetResourceStsTokenRequestBody.

        An IAM policy in JSON format that you want to use as an inline session policy

        :param policy: The policy of this GetResourceStsTokenRequestBody.
        :type policy: str
        """
        self._policy = policy

    @property
    def source_identity(self):
        r"""Gets the source_identity of this GetResourceStsTokenRequestBody.

        The source identity specified by the principal that is calling the operation

        :return: The source_identity of this GetResourceStsTokenRequestBody.
        :rtype: str
        """
        return self._source_identity

    @source_identity.setter
    def source_identity(self, source_identity):
        r"""Sets the source_identity of this GetResourceStsTokenRequestBody.

        The source identity specified by the principal that is calling the operation

        :param source_identity: The source_identity of this GetResourceStsTokenRequestBody.
        :type source_identity: str
        """
        self._source_identity = source_identity

    @property
    def tags(self):
        r"""Gets the tags of this GetResourceStsTokenRequestBody.

        A list of tags

        :return: The tags of this GetResourceStsTokenRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.StsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GetResourceStsTokenRequestBody.

        A list of tags

        :param tags: The tags of this GetResourceStsTokenRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.StsTag`]
        """
        self._tags = tags

    @property
    def transitive_tag_keys(self):
        r"""Gets the transitive_tag_keys of this GetResourceStsTokenRequestBody.

        A list of keys for session tags that you want to set as transitive

        :return: The transitive_tag_keys of this GetResourceStsTokenRequestBody.
        :rtype: list[str]
        """
        return self._transitive_tag_keys

    @transitive_tag_keys.setter
    def transitive_tag_keys(self, transitive_tag_keys):
        r"""Sets the transitive_tag_keys of this GetResourceStsTokenRequestBody.

        A list of keys for session tags that you want to set as transitive

        :param transitive_tag_keys: The transitive_tag_keys of this GetResourceStsTokenRequestBody.
        :type transitive_tag_keys: list[str]
        """
        self._transitive_tag_keys = transitive_tag_keys

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
        if not isinstance(other, GetResourceStsTokenRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
