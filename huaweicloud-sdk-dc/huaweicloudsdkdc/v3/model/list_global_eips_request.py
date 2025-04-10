# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalEipsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'fields': 'list[str]',
        'ext_fields': 'list[str]',
        'sort_key': 'str',
        'sort_dir': 'list[str]',
        'connect_gateway_id': 'str',
        'status': 'list[str]',
        'global_eip_id': 'list[str]',
        'global_eip_segment_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'fields': 'fields',
        'ext_fields': 'ext_fields',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'connect_gateway_id': 'connect_gateway_id',
        'status': 'status',
        'global_eip_id': 'global_eip_id',
        'global_eip_segment_id': 'global_eip_segment_id'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, ext_fields=None, sort_key=None, sort_dir=None, connect_gateway_id=None, status=None, global_eip_id=None, global_eip_segment_id=None):
        r"""ListGlobalEipsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param offset: 分页偏移量
        :type offset: int
        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param page_reverse: 分页参数
        :type page_reverse: bool
        :param fields: 显示字段列表
        :type fields: list[str]
        :param ext_fields: show response ext-fields
        :type ext_fields: list[str]
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param connect_gateway_id: 互联网关ID
        :type connect_gateway_id: str
        :param status: 根椐资源状态过滤实例
        :type status: list[str]
        :param global_eip_id: 全局弹性IP的ID
        :type global_eip_id: list[str]
        :param global_eip_segment_id: 全局弹性IP(有掩码)的ID
        :type global_eip_segment_id: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._fields = None
        self._ext_fields = None
        self._sort_key = None
        self._sort_dir = None
        self._connect_gateway_id = None
        self._status = None
        self._global_eip_id = None
        self._global_eip_segment_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if fields is not None:
            self.fields = fields
        if ext_fields is not None:
            self.ext_fields = ext_fields
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        self.connect_gateway_id = connect_gateway_id
        if status is not None:
            self.status = status
        if global_eip_id is not None:
            self.global_eip_id = global_eip_id
        if global_eip_segment_id is not None:
            self.global_eip_segment_id = global_eip_segment_id

    @property
    def limit(self):
        r"""Gets the limit of this ListGlobalEipsRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListGlobalEipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGlobalEipsRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListGlobalEipsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListGlobalEipsRequest.

        分页偏移量

        :return: The offset of this ListGlobalEipsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGlobalEipsRequest.

        分页偏移量

        :param offset: The offset of this ListGlobalEipsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListGlobalEipsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListGlobalEipsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListGlobalEipsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListGlobalEipsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListGlobalEipsRequest.

        分页参数

        :return: The page_reverse of this ListGlobalEipsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListGlobalEipsRequest.

        分页参数

        :param page_reverse: The page_reverse of this ListGlobalEipsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        r"""Gets the fields of this ListGlobalEipsRequest.

        显示字段列表

        :return: The fields of this ListGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListGlobalEipsRequest.

        显示字段列表

        :param fields: The fields of this ListGlobalEipsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def ext_fields(self):
        r"""Gets the ext_fields of this ListGlobalEipsRequest.

        show response ext-fields

        :return: The ext_fields of this ListGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        r"""Sets the ext_fields of this ListGlobalEipsRequest.

        show response ext-fields

        :param ext_fields: The ext_fields of this ListGlobalEipsRequest.
        :type ext_fields: list[str]
        """
        self._ext_fields = ext_fields

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListGlobalEipsRequest.

        排序字段。

        :return: The sort_key of this ListGlobalEipsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListGlobalEipsRequest.

        排序字段。

        :param sort_key: The sort_key of this ListGlobalEipsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListGlobalEipsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ListGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListGlobalEipsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ListGlobalEipsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def connect_gateway_id(self):
        r"""Gets the connect_gateway_id of this ListGlobalEipsRequest.

        互联网关ID

        :return: The connect_gateway_id of this ListGlobalEipsRequest.
        :rtype: str
        """
        return self._connect_gateway_id

    @connect_gateway_id.setter
    def connect_gateway_id(self, connect_gateway_id):
        r"""Sets the connect_gateway_id of this ListGlobalEipsRequest.

        互联网关ID

        :param connect_gateway_id: The connect_gateway_id of this ListGlobalEipsRequest.
        :type connect_gateway_id: str
        """
        self._connect_gateway_id = connect_gateway_id

    @property
    def status(self):
        r"""Gets the status of this ListGlobalEipsRequest.

        根椐资源状态过滤实例

        :return: The status of this ListGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGlobalEipsRequest.

        根椐资源状态过滤实例

        :param status: The status of this ListGlobalEipsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def global_eip_id(self):
        r"""Gets the global_eip_id of this ListGlobalEipsRequest.

        全局弹性IP的ID

        :return: The global_eip_id of this ListGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        r"""Sets the global_eip_id of this ListGlobalEipsRequest.

        全局弹性IP的ID

        :param global_eip_id: The global_eip_id of this ListGlobalEipsRequest.
        :type global_eip_id: list[str]
        """
        self._global_eip_id = global_eip_id

    @property
    def global_eip_segment_id(self):
        r"""Gets the global_eip_segment_id of this ListGlobalEipsRequest.

        全局弹性IP(有掩码)的ID

        :return: The global_eip_segment_id of this ListGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._global_eip_segment_id

    @global_eip_segment_id.setter
    def global_eip_segment_id(self, global_eip_segment_id):
        r"""Sets the global_eip_segment_id of this ListGlobalEipsRequest.

        全局弹性IP(有掩码)的ID

        :param global_eip_segment_id: The global_eip_segment_id of this ListGlobalEipsRequest.
        :type global_eip_segment_id: list[str]
        """
        self._global_eip_segment_id = global_eip_segment_id

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
        if not isinstance(other, ListGlobalEipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
