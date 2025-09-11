# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeDistributionOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'int',
        'availability_zone': 'str',
        'flavor_ref': 'str',
        'configuration_id': 'str'
    }

    attribute_map = {
        'num': 'num',
        'availability_zone': 'availability_zone',
        'flavor_ref': 'flavor_ref',
        'configuration_id': 'configuration_id'
    }

    def __init__(self, num=None, availability_zone=None, flavor_ref=None, configuration_id=None):
        r"""NodeDistributionOption

        The model defined in huaweicloud sdk

        :param num: **参数解释**: 对应可用区增加的只读节点数量。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type num: int
        :param availability_zone: **参数解释**: 可用分区。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type availability_zone: str
        :param flavor_ref: **参数解释**: 规格码。 **约束限制**: 不涉及。 **取值范围**: 非空。 **默认取值**: 不涉及。
        :type flavor_ref: str
        :param configuration_id: **参数解释**: 只读参数组ID **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type configuration_id: str
        """
        
        

        self._num = None
        self._availability_zone = None
        self._flavor_ref = None
        self._configuration_id = None
        self.discriminator = None

        self.num = num
        self.availability_zone = availability_zone
        self.flavor_ref = flavor_ref
        self.configuration_id = configuration_id

    @property
    def num(self):
        r"""Gets the num of this NodeDistributionOption.

        **参数解释**: 对应可用区增加的只读节点数量。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The num of this NodeDistributionOption.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this NodeDistributionOption.

        **参数解释**: 对应可用区增加的只读节点数量。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param num: The num of this NodeDistributionOption.
        :type num: int
        """
        self._num = num

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this NodeDistributionOption.

        **参数解释**: 可用分区。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The availability_zone of this NodeDistributionOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this NodeDistributionOption.

        **参数解释**: 可用分区。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param availability_zone: The availability_zone of this NodeDistributionOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this NodeDistributionOption.

        **参数解释**: 规格码。 **约束限制**: 不涉及。 **取值范围**: 非空。 **默认取值**: 不涉及。

        :return: The flavor_ref of this NodeDistributionOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this NodeDistributionOption.

        **参数解释**: 规格码。 **约束限制**: 不涉及。 **取值范围**: 非空。 **默认取值**: 不涉及。

        :param flavor_ref: The flavor_ref of this NodeDistributionOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this NodeDistributionOption.

        **参数解释**: 只读参数组ID **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The configuration_id of this NodeDistributionOption.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this NodeDistributionOption.

        **参数解释**: 只读参数组ID **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param configuration_id: The configuration_id of this NodeDistributionOption.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

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
        if not isinstance(other, NodeDistributionOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
