# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EgressCidr:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidr': 'str',
        'route_table_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'cidr': 'cidr',
        'route_table_id': 'route_table_id',
        'id': 'id'
    }

    def __init__(self, cidr=None, route_table_id=None, id=None):
        """EgressCidr

        The model defined in huaweicloud sdk

        :param cidr: 目的网络Cidr。
        :type cidr: str
        :param route_table_id: 目的网络所属CAE环境VPC的路由表ID。
        :type route_table_id: str
        :param id: CAE环境访问VPC配置ID。
        :type id: str
        """
        
        

        self._cidr = None
        self._route_table_id = None
        self._id = None
        self.discriminator = None

        self.cidr = cidr
        self.route_table_id = route_table_id
        if id is not None:
            self.id = id

    @property
    def cidr(self):
        """Gets the cidr of this EgressCidr.

        目的网络Cidr。

        :return: The cidr of this EgressCidr.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this EgressCidr.

        目的网络Cidr。

        :param cidr: The cidr of this EgressCidr.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def route_table_id(self):
        """Gets the route_table_id of this EgressCidr.

        目的网络所属CAE环境VPC的路由表ID。

        :return: The route_table_id of this EgressCidr.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this EgressCidr.

        目的网络所属CAE环境VPC的路由表ID。

        :param route_table_id: The route_table_id of this EgressCidr.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def id(self):
        """Gets the id of this EgressCidr.

        CAE环境访问VPC配置ID。

        :return: The id of this EgressCidr.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EgressCidr.

        CAE环境访问VPC配置ID。

        :param id: The id of this EgressCidr.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, EgressCidr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
