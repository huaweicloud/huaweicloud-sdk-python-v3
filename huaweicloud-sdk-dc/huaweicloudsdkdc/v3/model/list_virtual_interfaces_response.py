# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVirtualInterfacesResponse(SdkResponse):

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
        'virtual_interfaces': 'list[VirtualInterface]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'virtual_interfaces': 'virtual_interfaces',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, virtual_interfaces=None, page_info=None):
        """ListVirtualInterfacesResponse

        The model defined in huaweicloud sdk

        :param request_id: 操作请求ID
        :type request_id: str
        :param virtual_interfaces: 虚拟接口对象
        :type virtual_interfaces: list[:class:`huaweicloudsdkdc.v3.VirtualInterface`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        
        super(ListVirtualInterfacesResponse, self).__init__()

        self._request_id = None
        self._virtual_interfaces = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if virtual_interfaces is not None:
            self.virtual_interfaces = virtual_interfaces
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListVirtualInterfacesResponse.

        操作请求ID

        :return: The request_id of this ListVirtualInterfacesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListVirtualInterfacesResponse.

        操作请求ID

        :param request_id: The request_id of this ListVirtualInterfacesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def virtual_interfaces(self):
        """Gets the virtual_interfaces of this ListVirtualInterfacesResponse.

        虚拟接口对象

        :return: The virtual_interfaces of this ListVirtualInterfacesResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.VirtualInterface`]
        """
        return self._virtual_interfaces

    @virtual_interfaces.setter
    def virtual_interfaces(self, virtual_interfaces):
        """Sets the virtual_interfaces of this ListVirtualInterfacesResponse.

        虚拟接口对象

        :param virtual_interfaces: The virtual_interfaces of this ListVirtualInterfacesResponse.
        :type virtual_interfaces: list[:class:`huaweicloudsdkdc.v3.VirtualInterface`]
        """
        self._virtual_interfaces = virtual_interfaces

    @property
    def page_info(self):
        """Gets the page_info of this ListVirtualInterfacesResponse.

        :return: The page_info of this ListVirtualInterfacesResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListVirtualInterfacesResponse.

        :param page_info: The page_info of this ListVirtualInterfacesResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
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
        if not isinstance(other, ListVirtualInterfacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
