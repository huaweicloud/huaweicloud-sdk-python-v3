# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessoryAccessUrlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'accessory_urls': 'list[AccessoryUrl]'
    }

    attribute_map = {
        'accessory_urls': 'accessory_urls'
    }

    def __init__(self, accessory_urls=None):
        """ListAccessoryAccessUrlsResponse

        The model defined in huaweicloud sdk

        :param accessory_urls: 附件链接
        :type accessory_urls: list[:class:`huaweicloudsdkosm.v2.AccessoryUrl`]
        """
        
        super(ListAccessoryAccessUrlsResponse, self).__init__()

        self._accessory_urls = None
        self.discriminator = None

        if accessory_urls is not None:
            self.accessory_urls = accessory_urls

    @property
    def accessory_urls(self):
        """Gets the accessory_urls of this ListAccessoryAccessUrlsResponse.

        附件链接

        :return: The accessory_urls of this ListAccessoryAccessUrlsResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.AccessoryUrl`]
        """
        return self._accessory_urls

    @accessory_urls.setter
    def accessory_urls(self, accessory_urls):
        """Sets the accessory_urls of this ListAccessoryAccessUrlsResponse.

        附件链接

        :param accessory_urls: The accessory_urls of this ListAccessoryAccessUrlsResponse.
        :type accessory_urls: list[:class:`huaweicloudsdkosm.v2.AccessoryUrl`]
        """
        self._accessory_urls = accessory_urls

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
        if not isinstance(other, ListAccessoryAccessUrlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
