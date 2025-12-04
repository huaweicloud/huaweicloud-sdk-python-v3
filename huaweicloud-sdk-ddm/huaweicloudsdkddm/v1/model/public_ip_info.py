# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIpInfo:

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
        'type': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'binding_entity_id': 'str',
        'binding_entity_name': 'str',
        'binding_entity_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'binding_entity_id': 'binding_entity_id',
        'binding_entity_name': 'binding_entity_name',
        'binding_entity_type': 'binding_entity_type'
    }

    def __init__(self, id=None, type=None, public_ip=None, private_ip=None, binding_entity_id=None, binding_entity_name=None, binding_entity_type=None):
        r"""PublicIpInfo

        The model defined in huaweicloud sdk

        :param id: 弹性公网IP唯一标识。
        :type id: str
        :param type: 弹性公网IP的类型。
        :type type: str
        :param public_ip: 弹性公网IP的地址。
        :type public_ip: str
        :param private_ip: 绑定弹性公网IP的私有IP地址。
        :type private_ip: str
        :param binding_entity_id: 绑定弹性公网IP的实体ID。
        :type binding_entity_id: str
        :param binding_entity_name: 绑定弹性公网IP的实体名称。
        :type binding_entity_name: str
        :param binding_entity_type: 绑定弹性公网IP的实体类型（目前只支持绑定node）。
        :type binding_entity_type: str
        """
        
        

        self._id = None
        self._type = None
        self._public_ip = None
        self._private_ip = None
        self._binding_entity_id = None
        self._binding_entity_name = None
        self._binding_entity_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if binding_entity_id is not None:
            self.binding_entity_id = binding_entity_id
        if binding_entity_name is not None:
            self.binding_entity_name = binding_entity_name
        if binding_entity_type is not None:
            self.binding_entity_type = binding_entity_type

    @property
    def id(self):
        r"""Gets the id of this PublicIpInfo.

        弹性公网IP唯一标识。

        :return: The id of this PublicIpInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublicIpInfo.

        弹性公网IP唯一标识。

        :param id: The id of this PublicIpInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this PublicIpInfo.

        弹性公网IP的类型。

        :return: The type of this PublicIpInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PublicIpInfo.

        弹性公网IP的类型。

        :param type: The type of this PublicIpInfo.
        :type type: str
        """
        self._type = type

    @property
    def public_ip(self):
        r"""Gets the public_ip of this PublicIpInfo.

        弹性公网IP的地址。

        :return: The public_ip of this PublicIpInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this PublicIpInfo.

        弹性公网IP的地址。

        :param public_ip: The public_ip of this PublicIpInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this PublicIpInfo.

        绑定弹性公网IP的私有IP地址。

        :return: The private_ip of this PublicIpInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this PublicIpInfo.

        绑定弹性公网IP的私有IP地址。

        :param private_ip: The private_ip of this PublicIpInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def binding_entity_id(self):
        r"""Gets the binding_entity_id of this PublicIpInfo.

        绑定弹性公网IP的实体ID。

        :return: The binding_entity_id of this PublicIpInfo.
        :rtype: str
        """
        return self._binding_entity_id

    @binding_entity_id.setter
    def binding_entity_id(self, binding_entity_id):
        r"""Sets the binding_entity_id of this PublicIpInfo.

        绑定弹性公网IP的实体ID。

        :param binding_entity_id: The binding_entity_id of this PublicIpInfo.
        :type binding_entity_id: str
        """
        self._binding_entity_id = binding_entity_id

    @property
    def binding_entity_name(self):
        r"""Gets the binding_entity_name of this PublicIpInfo.

        绑定弹性公网IP的实体名称。

        :return: The binding_entity_name of this PublicIpInfo.
        :rtype: str
        """
        return self._binding_entity_name

    @binding_entity_name.setter
    def binding_entity_name(self, binding_entity_name):
        r"""Sets the binding_entity_name of this PublicIpInfo.

        绑定弹性公网IP的实体名称。

        :param binding_entity_name: The binding_entity_name of this PublicIpInfo.
        :type binding_entity_name: str
        """
        self._binding_entity_name = binding_entity_name

    @property
    def binding_entity_type(self):
        r"""Gets the binding_entity_type of this PublicIpInfo.

        绑定弹性公网IP的实体类型（目前只支持绑定node）。

        :return: The binding_entity_type of this PublicIpInfo.
        :rtype: str
        """
        return self._binding_entity_type

    @binding_entity_type.setter
    def binding_entity_type(self, binding_entity_type):
        r"""Sets the binding_entity_type of this PublicIpInfo.

        绑定弹性公网IP的实体类型（目前只支持绑定node）。

        :param binding_entity_type: The binding_entity_type of this PublicIpInfo.
        :type binding_entity_type: str
        """
        self._binding_entity_type = binding_entity_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicIpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
