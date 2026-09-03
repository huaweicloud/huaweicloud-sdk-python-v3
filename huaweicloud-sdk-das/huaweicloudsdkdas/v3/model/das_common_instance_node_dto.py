# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DasCommonInstanceNodeDto:

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
        'status': 'str',
        'role': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'group_id': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'role': 'role',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'group_id': 'group_id',
        'group_name': 'group_name'
    }

    def __init__(self, id=None, name=None, status=None, role=None, private_ip=None, public_ip=None, group_id=None, group_name=None):
        r"""DasCommonInstanceNodeDto

        The model defined in huaweicloud sdk

        :param id: 节点ID
        :type id: str
        :param name: 节点名称
        :type name: str
        :param status: 节点状态
        :type status: str
        :param role: 节点角色
        :type role: str
        :param private_ip: 节点私有IP
        :type private_ip: str
        :param public_ip: 节点公共IP
        :type public_ip: str
        :param group_id: 节点组ID
        :type group_id: str
        :param group_name: 节点组名称
        :type group_name: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._role = None
        self._private_ip = None
        self._public_ip = None
        self._group_id = None
        self._group_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if role is not None:
            self.role = role
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name

    @property
    def id(self):
        r"""Gets the id of this DasCommonInstanceNodeDto.

        节点ID

        :return: The id of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DasCommonInstanceNodeDto.

        节点ID

        :param id: The id of this DasCommonInstanceNodeDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DasCommonInstanceNodeDto.

        节点名称

        :return: The name of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DasCommonInstanceNodeDto.

        节点名称

        :param name: The name of this DasCommonInstanceNodeDto.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this DasCommonInstanceNodeDto.

        节点状态

        :return: The status of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DasCommonInstanceNodeDto.

        节点状态

        :param status: The status of this DasCommonInstanceNodeDto.
        :type status: str
        """
        self._status = status

    @property
    def role(self):
        r"""Gets the role of this DasCommonInstanceNodeDto.

        节点角色

        :return: The role of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this DasCommonInstanceNodeDto.

        节点角色

        :param role: The role of this DasCommonInstanceNodeDto.
        :type role: str
        """
        self._role = role

    @property
    def private_ip(self):
        r"""Gets the private_ip of this DasCommonInstanceNodeDto.

        节点私有IP

        :return: The private_ip of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this DasCommonInstanceNodeDto.

        节点私有IP

        :param private_ip: The private_ip of this DasCommonInstanceNodeDto.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this DasCommonInstanceNodeDto.

        节点公共IP

        :return: The public_ip of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this DasCommonInstanceNodeDto.

        节点公共IP

        :param public_ip: The public_ip of this DasCommonInstanceNodeDto.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def group_id(self):
        r"""Gets the group_id of this DasCommonInstanceNodeDto.

        节点组ID

        :return: The group_id of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DasCommonInstanceNodeDto.

        节点组ID

        :param group_id: The group_id of this DasCommonInstanceNodeDto.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this DasCommonInstanceNodeDto.

        节点组名称

        :return: The group_name of this DasCommonInstanceNodeDto.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this DasCommonInstanceNodeDto.

        节点组名称

        :param group_name: The group_name of this DasCommonInstanceNodeDto.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, DasCommonInstanceNodeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
