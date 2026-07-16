# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkspaceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'sort_by': 'str',
        'order': 'str',
        'enterprise_project_id': 'str',
        'name': 'str',
        'filter_accessible': 'bool'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'order': 'order',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'filter_accessible': 'filter_accessible'
    }

    def __init__(self, offset=None, limit=None, sort_by=None, order=None, enterprise_project_id=None, name=None, filter_accessible=None):
        r"""ListWorkspaceRequest

        The model defined in huaweicloud sdk

        :param offset: 分页列表的起始页，默认为&#39;0&#39;。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，默认为&#39;1000&#39;。
        :type limit: int
        :param sort_by: 指定排序字段，可选&#39;name&#39;、&#39;update_time&#39;、&#39;status&#39;，默认是&#39;name&#39;。
        :type sort_by: str
        :param order: 可选值。&#39;asc&#39;为递增排序。&#39;desc&#39;为递减排序，默认为&#39;desc&#39;。
        :type order: str
        :param enterprise_project_id: 企业项目id，指定此参数会只返回该企业项目id下的工作空间。默认显示所有工作空间。
        :type enterprise_project_id: str
        :param name: 工作空间名称查询参数，指定此参数会模糊查询该名称的工作空间。默认显示所有工作空间。
        :type name: str
        :param filter_accessible: 该参数用于筛选可访问的工作空间。指定该参数为true，则会筛选掉当前用户无权限访问的工作空间。该参数默认为false，即为显示所有工作空间。
        :type filter_accessible: bool
        """
        
        

        self._offset = None
        self._limit = None
        self._sort_by = None
        self._order = None
        self._enterprise_project_id = None
        self._name = None
        self._filter_accessible = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if filter_accessible is not None:
            self.filter_accessible = filter_accessible

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkspaceRequest.

        分页列表的起始页，默认为'0'。

        :return: The offset of this ListWorkspaceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkspaceRequest.

        分页列表的起始页，默认为'0'。

        :param offset: The offset of this ListWorkspaceRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkspaceRequest.

        指定每一页返回的最大条目数，默认为'1000'。

        :return: The limit of this ListWorkspaceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkspaceRequest.

        指定每一页返回的最大条目数，默认为'1000'。

        :param limit: The limit of this ListWorkspaceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListWorkspaceRequest.

        指定排序字段，可选'name'、'update_time'、'status'，默认是'name'。

        :return: The sort_by of this ListWorkspaceRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListWorkspaceRequest.

        指定排序字段，可选'name'、'update_time'、'status'，默认是'name'。

        :param sort_by: The sort_by of this ListWorkspaceRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this ListWorkspaceRequest.

        可选值。'asc'为递增排序。'desc'为递减排序，默认为'desc'。

        :return: The order of this ListWorkspaceRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListWorkspaceRequest.

        可选值。'asc'为递增排序。'desc'为递减排序，默认为'desc'。

        :param order: The order of this ListWorkspaceRequest.
        :type order: str
        """
        self._order = order

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWorkspaceRequest.

        企业项目id，指定此参数会只返回该企业项目id下的工作空间。默认显示所有工作空间。

        :return: The enterprise_project_id of this ListWorkspaceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWorkspaceRequest.

        企业项目id，指定此参数会只返回该企业项目id下的工作空间。默认显示所有工作空间。

        :param enterprise_project_id: The enterprise_project_id of this ListWorkspaceRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ListWorkspaceRequest.

        工作空间名称查询参数，指定此参数会模糊查询该名称的工作空间。默认显示所有工作空间。

        :return: The name of this ListWorkspaceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListWorkspaceRequest.

        工作空间名称查询参数，指定此参数会模糊查询该名称的工作空间。默认显示所有工作空间。

        :param name: The name of this ListWorkspaceRequest.
        :type name: str
        """
        self._name = name

    @property
    def filter_accessible(self):
        r"""Gets the filter_accessible of this ListWorkspaceRequest.

        该参数用于筛选可访问的工作空间。指定该参数为true，则会筛选掉当前用户无权限访问的工作空间。该参数默认为false，即为显示所有工作空间。

        :return: The filter_accessible of this ListWorkspaceRequest.
        :rtype: bool
        """
        return self._filter_accessible

    @filter_accessible.setter
    def filter_accessible(self, filter_accessible):
        r"""Sets the filter_accessible of this ListWorkspaceRequest.

        该参数用于筛选可访问的工作空间。指定该参数为true，则会筛选掉当前用户无权限访问的工作空间。该参数默认为false，即为显示所有工作空间。

        :param filter_accessible: The filter_accessible of this ListWorkspaceRequest.
        :type filter_accessible: bool
        """
        self._filter_accessible = filter_accessible

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
        if not isinstance(other, ListWorkspaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
