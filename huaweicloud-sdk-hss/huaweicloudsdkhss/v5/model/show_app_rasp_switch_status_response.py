# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppRaspSwitchStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):
        r"""ShowAppRaspSwitchStatusResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**: 应用防护状态 **约束限制**: 不涉及 **取值范围**: 包含如下7种。 - app_install_processing：防护开启中。 - app_protected：防护成功。 - app_install_failed：防护失败（安装失败）。 - app_not_configure：未防护。 - app_partially_protected：部分防护。 - app_all_failed：防护失败。 - app_uninstall_processing：卸载中。 **默认取值**: 不涉及 
        :type status: str
        """
        
        super().__init__()

        self._status = None
        self.discriminator = None

        if status is not None:
            self.status = status

    @property
    def status(self):
        r"""Gets the status of this ShowAppRaspSwitchStatusResponse.

        **参数解释**: 应用防护状态 **约束限制**: 不涉及 **取值范围**: 包含如下7种。 - app_install_processing：防护开启中。 - app_protected：防护成功。 - app_install_failed：防护失败（安装失败）。 - app_not_configure：未防护。 - app_partially_protected：部分防护。 - app_all_failed：防护失败。 - app_uninstall_processing：卸载中。 **默认取值**: 不涉及 

        :return: The status of this ShowAppRaspSwitchStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAppRaspSwitchStatusResponse.

        **参数解释**: 应用防护状态 **约束限制**: 不涉及 **取值范围**: 包含如下7种。 - app_install_processing：防护开启中。 - app_protected：防护成功。 - app_install_failed：防护失败（安装失败）。 - app_not_configure：未防护。 - app_partially_protected：部分防护。 - app_all_failed：防护失败。 - app_uninstall_processing：卸载中。 **默认取值**: 不涉及 

        :param status: The status of this ShowAppRaspSwitchStatusResponse.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("ShowAppRaspSwitchStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAppRaspSwitchStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
