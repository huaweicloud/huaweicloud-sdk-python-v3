# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_index': 'int',
        'page_size': 'int',
        'search': 'str',
        'sort_field': 'str',
        'sort_order': 'str',
        'creator_id': 'str',
        'build_status': 'str'
    }

    attribute_map = {
        'page_index': 'page_index',
        'page_size': 'page_size',
        'search': 'search',
        'sort_field': 'sort_field',
        'sort_order': 'sort_order',
        'creator_id': 'creator_id',
        'build_status': 'build_status'
    }

    def __init__(self, page_index=None, page_size=None, search=None, sort_field=None, sort_order=None, creator_id=None, build_status=None):
        r"""ListJobRequest

        The model defined in huaweicloud sdk

        :param page_index: 分页页码，表示从此页开始查询，page_index大于等于0
        :type page_index: int
        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: int
        :param search: 查询关键字
        :type search: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_order: 排序方式（ASC|DESC）
        :type sort_order: str
        :param creator_id: 创建人
        :type creator_id: str
        :param build_status: 构建状态
        :type build_status: str
        """
        
        

        self._page_index = None
        self._page_size = None
        self._search = None
        self._sort_field = None
        self._sort_order = None
        self._creator_id = None
        self._build_status = None
        self.discriminator = None

        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if search is not None:
            self.search = search
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order
        if creator_id is not None:
            self.creator_id = creator_id
        if build_status is not None:
            self.build_status = build_status

    @property
    def page_index(self):
        r"""Gets the page_index of this ListJobRequest.

        分页页码，表示从此页开始查询，page_index大于等于0

        :return: The page_index of this ListJobRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListJobRequest.

        分页页码，表示从此页开始查询，page_index大于等于0

        :param page_index: The page_index of this ListJobRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListJobRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ListJobRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListJobRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ListJobRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def search(self):
        r"""Gets the search of this ListJobRequest.

        查询关键字

        :return: The search of this ListJobRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListJobRequest.

        查询关键字

        :param search: The search of this ListJobRequest.
        :type search: str
        """
        self._search = search

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListJobRequest.

        排序字段

        :return: The sort_field of this ListJobRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListJobRequest.

        排序字段

        :param sort_field: The sort_field of this ListJobRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ListJobRequest.

        排序方式（ASC|DESC）

        :return: The sort_order of this ListJobRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ListJobRequest.

        排序方式（ASC|DESC）

        :param sort_order: The sort_order of this ListJobRequest.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ListJobRequest.

        创建人

        :return: The creator_id of this ListJobRequest.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ListJobRequest.

        创建人

        :param creator_id: The creator_id of this ListJobRequest.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def build_status(self):
        r"""Gets the build_status of this ListJobRequest.

        构建状态

        :return: The build_status of this ListJobRequest.
        :rtype: str
        """
        return self._build_status

    @build_status.setter
    def build_status(self, build_status):
        r"""Sets the build_status of this ListJobRequest.

        构建状态

        :param build_status: The build_status of this ListJobRequest.
        :type build_status: str
        """
        self._build_status = build_status

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
        if not isinstance(other, ListJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
