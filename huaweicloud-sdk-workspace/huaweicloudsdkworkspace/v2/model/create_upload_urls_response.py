# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUploadUrlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upload_urls': 'list[UploadUrlItem]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'upload_urls': 'upload_urls',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, upload_urls=None, x_request_id=None):
        r"""CreateUploadUrlsResponse

        The model defined in huaweicloud sdk

        :param upload_urls: 上传地址列表。
        :type upload_urls: list[:class:`huaweicloudsdkworkspace.v2.UploadUrlItem`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._upload_urls = None
        self._x_request_id = None
        self.discriminator = None

        if upload_urls is not None:
            self.upload_urls = upload_urls
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def upload_urls(self):
        r"""Gets the upload_urls of this CreateUploadUrlsResponse.

        上传地址列表。

        :return: The upload_urls of this CreateUploadUrlsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.UploadUrlItem`]
        """
        return self._upload_urls

    @upload_urls.setter
    def upload_urls(self, upload_urls):
        r"""Sets the upload_urls of this CreateUploadUrlsResponse.

        上传地址列表。

        :param upload_urls: The upload_urls of this CreateUploadUrlsResponse.
        :type upload_urls: list[:class:`huaweicloudsdkworkspace.v2.UploadUrlItem`]
        """
        self._upload_urls = upload_urls

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateUploadUrlsResponse.

        :return: The x_request_id of this CreateUploadUrlsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateUploadUrlsResponse.

        :param x_request_id: The x_request_id of this CreateUploadUrlsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateUploadUrlsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateUploadUrlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
