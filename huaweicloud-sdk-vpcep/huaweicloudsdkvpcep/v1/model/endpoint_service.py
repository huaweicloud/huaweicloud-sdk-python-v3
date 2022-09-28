# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointService:

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
        'owner': 'str',
        'service_name': 'str',
        'service_type': 'str',
        'created_at': 'str',
        'is_charge': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'service_name': 'service_name',
        'service_type': 'service_type',
        'created_at': 'created_at',
        'is_charge': 'is_charge'
    }

    def __init__(self, id=None, owner=None, service_name=None, service_type=None, created_at=None, is_charge=None):
        """EndpointService

        The model defined in huaweicloud sdk

        :param id: 公共终端节点服务的ID，唯一标识。
        :type id: str
        :param owner: 终端节点服务的所有者。
        :type owner: str
        :param service_name: 公共终端节点服务的名称。
        :type service_name: str
        :param service_type: 终端节点服务类型。 ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。
        :type service_type: str
        :param created_at: 终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYYMM-DDTHH:MM:SSZ
        :type created_at: str
        :param is_charge: 连接该终端节点服务的终端节点是否计费。 ● true：计费 ● false：不计费
        :type is_charge: bool
        """
        
        

        self._id = None
        self._owner = None
        self._service_name = None
        self._service_type = None
        self._created_at = None
        self._is_charge = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if service_name is not None:
            self.service_name = service_name
        if service_type is not None:
            self.service_type = service_type
        if created_at is not None:
            self.created_at = created_at
        if is_charge is not None:
            self.is_charge = is_charge

    @property
    def id(self):
        """Gets the id of this EndpointService.

        公共终端节点服务的ID，唯一标识。

        :return: The id of this EndpointService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointService.

        公共终端节点服务的ID，唯一标识。

        :param id: The id of this EndpointService.
        :type id: str
        """
        self._id = id

    @property
    def owner(self):
        """Gets the owner of this EndpointService.

        终端节点服务的所有者。

        :return: The owner of this EndpointService.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this EndpointService.

        终端节点服务的所有者。

        :param owner: The owner of this EndpointService.
        :type owner: str
        """
        self._owner = owner

    @property
    def service_name(self):
        """Gets the service_name of this EndpointService.

        公共终端节点服务的名称。

        :return: The service_name of this EndpointService.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this EndpointService.

        公共终端节点服务的名称。

        :param service_name: The service_name of this EndpointService.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def service_type(self):
        """Gets the service_type of this EndpointService.

        终端节点服务类型。 ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :return: The service_type of this EndpointService.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this EndpointService.

        终端节点服务类型。 ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :param service_type: The service_type of this EndpointService.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def created_at(self):
        """Gets the created_at of this EndpointService.

        终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYYMM-DDTHH:MM:SSZ

        :return: The created_at of this EndpointService.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EndpointService.

        终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYYMM-DDTHH:MM:SSZ

        :param created_at: The created_at of this EndpointService.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def is_charge(self):
        """Gets the is_charge of this EndpointService.

        连接该终端节点服务的终端节点是否计费。 ● true：计费 ● false：不计费

        :return: The is_charge of this EndpointService.
        :rtype: bool
        """
        return self._is_charge

    @is_charge.setter
    def is_charge(self, is_charge):
        """Sets the is_charge of this EndpointService.

        连接该终端节点服务的终端节点是否计费。 ● true：计费 ● false：不计费

        :param is_charge: The is_charge of this EndpointService.
        :type is_charge: bool
        """
        self._is_charge = is_charge

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
        if not isinstance(other, EndpointService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
