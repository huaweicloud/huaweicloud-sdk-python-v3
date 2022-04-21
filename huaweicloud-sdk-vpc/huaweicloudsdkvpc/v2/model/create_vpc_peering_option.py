# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcPeeringOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'request_vpc_info': 'VpcInfo',
        'accept_vpc_info': 'VpcInfo'
    }

    attribute_map = {
        'name': 'name',
        'request_vpc_info': 'request_vpc_info',
        'accept_vpc_info': 'accept_vpc_info'
    }

    def __init__(self, name=None, request_vpc_info=None, accept_vpc_info=None):
        """CreateVpcPeeringOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：对等连接名称 取值范围：支持1~64个字符
        :type name: str
        :param request_vpc_info: 
        :type request_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        :param accept_vpc_info: 
        :type accept_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        
        

        self._name = None
        self._request_vpc_info = None
        self._accept_vpc_info = None
        self.discriminator = None

        self.name = name
        self.request_vpc_info = request_vpc_info
        self.accept_vpc_info = accept_vpc_info

    @property
    def name(self):
        """Gets the name of this CreateVpcPeeringOption.

        功能说明：对等连接名称 取值范围：支持1~64个字符

        :return: The name of this CreateVpcPeeringOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVpcPeeringOption.

        功能说明：对等连接名称 取值范围：支持1~64个字符

        :param name: The name of this CreateVpcPeeringOption.
        :type name: str
        """
        self._name = name

    @property
    def request_vpc_info(self):
        """Gets the request_vpc_info of this CreateVpcPeeringOption.


        :return: The request_vpc_info of this CreateVpcPeeringOption.
        :rtype: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        return self._request_vpc_info

    @request_vpc_info.setter
    def request_vpc_info(self, request_vpc_info):
        """Sets the request_vpc_info of this CreateVpcPeeringOption.


        :param request_vpc_info: The request_vpc_info of this CreateVpcPeeringOption.
        :type request_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        self._request_vpc_info = request_vpc_info

    @property
    def accept_vpc_info(self):
        """Gets the accept_vpc_info of this CreateVpcPeeringOption.


        :return: The accept_vpc_info of this CreateVpcPeeringOption.
        :rtype: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        return self._accept_vpc_info

    @accept_vpc_info.setter
    def accept_vpc_info(self, accept_vpc_info):
        """Sets the accept_vpc_info of this CreateVpcPeeringOption.


        :param accept_vpc_info: The accept_vpc_info of this CreateVpcPeeringOption.
        :type accept_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        self._accept_vpc_info = accept_vpc_info

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
        if not isinstance(other, CreateVpcPeeringOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
