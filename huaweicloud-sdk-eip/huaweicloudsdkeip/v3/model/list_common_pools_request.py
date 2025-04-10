# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommonPoolsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, fields=None, limit=None, offset=None, name=None, public_border_group=None):
        r"""ListCommonPoolsRequest

        The model defined in huaweicloud sdk

        :param fields: 显示，形式为\&quot;fields&#x3D;id&amp;fields&#x3D;name&amp;...\&quot;  支持字段：id/name/status/type/used/allow_share_bandwidth_types/public_border_group/description
        :type fields: list[str]
        :param limit: 每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定
        :type limit: int
        :param offset: 分页查询起始的资源序号
        :type offset: int
        :param name: 公共池名称
        :type name: str
        :param public_border_group: 公共池位于中心还是边缘
        :type public_border_group: str
        """
        
        

        self._fields = None
        self._limit = None
        self._offset = None
        self._name = None
        self._public_border_group = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def fields(self):
        r"""Gets the fields of this ListCommonPoolsRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：id/name/status/type/used/allow_share_bandwidth_types/public_border_group/description

        :return: The fields of this ListCommonPoolsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListCommonPoolsRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：id/name/status/type/used/allow_share_bandwidth_types/public_border_group/description

        :param fields: The fields of this ListCommonPoolsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def limit(self):
        r"""Gets the limit of this ListCommonPoolsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :return: The limit of this ListCommonPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCommonPoolsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :param limit: The limit of this ListCommonPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCommonPoolsRequest.

        分页查询起始的资源序号

        :return: The offset of this ListCommonPoolsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCommonPoolsRequest.

        分页查询起始的资源序号

        :param offset: The offset of this ListCommonPoolsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListCommonPoolsRequest.

        公共池名称

        :return: The name of this ListCommonPoolsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCommonPoolsRequest.

        公共池名称

        :param name: The name of this ListCommonPoolsRequest.
        :type name: str
        """
        self._name = name

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ListCommonPoolsRequest.

        公共池位于中心还是边缘

        :return: The public_border_group of this ListCommonPoolsRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ListCommonPoolsRequest.

        公共池位于中心还是边缘

        :param public_border_group: The public_border_group of this ListCommonPoolsRequest.
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
        if not isinstance(other, ListCommonPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
