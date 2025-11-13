# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsoleConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_support_eps': 'bool',
        'is_support_sm2': 'bool',
        'is_support_dhsm': 'bool',
        'dhsm_regions': 'list[str]',
        'is_support_yearly_monthly_ca': 'bool',
        'is_support_iam5': 'bool',
        'is_support_ocsp': 'bool'
    }

    attribute_map = {
        'is_support_eps': 'is_support_eps',
        'is_support_sm2': 'is_support_sm2',
        'is_support_dhsm': 'is_support_dhsm',
        'dhsm_regions': 'dhsm_regions',
        'is_support_yearly_monthly_ca': 'is_support_yearly_monthly_ca',
        'is_support_iam5': 'is_support_iam5',
        'is_support_ocsp': 'is_support_ocsp'
    }

    def __init__(self, is_support_eps=None, is_support_sm2=None, is_support_dhsm=None, dhsm_regions=None, is_support_yearly_monthly_ca=None, is_support_iam5=None, is_support_ocsp=None):
        r"""ShowConsoleConfigResponse

        The model defined in huaweicloud sdk

        :param is_support_eps: 是否支持企业项目。
        :type is_support_eps: bool
        :param is_support_sm2: 是否支持SM2算法。
        :type is_support_sm2: bool
        :param is_support_dhsm: 是否支持专属加密集群。
        :type is_support_dhsm: bool
        :param dhsm_regions: 专属加密集群支持的region列表。
        :type dhsm_regions: list[str]
        :param is_support_yearly_monthly_ca: 是否支持包年包月CA。
        :type is_support_yearly_monthly_ca: bool
        :param is_support_iam5: 是否支持IAM5鉴权。
        :type is_support_iam5: bool
        :param is_support_ocsp: 是否支持OCSP查询。
        :type is_support_ocsp: bool
        """
        
        super().__init__()

        self._is_support_eps = None
        self._is_support_sm2 = None
        self._is_support_dhsm = None
        self._dhsm_regions = None
        self._is_support_yearly_monthly_ca = None
        self._is_support_iam5 = None
        self._is_support_ocsp = None
        self.discriminator = None

        if is_support_eps is not None:
            self.is_support_eps = is_support_eps
        if is_support_sm2 is not None:
            self.is_support_sm2 = is_support_sm2
        if is_support_dhsm is not None:
            self.is_support_dhsm = is_support_dhsm
        if dhsm_regions is not None:
            self.dhsm_regions = dhsm_regions
        if is_support_yearly_monthly_ca is not None:
            self.is_support_yearly_monthly_ca = is_support_yearly_monthly_ca
        if is_support_iam5 is not None:
            self.is_support_iam5 = is_support_iam5
        if is_support_ocsp is not None:
            self.is_support_ocsp = is_support_ocsp

    @property
    def is_support_eps(self):
        r"""Gets the is_support_eps of this ShowConsoleConfigResponse.

        是否支持企业项目。

        :return: The is_support_eps of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._is_support_eps

    @is_support_eps.setter
    def is_support_eps(self, is_support_eps):
        r"""Sets the is_support_eps of this ShowConsoleConfigResponse.

        是否支持企业项目。

        :param is_support_eps: The is_support_eps of this ShowConsoleConfigResponse.
        :type is_support_eps: bool
        """
        self._is_support_eps = is_support_eps

    @property
    def is_support_sm2(self):
        r"""Gets the is_support_sm2 of this ShowConsoleConfigResponse.

        是否支持SM2算法。

        :return: The is_support_sm2 of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._is_support_sm2

    @is_support_sm2.setter
    def is_support_sm2(self, is_support_sm2):
        r"""Sets the is_support_sm2 of this ShowConsoleConfigResponse.

        是否支持SM2算法。

        :param is_support_sm2: The is_support_sm2 of this ShowConsoleConfigResponse.
        :type is_support_sm2: bool
        """
        self._is_support_sm2 = is_support_sm2

    @property
    def is_support_dhsm(self):
        r"""Gets the is_support_dhsm of this ShowConsoleConfigResponse.

        是否支持专属加密集群。

        :return: The is_support_dhsm of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._is_support_dhsm

    @is_support_dhsm.setter
    def is_support_dhsm(self, is_support_dhsm):
        r"""Sets the is_support_dhsm of this ShowConsoleConfigResponse.

        是否支持专属加密集群。

        :param is_support_dhsm: The is_support_dhsm of this ShowConsoleConfigResponse.
        :type is_support_dhsm: bool
        """
        self._is_support_dhsm = is_support_dhsm

    @property
    def dhsm_regions(self):
        r"""Gets the dhsm_regions of this ShowConsoleConfigResponse.

        专属加密集群支持的region列表。

        :return: The dhsm_regions of this ShowConsoleConfigResponse.
        :rtype: list[str]
        """
        return self._dhsm_regions

    @dhsm_regions.setter
    def dhsm_regions(self, dhsm_regions):
        r"""Sets the dhsm_regions of this ShowConsoleConfigResponse.

        专属加密集群支持的region列表。

        :param dhsm_regions: The dhsm_regions of this ShowConsoleConfigResponse.
        :type dhsm_regions: list[str]
        """
        self._dhsm_regions = dhsm_regions

    @property
    def is_support_yearly_monthly_ca(self):
        r"""Gets the is_support_yearly_monthly_ca of this ShowConsoleConfigResponse.

        是否支持包年包月CA。

        :return: The is_support_yearly_monthly_ca of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._is_support_yearly_monthly_ca

    @is_support_yearly_monthly_ca.setter
    def is_support_yearly_monthly_ca(self, is_support_yearly_monthly_ca):
        r"""Sets the is_support_yearly_monthly_ca of this ShowConsoleConfigResponse.

        是否支持包年包月CA。

        :param is_support_yearly_monthly_ca: The is_support_yearly_monthly_ca of this ShowConsoleConfigResponse.
        :type is_support_yearly_monthly_ca: bool
        """
        self._is_support_yearly_monthly_ca = is_support_yearly_monthly_ca

    @property
    def is_support_iam5(self):
        r"""Gets the is_support_iam5 of this ShowConsoleConfigResponse.

        是否支持IAM5鉴权。

        :return: The is_support_iam5 of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._is_support_iam5

    @is_support_iam5.setter
    def is_support_iam5(self, is_support_iam5):
        r"""Sets the is_support_iam5 of this ShowConsoleConfigResponse.

        是否支持IAM5鉴权。

        :param is_support_iam5: The is_support_iam5 of this ShowConsoleConfigResponse.
        :type is_support_iam5: bool
        """
        self._is_support_iam5 = is_support_iam5

    @property
    def is_support_ocsp(self):
        r"""Gets the is_support_ocsp of this ShowConsoleConfigResponse.

        是否支持OCSP查询。

        :return: The is_support_ocsp of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._is_support_ocsp

    @is_support_ocsp.setter
    def is_support_ocsp(self, is_support_ocsp):
        r"""Sets the is_support_ocsp of this ShowConsoleConfigResponse.

        是否支持OCSP查询。

        :param is_support_ocsp: The is_support_ocsp of this ShowConsoleConfigResponse.
        :type is_support_ocsp: bool
        """
        self._is_support_ocsp = is_support_ocsp

    def to_dict(self):
        import warnings
        warnings.warn("ShowConsoleConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowConsoleConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
