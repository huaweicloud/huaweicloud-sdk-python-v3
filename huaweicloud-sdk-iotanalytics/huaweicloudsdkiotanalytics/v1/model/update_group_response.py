# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'name': 'str',
        'description': 'str',
        'warm_data_usage': 'int',
        'data_store_count': 'int',
        'cold_data_usage': 'int',
        'warm_data_retention_policy': 'str',
        'cold_data_retention_policy': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'type': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'name': 'name',
        'description': 'description',
        'warm_data_usage': 'warm_data_usage',
        'data_store_count': 'data_store_count',
        'cold_data_usage': 'cold_data_usage',
        'warm_data_retention_policy': 'warm_data_retention_policy',
        'cold_data_retention_policy': 'cold_data_retention_policy',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'type': 'type'
    }

    def __init__(self, group_id=None, name=None, description=None, warm_data_usage=None, data_store_count=None, cold_data_usage=None, warm_data_retention_policy=None, cold_data_retention_policy=None, created_time=None, modified_time=None, type=None):
        """UpdateGroupResponse

        The model defined in huaweicloud sdk

        :param group_id: 存储组 ID
        :type group_id: str
        :param name: 存储组名称
        :type name: str
        :param description: 描述
        :type description: str
        :param warm_data_usage: 温数据存储用量
        :type warm_data_usage: int
        :param data_store_count: 此存储组下存储实例的个数
        :type data_store_count: int
        :param cold_data_usage: 冷数据存储用量
        :type cold_data_usage: int
        :param warm_data_retention_policy: 温数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持
        :type warm_data_retention_policy: str
        :param cold_data_retention_policy: 冷数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持
        :type cold_data_retention_policy: str
        :param created_time: 创建时间
        :type created_time: str
        :param modified_time: 修改时间
        :type modified_time: str
        :param type: 存储类型，有资产存储(取值:AssetStorage)、设备存储(取值:DeviceStorage)两种类型
        :type type: str
        """
        
        super(UpdateGroupResponse, self).__init__()

        self._group_id = None
        self._name = None
        self._description = None
        self._warm_data_usage = None
        self._data_store_count = None
        self._cold_data_usage = None
        self._warm_data_retention_policy = None
        self._cold_data_retention_policy = None
        self._created_time = None
        self._modified_time = None
        self._type = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if warm_data_usage is not None:
            self.warm_data_usage = warm_data_usage
        if data_store_count is not None:
            self.data_store_count = data_store_count
        if cold_data_usage is not None:
            self.cold_data_usage = cold_data_usage
        if warm_data_retention_policy is not None:
            self.warm_data_retention_policy = warm_data_retention_policy
        if cold_data_retention_policy is not None:
            self.cold_data_retention_policy = cold_data_retention_policy
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if type is not None:
            self.type = type

    @property
    def group_id(self):
        """Gets the group_id of this UpdateGroupResponse.

        存储组 ID

        :return: The group_id of this UpdateGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateGroupResponse.

        存储组 ID

        :param group_id: The group_id of this UpdateGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this UpdateGroupResponse.

        存储组名称

        :return: The name of this UpdateGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateGroupResponse.

        存储组名称

        :param name: The name of this UpdateGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateGroupResponse.

        描述

        :return: The description of this UpdateGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateGroupResponse.

        描述

        :param description: The description of this UpdateGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def warm_data_usage(self):
        """Gets the warm_data_usage of this UpdateGroupResponse.

        温数据存储用量

        :return: The warm_data_usage of this UpdateGroupResponse.
        :rtype: int
        """
        return self._warm_data_usage

    @warm_data_usage.setter
    def warm_data_usage(self, warm_data_usage):
        """Sets the warm_data_usage of this UpdateGroupResponse.

        温数据存储用量

        :param warm_data_usage: The warm_data_usage of this UpdateGroupResponse.
        :type warm_data_usage: int
        """
        self._warm_data_usage = warm_data_usage

    @property
    def data_store_count(self):
        """Gets the data_store_count of this UpdateGroupResponse.

        此存储组下存储实例的个数

        :return: The data_store_count of this UpdateGroupResponse.
        :rtype: int
        """
        return self._data_store_count

    @data_store_count.setter
    def data_store_count(self, data_store_count):
        """Sets the data_store_count of this UpdateGroupResponse.

        此存储组下存储实例的个数

        :param data_store_count: The data_store_count of this UpdateGroupResponse.
        :type data_store_count: int
        """
        self._data_store_count = data_store_count

    @property
    def cold_data_usage(self):
        """Gets the cold_data_usage of this UpdateGroupResponse.

        冷数据存储用量

        :return: The cold_data_usage of this UpdateGroupResponse.
        :rtype: int
        """
        return self._cold_data_usage

    @cold_data_usage.setter
    def cold_data_usage(self, cold_data_usage):
        """Sets the cold_data_usage of this UpdateGroupResponse.

        冷数据存储用量

        :param cold_data_usage: The cold_data_usage of this UpdateGroupResponse.
        :type cold_data_usage: int
        """
        self._cold_data_usage = cold_data_usage

    @property
    def warm_data_retention_policy(self):
        """Gets the warm_data_retention_policy of this UpdateGroupResponse.

        温数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :return: The warm_data_retention_policy of this UpdateGroupResponse.
        :rtype: str
        """
        return self._warm_data_retention_policy

    @warm_data_retention_policy.setter
    def warm_data_retention_policy(self, warm_data_retention_policy):
        """Sets the warm_data_retention_policy of this UpdateGroupResponse.

        温数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :param warm_data_retention_policy: The warm_data_retention_policy of this UpdateGroupResponse.
        :type warm_data_retention_policy: str
        """
        self._warm_data_retention_policy = warm_data_retention_policy

    @property
    def cold_data_retention_policy(self):
        """Gets the cold_data_retention_policy of this UpdateGroupResponse.

        冷数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :return: The cold_data_retention_policy of this UpdateGroupResponse.
        :rtype: str
        """
        return self._cold_data_retention_policy

    @cold_data_retention_policy.setter
    def cold_data_retention_policy(self, cold_data_retention_policy):
        """Sets the cold_data_retention_policy of this UpdateGroupResponse.

        冷数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :param cold_data_retention_policy: The cold_data_retention_policy of this UpdateGroupResponse.
        :type cold_data_retention_policy: str
        """
        self._cold_data_retention_policy = cold_data_retention_policy

    @property
    def created_time(self):
        """Gets the created_time of this UpdateGroupResponse.

        创建时间

        :return: The created_time of this UpdateGroupResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateGroupResponse.

        创建时间

        :param created_time: The created_time of this UpdateGroupResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this UpdateGroupResponse.

        修改时间

        :return: The modified_time of this UpdateGroupResponse.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this UpdateGroupResponse.

        修改时间

        :param modified_time: The modified_time of this UpdateGroupResponse.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def type(self):
        """Gets the type of this UpdateGroupResponse.

        存储类型，有资产存储(取值:AssetStorage)、设备存储(取值:DeviceStorage)两种类型

        :return: The type of this UpdateGroupResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateGroupResponse.

        存储类型，有资产存储(取值:AssetStorage)、设备存储(取值:DeviceStorage)两种类型

        :param type: The type of this UpdateGroupResponse.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, UpdateGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
