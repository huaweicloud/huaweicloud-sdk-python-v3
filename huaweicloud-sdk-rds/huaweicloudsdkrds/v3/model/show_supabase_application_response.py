# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSupabaseApplicationResponse(SdkResponse):

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
        'status': 'str',
        'enable_ssl': 'bool',
        'cert_id': 'str',
        'security_group_id': 'str',
        'storage_component': 'SupabaseStorageComponentInfo',
        'managed_instance': 'SupabaseManagedInstanceInfo',
        'updated_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'enable_ssl': 'enable_ssl',
        'cert_id': 'cert_id',
        'security_group_id': 'security_group_id',
        'storage_component': 'storage_component',
        'managed_instance': 'managed_instance',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, name=None, status=None, enable_ssl=None, cert_id=None, security_group_id=None, storage_component=None, managed_instance=None, updated_time=None):
        r"""ShowSupabaseApplicationResponse

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param status: 运行状态。
        :type status: str
        :param enable_ssl: 
        :type enable_ssl: bool
        :param cert_id: 
        :type cert_id: str
        :param security_group_id: 
        :type security_group_id: str
        :param storage_component: 
        :type storage_component: :class:`huaweicloudsdkrds.v3.SupabaseStorageComponentInfo`
        :param managed_instance: 
        :type managed_instance: :class:`huaweicloudsdkrds.v3.SupabaseManagedInstanceInfo`
        :param updated_time: 
        :type updated_time: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._status = None
        self._enable_ssl = None
        self._cert_id = None
        self._security_group_id = None
        self._storage_component = None
        self._managed_instance = None
        self._updated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if cert_id is not None:
            self.cert_id = cert_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if storage_component is not None:
            self.storage_component = storage_component
        if managed_instance is not None:
            self.managed_instance = managed_instance
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        r"""Gets the id of this ShowSupabaseApplicationResponse.

        :return: The id of this ShowSupabaseApplicationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSupabaseApplicationResponse.

        :param id: The id of this ShowSupabaseApplicationResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowSupabaseApplicationResponse.

        :return: The name of this ShowSupabaseApplicationResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowSupabaseApplicationResponse.

        :param name: The name of this ShowSupabaseApplicationResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ShowSupabaseApplicationResponse.

        运行状态。

        :return: The status of this ShowSupabaseApplicationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSupabaseApplicationResponse.

        运行状态。

        :param status: The status of this ShowSupabaseApplicationResponse.
        :type status: str
        """
        self._status = status

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this ShowSupabaseApplicationResponse.

        :return: The enable_ssl of this ShowSupabaseApplicationResponse.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this ShowSupabaseApplicationResponse.

        :param enable_ssl: The enable_ssl of this ShowSupabaseApplicationResponse.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def cert_id(self):
        r"""Gets the cert_id of this ShowSupabaseApplicationResponse.

        :return: The cert_id of this ShowSupabaseApplicationResponse.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this ShowSupabaseApplicationResponse.

        :param cert_id: The cert_id of this ShowSupabaseApplicationResponse.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ShowSupabaseApplicationResponse.

        :return: The security_group_id of this ShowSupabaseApplicationResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ShowSupabaseApplicationResponse.

        :param security_group_id: The security_group_id of this ShowSupabaseApplicationResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def storage_component(self):
        r"""Gets the storage_component of this ShowSupabaseApplicationResponse.

        :return: The storage_component of this ShowSupabaseApplicationResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseStorageComponentInfo`
        """
        return self._storage_component

    @storage_component.setter
    def storage_component(self, storage_component):
        r"""Sets the storage_component of this ShowSupabaseApplicationResponse.

        :param storage_component: The storage_component of this ShowSupabaseApplicationResponse.
        :type storage_component: :class:`huaweicloudsdkrds.v3.SupabaseStorageComponentInfo`
        """
        self._storage_component = storage_component

    @property
    def managed_instance(self):
        r"""Gets the managed_instance of this ShowSupabaseApplicationResponse.

        :return: The managed_instance of this ShowSupabaseApplicationResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseManagedInstanceInfo`
        """
        return self._managed_instance

    @managed_instance.setter
    def managed_instance(self, managed_instance):
        r"""Sets the managed_instance of this ShowSupabaseApplicationResponse.

        :param managed_instance: The managed_instance of this ShowSupabaseApplicationResponse.
        :type managed_instance: :class:`huaweicloudsdkrds.v3.SupabaseManagedInstanceInfo`
        """
        self._managed_instance = managed_instance

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ShowSupabaseApplicationResponse.

        :return: The updated_time of this ShowSupabaseApplicationResponse.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ShowSupabaseApplicationResponse.

        :param updated_time: The updated_time of this ShowSupabaseApplicationResponse.
        :type updated_time: int
        """
        self._updated_time = updated_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowSupabaseApplicationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSupabaseApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
