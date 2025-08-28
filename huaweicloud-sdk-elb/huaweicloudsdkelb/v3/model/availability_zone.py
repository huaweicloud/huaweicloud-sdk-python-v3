# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailabilityZone:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'state': 'str',
        'protocol': 'list[str]',
        'public_border_group': 'str',
        'category': 'int',
        'spec_code': 'str'
    }

    attribute_map = {
        'code': 'code',
        'state': 'state',
        'protocol': 'protocol',
        'public_border_group': 'public_border_group',
        'category': 'category',
        'spec_code': 'spec_code'
    }

    def __init__(self, code=None, state=None, protocol=None, public_border_group=None, category=None, spec_code=None):
        r"""AvailabilityZone

        The model defined in huaweicloud sdk

        :param code: **参数解释**：可用区唯一编码。  **取值范围**：不涉及
        :type code: str
        :param state: **参数解释**：可用区状态。  **取值范围**：ACTIVE。
        :type state: str
        :param protocol: [**参数解释**：未售罄的LB规格类别。  **取值范围**：L4 表示网络型LB未售罄；L7 表示应用型LB未售罄。](tag:hws,hws_hk,hws_eu,otc,tlf,ct,sbc,g42,hk_g42,mix,hk_sbc,hws_ocb,dt) [**参数解释**：LB规格类别。  **取值范围**：L4 表示网络型LB；L7 表示应用型LB。](tag:ctc,cmcc,ocb,tm,srg,fcs,fcs_dt,hcso,hcso_dt,hk_vdf)
        :type protocol: list[str]
        :param public_border_group: **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组
        :type public_border_group: str
        :param category: **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。  **取值范围**：0表示center，21表示homezone，41表示IES。
        :type category: int
        :param spec_code: **参数解释**：可用区的产品编码，用于控制台购买ELB前查询定价，仅边缘场景有效。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type spec_code: str
        """
        
        

        self._code = None
        self._state = None
        self._protocol = None
        self._public_border_group = None
        self._category = None
        self._spec_code = None
        self.discriminator = None

        self.code = code
        self.state = state
        self.protocol = protocol
        self.public_border_group = public_border_group
        self.category = category
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def code(self):
        r"""Gets the code of this AvailabilityZone.

        **参数解释**：可用区唯一编码。  **取值范围**：不涉及

        :return: The code of this AvailabilityZone.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AvailabilityZone.

        **参数解释**：可用区唯一编码。  **取值范围**：不涉及

        :param code: The code of this AvailabilityZone.
        :type code: str
        """
        self._code = code

    @property
    def state(self):
        r"""Gets the state of this AvailabilityZone.

        **参数解释**：可用区状态。  **取值范围**：ACTIVE。

        :return: The state of this AvailabilityZone.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this AvailabilityZone.

        **参数解释**：可用区状态。  **取值范围**：ACTIVE。

        :param state: The state of this AvailabilityZone.
        :type state: str
        """
        self._state = state

    @property
    def protocol(self):
        r"""Gets the protocol of this AvailabilityZone.

        [**参数解释**：未售罄的LB规格类别。  **取值范围**：L4 表示网络型LB未售罄；L7 表示应用型LB未售罄。](tag:hws,hws_hk,hws_eu,otc,tlf,ct,sbc,g42,hk_g42,mix,hk_sbc,hws_ocb,dt) [**参数解释**：LB规格类别。  **取值范围**：L4 表示网络型LB；L7 表示应用型LB。](tag:ctc,cmcc,ocb,tm,srg,fcs,fcs_dt,hcso,hcso_dt,hk_vdf)

        :return: The protocol of this AvailabilityZone.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AvailabilityZone.

        [**参数解释**：未售罄的LB规格类别。  **取值范围**：L4 表示网络型LB未售罄；L7 表示应用型LB未售罄。](tag:hws,hws_hk,hws_eu,otc,tlf,ct,sbc,g42,hk_g42,mix,hk_sbc,hws_ocb,dt) [**参数解释**：LB规格类别。  **取值范围**：L4 表示网络型LB；L7 表示应用型LB。](tag:ctc,cmcc,ocb,tm,srg,fcs,fcs_dt,hcso,hcso_dt,hk_vdf)

        :param protocol: The protocol of this AvailabilityZone.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this AvailabilityZone.

        **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组

        :return: The public_border_group of this AvailabilityZone.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this AvailabilityZone.

        **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组

        :param public_border_group: The public_border_group of this AvailabilityZone.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def category(self):
        r"""Gets the category of this AvailabilityZone.

        **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。  **取值范围**：0表示center，21表示homezone，41表示IES。

        :return: The category of this AvailabilityZone.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this AvailabilityZone.

        **参数解释**：可用区子类型编码。该字段主要用于区分在边缘场景下，边缘AZ的类型。  **取值范围**：0表示center，21表示homezone，41表示IES。

        :param category: The category of this AvailabilityZone.
        :type category: int
        """
        self._category = category

    @property
    def spec_code(self):
        r"""Gets the spec_code of this AvailabilityZone.

        **参数解释**：可用区的产品编码，用于控制台购买ELB前查询定价，仅边缘场景有效。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The spec_code of this AvailabilityZone.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this AvailabilityZone.

        **参数解释**：可用区的产品编码，用于控制台购买ELB前查询定价，仅边缘场景有效。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param spec_code: The spec_code of this AvailabilityZone.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, AvailabilityZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
