# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrimaryKeySchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shard_key_fields': 'list[Field]',
        'shard_mode': 'str',
        'sort_key_fields': 'list[Field]'
    }

    attribute_map = {
        'shard_key_fields': 'shard_key_fields',
        'shard_mode': 'shard_mode',
        'sort_key_fields': 'sort_key_fields'
    }

    def __init__(self, shard_key_fields=None, shard_mode=None, sort_key_fields=None):
        r"""PrimaryKeySchema

        The model defined in huaweicloud sdk

        :param shard_key_fields: 分区键字段名数组，顺序组合。
        :type shard_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        :param shard_mode: 分区模式。
        :type shard_mode: str
        :param sort_key_fields: 排序键字段名数组，顺序组合。
        :type sort_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        
        

        self._shard_key_fields = None
        self._shard_mode = None
        self._sort_key_fields = None
        self.discriminator = None

        self.shard_key_fields = shard_key_fields
        if shard_mode is not None:
            self.shard_mode = shard_mode
        if sort_key_fields is not None:
            self.sort_key_fields = sort_key_fields

    @property
    def shard_key_fields(self):
        r"""Gets the shard_key_fields of this PrimaryKeySchema.

        分区键字段名数组，顺序组合。

        :return: The shard_key_fields of this PrimaryKeySchema.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        return self._shard_key_fields

    @shard_key_fields.setter
    def shard_key_fields(self, shard_key_fields):
        r"""Sets the shard_key_fields of this PrimaryKeySchema.

        分区键字段名数组，顺序组合。

        :param shard_key_fields: The shard_key_fields of this PrimaryKeySchema.
        :type shard_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        self._shard_key_fields = shard_key_fields

    @property
    def shard_mode(self):
        r"""Gets the shard_mode of this PrimaryKeySchema.

        分区模式。

        :return: The shard_mode of this PrimaryKeySchema.
        :rtype: str
        """
        return self._shard_mode

    @shard_mode.setter
    def shard_mode(self, shard_mode):
        r"""Sets the shard_mode of this PrimaryKeySchema.

        分区模式。

        :param shard_mode: The shard_mode of this PrimaryKeySchema.
        :type shard_mode: str
        """
        self._shard_mode = shard_mode

    @property
    def sort_key_fields(self):
        r"""Gets the sort_key_fields of this PrimaryKeySchema.

        排序键字段名数组，顺序组合。

        :return: The sort_key_fields of this PrimaryKeySchema.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        return self._sort_key_fields

    @sort_key_fields.setter
    def sort_key_fields(self, sort_key_fields):
        r"""Sets the sort_key_fields of this PrimaryKeySchema.

        排序键字段名数组，顺序组合。

        :param sort_key_fields: The sort_key_fields of this PrimaryKeySchema.
        :type sort_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        self._sort_key_fields = sort_key_fields

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
        if not isinstance(other, PrimaryKeySchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
