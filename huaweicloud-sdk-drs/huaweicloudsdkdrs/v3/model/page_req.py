# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cur_page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, cur_page=None, per_page=None):
        r"""PageReq

        The model defined in huaweicloud sdk

        :param cur_page: **参数解释**：  当前页码，用于分页查询时指定返回第几页的数据。填0可获取全部数据项。  **约束限制**：  - 当per_page填0时，cur_page只能填0或1。 - 不能超过传入jobID数量除每页任务数量的最大页。  **取值范围**：  不涉及。  **默认取值**：  1
        :type cur_page: int
        :param per_page: **参数解释**：  每页返回的记录数，用于分页查询时控制每页数据量。填0可获取全部数据项。  **约束限制**：  - 填0时，cur_page只能填0或1。  **取值范围**：  0-100。  **默认取值**：  5
        :type per_page: int
        """
        
        

        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def cur_page(self):
        r"""Gets the cur_page of this PageReq.

        **参数解释**：  当前页码，用于分页查询时指定返回第几页的数据。填0可获取全部数据项。  **约束限制**：  - 当per_page填0时，cur_page只能填0或1。 - 不能超过传入jobID数量除每页任务数量的最大页。  **取值范围**：  不涉及。  **默认取值**：  1

        :return: The cur_page of this PageReq.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this PageReq.

        **参数解释**：  当前页码，用于分页查询时指定返回第几页的数据。填0可获取全部数据项。  **约束限制**：  - 当per_page填0时，cur_page只能填0或1。 - 不能超过传入jobID数量除每页任务数量的最大页。  **取值范围**：  不涉及。  **默认取值**：  1

        :param cur_page: The cur_page of this PageReq.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this PageReq.

        **参数解释**：  每页返回的记录数，用于分页查询时控制每页数据量。填0可获取全部数据项。  **约束限制**：  - 填0时，cur_page只能填0或1。  **取值范围**：  0-100。  **默认取值**：  5

        :return: The per_page of this PageReq.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this PageReq.

        **参数解释**：  每页返回的记录数，用于分页查询时控制每页数据量。填0可获取全部数据项。  **约束限制**：  - 填0时，cur_page只能填0或1。  **取值范围**：  0-100。  **默认取值**：  5

        :param per_page: The per_page of this PageReq.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, PageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
