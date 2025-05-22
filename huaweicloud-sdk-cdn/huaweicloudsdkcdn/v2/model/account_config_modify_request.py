# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountConfigModifyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_agency_status': 'str',
        'scm_agency_status': 'str'
    }

    attribute_map = {
        'obs_agency_status': 'obs_agency_status',
        'scm_agency_status': 'scm_agency_status'
    }

    def __init__(self, obs_agency_status=None, scm_agency_status=None):
        r"""AccountConfigModifyRequest

        The model defined in huaweicloud sdk

        :param obs_agency_status: OBS委托授权，使用OBS私有桶作为源站时需要开启该委托授权。当前仅支持传on：开启OBS委托授权。
        :type obs_agency_status: str
        :param scm_agency_status: SCM委托授权，配置HTTPS证书时，证书来源选择SCM证书时需要开启该委托授权。当前仅支持传on：开启SCM委托授权。
        :type scm_agency_status: str
        """
        
        

        self._obs_agency_status = None
        self._scm_agency_status = None
        self.discriminator = None

        if obs_agency_status is not None:
            self.obs_agency_status = obs_agency_status
        if scm_agency_status is not None:
            self.scm_agency_status = scm_agency_status

    @property
    def obs_agency_status(self):
        r"""Gets the obs_agency_status of this AccountConfigModifyRequest.

        OBS委托授权，使用OBS私有桶作为源站时需要开启该委托授权。当前仅支持传on：开启OBS委托授权。

        :return: The obs_agency_status of this AccountConfigModifyRequest.
        :rtype: str
        """
        return self._obs_agency_status

    @obs_agency_status.setter
    def obs_agency_status(self, obs_agency_status):
        r"""Sets the obs_agency_status of this AccountConfigModifyRequest.

        OBS委托授权，使用OBS私有桶作为源站时需要开启该委托授权。当前仅支持传on：开启OBS委托授权。

        :param obs_agency_status: The obs_agency_status of this AccountConfigModifyRequest.
        :type obs_agency_status: str
        """
        self._obs_agency_status = obs_agency_status

    @property
    def scm_agency_status(self):
        r"""Gets the scm_agency_status of this AccountConfigModifyRequest.

        SCM委托授权，配置HTTPS证书时，证书来源选择SCM证书时需要开启该委托授权。当前仅支持传on：开启SCM委托授权。

        :return: The scm_agency_status of this AccountConfigModifyRequest.
        :rtype: str
        """
        return self._scm_agency_status

    @scm_agency_status.setter
    def scm_agency_status(self, scm_agency_status):
        r"""Sets the scm_agency_status of this AccountConfigModifyRequest.

        SCM委托授权，配置HTTPS证书时，证书来源选择SCM证书时需要开启该委托授权。当前仅支持传on：开启SCM委托授权。

        :param scm_agency_status: The scm_agency_status of this AccountConfigModifyRequest.
        :type scm_agency_status: str
        """
        self._scm_agency_status = scm_agency_status

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
        if not isinstance(other, AccountConfigModifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
