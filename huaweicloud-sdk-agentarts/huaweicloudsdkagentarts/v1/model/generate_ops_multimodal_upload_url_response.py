# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateOpsMultimodalUploadUrlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upload_url': 'str',
        'obs_path': 'str'
    }

    attribute_map = {
        'upload_url': 'upload_url',
        'obs_path': 'obs_path'
    }

    def __init__(self, upload_url=None, obs_path=None):
        r"""GenerateOpsMultimodalUploadUrlResponse

        The model defined in huaweicloud sdk

        :param upload_url: **参数解释：** OBS预签名上传链接，用户使用该链接上传多模态文件。 **约束限制：** 有效期为15分钟。 **取值范围：** HTTPS URL字符串。 **默认取值：** 不涉及。
        :type upload_url: str
        :param obs_path: **参数解释：** OBS对象路径，评估时传入此路径。 **约束限制：** 格式为{uuid}.{suffix}。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type obs_path: str
        """
        
        super().__init__()

        self._upload_url = None
        self._obs_path = None
        self.discriminator = None

        if upload_url is not None:
            self.upload_url = upload_url
        if obs_path is not None:
            self.obs_path = obs_path

    @property
    def upload_url(self):
        r"""Gets the upload_url of this GenerateOpsMultimodalUploadUrlResponse.

        **参数解释：** OBS预签名上传链接，用户使用该链接上传多模态文件。 **约束限制：** 有效期为15分钟。 **取值范围：** HTTPS URL字符串。 **默认取值：** 不涉及。

        :return: The upload_url of this GenerateOpsMultimodalUploadUrlResponse.
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        r"""Sets the upload_url of this GenerateOpsMultimodalUploadUrlResponse.

        **参数解释：** OBS预签名上传链接，用户使用该链接上传多模态文件。 **约束限制：** 有效期为15分钟。 **取值范围：** HTTPS URL字符串。 **默认取值：** 不涉及。

        :param upload_url: The upload_url of this GenerateOpsMultimodalUploadUrlResponse.
        :type upload_url: str
        """
        self._upload_url = upload_url

    @property
    def obs_path(self):
        r"""Gets the obs_path of this GenerateOpsMultimodalUploadUrlResponse.

        **参数解释：** OBS对象路径，评估时传入此路径。 **约束限制：** 格式为{uuid}.{suffix}。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The obs_path of this GenerateOpsMultimodalUploadUrlResponse.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        r"""Sets the obs_path of this GenerateOpsMultimodalUploadUrlResponse.

        **参数解释：** OBS对象路径，评估时传入此路径。 **约束限制：** 格式为{uuid}.{suffix}。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param obs_path: The obs_path of this GenerateOpsMultimodalUploadUrlResponse.
        :type obs_path: str
        """
        self._obs_path = obs_path

    def to_dict(self):
        import warnings
        warnings.warn("GenerateOpsMultimodalUploadUrlResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GenerateOpsMultimodalUploadUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
