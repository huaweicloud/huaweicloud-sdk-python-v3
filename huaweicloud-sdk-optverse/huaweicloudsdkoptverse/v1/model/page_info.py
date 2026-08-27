# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'page_size': 'page_size',
        'total': 'total'
    }

    def __init__(self, offset=None, page_size=None, total=None):
        r"""PageInfo

        The model defined in huaweicloud sdk

        :param offset: **参数解释**： 偏移量。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 不涉及 
        :type offset: int
        :param page_size: **参数解释**： 每条页数。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,10000]。 **默认取值**： 不涉及 
        :type page_size: int
        :param total: **参数解释**： 总条目数。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 不涉及 
        :type total: int
        """
        
        

        self._offset = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def offset(self):
        r"""Gets the offset of this PageInfo.

        **参数解释**： 偏移量。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 不涉及 

        :return: The offset of this PageInfo.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this PageInfo.

        **参数解释**： 偏移量。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 不涉及 

        :param offset: The offset of this PageInfo.
        :type offset: int
        """
        self._offset = offset

    @property
    def page_size(self):
        r"""Gets the page_size of this PageInfo.

        **参数解释**： 每条页数。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,10000]。 **默认取值**： 不涉及 

        :return: The page_size of this PageInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this PageInfo.

        **参数解释**： 每条页数。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,10000]。 **默认取值**： 不涉及 

        :param page_size: The page_size of this PageInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total(self):
        r"""Gets the total of this PageInfo.

        **参数解释**： 总条目数。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 不涉及 

        :return: The total of this PageInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this PageInfo.

        **参数解释**： 总条目数。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 不涉及 

        :param total: The total of this PageInfo.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, PageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
