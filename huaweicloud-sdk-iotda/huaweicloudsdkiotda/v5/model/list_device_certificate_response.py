# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeviceCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_certificates': 'list[DeviceCertificateSimple]',
        'page': 'Page'
    }

    attribute_map = {
        'device_certificates': 'device_certificates',
        'page': 'page'
    }

    def __init__(self, device_certificates=None, page=None):
        r"""ListDeviceCertificateResponse

        The model defined in huaweicloud sdk

        :param device_certificates: 设备证书列表
        :type device_certificates: list[:class:`huaweicloudsdkiotda.v5.DeviceCertificateSimple`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListDeviceCertificateResponse, self).__init__()

        self._device_certificates = None
        self._page = None
        self.discriminator = None

        if device_certificates is not None:
            self.device_certificates = device_certificates
        if page is not None:
            self.page = page

    @property
    def device_certificates(self):
        r"""Gets the device_certificates of this ListDeviceCertificateResponse.

        设备证书列表

        :return: The device_certificates of this ListDeviceCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.DeviceCertificateSimple`]
        """
        return self._device_certificates

    @device_certificates.setter
    def device_certificates(self, device_certificates):
        r"""Sets the device_certificates of this ListDeviceCertificateResponse.

        设备证书列表

        :param device_certificates: The device_certificates of this ListDeviceCertificateResponse.
        :type device_certificates: list[:class:`huaweicloudsdkiotda.v5.DeviceCertificateSimple`]
        """
        self._device_certificates = device_certificates

    @property
    def page(self):
        r"""Gets the page of this ListDeviceCertificateResponse.

        :return: The page of this ListDeviceCertificateResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListDeviceCertificateResponse.

        :param page: The page of this ListDeviceCertificateResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

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
        if not isinstance(other, ListDeviceCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
