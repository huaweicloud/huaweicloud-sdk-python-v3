# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BillingResource:

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
        'unit_num': 'int'
    }

    attribute_map = {
        'code': 'code',
        'unit_num': 'unit_num'
    }

    def __init__(self, code=None, unit_num=None):
        r"""BillingResource

        The model defined in huaweicloud sdk

        :param code: **参数解释：** 计费码。 **取值范围：** 不涉及。
        :type code: str
        :param unit_num: **参数解释：** 计费单元。 **取值范围：** 不涉及。
        :type unit_num: int
        """
        
        

        self._code = None
        self._unit_num = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if unit_num is not None:
            self.unit_num = unit_num

    @property
    def code(self):
        r"""Gets the code of this BillingResource.

        **参数解释：** 计费码。 **取值范围：** 不涉及。

        :return: The code of this BillingResource.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BillingResource.

        **参数解释：** 计费码。 **取值范围：** 不涉及。

        :param code: The code of this BillingResource.
        :type code: str
        """
        self._code = code

    @property
    def unit_num(self):
        r"""Gets the unit_num of this BillingResource.

        **参数解释：** 计费单元。 **取值范围：** 不涉及。

        :return: The unit_num of this BillingResource.
        :rtype: int
        """
        return self._unit_num

    @unit_num.setter
    def unit_num(self, unit_num):
        r"""Sets the unit_num of this BillingResource.

        **参数解释：** 计费单元。 **取值范围：** 不涉及。

        :param unit_num: The unit_num of this BillingResource.
        :type unit_num: int
        """
        self._unit_num = unit_num

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
        if not isinstance(other, BillingResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
