# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableZonesRespAvailableZones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sold_out': 'bool',
        'id': 'str',
        'code': 'str',
        'name': 'str',
        'port': 'str',
        'resource_availability': 'str',
        'default_az': 'bool',
        'remain_time': 'int',
        'ipv6_enable': 'bool'
    }

    attribute_map = {
        'sold_out': 'soldOut',
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'port': 'port',
        'resource_availability': 'resource_availability',
        'default_az': 'default_az',
        'remain_time': 'remain_time',
        'ipv6_enable': 'ipv6_enable'
    }

    def __init__(self, sold_out=None, id=None, code=None, name=None, port=None, resource_availability=None, default_az=None, remain_time=None, ipv6_enable=None):
        """ListAvailableZonesRespAvailableZones

        The model defined in huaweicloud sdk

        :param sold_out: 是否售罄。
        :type sold_out: bool
        :param id: 可用区ID。
        :type id: str
        :param code: 可用区编码。
        :type code: str
        :param name: 可用区名称。
        :type name: str
        :param port: 可用区端口号。
        :type port: str
        :param resource_availability: 分区上是否还有可用资源。
        :type resource_availability: str
        :param default_az: 是否为默认可用区。
        :type default_az: bool
        :param remain_time: 剩余时间。
        :type remain_time: int
        :param ipv6_enable: 是否支持IPv6。
        :type ipv6_enable: bool
        """
        
        

        self._sold_out = None
        self._id = None
        self._code = None
        self._name = None
        self._port = None
        self._resource_availability = None
        self._default_az = None
        self._remain_time = None
        self._ipv6_enable = None
        self.discriminator = None

        if sold_out is not None:
            self.sold_out = sold_out
        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if resource_availability is not None:
            self.resource_availability = resource_availability
        if default_az is not None:
            self.default_az = default_az
        if remain_time is not None:
            self.remain_time = remain_time
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable

    @property
    def sold_out(self):
        """Gets the sold_out of this ListAvailableZonesRespAvailableZones.

        是否售罄。

        :return: The sold_out of this ListAvailableZonesRespAvailableZones.
        :rtype: bool
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        """Sets the sold_out of this ListAvailableZonesRespAvailableZones.

        是否售罄。

        :param sold_out: The sold_out of this ListAvailableZonesRespAvailableZones.
        :type sold_out: bool
        """
        self._sold_out = sold_out

    @property
    def id(self):
        """Gets the id of this ListAvailableZonesRespAvailableZones.

        可用区ID。

        :return: The id of this ListAvailableZonesRespAvailableZones.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAvailableZonesRespAvailableZones.

        可用区ID。

        :param id: The id of this ListAvailableZonesRespAvailableZones.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        """Gets the code of this ListAvailableZonesRespAvailableZones.

        可用区编码。

        :return: The code of this ListAvailableZonesRespAvailableZones.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListAvailableZonesRespAvailableZones.

        可用区编码。

        :param code: The code of this ListAvailableZonesRespAvailableZones.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this ListAvailableZonesRespAvailableZones.

        可用区名称。

        :return: The name of this ListAvailableZonesRespAvailableZones.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAvailableZonesRespAvailableZones.

        可用区名称。

        :param name: The name of this ListAvailableZonesRespAvailableZones.
        :type name: str
        """
        self._name = name

    @property
    def port(self):
        """Gets the port of this ListAvailableZonesRespAvailableZones.

        可用区端口号。

        :return: The port of this ListAvailableZonesRespAvailableZones.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListAvailableZonesRespAvailableZones.

        可用区端口号。

        :param port: The port of this ListAvailableZonesRespAvailableZones.
        :type port: str
        """
        self._port = port

    @property
    def resource_availability(self):
        """Gets the resource_availability of this ListAvailableZonesRespAvailableZones.

        分区上是否还有可用资源。

        :return: The resource_availability of this ListAvailableZonesRespAvailableZones.
        :rtype: str
        """
        return self._resource_availability

    @resource_availability.setter
    def resource_availability(self, resource_availability):
        """Sets the resource_availability of this ListAvailableZonesRespAvailableZones.

        分区上是否还有可用资源。

        :param resource_availability: The resource_availability of this ListAvailableZonesRespAvailableZones.
        :type resource_availability: str
        """
        self._resource_availability = resource_availability

    @property
    def default_az(self):
        """Gets the default_az of this ListAvailableZonesRespAvailableZones.

        是否为默认可用区。

        :return: The default_az of this ListAvailableZonesRespAvailableZones.
        :rtype: bool
        """
        return self._default_az

    @default_az.setter
    def default_az(self, default_az):
        """Sets the default_az of this ListAvailableZonesRespAvailableZones.

        是否为默认可用区。

        :param default_az: The default_az of this ListAvailableZonesRespAvailableZones.
        :type default_az: bool
        """
        self._default_az = default_az

    @property
    def remain_time(self):
        """Gets the remain_time of this ListAvailableZonesRespAvailableZones.

        剩余时间。

        :return: The remain_time of this ListAvailableZonesRespAvailableZones.
        :rtype: int
        """
        return self._remain_time

    @remain_time.setter
    def remain_time(self, remain_time):
        """Sets the remain_time of this ListAvailableZonesRespAvailableZones.

        剩余时间。

        :param remain_time: The remain_time of this ListAvailableZonesRespAvailableZones.
        :type remain_time: int
        """
        self._remain_time = remain_time

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this ListAvailableZonesRespAvailableZones.

        是否支持IPv6。

        :return: The ipv6_enable of this ListAvailableZonesRespAvailableZones.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this ListAvailableZonesRespAvailableZones.

        是否支持IPv6。

        :param ipv6_enable: The ipv6_enable of this ListAvailableZonesRespAvailableZones.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

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
        if not isinstance(other, ListAvailableZonesRespAvailableZones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
