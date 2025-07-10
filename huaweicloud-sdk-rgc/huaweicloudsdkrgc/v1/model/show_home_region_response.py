# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHomeRegionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'home_region': 'str'
    }

    attribute_map = {
        'home_region': 'home_region'
    }

    def __init__(self, home_region=None):
        r"""ShowHomeRegionResponse

        The model defined in huaweicloud sdk

        :param home_region: 区域名称。
        :type home_region: str
        """
        
        super(ShowHomeRegionResponse, self).__init__()

        self._home_region = None
        self.discriminator = None

        if home_region is not None:
            self.home_region = home_region

    @property
    def home_region(self):
        r"""Gets the home_region of this ShowHomeRegionResponse.

        区域名称。

        :return: The home_region of this ShowHomeRegionResponse.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        r"""Sets the home_region of this ShowHomeRegionResponse.

        区域名称。

        :param home_region: The home_region of this ShowHomeRegionResponse.
        :type home_region: str
        """
        self._home_region = home_region

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
        if not isinstance(other, ShowHomeRegionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
