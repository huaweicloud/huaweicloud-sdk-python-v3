# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordSetsByZoneRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_id': 'str',
        'search_mode': 'str',
        'marker': 'str',
        'limit': 'int',
        'offset': 'int',
        'tags': 'str',
        'status': 'str',
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'zone_id': 'zone_id',
        'search_mode': 'search_mode',
        'marker': 'marker',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'status': 'status',
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, zone_id=None, search_mode=None, marker=None, limit=None, offset=None, tags=None, status=None, type=None, name=None, id=None, sort_key=None, sort_dir=None):
        r"""ListRecordSetsByZoneRequest

        The model defined in huaweicloud sdk

        :param zone_id: 所属zone id。
        :type zone_id: str
        :param search_mode: 查询条件搜索模式。  取值范围：  like：模糊搜索 equal：精确搜索
        :type search_mode: str
        :param marker: 分页查询起始的资源ID，为空时为查询第一页。  默认值为空。
        :type marker: str
        :param limit: 每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。
        :type limit: int
        :param offset: 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。
        :type offset: int
        :param tags: 资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用\&quot;|\&quot;分开，每个标签的键值用英文逗号\&quot;,\&quot;相隔。
        :type tags: str
        :param status: 待查询的Record Set的状态。 取值范围：ACTIVE、ERROR、DISABLE、FREEZE、PENDING_CREATE、PENDING_UPDATE、PENDING_DELETE
        :type status: str
        :param type: 待查询的Record Set的记录集类型。 公网域名场景的记录类型: A、AAAA、MX、CNAME、TXT、NS、SRV、CAA。 内网域名场景的记录类型: A、AAAA、MX、CNAME、TXT、SRV。
        :type type: str
        :param name: 待查询的Record Set的域名中包含此name。  搜索模式默认为模糊搜索。  默认值为空。
        :type name: str
        :param id: 待查询的Record Set的id包含此id。
        :type id: str
        :param sort_key: 查询结果中Record Set列表的排序字段。  取值范围为：  name：记录集名称 type：记录集类型 默认值为空，表示不排序。
        :type sort_key: str
        :param sort_dir: 查询结果中Record Set列表的排序方式。  取值范围：  desc：降序排序 asc：升序排序 默认值为空，表示不排序。
        :type sort_dir: str
        """
        
        

        self._zone_id = None
        self._search_mode = None
        self._marker = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._status = None
        self._type = None
        self._name = None
        self._id = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.zone_id = zone_id
        if search_mode is not None:
            self.search_mode = search_mode
        if marker is not None:
            self.marker = marker
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
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def zone_id(self):
        r"""Gets the zone_id of this ListRecordSetsByZoneRequest.

        所属zone id。

        :return: The zone_id of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this ListRecordSetsByZoneRequest.

        所属zone id。

        :param zone_id: The zone_id of this ListRecordSetsByZoneRequest.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def search_mode(self):
        r"""Gets the search_mode of this ListRecordSetsByZoneRequest.

        查询条件搜索模式。  取值范围：  like：模糊搜索 equal：精确搜索

        :return: The search_mode of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        r"""Sets the search_mode of this ListRecordSetsByZoneRequest.

        查询条件搜索模式。  取值范围：  like：模糊搜索 equal：精确搜索

        :param search_mode: The search_mode of this ListRecordSetsByZoneRequest.
        :type search_mode: str
        """
        self._search_mode = search_mode

    @property
    def marker(self):
        r"""Gets the marker of this ListRecordSetsByZoneRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :return: The marker of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRecordSetsByZoneRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :param marker: The marker of this ListRecordSetsByZoneRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListRecordSetsByZoneRequest.

        每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :return: The limit of this ListRecordSetsByZoneRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRecordSetsByZoneRequest.

        每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :param limit: The limit of this ListRecordSetsByZoneRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRecordSetsByZoneRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。

        :return: The offset of this ListRecordSetsByZoneRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRecordSetsByZoneRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。

        :param offset: The offset of this ListRecordSetsByZoneRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def tags(self):
        r"""Gets the tags of this ListRecordSetsByZoneRequest.

        资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用\"|\"分开，每个标签的键值用英文逗号\",\"相隔。

        :return: The tags of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListRecordSetsByZoneRequest.

        资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用\"|\"分开，每个标签的键值用英文逗号\",\"相隔。

        :param tags: The tags of this ListRecordSetsByZoneRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def status(self):
        r"""Gets the status of this ListRecordSetsByZoneRequest.

        待查询的Record Set的状态。 取值范围：ACTIVE、ERROR、DISABLE、FREEZE、PENDING_CREATE、PENDING_UPDATE、PENDING_DELETE

        :return: The status of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListRecordSetsByZoneRequest.

        待查询的Record Set的状态。 取值范围：ACTIVE、ERROR、DISABLE、FREEZE、PENDING_CREATE、PENDING_UPDATE、PENDING_DELETE

        :param status: The status of this ListRecordSetsByZoneRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListRecordSetsByZoneRequest.

        待查询的Record Set的记录集类型。 公网域名场景的记录类型: A、AAAA、MX、CNAME、TXT、NS、SRV、CAA。 内网域名场景的记录类型: A、AAAA、MX、CNAME、TXT、SRV。

        :return: The type of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListRecordSetsByZoneRequest.

        待查询的Record Set的记录集类型。 公网域名场景的记录类型: A、AAAA、MX、CNAME、TXT、NS、SRV、CAA。 内网域名场景的记录类型: A、AAAA、MX、CNAME、TXT、SRV。

        :param type: The type of this ListRecordSetsByZoneRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ListRecordSetsByZoneRequest.

        待查询的Record Set的域名中包含此name。  搜索模式默认为模糊搜索。  默认值为空。

        :return: The name of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListRecordSetsByZoneRequest.

        待查询的Record Set的域名中包含此name。  搜索模式默认为模糊搜索。  默认值为空。

        :param name: The name of this ListRecordSetsByZoneRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListRecordSetsByZoneRequest.

        待查询的Record Set的id包含此id。

        :return: The id of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListRecordSetsByZoneRequest.

        待查询的Record Set的id包含此id。

        :param id: The id of this ListRecordSetsByZoneRequest.
        :type id: str
        """
        self._id = id

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListRecordSetsByZoneRequest.

        查询结果中Record Set列表的排序字段。  取值范围为：  name：记录集名称 type：记录集类型 默认值为空，表示不排序。

        :return: The sort_key of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListRecordSetsByZoneRequest.

        查询结果中Record Set列表的排序字段。  取值范围为：  name：记录集名称 type：记录集类型 默认值为空，表示不排序。

        :param sort_key: The sort_key of this ListRecordSetsByZoneRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListRecordSetsByZoneRequest.

        查询结果中Record Set列表的排序方式。  取值范围：  desc：降序排序 asc：升序排序 默认值为空，表示不排序。

        :return: The sort_dir of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListRecordSetsByZoneRequest.

        查询结果中Record Set列表的排序方式。  取值范围：  desc：降序排序 asc：升序排序 默认值为空，表示不排序。

        :param sort_dir: The sort_dir of this ListRecordSetsByZoneRequest.
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
        if not isinstance(other, ListRecordSetsByZoneRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
