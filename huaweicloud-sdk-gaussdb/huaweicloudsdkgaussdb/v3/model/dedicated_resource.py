# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DedicatedResource:

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
        'resource_name': 'str',
        'engine_name': 'str',
        'architecture': 'str',
        'status': 'str',
        'capacity': 'DedicatedResourceCapacity',
        'availability_zone': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'resource_name': 'resource_name',
        'engine_name': 'engine_name',
        'architecture': 'architecture',
        'status': 'status',
        'capacity': 'capacity',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, resource_name=None, engine_name=None, architecture=None, status=None, capacity=None, availability_zone=None):
        """DedicatedResource

        The model defined in huaweicloud sdk

        :param id: 专属资源池ID。
        :type id: str
        :param resource_name: 专属资源池名称
        :type resource_name: str
        :param engine_name: 数据库引擎名称
        :type engine_name: str
        :param architecture: CPU架构
        :type architecture: str
        :param status: 专属资源池状态
        :type status: str
        :param capacity: 
        :type capacity: :class:`huaweicloudsdkgaussdb.v3.DedicatedResourceCapacity`
        :param availability_zone: 专属资源池可用区信息。
        :type availability_zone: list[str]
        """
        
        

        self._id = None
        self._resource_name = None
        self._engine_name = None
        self._architecture = None
        self._status = None
        self._capacity = None
        self._availability_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_name is not None:
            self.resource_name = resource_name
        if engine_name is not None:
            self.engine_name = engine_name
        if architecture is not None:
            self.architecture = architecture
        if status is not None:
            self.status = status
        if capacity is not None:
            self.capacity = capacity
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def id(self):
        """Gets the id of this DedicatedResource.

        专属资源池ID。

        :return: The id of this DedicatedResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DedicatedResource.

        专属资源池ID。

        :param id: The id of this DedicatedResource.
        :type id: str
        """
        self._id = id

    @property
    def resource_name(self):
        """Gets the resource_name of this DedicatedResource.

        专属资源池名称

        :return: The resource_name of this DedicatedResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this DedicatedResource.

        专属资源池名称

        :param resource_name: The resource_name of this DedicatedResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def engine_name(self):
        """Gets the engine_name of this DedicatedResource.

        数据库引擎名称

        :return: The engine_name of this DedicatedResource.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this DedicatedResource.

        数据库引擎名称

        :param engine_name: The engine_name of this DedicatedResource.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def architecture(self):
        """Gets the architecture of this DedicatedResource.

        CPU架构

        :return: The architecture of this DedicatedResource.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this DedicatedResource.

        CPU架构

        :param architecture: The architecture of this DedicatedResource.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def status(self):
        """Gets the status of this DedicatedResource.

        专属资源池状态

        :return: The status of this DedicatedResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DedicatedResource.

        专属资源池状态

        :param status: The status of this DedicatedResource.
        :type status: str
        """
        self._status = status

    @property
    def capacity(self):
        """Gets the capacity of this DedicatedResource.


        :return: The capacity of this DedicatedResource.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DedicatedResourceCapacity`
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this DedicatedResource.


        :param capacity: The capacity of this DedicatedResource.
        :type capacity: :class:`huaweicloudsdkgaussdb.v3.DedicatedResourceCapacity`
        """
        self._capacity = capacity

    @property
    def availability_zone(self):
        """Gets the availability_zone of this DedicatedResource.

        专属资源池可用区信息。

        :return: The availability_zone of this DedicatedResource.
        :rtype: list[str]
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this DedicatedResource.

        专属资源池可用区信息。

        :param availability_zone: The availability_zone of this DedicatedResource.
        :type availability_zone: list[str]
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, DedicatedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
