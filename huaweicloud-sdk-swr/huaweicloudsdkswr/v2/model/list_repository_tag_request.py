# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryTagRequest:

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
        'limit': 'int',
        'marker': 'str',
        'tag': 'str',
        'order_column': 'str',
        'order_type': 'str',
        'with_manifest': 'bool'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'limit': 'limit',
        'marker': 'marker',
        'tag': 'tag',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'with_manifest': 'with_manifest'
    }

    def __init__(self, namespace=None, repository=None, limit=None, marker=None, tag=None, order_column=None, order_type=None, with_manifest=None):
        r"""ListRepositoryTagRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param limit: 返回条数,默认返回100条，最多返回1000条数据。
        :type limit: int
        :param marker: Start position of the cursor for querying the next page in pagination query.
        :type marker: str
        :param tag: 镜像版本名。
        :type tag: str
        :param order_column: 按列排序，可设置为updated_at（按更新时间排序）或者tag（按照镜像版本排序）。注意：order_column和order_type参数需要配套使用。
        :type order_column: str
        :param order_type: 排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。
        :type order_type: str
        :param with_manifest: 是否返回镜像的manifest信息
        :type with_manifest: bool
        """
        
        

        self._namespace = None
        self._repository = None
        self._limit = None
        self._marker = None
        self._tag = None
        self._order_column = None
        self._order_type = None
        self._with_manifest = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if tag is not None:
            self.tag = tag
        if order_column is not None:
            self.order_column = order_column
        if order_type is not None:
            self.order_type = order_type
        if with_manifest is not None:
            self.with_manifest = with_manifest

    @property
    def namespace(self):
        r"""Gets the namespace of this ListRepositoryTagRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListRepositoryTagRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListRepositoryTagRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListRepositoryTagRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this ListRepositoryTagRequest.

        镜像仓库名称

        :return: The repository of this ListRepositoryTagRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this ListRepositoryTagRequest.

        镜像仓库名称

        :param repository: The repository of this ListRepositoryTagRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryTagRequest.

        返回条数,默认返回100条，最多返回1000条数据。

        :return: The limit of this ListRepositoryTagRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryTagRequest.

        返回条数,默认返回100条，最多返回1000条数据。

        :param limit: The limit of this ListRepositoryTagRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRepositoryTagRequest.

        Start position of the cursor for querying the next page in pagination query.

        :return: The marker of this ListRepositoryTagRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRepositoryTagRequest.

        Start position of the cursor for querying the next page in pagination query.

        :param marker: The marker of this ListRepositoryTagRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def tag(self):
        r"""Gets the tag of this ListRepositoryTagRequest.

        镜像版本名。

        :return: The tag of this ListRepositoryTagRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListRepositoryTagRequest.

        镜像版本名。

        :param tag: The tag of this ListRepositoryTagRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def order_column(self):
        r"""Gets the order_column of this ListRepositoryTagRequest.

        按列排序，可设置为updated_at（按更新时间排序）或者tag（按照镜像版本排序）。注意：order_column和order_type参数需要配套使用。

        :return: The order_column of this ListRepositoryTagRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        r"""Sets the order_column of this ListRepositoryTagRequest.

        按列排序，可设置为updated_at（按更新时间排序）或者tag（按照镜像版本排序）。注意：order_column和order_type参数需要配套使用。

        :param order_column: The order_column of this ListRepositoryTagRequest.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        r"""Gets the order_type of this ListRepositoryTagRequest.

        排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。

        :return: The order_type of this ListRepositoryTagRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ListRepositoryTagRequest.

        排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。

        :param order_type: The order_type of this ListRepositoryTagRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def with_manifest(self):
        r"""Gets the with_manifest of this ListRepositoryTagRequest.

        是否返回镜像的manifest信息

        :return: The with_manifest of this ListRepositoryTagRequest.
        :rtype: bool
        """
        return self._with_manifest

    @with_manifest.setter
    def with_manifest(self, with_manifest):
        r"""Sets the with_manifest of this ListRepositoryTagRequest.

        是否返回镜像的manifest信息

        :param with_manifest: The with_manifest of this ListRepositoryTagRequest.
        :type with_manifest: bool
        """
        self._with_manifest = with_manifest

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
        if not isinstance(other, ListRepositoryTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
