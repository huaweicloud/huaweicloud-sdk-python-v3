# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Eips:

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
        'address': 'str',
        'bandwidth_size': 'int',
        'eip_charge_mode': 'str',
        'create_time': 'str',
        'attached_desktop_id': 'str',
        'attached_desktop_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'bandwidth_size': 'bandwidth_size',
        'eip_charge_mode': 'eip_charge_mode',
        'create_time': 'create_time',
        'attached_desktop_id': 'attached_desktop_id',
        'attached_desktop_name': 'attached_desktop_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, address=None, bandwidth_size=None, eip_charge_mode=None, create_time=None, attached_desktop_id=None, attached_desktop_name=None, enterprise_project_id=None):
        """Eips

        The model defined in huaweicloud sdk

        :param id: EIP的id。
        :type id: str
        :param address: Eip地址。
        :type address: str
        :param bandwidth_size: 带宽大小。
        :type bandwidth_size: int
        :param eip_charge_mode: traffic（按流量计费），bandwidth（按带宽计费）。
        :type eip_charge_mode: str
        :param create_time: 创建时间，格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type create_time: str
        :param attached_desktop_id: 绑定的桌面id。
        :type attached_desktop_id: str
        :param attached_desktop_name: 绑定的桌面名称。
        :type attached_desktop_name: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._address = None
        self._bandwidth_size = None
        self._eip_charge_mode = None
        self._create_time = None
        self._attached_desktop_id = None
        self._attached_desktop_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if eip_charge_mode is not None:
            self.eip_charge_mode = eip_charge_mode
        if create_time is not None:
            self.create_time = create_time
        if attached_desktop_id is not None:
            self.attached_desktop_id = attached_desktop_id
        if attached_desktop_name is not None:
            self.attached_desktop_name = attached_desktop_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this Eips.

        EIP的id。

        :return: The id of this Eips.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Eips.

        EIP的id。

        :param id: The id of this Eips.
        :type id: str
        """
        self._id = id

    @property
    def address(self):
        """Gets the address of this Eips.

        Eip地址。

        :return: The address of this Eips.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Eips.

        Eip地址。

        :param address: The address of this Eips.
        :type address: str
        """
        self._address = address

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this Eips.

        带宽大小。

        :return: The bandwidth_size of this Eips.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this Eips.

        带宽大小。

        :param bandwidth_size: The bandwidth_size of this Eips.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def eip_charge_mode(self):
        """Gets the eip_charge_mode of this Eips.

        traffic（按流量计费），bandwidth（按带宽计费）。

        :return: The eip_charge_mode of this Eips.
        :rtype: str
        """
        return self._eip_charge_mode

    @eip_charge_mode.setter
    def eip_charge_mode(self, eip_charge_mode):
        """Sets the eip_charge_mode of this Eips.

        traffic（按流量计费），bandwidth（按带宽计费）。

        :param eip_charge_mode: The eip_charge_mode of this Eips.
        :type eip_charge_mode: str
        """
        self._eip_charge_mode = eip_charge_mode

    @property
    def create_time(self):
        """Gets the create_time of this Eips.

        创建时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The create_time of this Eips.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Eips.

        创建时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param create_time: The create_time of this Eips.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def attached_desktop_id(self):
        """Gets the attached_desktop_id of this Eips.

        绑定的桌面id。

        :return: The attached_desktop_id of this Eips.
        :rtype: str
        """
        return self._attached_desktop_id

    @attached_desktop_id.setter
    def attached_desktop_id(self, attached_desktop_id):
        """Sets the attached_desktop_id of this Eips.

        绑定的桌面id。

        :param attached_desktop_id: The attached_desktop_id of this Eips.
        :type attached_desktop_id: str
        """
        self._attached_desktop_id = attached_desktop_id

    @property
    def attached_desktop_name(self):
        """Gets the attached_desktop_name of this Eips.

        绑定的桌面名称。

        :return: The attached_desktop_name of this Eips.
        :rtype: str
        """
        return self._attached_desktop_name

    @attached_desktop_name.setter
    def attached_desktop_name(self, attached_desktop_name):
        """Sets the attached_desktop_name of this Eips.

        绑定的桌面名称。

        :param attached_desktop_name: The attached_desktop_name of this Eips.
        :type attached_desktop_name: str
        """
        self._attached_desktop_name = attached_desktop_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Eips.

        企业项目ID

        :return: The enterprise_project_id of this Eips.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Eips.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this Eips.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, Eips):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
