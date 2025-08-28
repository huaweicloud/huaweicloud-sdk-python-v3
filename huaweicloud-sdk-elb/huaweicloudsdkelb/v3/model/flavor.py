# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'info': 'FlavorInfo',
        'name': 'str',
        'shared': 'bool',
        'project_id': 'str',
        'type': 'str',
        'flavor_sold_out': 'bool',
        'public_border_group': 'str',
        'category': 'int'
    }

    attribute_map = {
        'id': 'id',
        'info': 'info',
        'name': 'name',
        'shared': 'shared',
        'project_id': 'project_id',
        'type': 'type',
        'flavor_sold_out': 'flavor_sold_out',
        'public_border_group': 'public_border_group',
        'category': 'category'
    }

    def __init__(self, id=None, info=None, name=None, shared=None, project_id=None, type=None, flavor_sold_out=None, public_border_group=None, category=None):
        r"""Flavor

        The model defined in huaweicloud sdk

        :param id: **参数解释**：规格ID。  **取值范围**：不涉及
        :type id: str
        :param info: 
        :type info: :class:`huaweicloudsdkelb.v3.FlavorInfo`
        :param name: **参数解释**：规格名称。  **取值范围**： [网络型有如下规格：   - L4_flavor.elb.s1.small: 小型 I   - L4_flavor.elb.s2.small: 小型 II   - L4_flavor.elb.s1.medium: 中型 I   - L4_flavor.elb.s2.medium: 中型 II   - L4_flavor.elb.s1.large: 大型 I   - L4_flavor.elb.s2.large: 大型 II   - L4_flavor.elb.pro.max: 四层弹性规格  应用型有如下规格：   - L7_flavor.elb.s1.small: 小型 I   - L7_flavor.elb.s2.small: 小型 II   - L7_flavor.elb.s1.medium: 中型 I   - L7_flavor.elb.s2.medium: 中型 II   - L7_flavor.elb.s1.large: 大型 I   - L7_flavor.elb.s2.large: 大型 II   - L7_flavor.elb.s1.extra-large: 超大型 I   - L7_flavor.elb.s2.extra-large: 超大型 II   - L7_flavor.elb.pro.max: 七层弹性规格](tag:hws,hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42) [网络型有如下规格：   - L4_flavor.elb.s1.small: 小型 I   - L4_flavor.elb.s2.small: 小型 II   - L4_flavor.elb.s1.medium: 中型 I   - L4_flavor.elb.s2.medium: 中型 II   - L4_flavor.elb.s1.large: 大型 I   - L4_flavor.elb.s2.large: 大型 II   - L4_flavor.elb.pro.max: 四层弹性规格  应用型有如下规格：   - L7_flavor.elb.s1.small: 小型 I   - L7_flavor.elb.s2.small: 小型 II   - L7_flavor.elb.s1.medium: 中型 I   - L7_flavor.elb.s2.medium: 中型 II   - L7_flavor.elb.s1.large: 大型 I   - L7_flavor.elb.s2.large: 大型 II   - L7_flavor.elb.pro.s1.small：弹性规格小型I。已不支持，请勿使用。   - L7_flavor.elb.pro.s1.medium：弹性规格中型I。已不支持，请勿使用。   - L7_flavor.elb.pro.s1.large：弹性规格大型I。已不支持，请勿使用。   - L7_flavor.elb.pro.max: 七层弹性规格](tag:dt,hcso_dt)
        :type name: str
        :param shared: **参数解释**：是否公共规格。  **取值范围**： - true表示公共规格，所有租户可见。 - false表示私有规格，为当前租户所有。
        :type shared: bool
        :param project_id: **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。
        :type project_id: str
        :param type: **参数解释**：规格类别。  **取值范围**：   - L4和L7 表示四层网络型和七层应用型flavor。   [- gateway 表示网关型LB的flavor，目前只支持弹性计费类型。当前仅支持欧洲局点。](tag:hws_eu)   - L4_elastic和L7_elastic 表示弹性扩缩容实例的下限规格。已废弃，请勿使用。   - L4_elastic_max、L7_elastic_max[和gateway_elastic_max](tag:hws_eu) 表示弹性扩缩容实例的上限规格。
        :type type: str
        :param flavor_sold_out: **参数解释**：[是否售罄。](tag:hws)[是否无法购买该规格的LB。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,ct)  **取值范围**： - true：[已售罄，将](tag:hws)无法购买该规格的LB。 - false：[未售罄，](tag:hws)可购买该规格的LB。
        :type flavor_sold_out: bool
        :param public_border_group: **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组
        :type public_border_group: str
        :param category: **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。  **取值范围**：0表示center，21表示homezone，41表示IES。
        :type category: int
        """
        
        

        self._id = None
        self._info = None
        self._name = None
        self._shared = None
        self._project_id = None
        self._type = None
        self._flavor_sold_out = None
        self._public_border_group = None
        self._category = None
        self.discriminator = None

        self.id = id
        self.info = info
        self.name = name
        self.shared = shared
        self.project_id = project_id
        self.type = type
        self.flavor_sold_out = flavor_sold_out
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if category is not None:
            self.category = category

    @property
    def id(self):
        r"""Gets the id of this Flavor.

        **参数解释**：规格ID。  **取值范围**：不涉及

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Flavor.

        **参数解释**：规格ID。  **取值范围**：不涉及

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def info(self):
        r"""Gets the info of this Flavor.

        :return: The info of this Flavor.
        :rtype: :class:`huaweicloudsdkelb.v3.FlavorInfo`
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this Flavor.

        :param info: The info of this Flavor.
        :type info: :class:`huaweicloudsdkelb.v3.FlavorInfo`
        """
        self._info = info

    @property
    def name(self):
        r"""Gets the name of this Flavor.

        **参数解释**：规格名称。  **取值范围**： [网络型有如下规格：   - L4_flavor.elb.s1.small: 小型 I   - L4_flavor.elb.s2.small: 小型 II   - L4_flavor.elb.s1.medium: 中型 I   - L4_flavor.elb.s2.medium: 中型 II   - L4_flavor.elb.s1.large: 大型 I   - L4_flavor.elb.s2.large: 大型 II   - L4_flavor.elb.pro.max: 四层弹性规格  应用型有如下规格：   - L7_flavor.elb.s1.small: 小型 I   - L7_flavor.elb.s2.small: 小型 II   - L7_flavor.elb.s1.medium: 中型 I   - L7_flavor.elb.s2.medium: 中型 II   - L7_flavor.elb.s1.large: 大型 I   - L7_flavor.elb.s2.large: 大型 II   - L7_flavor.elb.s1.extra-large: 超大型 I   - L7_flavor.elb.s2.extra-large: 超大型 II   - L7_flavor.elb.pro.max: 七层弹性规格](tag:hws,hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42) [网络型有如下规格：   - L4_flavor.elb.s1.small: 小型 I   - L4_flavor.elb.s2.small: 小型 II   - L4_flavor.elb.s1.medium: 中型 I   - L4_flavor.elb.s2.medium: 中型 II   - L4_flavor.elb.s1.large: 大型 I   - L4_flavor.elb.s2.large: 大型 II   - L4_flavor.elb.pro.max: 四层弹性规格  应用型有如下规格：   - L7_flavor.elb.s1.small: 小型 I   - L7_flavor.elb.s2.small: 小型 II   - L7_flavor.elb.s1.medium: 中型 I   - L7_flavor.elb.s2.medium: 中型 II   - L7_flavor.elb.s1.large: 大型 I   - L7_flavor.elb.s2.large: 大型 II   - L7_flavor.elb.pro.s1.small：弹性规格小型I。已不支持，请勿使用。   - L7_flavor.elb.pro.s1.medium：弹性规格中型I。已不支持，请勿使用。   - L7_flavor.elb.pro.s1.large：弹性规格大型I。已不支持，请勿使用。   - L7_flavor.elb.pro.max: 七层弹性规格](tag:dt,hcso_dt)

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Flavor.

        **参数解释**：规格名称。  **取值范围**： [网络型有如下规格：   - L4_flavor.elb.s1.small: 小型 I   - L4_flavor.elb.s2.small: 小型 II   - L4_flavor.elb.s1.medium: 中型 I   - L4_flavor.elb.s2.medium: 中型 II   - L4_flavor.elb.s1.large: 大型 I   - L4_flavor.elb.s2.large: 大型 II   - L4_flavor.elb.pro.max: 四层弹性规格  应用型有如下规格：   - L7_flavor.elb.s1.small: 小型 I   - L7_flavor.elb.s2.small: 小型 II   - L7_flavor.elb.s1.medium: 中型 I   - L7_flavor.elb.s2.medium: 中型 II   - L7_flavor.elb.s1.large: 大型 I   - L7_flavor.elb.s2.large: 大型 II   - L7_flavor.elb.s1.extra-large: 超大型 I   - L7_flavor.elb.s2.extra-large: 超大型 II   - L7_flavor.elb.pro.max: 七层弹性规格](tag:hws,hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42) [网络型有如下规格：   - L4_flavor.elb.s1.small: 小型 I   - L4_flavor.elb.s2.small: 小型 II   - L4_flavor.elb.s1.medium: 中型 I   - L4_flavor.elb.s2.medium: 中型 II   - L4_flavor.elb.s1.large: 大型 I   - L4_flavor.elb.s2.large: 大型 II   - L4_flavor.elb.pro.max: 四层弹性规格  应用型有如下规格：   - L7_flavor.elb.s1.small: 小型 I   - L7_flavor.elb.s2.small: 小型 II   - L7_flavor.elb.s1.medium: 中型 I   - L7_flavor.elb.s2.medium: 中型 II   - L7_flavor.elb.s1.large: 大型 I   - L7_flavor.elb.s2.large: 大型 II   - L7_flavor.elb.pro.s1.small：弹性规格小型I。已不支持，请勿使用。   - L7_flavor.elb.pro.s1.medium：弹性规格中型I。已不支持，请勿使用。   - L7_flavor.elb.pro.s1.large：弹性规格大型I。已不支持，请勿使用。   - L7_flavor.elb.pro.max: 七层弹性规格](tag:dt,hcso_dt)

        :param name: The name of this Flavor.
        :type name: str
        """
        self._name = name

    @property
    def shared(self):
        r"""Gets the shared of this Flavor.

        **参数解释**：是否公共规格。  **取值范围**： - true表示公共规格，所有租户可见。 - false表示私有规格，为当前租户所有。

        :return: The shared of this Flavor.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        r"""Sets the shared of this Flavor.

        **参数解释**：是否公共规格。  **取值范围**： - true表示公共规格，所有租户可见。 - false表示私有规格，为当前租户所有。

        :param shared: The shared of this Flavor.
        :type shared: bool
        """
        self._shared = shared

    @property
    def project_id(self):
        r"""Gets the project_id of this Flavor.

        **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。

        :return: The project_id of this Flavor.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Flavor.

        **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。

        :param project_id: The project_id of this Flavor.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this Flavor.

        **参数解释**：规格类别。  **取值范围**：   - L4和L7 表示四层网络型和七层应用型flavor。   [- gateway 表示网关型LB的flavor，目前只支持弹性计费类型。当前仅支持欧洲局点。](tag:hws_eu)   - L4_elastic和L7_elastic 表示弹性扩缩容实例的下限规格。已废弃，请勿使用。   - L4_elastic_max、L7_elastic_max[和gateway_elastic_max](tag:hws_eu) 表示弹性扩缩容实例的上限规格。

        :return: The type of this Flavor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Flavor.

        **参数解释**：规格类别。  **取值范围**：   - L4和L7 表示四层网络型和七层应用型flavor。   [- gateway 表示网关型LB的flavor，目前只支持弹性计费类型。当前仅支持欧洲局点。](tag:hws_eu)   - L4_elastic和L7_elastic 表示弹性扩缩容实例的下限规格。已废弃，请勿使用。   - L4_elastic_max、L7_elastic_max[和gateway_elastic_max](tag:hws_eu) 表示弹性扩缩容实例的上限规格。

        :param type: The type of this Flavor.
        :type type: str
        """
        self._type = type

    @property
    def flavor_sold_out(self):
        r"""Gets the flavor_sold_out of this Flavor.

        **参数解释**：[是否售罄。](tag:hws)[是否无法购买该规格的LB。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,ct)  **取值范围**： - true：[已售罄，将](tag:hws)无法购买该规格的LB。 - false：[未售罄，](tag:hws)可购买该规格的LB。

        :return: The flavor_sold_out of this Flavor.
        :rtype: bool
        """
        return self._flavor_sold_out

    @flavor_sold_out.setter
    def flavor_sold_out(self, flavor_sold_out):
        r"""Sets the flavor_sold_out of this Flavor.

        **参数解释**：[是否售罄。](tag:hws)[是否无法购买该规格的LB。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,ct)  **取值范围**： - true：[已售罄，将](tag:hws)无法购买该规格的LB。 - false：[未售罄，](tag:hws)可购买该规格的LB。

        :param flavor_sold_out: The flavor_sold_out of this Flavor.
        :type flavor_sold_out: bool
        """
        self._flavor_sold_out = flavor_sold_out

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this Flavor.

        **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组

        :return: The public_border_group of this Flavor.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this Flavor.

        **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组

        :param public_border_group: The public_border_group of this Flavor.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def category(self):
        r"""Gets the category of this Flavor.

        **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。  **取值范围**：0表示center，21表示homezone，41表示IES。

        :return: The category of this Flavor.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this Flavor.

        **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。  **取值范围**：0表示center，21表示homezone，41表示IES。

        :param category: The category of this Flavor.
        :type category: int
        """
        self._category = category

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
