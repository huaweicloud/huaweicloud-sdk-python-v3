# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalFeatureGatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_user_def_obs': 'bool',
        'enable_enterprise': 'bool',
        'cer_available': 'bool',
        'enable_intranet_access_switch': 'bool',
        'enable_console_agency': 'bool',
        'enable_v5_custom_agency': 'bool',
        'agency_name': 'str'
    }

    attribute_map = {
        'enable_user_def_obs': 'enableUserDefObs',
        'enable_enterprise': 'enableEnterprise',
        'cer_available': 'cerAvailable',
        'enable_intranet_access_switch': 'enableIntranetAccessSwitch',
        'enable_console_agency': 'enableConsoleAgency',
        'enable_v5_custom_agency': 'enableV5CustomAgency',
        'agency_name': 'agencyName'
    }

    def __init__(self, enable_user_def_obs=None, enable_enterprise=None, cer_available=None, enable_intranet_access_switch=None, enable_console_agency=None, enable_v5_custom_agency=None, agency_name=None):
        r"""ListGlobalFeatureGatesResponse

        The model defined in huaweicloud sdk

        :param enable_user_def_obs: 是否支持使用用户的obs桶
        :type enable_user_def_obs: bool
        :param enable_enterprise: 是否支持支持企业项目
        :type enable_enterprise: bool
        :param cer_available: 是否支持SWR企业版功能
        :type cer_available: bool
        :param enable_intranet_access_switch: 是否展示创建内网访问的开关按钮
        :type enable_intranet_access_switch: bool
        :param enable_console_agency: 是否支持Console侧的一键委托
        :type enable_console_agency: bool
        :param enable_v5_custom_agency: 是否支持IAM新平面的信任委托
        :type enable_v5_custom_agency: bool
        :param agency_name: 委托名称
        :type agency_name: str
        """
        
        super().__init__()

        self._enable_user_def_obs = None
        self._enable_enterprise = None
        self._cer_available = None
        self._enable_intranet_access_switch = None
        self._enable_console_agency = None
        self._enable_v5_custom_agency = None
        self._agency_name = None
        self.discriminator = None

        if enable_user_def_obs is not None:
            self.enable_user_def_obs = enable_user_def_obs
        if enable_enterprise is not None:
            self.enable_enterprise = enable_enterprise
        if cer_available is not None:
            self.cer_available = cer_available
        if enable_intranet_access_switch is not None:
            self.enable_intranet_access_switch = enable_intranet_access_switch
        if enable_console_agency is not None:
            self.enable_console_agency = enable_console_agency
        if enable_v5_custom_agency is not None:
            self.enable_v5_custom_agency = enable_v5_custom_agency
        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def enable_user_def_obs(self):
        r"""Gets the enable_user_def_obs of this ListGlobalFeatureGatesResponse.

        是否支持使用用户的obs桶

        :return: The enable_user_def_obs of this ListGlobalFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_user_def_obs

    @enable_user_def_obs.setter
    def enable_user_def_obs(self, enable_user_def_obs):
        r"""Sets the enable_user_def_obs of this ListGlobalFeatureGatesResponse.

        是否支持使用用户的obs桶

        :param enable_user_def_obs: The enable_user_def_obs of this ListGlobalFeatureGatesResponse.
        :type enable_user_def_obs: bool
        """
        self._enable_user_def_obs = enable_user_def_obs

    @property
    def enable_enterprise(self):
        r"""Gets the enable_enterprise of this ListGlobalFeatureGatesResponse.

        是否支持支持企业项目

        :return: The enable_enterprise of this ListGlobalFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_enterprise

    @enable_enterprise.setter
    def enable_enterprise(self, enable_enterprise):
        r"""Sets the enable_enterprise of this ListGlobalFeatureGatesResponse.

        是否支持支持企业项目

        :param enable_enterprise: The enable_enterprise of this ListGlobalFeatureGatesResponse.
        :type enable_enterprise: bool
        """
        self._enable_enterprise = enable_enterprise

    @property
    def cer_available(self):
        r"""Gets the cer_available of this ListGlobalFeatureGatesResponse.

        是否支持SWR企业版功能

        :return: The cer_available of this ListGlobalFeatureGatesResponse.
        :rtype: bool
        """
        return self._cer_available

    @cer_available.setter
    def cer_available(self, cer_available):
        r"""Sets the cer_available of this ListGlobalFeatureGatesResponse.

        是否支持SWR企业版功能

        :param cer_available: The cer_available of this ListGlobalFeatureGatesResponse.
        :type cer_available: bool
        """
        self._cer_available = cer_available

    @property
    def enable_intranet_access_switch(self):
        r"""Gets the enable_intranet_access_switch of this ListGlobalFeatureGatesResponse.

        是否展示创建内网访问的开关按钮

        :return: The enable_intranet_access_switch of this ListGlobalFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_intranet_access_switch

    @enable_intranet_access_switch.setter
    def enable_intranet_access_switch(self, enable_intranet_access_switch):
        r"""Sets the enable_intranet_access_switch of this ListGlobalFeatureGatesResponse.

        是否展示创建内网访问的开关按钮

        :param enable_intranet_access_switch: The enable_intranet_access_switch of this ListGlobalFeatureGatesResponse.
        :type enable_intranet_access_switch: bool
        """
        self._enable_intranet_access_switch = enable_intranet_access_switch

    @property
    def enable_console_agency(self):
        r"""Gets the enable_console_agency of this ListGlobalFeatureGatesResponse.

        是否支持Console侧的一键委托

        :return: The enable_console_agency of this ListGlobalFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_console_agency

    @enable_console_agency.setter
    def enable_console_agency(self, enable_console_agency):
        r"""Sets the enable_console_agency of this ListGlobalFeatureGatesResponse.

        是否支持Console侧的一键委托

        :param enable_console_agency: The enable_console_agency of this ListGlobalFeatureGatesResponse.
        :type enable_console_agency: bool
        """
        self._enable_console_agency = enable_console_agency

    @property
    def enable_v5_custom_agency(self):
        r"""Gets the enable_v5_custom_agency of this ListGlobalFeatureGatesResponse.

        是否支持IAM新平面的信任委托

        :return: The enable_v5_custom_agency of this ListGlobalFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_v5_custom_agency

    @enable_v5_custom_agency.setter
    def enable_v5_custom_agency(self, enable_v5_custom_agency):
        r"""Sets the enable_v5_custom_agency of this ListGlobalFeatureGatesResponse.

        是否支持IAM新平面的信任委托

        :param enable_v5_custom_agency: The enable_v5_custom_agency of this ListGlobalFeatureGatesResponse.
        :type enable_v5_custom_agency: bool
        """
        self._enable_v5_custom_agency = enable_v5_custom_agency

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ListGlobalFeatureGatesResponse.

        委托名称

        :return: The agency_name of this ListGlobalFeatureGatesResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ListGlobalFeatureGatesResponse.

        委托名称

        :param agency_name: The agency_name of this ListGlobalFeatureGatesResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    def to_dict(self):
        import warnings
        warnings.warn("ListGlobalFeatureGatesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListGlobalFeatureGatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
