# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepoAccessoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'tag': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'tag': 'tag',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, namespace=None, repository=None, tag=None, limit=None, offset=None):
        r"""ListRepoAccessoriesRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param tag: 镜像版本
        :type tag: str
        :param limit: 返回条数。如果不传该参数默认返回10条记录，最大支持100条记录
        :type limit: int
        :param offset: 起始索引,默认值为0
        :type offset: int
        """
        
        

        self._namespace = None
        self._repository = None
        self._tag = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.tag = tag
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def namespace(self):
        r"""Gets the namespace of this ListRepoAccessoriesRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListRepoAccessoriesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListRepoAccessoriesRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListRepoAccessoriesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this ListRepoAccessoriesRequest.

        镜像仓库名称

        :return: The repository of this ListRepoAccessoriesRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this ListRepoAccessoriesRequest.

        镜像仓库名称

        :param repository: The repository of this ListRepoAccessoriesRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def tag(self):
        r"""Gets the tag of this ListRepoAccessoriesRequest.

        镜像版本

        :return: The tag of this ListRepoAccessoriesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListRepoAccessoriesRequest.

        镜像版本

        :param tag: The tag of this ListRepoAccessoriesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def limit(self):
        r"""Gets the limit of this ListRepoAccessoriesRequest.

        返回条数。如果不传该参数默认返回10条记录，最大支持100条记录

        :return: The limit of this ListRepoAccessoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepoAccessoriesRequest.

        返回条数。如果不传该参数默认返回10条记录，最大支持100条记录

        :param limit: The limit of this ListRepoAccessoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRepoAccessoriesRequest.

        起始索引,默认值为0

        :return: The offset of this ListRepoAccessoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepoAccessoriesRequest.

        起始索引,默认值为0

        :param offset: The offset of this ListRepoAccessoriesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListRepoAccessoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
