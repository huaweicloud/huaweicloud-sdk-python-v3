# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointInput:

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
        'description': 'str',
        'type': 'EndpointType',
        'reserved_resource': 'ReservedResource',
        'ray_resource': 'RayResourceInput',
        'cap': 'CapRef',
        'log_config': 'LogConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'reserved_resource': 'reserved_resource',
        'ray_resource': 'ray_resource',
        'cap': 'cap',
        'log_config': 'log_config'
    }

    def __init__(self, name=None, description=None, type=None, reserved_resource=None, ray_resource=None, cap=None, log_config=None):
        r"""EndpointInput

        The model defined in huaweicloud sdk

        :param name: 一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        :param reserved_resource: 
        :type reserved_resource: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        :param ray_resource: 
        :type ray_resource: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInput`
        :param cap: 
        :type cap: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        :param log_config: 
        :type log_config: :class:`huaweicloudsdkdataartsfabric.v1.LogConfig`
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._reserved_resource = None
        self._ray_resource = None
        self._cap = None
        self._log_config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if reserved_resource is not None:
            self.reserved_resource = reserved_resource
        if ray_resource is not None:
            self.ray_resource = ray_resource
        if cap is not None:
            self.cap = cap
        if log_config is not None:
            self.log_config = log_config

    @property
    def name(self):
        r"""Gets the name of this EndpointInput.

        一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this EndpointInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EndpointInput.

        一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this EndpointInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EndpointInput.

        描述信息

        :return: The description of this EndpointInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EndpointInput.

        描述信息

        :param description: The description of this EndpointInput.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this EndpointInput.

        :return: The type of this EndpointInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EndpointInput.

        :param type: The type of this EndpointInput.
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        self._type = type

    @property
    def reserved_resource(self):
        r"""Gets the reserved_resource of this EndpointInput.

        :return: The reserved_resource of this EndpointInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        """
        return self._reserved_resource

    @reserved_resource.setter
    def reserved_resource(self, reserved_resource):
        r"""Sets the reserved_resource of this EndpointInput.

        :param reserved_resource: The reserved_resource of this EndpointInput.
        :type reserved_resource: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        """
        self._reserved_resource = reserved_resource

    @property
    def ray_resource(self):
        r"""Gets the ray_resource of this EndpointInput.

        :return: The ray_resource of this EndpointInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInput`
        """
        return self._ray_resource

    @ray_resource.setter
    def ray_resource(self, ray_resource):
        r"""Sets the ray_resource of this EndpointInput.

        :param ray_resource: The ray_resource of this EndpointInput.
        :type ray_resource: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInput`
        """
        self._ray_resource = ray_resource

    @property
    def cap(self):
        r"""Gets the cap of this EndpointInput.

        :return: The cap of this EndpointInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        """
        return self._cap

    @cap.setter
    def cap(self, cap):
        r"""Sets the cap of this EndpointInput.

        :param cap: The cap of this EndpointInput.
        :type cap: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        """
        self._cap = cap

    @property
    def log_config(self):
        r"""Gets the log_config of this EndpointInput.

        :return: The log_config of this EndpointInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.LogConfig`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this EndpointInput.

        :param log_config: The log_config of this EndpointInput.
        :type log_config: :class:`huaweicloudsdkdataartsfabric.v1.LogConfig`
        """
        self._log_config = log_config

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
        if not isinstance(other, EndpointInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
