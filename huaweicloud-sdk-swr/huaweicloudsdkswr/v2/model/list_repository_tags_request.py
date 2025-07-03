# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryTagsRequest:

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
        'limit': 'str',
        'offset': 'str',
        'order_column': 'str',
        'order_type': 'str',
        'tag': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'limit': 'limit',
        'offset': 'offset',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'tag': 'tag',
        'filter': 'filter'
    }

    def __init__(self, namespace=None, repository=None, limit=None, offset=None, order_column=None, order_type=None, tag=None, filter=None):
        r"""ListRepositoryTagsRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param limit: 返回条数,默认返回100条，最多返回1000条数据。注意：offset和limit参数需要配套使用。
        :type limit: str
        :param offset: 起始索引。注意：offset和limit参数需要配套使用。
        :type offset: str
        :param order_column: 按列排序，可设置为updated_at（按更新时间排序）。注意：order_column和order_type参数需要配套使用。
        :type order_column: str
        :param order_type: 排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。
        :type order_type: str
        :param tag: 镜像版本名。
        :type tag: str
        :param filter: 应填写 offset::{offset}|limit::{limit}|order_column::{order_column}|order_type::{order_type}|tag::{tag} ,其中{limit}为返回条数,{offset}为起始索引,注意：offset和limit参数需要配套使用。 {order_column}为按列排序，可设置为updated_at（按更新时间排序）,{order_type}为排序类型，可设置为desc（降序）、asc（升序），{tag}为镜像版本名。
        :type filter: str
        """
        
        

        self._namespace = None
        self._repository = None
        self._limit = None
        self._offset = None
        self._order_column = None
        self._order_type = None
        self._tag = None
        self._filter = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_column is not None:
            self.order_column = order_column
        if order_type is not None:
            self.order_type = order_type
        if tag is not None:
            self.tag = tag
        if filter is not None:
            self.filter = filter

    @property
    def namespace(self):
        r"""Gets the namespace of this ListRepositoryTagsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListRepositoryTagsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListRepositoryTagsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this ListRepositoryTagsRequest.

        镜像仓库名称

        :return: The repository of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this ListRepositoryTagsRequest.

        镜像仓库名称

        :param repository: The repository of this ListRepositoryTagsRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryTagsRequest.

        返回条数,默认返回100条，最多返回1000条数据。注意：offset和limit参数需要配套使用。

        :return: The limit of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryTagsRequest.

        返回条数,默认返回100条，最多返回1000条数据。注意：offset和limit参数需要配套使用。

        :param limit: The limit of this ListRepositoryTagsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryTagsRequest.

        起始索引。注意：offset和limit参数需要配套使用。

        :return: The offset of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryTagsRequest.

        起始索引。注意：offset和limit参数需要配套使用。

        :param offset: The offset of this ListRepositoryTagsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def order_column(self):
        r"""Gets the order_column of this ListRepositoryTagsRequest.

        按列排序，可设置为updated_at（按更新时间排序）。注意：order_column和order_type参数需要配套使用。

        :return: The order_column of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        r"""Sets the order_column of this ListRepositoryTagsRequest.

        按列排序，可设置为updated_at（按更新时间排序）。注意：order_column和order_type参数需要配套使用。

        :param order_column: The order_column of this ListRepositoryTagsRequest.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        r"""Gets the order_type of this ListRepositoryTagsRequest.

        排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。

        :return: The order_type of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ListRepositoryTagsRequest.

        排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。

        :param order_type: The order_type of this ListRepositoryTagsRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def tag(self):
        r"""Gets the tag of this ListRepositoryTagsRequest.

        镜像版本名。

        :return: The tag of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListRepositoryTagsRequest.

        镜像版本名。

        :param tag: The tag of this ListRepositoryTagsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def filter(self):
        r"""Gets the filter of this ListRepositoryTagsRequest.

        应填写 offset::{offset}|limit::{limit}|order_column::{order_column}|order_type::{order_type}|tag::{tag} ,其中{limit}为返回条数,{offset}为起始索引,注意：offset和limit参数需要配套使用。 {order_column}为按列排序，可设置为updated_at（按更新时间排序）,{order_type}为排序类型，可设置为desc（降序）、asc（升序），{tag}为镜像版本名。

        :return: The filter of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListRepositoryTagsRequest.

        应填写 offset::{offset}|limit::{limit}|order_column::{order_column}|order_type::{order_type}|tag::{tag} ,其中{limit}为返回条数,{offset}为起始索引,注意：offset和limit参数需要配套使用。 {order_column}为按列排序，可设置为updated_at（按更新时间排序）,{order_type}为排序类型，可设置为desc（降序）、asc（升序），{tag}为镜像版本名。

        :param filter: The filter of this ListRepositoryTagsRequest.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, ListRepositoryTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
