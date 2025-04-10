# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBindingGeip:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_eip_id': 'str',
        'global_eip_segment_id': 'str',
        'status': 'str',
        'type': 'str',
        'error_message': 'str',
        'cidr': 'str',
        'address_family': 'str',
        'ie_vtep_ip': 'str',
        'created_time': 'str',
        'gcb_id': 'str'
    }

    attribute_map = {
        'global_eip_id': 'global_eip_id',
        'global_eip_segment_id': 'global_eip_segment_id',
        'status': 'status',
        'type': 'type',
        'error_message': 'error_message',
        'cidr': 'cidr',
        'address_family': 'address_family',
        'ie_vtep_ip': 'ie_vtep_ip',
        'created_time': 'created_time',
        'gcb_id': 'gcb_id'
    }

    def __init__(self, global_eip_id=None, global_eip_segment_id=None, status=None, type=None, error_message=None, cidr=None, address_family=None, ie_vtep_ip=None, created_time=None, gcb_id=None):
        r"""ListBindingGeip

        The model defined in huaweicloud sdk

        :param global_eip_id: geip的id
        :type global_eip_id: str
        :param global_eip_segment_id: 网段geip的id
        :type global_eip_segment_id: str
        :param status: geip的绑定状态
        :type status: str
        :param type: geip类型：IP_ADDRESS/IP_SEGMENT
        :type type: str
        :param error_message: geip绑定失败的原因
        :type error_message: str
        :param cidr: geip的地址ip/mask
        :type cidr: str
        :param address_family: geip的地址簇
        :type address_family: str
        :param ie_vtep_ip: CloudPond的集群vtepIp
        :type ie_vtep_ip: str
        :param created_time: geip绑定时间
        :type created_time: str
        :param gcb_id: 带宽包的id
        :type gcb_id: str
        """
        
        

        self._global_eip_id = None
        self._global_eip_segment_id = None
        self._status = None
        self._type = None
        self._error_message = None
        self._cidr = None
        self._address_family = None
        self._ie_vtep_ip = None
        self._created_time = None
        self._gcb_id = None
        self.discriminator = None

        if global_eip_id is not None:
            self.global_eip_id = global_eip_id
        if global_eip_segment_id is not None:
            self.global_eip_segment_id = global_eip_segment_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if error_message is not None:
            self.error_message = error_message
        if cidr is not None:
            self.cidr = cidr
        if address_family is not None:
            self.address_family = address_family
        if ie_vtep_ip is not None:
            self.ie_vtep_ip = ie_vtep_ip
        if created_time is not None:
            self.created_time = created_time
        if gcb_id is not None:
            self.gcb_id = gcb_id

    @property
    def global_eip_id(self):
        r"""Gets the global_eip_id of this ListBindingGeip.

        geip的id

        :return: The global_eip_id of this ListBindingGeip.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        r"""Sets the global_eip_id of this ListBindingGeip.

        geip的id

        :param global_eip_id: The global_eip_id of this ListBindingGeip.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def global_eip_segment_id(self):
        r"""Gets the global_eip_segment_id of this ListBindingGeip.

        网段geip的id

        :return: The global_eip_segment_id of this ListBindingGeip.
        :rtype: str
        """
        return self._global_eip_segment_id

    @global_eip_segment_id.setter
    def global_eip_segment_id(self, global_eip_segment_id):
        r"""Sets the global_eip_segment_id of this ListBindingGeip.

        网段geip的id

        :param global_eip_segment_id: The global_eip_segment_id of this ListBindingGeip.
        :type global_eip_segment_id: str
        """
        self._global_eip_segment_id = global_eip_segment_id

    @property
    def status(self):
        r"""Gets the status of this ListBindingGeip.

        geip的绑定状态

        :return: The status of this ListBindingGeip.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListBindingGeip.

        geip的绑定状态

        :param status: The status of this ListBindingGeip.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListBindingGeip.

        geip类型：IP_ADDRESS/IP_SEGMENT

        :return: The type of this ListBindingGeip.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListBindingGeip.

        geip类型：IP_ADDRESS/IP_SEGMENT

        :param type: The type of this ListBindingGeip.
        :type type: str
        """
        self._type = type

    @property
    def error_message(self):
        r"""Gets the error_message of this ListBindingGeip.

        geip绑定失败的原因

        :return: The error_message of this ListBindingGeip.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ListBindingGeip.

        geip绑定失败的原因

        :param error_message: The error_message of this ListBindingGeip.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def cidr(self):
        r"""Gets the cidr of this ListBindingGeip.

        geip的地址ip/mask

        :return: The cidr of this ListBindingGeip.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this ListBindingGeip.

        geip的地址ip/mask

        :param cidr: The cidr of this ListBindingGeip.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def address_family(self):
        r"""Gets the address_family of this ListBindingGeip.

        geip的地址簇

        :return: The address_family of this ListBindingGeip.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        r"""Sets the address_family of this ListBindingGeip.

        geip的地址簇

        :param address_family: The address_family of this ListBindingGeip.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def ie_vtep_ip(self):
        r"""Gets the ie_vtep_ip of this ListBindingGeip.

        CloudPond的集群vtepIp

        :return: The ie_vtep_ip of this ListBindingGeip.
        :rtype: str
        """
        return self._ie_vtep_ip

    @ie_vtep_ip.setter
    def ie_vtep_ip(self, ie_vtep_ip):
        r"""Sets the ie_vtep_ip of this ListBindingGeip.

        CloudPond的集群vtepIp

        :param ie_vtep_ip: The ie_vtep_ip of this ListBindingGeip.
        :type ie_vtep_ip: str
        """
        self._ie_vtep_ip = ie_vtep_ip

    @property
    def created_time(self):
        r"""Gets the created_time of this ListBindingGeip.

        geip绑定时间

        :return: The created_time of this ListBindingGeip.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ListBindingGeip.

        geip绑定时间

        :param created_time: The created_time of this ListBindingGeip.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def gcb_id(self):
        r"""Gets the gcb_id of this ListBindingGeip.

        带宽包的id

        :return: The gcb_id of this ListBindingGeip.
        :rtype: str
        """
        return self._gcb_id

    @gcb_id.setter
    def gcb_id(self, gcb_id):
        r"""Sets the gcb_id of this ListBindingGeip.

        带宽包的id

        :param gcb_id: The gcb_id of this ListBindingGeip.
        :type gcb_id: str
        """
        self._gcb_id = gcb_id

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
        if not isinstance(other, ListBindingGeip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
