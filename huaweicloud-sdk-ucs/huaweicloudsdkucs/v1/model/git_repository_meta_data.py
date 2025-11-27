# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GitRepositoryMetaData:

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
        'namespace': 'str',
        'uid': 'str',
        'resource_version': 'str',
        'generation': 'int',
        'creation_timestamp': 'str',
        'finalizers': 'list[str]',
        'managed_fields': 'list[ManagedFieldsEntry]'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'uid': 'uid',
        'resource_version': 'resourceVersion',
        'generation': 'generation',
        'creation_timestamp': 'creationTimestamp',
        'finalizers': 'finalizers',
        'managed_fields': 'managedFields'
    }

    def __init__(self, name=None, namespace=None, uid=None, resource_version=None, generation=None, creation_timestamp=None, finalizers=None, managed_fields=None):
        r"""GitRepositoryMetaData

        The model defined in huaweicloud sdk

        :param name: 仓库名称
        :type name: str
        :param namespace: 所属命名空间
        :type namespace: str
        :param uid: 唯一标识符
        :type uid: str
        :param resource_version: 资源的内部版本标识，用于并发控制
        :type resource_version: str
        :param generation: 资源的期望状态的代数，每次修改spec会自增
        :type generation: int
        :param creation_timestamp: 创建时间
        :type creation_timestamp: str
        :param finalizers: 删除前需要执行的清理操作
        :type finalizers: list[str]
        :param managed_fields: 用于跟踪资源字段管理权，记录每个字段的管理者
        :type managed_fields: list[:class:`huaweicloudsdkucs.v1.ManagedFieldsEntry`]
        """
        
        

        self._name = None
        self._namespace = None
        self._uid = None
        self._resource_version = None
        self._generation = None
        self._creation_timestamp = None
        self._finalizers = None
        self._managed_fields = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if uid is not None:
            self.uid = uid
        if resource_version is not None:
            self.resource_version = resource_version
        if generation is not None:
            self.generation = generation
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if finalizers is not None:
            self.finalizers = finalizers
        if managed_fields is not None:
            self.managed_fields = managed_fields

    @property
    def name(self):
        r"""Gets the name of this GitRepositoryMetaData.

        仓库名称

        :return: The name of this GitRepositoryMetaData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GitRepositoryMetaData.

        仓库名称

        :param name: The name of this GitRepositoryMetaData.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this GitRepositoryMetaData.

        所属命名空间

        :return: The namespace of this GitRepositoryMetaData.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this GitRepositoryMetaData.

        所属命名空间

        :param namespace: The namespace of this GitRepositoryMetaData.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def uid(self):
        r"""Gets the uid of this GitRepositoryMetaData.

        唯一标识符

        :return: The uid of this GitRepositoryMetaData.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this GitRepositoryMetaData.

        唯一标识符

        :param uid: The uid of this GitRepositoryMetaData.
        :type uid: str
        """
        self._uid = uid

    @property
    def resource_version(self):
        r"""Gets the resource_version of this GitRepositoryMetaData.

        资源的内部版本标识，用于并发控制

        :return: The resource_version of this GitRepositoryMetaData.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        r"""Sets the resource_version of this GitRepositoryMetaData.

        资源的内部版本标识，用于并发控制

        :param resource_version: The resource_version of this GitRepositoryMetaData.
        :type resource_version: str
        """
        self._resource_version = resource_version

    @property
    def generation(self):
        r"""Gets the generation of this GitRepositoryMetaData.

        资源的期望状态的代数，每次修改spec会自增

        :return: The generation of this GitRepositoryMetaData.
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        r"""Sets the generation of this GitRepositoryMetaData.

        资源的期望状态的代数，每次修改spec会自增

        :param generation: The generation of this GitRepositoryMetaData.
        :type generation: int
        """
        self._generation = generation

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this GitRepositoryMetaData.

        创建时间

        :return: The creation_timestamp of this GitRepositoryMetaData.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this GitRepositoryMetaData.

        创建时间

        :param creation_timestamp: The creation_timestamp of this GitRepositoryMetaData.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def finalizers(self):
        r"""Gets the finalizers of this GitRepositoryMetaData.

        删除前需要执行的清理操作

        :return: The finalizers of this GitRepositoryMetaData.
        :rtype: list[str]
        """
        return self._finalizers

    @finalizers.setter
    def finalizers(self, finalizers):
        r"""Sets the finalizers of this GitRepositoryMetaData.

        删除前需要执行的清理操作

        :param finalizers: The finalizers of this GitRepositoryMetaData.
        :type finalizers: list[str]
        """
        self._finalizers = finalizers

    @property
    def managed_fields(self):
        r"""Gets the managed_fields of this GitRepositoryMetaData.

        用于跟踪资源字段管理权，记录每个字段的管理者

        :return: The managed_fields of this GitRepositoryMetaData.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ManagedFieldsEntry`]
        """
        return self._managed_fields

    @managed_fields.setter
    def managed_fields(self, managed_fields):
        r"""Sets the managed_fields of this GitRepositoryMetaData.

        用于跟踪资源字段管理权，记录每个字段的管理者

        :param managed_fields: The managed_fields of this GitRepositoryMetaData.
        :type managed_fields: list[:class:`huaweicloudsdkucs.v1.ManagedFieldsEntry`]
        """
        self._managed_fields = managed_fields

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
        if not isinstance(other, GitRepositoryMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
