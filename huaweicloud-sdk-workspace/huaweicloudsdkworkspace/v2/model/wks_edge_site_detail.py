# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WksEdgeSiteDetail:

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
        'description': 'str',
        'availability_zone_id': 'str',
        'address': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'cpu_usage_rate': 'float',
        'memory_usage_rate': 'float',
        'capacity_usage_rate': 'float',
        'site_info': 'SimpleSiteInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'availability_zone_id': 'availability_zone_id',
        'address': 'address',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cpu_usage_rate': 'cpu_usage_rate',
        'memory_usage_rate': 'memory_usage_rate',
        'capacity_usage_rate': 'capacity_usage_rate',
        'site_info': 'site_info'
    }

    def __init__(self, id=None, name=None, description=None, availability_zone_id=None, address=None, status=None, created_at=None, updated_at=None, cpu_usage_rate=None, memory_usage_rate=None, capacity_usage_rate=None, site_info=None):
        r"""WksEdgeSiteDetail

        The model defined in huaweicloud sdk

        :param id: 边缘小站id。
        :type id: str
        :param name: 边缘小站名称。
        :type name: str
        :param description: 边缘小站描述。
        :type description: str
        :param availability_zone_id: 边缘小站的可用区ID。
        :type availability_zone_id: str
        :param address: 部署位置。
        :type address: str
        :param status: 边缘小站的部署状态。 - initial：待部署。 - deploying：部署中。 - available：可用。 - unavailable：不可用。
        :type status: str
        :param created_at: 边缘小站创建时间。
        :type created_at: str
        :param updated_at: 边缘小站更新时间。
        :type updated_at: str
        :param cpu_usage_rate: cpu使用率。
        :type cpu_usage_rate: float
        :param memory_usage_rate: 内存使用率。
        :type memory_usage_rate: float
        :param capacity_usage_rate: 存储使用率。
        :type capacity_usage_rate: float
        :param site_info: 
        :type site_info: :class:`huaweicloudsdkworkspace.v2.SimpleSiteInfo`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._availability_zone_id = None
        self._address = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._cpu_usage_rate = None
        self._memory_usage_rate = None
        self._capacity_usage_rate = None
        self._site_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if cpu_usage_rate is not None:
            self.cpu_usage_rate = cpu_usage_rate
        if memory_usage_rate is not None:
            self.memory_usage_rate = memory_usage_rate
        if capacity_usage_rate is not None:
            self.capacity_usage_rate = capacity_usage_rate
        if site_info is not None:
            self.site_info = site_info

    @property
    def id(self):
        r"""Gets the id of this WksEdgeSiteDetail.

        边缘小站id。

        :return: The id of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WksEdgeSiteDetail.

        边缘小站id。

        :param id: The id of this WksEdgeSiteDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this WksEdgeSiteDetail.

        边缘小站名称。

        :return: The name of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WksEdgeSiteDetail.

        边缘小站名称。

        :param name: The name of this WksEdgeSiteDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this WksEdgeSiteDetail.

        边缘小站描述。

        :return: The description of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WksEdgeSiteDetail.

        边缘小站描述。

        :param description: The description of this WksEdgeSiteDetail.
        :type description: str
        """
        self._description = description

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this WksEdgeSiteDetail.

        边缘小站的可用区ID。

        :return: The availability_zone_id of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this WksEdgeSiteDetail.

        边缘小站的可用区ID。

        :param availability_zone_id: The availability_zone_id of this WksEdgeSiteDetail.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def address(self):
        r"""Gets the address of this WksEdgeSiteDetail.

        部署位置。

        :return: The address of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this WksEdgeSiteDetail.

        部署位置。

        :param address: The address of this WksEdgeSiteDetail.
        :type address: str
        """
        self._address = address

    @property
    def status(self):
        r"""Gets the status of this WksEdgeSiteDetail.

        边缘小站的部署状态。 - initial：待部署。 - deploying：部署中。 - available：可用。 - unavailable：不可用。

        :return: The status of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WksEdgeSiteDetail.

        边缘小站的部署状态。 - initial：待部署。 - deploying：部署中。 - available：可用。 - unavailable：不可用。

        :param status: The status of this WksEdgeSiteDetail.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this WksEdgeSiteDetail.

        边缘小站创建时间。

        :return: The created_at of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this WksEdgeSiteDetail.

        边缘小站创建时间。

        :param created_at: The created_at of this WksEdgeSiteDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this WksEdgeSiteDetail.

        边缘小站更新时间。

        :return: The updated_at of this WksEdgeSiteDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this WksEdgeSiteDetail.

        边缘小站更新时间。

        :param updated_at: The updated_at of this WksEdgeSiteDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def cpu_usage_rate(self):
        r"""Gets the cpu_usage_rate of this WksEdgeSiteDetail.

        cpu使用率。

        :return: The cpu_usage_rate of this WksEdgeSiteDetail.
        :rtype: float
        """
        return self._cpu_usage_rate

    @cpu_usage_rate.setter
    def cpu_usage_rate(self, cpu_usage_rate):
        r"""Sets the cpu_usage_rate of this WksEdgeSiteDetail.

        cpu使用率。

        :param cpu_usage_rate: The cpu_usage_rate of this WksEdgeSiteDetail.
        :type cpu_usage_rate: float
        """
        self._cpu_usage_rate = cpu_usage_rate

    @property
    def memory_usage_rate(self):
        r"""Gets the memory_usage_rate of this WksEdgeSiteDetail.

        内存使用率。

        :return: The memory_usage_rate of this WksEdgeSiteDetail.
        :rtype: float
        """
        return self._memory_usage_rate

    @memory_usage_rate.setter
    def memory_usage_rate(self, memory_usage_rate):
        r"""Sets the memory_usage_rate of this WksEdgeSiteDetail.

        内存使用率。

        :param memory_usage_rate: The memory_usage_rate of this WksEdgeSiteDetail.
        :type memory_usage_rate: float
        """
        self._memory_usage_rate = memory_usage_rate

    @property
    def capacity_usage_rate(self):
        r"""Gets the capacity_usage_rate of this WksEdgeSiteDetail.

        存储使用率。

        :return: The capacity_usage_rate of this WksEdgeSiteDetail.
        :rtype: float
        """
        return self._capacity_usage_rate

    @capacity_usage_rate.setter
    def capacity_usage_rate(self, capacity_usage_rate):
        r"""Sets the capacity_usage_rate of this WksEdgeSiteDetail.

        存储使用率。

        :param capacity_usage_rate: The capacity_usage_rate of this WksEdgeSiteDetail.
        :type capacity_usage_rate: float
        """
        self._capacity_usage_rate = capacity_usage_rate

    @property
    def site_info(self):
        r"""Gets the site_info of this WksEdgeSiteDetail.

        :return: The site_info of this WksEdgeSiteDetail.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SimpleSiteInfo`
        """
        return self._site_info

    @site_info.setter
    def site_info(self, site_info):
        r"""Sets the site_info of this WksEdgeSiteDetail.

        :param site_info: The site_info of this WksEdgeSiteDetail.
        :type site_info: :class:`huaweicloudsdkworkspace.v2.SimpleSiteInfo`
        """
        self._site_info = site_info

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
        if not isinstance(other, WksEdgeSiteDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
