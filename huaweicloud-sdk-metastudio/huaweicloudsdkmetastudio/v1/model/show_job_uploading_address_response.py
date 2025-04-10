# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobUploadingAddressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'segment_url': 'ShowJobUploadingAddressRspSegmentUrl',
        'package_url': 'ShowJobUploadingAddressRspPackageUrl',
        'authorization_letter_uploading_url': 'str'
    }

    attribute_map = {
        'segment_url': 'segment_url',
        'package_url': 'package_url',
        'authorization_letter_uploading_url': 'authorization_letter_uploading_url'
    }

    def __init__(self, segment_url=None, package_url=None, authorization_letter_uploading_url=None):
        r"""ShowJobUploadingAddressResponse

        The model defined in huaweicloud sdk

        :param segment_url: 
        :type segment_url: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRspSegmentUrl`
        :param package_url: 
        :type package_url: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRspPackageUrl`
        :param authorization_letter_uploading_url: 授权书的上传地址。
        :type authorization_letter_uploading_url: str
        """
        
        super(ShowJobUploadingAddressResponse, self).__init__()

        self._segment_url = None
        self._package_url = None
        self._authorization_letter_uploading_url = None
        self.discriminator = None

        if segment_url is not None:
            self.segment_url = segment_url
        if package_url is not None:
            self.package_url = package_url
        if authorization_letter_uploading_url is not None:
            self.authorization_letter_uploading_url = authorization_letter_uploading_url

    @property
    def segment_url(self):
        r"""Gets the segment_url of this ShowJobUploadingAddressResponse.

        :return: The segment_url of this ShowJobUploadingAddressResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRspSegmentUrl`
        """
        return self._segment_url

    @segment_url.setter
    def segment_url(self, segment_url):
        r"""Sets the segment_url of this ShowJobUploadingAddressResponse.

        :param segment_url: The segment_url of this ShowJobUploadingAddressResponse.
        :type segment_url: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRspSegmentUrl`
        """
        self._segment_url = segment_url

    @property
    def package_url(self):
        r"""Gets the package_url of this ShowJobUploadingAddressResponse.

        :return: The package_url of this ShowJobUploadingAddressResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRspPackageUrl`
        """
        return self._package_url

    @package_url.setter
    def package_url(self, package_url):
        r"""Sets the package_url of this ShowJobUploadingAddressResponse.

        :param package_url: The package_url of this ShowJobUploadingAddressResponse.
        :type package_url: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRspPackageUrl`
        """
        self._package_url = package_url

    @property
    def authorization_letter_uploading_url(self):
        r"""Gets the authorization_letter_uploading_url of this ShowJobUploadingAddressResponse.

        授权书的上传地址。

        :return: The authorization_letter_uploading_url of this ShowJobUploadingAddressResponse.
        :rtype: str
        """
        return self._authorization_letter_uploading_url

    @authorization_letter_uploading_url.setter
    def authorization_letter_uploading_url(self, authorization_letter_uploading_url):
        r"""Sets the authorization_letter_uploading_url of this ShowJobUploadingAddressResponse.

        授权书的上传地址。

        :param authorization_letter_uploading_url: The authorization_letter_uploading_url of this ShowJobUploadingAddressResponse.
        :type authorization_letter_uploading_url: str
        """
        self._authorization_letter_uploading_url = authorization_letter_uploading_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowJobUploadingAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
