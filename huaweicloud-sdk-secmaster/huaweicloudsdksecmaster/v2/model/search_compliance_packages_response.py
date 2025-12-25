# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCompliancePackagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'builtin_compliance_num': 'int',
        'customized_compliance_num': 'int',
        'disabled_compliance_num': 'int',
        'enabled_compliance_num': 'int',
        'compliance_packages': 'list[CompliancePackageModel]'
    }

    attribute_map = {
        'count': 'count',
        'builtin_compliance_num': 'builtin_compliance_num',
        'customized_compliance_num': 'customized_compliance_num',
        'disabled_compliance_num': 'disabled_compliance_num',
        'enabled_compliance_num': 'enabled_compliance_num',
        'compliance_packages': 'compliance_packages'
    }

    def __init__(self, count=None, builtin_compliance_num=None, customized_compliance_num=None, disabled_compliance_num=None, enabled_compliance_num=None, compliance_packages=None):
        r"""SearchCompliancePackagesResponse

        The model defined in huaweicloud sdk

        :param count: 遵从包总数
        :type count: int
        :param builtin_compliance_num: 内置遵从包数量
        :type builtin_compliance_num: int
        :param customized_compliance_num: 自定义遵从包数量
        :type customized_compliance_num: int
        :param disabled_compliance_num: 停用遵从包数量
        :type disabled_compliance_num: int
        :param enabled_compliance_num: 启用遵从包数量
        :type enabled_compliance_num: int
        :param compliance_packages: 遵从包列表
        :type compliance_packages: list[:class:`huaweicloudsdksecmaster.v2.CompliancePackageModel`]
        """
        
        super().__init__()

        self._count = None
        self._builtin_compliance_num = None
        self._customized_compliance_num = None
        self._disabled_compliance_num = None
        self._enabled_compliance_num = None
        self._compliance_packages = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if builtin_compliance_num is not None:
            self.builtin_compliance_num = builtin_compliance_num
        if customized_compliance_num is not None:
            self.customized_compliance_num = customized_compliance_num
        if disabled_compliance_num is not None:
            self.disabled_compliance_num = disabled_compliance_num
        if enabled_compliance_num is not None:
            self.enabled_compliance_num = enabled_compliance_num
        if compliance_packages is not None:
            self.compliance_packages = compliance_packages

    @property
    def count(self):
        r"""Gets the count of this SearchCompliancePackagesResponse.

        遵从包总数

        :return: The count of this SearchCompliancePackagesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SearchCompliancePackagesResponse.

        遵从包总数

        :param count: The count of this SearchCompliancePackagesResponse.
        :type count: int
        """
        self._count = count

    @property
    def builtin_compliance_num(self):
        r"""Gets the builtin_compliance_num of this SearchCompliancePackagesResponse.

        内置遵从包数量

        :return: The builtin_compliance_num of this SearchCompliancePackagesResponse.
        :rtype: int
        """
        return self._builtin_compliance_num

    @builtin_compliance_num.setter
    def builtin_compliance_num(self, builtin_compliance_num):
        r"""Sets the builtin_compliance_num of this SearchCompliancePackagesResponse.

        内置遵从包数量

        :param builtin_compliance_num: The builtin_compliance_num of this SearchCompliancePackagesResponse.
        :type builtin_compliance_num: int
        """
        self._builtin_compliance_num = builtin_compliance_num

    @property
    def customized_compliance_num(self):
        r"""Gets the customized_compliance_num of this SearchCompliancePackagesResponse.

        自定义遵从包数量

        :return: The customized_compliance_num of this SearchCompliancePackagesResponse.
        :rtype: int
        """
        return self._customized_compliance_num

    @customized_compliance_num.setter
    def customized_compliance_num(self, customized_compliance_num):
        r"""Sets the customized_compliance_num of this SearchCompliancePackagesResponse.

        自定义遵从包数量

        :param customized_compliance_num: The customized_compliance_num of this SearchCompliancePackagesResponse.
        :type customized_compliance_num: int
        """
        self._customized_compliance_num = customized_compliance_num

    @property
    def disabled_compliance_num(self):
        r"""Gets the disabled_compliance_num of this SearchCompliancePackagesResponse.

        停用遵从包数量

        :return: The disabled_compliance_num of this SearchCompliancePackagesResponse.
        :rtype: int
        """
        return self._disabled_compliance_num

    @disabled_compliance_num.setter
    def disabled_compliance_num(self, disabled_compliance_num):
        r"""Sets the disabled_compliance_num of this SearchCompliancePackagesResponse.

        停用遵从包数量

        :param disabled_compliance_num: The disabled_compliance_num of this SearchCompliancePackagesResponse.
        :type disabled_compliance_num: int
        """
        self._disabled_compliance_num = disabled_compliance_num

    @property
    def enabled_compliance_num(self):
        r"""Gets the enabled_compliance_num of this SearchCompliancePackagesResponse.

        启用遵从包数量

        :return: The enabled_compliance_num of this SearchCompliancePackagesResponse.
        :rtype: int
        """
        return self._enabled_compliance_num

    @enabled_compliance_num.setter
    def enabled_compliance_num(self, enabled_compliance_num):
        r"""Sets the enabled_compliance_num of this SearchCompliancePackagesResponse.

        启用遵从包数量

        :param enabled_compliance_num: The enabled_compliance_num of this SearchCompliancePackagesResponse.
        :type enabled_compliance_num: int
        """
        self._enabled_compliance_num = enabled_compliance_num

    @property
    def compliance_packages(self):
        r"""Gets the compliance_packages of this SearchCompliancePackagesResponse.

        遵从包列表

        :return: The compliance_packages of this SearchCompliancePackagesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CompliancePackageModel`]
        """
        return self._compliance_packages

    @compliance_packages.setter
    def compliance_packages(self, compliance_packages):
        r"""Sets the compliance_packages of this SearchCompliancePackagesResponse.

        遵从包列表

        :param compliance_packages: The compliance_packages of this SearchCompliancePackagesResponse.
        :type compliance_packages: list[:class:`huaweicloudsdksecmaster.v2.CompliancePackageModel`]
        """
        self._compliance_packages = compliance_packages

    def to_dict(self):
        import warnings
        warnings.warn("SearchCompliancePackagesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, SearchCompliancePackagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
