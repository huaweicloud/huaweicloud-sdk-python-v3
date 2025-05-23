# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointCreateReq:

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
        'vpc_id': 'str',
        'subnet_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'description': 'description'
    }

    def __init__(self, name=None, vpc_id=None, subnet_id=None, description=None):
        r"""EndpointCreateReq

        The model defined in huaweicloud sdk

        :param name: endpoint名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须以字母或数字开头
        :type name: str
        :param vpc_id: 访问端点所在的VPC的ID
        :type vpc_id: str
        :param subnet_id: 访问端点所在的子网的ID
        :type subnet_id: str
        :param description: 描述
        :type description: str
        """
        
        

        self._name = None
        self._vpc_id = None
        self._subnet_id = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this EndpointCreateReq.

        endpoint名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须以字母或数字开头

        :return: The name of this EndpointCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EndpointCreateReq.

        endpoint名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须以字母或数字开头

        :param name: The name of this EndpointCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this EndpointCreateReq.

        访问端点所在的VPC的ID

        :return: The vpc_id of this EndpointCreateReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this EndpointCreateReq.

        访问端点所在的VPC的ID

        :param vpc_id: The vpc_id of this EndpointCreateReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this EndpointCreateReq.

        访问端点所在的子网的ID

        :return: The subnet_id of this EndpointCreateReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this EndpointCreateReq.

        访问端点所在的子网的ID

        :param subnet_id: The subnet_id of this EndpointCreateReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def description(self):
        r"""Gets the description of this EndpointCreateReq.

        描述

        :return: The description of this EndpointCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EndpointCreateReq.

        描述

        :param description: The description of this EndpointCreateReq.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, EndpointCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
