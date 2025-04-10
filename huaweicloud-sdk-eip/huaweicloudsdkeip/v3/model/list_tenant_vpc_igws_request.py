# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantVpcIgwsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[str]',
        'id': 'str',
        'vpc_id': 'str',
        'name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'id': 'id',
        'vpc_id': 'vpc_id',
        'name': 'name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker'
    }

    def __init__(self, fields=None, id=None, vpc_id=None, name=None, sort_key=None, sort_dir=None, limit=None, offset=None, marker=None):
        r"""ListTenantVpcIgwsRequest

        The model defined in huaweicloud sdk

        :param fields: 形式为\\\&quot;fields&#x3D;id&amp;fields&#x3D;project_id&amp;...\\\&quot;，支持字段：id/project_id/vpc_id/created_at/updated_at/name
        :type fields: list[str]
        :param id: 虚拟IGW的uuid
        :type id: str
        :param vpc_id: 虚拟igw所在的vpcid
        :type vpc_id: str
        :param name: 虚拟igw的名称
        :type name: str
        :param sort_key: 排序，形式为\&quot;sort_key&#x3D;i2a_id&amp;sort_dir&#x3D;asc\&quot;  支持字段：id/created_at/updated_at
        :type sort_key: str
        :param sort_dir: 排序方向  取值范围：asc、desc
        :type sort_dir: str
        :param limit: 每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定
        :type limit: int
        :param offset: 分页起始点
        :type offset: int
        :param marker: 分页起始点
        :type marker: str
        """
        
        

        self._fields = None
        self._id = None
        self._vpc_id = None
        self._name = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._marker = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if id is not None:
            self.id = id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if name is not None:
            self.name = name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker

    @property
    def fields(self):
        r"""Gets the fields of this ListTenantVpcIgwsRequest.

        形式为\\\"fields=id&fields=project_id&...\\\"，支持字段：id/project_id/vpc_id/created_at/updated_at/name

        :return: The fields of this ListTenantVpcIgwsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListTenantVpcIgwsRequest.

        形式为\\\"fields=id&fields=project_id&...\\\"，支持字段：id/project_id/vpc_id/created_at/updated_at/name

        :param fields: The fields of this ListTenantVpcIgwsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def id(self):
        r"""Gets the id of this ListTenantVpcIgwsRequest.

        虚拟IGW的uuid

        :return: The id of this ListTenantVpcIgwsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListTenantVpcIgwsRequest.

        虚拟IGW的uuid

        :param id: The id of this ListTenantVpcIgwsRequest.
        :type id: str
        """
        self._id = id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListTenantVpcIgwsRequest.

        虚拟igw所在的vpcid

        :return: The vpc_id of this ListTenantVpcIgwsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListTenantVpcIgwsRequest.

        虚拟igw所在的vpcid

        :param vpc_id: The vpc_id of this ListTenantVpcIgwsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def name(self):
        r"""Gets the name of this ListTenantVpcIgwsRequest.

        虚拟igw的名称

        :return: The name of this ListTenantVpcIgwsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTenantVpcIgwsRequest.

        虚拟igw的名称

        :param name: The name of this ListTenantVpcIgwsRequest.
        :type name: str
        """
        self._name = name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListTenantVpcIgwsRequest.

        排序，形式为\"sort_key=i2a_id&sort_dir=asc\"  支持字段：id/created_at/updated_at

        :return: The sort_key of this ListTenantVpcIgwsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListTenantVpcIgwsRequest.

        排序，形式为\"sort_key=i2a_id&sort_dir=asc\"  支持字段：id/created_at/updated_at

        :param sort_key: The sort_key of this ListTenantVpcIgwsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListTenantVpcIgwsRequest.

        排序方向  取值范围：asc、desc

        :return: The sort_dir of this ListTenantVpcIgwsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListTenantVpcIgwsRequest.

        排序方向  取值范围：asc、desc

        :param sort_dir: The sort_dir of this ListTenantVpcIgwsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListTenantVpcIgwsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :return: The limit of this ListTenantVpcIgwsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTenantVpcIgwsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :param limit: The limit of this ListTenantVpcIgwsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTenantVpcIgwsRequest.

        分页起始点

        :return: The offset of this ListTenantVpcIgwsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTenantVpcIgwsRequest.

        分页起始点

        :param offset: The offset of this ListTenantVpcIgwsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListTenantVpcIgwsRequest.

        分页起始点

        :return: The marker of this ListTenantVpcIgwsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTenantVpcIgwsRequest.

        分页起始点

        :param marker: The marker of this ListTenantVpcIgwsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListTenantVpcIgwsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
