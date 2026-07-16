# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlgorithmsRequest:

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
        'group_by': 'str',
        'searches': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'order': 'order',
        'group_by': 'group_by',
        'searches': 'searches',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, offset=None, limit=None, sort_by=None, order=None, group_by=None, searches=None, workspace_id=None):
        r"""ListAlgorithmsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询算法的偏移量，最小为0。例如设置为1，则表示从第二条开始查。
        :type offset: int
        :param limit: 查询算法的限制量。最小为1，最大为50。
        :type limit: int
        :param sort_by: 查询算法排列顺序的指标。默认使用create_time排序。
        :type sort_by: str
        :param order: 查询算法排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。
        :type order: str
        :param group_by: 查询算法要搜索的分组条件。
        :type group_by: str
        :param searches: 查询算法所要过滤的条件，如算法名称模糊匹配。
        :type searches: str
        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._sort_by = None
        self._order = None
        self._group_by = None
        self._searches = None
        self._workspace_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if group_by is not None:
            self.group_by = group_by
        if searches is not None:
            self.searches = searches
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAlgorithmsRequest.

        查询算法的偏移量，最小为0。例如设置为1，则表示从第二条开始查。

        :return: The offset of this ListAlgorithmsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlgorithmsRequest.

        查询算法的偏移量，最小为0。例如设置为1，则表示从第二条开始查。

        :param offset: The offset of this ListAlgorithmsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlgorithmsRequest.

        查询算法的限制量。最小为1，最大为50。

        :return: The limit of this ListAlgorithmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlgorithmsRequest.

        查询算法的限制量。最小为1，最大为50。

        :param limit: The limit of this ListAlgorithmsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListAlgorithmsRequest.

        查询算法排列顺序的指标。默认使用create_time排序。

        :return: The sort_by of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListAlgorithmsRequest.

        查询算法排列顺序的指标。默认使用create_time排序。

        :param sort_by: The sort_by of this ListAlgorithmsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this ListAlgorithmsRequest.

        查询算法排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :return: The order of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListAlgorithmsRequest.

        查询算法排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :param order: The order of this ListAlgorithmsRequest.
        :type order: str
        """
        self._order = order

    @property
    def group_by(self):
        r"""Gets the group_by of this ListAlgorithmsRequest.

        查询算法要搜索的分组条件。

        :return: The group_by of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ListAlgorithmsRequest.

        查询算法要搜索的分组条件。

        :param group_by: The group_by of this ListAlgorithmsRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def searches(self):
        r"""Gets the searches of this ListAlgorithmsRequest.

        查询算法所要过滤的条件，如算法名称模糊匹配。

        :return: The searches of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._searches

    @searches.setter
    def searches(self, searches):
        r"""Sets the searches of this ListAlgorithmsRequest.

        查询算法所要过滤的条件，如算法名称模糊匹配。

        :param searches: The searches of this ListAlgorithmsRequest.
        :type searches: str
        """
        self._searches = searches

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAlgorithmsRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAlgorithmsRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this ListAlgorithmsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ListAlgorithmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
