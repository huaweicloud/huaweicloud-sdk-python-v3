# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpsWhiteListsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'total': 'int',
        'records': 'list[IpsWhiteListVO]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'total': 'total',
        'records': 'records'
    }

    def __init__(self, limit=None, offset=None, total=None, records=None):
        r"""ListIpsWhiteListsVO

        The model defined in huaweicloud sdk

        :param limit: **参数解释**：  每页数量 **取值范围**： 不涉及
        :type limit: int
        :param offset: **参数解释**：  偏移量 **取值范围**： 不涉及
        :type offset: int
        :param total: **参数解释**：  总数 **取值范围**： 不涉及
        :type total: int
        :param records: **参数解释**：  IPS白名单列表 **取值范围**： 不涉及
        :type records: list[:class:`huaweicloudsdkcfw.v1.IpsWhiteListVO`]
        """
        
        

        self._limit = None
        self._offset = None
        self._total = None
        self._records = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total
        if records is not None:
            self.records = records

    @property
    def limit(self):
        r"""Gets the limit of this ListIpsWhiteListsVO.

        **参数解释**：  每页数量 **取值范围**： 不涉及

        :return: The limit of this ListIpsWhiteListsVO.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIpsWhiteListsVO.

        **参数解释**：  每页数量 **取值范围**： 不涉及

        :param limit: The limit of this ListIpsWhiteListsVO.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListIpsWhiteListsVO.

        **参数解释**：  偏移量 **取值范围**： 不涉及

        :return: The offset of this ListIpsWhiteListsVO.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIpsWhiteListsVO.

        **参数解释**：  偏移量 **取值范围**： 不涉及

        :param offset: The offset of this ListIpsWhiteListsVO.
        :type offset: int
        """
        self._offset = offset

    @property
    def total(self):
        r"""Gets the total of this ListIpsWhiteListsVO.

        **参数解释**：  总数 **取值范围**： 不涉及

        :return: The total of this ListIpsWhiteListsVO.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListIpsWhiteListsVO.

        **参数解释**：  总数 **取值范围**： 不涉及

        :param total: The total of this ListIpsWhiteListsVO.
        :type total: int
        """
        self._total = total

    @property
    def records(self):
        r"""Gets the records of this ListIpsWhiteListsVO.

        **参数解释**：  IPS白名单列表 **取值范围**： 不涉及

        :return: The records of this ListIpsWhiteListsVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.IpsWhiteListVO`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListIpsWhiteListsVO.

        **参数解释**：  IPS白名单列表 **取值范围**： 不涉及

        :param records: The records of this ListIpsWhiteListsVO.
        :type records: list[:class:`huaweicloudsdkcfw.v1.IpsWhiteListVO`]
        """
        self._records = records

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
        if not isinstance(other, ListIpsWhiteListsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
