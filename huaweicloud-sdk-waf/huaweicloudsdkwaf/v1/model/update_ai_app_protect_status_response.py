# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAiAppProtectStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'protect_status': 'int'
    }

    attribute_map = {
        'app_id': 'appId',
        'protect_status': 'protect_status'
    }

    def __init__(self, app_id=None, protect_status=None):
        r"""UpdateAiAppProtectStatusResponse

        The model defined in huaweicloud sdk

        :param app_id: AI应用ID
        :type app_id: str
        :param protect_status: 防护状态（0：禁用，1：启用）
        :type protect_status: int
        """
        
        super().__init__()

        self._app_id = None
        self._protect_status = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def app_id(self):
        r"""Gets the app_id of this UpdateAiAppProtectStatusResponse.

        AI应用ID

        :return: The app_id of this UpdateAiAppProtectStatusResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this UpdateAiAppProtectStatusResponse.

        AI应用ID

        :param app_id: The app_id of this UpdateAiAppProtectStatusResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def protect_status(self):
        r"""Gets the protect_status of this UpdateAiAppProtectStatusResponse.

        防护状态（0：禁用，1：启用）

        :return: The protect_status of this UpdateAiAppProtectStatusResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this UpdateAiAppProtectStatusResponse.

        防护状态（0：禁用，1：启用）

        :param protect_status: The protect_status of this UpdateAiAppProtectStatusResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAiAppProtectStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateAiAppProtectStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
