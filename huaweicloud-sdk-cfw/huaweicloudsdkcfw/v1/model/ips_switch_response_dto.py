# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsSwitchResponseDTO:

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
        'basic_defense_status': 'int',
        'virtual_patches_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'basic_defense_status': 'basic_defense_status',
        'virtual_patches_status': 'virtual_patches_status'
    }

    def __init__(self, id=None, basic_defense_status=None, virtual_patches_status=None):
        r"""IpsSwitchResponseDTO

        The model defined in huaweicloud sdk

        :param id: ips开关id，此处为互联网边界防护对象id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得
        :type id: str
        :param basic_defense_status: 基础防御状态，0表示关闭，1表示开启
        :type basic_defense_status: int
        :param virtual_patches_status: 虚拟补丁状态，0表示关闭，1表示开启
        :type virtual_patches_status: int
        """
        
        

        self._id = None
        self._basic_defense_status = None
        self._virtual_patches_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if basic_defense_status is not None:
            self.basic_defense_status = basic_defense_status
        if virtual_patches_status is not None:
            self.virtual_patches_status = virtual_patches_status

    @property
    def id(self):
        r"""Gets the id of this IpsSwitchResponseDTO.

        ips开关id，此处为互联网边界防护对象id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得

        :return: The id of this IpsSwitchResponseDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IpsSwitchResponseDTO.

        ips开关id，此处为互联网边界防护对象id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得

        :param id: The id of this IpsSwitchResponseDTO.
        :type id: str
        """
        self._id = id

    @property
    def basic_defense_status(self):
        r"""Gets the basic_defense_status of this IpsSwitchResponseDTO.

        基础防御状态，0表示关闭，1表示开启

        :return: The basic_defense_status of this IpsSwitchResponseDTO.
        :rtype: int
        """
        return self._basic_defense_status

    @basic_defense_status.setter
    def basic_defense_status(self, basic_defense_status):
        r"""Sets the basic_defense_status of this IpsSwitchResponseDTO.

        基础防御状态，0表示关闭，1表示开启

        :param basic_defense_status: The basic_defense_status of this IpsSwitchResponseDTO.
        :type basic_defense_status: int
        """
        self._basic_defense_status = basic_defense_status

    @property
    def virtual_patches_status(self):
        r"""Gets the virtual_patches_status of this IpsSwitchResponseDTO.

        虚拟补丁状态，0表示关闭，1表示开启

        :return: The virtual_patches_status of this IpsSwitchResponseDTO.
        :rtype: int
        """
        return self._virtual_patches_status

    @virtual_patches_status.setter
    def virtual_patches_status(self, virtual_patches_status):
        r"""Sets the virtual_patches_status of this IpsSwitchResponseDTO.

        虚拟补丁状态，0表示关闭，1表示开启

        :param virtual_patches_status: The virtual_patches_status of this IpsSwitchResponseDTO.
        :type virtual_patches_status: int
        """
        self._virtual_patches_status = virtual_patches_status

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
        if not isinstance(other, IpsSwitchResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
