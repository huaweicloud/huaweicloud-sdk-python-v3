# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEWFirewallInspectVpcResp:

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
        'subnet_ids': 'list[str]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_ids': 'subnet_ids'
    }

    def __init__(self, vpc_id=None, subnet_ids=None):
        r"""CreateEWFirewallInspectVpcResp

        The model defined in huaweicloud sdk

        :param vpc_id: 引流VPC的ID
        :type vpc_id: str
        :param subnet_ids: 创建的引流VPC的子网ID列表
        :type subnet_ids: list[str]
        """
        
        

        self._vpc_id = None
        self._subnet_ids = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateEWFirewallInspectVpcResp.

        引流VPC的ID

        :return: The vpc_id of this CreateEWFirewallInspectVpcResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateEWFirewallInspectVpcResp.

        引流VPC的ID

        :param vpc_id: The vpc_id of this CreateEWFirewallInspectVpcResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_ids(self):
        r"""Gets the subnet_ids of this CreateEWFirewallInspectVpcResp.

        创建的引流VPC的子网ID列表

        :return: The subnet_ids of this CreateEWFirewallInspectVpcResp.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        r"""Sets the subnet_ids of this CreateEWFirewallInspectVpcResp.

        创建的引流VPC的子网ID列表

        :param subnet_ids: The subnet_ids of this CreateEWFirewallInspectVpcResp.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

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
        if not isinstance(other, CreateEWFirewallInspectVpcResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
