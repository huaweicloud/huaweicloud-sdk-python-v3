# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordSetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_type': 'str',
        'marker': 'str',
        'search_mode': 'str',
        'limit': 'int',
        'offset': 'int',
        'tags': 'str',
        'status': 'str',
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'records': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'zone_type': 'zone_type',
        'marker': 'marker',
        'search_mode': 'search_mode',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'status': 'status',
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'records': 'records',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, zone_type=None, marker=None, search_mode=None, limit=None, offset=None, tags=None, status=None, type=None, name=None, id=None, records=None, sort_key=None, sort_dir=None):
        r"""ListRecordSetsRequest

        The model defined in huaweicloud sdk

        :param zone_type: **参数解释：** 记录集所属域名的类型。 **约束限制：** 不涉及。 **取值范围：** - public：表示查询公网域名的记录集。 - private：表示查询内网域名的记录集。  **默认取值：** public。
        :type zone_type: str
        :param marker: **参数解释：** 分页查询的起始资源ID。 - 查询第一页时，设置为空。 - 查询下一页时，设置为上一页最后一条资源的ID。  **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type marker: str
        :param search_mode: **参数解释：** 查询条件搜索模式。 **约束限制：** 不涉及。 **取值范围：** - like：模糊搜索 - equal：精确搜索  **默认取值：** 不涉及。
        :type search_mode: str
        :param limit: **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500
        :type limit: int
        :param offset: **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0
        :type offset: int
        :param tags: **参数解释：** 记录集的标签，包括标签键和标签值。 取值格式：key1,value1|key2,value2。 **约束限制：** - 多个标签之间用“|”分开，每个标签的键值用英文逗号“,”相隔。 - 多个标签之间为“与”的关系。 - 搜索模式为精确搜索。如果资源标签值value是以&amp;ast;开头时，则按照&amp;ast;后面的值全模糊匹配。  **取值范围：** 最多可以查询20个标签。 **默认取值：** 不涉及。
        :type tags: str
        :param status: **参数解释：** 记录集状态。 **约束限制：** 不涉及。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败  **默认取值：** 不涉及。
        :type status: str
        :param type: **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。
        :type type: str
        :param name: **参数解释：** 待查询的记录集的域名中包含此name。 搜索模式默认为模糊搜索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param id: **参数解释：** 待查询的记录集ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param records: **参数解释：** 待查询的记录集的值。 搜索模式默认为模糊搜索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type records: str
        :param sort_key: **参数解释：** 查询结果中记录集列表的排序字段。 **约束限制：** 不涉及。 **取值范围：** - name：记录集名称 - type：记录集类型  **默认取值：** 默认值为空，表示不排序。
        :type sort_key: str
        :param sort_dir: **参数解释：** 查询结果中记录集列表的排序方式。 **约束限制：** 不涉及。 **取值范围：** - desc：降序排序 - asc：升序排序  **默认取值：** 默认值为空，表示不排序。
        :type sort_dir: str
        """
        
        

        self._zone_type = None
        self._marker = None
        self._search_mode = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._status = None
        self._type = None
        self._name = None
        self._id = None
        self._records = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if zone_type is not None:
            self.zone_type = zone_type
        if marker is not None:
            self.marker = marker
        if search_mode is not None:
            self.search_mode = search_mode
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if records is not None:
            self.records = records
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def zone_type(self):
        r"""Gets the zone_type of this ListRecordSetsRequest.

        **参数解释：** 记录集所属域名的类型。 **约束限制：** 不涉及。 **取值范围：** - public：表示查询公网域名的记录集。 - private：表示查询内网域名的记录集。  **默认取值：** public。

        :return: The zone_type of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        r"""Sets the zone_type of this ListRecordSetsRequest.

        **参数解释：** 记录集所属域名的类型。 **约束限制：** 不涉及。 **取值范围：** - public：表示查询公网域名的记录集。 - private：表示查询内网域名的记录集。  **默认取值：** public。

        :param zone_type: The zone_type of this ListRecordSetsRequest.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def marker(self):
        r"""Gets the marker of this ListRecordSetsRequest.

        **参数解释：** 分页查询的起始资源ID。 - 查询第一页时，设置为空。 - 查询下一页时，设置为上一页最后一条资源的ID。  **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The marker of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRecordSetsRequest.

        **参数解释：** 分页查询的起始资源ID。 - 查询第一页时，设置为空。 - 查询下一页时，设置为上一页最后一条资源的ID。  **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param marker: The marker of this ListRecordSetsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def search_mode(self):
        r"""Gets the search_mode of this ListRecordSetsRequest.

        **参数解释：** 查询条件搜索模式。 **约束限制：** 不涉及。 **取值范围：** - like：模糊搜索 - equal：精确搜索  **默认取值：** 不涉及。

        :return: The search_mode of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        r"""Sets the search_mode of this ListRecordSetsRequest.

        **参数解释：** 查询条件搜索模式。 **约束限制：** 不涉及。 **取值范围：** - like：模糊搜索 - equal：精确搜索  **默认取值：** 不涉及。

        :param search_mode: The search_mode of this ListRecordSetsRequest.
        :type search_mode: str
        """
        self._search_mode = search_mode

    @property
    def limit(self):
        r"""Gets the limit of this ListRecordSetsRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :return: The limit of this ListRecordSetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRecordSetsRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :param limit: The limit of this ListRecordSetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRecordSetsRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :return: The offset of this ListRecordSetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRecordSetsRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :param offset: The offset of this ListRecordSetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def tags(self):
        r"""Gets the tags of this ListRecordSetsRequest.

        **参数解释：** 记录集的标签，包括标签键和标签值。 取值格式：key1,value1|key2,value2。 **约束限制：** - 多个标签之间用“|”分开，每个标签的键值用英文逗号“,”相隔。 - 多个标签之间为“与”的关系。 - 搜索模式为精确搜索。如果资源标签值value是以&ast;开头时，则按照&ast;后面的值全模糊匹配。  **取值范围：** 最多可以查询20个标签。 **默认取值：** 不涉及。

        :return: The tags of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListRecordSetsRequest.

        **参数解释：** 记录集的标签，包括标签键和标签值。 取值格式：key1,value1|key2,value2。 **约束限制：** - 多个标签之间用“|”分开，每个标签的键值用英文逗号“,”相隔。 - 多个标签之间为“与”的关系。 - 搜索模式为精确搜索。如果资源标签值value是以&ast;开头时，则按照&ast;后面的值全模糊匹配。  **取值范围：** 最多可以查询20个标签。 **默认取值：** 不涉及。

        :param tags: The tags of this ListRecordSetsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def status(self):
        r"""Gets the status of this ListRecordSetsRequest.

        **参数解释：** 记录集状态。 **约束限制：** 不涉及。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败  **默认取值：** 不涉及。

        :return: The status of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListRecordSetsRequest.

        **参数解释：** 记录集状态。 **约束限制：** 不涉及。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败  **默认取值：** 不涉及。

        :param status: The status of this ListRecordSetsRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListRecordSetsRequest.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。

        :return: The type of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListRecordSetsRequest.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。

        :param type: The type of this ListRecordSetsRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ListRecordSetsRequest.

        **参数解释：** 待查询的记录集的域名中包含此name。 搜索模式默认为模糊搜索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListRecordSetsRequest.

        **参数解释：** 待查询的记录集的域名中包含此name。 搜索模式默认为模糊搜索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this ListRecordSetsRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListRecordSetsRequest.

        **参数解释：** 待查询的记录集ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListRecordSetsRequest.

        **参数解释：** 待查询的记录集ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this ListRecordSetsRequest.
        :type id: str
        """
        self._id = id

    @property
    def records(self):
        r"""Gets the records of this ListRecordSetsRequest.

        **参数解释：** 待查询的记录集的值。 搜索模式默认为模糊搜索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The records of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListRecordSetsRequest.

        **参数解释：** 待查询的记录集的值。 搜索模式默认为模糊搜索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param records: The records of this ListRecordSetsRequest.
        :type records: str
        """
        self._records = records

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListRecordSetsRequest.

        **参数解释：** 查询结果中记录集列表的排序字段。 **约束限制：** 不涉及。 **取值范围：** - name：记录集名称 - type：记录集类型  **默认取值：** 默认值为空，表示不排序。

        :return: The sort_key of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListRecordSetsRequest.

        **参数解释：** 查询结果中记录集列表的排序字段。 **约束限制：** 不涉及。 **取值范围：** - name：记录集名称 - type：记录集类型  **默认取值：** 默认值为空，表示不排序。

        :param sort_key: The sort_key of this ListRecordSetsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListRecordSetsRequest.

        **参数解释：** 查询结果中记录集列表的排序方式。 **约束限制：** 不涉及。 **取值范围：** - desc：降序排序 - asc：升序排序  **默认取值：** 默认值为空，表示不排序。

        :return: The sort_dir of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListRecordSetsRequest.

        **参数解释：** 查询结果中记录集列表的排序方式。 **约束限制：** 不涉及。 **取值范围：** - desc：降序排序 - asc：升序排序  **默认取值：** 默认值为空，表示不排序。

        :param sort_dir: The sort_dir of this ListRecordSetsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListRecordSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
