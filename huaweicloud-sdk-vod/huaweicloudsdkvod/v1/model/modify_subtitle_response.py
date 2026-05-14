# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifySubtitleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'thumbnail_task_id': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'thumbnail_task_id': 'thumbnail_task_id'
    }

    def __init__(self, asset_id=None, thumbnail_task_id=None):
        r"""ModifySubtitleResponse

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param thumbnail_task_id: 截图任务id，仅支持多截图场景会返回。
        :type thumbnail_task_id: str
        """
        
        super().__init__()

        self._asset_id = None
        self._thumbnail_task_id = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if thumbnail_task_id is not None:
            self.thumbnail_task_id = thumbnail_task_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ModifySubtitleResponse.

        媒资ID。

        :return: The asset_id of this ModifySubtitleResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ModifySubtitleResponse.

        媒资ID。

        :param asset_id: The asset_id of this ModifySubtitleResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def thumbnail_task_id(self):
        r"""Gets the thumbnail_task_id of this ModifySubtitleResponse.

        截图任务id，仅支持多截图场景会返回。

        :return: The thumbnail_task_id of this ModifySubtitleResponse.
        :rtype: str
        """
        return self._thumbnail_task_id

    @thumbnail_task_id.setter
    def thumbnail_task_id(self, thumbnail_task_id):
        r"""Sets the thumbnail_task_id of this ModifySubtitleResponse.

        截图任务id，仅支持多截图场景会返回。

        :param thumbnail_task_id: The thumbnail_task_id of this ModifySubtitleResponse.
        :type thumbnail_task_id: str
        """
        self._thumbnail_task_id = thumbnail_task_id

    def to_dict(self):
        import warnings
        warnings.warn("ModifySubtitleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ModifySubtitleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
