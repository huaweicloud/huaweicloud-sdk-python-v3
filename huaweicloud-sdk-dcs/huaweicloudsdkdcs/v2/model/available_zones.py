# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableZones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'port': 'str',
        'name': 'str',
        'id': 'str',
        'resource_availability': 'str'
    }

    attribute_map = {
        'code': 'code',
        'port': 'port',
        'name': 'name',
        'id': 'id',
        'resource_availability': 'resource_availability'
    }

    def __init__(self, code=None, port=None, name=None, id=None, resource_availability=None):
        r"""AvailableZones

        The model defined in huaweicloud sdk

        :param code: 可用区编码。
        :type code: str
        :param port: 可用区端口号。
        :type port: str
        :param name: 可用区名称。
        :type name: str
        :param id: 可用区ID。
        :type id: str
        :param resource_availability: 分区上是否还有可用资源。 - true：还有资源。 - false：资源已售罄。 
        :type resource_availability: str
        """
        
        

        self._code = None
        self._port = None
        self._name = None
        self._id = None
        self._resource_availability = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if port is not None:
            self.port = port
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if resource_availability is not None:
            self.resource_availability = resource_availability

    @property
    def code(self):
        r"""Gets the code of this AvailableZones.

        可用区编码。

        :return: The code of this AvailableZones.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AvailableZones.

        可用区编码。

        :param code: The code of this AvailableZones.
        :type code: str
        """
        self._code = code

    @property
    def port(self):
        r"""Gets the port of this AvailableZones.

        可用区端口号。

        :return: The port of this AvailableZones.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AvailableZones.

        可用区端口号。

        :param port: The port of this AvailableZones.
        :type port: str
        """
        self._port = port

    @property
    def name(self):
        r"""Gets the name of this AvailableZones.

        可用区名称。

        :return: The name of this AvailableZones.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AvailableZones.

        可用区名称。

        :param name: The name of this AvailableZones.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this AvailableZones.

        可用区ID。

        :return: The id of this AvailableZones.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AvailableZones.

        可用区ID。

        :param id: The id of this AvailableZones.
        :type id: str
        """
        self._id = id

    @property
    def resource_availability(self):
        r"""Gets the resource_availability of this AvailableZones.

        分区上是否还有可用资源。 - true：还有资源。 - false：资源已售罄。 

        :return: The resource_availability of this AvailableZones.
        :rtype: str
        """
        return self._resource_availability

    @resource_availability.setter
    def resource_availability(self, resource_availability):
        r"""Sets the resource_availability of this AvailableZones.

        分区上是否还有可用资源。 - true：还有资源。 - false：资源已售罄。 

        :param resource_availability: The resource_availability of this AvailableZones.
        :type resource_availability: str
        """
        self._resource_availability = resource_availability

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
        if not isinstance(other, AvailableZones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
