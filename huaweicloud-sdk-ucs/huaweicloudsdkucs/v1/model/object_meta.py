# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'name': 'str',
        'generate_name': 'str',
        'namespace': 'str',
        'labels': 'dict(str, str)',
        'annotations': 'dict(str, str)',
        'creation_timestamp': 'str',
        'update_timestamp': 'str',
        'resource_version': 'str',
        'generation': 'str',
        'managed_fields': 'list[ManagedFieldsEntry]',
        'owner_references': 'list[OwnerReference]'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'generate_name': 'generateName',
        'namespace': 'namespace',
        'labels': 'labels',
        'annotations': 'annotations',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp',
        'resource_version': 'resourceVersion',
        'generation': 'generation',
        'managed_fields': 'managedFields',
        'owner_references': 'ownerReferences'
    }

    def __init__(self, uid=None, name=None, generate_name=None, namespace=None, labels=None, annotations=None, creation_timestamp=None, update_timestamp=None, resource_version=None, generation=None, managed_fields=None, owner_references=None):
        r"""ObjectMeta

        The model defined in huaweicloud sdk

        :param uid: 资源ID
        :type uid: str
        :param name: 资源名称
        :type name: str
        :param generate_name: 当未提供name时，服务器使用的前缀来生成唯一名称
        :type generate_name: str
        :param namespace: 命名空间
        :type namespace: str
        :param labels: 标签
        :type labels: dict(str, str)
        :param annotations: 注解
        :type annotations: dict(str, str)
        :param creation_timestamp: 创建时间
        :type creation_timestamp: str
        :param update_timestamp: 更新时间
        :type update_timestamp: str
        :param resource_version: 资源内部版本
        :type resource_version: str
        :param generation: 资源期望状态的代数
        :type generation: str
        :param managed_fields: 记录哪些字段由哪些工作流管理
        :type managed_fields: list[:class:`huaweicloudsdkucs.v1.ManagedFieldsEntry`]
        :param owner_references: 用于定义对象间所有权关系，管理对象的依赖关系和垃圾回收机制，支持控制器对资源的管理
        :type owner_references: list[:class:`huaweicloudsdkucs.v1.OwnerReference`]
        """
        
        

        self._uid = None
        self._name = None
        self._generate_name = None
        self._namespace = None
        self._labels = None
        self._annotations = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self._resource_version = None
        self._generation = None
        self._managed_fields = None
        self._owner_references = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if generate_name is not None:
            self.generate_name = generate_name
        if namespace is not None:
            self.namespace = namespace
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if resource_version is not None:
            self.resource_version = resource_version
        if generation is not None:
            self.generation = generation
        if managed_fields is not None:
            self.managed_fields = managed_fields
        if owner_references is not None:
            self.owner_references = owner_references

    @property
    def uid(self):
        r"""Gets the uid of this ObjectMeta.

        资源ID

        :return: The uid of this ObjectMeta.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this ObjectMeta.

        资源ID

        :param uid: The uid of this ObjectMeta.
        :type uid: str
        """
        self._uid = uid

    @property
    def name(self):
        r"""Gets the name of this ObjectMeta.

        资源名称

        :return: The name of this ObjectMeta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ObjectMeta.

        资源名称

        :param name: The name of this ObjectMeta.
        :type name: str
        """
        self._name = name

    @property
    def generate_name(self):
        r"""Gets the generate_name of this ObjectMeta.

        当未提供name时，服务器使用的前缀来生成唯一名称

        :return: The generate_name of this ObjectMeta.
        :rtype: str
        """
        return self._generate_name

    @generate_name.setter
    def generate_name(self, generate_name):
        r"""Sets the generate_name of this ObjectMeta.

        当未提供name时，服务器使用的前缀来生成唯一名称

        :param generate_name: The generate_name of this ObjectMeta.
        :type generate_name: str
        """
        self._generate_name = generate_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ObjectMeta.

        命名空间

        :return: The namespace of this ObjectMeta.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ObjectMeta.

        命名空间

        :param namespace: The namespace of this ObjectMeta.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def labels(self):
        r"""Gets the labels of this ObjectMeta.

        标签

        :return: The labels of this ObjectMeta.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ObjectMeta.

        标签

        :param labels: The labels of this ObjectMeta.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def annotations(self):
        r"""Gets the annotations of this ObjectMeta.

        注解

        :return: The annotations of this ObjectMeta.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this ObjectMeta.

        注解

        :param annotations: The annotations of this ObjectMeta.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this ObjectMeta.

        创建时间

        :return: The creation_timestamp of this ObjectMeta.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this ObjectMeta.

        创建时间

        :param creation_timestamp: The creation_timestamp of this ObjectMeta.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this ObjectMeta.

        更新时间

        :return: The update_timestamp of this ObjectMeta.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this ObjectMeta.

        更新时间

        :param update_timestamp: The update_timestamp of this ObjectMeta.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    @property
    def resource_version(self):
        r"""Gets the resource_version of this ObjectMeta.

        资源内部版本

        :return: The resource_version of this ObjectMeta.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        r"""Sets the resource_version of this ObjectMeta.

        资源内部版本

        :param resource_version: The resource_version of this ObjectMeta.
        :type resource_version: str
        """
        self._resource_version = resource_version

    @property
    def generation(self):
        r"""Gets the generation of this ObjectMeta.

        资源期望状态的代数

        :return: The generation of this ObjectMeta.
        :rtype: str
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        r"""Sets the generation of this ObjectMeta.

        资源期望状态的代数

        :param generation: The generation of this ObjectMeta.
        :type generation: str
        """
        self._generation = generation

    @property
    def managed_fields(self):
        r"""Gets the managed_fields of this ObjectMeta.

        记录哪些字段由哪些工作流管理

        :return: The managed_fields of this ObjectMeta.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ManagedFieldsEntry`]
        """
        return self._managed_fields

    @managed_fields.setter
    def managed_fields(self, managed_fields):
        r"""Sets the managed_fields of this ObjectMeta.

        记录哪些字段由哪些工作流管理

        :param managed_fields: The managed_fields of this ObjectMeta.
        :type managed_fields: list[:class:`huaweicloudsdkucs.v1.ManagedFieldsEntry`]
        """
        self._managed_fields = managed_fields

    @property
    def owner_references(self):
        r"""Gets the owner_references of this ObjectMeta.

        用于定义对象间所有权关系，管理对象的依赖关系和垃圾回收机制，支持控制器对资源的管理

        :return: The owner_references of this ObjectMeta.
        :rtype: list[:class:`huaweicloudsdkucs.v1.OwnerReference`]
        """
        return self._owner_references

    @owner_references.setter
    def owner_references(self, owner_references):
        r"""Sets the owner_references of this ObjectMeta.

        用于定义对象间所有权关系，管理对象的依赖关系和垃圾回收机制，支持控制器对资源的管理

        :param owner_references: The owner_references of this ObjectMeta.
        :type owner_references: list[:class:`huaweicloudsdkucs.v1.OwnerReference`]
        """
        self._owner_references = owner_references

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
        if not isinstance(other, ObjectMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
