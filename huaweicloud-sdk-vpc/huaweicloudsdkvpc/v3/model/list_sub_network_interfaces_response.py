# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubNetworkInterfacesResponse(SdkResponse):

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
        'sub_network_interfaces': 'list[SubNetworkInterface]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'sub_network_interfaces': 'sub_network_interfaces',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, sub_network_interfaces=None, page_info=None):
        """ListSubNetworkInterfacesResponse

        The model defined in huaweicloud sdk

        :param request_id: 1、功能说明：请求ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type request_id: str
        :param sub_network_interfaces: 1、功能说明：辅助弹性网卡查询对象 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type sub_network_interfaces: list[:class:`huaweicloudsdkvpc.v3.SubNetworkInterface`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        
        super(ListSubNetworkInterfacesResponse, self).__init__()

        self._request_id = None
        self._sub_network_interfaces = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if sub_network_interfaces is not None:
            self.sub_network_interfaces = sub_network_interfaces
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListSubNetworkInterfacesResponse.

        1、功能说明：请求ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The request_id of this ListSubNetworkInterfacesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListSubNetworkInterfacesResponse.

        1、功能说明：请求ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param request_id: The request_id of this ListSubNetworkInterfacesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def sub_network_interfaces(self):
        """Gets the sub_network_interfaces of this ListSubNetworkInterfacesResponse.

        1、功能说明：辅助弹性网卡查询对象 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The sub_network_interfaces of this ListSubNetworkInterfacesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.SubNetworkInterface`]
        """
        return self._sub_network_interfaces

    @sub_network_interfaces.setter
    def sub_network_interfaces(self, sub_network_interfaces):
        """Sets the sub_network_interfaces of this ListSubNetworkInterfacesResponse.

        1、功能说明：辅助弹性网卡查询对象 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param sub_network_interfaces: The sub_network_interfaces of this ListSubNetworkInterfacesResponse.
        :type sub_network_interfaces: list[:class:`huaweicloudsdkvpc.v3.SubNetworkInterface`]
        """
        self._sub_network_interfaces = sub_network_interfaces

    @property
    def page_info(self):
        """Gets the page_info of this ListSubNetworkInterfacesResponse.

        :return: The page_info of this ListSubNetworkInterfacesResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListSubNetworkInterfacesResponse.

        :param page_info: The page_info of this ListSubNetworkInterfacesResponse.
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
        if not isinstance(other, ListSubNetworkInterfacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
