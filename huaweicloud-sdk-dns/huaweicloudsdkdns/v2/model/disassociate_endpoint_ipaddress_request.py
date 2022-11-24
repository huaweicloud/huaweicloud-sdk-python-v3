# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateEndpointIpaddressRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_id': 'str',
        'ipaddress_id': 'str'
    }

    attribute_map = {
        'endpoint_id': 'endpoint_id',
        'ipaddress_id': 'ipaddress_id'
    }

    def __init__(self, endpoint_id=None, ipaddress_id=None):
        """DisassociateEndpointIpaddressRequest

        The model defined in huaweicloud sdk

        :param endpoint_id: 待解绑定的ip地址所属endpoint的ID。
        :type endpoint_id: str
        :param ipaddress_id: 待解绑定ip地址的ID。
        :type ipaddress_id: str
        """
        
        

        self._endpoint_id = None
        self._ipaddress_id = None
        self.discriminator = None

        self.endpoint_id = endpoint_id
        self.ipaddress_id = ipaddress_id

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this DisassociateEndpointIpaddressRequest.

        待解绑定的ip地址所属endpoint的ID。

        :return: The endpoint_id of this DisassociateEndpointIpaddressRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this DisassociateEndpointIpaddressRequest.

        待解绑定的ip地址所属endpoint的ID。

        :param endpoint_id: The endpoint_id of this DisassociateEndpointIpaddressRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def ipaddress_id(self):
        """Gets the ipaddress_id of this DisassociateEndpointIpaddressRequest.

        待解绑定ip地址的ID。

        :return: The ipaddress_id of this DisassociateEndpointIpaddressRequest.
        :rtype: str
        """
        return self._ipaddress_id

    @ipaddress_id.setter
    def ipaddress_id(self, ipaddress_id):
        """Sets the ipaddress_id of this DisassociateEndpointIpaddressRequest.

        待解绑定ip地址的ID。

        :param ipaddress_id: The ipaddress_id of this DisassociateEndpointIpaddressRequest.
        :type ipaddress_id: str
        """
        self._ipaddress_id = ipaddress_id

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
        if not isinstance(other, DisassociateEndpointIpaddressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
