# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReportSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setting_id': 'str'
    }

    attribute_map = {
        'setting_id': 'setting_id'
    }

    def __init__(self, setting_id=None):
        r"""CreateReportSettingResponse

        The model defined in huaweicloud sdk

        :param setting_id: 配置ID
        :type setting_id: str
        """
        
        super().__init__()

        self._setting_id = None
        self.discriminator = None

        if setting_id is not None:
            self.setting_id = setting_id

    @property
    def setting_id(self):
        r"""Gets the setting_id of this CreateReportSettingResponse.

        配置ID

        :return: The setting_id of this CreateReportSettingResponse.
        :rtype: str
        """
        return self._setting_id

    @setting_id.setter
    def setting_id(self, setting_id):
        r"""Sets the setting_id of this CreateReportSettingResponse.

        配置ID

        :param setting_id: The setting_id of this CreateReportSettingResponse.
        :type setting_id: str
        """
        self._setting_id = setting_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateReportSettingResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateReportSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
