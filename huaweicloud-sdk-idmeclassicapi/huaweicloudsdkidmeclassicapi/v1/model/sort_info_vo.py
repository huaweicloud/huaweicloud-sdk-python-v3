# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SortInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'character_set': 'CharacterSetEnum',
        'order_by': 'str',
        'sort': 'str',
        'sort_info': 'str',
        'sort_info_order_by': 'str'
    }

    attribute_map = {
        'character_set': 'characterSet',
        'order_by': 'orderBy',
        'sort': 'sort',
        'sort_info': 'sortInfo',
        'sort_info_order_by': 'sortInfoOrderBy'
    }

    def __init__(self, character_set=None, order_by=None, sort=None, sort_info=None, sort_info_order_by=None):
        r"""SortInfoVo

        The model defined in huaweicloud sdk

        :param character_set: 
        :type character_set: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        :param order_by: **参数解释：**  按某个字段进行排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type order_by: str
        :param sort: **参数解释：**  排序方向。  **约束限制：**  不涉及。  **取值范围：**  - ASC：表示升序。 - DESC：表示降序。  **默认取值：**  ASC。 
        :type sort: str
        :param sort_info: **参数解释：**  排序信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type sort_info: str
        :param sort_info_order_by: **参数解释：**  排序信息字段。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type sort_info_order_by: str
        """
        
        

        self._character_set = None
        self._order_by = None
        self._sort = None
        self._sort_info = None
        self._sort_info_order_by = None
        self.discriminator = None

        if character_set is not None:
            self.character_set = character_set
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if sort_info is not None:
            self.sort_info = sort_info
        if sort_info_order_by is not None:
            self.sort_info_order_by = sort_info_order_by

    @property
    def character_set(self):
        r"""Gets the character_set of this SortInfoVo.

        :return: The character_set of this SortInfoVo.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        r"""Sets the character_set of this SortInfoVo.

        :param character_set: The character_set of this SortInfoVo.
        :type character_set: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        """
        self._character_set = character_set

    @property
    def order_by(self):
        r"""Gets the order_by of this SortInfoVo.

        **参数解释：**  按某个字段进行排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The order_by of this SortInfoVo.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this SortInfoVo.

        **参数解释：**  按某个字段进行排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param order_by: The order_by of this SortInfoVo.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this SortInfoVo.

        **参数解释：**  排序方向。  **约束限制：**  不涉及。  **取值范围：**  - ASC：表示升序。 - DESC：表示降序。  **默认取值：**  ASC。 

        :return: The sort of this SortInfoVo.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this SortInfoVo.

        **参数解释：**  排序方向。  **约束限制：**  不涉及。  **取值范围：**  - ASC：表示升序。 - DESC：表示降序。  **默认取值：**  ASC。 

        :param sort: The sort of this SortInfoVo.
        :type sort: str
        """
        self._sort = sort

    @property
    def sort_info(self):
        r"""Gets the sort_info of this SortInfoVo.

        **参数解释：**  排序信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The sort_info of this SortInfoVo.
        :rtype: str
        """
        return self._sort_info

    @sort_info.setter
    def sort_info(self, sort_info):
        r"""Sets the sort_info of this SortInfoVo.

        **参数解释：**  排序信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param sort_info: The sort_info of this SortInfoVo.
        :type sort_info: str
        """
        self._sort_info = sort_info

    @property
    def sort_info_order_by(self):
        r"""Gets the sort_info_order_by of this SortInfoVo.

        **参数解释：**  排序信息字段。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The sort_info_order_by of this SortInfoVo.
        :rtype: str
        """
        return self._sort_info_order_by

    @sort_info_order_by.setter
    def sort_info_order_by(self, sort_info_order_by):
        r"""Sets the sort_info_order_by of this SortInfoVo.

        **参数解释：**  排序信息字段。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param sort_info_order_by: The sort_info_order_by of this SortInfoVo.
        :type sort_info_order_by: str
        """
        self._sort_info_order_by = sort_info_order_by

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
        if not isinstance(other, SortInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
