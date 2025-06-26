# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DssPool:

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
        'type': 'str',
        'project_id': 'str',
        'availability_zone': 'str',
        'capacity': 'int',
        'status': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'project_id': 'project_id',
        'availability_zone': 'availability_zone',
        'capacity': 'capacity',
        'status': 'status',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, name=None, type=None, project_id=None, availability_zone=None, capacity=None, status=None, created_at=None):
        r"""DssPool

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 专属分布式存储池名称。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 专属分布式存储池ID。 **取值范围**： 不涉及。
        :type name: str
        :param type: **参数解释**： 专属分布式存储池的存储类型。 - SSD：超高IO专属分布式存储池。 **取值范围**： 不涉及。
        :type type: str
        :param project_id: **参数解释**： 项目ID。获取方法请参见[获取项目ID](dws_02_0011.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type project_id: str
        :param availability_zone: **参数解释**： 专属分布式存储池所属可用区。 **取值范围**： 不涉及。
        :type availability_zone: str
        :param capacity: **参数解释**： 申请的专属分布式存储容量，单位TB。 **取值范围**： 不涉及。
        :type capacity: int
        :param status: **参数解释**： 专属分布式存储池的状态。 **取值范围**： available：专属分布式存储池处于可用状态。 deploying：专属分布式存储池处于正在部署的过程中，不可使用。 extending：专属分布式存储池处于正在扩容的过程中，可使用。
        :type status: str
        :param created_at: **参数解释**： 专属分布式存储池的创建时间。 **取值范围**： 时间格式：UTC YYYY-MM-DDTHH:MM:SS
        :type created_at: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._project_id = None
        self._availability_zone = None
        self._capacity = None
        self._status = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.project_id = project_id
        self.availability_zone = availability_zone
        self.capacity = capacity
        self.status = status
        self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this DssPool.

        **参数解释**： 专属分布式存储池名称。 **取值范围**： 不涉及。

        :return: The id of this DssPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DssPool.

        **参数解释**： 专属分布式存储池名称。 **取值范围**： 不涉及。

        :param id: The id of this DssPool.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DssPool.

        **参数解释**： 专属分布式存储池ID。 **取值范围**： 不涉及。

        :return: The name of this DssPool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DssPool.

        **参数解释**： 专属分布式存储池ID。 **取值范围**： 不涉及。

        :param name: The name of this DssPool.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DssPool.

        **参数解释**： 专属分布式存储池的存储类型。 - SSD：超高IO专属分布式存储池。 **取值范围**： 不涉及。

        :return: The type of this DssPool.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DssPool.

        **参数解释**： 专属分布式存储池的存储类型。 - SSD：超高IO专属分布式存储池。 **取值范围**： 不涉及。

        :param type: The type of this DssPool.
        :type type: str
        """
        self._type = type

    @property
    def project_id(self):
        r"""Gets the project_id of this DssPool.

        **参数解释**： 项目ID。获取方法请参见[获取项目ID](dws_02_0011.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The project_id of this DssPool.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DssPool.

        **参数解释**： 项目ID。获取方法请参见[获取项目ID](dws_02_0011.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param project_id: The project_id of this DssPool.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this DssPool.

        **参数解释**： 专属分布式存储池所属可用区。 **取值范围**： 不涉及。

        :return: The availability_zone of this DssPool.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this DssPool.

        **参数解释**： 专属分布式存储池所属可用区。 **取值范围**： 不涉及。

        :param availability_zone: The availability_zone of this DssPool.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def capacity(self):
        r"""Gets the capacity of this DssPool.

        **参数解释**： 申请的专属分布式存储容量，单位TB。 **取值范围**： 不涉及。

        :return: The capacity of this DssPool.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this DssPool.

        **参数解释**： 申请的专属分布式存储容量，单位TB。 **取值范围**： 不涉及。

        :param capacity: The capacity of this DssPool.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def status(self):
        r"""Gets the status of this DssPool.

        **参数解释**： 专属分布式存储池的状态。 **取值范围**： available：专属分布式存储池处于可用状态。 deploying：专属分布式存储池处于正在部署的过程中，不可使用。 extending：专属分布式存储池处于正在扩容的过程中，可使用。

        :return: The status of this DssPool.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DssPool.

        **参数解释**： 专属分布式存储池的状态。 **取值范围**： available：专属分布式存储池处于可用状态。 deploying：专属分布式存储池处于正在部署的过程中，不可使用。 extending：专属分布式存储池处于正在扩容的过程中，可使用。

        :param status: The status of this DssPool.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this DssPool.

        **参数解释**： 专属分布式存储池的创建时间。 **取值范围**： 时间格式：UTC YYYY-MM-DDTHH:MM:SS

        :return: The created_at of this DssPool.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DssPool.

        **参数解释**： 专属分布式存储池的创建时间。 **取值范围**： 时间格式：UTC YYYY-MM-DDTHH:MM:SS

        :param created_at: The created_at of this DssPool.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, DssPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
