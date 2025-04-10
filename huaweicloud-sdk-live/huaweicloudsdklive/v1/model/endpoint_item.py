# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hls_package': 'list[HlsPackageItem]',
        'dash_package': 'list[DashPackageItem]',
        'mss_package': 'list[MssPackageItem]'
    }

    attribute_map = {
        'hls_package': 'hls_package',
        'dash_package': 'dash_package',
        'mss_package': 'mss_package'
    }

    def __init__(self, hls_package=None, dash_package=None, mss_package=None):
        r"""EndpointItem

        The model defined in huaweicloud sdk

        :param hls_package: HLS打包信息
        :type hls_package: list[:class:`huaweicloudsdklive.v1.HlsPackageItem`]
        :param dash_package: DASH打包信息
        :type dash_package: list[:class:`huaweicloudsdklive.v1.DashPackageItem`]
        :param mss_package: MSS打包信息
        :type mss_package: list[:class:`huaweicloudsdklive.v1.MssPackageItem`]
        """
        
        

        self._hls_package = None
        self._dash_package = None
        self._mss_package = None
        self.discriminator = None

        if hls_package is not None:
            self.hls_package = hls_package
        if dash_package is not None:
            self.dash_package = dash_package
        if mss_package is not None:
            self.mss_package = mss_package

    @property
    def hls_package(self):
        r"""Gets the hls_package of this EndpointItem.

        HLS打包信息

        :return: The hls_package of this EndpointItem.
        :rtype: list[:class:`huaweicloudsdklive.v1.HlsPackageItem`]
        """
        return self._hls_package

    @hls_package.setter
    def hls_package(self, hls_package):
        r"""Sets the hls_package of this EndpointItem.

        HLS打包信息

        :param hls_package: The hls_package of this EndpointItem.
        :type hls_package: list[:class:`huaweicloudsdklive.v1.HlsPackageItem`]
        """
        self._hls_package = hls_package

    @property
    def dash_package(self):
        r"""Gets the dash_package of this EndpointItem.

        DASH打包信息

        :return: The dash_package of this EndpointItem.
        :rtype: list[:class:`huaweicloudsdklive.v1.DashPackageItem`]
        """
        return self._dash_package

    @dash_package.setter
    def dash_package(self, dash_package):
        r"""Sets the dash_package of this EndpointItem.

        DASH打包信息

        :param dash_package: The dash_package of this EndpointItem.
        :type dash_package: list[:class:`huaweicloudsdklive.v1.DashPackageItem`]
        """
        self._dash_package = dash_package

    @property
    def mss_package(self):
        r"""Gets the mss_package of this EndpointItem.

        MSS打包信息

        :return: The mss_package of this EndpointItem.
        :rtype: list[:class:`huaweicloudsdklive.v1.MssPackageItem`]
        """
        return self._mss_package

    @mss_package.setter
    def mss_package(self, mss_package):
        r"""Sets the mss_package of this EndpointItem.

        MSS打包信息

        :param mss_package: The mss_package of this EndpointItem.
        :type mss_package: list[:class:`huaweicloudsdklive.v1.MssPackageItem`]
        """
        self._mss_package = mss_package

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
        if not isinstance(other, EndpointItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
