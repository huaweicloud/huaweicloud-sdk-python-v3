# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceSpecificCredentialMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'datetime',
        'service_name': 'str',
        'credential_id': 'str',
        'status': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'expires_at': 'datetime',
        'credential_mask': 'str',
        'description': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'service_name': 'service_name',
        'credential_id': 'credential_id',
        'status': 'status',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'expires_at': 'expires_at',
        'credential_mask': 'credential_mask',
        'description': 'description'
    }

    def __init__(self, created_at=None, service_name=None, credential_id=None, status=None, user_id=None, user_name=None, expires_at=None, credential_mask=None, description=None):
        r"""ServiceSpecificCredentialMetadata

        The model defined in huaweicloud sdk

        :param created_at: 创建日期和时间，ISO 8601格式。
        :type created_at: datetime
        :param service_name: 关联的服务名称。
        :type service_name: str
        :param credential_id: 凭证标识符ID。
        :type credential_id: str
        :param status: 凭证状态。
        :type status: str
        :param user_id: 与服务专属凭证关联的IAM用户ID。
        :type user_id: str
        :param user_name: 关联的IAM用户名称。
        :type user_name: str
        :param expires_at: 过期日期和时间，仅指定credential_age_days时返回。
        :type expires_at: datetime
        :param credential_mask: 凭证的掩码值。
        :type credential_mask: str
        :param description: 凭证描述。
        :type description: str
        """
        
        

        self._created_at = None
        self._service_name = None
        self._credential_id = None
        self._status = None
        self._user_id = None
        self._user_name = None
        self._expires_at = None
        self._credential_mask = None
        self._description = None
        self.discriminator = None

        self.created_at = created_at
        self.service_name = service_name
        self.credential_id = credential_id
        self.status = status
        self.user_id = user_id
        self.user_name = user_name
        if expires_at is not None:
            self.expires_at = expires_at
        self.credential_mask = credential_mask
        self.description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ServiceSpecificCredentialMetadata.

        创建日期和时间，ISO 8601格式。

        :return: The created_at of this ServiceSpecificCredentialMetadata.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ServiceSpecificCredentialMetadata.

        创建日期和时间，ISO 8601格式。

        :param created_at: The created_at of this ServiceSpecificCredentialMetadata.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def service_name(self):
        r"""Gets the service_name of this ServiceSpecificCredentialMetadata.

        关联的服务名称。

        :return: The service_name of this ServiceSpecificCredentialMetadata.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ServiceSpecificCredentialMetadata.

        关联的服务名称。

        :param service_name: The service_name of this ServiceSpecificCredentialMetadata.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def credential_id(self):
        r"""Gets the credential_id of this ServiceSpecificCredentialMetadata.

        凭证标识符ID。

        :return: The credential_id of this ServiceSpecificCredentialMetadata.
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        r"""Sets the credential_id of this ServiceSpecificCredentialMetadata.

        凭证标识符ID。

        :param credential_id: The credential_id of this ServiceSpecificCredentialMetadata.
        :type credential_id: str
        """
        self._credential_id = credential_id

    @property
    def status(self):
        r"""Gets the status of this ServiceSpecificCredentialMetadata.

        凭证状态。

        :return: The status of this ServiceSpecificCredentialMetadata.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServiceSpecificCredentialMetadata.

        凭证状态。

        :param status: The status of this ServiceSpecificCredentialMetadata.
        :type status: str
        """
        self._status = status

    @property
    def user_id(self):
        r"""Gets the user_id of this ServiceSpecificCredentialMetadata.

        与服务专属凭证关联的IAM用户ID。

        :return: The user_id of this ServiceSpecificCredentialMetadata.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ServiceSpecificCredentialMetadata.

        与服务专属凭证关联的IAM用户ID。

        :param user_id: The user_id of this ServiceSpecificCredentialMetadata.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ServiceSpecificCredentialMetadata.

        关联的IAM用户名称。

        :return: The user_name of this ServiceSpecificCredentialMetadata.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ServiceSpecificCredentialMetadata.

        关联的IAM用户名称。

        :param user_name: The user_name of this ServiceSpecificCredentialMetadata.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def expires_at(self):
        r"""Gets the expires_at of this ServiceSpecificCredentialMetadata.

        过期日期和时间，仅指定credential_age_days时返回。

        :return: The expires_at of this ServiceSpecificCredentialMetadata.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this ServiceSpecificCredentialMetadata.

        过期日期和时间，仅指定credential_age_days时返回。

        :param expires_at: The expires_at of this ServiceSpecificCredentialMetadata.
        :type expires_at: datetime
        """
        self._expires_at = expires_at

    @property
    def credential_mask(self):
        r"""Gets the credential_mask of this ServiceSpecificCredentialMetadata.

        凭证的掩码值。

        :return: The credential_mask of this ServiceSpecificCredentialMetadata.
        :rtype: str
        """
        return self._credential_mask

    @credential_mask.setter
    def credential_mask(self, credential_mask):
        r"""Sets the credential_mask of this ServiceSpecificCredentialMetadata.

        凭证的掩码值。

        :param credential_mask: The credential_mask of this ServiceSpecificCredentialMetadata.
        :type credential_mask: str
        """
        self._credential_mask = credential_mask

    @property
    def description(self):
        r"""Gets the description of this ServiceSpecificCredentialMetadata.

        凭证描述。

        :return: The description of this ServiceSpecificCredentialMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceSpecificCredentialMetadata.

        凭证描述。

        :param description: The description of this ServiceSpecificCredentialMetadata.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ServiceSpecificCredentialMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
