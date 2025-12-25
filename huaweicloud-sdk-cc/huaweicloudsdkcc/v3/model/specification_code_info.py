# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecificationCodeInfo:

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
        'billing_mode': 'int',
        'max_bandwidth': 'int',
        'mim_bandwidth': 'int'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'billing_mode': 'billing_mode',
        'max_bandwidth': 'max_bandwidth',
        'mim_bandwidth': 'mim_bandwidth'
    }

    def __init__(self, spec_code=None, billing_mode=None, max_bandwidth=None, mim_bandwidth=None):
        r"""SpecificationCodeInfo

        The model defined in huaweicloud sdk

        :param spec_code: 带宽包实例的规格编码。
        :type spec_code: str
        :param billing_mode: 带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期。 2：国际站包周期。 3：大陆站按需计费。 4：国际站按需计费。 5：大陆站按95方式计费。 6：国际站按95方式计费。 7：大陆站按日95方式计费。 8：国际站按日95方式计费。
        :type billing_mode: int
        :param max_bandwidth: 最大带宽。
        :type max_bandwidth: int
        :param mim_bandwidth: 最小带宽。
        :type mim_bandwidth: int
        """
        
        

        self._spec_code = None
        self._billing_mode = None
        self._max_bandwidth = None
        self._mim_bandwidth = None
        self.discriminator = None

        self.spec_code = spec_code
        self.billing_mode = billing_mode
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if mim_bandwidth is not None:
            self.mim_bandwidth = mim_bandwidth

    @property
    def spec_code(self):
        r"""Gets the spec_code of this SpecificationCodeInfo.

        带宽包实例的规格编码。

        :return: The spec_code of this SpecificationCodeInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this SpecificationCodeInfo.

        带宽包实例的规格编码。

        :param spec_code: The spec_code of this SpecificationCodeInfo.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this SpecificationCodeInfo.

        带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期。 2：国际站包周期。 3：大陆站按需计费。 4：国际站按需计费。 5：大陆站按95方式计费。 6：国际站按95方式计费。 7：大陆站按日95方式计费。 8：国际站按日95方式计费。

        :return: The billing_mode of this SpecificationCodeInfo.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this SpecificationCodeInfo.

        带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期。 2：国际站包周期。 3：大陆站按需计费。 4：国际站按需计费。 5：大陆站按95方式计费。 6：国际站按95方式计费。 7：大陆站按日95方式计费。 8：国际站按日95方式计费。

        :param billing_mode: The billing_mode of this SpecificationCodeInfo.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def max_bandwidth(self):
        r"""Gets the max_bandwidth of this SpecificationCodeInfo.

        最大带宽。

        :return: The max_bandwidth of this SpecificationCodeInfo.
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        r"""Sets the max_bandwidth of this SpecificationCodeInfo.

        最大带宽。

        :param max_bandwidth: The max_bandwidth of this SpecificationCodeInfo.
        :type max_bandwidth: int
        """
        self._max_bandwidth = max_bandwidth

    @property
    def mim_bandwidth(self):
        r"""Gets the mim_bandwidth of this SpecificationCodeInfo.

        最小带宽。

        :return: The mim_bandwidth of this SpecificationCodeInfo.
        :rtype: int
        """
        return self._mim_bandwidth

    @mim_bandwidth.setter
    def mim_bandwidth(self, mim_bandwidth):
        r"""Sets the mim_bandwidth of this SpecificationCodeInfo.

        最小带宽。

        :param mim_bandwidth: The mim_bandwidth of this SpecificationCodeInfo.
        :type mim_bandwidth: int
        """
        self._mim_bandwidth = mim_bandwidth

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
        if not isinstance(other, SpecificationCodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
