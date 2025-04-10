# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRegionInfoOfMeetingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_ip': 'str',
        'region_url': 'str'
    }

    attribute_map = {
        'region_ip': 'regionIP',
        'region_url': 'regionUrl'
    }

    def __init__(self, region_ip=None, region_url=None):
        r"""ShowRegionInfoOfMeetingResponse

        The model defined in huaweicloud sdk

        :param region_ip: 会议所在区域的公网IP地址。
        :type region_ip: str
        :param region_url: 会议所在区域的公网域名。
        :type region_url: str
        """
        
        super(ShowRegionInfoOfMeetingResponse, self).__init__()

        self._region_ip = None
        self._region_url = None
        self.discriminator = None

        if region_ip is not None:
            self.region_ip = region_ip
        if region_url is not None:
            self.region_url = region_url

    @property
    def region_ip(self):
        r"""Gets the region_ip of this ShowRegionInfoOfMeetingResponse.

        会议所在区域的公网IP地址。

        :return: The region_ip of this ShowRegionInfoOfMeetingResponse.
        :rtype: str
        """
        return self._region_ip

    @region_ip.setter
    def region_ip(self, region_ip):
        r"""Sets the region_ip of this ShowRegionInfoOfMeetingResponse.

        会议所在区域的公网IP地址。

        :param region_ip: The region_ip of this ShowRegionInfoOfMeetingResponse.
        :type region_ip: str
        """
        self._region_ip = region_ip

    @property
    def region_url(self):
        r"""Gets the region_url of this ShowRegionInfoOfMeetingResponse.

        会议所在区域的公网域名。

        :return: The region_url of this ShowRegionInfoOfMeetingResponse.
        :rtype: str
        """
        return self._region_url

    @region_url.setter
    def region_url(self, region_url):
        r"""Sets the region_url of this ShowRegionInfoOfMeetingResponse.

        会议所在区域的公网域名。

        :param region_url: The region_url of this ShowRegionInfoOfMeetingResponse.
        :type region_url: str
        """
        self._region_url = region_url

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
        if not isinstance(other, ShowRegionInfoOfMeetingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
