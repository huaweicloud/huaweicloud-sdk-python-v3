# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubnetResponseObject:

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
        'status': 'str',
        'ipv6_enable': 'bool',
        'neutron_subnet_id_v6': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'ipv6_enable': 'ipv6_enable',
        'neutron_subnet_id_v6': 'neutron_subnet_id_v6'
    }

    def __init__(self, id=None, status=None, ipv6_enable=None, neutron_subnet_id_v6=None):
        r"""UpdateSubnetResponseObject

        The model defined in huaweicloud sdk

        :param id: 子网ID
        :type id: str
        :param status: 子网的状态  取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障
        :type status: str
        :param ipv6_enable: 是否开启IPv6
        :type ipv6_enable: bool
        :param neutron_subnet_id_v6: 对应IPv6子网（OpenStack Neutron接口）id，如果子网为IPv4子网，则不返回此参数。 
        :type neutron_subnet_id_v6: str
        """
        
        

        self._id = None
        self._status = None
        self._ipv6_enable = None
        self._neutron_subnet_id_v6 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if neutron_subnet_id_v6 is not None:
            self.neutron_subnet_id_v6 = neutron_subnet_id_v6

    @property
    def id(self):
        r"""Gets the id of this UpdateSubnetResponseObject.

        子网ID

        :return: The id of this UpdateSubnetResponseObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSubnetResponseObject.

        子网ID

        :param id: The id of this UpdateSubnetResponseObject.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this UpdateSubnetResponseObject.

        子网的状态  取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障

        :return: The status of this UpdateSubnetResponseObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateSubnetResponseObject.

        子网的状态  取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障

        :param status: The status of this UpdateSubnetResponseObject.
        :type status: str
        """
        self._status = status

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this UpdateSubnetResponseObject.

        是否开启IPv6

        :return: The ipv6_enable of this UpdateSubnetResponseObject.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this UpdateSubnetResponseObject.

        是否开启IPv6

        :param ipv6_enable: The ipv6_enable of this UpdateSubnetResponseObject.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def neutron_subnet_id_v6(self):
        r"""Gets the neutron_subnet_id_v6 of this UpdateSubnetResponseObject.

        对应IPv6子网（OpenStack Neutron接口）id，如果子网为IPv4子网，则不返回此参数。 

        :return: The neutron_subnet_id_v6 of this UpdateSubnetResponseObject.
        :rtype: str
        """
        return self._neutron_subnet_id_v6

    @neutron_subnet_id_v6.setter
    def neutron_subnet_id_v6(self, neutron_subnet_id_v6):
        r"""Sets the neutron_subnet_id_v6 of this UpdateSubnetResponseObject.

        对应IPv6子网（OpenStack Neutron接口）id，如果子网为IPv4子网，则不返回此参数。 

        :param neutron_subnet_id_v6: The neutron_subnet_id_v6 of this UpdateSubnetResponseObject.
        :type neutron_subnet_id_v6: str
        """
        self._neutron_subnet_id_v6 = neutron_subnet_id_v6

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
        if not isinstance(other, UpdateSubnetResponseObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
