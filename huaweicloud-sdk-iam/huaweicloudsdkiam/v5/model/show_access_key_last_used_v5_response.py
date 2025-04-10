# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccessKeyLastUsedV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_last_used': 'AccessKeyLastUsed'
    }

    attribute_map = {
        'access_key_last_used': 'access_key_last_used'
    }

    def __init__(self, access_key_last_used=None):
        r"""ShowAccessKeyLastUsedV5Response

        The model defined in huaweicloud sdk

        :param access_key_last_used: 
        :type access_key_last_used: :class:`huaweicloudsdkiam.v5.AccessKeyLastUsed`
        """
        
        super(ShowAccessKeyLastUsedV5Response, self).__init__()

        self._access_key_last_used = None
        self.discriminator = None

        if access_key_last_used is not None:
            self.access_key_last_used = access_key_last_used

    @property
    def access_key_last_used(self):
        r"""Gets the access_key_last_used of this ShowAccessKeyLastUsedV5Response.

        :return: The access_key_last_used of this ShowAccessKeyLastUsedV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.AccessKeyLastUsed`
        """
        return self._access_key_last_used

    @access_key_last_used.setter
    def access_key_last_used(self, access_key_last_used):
        r"""Sets the access_key_last_used of this ShowAccessKeyLastUsedV5Response.

        :param access_key_last_used: The access_key_last_used of this ShowAccessKeyLastUsedV5Response.
        :type access_key_last_used: :class:`huaweicloudsdkiam.v5.AccessKeyLastUsed`
        """
        self._access_key_last_used = access_key_last_used

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
        if not isinstance(other, ShowAccessKeyLastUsedV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
