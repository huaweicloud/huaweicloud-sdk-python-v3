# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResizeFlavorRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'spec_code': 'str',
        'delay': 'bool',
        'auto_pay': 'bool',
        'occupy_ip': 'bool'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'spec_code': 'spec_code',
        'delay': 'delay',
        'auto_pay': 'auto_pay',
        'occupy_ip': 'occupy_ip'
    }

    def __init__(self, instance_ids=None, spec_code=None, delay=None, auto_pay=None, occupy_ip=None):
        r"""BatchResizeFlavorRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: **参数解释**：   实例ID列表。   **约束限制**：  一次最多下发10个实例。   **取值范围**：  不涉及。  **默认取值**：   不涉及。
        :type instance_ids: list[str]
        :param spec_code: **参数解释**：  资源规格编码。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   不涉及。
        :type spec_code: str
        :param delay: **参数解释**：  是否进行定时规格变更。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   false
        :type delay: bool
        :param auto_pay: **参数解释**：  变更包周期实例的规格时可指定，表示是否自动从客户的账户中支付。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   false
        :type auto_pay: bool
        :param occupy_ip: **参数解释**：  表示是否占用ip进行规格变更。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   true
        :type occupy_ip: bool
        """
        
        

        self._instance_ids = None
        self._spec_code = None
        self._delay = None
        self._auto_pay = None
        self._occupy_ip = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.spec_code = spec_code
        if delay is not None:
            self.delay = delay
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if occupy_ip is not None:
            self.occupy_ip = occupy_ip

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchResizeFlavorRequestBody.

        **参数解释**：   实例ID列表。   **约束限制**：  一次最多下发10个实例。   **取值范围**：  不涉及。  **默认取值**：   不涉及。

        :return: The instance_ids of this BatchResizeFlavorRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchResizeFlavorRequestBody.

        **参数解释**：   实例ID列表。   **约束限制**：  一次最多下发10个实例。   **取值范围**：  不涉及。  **默认取值**：   不涉及。

        :param instance_ids: The instance_ids of this BatchResizeFlavorRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def spec_code(self):
        r"""Gets the spec_code of this BatchResizeFlavorRequestBody.

        **参数解释**：  资源规格编码。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   不涉及。

        :return: The spec_code of this BatchResizeFlavorRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this BatchResizeFlavorRequestBody.

        **参数解释**：  资源规格编码。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   不涉及。

        :param spec_code: The spec_code of this BatchResizeFlavorRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def delay(self):
        r"""Gets the delay of this BatchResizeFlavorRequestBody.

        **参数解释**：  是否进行定时规格变更。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   false

        :return: The delay of this BatchResizeFlavorRequestBody.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this BatchResizeFlavorRequestBody.

        **参数解释**：  是否进行定时规格变更。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   false

        :param delay: The delay of this BatchResizeFlavorRequestBody.
        :type delay: bool
        """
        self._delay = delay

    @property
    def auto_pay(self):
        r"""Gets the auto_pay of this BatchResizeFlavorRequestBody.

        **参数解释**：  变更包周期实例的规格时可指定，表示是否自动从客户的账户中支付。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   false

        :return: The auto_pay of this BatchResizeFlavorRequestBody.
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        r"""Sets the auto_pay of this BatchResizeFlavorRequestBody.

        **参数解释**：  变更包周期实例的规格时可指定，表示是否自动从客户的账户中支付。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   false

        :param auto_pay: The auto_pay of this BatchResizeFlavorRequestBody.
        :type auto_pay: bool
        """
        self._auto_pay = auto_pay

    @property
    def occupy_ip(self):
        r"""Gets the occupy_ip of this BatchResizeFlavorRequestBody.

        **参数解释**：  表示是否占用ip进行规格变更。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   true

        :return: The occupy_ip of this BatchResizeFlavorRequestBody.
        :rtype: bool
        """
        return self._occupy_ip

    @occupy_ip.setter
    def occupy_ip(self, occupy_ip):
        r"""Sets the occupy_ip of this BatchResizeFlavorRequestBody.

        **参数解释**：  表示是否占用ip进行规格变更。  **约束限制**：   不涉及。   **取值范围**：  不涉及。   **默认取值**：   true

        :param occupy_ip: The occupy_ip of this BatchResizeFlavorRequestBody.
        :type occupy_ip: bool
        """
        self._occupy_ip = occupy_ip

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
        if not isinstance(other, BatchResizeFlavorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
