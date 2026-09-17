# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCacheDatasResposeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[FieldVO]',
        'visible_fields': 'list[FieldVO]'
    }

    attribute_map = {
        'fields': 'fields',
        'visible_fields': 'visibleFields'
    }

    def __init__(self, fields=None, visible_fields=None):
        r"""ListCacheDatasResposeResult

        The model defined in huaweicloud sdk

        :param fields: **参数解释：** 全部字段。
        :type fields: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        :param visible_fields: **参数解释：** 表头显示字段。
        :type visible_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        
        

        self._fields = None
        self._visible_fields = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if visible_fields is not None:
            self.visible_fields = visible_fields

    @property
    def fields(self):
        r"""Gets the fields of this ListCacheDatasResposeResult.

        **参数解释：** 全部字段。

        :return: The fields of this ListCacheDatasResposeResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListCacheDatasResposeResult.

        **参数解释：** 全部字段。

        :param fields: The fields of this ListCacheDatasResposeResult.
        :type fields: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        self._fields = fields

    @property
    def visible_fields(self):
        r"""Gets the visible_fields of this ListCacheDatasResposeResult.

        **参数解释：** 表头显示字段。

        :return: The visible_fields of this ListCacheDatasResposeResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        return self._visible_fields

    @visible_fields.setter
    def visible_fields(self, visible_fields):
        r"""Sets the visible_fields of this ListCacheDatasResposeResult.

        **参数解释：** 表头显示字段。

        :param visible_fields: The visible_fields of this ListCacheDatasResposeResult.
        :type visible_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        self._visible_fields = visible_fields

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCacheDatasResposeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
