# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGdgwRouteTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'gdgw_routetable': 'list[CommonRoutetable]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'gdgw_routetable': 'gdgw_routetable'
    }

    def __init__(self, request_id=None, gdgw_routetable=None):
        """UpdateGdgwRouteTableResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求id
        :type request_id: str
        :param gdgw_routetable: 全域接入网关路由表
        :type gdgw_routetable: list[:class:`huaweicloudsdkdc.v3.CommonRoutetable`]
        """
        
        super(UpdateGdgwRouteTableResponse, self).__init__()

        self._request_id = None
        self._gdgw_routetable = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if gdgw_routetable is not None:
            self.gdgw_routetable = gdgw_routetable

    @property
    def request_id(self):
        """Gets the request_id of this UpdateGdgwRouteTableResponse.

        请求id

        :return: The request_id of this UpdateGdgwRouteTableResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateGdgwRouteTableResponse.

        请求id

        :param request_id: The request_id of this UpdateGdgwRouteTableResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def gdgw_routetable(self):
        """Gets the gdgw_routetable of this UpdateGdgwRouteTableResponse.

        全域接入网关路由表

        :return: The gdgw_routetable of this UpdateGdgwRouteTableResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.CommonRoutetable`]
        """
        return self._gdgw_routetable

    @gdgw_routetable.setter
    def gdgw_routetable(self, gdgw_routetable):
        """Sets the gdgw_routetable of this UpdateGdgwRouteTableResponse.

        全域接入网关路由表

        :param gdgw_routetable: The gdgw_routetable of this UpdateGdgwRouteTableResponse.
        :type gdgw_routetable: list[:class:`huaweicloudsdkdc.v3.CommonRoutetable`]
        """
        self._gdgw_routetable = gdgw_routetable

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
        if not isinstance(other, UpdateGdgwRouteTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
