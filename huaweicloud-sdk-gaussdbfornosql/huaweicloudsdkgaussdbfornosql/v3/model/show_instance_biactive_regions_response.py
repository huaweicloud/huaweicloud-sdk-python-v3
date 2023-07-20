# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceBiactiveRegionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_codes': 'list[str]'
    }

    attribute_map = {
        'region_codes': 'region_codes'
    }

    def __init__(self, region_codes=None):
        """ShowInstanceBiactiveRegionsResponse

        The model defined in huaweicloud sdk

        :param region_codes: 
        :type region_codes: list[str]
        """
        
        super(ShowInstanceBiactiveRegionsResponse, self).__init__()

        self._region_codes = None
        self.discriminator = None

        if region_codes is not None:
            self.region_codes = region_codes

    @property
    def region_codes(self):
        """Gets the region_codes of this ShowInstanceBiactiveRegionsResponse.

        :return: The region_codes of this ShowInstanceBiactiveRegionsResponse.
        :rtype: list[str]
        """
        return self._region_codes

    @region_codes.setter
    def region_codes(self, region_codes):
        """Sets the region_codes of this ShowInstanceBiactiveRegionsResponse.

        :param region_codes: The region_codes of this ShowInstanceBiactiveRegionsResponse.
        :type region_codes: list[str]
        """
        self._region_codes = region_codes

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
        if not isinstance(other, ShowInstanceBiactiveRegionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
