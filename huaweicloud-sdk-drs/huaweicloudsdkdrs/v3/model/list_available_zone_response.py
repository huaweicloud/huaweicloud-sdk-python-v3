# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableZoneResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az_infos': 'list[AzInfoResp]'
    }

    attribute_map = {
        'az_infos': 'az_infos'
    }

    def __init__(self, az_infos=None):
        """ListAvailableZoneResponse

        The model defined in huaweicloud sdk

        :param az_infos: 可用区信息
        :type az_infos: list[:class:`huaweicloudsdkdrs.v3.AzInfoResp`]
        """
        
        super(ListAvailableZoneResponse, self).__init__()

        self._az_infos = None
        self.discriminator = None

        if az_infos is not None:
            self.az_infos = az_infos

    @property
    def az_infos(self):
        """Gets the az_infos of this ListAvailableZoneResponse.

        可用区信息

        :return: The az_infos of this ListAvailableZoneResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.AzInfoResp`]
        """
        return self._az_infos

    @az_infos.setter
    def az_infos(self, az_infos):
        """Sets the az_infos of this ListAvailableZoneResponse.

        可用区信息

        :param az_infos: The az_infos of this ListAvailableZoneResponse.
        :type az_infos: list[:class:`huaweicloudsdkdrs.v3.AzInfoResp`]
        """
        self._az_infos = az_infos

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
        if not isinstance(other, ListAvailableZoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
