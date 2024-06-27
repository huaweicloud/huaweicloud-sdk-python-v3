# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFirewallReq:

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
        'enterprise_project_id': 'str',
        'tags': 'list[CreateFirewallReqTags]',
        'flavor': 'CreateFirewallReqFlavor',
        'charge_info': 'CreateFirewallReqChargeInfo'
    }

    attribute_map = {
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'flavor': 'flavor',
        'charge_info': 'charge_info'
    }

    def __init__(self, name=None, enterprise_project_id=None, tags=None, flavor=None, charge_info=None):
        """CreateFirewallReq

        The model defined in huaweicloud sdk

        :param name: 防火墙名称
        :type name: str
        :param enterprise_project_id: 企业项目ID，租户未开启企业项目时传0
        :type enterprise_project_id: str
        :param tags: 资源标签
        :type tags: list[:class:`huaweicloudsdkcfw.v1.CreateFirewallReqTags`]
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkcfw.v1.CreateFirewallReqFlavor`
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkcfw.v1.CreateFirewallReqChargeInfo`
        """
        
        

        self._name = None
        self._enterprise_project_id = None
        self._tags = None
        self._flavor = None
        self._charge_info = None
        self.discriminator = None

        self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        self.flavor = flavor
        self.charge_info = charge_info

    @property
    def name(self):
        """Gets the name of this CreateFirewallReq.

        防火墙名称

        :return: The name of this CreateFirewallReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFirewallReq.

        防火墙名称

        :param name: The name of this CreateFirewallReq.
        :type name: str
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateFirewallReq.

        企业项目ID，租户未开启企业项目时传0

        :return: The enterprise_project_id of this CreateFirewallReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateFirewallReq.

        企业项目ID，租户未开启企业项目时传0

        :param enterprise_project_id: The enterprise_project_id of this CreateFirewallReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateFirewallReq.

        资源标签

        :return: The tags of this CreateFirewallReq.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.CreateFirewallReqTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateFirewallReq.

        资源标签

        :param tags: The tags of this CreateFirewallReq.
        :type tags: list[:class:`huaweicloudsdkcfw.v1.CreateFirewallReqTags`]
        """
        self._tags = tags

    @property
    def flavor(self):
        """Gets the flavor of this CreateFirewallReq.

        :return: The flavor of this CreateFirewallReq.
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateFirewallReqFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this CreateFirewallReq.

        :param flavor: The flavor of this CreateFirewallReq.
        :type flavor: :class:`huaweicloudsdkcfw.v1.CreateFirewallReqFlavor`
        """
        self._flavor = flavor

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateFirewallReq.

        :return: The charge_info of this CreateFirewallReq.
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateFirewallReqChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateFirewallReq.

        :param charge_info: The charge_info of this CreateFirewallReq.
        :type charge_info: :class:`huaweicloudsdkcfw.v1.CreateFirewallReqChargeInfo`
        """
        self._charge_info = charge_info

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
        if not isinstance(other, CreateFirewallReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
