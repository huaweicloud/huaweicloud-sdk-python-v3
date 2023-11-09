# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVgwRequestBodyContent:

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
        'local_subnets': 'list[str]',
        'master_eip_id': 'str',
        'slave_eip_id': 'str',
        'eip_id_1': 'str',
        'eip_id_2': 'str'
    }

    attribute_map = {
        'name': 'name',
        'local_subnets': 'local_subnets',
        'master_eip_id': 'master_eip_id',
        'slave_eip_id': 'slave_eip_id',
        'eip_id_1': 'eip_id_1',
        'eip_id_2': 'eip_id_2'
    }

    def __init__(self, name=None, local_subnets=None, master_eip_id=None, slave_eip_id=None, eip_id_1=None, eip_id_2=None):
        """UpdateVgwRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: 网关名称
        :type name: str
        :param local_subnets: 本端子网
        :type local_subnets: list[str]
        :param master_eip_id: 主eip的ID。用于给VPN网关绑定新的主EIP，需要先解绑当前的主EIP
        :type master_eip_id: str
        :param slave_eip_id: 备eip的ID。用于给VPN网关绑定新的备EIP，需要先解绑当前的备EIP
        :type slave_eip_id: str
        :param eip_id_1: 主eip的ID。用于给VPN网关绑定新的主EIP，需要先解绑当前的主EIP
        :type eip_id_1: str
        :param eip_id_2: 备eip的ID。用于给VPN网关绑定新的备EIP，需要先解绑当前的备EIP
        :type eip_id_2: str
        """
        
        

        self._name = None
        self._local_subnets = None
        self._master_eip_id = None
        self._slave_eip_id = None
        self._eip_id_1 = None
        self._eip_id_2 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if local_subnets is not None:
            self.local_subnets = local_subnets
        if master_eip_id is not None:
            self.master_eip_id = master_eip_id
        if slave_eip_id is not None:
            self.slave_eip_id = slave_eip_id
        if eip_id_1 is not None:
            self.eip_id_1 = eip_id_1
        if eip_id_2 is not None:
            self.eip_id_2 = eip_id_2

    @property
    def name(self):
        """Gets the name of this UpdateVgwRequestBodyContent.

        网关名称

        :return: The name of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVgwRequestBodyContent.

        网关名称

        :param name: The name of this UpdateVgwRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def local_subnets(self):
        """Gets the local_subnets of this UpdateVgwRequestBodyContent.

        本端子网

        :return: The local_subnets of this UpdateVgwRequestBodyContent.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        """Sets the local_subnets of this UpdateVgwRequestBodyContent.

        本端子网

        :param local_subnets: The local_subnets of this UpdateVgwRequestBodyContent.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def master_eip_id(self):
        """Gets the master_eip_id of this UpdateVgwRequestBodyContent.

        主eip的ID。用于给VPN网关绑定新的主EIP，需要先解绑当前的主EIP

        :return: The master_eip_id of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._master_eip_id

    @master_eip_id.setter
    def master_eip_id(self, master_eip_id):
        """Sets the master_eip_id of this UpdateVgwRequestBodyContent.

        主eip的ID。用于给VPN网关绑定新的主EIP，需要先解绑当前的主EIP

        :param master_eip_id: The master_eip_id of this UpdateVgwRequestBodyContent.
        :type master_eip_id: str
        """
        self._master_eip_id = master_eip_id

    @property
    def slave_eip_id(self):
        """Gets the slave_eip_id of this UpdateVgwRequestBodyContent.

        备eip的ID。用于给VPN网关绑定新的备EIP，需要先解绑当前的备EIP

        :return: The slave_eip_id of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._slave_eip_id

    @slave_eip_id.setter
    def slave_eip_id(self, slave_eip_id):
        """Sets the slave_eip_id of this UpdateVgwRequestBodyContent.

        备eip的ID。用于给VPN网关绑定新的备EIP，需要先解绑当前的备EIP

        :param slave_eip_id: The slave_eip_id of this UpdateVgwRequestBodyContent.
        :type slave_eip_id: str
        """
        self._slave_eip_id = slave_eip_id

    @property
    def eip_id_1(self):
        """Gets the eip_id_1 of this UpdateVgwRequestBodyContent.

        主eip的ID。用于给VPN网关绑定新的主EIP，需要先解绑当前的主EIP

        :return: The eip_id_1 of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._eip_id_1

    @eip_id_1.setter
    def eip_id_1(self, eip_id_1):
        """Sets the eip_id_1 of this UpdateVgwRequestBodyContent.

        主eip的ID。用于给VPN网关绑定新的主EIP，需要先解绑当前的主EIP

        :param eip_id_1: The eip_id_1 of this UpdateVgwRequestBodyContent.
        :type eip_id_1: str
        """
        self._eip_id_1 = eip_id_1

    @property
    def eip_id_2(self):
        """Gets the eip_id_2 of this UpdateVgwRequestBodyContent.

        备eip的ID。用于给VPN网关绑定新的备EIP，需要先解绑当前的备EIP

        :return: The eip_id_2 of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._eip_id_2

    @eip_id_2.setter
    def eip_id_2(self, eip_id_2):
        """Sets the eip_id_2 of this UpdateVgwRequestBodyContent.

        备eip的ID。用于给VPN网关绑定新的备EIP，需要先解绑当前的备EIP

        :param eip_id_2: The eip_id_2 of this UpdateVgwRequestBodyContent.
        :type eip_id_2: str
        """
        self._eip_id_2 = eip_id_2

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
        if not isinstance(other, UpdateVgwRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
