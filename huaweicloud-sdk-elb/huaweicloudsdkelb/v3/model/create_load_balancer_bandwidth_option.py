# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadBalancerBandwidthOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'size': 'int',
        'charge_mode': 'str',
        'share_type': 'str',
        'billing_info': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'charge_mode': 'charge_mode',
        'share_type': 'share_type',
        'billing_info': 'billing_info',
        'id': 'id'
    }

    def __init__(self, name=None, size=None, charge_mode=None, share_type=None, billing_info=None, id=None):
        r"""CreateLoadBalancerBandwidthOption

        The model defined in huaweicloud sdk

        :param name: **参数解释**：带宽名称。  **约束限制**： - 如果share_type是PER，该字段是必选。 - 如果bandwidth对象的id有值，该字段被忽略。  **取值范围**：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  **默认取值**：不涉及
        :type name: str
        :param size: **参数解释**：带宽大小。  **约束限制**： - 当id字段为null时，size是必须的。 - 调整带宽时的最小单位会根据带宽范围不同存在差异。   + 小于等于300Mbit/s: 默认最小单位为1Mbit/s。   + 300Mbit/s~1000Mbit/s: 默认最小单位为50Mbit/s。   + 大于1000Mbit/s: 默认最小单位为500Mbit/s。  **取值范围**：默认1Mbit/s~2000Mbit/s(具体范围以各区域配置为准,请参见控制台对应页面显示)。  **默认取值**：不涉及
        :type size: int
        :param charge_mode: **参数解释**：计费模式。  **约束限制**：当id字段为null时，charge_mode是必须的。 [当前仅支持traffic按流量计费。](tag:hws_eu,g42,hk_g42,dt,hcso_dt)  **取值范围**：  - bandwidth：按带宽计费。  - traffic： 按流量计费。  **默认取值**：不涉及
        :type charge_mode: str
        :param share_type: **参数解释**：带宽类型。  **约束限制**： - 当id字段为null时，share_type是必须的。当id不为null时，该字段被忽略。 - 该字段为WHOLE时,必须指定带宽ID。 - IPv6的EIP不支持WHOLE类型带宽。  **取值范围**： - PER：独享带宽。 - WHOLE：共享带宽。  **默认取值**：不涉及
        :type share_type: str
        :param billing_info: **参数解释**：资源计费信息。  [**约束限制**： 如果billing_info不为空，说明是包周期计费的带宽，否则为按需计费的带宽。](tag:hws) [**约束限制**：不涉及](tag:hws,hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)
        :type billing_info: str
        :param id: **参数解释**：共享带宽ID。使用已存在的共享带宽。  **约束限制**：必须是已存在共享带宽ID。在预付费的情况下，不填该字段。该字段取空字符串时，会被忽略。  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: str
        """
        
        

        self._name = None
        self._size = None
        self._charge_mode = None
        self._share_type = None
        self._billing_info = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if share_type is not None:
            self.share_type = share_type
        if billing_info is not None:
            self.billing_info = billing_info
        if id is not None:
            self.id = id

    @property
    def name(self):
        r"""Gets the name of this CreateLoadBalancerBandwidthOption.

        **参数解释**：带宽名称。  **约束限制**： - 如果share_type是PER，该字段是必选。 - 如果bandwidth对象的id有值，该字段被忽略。  **取值范围**：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  **默认取值**：不涉及

        :return: The name of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateLoadBalancerBandwidthOption.

        **参数解释**：带宽名称。  **约束限制**： - 如果share_type是PER，该字段是必选。 - 如果bandwidth对象的id有值，该字段被忽略。  **取值范围**：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  **默认取值**：不涉及

        :param name: The name of this CreateLoadBalancerBandwidthOption.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this CreateLoadBalancerBandwidthOption.

        **参数解释**：带宽大小。  **约束限制**： - 当id字段为null时，size是必须的。 - 调整带宽时的最小单位会根据带宽范围不同存在差异。   + 小于等于300Mbit/s: 默认最小单位为1Mbit/s。   + 300Mbit/s~1000Mbit/s: 默认最小单位为50Mbit/s。   + 大于1000Mbit/s: 默认最小单位为500Mbit/s。  **取值范围**：默认1Mbit/s~2000Mbit/s(具体范围以各区域配置为准,请参见控制台对应页面显示)。  **默认取值**：不涉及

        :return: The size of this CreateLoadBalancerBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CreateLoadBalancerBandwidthOption.

        **参数解释**：带宽大小。  **约束限制**： - 当id字段为null时，size是必须的。 - 调整带宽时的最小单位会根据带宽范围不同存在差异。   + 小于等于300Mbit/s: 默认最小单位为1Mbit/s。   + 300Mbit/s~1000Mbit/s: 默认最小单位为50Mbit/s。   + 大于1000Mbit/s: 默认最小单位为500Mbit/s。  **取值范围**：默认1Mbit/s~2000Mbit/s(具体范围以各区域配置为准,请参见控制台对应页面显示)。  **默认取值**：不涉及

        :param size: The size of this CreateLoadBalancerBandwidthOption.
        :type size: int
        """
        self._size = size

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this CreateLoadBalancerBandwidthOption.

        **参数解释**：计费模式。  **约束限制**：当id字段为null时，charge_mode是必须的。 [当前仅支持traffic按流量计费。](tag:hws_eu,g42,hk_g42,dt,hcso_dt)  **取值范围**：  - bandwidth：按带宽计费。  - traffic： 按流量计费。  **默认取值**：不涉及

        :return: The charge_mode of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this CreateLoadBalancerBandwidthOption.

        **参数解释**：计费模式。  **约束限制**：当id字段为null时，charge_mode是必须的。 [当前仅支持traffic按流量计费。](tag:hws_eu,g42,hk_g42,dt,hcso_dt)  **取值范围**：  - bandwidth：按带宽计费。  - traffic： 按流量计费。  **默认取值**：不涉及

        :param charge_mode: The charge_mode of this CreateLoadBalancerBandwidthOption.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def share_type(self):
        r"""Gets the share_type of this CreateLoadBalancerBandwidthOption.

        **参数解释**：带宽类型。  **约束限制**： - 当id字段为null时，share_type是必须的。当id不为null时，该字段被忽略。 - 该字段为WHOLE时,必须指定带宽ID。 - IPv6的EIP不支持WHOLE类型带宽。  **取值范围**： - PER：独享带宽。 - WHOLE：共享带宽。  **默认取值**：不涉及

        :return: The share_type of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this CreateLoadBalancerBandwidthOption.

        **参数解释**：带宽类型。  **约束限制**： - 当id字段为null时，share_type是必须的。当id不为null时，该字段被忽略。 - 该字段为WHOLE时,必须指定带宽ID。 - IPv6的EIP不支持WHOLE类型带宽。  **取值范围**： - PER：独享带宽。 - WHOLE：共享带宽。  **默认取值**：不涉及

        :param share_type: The share_type of this CreateLoadBalancerBandwidthOption.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def billing_info(self):
        r"""Gets the billing_info of this CreateLoadBalancerBandwidthOption.

        **参数解释**：资源计费信息。  [**约束限制**： 如果billing_info不为空，说明是包周期计费的带宽，否则为按需计费的带宽。](tag:hws) [**约束限制**：不涉及](tag:hws,hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)

        :return: The billing_info of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this CreateLoadBalancerBandwidthOption.

        **参数解释**：资源计费信息。  [**约束限制**： 如果billing_info不为空，说明是包周期计费的带宽，否则为按需计费的带宽。](tag:hws) [**约束限制**：不涉及](tag:hws,hws_hk,hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)

        :param billing_info: The billing_info of this CreateLoadBalancerBandwidthOption.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def id(self):
        r"""Gets the id of this CreateLoadBalancerBandwidthOption.

        **参数解释**：共享带宽ID。使用已存在的共享带宽。  **约束限制**：必须是已存在共享带宽ID。在预付费的情况下，不填该字段。该字段取空字符串时，会被忽略。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateLoadBalancerBandwidthOption.

        **参数解释**：共享带宽ID。使用已存在的共享带宽。  **约束限制**：必须是已存在共享带宽ID。在预付费的情况下，不填该字段。该字段取空字符串时，会被忽略。  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this CreateLoadBalancerBandwidthOption.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, CreateLoadBalancerBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
