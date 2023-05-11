# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDedicatedResourceResult:

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
        'availability_zone': 'str',
        'architecture': 'str',
        'capacity': 'DedicatedResourceCapacity',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_name': 'resource_name',
        'engine_name': 'engine_name',
        'availability_zone': 'availability_zone',
        'architecture': 'architecture',
        'capacity': 'capacity',
        'status': 'status'
    }

    def __init__(self, id=None, resource_name=None, engine_name=None, availability_zone=None, architecture=None, capacity=None, status=None):
        """ListDedicatedResourceResult

        The model defined in huaweicloud sdk

        :param id: 专属资源ID。
        :type id: str
        :param resource_name: 专属资源的名称。
        :type resource_name: str
        :param engine_name: 引擎名称。
        :type engine_name: str
        :param availability_zone: 可用区信息。
        :type availability_zone: str
        :param architecture: 专属资源的计算架构。
        :type architecture: str
        :param capacity: 
        :type capacity: :class:`huaweicloudsdkgaussdbfornosql.v3.DedicatedResourceCapacity`
        :param status: 专属资源的状态信息。
        :type status: str
        """
        
        

        self._id = None
        self._resource_name = None
        self._engine_name = None
        self._availability_zone = None
        self._architecture = None
        self._capacity = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.resource_name = resource_name
        self.engine_name = engine_name
        self.availability_zone = availability_zone
        self.architecture = architecture
        self.capacity = capacity
        self.status = status

    @property
    def id(self):
        """Gets the id of this ListDedicatedResourceResult.

        专属资源ID。

        :return: The id of this ListDedicatedResourceResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListDedicatedResourceResult.

        专属资源ID。

        :param id: The id of this ListDedicatedResourceResult.
        :type id: str
        """
        self._id = id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListDedicatedResourceResult.

        专属资源的名称。

        :return: The resource_name of this ListDedicatedResourceResult.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListDedicatedResourceResult.

        专属资源的名称。

        :param resource_name: The resource_name of this ListDedicatedResourceResult.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def engine_name(self):
        """Gets the engine_name of this ListDedicatedResourceResult.

        引擎名称。

        :return: The engine_name of this ListDedicatedResourceResult.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this ListDedicatedResourceResult.

        引擎名称。

        :param engine_name: The engine_name of this ListDedicatedResourceResult.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListDedicatedResourceResult.

        可用区信息。

        :return: The availability_zone of this ListDedicatedResourceResult.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListDedicatedResourceResult.

        可用区信息。

        :param availability_zone: The availability_zone of this ListDedicatedResourceResult.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def architecture(self):
        """Gets the architecture of this ListDedicatedResourceResult.

        专属资源的计算架构。

        :return: The architecture of this ListDedicatedResourceResult.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ListDedicatedResourceResult.

        专属资源的计算架构。

        :param architecture: The architecture of this ListDedicatedResourceResult.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def capacity(self):
        """Gets the capacity of this ListDedicatedResourceResult.

        :return: The capacity of this ListDedicatedResourceResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DedicatedResourceCapacity`
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ListDedicatedResourceResult.

        :param capacity: The capacity of this ListDedicatedResourceResult.
        :type capacity: :class:`huaweicloudsdkgaussdbfornosql.v3.DedicatedResourceCapacity`
        """
        self._capacity = capacity

    @property
    def status(self):
        """Gets the status of this ListDedicatedResourceResult.

        专属资源的状态信息。

        :return: The status of this ListDedicatedResourceResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDedicatedResourceResult.

        专属资源的状态信息。

        :param status: The status of this ListDedicatedResourceResult.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListDedicatedResourceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
