# coding: utf-8

import six

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
        'cer_available': 'bool'
    }

    attribute_map = {
        'enable_user_def_obs': 'enableUserDefObs',
        'enable_enterprise': 'enableEnterprise',
        'cer_available': 'cerAvailable'
    }

    def __init__(self, enable_user_def_obs=None, enable_enterprise=None, cer_available=None):
        r"""ListGlobalFeatureGatesResponse

        The model defined in huaweicloud sdk

        :param enable_user_def_obs: 是否支持使用用户的obs桶
        :type enable_user_def_obs: bool
        :param enable_enterprise: 是否支持支持企业项目
        :type enable_enterprise: bool
        :param cer_available: 是否支持SWR企业版功能
        :type cer_available: bool
        """
        
        super(ListGlobalFeatureGatesResponse, self).__init__()

        self._enable_user_def_obs = None
        self._enable_enterprise = None
        self._cer_available = None
        self.discriminator = None

        if enable_user_def_obs is not None:
            self.enable_user_def_obs = enable_user_def_obs
        if enable_enterprise is not None:
            self.enable_enterprise = enable_enterprise
        if cer_available is not None:
            self.cer_available = cer_available

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
        if not isinstance(other, ListGlobalFeatureGatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
