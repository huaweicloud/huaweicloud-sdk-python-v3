# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadIdentitySummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'urn': 'str',
        'authorizer_type': 'AuthorizerType',
        'created_by': 'CreatedBy',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'urn': 'urn',
        'authorizer_type': 'authorizer_type',
        'created_by': 'created_by',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags'
    }

    def __init__(self, name=None, urn=None, authorizer_type=None, created_by=None, created_at=None, updated_at=None, tags=None):
        r"""WorkloadIdentitySummary

        The model defined in huaweicloud sdk

        :param name: The name of the workload identity.
        :type name: str
        :param urn: The URN of the workload identity.
        :type urn: str
        :param authorizer_type: 
        :type authorizer_type: :class:`huaweicloudsdkagentidentity.v1.AuthorizerType`
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkagentidentity.v1.CreatedBy`
        :param created_at: Timestamp in RFC 3339 format (UTC)
        :type created_at: datetime
        :param updated_at: Timestamp in RFC 3339 format (UTC)
        :type updated_at: datetime
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._name = None
        self._urn = None
        self._authorizer_type = None
        self._created_by = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.urn = urn
        self.authorizer_type = authorizer_type
        self.created_by = created_by
        self.created_at = created_at
        self.updated_at = updated_at
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this WorkloadIdentitySummary.

        The name of the workload identity.

        :return: The name of this WorkloadIdentitySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkloadIdentitySummary.

        The name of the workload identity.

        :param name: The name of this WorkloadIdentitySummary.
        :type name: str
        """
        self._name = name

    @property
    def urn(self):
        r"""Gets the urn of this WorkloadIdentitySummary.

        The URN of the workload identity.

        :return: The urn of this WorkloadIdentitySummary.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this WorkloadIdentitySummary.

        The URN of the workload identity.

        :param urn: The urn of this WorkloadIdentitySummary.
        :type urn: str
        """
        self._urn = urn

    @property
    def authorizer_type(self):
        r"""Gets the authorizer_type of this WorkloadIdentitySummary.

        :return: The authorizer_type of this WorkloadIdentitySummary.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.AuthorizerType`
        """
        return self._authorizer_type

    @authorizer_type.setter
    def authorizer_type(self, authorizer_type):
        r"""Sets the authorizer_type of this WorkloadIdentitySummary.

        :param authorizer_type: The authorizer_type of this WorkloadIdentitySummary.
        :type authorizer_type: :class:`huaweicloudsdkagentidentity.v1.AuthorizerType`
        """
        self._authorizer_type = authorizer_type

    @property
    def created_by(self):
        r"""Gets the created_by of this WorkloadIdentitySummary.

        :return: The created_by of this WorkloadIdentitySummary.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreatedBy`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this WorkloadIdentitySummary.

        :param created_by: The created_by of this WorkloadIdentitySummary.
        :type created_by: :class:`huaweicloudsdkagentidentity.v1.CreatedBy`
        """
        self._created_by = created_by

    @property
    def created_at(self):
        r"""Gets the created_at of this WorkloadIdentitySummary.

        Timestamp in RFC 3339 format (UTC)

        :return: The created_at of this WorkloadIdentitySummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this WorkloadIdentitySummary.

        Timestamp in RFC 3339 format (UTC)

        :param created_at: The created_at of this WorkloadIdentitySummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this WorkloadIdentitySummary.

        Timestamp in RFC 3339 format (UTC)

        :return: The updated_at of this WorkloadIdentitySummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this WorkloadIdentitySummary.

        Timestamp in RFC 3339 format (UTC)

        :param updated_at: The updated_at of this WorkloadIdentitySummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this WorkloadIdentitySummary.

        自定义标签列表。

        :return: The tags of this WorkloadIdentitySummary.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this WorkloadIdentitySummary.

        自定义标签列表。

        :param tags: The tags of this WorkloadIdentitySummary.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, WorkloadIdentitySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
