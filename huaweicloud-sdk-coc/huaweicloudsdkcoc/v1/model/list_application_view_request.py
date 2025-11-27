# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationViewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_like': 'str',
        'code_list': 'list[str]',
        'marker': 'str',
        'limit': 'int',
        'page_no': 'int',
        'is_collection': 'bool'
    }

    attribute_map = {
        'name_like': 'name_like',
        'code_list': 'code_list',
        'marker': 'marker',
        'limit': 'limit',
        'page_no': 'page_no',
        'is_collection': 'is_collection'
    }

    def __init__(self, name_like=None, code_list=None, marker=None, limit=None, page_no=None, is_collection=None):
        r"""ListApplicationViewRequest

        The model defined in huaweicloud sdk

        :param name_like: **参数解释：** 名称模糊匹配，支持模糊查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name_like: str
        :param code_list: **参数解释：** 应用、组件、分组code组成。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type code_list: list[str]
        :param marker: **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type marker: str
        :param limit: **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。
        :type limit: int
        :param page_no: **参数解释：** 分页页码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type page_no: int
        :param is_collection: **参数解释：** 是否收藏。 **约束限制：** 不涉及。 **取值范围：** - true：在我的收藏去查询应用、组件、分组，默认为true。 - false：在全部应用中查询应用、组件、分组，可以不传。 **默认取值：** 默认未收藏。
        :type is_collection: bool
        """
        
        

        self._name_like = None
        self._code_list = None
        self._marker = None
        self._limit = None
        self._page_no = None
        self._is_collection = None
        self.discriminator = None

        if name_like is not None:
            self.name_like = name_like
        if code_list is not None:
            self.code_list = code_list
        if marker is not None:
            self.marker = marker
        self.limit = limit
        if page_no is not None:
            self.page_no = page_no
        if is_collection is not None:
            self.is_collection = is_collection

    @property
    def name_like(self):
        r"""Gets the name_like of this ListApplicationViewRequest.

        **参数解释：** 名称模糊匹配，支持模糊查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name_like of this ListApplicationViewRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        r"""Sets the name_like of this ListApplicationViewRequest.

        **参数解释：** 名称模糊匹配，支持模糊查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name_like: The name_like of this ListApplicationViewRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def code_list(self):
        r"""Gets the code_list of this ListApplicationViewRequest.

        **参数解释：** 应用、组件、分组code组成。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The code_list of this ListApplicationViewRequest.
        :rtype: list[str]
        """
        return self._code_list

    @code_list.setter
    def code_list(self, code_list):
        r"""Sets the code_list of this ListApplicationViewRequest.

        **参数解释：** 应用、组件、分组code组成。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param code_list: The code_list of this ListApplicationViewRequest.
        :type code_list: list[str]
        """
        self._code_list = code_list

    @property
    def marker(self):
        r"""Gets the marker of this ListApplicationViewRequest.

        **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The marker of this ListApplicationViewRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListApplicationViewRequest.

        **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param marker: The marker of this ListApplicationViewRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListApplicationViewRequest.

        **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。

        :return: The limit of this ListApplicationViewRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApplicationViewRequest.

        **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。

        :param limit: The limit of this ListApplicationViewRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_no(self):
        r"""Gets the page_no of this ListApplicationViewRequest.

        **参数解释：** 分页页码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The page_no of this ListApplicationViewRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListApplicationViewRequest.

        **参数解释：** 分页页码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param page_no: The page_no of this ListApplicationViewRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def is_collection(self):
        r"""Gets the is_collection of this ListApplicationViewRequest.

        **参数解释：** 是否收藏。 **约束限制：** 不涉及。 **取值范围：** - true：在我的收藏去查询应用、组件、分组，默认为true。 - false：在全部应用中查询应用、组件、分组，可以不传。 **默认取值：** 默认未收藏。

        :return: The is_collection of this ListApplicationViewRequest.
        :rtype: bool
        """
        return self._is_collection

    @is_collection.setter
    def is_collection(self, is_collection):
        r"""Sets the is_collection of this ListApplicationViewRequest.

        **参数解释：** 是否收藏。 **约束限制：** 不涉及。 **取值范围：** - true：在我的收藏去查询应用、组件、分组，默认为true。 - false：在全部应用中查询应用、组件、分组，可以不传。 **默认取值：** 默认未收藏。

        :param is_collection: The is_collection of this ListApplicationViewRequest.
        :type is_collection: bool
        """
        self._is_collection = is_collection

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
        if not isinstance(other, ListApplicationViewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
