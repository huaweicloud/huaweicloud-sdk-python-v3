# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'name': 'list[str]',
        'type': 'list[str]',
        'shared': 'bool',
        'public_border_group': 'list[str]',
        'category': 'list[int]',
        'list_all': 'bool',
        'flavor_sold_out': 'bool'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'shared': 'shared',
        'public_border_group': 'public_border_group',
        'category': 'category',
        'list_all': 'list_all',
        'flavor_sold_out': 'flavor_sold_out'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, name=None, type=None, shared=None, public_border_group=None, category=None, list_all=None, flavor_sold_out=None):
        r"""ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param id: **参数解释**：规格ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：规格名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param type: **参数解释**：规格类别。 支持多值查询，查询条件格式：*type&#x3D;xxx&amp;type&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - L4和L7 表示四层网络型和七层应用型flavor。 [- gateway 表示网关型LB的flavor，目前只支持弹性计费类型。当前仅支持欧洲局点。](tag:hws_eu) - L4_elastic和L7_elastic 表示弹性扩缩容实例的下限规格。 - L4_elastic_max、L7_elastic_max[和gateway_elastic_max](tag:hws_eu) 表示弹性扩缩容实例的上限规格。  **默认取值**：不涉及
        :type type: list[str]
        :param shared: **参数解释**：是否查询公共规格。  **约束限制**：不涉及  **取值范围**： - true表示查询公共规格，所有租户可见的规格。 - false表示查询私有规格，当前仅租户可见的规格。  **默认取值**：不涉及
        :type shared: bool
        :param public_border_group: **参数解释**：公网边界组。 支持多值查询，查询条件格式：*public_border_group&#x3D;xxx&amp;public_border_group&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及
        :type public_border_group: list[str]
        :param category: **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。 支持多值查询，查询条件格式：*category&#x3D;xxx&amp;category&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：0表示center，21表示homezone，41表示IES。  **默认取值**：不涉及
        :type category: list[int]
        :param list_all: **参数解释**：是否查询当前租户所有的弹性上限规格。  **约束限制**：不涉及  **取值范围**： - true：查询当前租户所有的弹性上限规格（l4_elastic_max、l7_elastic_max）。 - false：查询租户弹性上限规格中最大的规格（l4类型优先比较cps指标，然后是带宽；l7类型优先比较https cps指标然后是qps指标）。  **默认取值**：不涉及
        :type list_all: bool
        :param flavor_sold_out: **参数解释**：[是否售罄。](tag:hws)[是否无法购买该规格的LB。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,ct)  **约束限制**：不涉及  **取值范围**： - true：[已售罄，将](tag:hws)无法购买该规格的LB。 - false：[未售罄，](tag:hws)可购买该规格的LB。  **默认取值**：不涉及
        :type flavor_sold_out: bool
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._type = None
        self._shared = None
        self._public_border_group = None
        self._category = None
        self._list_all = None
        self._flavor_sold_out = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if shared is not None:
            self.shared = shared
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if category is not None:
            self.category = category
        if list_all is not None:
            self.list_all = list_all
        if flavor_sold_out is not None:
            self.flavor_sold_out = flavor_sold_out

    @property
    def marker(self):
        r"""Gets the marker of this ListFlavorsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListFlavorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFlavorsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListFlavorsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListFlavorsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlavorsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListFlavorsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListFlavorsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListFlavorsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListFlavorsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListFlavorsRequest.

        **参数解释**：规格ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListFlavorsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListFlavorsRequest.

        **参数解释**：规格ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListFlavorsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListFlavorsRequest.

        **参数解释**：规格名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListFlavorsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFlavorsRequest.

        **参数解释**：规格名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListFlavorsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ListFlavorsRequest.

        **参数解释**：规格类别。 支持多值查询，查询条件格式：*type=xxx&type=xxx*。  **约束限制**：不涉及  **取值范围**： - L4和L7 表示四层网络型和七层应用型flavor。 [- gateway 表示网关型LB的flavor，目前只支持弹性计费类型。当前仅支持欧洲局点。](tag:hws_eu) - L4_elastic和L7_elastic 表示弹性扩缩容实例的下限规格。 - L4_elastic_max、L7_elastic_max[和gateway_elastic_max](tag:hws_eu) 表示弹性扩缩容实例的上限规格。  **默认取值**：不涉及

        :return: The type of this ListFlavorsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListFlavorsRequest.

        **参数解释**：规格类别。 支持多值查询，查询条件格式：*type=xxx&type=xxx*。  **约束限制**：不涉及  **取值范围**： - L4和L7 表示四层网络型和七层应用型flavor。 [- gateway 表示网关型LB的flavor，目前只支持弹性计费类型。当前仅支持欧洲局点。](tag:hws_eu) - L4_elastic和L7_elastic 表示弹性扩缩容实例的下限规格。 - L4_elastic_max、L7_elastic_max[和gateway_elastic_max](tag:hws_eu) 表示弹性扩缩容实例的上限规格。  **默认取值**：不涉及

        :param type: The type of this ListFlavorsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def shared(self):
        r"""Gets the shared of this ListFlavorsRequest.

        **参数解释**：是否查询公共规格。  **约束限制**：不涉及  **取值范围**： - true表示查询公共规格，所有租户可见的规格。 - false表示查询私有规格，当前仅租户可见的规格。  **默认取值**：不涉及

        :return: The shared of this ListFlavorsRequest.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        r"""Sets the shared of this ListFlavorsRequest.

        **参数解释**：是否查询公共规格。  **约束限制**：不涉及  **取值范围**： - true表示查询公共规格，所有租户可见的规格。 - false表示查询私有规格，当前仅租户可见的规格。  **默认取值**：不涉及

        :param shared: The shared of this ListFlavorsRequest.
        :type shared: bool
        """
        self._shared = shared

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ListFlavorsRequest.

        **参数解释**：公网边界组。 支持多值查询，查询条件格式：*public_border_group=xxx&public_border_group=xxx*。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及

        :return: The public_border_group of this ListFlavorsRequest.
        :rtype: list[str]
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ListFlavorsRequest.

        **参数解释**：公网边界组。 支持多值查询，查询条件格式：*public_border_group=xxx&public_border_group=xxx*。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及

        :param public_border_group: The public_border_group of this ListFlavorsRequest.
        :type public_border_group: list[str]
        """
        self._public_border_group = public_border_group

    @property
    def category(self):
        r"""Gets the category of this ListFlavorsRequest.

        **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。 支持多值查询，查询条件格式：*category=xxx&category=xxx*。  **约束限制**：不涉及  **取值范围**：0表示center，21表示homezone，41表示IES。  **默认取值**：不涉及

        :return: The category of this ListFlavorsRequest.
        :rtype: list[int]
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListFlavorsRequest.

        **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。 支持多值查询，查询条件格式：*category=xxx&category=xxx*。  **约束限制**：不涉及  **取值范围**：0表示center，21表示homezone，41表示IES。  **默认取值**：不涉及

        :param category: The category of this ListFlavorsRequest.
        :type category: list[int]
        """
        self._category = category

    @property
    def list_all(self):
        r"""Gets the list_all of this ListFlavorsRequest.

        **参数解释**：是否查询当前租户所有的弹性上限规格。  **约束限制**：不涉及  **取值范围**： - true：查询当前租户所有的弹性上限规格（l4_elastic_max、l7_elastic_max）。 - false：查询租户弹性上限规格中最大的规格（l4类型优先比较cps指标，然后是带宽；l7类型优先比较https cps指标然后是qps指标）。  **默认取值**：不涉及

        :return: The list_all of this ListFlavorsRequest.
        :rtype: bool
        """
        return self._list_all

    @list_all.setter
    def list_all(self, list_all):
        r"""Sets the list_all of this ListFlavorsRequest.

        **参数解释**：是否查询当前租户所有的弹性上限规格。  **约束限制**：不涉及  **取值范围**： - true：查询当前租户所有的弹性上限规格（l4_elastic_max、l7_elastic_max）。 - false：查询租户弹性上限规格中最大的规格（l4类型优先比较cps指标，然后是带宽；l7类型优先比较https cps指标然后是qps指标）。  **默认取值**：不涉及

        :param list_all: The list_all of this ListFlavorsRequest.
        :type list_all: bool
        """
        self._list_all = list_all

    @property
    def flavor_sold_out(self):
        r"""Gets the flavor_sold_out of this ListFlavorsRequest.

        **参数解释**：[是否售罄。](tag:hws)[是否无法购买该规格的LB。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,ct)  **约束限制**：不涉及  **取值范围**： - true：[已售罄，将](tag:hws)无法购买该规格的LB。 - false：[未售罄，](tag:hws)可购买该规格的LB。  **默认取值**：不涉及

        :return: The flavor_sold_out of this ListFlavorsRequest.
        :rtype: bool
        """
        return self._flavor_sold_out

    @flavor_sold_out.setter
    def flavor_sold_out(self, flavor_sold_out):
        r"""Sets the flavor_sold_out of this ListFlavorsRequest.

        **参数解释**：[是否售罄。](tag:hws)[是否无法购买该规格的LB。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,ct)  **约束限制**：不涉及  **取值范围**： - true：[已售罄，将](tag:hws)无法购买该规格的LB。 - false：[未售罄，](tag:hws)可购买该规格的LB。  **默认取值**：不涉及

        :param flavor_sold_out: The flavor_sold_out of this ListFlavorsRequest.
        :type flavor_sold_out: bool
        """
        self._flavor_sold_out = flavor_sold_out

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
