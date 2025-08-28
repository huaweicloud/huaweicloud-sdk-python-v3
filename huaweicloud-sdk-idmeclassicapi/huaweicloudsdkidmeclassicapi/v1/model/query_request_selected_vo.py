# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRequestSelectedVo:

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
        'conditions': 'list[QueryCondition]',
        'decrypt': 'bool',
        'entity_type': 'str',
        'filter': 'QueryCondition',
        'is_need_total': 'bool',
        'is_present_all': 'bool',
        'need_present_detail': 'list[str]',
        'order_by': 'str',
        'order_by_table_alias': 'str',
        'public_data': 'str',
        'selected_field': 'list[SelectedField]',
        'sort': 'str',
        'sorts': 'list[SortInfoVo]',
        'is_transform_res_body': 'bool'
    }

    attribute_map = {
        'character_set': 'characterSet',
        'conditions': 'conditions',
        'decrypt': 'decrypt',
        'entity_type': 'entityType',
        'filter': 'filter',
        'is_need_total': 'isNeedTotal',
        'is_present_all': 'isPresentAll',
        'need_present_detail': 'needPresentDetail',
        'order_by': 'orderBy',
        'order_by_table_alias': 'orderByTableAlias',
        'public_data': 'publicData',
        'selected_field': 'selectedField',
        'sort': 'sort',
        'sorts': 'sorts',
        'is_transform_res_body': 'isTransformResBody'
    }

    def __init__(self, character_set=None, conditions=None, decrypt=None, entity_type=None, filter=None, is_need_total=None, is_present_all=None, need_present_detail=None, order_by=None, order_by_table_alias=None, public_data=None, selected_field=None, sort=None, sorts=None, is_transform_res_body=None):
        r"""QueryRequestSelectedVo

        The model defined in huaweicloud sdk

        :param character_set: 
        :type character_set: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        :param conditions: **参数解释：**  查询条件。  此参数已废弃，不建议继续使用，建议使用替代参数filter。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type conditions: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        :param decrypt: **参数解释：**  是否加密。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。
        :type decrypt: bool
        :param entity_type: **参数解释：**  实体类型。  **约束限制：**  不涉及。  **取值范围：**  - ENTITY：数据实体。 - RRELATION：关系实体。  **默认取值：**  不涉及。
        :type entity_type: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        :param is_need_total: **参数解释：**  是否需要查询总记录数。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  不涉及。
        :type is_need_total: bool
        :param is_present_all: **参数解释：**  是否需要展示所有参考对象信息。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  不涉及。
        :type is_present_all: bool
        :param need_present_detail: **参数解释：**  需要展示详细信息的参考对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type need_present_detail: list[str]
        :param order_by: **参数解释：**  按某个字段进行排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type order_by: str
        :param order_by_table_alias: **参数解释：**  排序字段的表别名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type order_by_table_alias: str
        :param public_data: **参数解释：**  多租查询参数。  **约束限制：**  不涉及。  **取值范围：**  - EXCLUDE_PUBLIC_DATA：不包括公共数据。 - INCLUDE_PUBLIC_DATA：包括公共数据。 - ONLY_NEED_PUBLIC_DATA：只有公共数据。  **默认取值：**  不涉及。
        :type public_data: str
        :param selected_field: **参数解释：**  指定需返回的属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type selected_field: list[:class:`huaweicloudsdkidmeclassicapi.v1.SelectedField`]
        :param sort: **参数解释：**  排序方向。  **约束限制：**  不涉及。  **取值范围：**  - ASC：表示升序。 - DESC：表示降序。  **默认取值：**  不涉及。
        :type sort: str
        :param sorts: **参数解释：**  排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type sorts: list[:class:`huaweicloudsdkidmeclassicapi.v1.SortInfoVo`]
        :param is_transform_res_body: **参数解释：**  是否需要格式化分类属性。  **约束限制：**  不涉及。  **取值范围：**  - true：需要格式化分类属性。 - false：不需要格式化分类属性。  **默认取值：**  不涉及。
        :type is_transform_res_body: bool
        """
        
        

        self._character_set = None
        self._conditions = None
        self._decrypt = None
        self._entity_type = None
        self._filter = None
        self._is_need_total = None
        self._is_present_all = None
        self._need_present_detail = None
        self._order_by = None
        self._order_by_table_alias = None
        self._public_data = None
        self._selected_field = None
        self._sort = None
        self._sorts = None
        self._is_transform_res_body = None
        self.discriminator = None

        if character_set is not None:
            self.character_set = character_set
        if conditions is not None:
            self.conditions = conditions
        if decrypt is not None:
            self.decrypt = decrypt
        if entity_type is not None:
            self.entity_type = entity_type
        if filter is not None:
            self.filter = filter
        if is_need_total is not None:
            self.is_need_total = is_need_total
        if is_present_all is not None:
            self.is_present_all = is_present_all
        if need_present_detail is not None:
            self.need_present_detail = need_present_detail
        if order_by is not None:
            self.order_by = order_by
        if order_by_table_alias is not None:
            self.order_by_table_alias = order_by_table_alias
        if public_data is not None:
            self.public_data = public_data
        self.selected_field = selected_field
        if sort is not None:
            self.sort = sort
        if sorts is not None:
            self.sorts = sorts
        if is_transform_res_body is not None:
            self.is_transform_res_body = is_transform_res_body

    @property
    def character_set(self):
        r"""Gets the character_set of this QueryRequestSelectedVo.

        :return: The character_set of this QueryRequestSelectedVo.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        r"""Sets the character_set of this QueryRequestSelectedVo.

        :param character_set: The character_set of this QueryRequestSelectedVo.
        :type character_set: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        """
        self._character_set = character_set

    @property
    def conditions(self):
        r"""Gets the conditions of this QueryRequestSelectedVo.

        **参数解释：**  查询条件。  此参数已废弃，不建议继续使用，建议使用替代参数filter。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The conditions of this QueryRequestSelectedVo.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this QueryRequestSelectedVo.

        **参数解释：**  查询条件。  此参数已废弃，不建议继续使用，建议使用替代参数filter。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param conditions: The conditions of this QueryRequestSelectedVo.
        :type conditions: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        """
        self._conditions = conditions

    @property
    def decrypt(self):
        r"""Gets the decrypt of this QueryRequestSelectedVo.

        **参数解释：**  是否加密。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。

        :return: The decrypt of this QueryRequestSelectedVo.
        :rtype: bool
        """
        return self._decrypt

    @decrypt.setter
    def decrypt(self, decrypt):
        r"""Sets the decrypt of this QueryRequestSelectedVo.

        **参数解释：**  是否加密。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。

        :param decrypt: The decrypt of this QueryRequestSelectedVo.
        :type decrypt: bool
        """
        self._decrypt = decrypt

    @property
    def entity_type(self):
        r"""Gets the entity_type of this QueryRequestSelectedVo.

        **参数解释：**  实体类型。  **约束限制：**  不涉及。  **取值范围：**  - ENTITY：数据实体。 - RRELATION：关系实体。  **默认取值：**  不涉及。

        :return: The entity_type of this QueryRequestSelectedVo.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        r"""Sets the entity_type of this QueryRequestSelectedVo.

        **参数解释：**  实体类型。  **约束限制：**  不涉及。  **取值范围：**  - ENTITY：数据实体。 - RRELATION：关系实体。  **默认取值：**  不涉及。

        :param entity_type: The entity_type of this QueryRequestSelectedVo.
        :type entity_type: str
        """
        self._entity_type = entity_type

    @property
    def filter(self):
        r"""Gets the filter of this QueryRequestSelectedVo.

        :return: The filter of this QueryRequestSelectedVo.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this QueryRequestSelectedVo.

        :param filter: The filter of this QueryRequestSelectedVo.
        :type filter: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        """
        self._filter = filter

    @property
    def is_need_total(self):
        r"""Gets the is_need_total of this QueryRequestSelectedVo.

        **参数解释：**  是否需要查询总记录数。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  不涉及。

        :return: The is_need_total of this QueryRequestSelectedVo.
        :rtype: bool
        """
        return self._is_need_total

    @is_need_total.setter
    def is_need_total(self, is_need_total):
        r"""Sets the is_need_total of this QueryRequestSelectedVo.

        **参数解释：**  是否需要查询总记录数。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  不涉及。

        :param is_need_total: The is_need_total of this QueryRequestSelectedVo.
        :type is_need_total: bool
        """
        self._is_need_total = is_need_total

    @property
    def is_present_all(self):
        r"""Gets the is_present_all of this QueryRequestSelectedVo.

        **参数解释：**  是否需要展示所有参考对象信息。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  不涉及。

        :return: The is_present_all of this QueryRequestSelectedVo.
        :rtype: bool
        """
        return self._is_present_all

    @is_present_all.setter
    def is_present_all(self, is_present_all):
        r"""Sets the is_present_all of this QueryRequestSelectedVo.

        **参数解释：**  是否需要展示所有参考对象信息。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  不涉及。

        :param is_present_all: The is_present_all of this QueryRequestSelectedVo.
        :type is_present_all: bool
        """
        self._is_present_all = is_present_all

    @property
    def need_present_detail(self):
        r"""Gets the need_present_detail of this QueryRequestSelectedVo.

        **参数解释：**  需要展示详细信息的参考对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The need_present_detail of this QueryRequestSelectedVo.
        :rtype: list[str]
        """
        return self._need_present_detail

    @need_present_detail.setter
    def need_present_detail(self, need_present_detail):
        r"""Sets the need_present_detail of this QueryRequestSelectedVo.

        **参数解释：**  需要展示详细信息的参考对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param need_present_detail: The need_present_detail of this QueryRequestSelectedVo.
        :type need_present_detail: list[str]
        """
        self._need_present_detail = need_present_detail

    @property
    def order_by(self):
        r"""Gets the order_by of this QueryRequestSelectedVo.

        **参数解释：**  按某个字段进行排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The order_by of this QueryRequestSelectedVo.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this QueryRequestSelectedVo.

        **参数解释：**  按某个字段进行排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param order_by: The order_by of this QueryRequestSelectedVo.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_table_alias(self):
        r"""Gets the order_by_table_alias of this QueryRequestSelectedVo.

        **参数解释：**  排序字段的表别名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The order_by_table_alias of this QueryRequestSelectedVo.
        :rtype: str
        """
        return self._order_by_table_alias

    @order_by_table_alias.setter
    def order_by_table_alias(self, order_by_table_alias):
        r"""Sets the order_by_table_alias of this QueryRequestSelectedVo.

        **参数解释：**  排序字段的表别名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param order_by_table_alias: The order_by_table_alias of this QueryRequestSelectedVo.
        :type order_by_table_alias: str
        """
        self._order_by_table_alias = order_by_table_alias

    @property
    def public_data(self):
        r"""Gets the public_data of this QueryRequestSelectedVo.

        **参数解释：**  多租查询参数。  **约束限制：**  不涉及。  **取值范围：**  - EXCLUDE_PUBLIC_DATA：不包括公共数据。 - INCLUDE_PUBLIC_DATA：包括公共数据。 - ONLY_NEED_PUBLIC_DATA：只有公共数据。  **默认取值：**  不涉及。

        :return: The public_data of this QueryRequestSelectedVo.
        :rtype: str
        """
        return self._public_data

    @public_data.setter
    def public_data(self, public_data):
        r"""Sets the public_data of this QueryRequestSelectedVo.

        **参数解释：**  多租查询参数。  **约束限制：**  不涉及。  **取值范围：**  - EXCLUDE_PUBLIC_DATA：不包括公共数据。 - INCLUDE_PUBLIC_DATA：包括公共数据。 - ONLY_NEED_PUBLIC_DATA：只有公共数据。  **默认取值：**  不涉及。

        :param public_data: The public_data of this QueryRequestSelectedVo.
        :type public_data: str
        """
        self._public_data = public_data

    @property
    def selected_field(self):
        r"""Gets the selected_field of this QueryRequestSelectedVo.

        **参数解释：**  指定需返回的属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The selected_field of this QueryRequestSelectedVo.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.SelectedField`]
        """
        return self._selected_field

    @selected_field.setter
    def selected_field(self, selected_field):
        r"""Sets the selected_field of this QueryRequestSelectedVo.

        **参数解释：**  指定需返回的属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param selected_field: The selected_field of this QueryRequestSelectedVo.
        :type selected_field: list[:class:`huaweicloudsdkidmeclassicapi.v1.SelectedField`]
        """
        self._selected_field = selected_field

    @property
    def sort(self):
        r"""Gets the sort of this QueryRequestSelectedVo.

        **参数解释：**  排序方向。  **约束限制：**  不涉及。  **取值范围：**  - ASC：表示升序。 - DESC：表示降序。  **默认取值：**  不涉及。

        :return: The sort of this QueryRequestSelectedVo.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this QueryRequestSelectedVo.

        **参数解释：**  排序方向。  **约束限制：**  不涉及。  **取值范围：**  - ASC：表示升序。 - DESC：表示降序。  **默认取值：**  不涉及。

        :param sort: The sort of this QueryRequestSelectedVo.
        :type sort: str
        """
        self._sort = sort

    @property
    def sorts(self):
        r"""Gets the sorts of this QueryRequestSelectedVo.

        **参数解释：**  排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The sorts of this QueryRequestSelectedVo.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.SortInfoVo`]
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        r"""Sets the sorts of this QueryRequestSelectedVo.

        **参数解释：**  排序。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param sorts: The sorts of this QueryRequestSelectedVo.
        :type sorts: list[:class:`huaweicloudsdkidmeclassicapi.v1.SortInfoVo`]
        """
        self._sorts = sorts

    @property
    def is_transform_res_body(self):
        r"""Gets the is_transform_res_body of this QueryRequestSelectedVo.

        **参数解释：**  是否需要格式化分类属性。  **约束限制：**  不涉及。  **取值范围：**  - true：需要格式化分类属性。 - false：不需要格式化分类属性。  **默认取值：**  不涉及。

        :return: The is_transform_res_body of this QueryRequestSelectedVo.
        :rtype: bool
        """
        return self._is_transform_res_body

    @is_transform_res_body.setter
    def is_transform_res_body(self, is_transform_res_body):
        r"""Sets the is_transform_res_body of this QueryRequestSelectedVo.

        **参数解释：**  是否需要格式化分类属性。  **约束限制：**  不涉及。  **取值范围：**  - true：需要格式化分类属性。 - false：不需要格式化分类属性。  **默认取值：**  不涉及。

        :param is_transform_res_body: The is_transform_res_body of this QueryRequestSelectedVo.
        :type is_transform_res_body: bool
        """
        self._is_transform_res_body = is_transform_res_body

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
        if not isinstance(other, QueryRequestSelectedVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
