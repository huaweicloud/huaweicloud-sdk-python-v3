# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadUrlItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'upload_url': 'str',
        'obs_bucket': 'str',
        'obs_object_key': 'str'
    }

    attribute_map = {
        'region': 'region',
        'upload_url': 'upload_url',
        'obs_bucket': 'obs_bucket',
        'obs_object_key': 'obs_object_key'
    }

    def __init__(self, region=None, upload_url=None, obs_bucket=None, obs_object_key=None):
        r"""UploadUrlItem

        The model defined in huaweicloud sdk

        :param region: 区域标识。
        :type region: str
        :param upload_url: OBS 预签名上传地址。
        :type upload_url: str
        :param obs_bucket: OBS 桶名。
        :type obs_bucket: str
        :param obs_object_key: OBS 对象键。
        :type obs_object_key: str
        """
        
        

        self._region = None
        self._upload_url = None
        self._obs_bucket = None
        self._obs_object_key = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if upload_url is not None:
            self.upload_url = upload_url
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if obs_object_key is not None:
            self.obs_object_key = obs_object_key

    @property
    def region(self):
        r"""Gets the region of this UploadUrlItem.

        区域标识。

        :return: The region of this UploadUrlItem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this UploadUrlItem.

        区域标识。

        :param region: The region of this UploadUrlItem.
        :type region: str
        """
        self._region = region

    @property
    def upload_url(self):
        r"""Gets the upload_url of this UploadUrlItem.

        OBS 预签名上传地址。

        :return: The upload_url of this UploadUrlItem.
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        r"""Sets the upload_url of this UploadUrlItem.

        OBS 预签名上传地址。

        :param upload_url: The upload_url of this UploadUrlItem.
        :type upload_url: str
        """
        self._upload_url = upload_url

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this UploadUrlItem.

        OBS 桶名。

        :return: The obs_bucket of this UploadUrlItem.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this UploadUrlItem.

        OBS 桶名。

        :param obs_bucket: The obs_bucket of this UploadUrlItem.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def obs_object_key(self):
        r"""Gets the obs_object_key of this UploadUrlItem.

        OBS 对象键。

        :return: The obs_object_key of this UploadUrlItem.
        :rtype: str
        """
        return self._obs_object_key

    @obs_object_key.setter
    def obs_object_key(self, obs_object_key):
        r"""Sets the obs_object_key of this UploadUrlItem.

        OBS 对象键。

        :param obs_object_key: The obs_object_key of this UploadUrlItem.
        :type obs_object_key: str
        """
        self._obs_object_key = obs_object_key

    def to_dict(self):
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
        if not isinstance(other, UploadUrlItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
