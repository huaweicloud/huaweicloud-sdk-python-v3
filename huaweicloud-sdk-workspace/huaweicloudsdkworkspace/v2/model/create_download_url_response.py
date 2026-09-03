# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDownloadUrlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'download_url': 'str',
        'obs_bucket': 'str',
        'obs_object_key': 'str',
        'expires_at': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'download_url': 'download_url',
        'obs_bucket': 'obs_bucket',
        'obs_object_key': 'obs_object_key',
        'expires_at': 'expires_at',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, download_url=None, obs_bucket=None, obs_object_key=None, expires_at=None, x_request_id=None):
        r"""CreateDownloadUrlResponse

        The model defined in huaweicloud sdk

        :param download_url: OBS 预签名下载地址。
        :type download_url: str
        :param obs_bucket: OBS 桶名。
        :type obs_bucket: str
        :param obs_object_key: OBS 对象键。
        :type obs_object_key: str
        :param expires_at: 下载地址过期时间（ISO8601格式，UTC时区）。
        :type expires_at: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._download_url = None
        self._obs_bucket = None
        self._obs_object_key = None
        self._expires_at = None
        self._x_request_id = None
        self.discriminator = None

        if download_url is not None:
            self.download_url = download_url
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if obs_object_key is not None:
            self.obs_object_key = obs_object_key
        if expires_at is not None:
            self.expires_at = expires_at
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def download_url(self):
        r"""Gets the download_url of this CreateDownloadUrlResponse.

        OBS 预签名下载地址。

        :return: The download_url of this CreateDownloadUrlResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this CreateDownloadUrlResponse.

        OBS 预签名下载地址。

        :param download_url: The download_url of this CreateDownloadUrlResponse.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this CreateDownloadUrlResponse.

        OBS 桶名。

        :return: The obs_bucket of this CreateDownloadUrlResponse.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this CreateDownloadUrlResponse.

        OBS 桶名。

        :param obs_bucket: The obs_bucket of this CreateDownloadUrlResponse.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def obs_object_key(self):
        r"""Gets the obs_object_key of this CreateDownloadUrlResponse.

        OBS 对象键。

        :return: The obs_object_key of this CreateDownloadUrlResponse.
        :rtype: str
        """
        return self._obs_object_key

    @obs_object_key.setter
    def obs_object_key(self, obs_object_key):
        r"""Sets the obs_object_key of this CreateDownloadUrlResponse.

        OBS 对象键。

        :param obs_object_key: The obs_object_key of this CreateDownloadUrlResponse.
        :type obs_object_key: str
        """
        self._obs_object_key = obs_object_key

    @property
    def expires_at(self):
        r"""Gets the expires_at of this CreateDownloadUrlResponse.

        下载地址过期时间（ISO8601格式，UTC时区）。

        :return: The expires_at of this CreateDownloadUrlResponse.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this CreateDownloadUrlResponse.

        下载地址过期时间（ISO8601格式，UTC时区）。

        :param expires_at: The expires_at of this CreateDownloadUrlResponse.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateDownloadUrlResponse.

        :return: The x_request_id of this CreateDownloadUrlResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateDownloadUrlResponse.

        :param x_request_id: The x_request_id of this CreateDownloadUrlResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateDownloadUrlResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateDownloadUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
