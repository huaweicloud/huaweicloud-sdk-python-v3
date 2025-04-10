# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'create_until': 'str',
        'create_since': 'str',
        'name': 'str',
        'tag': 'str',
        'state': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'create_until': 'create_until',
        'create_since': 'create_since',
        'name': 'name',
        'tag': 'tag',
        'state': 'state'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, create_until=None, create_since=None, name=None, tag=None, state=None):
        r"""ListProductsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param sort_key: 排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order
        :type sort_key: str
        :param sort_dir: 排序方式。 * asc：升序 * desc：降序  默认asc升序。
        :type sort_dir: str
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。
        :type create_until: str
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。
        :type create_since: str
        :param name: 按名称模糊查询。
        :type name: str
        :param tag: 按标签模糊查询。
        :type tag: str
        :param state: 按状态查询，多状态使用英文逗号分隔。
        :type state: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._create_until = None
        self._create_since = None
        self._name = None
        self._tag = None
        self._state = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if create_until is not None:
            self.create_until = create_until
        if create_since is not None:
            self.create_since = create_since
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if state is not None:
            self.state = state

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListProductsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListProductsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListProductsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListProductsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProductsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListProductsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProductsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListProductsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProductsRequest.

        每页显示的条目数量。

        :return: The limit of this ListProductsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProductsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListProductsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListProductsRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :return: The sort_key of this ListProductsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListProductsRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :param sort_key: The sort_key of this ListProductsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListProductsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :return: The sort_dir of this ListProductsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListProductsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :param sort_dir: The sort_dir of this ListProductsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def create_until(self):
        r"""Gets the create_until of this ListProductsRequest.

        过滤创建时间<=输入时间的记录。

        :return: The create_until of this ListProductsRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this ListProductsRequest.

        过滤创建时间<=输入时间的记录。

        :param create_until: The create_until of this ListProductsRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def create_since(self):
        r"""Gets the create_since of this ListProductsRequest.

        过滤创建时间>=输入时间的记录。

        :return: The create_since of this ListProductsRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this ListProductsRequest.

        过滤创建时间>=输入时间的记录。

        :param create_since: The create_since of this ListProductsRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def name(self):
        r"""Gets the name of this ListProductsRequest.

        按名称模糊查询。

        :return: The name of this ListProductsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListProductsRequest.

        按名称模糊查询。

        :param name: The name of this ListProductsRequest.
        :type name: str
        """
        self._name = name

    @property
    def tag(self):
        r"""Gets the tag of this ListProductsRequest.

        按标签模糊查询。

        :return: The tag of this ListProductsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListProductsRequest.

        按标签模糊查询。

        :param tag: The tag of this ListProductsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def state(self):
        r"""Gets the state of this ListProductsRequest.

        按状态查询，多状态使用英文逗号分隔。

        :return: The state of this ListProductsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListProductsRequest.

        按状态查询，多状态使用英文逗号分隔。

        :param state: The state of this ListProductsRequest.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, ListProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
