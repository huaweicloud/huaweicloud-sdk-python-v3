# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailabilityZoneInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'azs': 'list[AzInfo]'
    }

    attribute_map = {
        'azs': 'azs'
    }

    def __init__(self, azs=None):
        """ListAvailabilityZoneInfosResponse

        The model defined in huaweicloud sdk

        :param azs: az列表
        :type azs: list[:class:`huaweicloudsdkdbss.v1.AzInfo`]
        """
        
        super(ListAvailabilityZoneInfosResponse, self).__init__()

        self._azs = None
        self.discriminator = None

        if azs is not None:
            self.azs = azs

    @property
    def azs(self):
        """Gets the azs of this ListAvailabilityZoneInfosResponse.

        az列表

        :return: The azs of this ListAvailabilityZoneInfosResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AzInfo`]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        """Sets the azs of this ListAvailabilityZoneInfosResponse.

        az列表

        :param azs: The azs of this ListAvailabilityZoneInfosResponse.
        :type azs: list[:class:`huaweicloudsdkdbss.v1.AzInfo`]
        """
        self._azs = azs

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
        if not isinstance(other, ListAvailabilityZoneInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
