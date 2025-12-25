# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttentionPageResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_records': 'int',
        'total_pages': 'int',
        'data': 'list[ListAttentionResult]'
    }

    attribute_map = {
        'total_records': 'totalRecords',
        'total_pages': 'totalPages',
        'data': 'data'
    }

    def __init__(self, total_records=None, total_pages=None, data=None):
        r"""ListAttentionPageResult

        The model defined in huaweicloud sdk

        :param total_records: **参数解释**： 总记录数。 **取值范围**： 不涉及。 
        :type total_records: int
        :param total_pages: **参数解释**： 总页数。 **取值范围**： 不涉及。 
        :type total_pages: int
        :param data: **参数解释**： 关注列表。 **取值范围**： 不涉及。 
        :type data: list[:class:`huaweicloudsdkcodeartsartifact.v2.ListAttentionResult`]
        """
        
        

        self._total_records = None
        self._total_pages = None
        self._data = None
        self.discriminator = None

        if total_records is not None:
            self.total_records = total_records
        if total_pages is not None:
            self.total_pages = total_pages
        if data is not None:
            self.data = data

    @property
    def total_records(self):
        r"""Gets the total_records of this ListAttentionPageResult.

        **参数解释**： 总记录数。 **取值范围**： 不涉及。 

        :return: The total_records of this ListAttentionPageResult.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        r"""Sets the total_records of this ListAttentionPageResult.

        **参数解释**： 总记录数。 **取值范围**： 不涉及。 

        :param total_records: The total_records of this ListAttentionPageResult.
        :type total_records: int
        """
        self._total_records = total_records

    @property
    def total_pages(self):
        r"""Gets the total_pages of this ListAttentionPageResult.

        **参数解释**： 总页数。 **取值范围**： 不涉及。 

        :return: The total_pages of this ListAttentionPageResult.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        r"""Sets the total_pages of this ListAttentionPageResult.

        **参数解释**： 总页数。 **取值范围**： 不涉及。 

        :param total_pages: The total_pages of this ListAttentionPageResult.
        :type total_pages: int
        """
        self._total_pages = total_pages

    @property
    def data(self):
        r"""Gets the data of this ListAttentionPageResult.

        **参数解释**： 关注列表。 **取值范围**： 不涉及。 

        :return: The data of this ListAttentionPageResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.ListAttentionResult`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListAttentionPageResult.

        **参数解释**： 关注列表。 **取值范围**： 不涉及。 

        :param data: The data of this ListAttentionPageResult.
        :type data: list[:class:`huaweicloudsdkcodeartsartifact.v2.ListAttentionResult`]
        """
        self._data = data

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
        if not isinstance(other, ListAttentionPageResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
