# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicRepositoryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'namespace': 'str',
        'path': 'str',
        'develop_mode': 'str',
        'visibility': 'str',
        'security': 'str',
        'name_with_namespace': 'str',
        'archived': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'namespace': 'namespace',
        'path': 'path',
        'develop_mode': 'develop_mode',
        'visibility': 'visibility',
        'security': 'security',
        'name_with_namespace': 'name_with_namespace',
        'archived': 'archived',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, namespace=None, path=None, develop_mode=None, visibility=None, security=None, name_with_namespace=None, archived=None, status=None):
        r"""BasicRepositoryDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库ID **约束限制：** 不涉及。
        :type id: int
        :param name: **参数解释：** 仓库名称。 **约束限制：** 不涉及。
        :type name: str
        :param namespace: **参数解释：** 命名空间。 **约束限制：** 不涉及。
        :type namespace: str
        :param path: **参数解释：** 仓库路径。 **约束限制：** 不涉及。
        :type path: str
        :param develop_mode: **参数解释：** 开发模式。 枚举值：normal：合并请求模式；CR：变更请求模式。 **约束限制：** 不涉及。
        :type develop_mode: str
        :param visibility: **参数解释：** 仓库可见性。 枚举值：private：私有；internal：内部公开；public：公开。 **约束限制：** 不涉及。
        :type visibility: str
        :param security: **参数解释：** 安全级别。 枚举值：product_internal：项目内公开；tenant_internal：租户内公开。 **约束限制：** 不涉及。
        :type security: str
        :param name_with_namespace: **参数解释：** 包含命名空间的仓库名称。 **约束限制：** 不涉及。
        :type name_with_namespace: str
        :param archived: **参数解释：** 是否归档。true：已归档；false：未归档。 **约束限制：** 不涉及。
        :type archived: bool
        :param status: **参数解释：** 仓库状态。 **约束限制：** 不涉及。
        :type status: str
        """
        
        

        self._id = None
        self._name = None
        self._namespace = None
        self._path = None
        self._develop_mode = None
        self._visibility = None
        self._security = None
        self._name_with_namespace = None
        self._archived = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if path is not None:
            self.path = path
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if visibility is not None:
            self.visibility = visibility
        if security is not None:
            self.security = security
        if name_with_namespace is not None:
            self.name_with_namespace = name_with_namespace
        if archived is not None:
            self.archived = archived
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this BasicRepositoryDto.

        **参数解释：** 仓库ID **约束限制：** 不涉及。

        :return: The id of this BasicRepositoryDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BasicRepositoryDto.

        **参数解释：** 仓库ID **约束限制：** 不涉及。

        :param id: The id of this BasicRepositoryDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BasicRepositoryDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :return: The name of this BasicRepositoryDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BasicRepositoryDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :param name: The name of this BasicRepositoryDto.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this BasicRepositoryDto.

        **参数解释：** 命名空间。 **约束限制：** 不涉及。

        :return: The namespace of this BasicRepositoryDto.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this BasicRepositoryDto.

        **参数解释：** 命名空间。 **约束限制：** 不涉及。

        :param namespace: The namespace of this BasicRepositoryDto.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def path(self):
        r"""Gets the path of this BasicRepositoryDto.

        **参数解释：** 仓库路径。 **约束限制：** 不涉及。

        :return: The path of this BasicRepositoryDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this BasicRepositoryDto.

        **参数解释：** 仓库路径。 **约束限制：** 不涉及。

        :param path: The path of this BasicRepositoryDto.
        :type path: str
        """
        self._path = path

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this BasicRepositoryDto.

        **参数解释：** 开发模式。 枚举值：normal：合并请求模式；CR：变更请求模式。 **约束限制：** 不涉及。

        :return: The develop_mode of this BasicRepositoryDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this BasicRepositoryDto.

        **参数解释：** 开发模式。 枚举值：normal：合并请求模式；CR：变更请求模式。 **约束限制：** 不涉及。

        :param develop_mode: The develop_mode of this BasicRepositoryDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def visibility(self):
        r"""Gets the visibility of this BasicRepositoryDto.

        **参数解释：** 仓库可见性。 枚举值：private：私有；internal：内部公开；public：公开。 **约束限制：** 不涉及。

        :return: The visibility of this BasicRepositoryDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this BasicRepositoryDto.

        **参数解释：** 仓库可见性。 枚举值：private：私有；internal：内部公开；public：公开。 **约束限制：** 不涉及。

        :param visibility: The visibility of this BasicRepositoryDto.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def security(self):
        r"""Gets the security of this BasicRepositoryDto.

        **参数解释：** 安全级别。 枚举值：product_internal：项目内公开；tenant_internal：租户内公开。 **约束限制：** 不涉及。

        :return: The security of this BasicRepositoryDto.
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        r"""Sets the security of this BasicRepositoryDto.

        **参数解释：** 安全级别。 枚举值：product_internal：项目内公开；tenant_internal：租户内公开。 **约束限制：** 不涉及。

        :param security: The security of this BasicRepositoryDto.
        :type security: str
        """
        self._security = security

    @property
    def name_with_namespace(self):
        r"""Gets the name_with_namespace of this BasicRepositoryDto.

        **参数解释：** 包含命名空间的仓库名称。 **约束限制：** 不涉及。

        :return: The name_with_namespace of this BasicRepositoryDto.
        :rtype: str
        """
        return self._name_with_namespace

    @name_with_namespace.setter
    def name_with_namespace(self, name_with_namespace):
        r"""Sets the name_with_namespace of this BasicRepositoryDto.

        **参数解释：** 包含命名空间的仓库名称。 **约束限制：** 不涉及。

        :param name_with_namespace: The name_with_namespace of this BasicRepositoryDto.
        :type name_with_namespace: str
        """
        self._name_with_namespace = name_with_namespace

    @property
    def archived(self):
        r"""Gets the archived of this BasicRepositoryDto.

        **参数解释：** 是否归档。true：已归档；false：未归档。 **约束限制：** 不涉及。

        :return: The archived of this BasicRepositoryDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this BasicRepositoryDto.

        **参数解释：** 是否归档。true：已归档；false：未归档。 **约束限制：** 不涉及。

        :param archived: The archived of this BasicRepositoryDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def status(self):
        r"""Gets the status of this BasicRepositoryDto.

        **参数解释：** 仓库状态。 **约束限制：** 不涉及。

        :return: The status of this BasicRepositoryDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BasicRepositoryDto.

        **参数解释：** 仓库状态。 **约束限制：** 不涉及。

        :param status: The status of this BasicRepositoryDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, BasicRepositoryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
