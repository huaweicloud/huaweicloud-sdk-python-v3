# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowObsUrlOfTrainingJobLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_url': 'str',
        'shards': 'Shards'
    }

    attribute_map = {
        'obs_url': 'obs_url',
        'shards': 'shards'
    }

    def __init__(self, obs_url=None, shards=None):
        r"""ShowObsUrlOfTrainingJobLogsResponse

        The model defined in huaweicloud sdk

        :param obs_url: 日志OBS临时链接（复制到浏览器可查看当前全量日志）。
        :type obs_url: str
        :param shards: 
        :type shards: :class:`huaweicloudsdkmodelarts.v1.Shards`
        """
        
        super().__init__()

        self._obs_url = None
        self._shards = None
        self.discriminator = None

        if obs_url is not None:
            self.obs_url = obs_url
        if shards is not None:
            self.shards = shards

    @property
    def obs_url(self):
        r"""Gets the obs_url of this ShowObsUrlOfTrainingJobLogsResponse.

        日志OBS临时链接（复制到浏览器可查看当前全量日志）。

        :return: The obs_url of this ShowObsUrlOfTrainingJobLogsResponse.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        r"""Sets the obs_url of this ShowObsUrlOfTrainingJobLogsResponse.

        日志OBS临时链接（复制到浏览器可查看当前全量日志）。

        :param obs_url: The obs_url of this ShowObsUrlOfTrainingJobLogsResponse.
        :type obs_url: str
        """
        self._obs_url = obs_url

    @property
    def shards(self):
        r"""Gets the shards of this ShowObsUrlOfTrainingJobLogsResponse.

        :return: The shards of this ShowObsUrlOfTrainingJobLogsResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Shards`
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this ShowObsUrlOfTrainingJobLogsResponse.

        :param shards: The shards of this ShowObsUrlOfTrainingJobLogsResponse.
        :type shards: :class:`huaweicloudsdkmodelarts.v1.Shards`
        """
        self._shards = shards

    def to_dict(self):
        import warnings
        warnings.warn("ShowObsUrlOfTrainingJobLogsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowObsUrlOfTrainingJobLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
