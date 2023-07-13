# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcEndpointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'xrole': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'xrole': 'xrole',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, flavor=None, xrole=None, vpc_id=None, subnet_id=None):
        """CreateVpcEndpointRequestBody

        The model defined in huaweicloud sdk

        :param flavor: 选定EP的规格，默认为大规格
        :type flavor: str
        :param xrole: 制作EP时使用的租户委托名称
        :type xrole: str
        :param vpc_id: 对接EP使用的租户VPCID
        :type vpc_id: str
        :param subnet_id: 对接EP使用的租户子网ID
        :type subnet_id: str
        """
        
        

        self._flavor = None
        self._xrole = None
        self._vpc_id = None
        self._subnet_id = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if xrole is not None:
            self.xrole = xrole
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

    @property
    def flavor(self):
        """Gets the flavor of this CreateVpcEndpointRequestBody.

        选定EP的规格，默认为大规格

        :return: The flavor of this CreateVpcEndpointRequestBody.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this CreateVpcEndpointRequestBody.

        选定EP的规格，默认为大规格

        :param flavor: The flavor of this CreateVpcEndpointRequestBody.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def xrole(self):
        """Gets the xrole of this CreateVpcEndpointRequestBody.

        制作EP时使用的租户委托名称

        :return: The xrole of this CreateVpcEndpointRequestBody.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        """Sets the xrole of this CreateVpcEndpointRequestBody.

        制作EP时使用的租户委托名称

        :param xrole: The xrole of this CreateVpcEndpointRequestBody.
        :type xrole: str
        """
        self._xrole = xrole

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateVpcEndpointRequestBody.

        对接EP使用的租户VPCID

        :return: The vpc_id of this CreateVpcEndpointRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateVpcEndpointRequestBody.

        对接EP使用的租户VPCID

        :param vpc_id: The vpc_id of this CreateVpcEndpointRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateVpcEndpointRequestBody.

        对接EP使用的租户子网ID

        :return: The subnet_id of this CreateVpcEndpointRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateVpcEndpointRequestBody.

        对接EP使用的租户子网ID

        :param subnet_id: The subnet_id of this CreateVpcEndpointRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, CreateVpcEndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
