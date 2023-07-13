# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharedReposDetailsRequest:

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
        'name': 'str',
        'center': 'str',
        'limit': 'str',
        'offset': 'str',
        'order_column': 'str',
        'order_type': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'name': 'name',
        'center': 'center',
        'limit': 'limit',
        'offset': 'offset',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'filter': 'filter'
    }

    def __init__(self, namespace=None, name=None, center=None, limit=None, offset=None, order_column=None, order_type=None, filter=None):
        """ListSharedReposDetailsRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param name: 镜像仓库名称
        :type name: str
        :param center: self: 我共享的镜像。thirdparty: 他人共享给我的镜像
        :type center: str
        :param limit: 返回条数。注意：offset和limit参数需要配套使用。
        :type limit: str
        :param offset: 起始索引。注意：offset和limit参数需要配套使用。
        :type offset: str
        :param order_column: 按列排序，可设置为updated_at（按更新时间排序）。注意：order_column和order_type参数需要配套使用。
        :type order_column: str
        :param order_type: 排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。
        :type order_type: str
        :param filter: 应填写 center::{center}|name::{name}|limit::{limit}|offset::{offset}|namespace::{namespace}|order_column::{order_column}|order_type::{order_type} ,其中 {center}可选为self: 我共享的镜像。thirdparty: 他人共享给我的镜像，namespace为组织名称，name为镜像仓库名称， {limit}为返回条数,{offset}为起始索引,{order_column}为按列排序，可设置为name、updated_time、tag_count,{order_type}为排序类型，可设置为desc（降序）、asc（升序）
        :type filter: str
        """
        
        

        self._namespace = None
        self._name = None
        self._center = None
        self._limit = None
        self._offset = None
        self._order_column = None
        self._order_type = None
        self._filter = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        if center is not None:
            self.center = center
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_column is not None:
            self.order_column = order_column
        if order_type is not None:
            self.order_type = order_type
        if filter is not None:
            self.filter = filter

    @property
    def namespace(self):
        """Gets the namespace of this ListSharedReposDetailsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListSharedReposDetailsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListSharedReposDetailsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def name(self):
        """Gets the name of this ListSharedReposDetailsRequest.

        镜像仓库名称

        :return: The name of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSharedReposDetailsRequest.

        镜像仓库名称

        :param name: The name of this ListSharedReposDetailsRequest.
        :type name: str
        """
        self._name = name

    @property
    def center(self):
        """Gets the center of this ListSharedReposDetailsRequest.

        self: 我共享的镜像。thirdparty: 他人共享给我的镜像

        :return: The center of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this ListSharedReposDetailsRequest.

        self: 我共享的镜像。thirdparty: 他人共享给我的镜像

        :param center: The center of this ListSharedReposDetailsRequest.
        :type center: str
        """
        self._center = center

    @property
    def limit(self):
        """Gets the limit of this ListSharedReposDetailsRequest.

        返回条数。注意：offset和limit参数需要配套使用。

        :return: The limit of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSharedReposDetailsRequest.

        返回条数。注意：offset和limit参数需要配套使用。

        :param limit: The limit of this ListSharedReposDetailsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSharedReposDetailsRequest.

        起始索引。注意：offset和limit参数需要配套使用。

        :return: The offset of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSharedReposDetailsRequest.

        起始索引。注意：offset和limit参数需要配套使用。

        :param offset: The offset of this ListSharedReposDetailsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def order_column(self):
        """Gets the order_column of this ListSharedReposDetailsRequest.

        按列排序，可设置为updated_at（按更新时间排序）。注意：order_column和order_type参数需要配套使用。

        :return: The order_column of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        """Sets the order_column of this ListSharedReposDetailsRequest.

        按列排序，可设置为updated_at（按更新时间排序）。注意：order_column和order_type参数需要配套使用。

        :param order_column: The order_column of this ListSharedReposDetailsRequest.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        """Gets the order_type of this ListSharedReposDetailsRequest.

        排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。

        :return: The order_type of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this ListSharedReposDetailsRequest.

        排序类型，可设置为desc（降序）、asc（升序）。注意：order_column和order_type参数需要配套使用。

        :param order_type: The order_type of this ListSharedReposDetailsRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def filter(self):
        """Gets the filter of this ListSharedReposDetailsRequest.

        应填写 center::{center}|name::{name}|limit::{limit}|offset::{offset}|namespace::{namespace}|order_column::{order_column}|order_type::{order_type} ,其中 {center}可选为self: 我共享的镜像。thirdparty: 他人共享给我的镜像，namespace为组织名称，name为镜像仓库名称， {limit}为返回条数,{offset}为起始索引,{order_column}为按列排序，可设置为name、updated_time、tag_count,{order_type}为排序类型，可设置为desc（降序）、asc（升序）

        :return: The filter of this ListSharedReposDetailsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListSharedReposDetailsRequest.

        应填写 center::{center}|name::{name}|limit::{limit}|offset::{offset}|namespace::{namespace}|order_column::{order_column}|order_type::{order_type} ,其中 {center}可选为self: 我共享的镜像。thirdparty: 他人共享给我的镜像，namespace为组织名称，name为镜像仓库名称， {limit}为返回条数,{offset}为起始索引,{order_column}为按列排序，可设置为name、updated_time、tag_count,{order_type}为排序类型，可设置为desc（降序）、asc（升序）

        :param filter: The filter of this ListSharedReposDetailsRequest.
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
        if not isinstance(other, ListSharedReposDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
