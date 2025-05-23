# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteVpcEndpointRequest:

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
        'subnet_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, vpc_id=None, subnet_id=None):
        r"""DeleteVpcEndpointRequest

        The model defined in huaweicloud sdk

        :param vpc_id: vpc ID
        :type vpc_id: str
        :param subnet_id: 子网编号
        :type subnet_id: str
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this DeleteVpcEndpointRequest.

        vpc ID

        :return: The vpc_id of this DeleteVpcEndpointRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this DeleteVpcEndpointRequest.

        vpc ID

        :param vpc_id: The vpc_id of this DeleteVpcEndpointRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this DeleteVpcEndpointRequest.

        子网编号

        :return: The subnet_id of this DeleteVpcEndpointRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this DeleteVpcEndpointRequest.

        子网编号

        :param subnet_id: The subnet_id of this DeleteVpcEndpointRequest.
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
        if not isinstance(other, DeleteVpcEndpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
