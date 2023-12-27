# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSourceIpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips': 'list[str]'
    }

    attribute_map = {
        'ips': 'ips'
    }

    def __init__(self, ips=None):
        """ListSourceIpsResponse

        The model defined in huaweicloud sdk

        :param ips: 查询高防回源IP段列表
        :type ips: list[str]
        """
        
        super(ListSourceIpsResponse, self).__init__()

        self._ips = None
        self.discriminator = None

        if ips is not None:
            self.ips = ips

    @property
    def ips(self):
        """Gets the ips of this ListSourceIpsResponse.

        查询高防回源IP段列表

        :return: The ips of this ListSourceIpsResponse.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this ListSourceIpsResponse.

        查询高防回源IP段列表

        :param ips: The ips of this ListSourceIpsResponse.
        :type ips: list[str]
        """
        self._ips = ips

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
        if not isinstance(other, ListSourceIpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
