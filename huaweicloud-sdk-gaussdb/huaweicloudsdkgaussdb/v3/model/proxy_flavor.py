# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'db_type': 'str',
        'az_status': 'object',
        'supported_ipv6': 'bool'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'db_type': 'db_type',
        'az_status': 'az_status',
        'supported_ipv6': 'supported_ipv6'
    }

    def __init__(self, spec_code=None, vcpus=None, ram=None, db_type=None, az_status=None, supported_ipv6=None):
        r"""ProxyFlavor

        The model defined in huaweicloud sdk

        :param spec_code: **参数解释**：  规格码。  **取值范围**：  不涉及。
        :type spec_code: str
        :param vcpus: **参数解释**：  cpu核数。  **取值范围**：  不涉及。
        :type vcpus: str
        :param ram: **参数解释**：  内存。  **取值范围**：  不涉及。
        :type ram: str
        :param db_type: **参数解释**：  数据库类型。  **取值范围**：  不涉及。
        :type db_type: str
        :param az_status: **参数解释**：  az状态。
        :type az_status: object
        :param supported_ipv6: **参数解释**：  是否支持ipv6。  **取值范围**：  - true: 支持ipv6。 - false: 不支持ipv6。
        :type supported_ipv6: bool
        """
        
        

        self._spec_code = None
        self._vcpus = None
        self._ram = None
        self._db_type = None
        self._az_status = None
        self._supported_ipv6 = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if db_type is not None:
            self.db_type = db_type
        if az_status is not None:
            self.az_status = az_status
        if supported_ipv6 is not None:
            self.supported_ipv6 = supported_ipv6

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ProxyFlavor.

        **参数解释**：  规格码。  **取值范围**：  不涉及。

        :return: The spec_code of this ProxyFlavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ProxyFlavor.

        **参数解释**：  规格码。  **取值范围**：  不涉及。

        :param spec_code: The spec_code of this ProxyFlavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def vcpus(self):
        r"""Gets the vcpus of this ProxyFlavor.

        **参数解释**：  cpu核数。  **取值范围**：  不涉及。

        :return: The vcpus of this ProxyFlavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this ProxyFlavor.

        **参数解释**：  cpu核数。  **取值范围**：  不涉及。

        :param vcpus: The vcpus of this ProxyFlavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this ProxyFlavor.

        **参数解释**：  内存。  **取值范围**：  不涉及。

        :return: The ram of this ProxyFlavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ProxyFlavor.

        **参数解释**：  内存。  **取值范围**：  不涉及。

        :param ram: The ram of this ProxyFlavor.
        :type ram: str
        """
        self._ram = ram

    @property
    def db_type(self):
        r"""Gets the db_type of this ProxyFlavor.

        **参数解释**：  数据库类型。  **取值范围**：  不涉及。

        :return: The db_type of this ProxyFlavor.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ProxyFlavor.

        **参数解释**：  数据库类型。  **取值范围**：  不涉及。

        :param db_type: The db_type of this ProxyFlavor.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def az_status(self):
        r"""Gets the az_status of this ProxyFlavor.

        **参数解释**：  az状态。

        :return: The az_status of this ProxyFlavor.
        :rtype: object
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this ProxyFlavor.

        **参数解释**：  az状态。

        :param az_status: The az_status of this ProxyFlavor.
        :type az_status: object
        """
        self._az_status = az_status

    @property
    def supported_ipv6(self):
        r"""Gets the supported_ipv6 of this ProxyFlavor.

        **参数解释**：  是否支持ipv6。  **取值范围**：  - true: 支持ipv6。 - false: 不支持ipv6。

        :return: The supported_ipv6 of this ProxyFlavor.
        :rtype: bool
        """
        return self._supported_ipv6

    @supported_ipv6.setter
    def supported_ipv6(self, supported_ipv6):
        r"""Sets the supported_ipv6 of this ProxyFlavor.

        **参数解释**：  是否支持ipv6。  **取值范围**：  - true: 支持ipv6。 - false: 不支持ipv6。

        :param supported_ipv6: The supported_ipv6 of this ProxyFlavor.
        :type supported_ipv6: bool
        """
        self._supported_ipv6 = supported_ipv6

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
        if not isinstance(other, ProxyFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
