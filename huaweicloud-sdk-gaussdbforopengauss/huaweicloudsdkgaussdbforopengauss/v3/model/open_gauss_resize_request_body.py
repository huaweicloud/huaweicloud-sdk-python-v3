# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussResizeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'is_auto_pay': 'bool',
        'cn_concurrent_resize_num': 'int',
        'dn_concurrent_resize_num': 'int'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'is_auto_pay': 'is_auto_pay',
        'cn_concurrent_resize_num': 'cn_concurrent_resize_num',
        'dn_concurrent_resize_num': 'dn_concurrent_resize_num'
    }

    def __init__(self, flavor_ref=None, is_auto_pay=None, cn_concurrent_resize_num=None, dn_concurrent_resize_num=None):
        r"""OpenGaussResizeRequestBody

        The model defined in huaweicloud sdk

        :param flavor_ref: **参数解释**: 规格变更的新规格的资源规格编码。参考表1中的“规格编码”列内容获取。参考查询数据库规格 - QueryingInstanceSpecifications中“spec_code”字段获取。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type flavor_ref: str
        :param is_auto_pay: **参数解释**: 包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 **约束限制**: 不涉及。 **取值范围**: - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。  **默认取值**: false
        :type is_auto_pay: bool
        :param cn_concurrent_resize_num: **参数解释**: 指定CN节点的规格变更并行数。 调整CN节点并行变更数可以加快规格变更的过程，建议使用系统默认配置的规格。如需调整，请根据当前系统负载评估剩余CN节点业务负载变化情况，确保业务稳定性和中断时长在可接受范围内。 **约束限制**: 仅对独立部署形态实例生效。 **取值范围**: [1, floor(总协调节点数/2)]，单批次最多变更20个协调节点。 **默认取值**: 1
        :type cn_concurrent_resize_num: int
        :param dn_concurrent_resize_num: **参数解释**: 指定DN节点的规格变更并行数。 调整DN节点并行变更数可以加快规格变更的过程，建议使用系统默认配置的规格。如需调整，建议根据当前系统负载评估短时间内倒换DN节点数量情况，确保业务稳定性和中断时长在可接受范围内。 **约束限制**: 不涉及。 **取值范围**: - 当总分片数&lt;&#x3D;5时，取值范围为[1, 总分片数]。 - 当总分片数＞5时，取值范围为[1, max(floor(分片数/2),5)]，单批次最多变更20个分片。  **默认取值**: 不指定分片并发数时，分为以下两种情况： - 当总分片数&lt;&#x3D;5时，默认一起变更。 - 当总分片数＞5时，默认每次变更5个，最后一批可不足5个。
        :type dn_concurrent_resize_num: int
        """
        
        

        self._flavor_ref = None
        self._is_auto_pay = None
        self._cn_concurrent_resize_num = None
        self._dn_concurrent_resize_num = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if cn_concurrent_resize_num is not None:
            self.cn_concurrent_resize_num = cn_concurrent_resize_num
        if dn_concurrent_resize_num is not None:
            self.dn_concurrent_resize_num = dn_concurrent_resize_num

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this OpenGaussResizeRequestBody.

        **参数解释**: 规格变更的新规格的资源规格编码。参考表1中的“规格编码”列内容获取。参考查询数据库规格 - QueryingInstanceSpecifications中“spec_code”字段获取。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The flavor_ref of this OpenGaussResizeRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this OpenGaussResizeRequestBody.

        **参数解释**: 规格变更的新规格的资源规格编码。参考表1中的“规格编码”列内容获取。参考查询数据库规格 - QueryingInstanceSpecifications中“spec_code”字段获取。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param flavor_ref: The flavor_ref of this OpenGaussResizeRequestBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this OpenGaussResizeRequestBody.

        **参数解释**: 包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 **约束限制**: 不涉及。 **取值范围**: - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。  **默认取值**: false

        :return: The is_auto_pay of this OpenGaussResizeRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this OpenGaussResizeRequestBody.

        **参数解释**: 包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 **约束限制**: 不涉及。 **取值范围**: - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。  **默认取值**: false

        :param is_auto_pay: The is_auto_pay of this OpenGaussResizeRequestBody.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def cn_concurrent_resize_num(self):
        r"""Gets the cn_concurrent_resize_num of this OpenGaussResizeRequestBody.

        **参数解释**: 指定CN节点的规格变更并行数。 调整CN节点并行变更数可以加快规格变更的过程，建议使用系统默认配置的规格。如需调整，请根据当前系统负载评估剩余CN节点业务负载变化情况，确保业务稳定性和中断时长在可接受范围内。 **约束限制**: 仅对独立部署形态实例生效。 **取值范围**: [1, floor(总协调节点数/2)]，单批次最多变更20个协调节点。 **默认取值**: 1

        :return: The cn_concurrent_resize_num of this OpenGaussResizeRequestBody.
        :rtype: int
        """
        return self._cn_concurrent_resize_num

    @cn_concurrent_resize_num.setter
    def cn_concurrent_resize_num(self, cn_concurrent_resize_num):
        r"""Sets the cn_concurrent_resize_num of this OpenGaussResizeRequestBody.

        **参数解释**: 指定CN节点的规格变更并行数。 调整CN节点并行变更数可以加快规格变更的过程，建议使用系统默认配置的规格。如需调整，请根据当前系统负载评估剩余CN节点业务负载变化情况，确保业务稳定性和中断时长在可接受范围内。 **约束限制**: 仅对独立部署形态实例生效。 **取值范围**: [1, floor(总协调节点数/2)]，单批次最多变更20个协调节点。 **默认取值**: 1

        :param cn_concurrent_resize_num: The cn_concurrent_resize_num of this OpenGaussResizeRequestBody.
        :type cn_concurrent_resize_num: int
        """
        self._cn_concurrent_resize_num = cn_concurrent_resize_num

    @property
    def dn_concurrent_resize_num(self):
        r"""Gets the dn_concurrent_resize_num of this OpenGaussResizeRequestBody.

        **参数解释**: 指定DN节点的规格变更并行数。 调整DN节点并行变更数可以加快规格变更的过程，建议使用系统默认配置的规格。如需调整，建议根据当前系统负载评估短时间内倒换DN节点数量情况，确保业务稳定性和中断时长在可接受范围内。 **约束限制**: 不涉及。 **取值范围**: - 当总分片数<=5时，取值范围为[1, 总分片数]。 - 当总分片数＞5时，取值范围为[1, max(floor(分片数/2),5)]，单批次最多变更20个分片。  **默认取值**: 不指定分片并发数时，分为以下两种情况： - 当总分片数<=5时，默认一起变更。 - 当总分片数＞5时，默认每次变更5个，最后一批可不足5个。

        :return: The dn_concurrent_resize_num of this OpenGaussResizeRequestBody.
        :rtype: int
        """
        return self._dn_concurrent_resize_num

    @dn_concurrent_resize_num.setter
    def dn_concurrent_resize_num(self, dn_concurrent_resize_num):
        r"""Sets the dn_concurrent_resize_num of this OpenGaussResizeRequestBody.

        **参数解释**: 指定DN节点的规格变更并行数。 调整DN节点并行变更数可以加快规格变更的过程，建议使用系统默认配置的规格。如需调整，建议根据当前系统负载评估短时间内倒换DN节点数量情况，确保业务稳定性和中断时长在可接受范围内。 **约束限制**: 不涉及。 **取值范围**: - 当总分片数<=5时，取值范围为[1, 总分片数]。 - 当总分片数＞5时，取值范围为[1, max(floor(分片数/2),5)]，单批次最多变更20个分片。  **默认取值**: 不指定分片并发数时，分为以下两种情况： - 当总分片数<=5时，默认一起变更。 - 当总分片数＞5时，默认每次变更5个，最后一批可不足5个。

        :param dn_concurrent_resize_num: The dn_concurrent_resize_num of this OpenGaussResizeRequestBody.
        :type dn_concurrent_resize_num: int
        """
        self._dn_concurrent_resize_num = dn_concurrent_resize_num

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
        if not isinstance(other, OpenGaussResizeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
