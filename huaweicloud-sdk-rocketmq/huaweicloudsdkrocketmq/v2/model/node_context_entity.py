# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeContextEntity:

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
        'broker_name': 'str',
        'broker_id': 'int',
        'address': 'str',
        'public_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'broker_name': 'broker_name',
        'broker_id': 'broker_id',
        'address': 'address',
        'public_address': 'public_address'
    }

    def __init__(self, id=None, broker_name=None, broker_id=None, address=None, public_address=None):
        r"""NodeContextEntity

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param broker_name: broker名称
        :type broker_name: str
        :param broker_id: broker的ID
        :type broker_id: int
        :param address: 地址
        :type address: str
        :param public_address: 公网地址
        :type public_address: str
        """
        
        

        self._id = None
        self._broker_name = None
        self._broker_id = None
        self._address = None
        self._public_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if broker_name is not None:
            self.broker_name = broker_name
        if broker_id is not None:
            self.broker_id = broker_id
        if address is not None:
            self.address = address
        if public_address is not None:
            self.public_address = public_address

    @property
    def id(self):
        r"""Gets the id of this NodeContextEntity.

        ID

        :return: The id of this NodeContextEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NodeContextEntity.

        ID

        :param id: The id of this NodeContextEntity.
        :type id: str
        """
        self._id = id

    @property
    def broker_name(self):
        r"""Gets the broker_name of this NodeContextEntity.

        broker名称

        :return: The broker_name of this NodeContextEntity.
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        r"""Sets the broker_name of this NodeContextEntity.

        broker名称

        :param broker_name: The broker_name of this NodeContextEntity.
        :type broker_name: str
        """
        self._broker_name = broker_name

    @property
    def broker_id(self):
        r"""Gets the broker_id of this NodeContextEntity.

        broker的ID

        :return: The broker_id of this NodeContextEntity.
        :rtype: int
        """
        return self._broker_id

    @broker_id.setter
    def broker_id(self, broker_id):
        r"""Sets the broker_id of this NodeContextEntity.

        broker的ID

        :param broker_id: The broker_id of this NodeContextEntity.
        :type broker_id: int
        """
        self._broker_id = broker_id

    @property
    def address(self):
        r"""Gets the address of this NodeContextEntity.

        地址

        :return: The address of this NodeContextEntity.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this NodeContextEntity.

        地址

        :param address: The address of this NodeContextEntity.
        :type address: str
        """
        self._address = address

    @property
    def public_address(self):
        r"""Gets the public_address of this NodeContextEntity.

        公网地址

        :return: The public_address of this NodeContextEntity.
        :rtype: str
        """
        return self._public_address

    @public_address.setter
    def public_address(self, public_address):
        r"""Sets the public_address of this NodeContextEntity.

        公网地址

        :param public_address: The public_address of this NodeContextEntity.
        :type public_address: str
        """
        self._public_address = public_address

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
        if not isinstance(other, NodeContextEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
