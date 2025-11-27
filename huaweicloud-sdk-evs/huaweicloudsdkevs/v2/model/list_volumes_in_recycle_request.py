# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumesInRecycleRequest:

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
        'status': 'str',
        'limit': 'int',
        'availability_zone': 'str',
        'service_type': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'limit': 'limit',
        'availability_zone': 'availability_zone',
        'service_type': 'service_type',
        'offset': 'offset'
    }

    def __init__(self, name=None, status=None, limit=None, availability_zone=None, service_type=None, offset=None):
        r"""ListVolumesInRecycleRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释** 云硬盘名称。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘名称。 **约束限制** 最大支持64个字符。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type name: str
        :param status: **参数解释** 云硬盘状态，取值可参考：\&quot;[云硬盘状态](evs_04_0040.xml)\&quot;。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type status: str
        :param limit: **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 1-1000 **默认取值** 1000
        :type limit: int
        :param availability_zone: **参数解释** 可用区信息。 可通过接口[查询所有的可用分区信息](evs_04_2081.xml)获取，也可参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint)获取。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type availability_zone: str
        :param service_type: **参数解释** 服务类型。 **约束限制** 不涉及。 **取值范围** - EVS：云硬盘。 - DSS：专属分布式存储服务。 **默认取值** 不涉及。
        :type service_type: str
        :param offset: **参数解释** 分页查询时的偏移量。 **约束限制** 不涉及。 **取值范围** 取值为一个大于0小于磁盘总个数的整数。 **默认取值** 0
        :type offset: int
        """
        
        

        self._name = None
        self._status = None
        self._limit = None
        self._availability_zone = None
        self._service_type = None
        self._offset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if service_type is not None:
            self.service_type = service_type
        if offset is not None:
            self.offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListVolumesInRecycleRequest.

        **参数解释** 云硬盘名称。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘名称。 **约束限制** 最大支持64个字符。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The name of this ListVolumesInRecycleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVolumesInRecycleRequest.

        **参数解释** 云硬盘名称。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘名称。 **约束限制** 最大支持64个字符。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param name: The name of this ListVolumesInRecycleRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListVolumesInRecycleRequest.

        **参数解释** 云硬盘状态，取值可参考：\"[云硬盘状态](evs_04_0040.xml)\"。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The status of this ListVolumesInRecycleRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVolumesInRecycleRequest.

        **参数解释** 云硬盘状态，取值可参考：\"[云硬盘状态](evs_04_0040.xml)\"。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param status: The status of this ListVolumesInRecycleRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        r"""Gets the limit of this ListVolumesInRecycleRequest.

        **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 1-1000 **默认取值** 1000

        :return: The limit of this ListVolumesInRecycleRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVolumesInRecycleRequest.

        **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 1-1000 **默认取值** 1000

        :param limit: The limit of this ListVolumesInRecycleRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListVolumesInRecycleRequest.

        **参数解释** 可用区信息。 可通过接口[查询所有的可用分区信息](evs_04_2081.xml)获取，也可参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint)获取。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The availability_zone of this ListVolumesInRecycleRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListVolumesInRecycleRequest.

        **参数解释** 可用区信息。 可通过接口[查询所有的可用分区信息](evs_04_2081.xml)获取，也可参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint)获取。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param availability_zone: The availability_zone of this ListVolumesInRecycleRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def service_type(self):
        r"""Gets the service_type of this ListVolumesInRecycleRequest.

        **参数解释** 服务类型。 **约束限制** 不涉及。 **取值范围** - EVS：云硬盘。 - DSS：专属分布式存储服务。 **默认取值** 不涉及。

        :return: The service_type of this ListVolumesInRecycleRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListVolumesInRecycleRequest.

        **参数解释** 服务类型。 **约束限制** 不涉及。 **取值范围** - EVS：云硬盘。 - DSS：专属分布式存储服务。 **默认取值** 不涉及。

        :param service_type: The service_type of this ListVolumesInRecycleRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def offset(self):
        r"""Gets the offset of this ListVolumesInRecycleRequest.

        **参数解释** 分页查询时的偏移量。 **约束限制** 不涉及。 **取值范围** 取值为一个大于0小于磁盘总个数的整数。 **默认取值** 0

        :return: The offset of this ListVolumesInRecycleRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVolumesInRecycleRequest.

        **参数解释** 分页查询时的偏移量。 **约束限制** 不涉及。 **取值范围** 取值为一个大于0小于磁盘总个数的整数。 **默认取值** 0

        :param offset: The offset of this ListVolumesInRecycleRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListVolumesInRecycleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
