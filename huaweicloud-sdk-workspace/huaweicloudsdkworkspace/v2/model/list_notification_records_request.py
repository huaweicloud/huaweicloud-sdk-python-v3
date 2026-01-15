# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_type': 'str',
        'desktop_name': 'str',
        'desktop_pool_name': 'str',
        'user_name': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_field': 'str',
        'sort_type': 'str'
    }

    attribute_map = {
        'query_type': 'query_type',
        'desktop_name': 'desktop_name',
        'desktop_pool_name': 'desktop_pool_name',
        'user_name': 'user_name',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type'
    }

    def __init__(self, query_type=None, desktop_name=None, desktop_pool_name=None, user_name=None, type=None, offset=None, limit=None, sort_field=None, sort_type=None):
        r"""ListNotificationRecordsRequest

        The model defined in huaweicloud sdk

        :param query_type: 通过该类型查询桌面或桌面池相关的通知拦截记录 - DESKTOP: 查找当前projectId下与桌面相关的通知拦截记录 - DESKTOP_POOL: 查找当前projectId下与桌面池相关的通知拦截记录
        :type query_type: str
        :param desktop_name: 桌面名
        :type desktop_name: str
        :param desktop_pool_name: 桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。
        :type desktop_pool_name: str
        :param user_name: 用户名
        :type user_name: str
        :param type: 过滤出与SMN通知类型一致的通知拦截记录 - EMAIL: 通过邮件查找通知拦截记录 - SMS: 通过短信查找通知拦截记录
        :type type: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，取值范围0-1000，默认值1000。
        :type limit: int
        :param sort_field: 排序字段名称，需要结合sort_type字段一起使用。 - operate_time 发送时间
        :type sort_field: str
        :param sort_type: 排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。
        :type sort_type: str
        """
        
        

        self._query_type = None
        self._desktop_name = None
        self._desktop_pool_name = None
        self._user_name = None
        self._type = None
        self._offset = None
        self._limit = None
        self._sort_field = None
        self._sort_type = None
        self.discriminator = None

        self.query_type = query_type
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_pool_name is not None:
            self.desktop_pool_name = desktop_pool_name
        if user_name is not None:
            self.user_name = user_name
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type

    @property
    def query_type(self):
        r"""Gets the query_type of this ListNotificationRecordsRequest.

        通过该类型查询桌面或桌面池相关的通知拦截记录 - DESKTOP: 查找当前projectId下与桌面相关的通知拦截记录 - DESKTOP_POOL: 查找当前projectId下与桌面池相关的通知拦截记录

        :return: The query_type of this ListNotificationRecordsRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ListNotificationRecordsRequest.

        通过该类型查询桌面或桌面池相关的通知拦截记录 - DESKTOP: 查找当前projectId下与桌面相关的通知拦截记录 - DESKTOP_POOL: 查找当前projectId下与桌面池相关的通知拦截记录

        :param query_type: The query_type of this ListNotificationRecordsRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this ListNotificationRecordsRequest.

        桌面名

        :return: The desktop_name of this ListNotificationRecordsRequest.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this ListNotificationRecordsRequest.

        桌面名

        :param desktop_name: The desktop_name of this ListNotificationRecordsRequest.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_pool_name(self):
        r"""Gets the desktop_pool_name of this ListNotificationRecordsRequest.

        桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。

        :return: The desktop_pool_name of this ListNotificationRecordsRequest.
        :rtype: str
        """
        return self._desktop_pool_name

    @desktop_pool_name.setter
    def desktop_pool_name(self, desktop_pool_name):
        r"""Sets the desktop_pool_name of this ListNotificationRecordsRequest.

        桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。

        :param desktop_pool_name: The desktop_pool_name of this ListNotificationRecordsRequest.
        :type desktop_pool_name: str
        """
        self._desktop_pool_name = desktop_pool_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ListNotificationRecordsRequest.

        用户名

        :return: The user_name of this ListNotificationRecordsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListNotificationRecordsRequest.

        用户名

        :param user_name: The user_name of this ListNotificationRecordsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def type(self):
        r"""Gets the type of this ListNotificationRecordsRequest.

        过滤出与SMN通知类型一致的通知拦截记录 - EMAIL: 通过邮件查找通知拦截记录 - SMS: 通过短信查找通知拦截记录

        :return: The type of this ListNotificationRecordsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListNotificationRecordsRequest.

        过滤出与SMN通知类型一致的通知拦截记录 - EMAIL: 通过邮件查找通知拦截记录 - SMS: 通过短信查找通知拦截记录

        :param type: The type of this ListNotificationRecordsRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListNotificationRecordsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListNotificationRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNotificationRecordsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListNotificationRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNotificationRecordsRequest.

        用于分页查询，取值范围0-1000，默认值1000。

        :return: The limit of this ListNotificationRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNotificationRecordsRequest.

        用于分页查询，取值范围0-1000，默认值1000。

        :param limit: The limit of this ListNotificationRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListNotificationRecordsRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - operate_time 发送时间

        :return: The sort_field of this ListNotificationRecordsRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListNotificationRecordsRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - operate_time 发送时间

        :param sort_field: The sort_field of this ListNotificationRecordsRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ListNotificationRecordsRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :return: The sort_type of this ListNotificationRecordsRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ListNotificationRecordsRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :param sort_type: The sort_type of this ListNotificationRecordsRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

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
        if not isinstance(other, ListNotificationRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
