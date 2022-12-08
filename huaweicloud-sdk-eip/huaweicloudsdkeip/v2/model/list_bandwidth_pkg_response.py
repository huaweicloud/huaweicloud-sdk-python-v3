# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPkgResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidthpkgs': 'list[BandwidthPkgResp]',
        'bandwidthpkgs_links': 'list[BandwidthPkgPage]'
    }

    attribute_map = {
        'bandwidthpkgs': 'bandwidthpkgs',
        'bandwidthpkgs_links': 'bandwidthpkgs_links'
    }

    def __init__(self, bandwidthpkgs=None, bandwidthpkgs_links=None):
        """ListBandwidthPkgResponse

        The model defined in huaweicloud sdk

        :param bandwidthpkgs: bandwidthpkg对象列表
        :type bandwidthpkgs: list[:class:`huaweicloudsdkeip.v2.BandwidthPkgResp`]
        :param bandwidthpkgs_links: 翻页展示
        :type bandwidthpkgs_links: list[:class:`huaweicloudsdkeip.v2.BandwidthPkgPage`]
        """
        
        super(ListBandwidthPkgResponse, self).__init__()

        self._bandwidthpkgs = None
        self._bandwidthpkgs_links = None
        self.discriminator = None

        if bandwidthpkgs is not None:
            self.bandwidthpkgs = bandwidthpkgs
        if bandwidthpkgs_links is not None:
            self.bandwidthpkgs_links = bandwidthpkgs_links

    @property
    def bandwidthpkgs(self):
        """Gets the bandwidthpkgs of this ListBandwidthPkgResponse.

        bandwidthpkg对象列表

        :return: The bandwidthpkgs of this ListBandwidthPkgResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v2.BandwidthPkgResp`]
        """
        return self._bandwidthpkgs

    @bandwidthpkgs.setter
    def bandwidthpkgs(self, bandwidthpkgs):
        """Sets the bandwidthpkgs of this ListBandwidthPkgResponse.

        bandwidthpkg对象列表

        :param bandwidthpkgs: The bandwidthpkgs of this ListBandwidthPkgResponse.
        :type bandwidthpkgs: list[:class:`huaweicloudsdkeip.v2.BandwidthPkgResp`]
        """
        self._bandwidthpkgs = bandwidthpkgs

    @property
    def bandwidthpkgs_links(self):
        """Gets the bandwidthpkgs_links of this ListBandwidthPkgResponse.

        翻页展示

        :return: The bandwidthpkgs_links of this ListBandwidthPkgResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v2.BandwidthPkgPage`]
        """
        return self._bandwidthpkgs_links

    @bandwidthpkgs_links.setter
    def bandwidthpkgs_links(self, bandwidthpkgs_links):
        """Sets the bandwidthpkgs_links of this ListBandwidthPkgResponse.

        翻页展示

        :param bandwidthpkgs_links: The bandwidthpkgs_links of this ListBandwidthPkgResponse.
        :type bandwidthpkgs_links: list[:class:`huaweicloudsdkeip.v2.BandwidthPkgPage`]
        """
        self._bandwidthpkgs_links = bandwidthpkgs_links

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
        if not isinstance(other, ListBandwidthPkgResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
