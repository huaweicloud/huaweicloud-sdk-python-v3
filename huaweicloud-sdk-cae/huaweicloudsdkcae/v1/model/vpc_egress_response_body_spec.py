# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcEgressResponseBodySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'subnet_id': 'str',
        'cidrs': 'list[EgressCidr]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'cidrs': 'cidrs'
    }

    def __init__(self, vpc_id=None, subnet_id=None, cidrs=None):
        """VpcEgressResponseBodySpec

        The model defined in huaweicloud sdk

        :param vpc_id: CAE环境VPCID。
        :type vpc_id: str
        :param subnet_id: CAE环境子网ID。
        :type subnet_id: str
        :param cidrs: CAE环境访问VPC配置。
        :type cidrs: list[:class:`huaweicloudsdkcae.v1.EgressCidr`]
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._cidrs = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def vpc_id(self):
        """Gets the vpc_id of this VpcEgressResponseBodySpec.

        CAE环境VPCID。

        :return: The vpc_id of this VpcEgressResponseBodySpec.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this VpcEgressResponseBodySpec.

        CAE环境VPCID。

        :param vpc_id: The vpc_id of this VpcEgressResponseBodySpec.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this VpcEgressResponseBodySpec.

        CAE环境子网ID。

        :return: The subnet_id of this VpcEgressResponseBodySpec.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this VpcEgressResponseBodySpec.

        CAE环境子网ID。

        :param subnet_id: The subnet_id of this VpcEgressResponseBodySpec.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def cidrs(self):
        """Gets the cidrs of this VpcEgressResponseBodySpec.

        CAE环境访问VPC配置。

        :return: The cidrs of this VpcEgressResponseBodySpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.EgressCidr`]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this VpcEgressResponseBodySpec.

        CAE环境访问VPC配置。

        :param cidrs: The cidrs of this VpcEgressResponseBodySpec.
        :type cidrs: list[:class:`huaweicloudsdkcae.v1.EgressCidr`]
        """
        self._cidrs = cidrs

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
        if not isinstance(other, VpcEgressResponseBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
