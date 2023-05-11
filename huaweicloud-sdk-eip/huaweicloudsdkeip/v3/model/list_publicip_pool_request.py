# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicipPoolRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'fields': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'id': 'str',
        'name': 'str',
        'size': 'int',
        'status': 'str',
        'type': 'str',
        'description': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'fields': 'fields',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'size': 'size',
        'status': 'status',
        'type': 'type',
        'description': 'description',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, marker=None, limit=None, fields=None, sort_key=None, sort_dir=None, id=None, name=None, size=None, status=None, type=None, description=None, public_border_group=None):
        """ListPublicipPoolRequest

        The model defined in huaweicloud sdk

        :param marker: 分页查询起始的资源ID，为空时为查询第一页
        :type marker: str
        :param limit: 每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定
        :type limit: int
        :param fields: 显示，形式为\&quot;fields&#x3D;id&amp;fields&#x3D;name&amp;...\&quot;  支持字段：id/name/size/used/project_id/status/billing_info/created_at/updated_at/type/shared/is_common/description/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group
        :type fields: str
        :param sort_key: 排序，形式为\&quot;sort_key&#x3D;id&amp;sort_dir&#x3D;asc\&quot;  支持字段：id/name/created_at/updated_at/public_border_group
        :type sort_key: str
        :param sort_dir: 排序方向  取值范围：asc、desc
        :type sort_dir: str
        :param id: 根据id过滤
        :type id: str
        :param name: 根据name过滤
        :type name: str
        :param size: 根据size过滤
        :type size: int
        :param status: 根据status过滤
        :type status: str
        :param type: 根据type过滤
        :type type: str
        :param description: 根据description过滤
        :type description: str
        :param public_border_group: 根据public_border_group过滤
        :type public_border_group: str
        """
        
        

        self._marker = None
        self._limit = None
        self._fields = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
        self._size = None
        self._status = None
        self._type = None
        self._description = None
        self._public_border_group = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if fields is not None:
            self.fields = fields
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def marker(self):
        """Gets the marker of this ListPublicipPoolRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :return: The marker of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPublicipPoolRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :param marker: The marker of this ListPublicipPoolRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListPublicipPoolRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :return: The limit of this ListPublicipPoolRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublicipPoolRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :param limit: The limit of this ListPublicipPoolRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fields(self):
        """Gets the fields of this ListPublicipPoolRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：id/name/size/used/project_id/status/billing_info/created_at/updated_at/type/shared/is_common/description/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group

        :return: The fields of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListPublicipPoolRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：id/name/size/used/project_id/status/billing_info/created_at/updated_at/type/shared/is_common/description/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group

        :param fields: The fields of this ListPublicipPoolRequest.
        :type fields: str
        """
        self._fields = fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListPublicipPoolRequest.

        排序，形式为\"sort_key=id&sort_dir=asc\"  支持字段：id/name/created_at/updated_at/public_border_group

        :return: The sort_key of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListPublicipPoolRequest.

        排序，形式为\"sort_key=id&sort_dir=asc\"  支持字段：id/name/created_at/updated_at/public_border_group

        :param sort_key: The sort_key of this ListPublicipPoolRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListPublicipPoolRequest.

        排序方向  取值范围：asc、desc

        :return: The sort_dir of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListPublicipPoolRequest.

        排序方向  取值范围：asc、desc

        :param sort_dir: The sort_dir of this ListPublicipPoolRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListPublicipPoolRequest.

        根据id过滤

        :return: The id of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPublicipPoolRequest.

        根据id过滤

        :param id: The id of this ListPublicipPoolRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListPublicipPoolRequest.

        根据name过滤

        :return: The name of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPublicipPoolRequest.

        根据name过滤

        :param name: The name of this ListPublicipPoolRequest.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this ListPublicipPoolRequest.

        根据size过滤

        :return: The size of this ListPublicipPoolRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListPublicipPoolRequest.

        根据size过滤

        :param size: The size of this ListPublicipPoolRequest.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this ListPublicipPoolRequest.

        根据status过滤

        :return: The status of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPublicipPoolRequest.

        根据status过滤

        :param status: The status of this ListPublicipPoolRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListPublicipPoolRequest.

        根据type过滤

        :return: The type of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPublicipPoolRequest.

        根据type过滤

        :param type: The type of this ListPublicipPoolRequest.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this ListPublicipPoolRequest.

        根据description过滤

        :return: The description of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPublicipPoolRequest.

        根据description过滤

        :param description: The description of this ListPublicipPoolRequest.
        :type description: str
        """
        self._description = description

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListPublicipPoolRequest.

        根据public_border_group过滤

        :return: The public_border_group of this ListPublicipPoolRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListPublicipPoolRequest.

        根据public_border_group过滤

        :param public_border_group: The public_border_group of this ListPublicipPoolRequest.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, ListPublicipPoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
