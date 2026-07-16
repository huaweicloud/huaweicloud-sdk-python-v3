# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreIngressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'enable_public_network': 'bool',
        'public_domain_name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'enable_public_network': 'enable_public_network',
        'public_domain_name': 'public_domain_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, status=None, enable_public_network=None, public_domain_name=None, created_at=None, updated_at=None):
        r"""UpdateCoreIngressResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**: Ingress ID。
        :type id: str
        :param name: **参数解释**: Ingress名称。
        :type name: str
        :param description: **参数解释**: Ingress描述。
        :type description: str
        :param status: **参数解释**: Ingress状态。
        :type status: str
        :param enable_public_network: **参数解释**: 是否启用公网访问。
        :type enable_public_network: bool
        :param public_domain_name: **参数解释**: 公网域名。
        :type public_domain_name: str
        :param created_at: **参数解释**: 资源创建时间。
        :type created_at: datetime
        :param updated_at: **参数解释**: 资源最后更新时间。
        :type updated_at: datetime
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._enable_public_network = None
        self._public_domain_name = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if enable_public_network is not None:
            self.enable_public_network = enable_public_network
        if public_domain_name is not None:
            self.public_domain_name = public_domain_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this UpdateCoreIngressResponse.

        **参数解释**: Ingress ID。

        :return: The id of this UpdateCoreIngressResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateCoreIngressResponse.

        **参数解释**: Ingress ID。

        :param id: The id of this UpdateCoreIngressResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateCoreIngressResponse.

        **参数解释**: Ingress名称。

        :return: The name of this UpdateCoreIngressResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCoreIngressResponse.

        **参数解释**: Ingress名称。

        :param name: The name of this UpdateCoreIngressResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreIngressResponse.

        **参数解释**: Ingress描述。

        :return: The description of this UpdateCoreIngressResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreIngressResponse.

        **参数解释**: Ingress描述。

        :param description: The description of this UpdateCoreIngressResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this UpdateCoreIngressResponse.

        **参数解释**: Ingress状态。

        :return: The status of this UpdateCoreIngressResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateCoreIngressResponse.

        **参数解释**: Ingress状态。

        :param status: The status of this UpdateCoreIngressResponse.
        :type status: str
        """
        self._status = status

    @property
    def enable_public_network(self):
        r"""Gets the enable_public_network of this UpdateCoreIngressResponse.

        **参数解释**: 是否启用公网访问。

        :return: The enable_public_network of this UpdateCoreIngressResponse.
        :rtype: bool
        """
        return self._enable_public_network

    @enable_public_network.setter
    def enable_public_network(self, enable_public_network):
        r"""Sets the enable_public_network of this UpdateCoreIngressResponse.

        **参数解释**: 是否启用公网访问。

        :param enable_public_network: The enable_public_network of this UpdateCoreIngressResponse.
        :type enable_public_network: bool
        """
        self._enable_public_network = enable_public_network

    @property
    def public_domain_name(self):
        r"""Gets the public_domain_name of this UpdateCoreIngressResponse.

        **参数解释**: 公网域名。

        :return: The public_domain_name of this UpdateCoreIngressResponse.
        :rtype: str
        """
        return self._public_domain_name

    @public_domain_name.setter
    def public_domain_name(self, public_domain_name):
        r"""Sets the public_domain_name of this UpdateCoreIngressResponse.

        **参数解释**: 公网域名。

        :param public_domain_name: The public_domain_name of this UpdateCoreIngressResponse.
        :type public_domain_name: str
        """
        self._public_domain_name = public_domain_name

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateCoreIngressResponse.

        **参数解释**: 资源创建时间。

        :return: The created_at of this UpdateCoreIngressResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateCoreIngressResponse.

        **参数解释**: 资源创建时间。

        :param created_at: The created_at of this UpdateCoreIngressResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateCoreIngressResponse.

        **参数解释**: 资源最后更新时间。

        :return: The updated_at of this UpdateCoreIngressResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateCoreIngressResponse.

        **参数解释**: 资源最后更新时间。

        :param updated_at: The updated_at of this UpdateCoreIngressResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("UpdateCoreIngressResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateCoreIngressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
