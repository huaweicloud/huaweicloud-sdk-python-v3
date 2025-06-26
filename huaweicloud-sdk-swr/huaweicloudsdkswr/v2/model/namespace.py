# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Namespace:

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
        'metadata': 'NamespaceMetadata',
        'namespace_id': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'repo_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata',
        'namespace_id': 'namespace_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'repo_count': 'repo_count'
    }

    def __init__(self, name=None, metadata=None, namespace_id=None, created_at=None, updated_at=None, repo_count=None):
        r"""Namespace

        The model defined in huaweicloud sdk

        :param name: 命名空间名称
        :type name: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
        :param namespace_id: 命名空间ID
        :type namespace_id: int
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param repo_count: 镜像数量
        :type repo_count: int
        """
        
        

        self._name = None
        self._metadata = None
        self._namespace_id = None
        self._created_at = None
        self._updated_at = None
        self._repo_count = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if repo_count is not None:
            self.repo_count = repo_count

    @property
    def name(self):
        r"""Gets the name of this Namespace.

        命名空间名称

        :return: The name of this Namespace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Namespace.

        命名空间名称

        :param name: The name of this Namespace.
        :type name: str
        """
        self._name = name

    @property
    def metadata(self):
        r"""Gets the metadata of this Namespace.

        :return: The metadata of this Namespace.
        :rtype: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this Namespace.

        :param metadata: The metadata of this Namespace.
        :type metadata: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
        """
        self._metadata = metadata

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this Namespace.

        命名空间ID

        :return: The namespace_id of this Namespace.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this Namespace.

        命名空间ID

        :param namespace_id: The namespace_id of this Namespace.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def created_at(self):
        r"""Gets the created_at of this Namespace.

        创建时间

        :return: The created_at of this Namespace.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Namespace.

        创建时间

        :param created_at: The created_at of this Namespace.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Namespace.

        更新时间

        :return: The updated_at of this Namespace.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Namespace.

        更新时间

        :param updated_at: The updated_at of this Namespace.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def repo_count(self):
        r"""Gets the repo_count of this Namespace.

        镜像数量

        :return: The repo_count of this Namespace.
        :rtype: int
        """
        return self._repo_count

    @repo_count.setter
    def repo_count(self, repo_count):
        r"""Sets the repo_count of this Namespace.

        镜像数量

        :param repo_count: The repo_count of this Namespace.
        :type repo_count: int
        """
        self._repo_count = repo_count

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
        if not isinstance(other, Namespace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
