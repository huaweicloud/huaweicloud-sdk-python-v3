# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWhitelistResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'whitelist': 'WhitelistResp'
    }

    attribute_map = {
        'whitelist': 'whitelist'
    }

    def __init__(self, whitelist=None):
        r"""CreateWhitelistResponse

        The model defined in huaweicloud sdk

        :param whitelist: 
        :type whitelist: :class:`huaweicloudsdkelb.v2.WhitelistResp`
        """
        
        super(CreateWhitelistResponse, self).__init__()

        self._whitelist = None
        self.discriminator = None

        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def whitelist(self):
        r"""Gets the whitelist of this CreateWhitelistResponse.

        :return: The whitelist of this CreateWhitelistResponse.
        :rtype: :class:`huaweicloudsdkelb.v2.WhitelistResp`
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        r"""Sets the whitelist of this CreateWhitelistResponse.

        :param whitelist: The whitelist of this CreateWhitelistResponse.
        :type whitelist: :class:`huaweicloudsdkelb.v2.WhitelistResp`
        """
        self._whitelist = whitelist

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
        if not isinstance(other, CreateWhitelistResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
