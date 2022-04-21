# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAddressGroupResponse(SdkResponse):

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
        'address_groups': 'list[AddressGroup]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'address_groups': 'address_groups',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, address_groups=None, page_info=None):
        """ListAddressGroupResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param address_groups: 地址组列表响应体
        :type address_groups: list[:class:`huaweicloudsdkvpc.v3.AddressGroup`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        
        super(ListAddressGroupResponse, self).__init__()

        self._request_id = None
        self._address_groups = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if address_groups is not None:
            self.address_groups = address_groups
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListAddressGroupResponse.

        请求ID

        :return: The request_id of this ListAddressGroupResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListAddressGroupResponse.

        请求ID

        :param request_id: The request_id of this ListAddressGroupResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def address_groups(self):
        """Gets the address_groups of this ListAddressGroupResponse.

        地址组列表响应体

        :return: The address_groups of this ListAddressGroupResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.AddressGroup`]
        """
        return self._address_groups

    @address_groups.setter
    def address_groups(self, address_groups):
        """Sets the address_groups of this ListAddressGroupResponse.

        地址组列表响应体

        :param address_groups: The address_groups of this ListAddressGroupResponse.
        :type address_groups: list[:class:`huaweicloudsdkvpc.v3.AddressGroup`]
        """
        self._address_groups = address_groups

    @property
    def page_info(self):
        """Gets the page_info of this ListAddressGroupResponse.


        :return: The page_info of this ListAddressGroupResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAddressGroupResponse.


        :param page_info: The page_info of this ListAddressGroupResponse.
        :type page_info: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAddressGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
