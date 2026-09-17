# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlanListResponsePage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'size': 'int',
        'count': 'int'
    }

    attribute_map = {
        'page': 'page',
        'size': 'size',
        'count': 'count'
    }

    def __init__(self, page=None, size=None, count=None):
        r"""PlanListResponsePage

        The model defined in huaweicloud sdk

        :param page: **参数解释：** 页码 **取值范围：** 不涉及
        :type page: int
        :param size: **参数解释：** 分页数量 **取值范围：** 不涉及
        :type size: int
        :param count: **参数解释：** 当前页数量 **取值范围：** 不涉及
        :type count: int
        """
        
        

        self._page = None
        self._size = None
        self._count = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if count is not None:
            self.count = count

    @property
    def page(self):
        r"""Gets the page of this PlanListResponsePage.

        **参数解释：** 页码 **取值范围：** 不涉及

        :return: The page of this PlanListResponsePage.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this PlanListResponsePage.

        **参数解释：** 页码 **取值范围：** 不涉及

        :param page: The page of this PlanListResponsePage.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this PlanListResponsePage.

        **参数解释：** 分页数量 **取值范围：** 不涉及

        :return: The size of this PlanListResponsePage.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PlanListResponsePage.

        **参数解释：** 分页数量 **取值范围：** 不涉及

        :param size: The size of this PlanListResponsePage.
        :type size: int
        """
        self._size = size

    @property
    def count(self):
        r"""Gets the count of this PlanListResponsePage.

        **参数解释：** 当前页数量 **取值范围：** 不涉及

        :return: The count of this PlanListResponsePage.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PlanListResponsePage.

        **参数解释：** 当前页数量 **取值范围：** 不涉及

        :param count: The count of this PlanListResponsePage.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, PlanListResponsePage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
