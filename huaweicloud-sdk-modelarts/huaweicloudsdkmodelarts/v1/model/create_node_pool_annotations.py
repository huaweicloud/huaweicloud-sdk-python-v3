# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNodePoolAnnotations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_billing_mode': 'str',
        'os_modelarts_period_num': 'str',
        'os_modelarts_period_type': 'str',
        'os_modelarts_auto_renew': 'str',
        'os_modelarts_promotion_info': 'str',
        'os_modelarts_service_console_url': 'str',
        'os_modelarts_order_id': 'str'
    }

    attribute_map = {
        'os_modelarts_billing_mode': 'os.modelarts/billing.mode',
        'os_modelarts_period_num': 'os.modelarts/period.num',
        'os_modelarts_period_type': 'os.modelarts/period.type',
        'os_modelarts_auto_renew': 'os.modelarts/auto.renew',
        'os_modelarts_promotion_info': 'os.modelarts/promotion.info',
        'os_modelarts_service_console_url': 'os.modelarts/service.console.url',
        'os_modelarts_order_id': 'os.modelarts/order.id'
    }

    def __init__(self, os_modelarts_billing_mode=None, os_modelarts_period_num=None, os_modelarts_period_type=None, os_modelarts_auto_renew=None, os_modelarts_promotion_info=None, os_modelarts_service_console_url=None, os_modelarts_order_id=None):
        r"""CreateNodePoolAnnotations

        The model defined in huaweicloud sdk

        :param os_modelarts_billing_mode: **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：按需计费 - 1：包周期计费 **默认取值**：不涉及。
        :type os_modelarts_billing_mode: str
        :param os_modelarts_period_num: **参数解释**：包周期订购周期，比如2。当计费模式为包周期时该参数必传。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_period_num: str
        :param os_modelarts_period_type: **参数解释**：包周期订购类型。当计费模式为包周期时该参数必传 **约束限制**：不涉及。 **取值范围**：可选值如下： - 2：月 - 3：年 - 4：小时 **默认取值**：不涉及。
        :type os_modelarts_period_type: str
        :param os_modelarts_auto_renew: **参数解释**：是否自动续费。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：不自动续费 - 1：自动续费 **默认取值**：0。
        :type os_modelarts_auto_renew: str
        :param os_modelarts_promotion_info: **参数解释**：用户在运营平台选择的折扣信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_promotion_info: str
        :param os_modelarts_service_console_url: **参数解释**：订购订单支付完成后跳转的url地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_service_console_url: str
        :param os_modelarts_order_id: **参数解释**：订单id，包周期资源创建或者计费模式变更的时候该参数必需。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_order_id: str
        """
        
        

        self._os_modelarts_billing_mode = None
        self._os_modelarts_period_num = None
        self._os_modelarts_period_type = None
        self._os_modelarts_auto_renew = None
        self._os_modelarts_promotion_info = None
        self._os_modelarts_service_console_url = None
        self._os_modelarts_order_id = None
        self.discriminator = None

        if os_modelarts_billing_mode is not None:
            self.os_modelarts_billing_mode = os_modelarts_billing_mode
        if os_modelarts_period_num is not None:
            self.os_modelarts_period_num = os_modelarts_period_num
        if os_modelarts_period_type is not None:
            self.os_modelarts_period_type = os_modelarts_period_type
        if os_modelarts_auto_renew is not None:
            self.os_modelarts_auto_renew = os_modelarts_auto_renew
        if os_modelarts_promotion_info is not None:
            self.os_modelarts_promotion_info = os_modelarts_promotion_info
        if os_modelarts_service_console_url is not None:
            self.os_modelarts_service_console_url = os_modelarts_service_console_url
        if os_modelarts_order_id is not None:
            self.os_modelarts_order_id = os_modelarts_order_id

    @property
    def os_modelarts_billing_mode(self):
        r"""Gets the os_modelarts_billing_mode of this CreateNodePoolAnnotations.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：按需计费 - 1：包周期计费 **默认取值**：不涉及。

        :return: The os_modelarts_billing_mode of this CreateNodePoolAnnotations.
        :rtype: str
        """
        return self._os_modelarts_billing_mode

    @os_modelarts_billing_mode.setter
    def os_modelarts_billing_mode(self, os_modelarts_billing_mode):
        r"""Sets the os_modelarts_billing_mode of this CreateNodePoolAnnotations.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：按需计费 - 1：包周期计费 **默认取值**：不涉及。

        :param os_modelarts_billing_mode: The os_modelarts_billing_mode of this CreateNodePoolAnnotations.
        :type os_modelarts_billing_mode: str
        """
        self._os_modelarts_billing_mode = os_modelarts_billing_mode

    @property
    def os_modelarts_period_num(self):
        r"""Gets the os_modelarts_period_num of this CreateNodePoolAnnotations.

        **参数解释**：包周期订购周期，比如2。当计费模式为包周期时该参数必传。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_period_num of this CreateNodePoolAnnotations.
        :rtype: str
        """
        return self._os_modelarts_period_num

    @os_modelarts_period_num.setter
    def os_modelarts_period_num(self, os_modelarts_period_num):
        r"""Sets the os_modelarts_period_num of this CreateNodePoolAnnotations.

        **参数解释**：包周期订购周期，比如2。当计费模式为包周期时该参数必传。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_period_num: The os_modelarts_period_num of this CreateNodePoolAnnotations.
        :type os_modelarts_period_num: str
        """
        self._os_modelarts_period_num = os_modelarts_period_num

    @property
    def os_modelarts_period_type(self):
        r"""Gets the os_modelarts_period_type of this CreateNodePoolAnnotations.

        **参数解释**：包周期订购类型。当计费模式为包周期时该参数必传 **约束限制**：不涉及。 **取值范围**：可选值如下： - 2：月 - 3：年 - 4：小时 **默认取值**：不涉及。

        :return: The os_modelarts_period_type of this CreateNodePoolAnnotations.
        :rtype: str
        """
        return self._os_modelarts_period_type

    @os_modelarts_period_type.setter
    def os_modelarts_period_type(self, os_modelarts_period_type):
        r"""Sets the os_modelarts_period_type of this CreateNodePoolAnnotations.

        **参数解释**：包周期订购类型。当计费模式为包周期时该参数必传 **约束限制**：不涉及。 **取值范围**：可选值如下： - 2：月 - 3：年 - 4：小时 **默认取值**：不涉及。

        :param os_modelarts_period_type: The os_modelarts_period_type of this CreateNodePoolAnnotations.
        :type os_modelarts_period_type: str
        """
        self._os_modelarts_period_type = os_modelarts_period_type

    @property
    def os_modelarts_auto_renew(self):
        r"""Gets the os_modelarts_auto_renew of this CreateNodePoolAnnotations.

        **参数解释**：是否自动续费。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：不自动续费 - 1：自动续费 **默认取值**：0。

        :return: The os_modelarts_auto_renew of this CreateNodePoolAnnotations.
        :rtype: str
        """
        return self._os_modelarts_auto_renew

    @os_modelarts_auto_renew.setter
    def os_modelarts_auto_renew(self, os_modelarts_auto_renew):
        r"""Sets the os_modelarts_auto_renew of this CreateNodePoolAnnotations.

        **参数解释**：是否自动续费。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：不自动续费 - 1：自动续费 **默认取值**：0。

        :param os_modelarts_auto_renew: The os_modelarts_auto_renew of this CreateNodePoolAnnotations.
        :type os_modelarts_auto_renew: str
        """
        self._os_modelarts_auto_renew = os_modelarts_auto_renew

    @property
    def os_modelarts_promotion_info(self):
        r"""Gets the os_modelarts_promotion_info of this CreateNodePoolAnnotations.

        **参数解释**：用户在运营平台选择的折扣信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_promotion_info of this CreateNodePoolAnnotations.
        :rtype: str
        """
        return self._os_modelarts_promotion_info

    @os_modelarts_promotion_info.setter
    def os_modelarts_promotion_info(self, os_modelarts_promotion_info):
        r"""Sets the os_modelarts_promotion_info of this CreateNodePoolAnnotations.

        **参数解释**：用户在运营平台选择的折扣信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_promotion_info: The os_modelarts_promotion_info of this CreateNodePoolAnnotations.
        :type os_modelarts_promotion_info: str
        """
        self._os_modelarts_promotion_info = os_modelarts_promotion_info

    @property
    def os_modelarts_service_console_url(self):
        r"""Gets the os_modelarts_service_console_url of this CreateNodePoolAnnotations.

        **参数解释**：订购订单支付完成后跳转的url地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_service_console_url of this CreateNodePoolAnnotations.
        :rtype: str
        """
        return self._os_modelarts_service_console_url

    @os_modelarts_service_console_url.setter
    def os_modelarts_service_console_url(self, os_modelarts_service_console_url):
        r"""Sets the os_modelarts_service_console_url of this CreateNodePoolAnnotations.

        **参数解释**：订购订单支付完成后跳转的url地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_service_console_url: The os_modelarts_service_console_url of this CreateNodePoolAnnotations.
        :type os_modelarts_service_console_url: str
        """
        self._os_modelarts_service_console_url = os_modelarts_service_console_url

    @property
    def os_modelarts_order_id(self):
        r"""Gets the os_modelarts_order_id of this CreateNodePoolAnnotations.

        **参数解释**：订单id，包周期资源创建或者计费模式变更的时候该参数必需。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_order_id of this CreateNodePoolAnnotations.
        :rtype: str
        """
        return self._os_modelarts_order_id

    @os_modelarts_order_id.setter
    def os_modelarts_order_id(self, os_modelarts_order_id):
        r"""Sets the os_modelarts_order_id of this CreateNodePoolAnnotations.

        **参数解释**：订单id，包周期资源创建或者计费模式变更的时候该参数必需。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_order_id: The os_modelarts_order_id of this CreateNodePoolAnnotations.
        :type os_modelarts_order_id: str
        """
        self._os_modelarts_order_id = os_modelarts_order_id

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
        if not isinstance(other, CreateNodePoolAnnotations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
