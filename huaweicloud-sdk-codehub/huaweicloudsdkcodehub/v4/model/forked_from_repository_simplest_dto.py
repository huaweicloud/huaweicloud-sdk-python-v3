# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForkedFromRepositorySimplestDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_with_namespace': 'str',
        'path_with_namespace': 'str',
        'name': 'str',
        'namespace': 'str',
        'id': 'int',
        'project_id': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'name_with_namespace': 'name_with_namespace',
        'path_with_namespace': 'path_with_namespace',
        'name': 'name',
        'namespace': 'namespace',
        'id': 'id',
        'project_id': 'project_id',
        'project_name': 'project_name'
    }

    def __init__(self, name_with_namespace=None, path_with_namespace=None, name=None, namespace=None, id=None, project_id=None, project_name=None):
        r"""ForkedFromRepositorySimplestDto

        The model defined in huaweicloud sdk

        :param name_with_namespace: **参数解释：** 带命名空间的仓库名称。 **约束限制：** 不涉及。
        :type name_with_namespace: str
        :param path_with_namespace: **参数解释：** 带命名空间的仓库路径。 **约束限制：** 不涉及。
        :type path_with_namespace: str
        :param name: **参数解释：** 仓库名称。 **约束限制：** 不涉及。
        :type name: str
        :param namespace: **参数解释：** 命名空间。 **约束限制：** 不涉及。
        :type namespace: str
        :param id: **参数解释：** 仓库ID **约束限制：** 不涉及。
        :type id: int
        :param project_id: **参数解释：** 产品ID。 **约束限制：** 不涉及。
        :type project_id: str
        :param project_name: **参数解释：** 产品名称。 **约束限制：** 不涉及。
        :type project_name: str
        """
        
        

        self._name_with_namespace = None
        self._path_with_namespace = None
        self._name = None
        self._namespace = None
        self._id = None
        self._project_id = None
        self._project_name = None
        self.discriminator = None

        if name_with_namespace is not None:
            self.name_with_namespace = name_with_namespace
        if path_with_namespace is not None:
            self.path_with_namespace = path_with_namespace
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name

    @property
    def name_with_namespace(self):
        r"""Gets the name_with_namespace of this ForkedFromRepositorySimplestDto.

        **参数解释：** 带命名空间的仓库名称。 **约束限制：** 不涉及。

        :return: The name_with_namespace of this ForkedFromRepositorySimplestDto.
        :rtype: str
        """
        return self._name_with_namespace

    @name_with_namespace.setter
    def name_with_namespace(self, name_with_namespace):
        r"""Sets the name_with_namespace of this ForkedFromRepositorySimplestDto.

        **参数解释：** 带命名空间的仓库名称。 **约束限制：** 不涉及。

        :param name_with_namespace: The name_with_namespace of this ForkedFromRepositorySimplestDto.
        :type name_with_namespace: str
        """
        self._name_with_namespace = name_with_namespace

    @property
    def path_with_namespace(self):
        r"""Gets the path_with_namespace of this ForkedFromRepositorySimplestDto.

        **参数解释：** 带命名空间的仓库路径。 **约束限制：** 不涉及。

        :return: The path_with_namespace of this ForkedFromRepositorySimplestDto.
        :rtype: str
        """
        return self._path_with_namespace

    @path_with_namespace.setter
    def path_with_namespace(self, path_with_namespace):
        r"""Sets the path_with_namespace of this ForkedFromRepositorySimplestDto.

        **参数解释：** 带命名空间的仓库路径。 **约束限制：** 不涉及。

        :param path_with_namespace: The path_with_namespace of this ForkedFromRepositorySimplestDto.
        :type path_with_namespace: str
        """
        self._path_with_namespace = path_with_namespace

    @property
    def name(self):
        r"""Gets the name of this ForkedFromRepositorySimplestDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :return: The name of this ForkedFromRepositorySimplestDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ForkedFromRepositorySimplestDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :param name: The name of this ForkedFromRepositorySimplestDto.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this ForkedFromRepositorySimplestDto.

        **参数解释：** 命名空间。 **约束限制：** 不涉及。

        :return: The namespace of this ForkedFromRepositorySimplestDto.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ForkedFromRepositorySimplestDto.

        **参数解释：** 命名空间。 **约束限制：** 不涉及。

        :param namespace: The namespace of this ForkedFromRepositorySimplestDto.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def id(self):
        r"""Gets the id of this ForkedFromRepositorySimplestDto.

        **参数解释：** 仓库ID **约束限制：** 不涉及。

        :return: The id of this ForkedFromRepositorySimplestDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ForkedFromRepositorySimplestDto.

        **参数解释：** 仓库ID **约束限制：** 不涉及。

        :param id: The id of this ForkedFromRepositorySimplestDto.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ForkedFromRepositorySimplestDto.

        **参数解释：** 产品ID。 **约束限制：** 不涉及。

        :return: The project_id of this ForkedFromRepositorySimplestDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ForkedFromRepositorySimplestDto.

        **参数解释：** 产品ID。 **约束限制：** 不涉及。

        :param project_id: The project_id of this ForkedFromRepositorySimplestDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ForkedFromRepositorySimplestDto.

        **参数解释：** 产品名称。 **约束限制：** 不涉及。

        :return: The project_name of this ForkedFromRepositorySimplestDto.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ForkedFromRepositorySimplestDto.

        **参数解释：** 产品名称。 **约束限制：** 不涉及。

        :param project_name: The project_name of this ForkedFromRepositorySimplestDto.
        :type project_name: str
        """
        self._project_name = project_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ForkedFromRepositorySimplestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
