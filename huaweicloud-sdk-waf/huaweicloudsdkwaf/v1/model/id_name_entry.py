# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdNameEntry:

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
        'service_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'service_ip': 'service_ip'
    }

    def __init__(self, id=None, name=None, service_ip=None):
        r"""IdNameEntry

        The model defined in huaweicloud sdk

        :param id: 资源id
        :type id: str
        :param name: 资源名称
        :type name: str
        :param service_ip: 引擎实例IP
        :type service_ip: str
        """
        
        

        self._id = None
        self._name = None
        self._service_ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if service_ip is not None:
            self.service_ip = service_ip

    @property
    def id(self):
        r"""Gets the id of this IdNameEntry.

        资源id

        :return: The id of this IdNameEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IdNameEntry.

        资源id

        :param id: The id of this IdNameEntry.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this IdNameEntry.

        资源名称

        :return: The name of this IdNameEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IdNameEntry.

        资源名称

        :param name: The name of this IdNameEntry.
        :type name: str
        """
        self._name = name

    @property
    def service_ip(self):
        r"""Gets the service_ip of this IdNameEntry.

        引擎实例IP

        :return: The service_ip of this IdNameEntry.
        :rtype: str
        """
        return self._service_ip

    @service_ip.setter
    def service_ip(self, service_ip):
        r"""Sets the service_ip of this IdNameEntry.

        引擎实例IP

        :param service_ip: The service_ip of this IdNameEntry.
        :type service_ip: str
        """
        self._service_ip = service_ip

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
        if not isinstance(other, IdNameEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
