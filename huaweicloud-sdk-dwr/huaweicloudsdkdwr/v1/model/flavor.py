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
        'cu': 'str',
        'num': 'int'
    }

    attribute_map = {
        'cu': 'cu',
        'num': 'num'
    }

    def __init__(self, cu=None, num=None):
        r"""Flavor

        The model defined in huaweicloud sdk

        :param cu: **参数解释：** CU规格。 **约束限制：** 不涉及。 **取值范围：** xlarge, 2xlarge, 4xlarge, 8xlarge, 16xlarge。 **默认取值:** 不涉及。
        :type cu: str
        :param num: **参数解释：** 选择CU规格的数量。 **约束限制：** 不能超过CU配额，如有大量需求，请提工单申请。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type num: int
        """
        
        

        self._cu = None
        self._num = None
        self.discriminator = None

        self.cu = cu
        self.num = num

    @property
    def cu(self):
        r"""Gets the cu of this Flavor.

        **参数解释：** CU规格。 **约束限制：** 不涉及。 **取值范围：** xlarge, 2xlarge, 4xlarge, 8xlarge, 16xlarge。 **默认取值:** 不涉及。

        :return: The cu of this Flavor.
        :rtype: str
        """
        return self._cu

    @cu.setter
    def cu(self, cu):
        r"""Sets the cu of this Flavor.

        **参数解释：** CU规格。 **约束限制：** 不涉及。 **取值范围：** xlarge, 2xlarge, 4xlarge, 8xlarge, 16xlarge。 **默认取值:** 不涉及。

        :param cu: The cu of this Flavor.
        :type cu: str
        """
        self._cu = cu

    @property
    def num(self):
        r"""Gets the num of this Flavor.

        **参数解释：** 选择CU规格的数量。 **约束限制：** 不能超过CU配额，如有大量需求，请提工单申请。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The num of this Flavor.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this Flavor.

        **参数解释：** 选择CU规格的数量。 **约束限制：** 不能超过CU配额，如有大量需求，请提工单申请。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param num: The num of this Flavor.
        :type num: int
        """
        self._num = num

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
