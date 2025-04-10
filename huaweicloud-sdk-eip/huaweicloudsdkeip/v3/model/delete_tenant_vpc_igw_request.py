# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTenantVpcIgwRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_igw_id': 'str'
    }

    attribute_map = {
        'vpc_igw_id': 'vpc_igw_id'
    }

    def __init__(self, vpc_igw_id=None):
        r"""DeleteTenantVpcIgwRequest

        The model defined in huaweicloud sdk

        :param vpc_igw_id: 虚拟igw的uuid
        :type vpc_igw_id: str
        """
        
        

        self._vpc_igw_id = None
        self.discriminator = None

        self.vpc_igw_id = vpc_igw_id

    @property
    def vpc_igw_id(self):
        r"""Gets the vpc_igw_id of this DeleteTenantVpcIgwRequest.

        虚拟igw的uuid

        :return: The vpc_igw_id of this DeleteTenantVpcIgwRequest.
        :rtype: str
        """
        return self._vpc_igw_id

    @vpc_igw_id.setter
    def vpc_igw_id(self, vpc_igw_id):
        r"""Sets the vpc_igw_id of this DeleteTenantVpcIgwRequest.

        虚拟igw的uuid

        :param vpc_igw_id: The vpc_igw_id of this DeleteTenantVpcIgwRequest.
        :type vpc_igw_id: str
        """
        self._vpc_igw_id = vpc_igw_id

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
        if not isinstance(other, DeleteTenantVpcIgwRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
