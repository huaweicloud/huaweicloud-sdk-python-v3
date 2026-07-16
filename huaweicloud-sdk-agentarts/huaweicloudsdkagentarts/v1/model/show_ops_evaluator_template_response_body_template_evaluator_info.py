# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'benchmark': 'str',
        'user_manual_url': 'str',
        'vendor': 'str',
        'vendor_url': 'str'
    }

    attribute_map = {
        'benchmark': 'benchmark',
        'user_manual_url': 'user_manual_url',
        'vendor': 'vendor',
        'vendor_url': 'vendor_url'
    }

    def __init__(self, benchmark=None, user_manual_url=None, vendor=None, vendor_url=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo

        The model defined in huaweicloud sdk

        :param benchmark: **参数解释：** 评估器的测试标准或参考系。 **取值范围：** 不涉及。 
        :type benchmark: str
        :param user_manual_url: **参数解释：** 指向评估器用户手册的网址。 **取值范围：** 不涉及。 
        :type user_manual_url: str
        :param vendor: **参数解释：** 评估器的提供方标识。 **取值范围：** 不涉及。 
        :type vendor: str
        :param vendor_url: **参数解释：** 供应商的官方网址。 **取值范围：** 不涉及。 
        :type vendor_url: str
        """
        
        

        self._benchmark = None
        self._user_manual_url = None
        self._vendor = None
        self._vendor_url = None
        self.discriminator = None

        if benchmark is not None:
            self.benchmark = benchmark
        if user_manual_url is not None:
            self.user_manual_url = user_manual_url
        if vendor is not None:
            self.vendor = vendor
        if vendor_url is not None:
            self.vendor_url = vendor_url

    @property
    def benchmark(self):
        r"""Gets the benchmark of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 评估器的测试标准或参考系。 **取值范围：** 不涉及。 

        :return: The benchmark of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :rtype: str
        """
        return self._benchmark

    @benchmark.setter
    def benchmark(self, benchmark):
        r"""Sets the benchmark of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 评估器的测试标准或参考系。 **取值范围：** 不涉及。 

        :param benchmark: The benchmark of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :type benchmark: str
        """
        self._benchmark = benchmark

    @property
    def user_manual_url(self):
        r"""Gets the user_manual_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 指向评估器用户手册的网址。 **取值范围：** 不涉及。 

        :return: The user_manual_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :rtype: str
        """
        return self._user_manual_url

    @user_manual_url.setter
    def user_manual_url(self, user_manual_url):
        r"""Sets the user_manual_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 指向评估器用户手册的网址。 **取值范围：** 不涉及。 

        :param user_manual_url: The user_manual_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :type user_manual_url: str
        """
        self._user_manual_url = user_manual_url

    @property
    def vendor(self):
        r"""Gets the vendor of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 评估器的提供方标识。 **取值范围：** 不涉及。 

        :return: The vendor of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 评估器的提供方标识。 **取值范围：** 不涉及。 

        :param vendor: The vendor of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def vendor_url(self):
        r"""Gets the vendor_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 供应商的官方网址。 **取值范围：** 不涉及。 

        :return: The vendor_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :rtype: str
        """
        return self._vendor_url

    @vendor_url.setter
    def vendor_url(self, vendor_url):
        r"""Sets the vendor_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.

        **参数解释：** 供应商的官方网址。 **取值范围：** 不涉及。 

        :param vendor_url: The vendor_url of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo.
        :type vendor_url: str
        """
        self._vendor_url = vendor_url

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
