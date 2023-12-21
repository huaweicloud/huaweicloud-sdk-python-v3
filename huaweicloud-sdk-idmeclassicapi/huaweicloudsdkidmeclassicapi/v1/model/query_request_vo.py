# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRequestVo:

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
        'sort': 'str',
        'sorts': 'list[SortInfoVo]'
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
        'sort': 'sort',
        'sorts': 'sorts'
    }

    def __init__(self, character_set=None, conditions=None, decrypt=None, entity_type=None, filter=None, is_need_total=None, is_present_all=None, need_present_detail=None, order_by=None, order_by_table_alias=None, public_data=None, sort=None, sorts=None):
        """QueryRequestVo

        The model defined in huaweicloud sdk

        :param character_set: 
        :type character_set: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        :param conditions: 查询条件。
        :type conditions: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        :param decrypt: 是否加密。 - true：加密。 - false：不加密。
        :type decrypt: bool
        :param entity_type: 实体类型。
        :type entity_type: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        :param is_need_total: 是否需要查询总记录数。 - true：需要。 - false：不需要。
        :type is_need_total: bool
        :param is_present_all: 是否需要展示所有参考对象信息。 - true：需要。 - false：不需要。
        :type is_present_all: bool
        :param need_present_detail: 需要展示详细信息的参考对象。
        :type need_present_detail: list[str]
        :param order_by: 按某个字段进行排序。
        :type order_by: str
        :param order_by_table_alias: 排序字段的表别名。
        :type order_by_table_alias: str
        :param public_data: 多租查询参数。 - EXCLUDE_PUBLIC_DATA：不包括公共数据。 - INCLUDE_PUBLIC_DATA：包括公共数据。 - ONLY_NEED_PUBLIC_DATA：只有公共数据。
        :type public_data: str
        :param sort: 排序方向。 - ASC：表示升序。 - DESC：表示降序。
        :type sort: str
        :param sorts: 排序。
        :type sorts: list[:class:`huaweicloudsdkidmeclassicapi.v1.SortInfoVo`]
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
        self._sort = None
        self._sorts = None
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
        if sort is not None:
            self.sort = sort
        if sorts is not None:
            self.sorts = sorts

    @property
    def character_set(self):
        """Gets the character_set of this QueryRequestVo.

        :return: The character_set of this QueryRequestVo.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this QueryRequestVo.

        :param character_set: The character_set of this QueryRequestVo.
        :type character_set: :class:`huaweicloudsdkidmeclassicapi.v1.CharacterSetEnum`
        """
        self._character_set = character_set

    @property
    def conditions(self):
        """Gets the conditions of this QueryRequestVo.

        查询条件。

        :return: The conditions of this QueryRequestVo.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this QueryRequestVo.

        查询条件。

        :param conditions: The conditions of this QueryRequestVo.
        :type conditions: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        """
        self._conditions = conditions

    @property
    def decrypt(self):
        """Gets the decrypt of this QueryRequestVo.

        是否加密。 - true：加密。 - false：不加密。

        :return: The decrypt of this QueryRequestVo.
        :rtype: bool
        """
        return self._decrypt

    @decrypt.setter
    def decrypt(self, decrypt):
        """Sets the decrypt of this QueryRequestVo.

        是否加密。 - true：加密。 - false：不加密。

        :param decrypt: The decrypt of this QueryRequestVo.
        :type decrypt: bool
        """
        self._decrypt = decrypt

    @property
    def entity_type(self):
        """Gets the entity_type of this QueryRequestVo.

        实体类型。

        :return: The entity_type of this QueryRequestVo.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this QueryRequestVo.

        实体类型。

        :param entity_type: The entity_type of this QueryRequestVo.
        :type entity_type: str
        """
        self._entity_type = entity_type

    @property
    def filter(self):
        """Gets the filter of this QueryRequestVo.

        :return: The filter of this QueryRequestVo.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this QueryRequestVo.

        :param filter: The filter of this QueryRequestVo.
        :type filter: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        """
        self._filter = filter

    @property
    def is_need_total(self):
        """Gets the is_need_total of this QueryRequestVo.

        是否需要查询总记录数。 - true：需要。 - false：不需要。

        :return: The is_need_total of this QueryRequestVo.
        :rtype: bool
        """
        return self._is_need_total

    @is_need_total.setter
    def is_need_total(self, is_need_total):
        """Sets the is_need_total of this QueryRequestVo.

        是否需要查询总记录数。 - true：需要。 - false：不需要。

        :param is_need_total: The is_need_total of this QueryRequestVo.
        :type is_need_total: bool
        """
        self._is_need_total = is_need_total

    @property
    def is_present_all(self):
        """Gets the is_present_all of this QueryRequestVo.

        是否需要展示所有参考对象信息。 - true：需要。 - false：不需要。

        :return: The is_present_all of this QueryRequestVo.
        :rtype: bool
        """
        return self._is_present_all

    @is_present_all.setter
    def is_present_all(self, is_present_all):
        """Sets the is_present_all of this QueryRequestVo.

        是否需要展示所有参考对象信息。 - true：需要。 - false：不需要。

        :param is_present_all: The is_present_all of this QueryRequestVo.
        :type is_present_all: bool
        """
        self._is_present_all = is_present_all

    @property
    def need_present_detail(self):
        """Gets the need_present_detail of this QueryRequestVo.

        需要展示详细信息的参考对象。

        :return: The need_present_detail of this QueryRequestVo.
        :rtype: list[str]
        """
        return self._need_present_detail

    @need_present_detail.setter
    def need_present_detail(self, need_present_detail):
        """Sets the need_present_detail of this QueryRequestVo.

        需要展示详细信息的参考对象。

        :param need_present_detail: The need_present_detail of this QueryRequestVo.
        :type need_present_detail: list[str]
        """
        self._need_present_detail = need_present_detail

    @property
    def order_by(self):
        """Gets the order_by of this QueryRequestVo.

        按某个字段进行排序。

        :return: The order_by of this QueryRequestVo.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this QueryRequestVo.

        按某个字段进行排序。

        :param order_by: The order_by of this QueryRequestVo.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_table_alias(self):
        """Gets the order_by_table_alias of this QueryRequestVo.

        排序字段的表别名。

        :return: The order_by_table_alias of this QueryRequestVo.
        :rtype: str
        """
        return self._order_by_table_alias

    @order_by_table_alias.setter
    def order_by_table_alias(self, order_by_table_alias):
        """Sets the order_by_table_alias of this QueryRequestVo.

        排序字段的表别名。

        :param order_by_table_alias: The order_by_table_alias of this QueryRequestVo.
        :type order_by_table_alias: str
        """
        self._order_by_table_alias = order_by_table_alias

    @property
    def public_data(self):
        """Gets the public_data of this QueryRequestVo.

        多租查询参数。 - EXCLUDE_PUBLIC_DATA：不包括公共数据。 - INCLUDE_PUBLIC_DATA：包括公共数据。 - ONLY_NEED_PUBLIC_DATA：只有公共数据。

        :return: The public_data of this QueryRequestVo.
        :rtype: str
        """
        return self._public_data

    @public_data.setter
    def public_data(self, public_data):
        """Sets the public_data of this QueryRequestVo.

        多租查询参数。 - EXCLUDE_PUBLIC_DATA：不包括公共数据。 - INCLUDE_PUBLIC_DATA：包括公共数据。 - ONLY_NEED_PUBLIC_DATA：只有公共数据。

        :param public_data: The public_data of this QueryRequestVo.
        :type public_data: str
        """
        self._public_data = public_data

    @property
    def sort(self):
        """Gets the sort of this QueryRequestVo.

        排序方向。 - ASC：表示升序。 - DESC：表示降序。

        :return: The sort of this QueryRequestVo.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this QueryRequestVo.

        排序方向。 - ASC：表示升序。 - DESC：表示降序。

        :param sort: The sort of this QueryRequestVo.
        :type sort: str
        """
        self._sort = sort

    @property
    def sorts(self):
        """Gets the sorts of this QueryRequestVo.

        排序。

        :return: The sorts of this QueryRequestVo.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.SortInfoVo`]
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        """Sets the sorts of this QueryRequestVo.

        排序。

        :param sorts: The sorts of this QueryRequestVo.
        :type sorts: list[:class:`huaweicloudsdkidmeclassicapi.v1.SortInfoVo`]
        """
        self._sorts = sorts

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
        if not isinstance(other, QueryRequestVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
