# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcObject:

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
        'cidr': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr'
    }

    def __init__(self, id=None, name=None, cidr=None):
        """VpcObject

        The model defined in huaweicloud sdk

        :param id: 虚拟私有云ID，如果是自动创建，填“autoCreate”
        :type id: str
        :param name: 虚拟私有云名称
        :type name: str
        :param cidr: VPC的网段，默认192.168.0.0/16
        :type cidr: str
        """
        
        

        self._id = None
        self._name = None
        self._cidr = None
        self.discriminator = None

        self.id = id
        self.name = name
        if cidr is not None:
            self.cidr = cidr

    @property
    def id(self):
        """Gets the id of this VpcObject.

        虚拟私有云ID，如果是自动创建，填“autoCreate”

        :return: The id of this VpcObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpcObject.

        虚拟私有云ID，如果是自动创建，填“autoCreate”

        :param id: The id of this VpcObject.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VpcObject.

        虚拟私有云名称

        :return: The name of this VpcObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpcObject.

        虚拟私有云名称

        :param name: The name of this VpcObject.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this VpcObject.

        VPC的网段，默认192.168.0.0/16

        :return: The cidr of this VpcObject.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this VpcObject.

        VPC的网段，默认192.168.0.0/16

        :param cidr: The cidr of this VpcObject.
        :type cidr: str
        """
        self._cidr = cidr

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
        if not isinstance(other, VpcObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
