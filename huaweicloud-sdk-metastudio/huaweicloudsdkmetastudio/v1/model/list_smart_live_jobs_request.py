# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmartLiveJobsRequest:

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
        'state': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'create_since': 'str',
        'create_until': 'str',
        'room_name': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'state': 'state',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'create_since': 'create_since',
        'create_until': 'create_until',
        'room_name': 'room_name'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, state=None, sort_key=None, sort_dir=None, create_since=None, create_until=None, room_name=None):
        r"""ListSmartLiveJobsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param state: 任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state&#x3D;CREATING,PUBLISHED
        :type state: str
        :param sort_key: 排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order
        :type sort_key: str
        :param sort_dir: 排序方式。 * asc：升序 * desc：降序  默认asc升序。
        :type sort_dir: str
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。
        :type create_since: str
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。
        :type create_until: str
        :param room_name: 按直播间名称模糊查询。
        :type room_name: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._state = None
        self._sort_key = None
        self._sort_dir = None
        self._create_since = None
        self._create_until = None
        self._room_name = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if state is not None:
            self.state = state
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if create_since is not None:
            self.create_since = create_since
        if create_until is not None:
            self.create_until = create_until
        if room_name is not None:
            self.room_name = room_name

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListSmartLiveJobsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListSmartLiveJobsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListSmartLiveJobsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListSmartLiveJobsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListSmartLiveJobsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListSmartLiveJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSmartLiveJobsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListSmartLiveJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSmartLiveJobsRequest.

        每页显示的条目数量。

        :return: The limit of this ListSmartLiveJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSmartLiveJobsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListSmartLiveJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def state(self):
        r"""Gets the state of this ListSmartLiveJobsRequest.

        任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state=CREATING,PUBLISHED

        :return: The state of this ListSmartLiveJobsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListSmartLiveJobsRequest.

        任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state=CREATING,PUBLISHED

        :param state: The state of this ListSmartLiveJobsRequest.
        :type state: str
        """
        self._state = state

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSmartLiveJobsRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :return: The sort_key of this ListSmartLiveJobsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSmartLiveJobsRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :param sort_key: The sort_key of this ListSmartLiveJobsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSmartLiveJobsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :return: The sort_dir of this ListSmartLiveJobsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSmartLiveJobsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :param sort_dir: The sort_dir of this ListSmartLiveJobsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def create_since(self):
        r"""Gets the create_since of this ListSmartLiveJobsRequest.

        过滤创建时间>=输入时间的记录。

        :return: The create_since of this ListSmartLiveJobsRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this ListSmartLiveJobsRequest.

        过滤创建时间>=输入时间的记录。

        :param create_since: The create_since of this ListSmartLiveJobsRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def create_until(self):
        r"""Gets the create_until of this ListSmartLiveJobsRequest.

        过滤创建时间<=输入时间的记录。

        :return: The create_until of this ListSmartLiveJobsRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this ListSmartLiveJobsRequest.

        过滤创建时间<=输入时间的记录。

        :param create_until: The create_until of this ListSmartLiveJobsRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def room_name(self):
        r"""Gets the room_name of this ListSmartLiveJobsRequest.

        按直播间名称模糊查询。

        :return: The room_name of this ListSmartLiveJobsRequest.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this ListSmartLiveJobsRequest.

        按直播间名称模糊查询。

        :param room_name: The room_name of this ListSmartLiveJobsRequest.
        :type room_name: str
        """
        self._room_name = room_name

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
        if not isinstance(other, ListSmartLiveJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
