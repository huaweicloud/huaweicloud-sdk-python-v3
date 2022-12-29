# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecordSetByZoneRequest:

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
        'marker': 'str',
        'limit': 'int',
        'offset': 'int',
        'line_id': 'str',
        'tags': 'str',
        'status': 'str',
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'search_mode': 'str'
    }

    attribute_map = {
        'zone_id': 'zone_id',
        'marker': 'marker',
        'limit': 'limit',
        'offset': 'offset',
        'line_id': 'line_id',
        'tags': 'tags',
        'status': 'status',
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'search_mode': 'search_mode'
    }

    def __init__(self, zone_id=None, marker=None, limit=None, offset=None, line_id=None, tags=None, status=None, type=None, name=None, id=None, sort_key=None, sort_dir=None, search_mode=None):
        """ShowRecordSetByZoneRequest

        The model defined in huaweicloud sdk

        :param zone_id: 所属zone的ID。
        :type zone_id: str
        :param marker: 分页查询起始的资源ID，为空时为查询第一页。  默认值为空。
        :type marker: str
        :param limit: 每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。
        :type limit: int
        :param offset: 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。
        :type offset: int
        :param line_id: 解析线路ID。
        :type line_id: str
        :param tags: 资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用\&quot;|\&quot;分开，每个标签的键值用英文逗号\&quot;,\&quot;相隔。
        :type tags: str
        :param status: 待查询的Record Set的状态。  取值范围：ACTIVE、ERROR、DISABLE、FREEZE、PENDING_CREATE、PENDING_UPDATE、PENDING_DELETE
        :type status: str
        :param type: 待查询的Record Set的记录集类型。  取值范围：A、CNAME、MX、AAAA、TXT、SRV、NS、CAA
        :type type: str
        :param name: 待查询的Record Set的域名中包含此name。  搜索模式默认为模糊搜索。  默认值为空。
        :type name: str
        :param id: 待查询的Record Set的id包含此id。  搜索模式默认为模糊搜索。  默认值为空。
        :type id: str
        :param sort_key: 查询结果中Record Set列表的排序字段。  取值范围：  name：域名 type：记录集类型 默认值为空，表示不排序。
        :type sort_key: str
        :param sort_dir: 查询结果中Record Set列表的排序方式。  取值范围：  desc：降序排序 asc：升序排序 默认值为空，表示不排序。
        :type sort_dir: str
        :param search_mode: 查询条件搜索模式。  取值范围：  like：模糊搜索 equal：精确搜索 默认值为like。
        :type search_mode: str
        """
        
        

        self._zone_id = None
        self._marker = None
        self._limit = None
        self._offset = None
        self._line_id = None
        self._tags = None
        self._status = None
        self._type = None
        self._name = None
        self._id = None
        self._sort_key = None
        self._sort_dir = None
        self._search_mode = None
        self.discriminator = None

        self.zone_id = zone_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if line_id is not None:
            self.line_id = line_id
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
        if search_mode is not None:
            self.search_mode = search_mode

    @property
    def zone_id(self):
        """Gets the zone_id of this ShowRecordSetByZoneRequest.

        所属zone的ID。

        :return: The zone_id of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ShowRecordSetByZoneRequest.

        所属zone的ID。

        :param zone_id: The zone_id of this ShowRecordSetByZoneRequest.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def marker(self):
        """Gets the marker of this ShowRecordSetByZoneRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :return: The marker of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowRecordSetByZoneRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :param marker: The marker of this ShowRecordSetByZoneRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ShowRecordSetByZoneRequest.

        每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :return: The limit of this ShowRecordSetByZoneRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowRecordSetByZoneRequest.

        每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :param limit: The limit of this ShowRecordSetByZoneRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowRecordSetByZoneRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。

        :return: The offset of this ShowRecordSetByZoneRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowRecordSetByZoneRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。

        :param offset: The offset of this ShowRecordSetByZoneRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def line_id(self):
        """Gets the line_id of this ShowRecordSetByZoneRequest.

        解析线路ID。

        :return: The line_id of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this ShowRecordSetByZoneRequest.

        解析线路ID。

        :param line_id: The line_id of this ShowRecordSetByZoneRequest.
        :type line_id: str
        """
        self._line_id = line_id

    @property
    def tags(self):
        """Gets the tags of this ShowRecordSetByZoneRequest.

        资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用\"|\"分开，每个标签的键值用英文逗号\",\"相隔。

        :return: The tags of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowRecordSetByZoneRequest.

        资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用\"|\"分开，每个标签的键值用英文逗号\",\"相隔。

        :param tags: The tags of this ShowRecordSetByZoneRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this ShowRecordSetByZoneRequest.

        待查询的Record Set的状态。  取值范围：ACTIVE、ERROR、DISABLE、FREEZE、PENDING_CREATE、PENDING_UPDATE、PENDING_DELETE

        :return: The status of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowRecordSetByZoneRequest.

        待查询的Record Set的状态。  取值范围：ACTIVE、ERROR、DISABLE、FREEZE、PENDING_CREATE、PENDING_UPDATE、PENDING_DELETE

        :param status: The status of this ShowRecordSetByZoneRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ShowRecordSetByZoneRequest.

        待查询的Record Set的记录集类型。  取值范围：A、CNAME、MX、AAAA、TXT、SRV、NS、CAA

        :return: The type of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowRecordSetByZoneRequest.

        待查询的Record Set的记录集类型。  取值范围：A、CNAME、MX、AAAA、TXT、SRV、NS、CAA

        :param type: The type of this ShowRecordSetByZoneRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ShowRecordSetByZoneRequest.

        待查询的Record Set的域名中包含此name。  搜索模式默认为模糊搜索。  默认值为空。

        :return: The name of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowRecordSetByZoneRequest.

        待查询的Record Set的域名中包含此name。  搜索模式默认为模糊搜索。  默认值为空。

        :param name: The name of this ShowRecordSetByZoneRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ShowRecordSetByZoneRequest.

        待查询的Record Set的id包含此id。  搜索模式默认为模糊搜索。  默认值为空。

        :return: The id of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowRecordSetByZoneRequest.

        待查询的Record Set的id包含此id。  搜索模式默认为模糊搜索。  默认值为空。

        :param id: The id of this ShowRecordSetByZoneRequest.
        :type id: str
        """
        self._id = id

    @property
    def sort_key(self):
        """Gets the sort_key of this ShowRecordSetByZoneRequest.

        查询结果中Record Set列表的排序字段。  取值范围：  name：域名 type：记录集类型 默认值为空，表示不排序。

        :return: The sort_key of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ShowRecordSetByZoneRequest.

        查询结果中Record Set列表的排序字段。  取值范围：  name：域名 type：记录集类型 默认值为空，表示不排序。

        :param sort_key: The sort_key of this ShowRecordSetByZoneRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ShowRecordSetByZoneRequest.

        查询结果中Record Set列表的排序方式。  取值范围：  desc：降序排序 asc：升序排序 默认值为空，表示不排序。

        :return: The sort_dir of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ShowRecordSetByZoneRequest.

        查询结果中Record Set列表的排序方式。  取值范围：  desc：降序排序 asc：升序排序 默认值为空，表示不排序。

        :param sort_dir: The sort_dir of this ShowRecordSetByZoneRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def search_mode(self):
        """Gets the search_mode of this ShowRecordSetByZoneRequest.

        查询条件搜索模式。  取值范围：  like：模糊搜索 equal：精确搜索 默认值为like。

        :return: The search_mode of this ShowRecordSetByZoneRequest.
        :rtype: str
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        """Sets the search_mode of this ShowRecordSetByZoneRequest.

        查询条件搜索模式。  取值范围：  like：模糊搜索 equal：精确搜索 默认值为like。

        :param search_mode: The search_mode of this ShowRecordSetByZoneRequest.
        :type search_mode: str
        """
        self._search_mode = search_mode

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
        if not isinstance(other, ShowRecordSetByZoneRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
