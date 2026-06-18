# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantDevelopModeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cr_enable': 'bool',
        'repo_encryption_enabled': 'bool'
    }

    attribute_map = {
        'cr_enable': 'cr_enable',
        'repo_encryption_enabled': 'repo_encryption_enabled'
    }

    def __init__(self, cr_enable=None, repo_encryption_enabled=None):
        r"""ShowTenantDevelopModeResponse

        The model defined in huaweicloud sdk

        :param cr_enable: **参数解释：** 是否开启cr模式。
        :type cr_enable: bool
        :param repo_encryption_enabled: **参数解释：** 是否开启租户下加密设置。
        :type repo_encryption_enabled: bool
        """
        
        super().__init__()

        self._cr_enable = None
        self._repo_encryption_enabled = None
        self.discriminator = None

        if cr_enable is not None:
            self.cr_enable = cr_enable
        if repo_encryption_enabled is not None:
            self.repo_encryption_enabled = repo_encryption_enabled

    @property
    def cr_enable(self):
        r"""Gets the cr_enable of this ShowTenantDevelopModeResponse.

        **参数解释：** 是否开启cr模式。

        :return: The cr_enable of this ShowTenantDevelopModeResponse.
        :rtype: bool
        """
        return self._cr_enable

    @cr_enable.setter
    def cr_enable(self, cr_enable):
        r"""Sets the cr_enable of this ShowTenantDevelopModeResponse.

        **参数解释：** 是否开启cr模式。

        :param cr_enable: The cr_enable of this ShowTenantDevelopModeResponse.
        :type cr_enable: bool
        """
        self._cr_enable = cr_enable

    @property
    def repo_encryption_enabled(self):
        r"""Gets the repo_encryption_enabled of this ShowTenantDevelopModeResponse.

        **参数解释：** 是否开启租户下加密设置。

        :return: The repo_encryption_enabled of this ShowTenantDevelopModeResponse.
        :rtype: bool
        """
        return self._repo_encryption_enabled

    @repo_encryption_enabled.setter
    def repo_encryption_enabled(self, repo_encryption_enabled):
        r"""Sets the repo_encryption_enabled of this ShowTenantDevelopModeResponse.

        **参数解释：** 是否开启租户下加密设置。

        :param repo_encryption_enabled: The repo_encryption_enabled of this ShowTenantDevelopModeResponse.
        :type repo_encryption_enabled: bool
        """
        self._repo_encryption_enabled = repo_encryption_enabled

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantDevelopModeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTenantDevelopModeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
