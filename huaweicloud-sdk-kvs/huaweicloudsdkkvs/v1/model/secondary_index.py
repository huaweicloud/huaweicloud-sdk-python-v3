# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecondaryIndex:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_name': 'str',
        'sort_key_fields': 'list[Field]',
        'abstract_fields': 'list[str]'
    }

    attribute_map = {
        'index_name': 'index_name',
        'sort_key_fields': 'sort_key_fields',
        'abstract_fields': 'abstract_fields'
    }

    def __init__(self, index_name=None, sort_key_fields=None, abstract_fields=None):
        r"""SecondaryIndex

        The model defined in huaweicloud sdk

        :param index_name: 二级索引名称，表内唯一。
        :type index_name: str
        :param sort_key_fields: 排序键字段名数组，顺序组合。
        :type sort_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        :param abstract_fields: 摘要字段名数组。
        :type abstract_fields: list[str]
        """
        
        

        self._index_name = None
        self._sort_key_fields = None
        self._abstract_fields = None
        self.discriminator = None

        self.index_name = index_name
        self.sort_key_fields = sort_key_fields
        if abstract_fields is not None:
            self.abstract_fields = abstract_fields

    @property
    def index_name(self):
        r"""Gets the index_name of this SecondaryIndex.

        二级索引名称，表内唯一。

        :return: The index_name of this SecondaryIndex.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this SecondaryIndex.

        二级索引名称，表内唯一。

        :param index_name: The index_name of this SecondaryIndex.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def sort_key_fields(self):
        r"""Gets the sort_key_fields of this SecondaryIndex.

        排序键字段名数组，顺序组合。

        :return: The sort_key_fields of this SecondaryIndex.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        return self._sort_key_fields

    @sort_key_fields.setter
    def sort_key_fields(self, sort_key_fields):
        r"""Sets the sort_key_fields of this SecondaryIndex.

        排序键字段名数组，顺序组合。

        :param sort_key_fields: The sort_key_fields of this SecondaryIndex.
        :type sort_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        self._sort_key_fields = sort_key_fields

    @property
    def abstract_fields(self):
        r"""Gets the abstract_fields of this SecondaryIndex.

        摘要字段名数组。

        :return: The abstract_fields of this SecondaryIndex.
        :rtype: list[str]
        """
        return self._abstract_fields

    @abstract_fields.setter
    def abstract_fields(self, abstract_fields):
        r"""Sets the abstract_fields of this SecondaryIndex.

        摘要字段名数组。

        :param abstract_fields: The abstract_fields of this SecondaryIndex.
        :type abstract_fields: list[str]
        """
        self._abstract_fields = abstract_fields

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
        if not isinstance(other, SecondaryIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
