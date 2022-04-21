# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageGroup:

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
        'warm_data_retention_policy': 'str',
        'cold_data_retention_policy': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'warm_data_retention_policy': 'warm_data_retention_policy',
        'cold_data_retention_policy': 'cold_data_retention_policy'
    }

    def __init__(self, name=None, description=None, warm_data_retention_policy=None, cold_data_retention_policy=None):
        """StorageGroup

        The model defined in huaweicloud sdk

        :param name: 存储组名称
        :type name: str
        :param description: 描述
        :type description: str
        :param warm_data_retention_policy: 温数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持
        :type warm_data_retention_policy: str
        :param cold_data_retention_policy: 冷数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持
        :type cold_data_retention_policy: str
        """
        
        

        self._name = None
        self._description = None
        self._warm_data_retention_policy = None
        self._cold_data_retention_policy = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if warm_data_retention_policy is not None:
            self.warm_data_retention_policy = warm_data_retention_policy
        if cold_data_retention_policy is not None:
            self.cold_data_retention_policy = cold_data_retention_policy

    @property
    def name(self):
        """Gets the name of this StorageGroup.

        存储组名称

        :return: The name of this StorageGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageGroup.

        存储组名称

        :param name: The name of this StorageGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this StorageGroup.

        描述

        :return: The description of this StorageGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StorageGroup.

        描述

        :param description: The description of this StorageGroup.
        :type description: str
        """
        self._description = description

    @property
    def warm_data_retention_policy(self):
        """Gets the warm_data_retention_policy of this StorageGroup.

        温数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :return: The warm_data_retention_policy of this StorageGroup.
        :rtype: str
        """
        return self._warm_data_retention_policy

    @warm_data_retention_policy.setter
    def warm_data_retention_policy(self, warm_data_retention_policy):
        """Sets the warm_data_retention_policy of this StorageGroup.

        温数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :param warm_data_retention_policy: The warm_data_retention_policy of this StorageGroup.
        :type warm_data_retention_policy: str
        """
        self._warm_data_retention_policy = warm_data_retention_policy

    @property
    def cold_data_retention_policy(self):
        """Gets the cold_data_retention_policy of this StorageGroup.

        冷数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :return: The cold_data_retention_policy of this StorageGroup.
        :rtype: str
        """
        return self._cold_data_retention_policy

    @cold_data_retention_policy.setter
    def cold_data_retention_policy(self, cold_data_retention_policy):
        """Sets the cold_data_retention_policy of this StorageGroup.

        冷数据老化策略，单位只支持d（天），且只支持整数，如365天则可配置为“365d”，如“365h”或“360.5d”等均不被支持

        :param cold_data_retention_policy: The cold_data_retention_policy of this StorageGroup.
        :type cold_data_retention_policy: str
        """
        self._cold_data_retention_policy = cold_data_retention_policy

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
        if not isinstance(other, StorageGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
