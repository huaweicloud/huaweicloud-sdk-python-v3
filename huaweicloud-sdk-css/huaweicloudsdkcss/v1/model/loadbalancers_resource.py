# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadbalancersResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'l7_flavor_id': 'str',
        'ip_target_enable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'l7_flavor_id': 'l7_flavor_id',
        'ip_target_enable': 'ip_target_enable'
    }

    def __init__(self, id=None, name=None, l7_flavor_id=None, ip_target_enable=None):
        r"""LoadbalancersResource

        The model defined in huaweicloud sdk

        :param id: 负载均衡器ID。
        :type id: str
        :param name: 负载均衡器名称。
        :type name: str
        :param l7_flavor_id: 7层协议Id。
        :type l7_flavor_id: str
        :param ip_target_enable: 是否开启跨VPC后端。
        :type ip_target_enable: bool
        """
        
        

        self._id = None
        self._name = None
        self._l7_flavor_id = None
        self._ip_target_enable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable

    @property
    def id(self):
        r"""Gets the id of this LoadbalancersResource.

        负载均衡器ID。

        :return: The id of this LoadbalancersResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LoadbalancersResource.

        负载均衡器ID。

        :param id: The id of this LoadbalancersResource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this LoadbalancersResource.

        负载均衡器名称。

        :return: The name of this LoadbalancersResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LoadbalancersResource.

        负载均衡器名称。

        :param name: The name of this LoadbalancersResource.
        :type name: str
        """
        self._name = name

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this LoadbalancersResource.

        7层协议Id。

        :return: The l7_flavor_id of this LoadbalancersResource.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this LoadbalancersResource.

        7层协议Id。

        :param l7_flavor_id: The l7_flavor_id of this LoadbalancersResource.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def ip_target_enable(self):
        r"""Gets the ip_target_enable of this LoadbalancersResource.

        是否开启跨VPC后端。

        :return: The ip_target_enable of this LoadbalancersResource.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        r"""Sets the ip_target_enable of this LoadbalancersResource.

        是否开启跨VPC后端。

        :param ip_target_enable: The ip_target_enable of this LoadbalancersResource.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

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
        if not isinstance(other, LoadbalancersResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
