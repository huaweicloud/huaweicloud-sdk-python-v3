# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unit': 'str',
        'resource_type_name': 'str',
        'source_resource_spec_code': 'str',
        'resource_spec_code': 'object',
        'source_type': 'str',
        'used_percent': 'float',
        'quota': 'float',
        'used': 'float',
        'free': 'float'
    }

    attribute_map = {
        'unit': 'unit',
        'resource_type_name': 'resource_type_name',
        'source_resource_spec_code': 'source_resource_spec_code',
        'resource_spec_code': 'resource_spec_code',
        'source_type': 'source_type',
        'used_percent': 'used_percent',
        'quota': 'quota',
        'used': 'used',
        'free': 'free'
    }

    def __init__(self, unit=None, resource_type_name=None, source_resource_spec_code=None, resource_spec_code=None, source_type=None, used_percent=None, quota=None, used=None, free=None):
        r"""ResourceUsage

        The model defined in huaweicloud sdk

        :param unit: 使用量单位，OPS 次，MB 流量体积MB，GB 流量体积GB
        :type unit: str
        :param resource_type_name: 资源类型名称
        :type resource_type_name: str
        :param source_resource_spec_code: 源资源规格编码
        :type source_resource_spec_code: str
        :param resource_spec_code: 源资源规格编码
        :type resource_spec_code: object
        :param source_type: 源资源类型编码
        :type source_type: str
        :param used_percent: 用量百分比
        :type used_percent: float
        :param quota: 配额总量
        :type quota: float
        :param used: 已用量
        :type used: float
        :param free: 剩余量
        :type free: float
        """
        
        

        self._unit = None
        self._resource_type_name = None
        self._source_resource_spec_code = None
        self._resource_spec_code = None
        self._source_type = None
        self._used_percent = None
        self._quota = None
        self._used = None
        self._free = None
        self.discriminator = None

        if unit is not None:
            self.unit = unit
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if source_resource_spec_code is not None:
            self.source_resource_spec_code = source_resource_spec_code
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if source_type is not None:
            self.source_type = source_type
        if used_percent is not None:
            self.used_percent = used_percent
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if free is not None:
            self.free = free

    @property
    def unit(self):
        r"""Gets the unit of this ResourceUsage.

        使用量单位，OPS 次，MB 流量体积MB，GB 流量体积GB

        :return: The unit of this ResourceUsage.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ResourceUsage.

        使用量单位，OPS 次，MB 流量体积MB，GB 流量体积GB

        :param unit: The unit of this ResourceUsage.
        :type unit: str
        """
        self._unit = unit

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this ResourceUsage.

        资源类型名称

        :return: The resource_type_name of this ResourceUsage.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this ResourceUsage.

        资源类型名称

        :param resource_type_name: The resource_type_name of this ResourceUsage.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def source_resource_spec_code(self):
        r"""Gets the source_resource_spec_code of this ResourceUsage.

        源资源规格编码

        :return: The source_resource_spec_code of this ResourceUsage.
        :rtype: str
        """
        return self._source_resource_spec_code

    @source_resource_spec_code.setter
    def source_resource_spec_code(self, source_resource_spec_code):
        r"""Sets the source_resource_spec_code of this ResourceUsage.

        源资源规格编码

        :param source_resource_spec_code: The source_resource_spec_code of this ResourceUsage.
        :type source_resource_spec_code: str
        """
        self._source_resource_spec_code = source_resource_spec_code

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ResourceUsage.

        源资源规格编码

        :return: The resource_spec_code of this ResourceUsage.
        :rtype: object
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ResourceUsage.

        源资源规格编码

        :param resource_spec_code: The resource_spec_code of this ResourceUsage.
        :type resource_spec_code: object
        """
        self._resource_spec_code = resource_spec_code

    @property
    def source_type(self):
        r"""Gets the source_type of this ResourceUsage.

        源资源类型编码

        :return: The source_type of this ResourceUsage.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ResourceUsage.

        源资源类型编码

        :param source_type: The source_type of this ResourceUsage.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def used_percent(self):
        r"""Gets the used_percent of this ResourceUsage.

        用量百分比

        :return: The used_percent of this ResourceUsage.
        :rtype: float
        """
        return self._used_percent

    @used_percent.setter
    def used_percent(self, used_percent):
        r"""Sets the used_percent of this ResourceUsage.

        用量百分比

        :param used_percent: The used_percent of this ResourceUsage.
        :type used_percent: float
        """
        self._used_percent = used_percent

    @property
    def quota(self):
        r"""Gets the quota of this ResourceUsage.

        配额总量

        :return: The quota of this ResourceUsage.
        :rtype: float
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ResourceUsage.

        配额总量

        :param quota: The quota of this ResourceUsage.
        :type quota: float
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this ResourceUsage.

        已用量

        :return: The used of this ResourceUsage.
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ResourceUsage.

        已用量

        :param used: The used of this ResourceUsage.
        :type used: float
        """
        self._used = used

    @property
    def free(self):
        r"""Gets the free of this ResourceUsage.

        剩余量

        :return: The free of this ResourceUsage.
        :rtype: float
        """
        return self._free

    @free.setter
    def free(self, free):
        r"""Sets the free of this ResourceUsage.

        剩余量

        :param free: The free of this ResourceUsage.
        :type free: float
        """
        self._free = free

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
        if not isinstance(other, ResourceUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
