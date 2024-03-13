# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueriesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'project_id': 'str',
        'offset': 'str',
        'limit': 'str',
        'conditions': 'list[ListQueriesCondition]',
        'order_by': 'str',
        'target': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'conditions': 'conditions',
        'order_by': 'order_by',
        'target': 'target'
    }

    def __init__(self, cluster_id=None, project_id=None, offset=None, limit=None, conditions=None, order_by=None, target=None):
        """ListQueriesRequestBody

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset&gt;&#x3D;0。
        :type offset: str
        :param limit: 每页显示的条目数量。
        :type limit: str
        :param conditions: 查询条件数组
        :type conditions: list[:class:`huaweicloudsdkdws.v2.ListQueriesCondition`]
        :param order_by: 排序字段
        :type order_by: str
        :param target: 固定值db_queries
        :type target: str
        """
        
        

        self._cluster_id = None
        self._project_id = None
        self._offset = None
        self._limit = None
        self._conditions = None
        self._order_by = None
        self._target = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.project_id = project_id
        self.offset = offset
        self.limit = limit
        self.conditions = conditions
        if order_by is not None:
            self.order_by = order_by
        self.target = target

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListQueriesRequestBody.

        集群ID。

        :return: The cluster_id of this ListQueriesRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListQueriesRequestBody.

        集群ID。

        :param cluster_id: The cluster_id of this ListQueriesRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def project_id(self):
        """Gets the project_id of this ListQueriesRequestBody.

        项目ID。

        :return: The project_id of this ListQueriesRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListQueriesRequestBody.

        项目ID。

        :param project_id: The project_id of this ListQueriesRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        """Gets the offset of this ListQueriesRequestBody.

        偏移量，表示从此偏移量开始查询，offset>=0。

        :return: The offset of this ListQueriesRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListQueriesRequestBody.

        偏移量，表示从此偏移量开始查询，offset>=0。

        :param offset: The offset of this ListQueriesRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListQueriesRequestBody.

        每页显示的条目数量。

        :return: The limit of this ListQueriesRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListQueriesRequestBody.

        每页显示的条目数量。

        :param limit: The limit of this ListQueriesRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def conditions(self):
        """Gets the conditions of this ListQueriesRequestBody.

        查询条件数组

        :return: The conditions of this ListQueriesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ListQueriesCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ListQueriesRequestBody.

        查询条件数组

        :param conditions: The conditions of this ListQueriesRequestBody.
        :type conditions: list[:class:`huaweicloudsdkdws.v2.ListQueriesCondition`]
        """
        self._conditions = conditions

    @property
    def order_by(self):
        """Gets the order_by of this ListQueriesRequestBody.

        排序字段

        :return: The order_by of this ListQueriesRequestBody.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListQueriesRequestBody.

        排序字段

        :param order_by: The order_by of this ListQueriesRequestBody.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def target(self):
        """Gets the target of this ListQueriesRequestBody.

        固定值db_queries

        :return: The target of this ListQueriesRequestBody.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ListQueriesRequestBody.

        固定值db_queries

        :param target: The target of this ListQueriesRequestBody.
        :type target: str
        """
        self._target = target

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
        if not isinstance(other, ListQueriesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
