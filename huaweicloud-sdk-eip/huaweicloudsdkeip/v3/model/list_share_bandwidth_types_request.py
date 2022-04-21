# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareBandwidthTypesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'fields': 'str',
        'id': 'str',
        'bandwidth_type': 'str',
        'name_en': 'str',
        'name_zh': 'str',
        'public_border_group': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'fields': 'fields',
        'id': 'id',
        'bandwidth_type': 'bandwidth_type',
        'name_en': 'name_en',
        'name_zh': 'name_zh',
        'public_border_group': 'public_border_group',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit'
    }

    def __init__(self, fields=None, id=None, bandwidth_type=None, name_en=None, name_zh=None, public_border_group=None, sort_key=None, sort_dir=None, limit=None):
        """ListShareBandwidthTypesRequest

        The model defined in huaweicloud sdk

        :param fields: 形式为\\\&quot;fields&#x3D;id&amp;fields&#x3D;bandwidth_type&amp;...\\\&quot;，支持字段：id/bandwidth_type/name_en/name_zh/created_at/update_at/public_border_group/description
        :type fields: str
        :param id: 支持带宽类型的id
        :type id: str
        :param bandwidth_type: 带宽支持类型
        :type bandwidth_type: str
        :param name_en: 带宽类型英文表述
        :type name_en: str
        :param name_zh: 带宽类型中文表述
        :type name_zh: str
        :param public_border_group: 带宽类型所处位置，中心站点or边缘站点
        :type public_border_group: str
        :param sort_key: 排序，形式为\&quot;sort_key&#x3D;id&amp;sort_dir&#x3D;asc\&quot;  支持字段：id/bandwidth_type/public_border_group
        :type sort_key: str
        :param sort_dir: 排序方向  取值范围：asc、desc
        :type sort_dir: str
        :param limit: 每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定
        :type limit: int
        """
        
        

        self._fields = None
        self._id = None
        self._bandwidth_type = None
        self._name_en = None
        self._name_zh = None
        self._public_border_group = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if id is not None:
            self.id = id
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if name_en is not None:
            self.name_en = name_en
        if name_zh is not None:
            self.name_zh = name_zh
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit

    @property
    def fields(self):
        """Gets the fields of this ListShareBandwidthTypesRequest.

        形式为\\\"fields=id&fields=bandwidth_type&...\\\"，支持字段：id/bandwidth_type/name_en/name_zh/created_at/update_at/public_border_group/description

        :return: The fields of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListShareBandwidthTypesRequest.

        形式为\\\"fields=id&fields=bandwidth_type&...\\\"，支持字段：id/bandwidth_type/name_en/name_zh/created_at/update_at/public_border_group/description

        :param fields: The fields of this ListShareBandwidthTypesRequest.
        :type fields: str
        """
        self._fields = fields

    @property
    def id(self):
        """Gets the id of this ListShareBandwidthTypesRequest.

        支持带宽类型的id

        :return: The id of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListShareBandwidthTypesRequest.

        支持带宽类型的id

        :param id: The id of this ListShareBandwidthTypesRequest.
        :type id: str
        """
        self._id = id

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this ListShareBandwidthTypesRequest.

        带宽支持类型

        :return: The bandwidth_type of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this ListShareBandwidthTypesRequest.

        带宽支持类型

        :param bandwidth_type: The bandwidth_type of this ListShareBandwidthTypesRequest.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def name_en(self):
        """Gets the name_en of this ListShareBandwidthTypesRequest.

        带宽类型英文表述

        :return: The name_en of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this ListShareBandwidthTypesRequest.

        带宽类型英文表述

        :param name_en: The name_en of this ListShareBandwidthTypesRequest.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_zh(self):
        """Gets the name_zh of this ListShareBandwidthTypesRequest.

        带宽类型中文表述

        :return: The name_zh of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        """Sets the name_zh of this ListShareBandwidthTypesRequest.

        带宽类型中文表述

        :param name_zh: The name_zh of this ListShareBandwidthTypesRequest.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListShareBandwidthTypesRequest.

        带宽类型所处位置，中心站点or边缘站点

        :return: The public_border_group of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListShareBandwidthTypesRequest.

        带宽类型所处位置，中心站点or边缘站点

        :param public_border_group: The public_border_group of this ListShareBandwidthTypesRequest.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def sort_key(self):
        """Gets the sort_key of this ListShareBandwidthTypesRequest.

        排序，形式为\"sort_key=id&sort_dir=asc\"  支持字段：id/bandwidth_type/public_border_group

        :return: The sort_key of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListShareBandwidthTypesRequest.

        排序，形式为\"sort_key=id&sort_dir=asc\"  支持字段：id/bandwidth_type/public_border_group

        :param sort_key: The sort_key of this ListShareBandwidthTypesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListShareBandwidthTypesRequest.

        排序方向  取值范围：asc、desc

        :return: The sort_dir of this ListShareBandwidthTypesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListShareBandwidthTypesRequest.

        排序方向  取值范围：asc、desc

        :param sort_dir: The sort_dir of this ListShareBandwidthTypesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListShareBandwidthTypesRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :return: The limit of this ListShareBandwidthTypesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListShareBandwidthTypesRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :param limit: The limit of this ListShareBandwidthTypesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListShareBandwidthTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
