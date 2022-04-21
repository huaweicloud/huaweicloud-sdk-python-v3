# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEngineSupportFeaturesPropertiesEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'max_task': 'str',
        'min_task': 'str',
        'max_node': 'str',
        'min_node': 'str'
    }

    attribute_map = {
        'max_task': 'max_task',
        'min_task': 'min_task',
        'max_node': 'max_node',
        'min_node': 'min_node'
    }

    def __init__(self, max_task=None, min_task=None, max_node=None, min_node=None):
        """ListEngineSupportFeaturesPropertiesEntity

        The model defined in huaweicloud sdk

        :param max_task: 转储功能的最大任务数。
        :type max_task: str
        :param min_task: 转储功能的最小任务数。
        :type min_task: str
        :param max_node: 转储功能的最大节点数。
        :type max_node: str
        :param min_node: 转储功能的最小节点数。
        :type min_node: str
        """
        
        

        self._max_task = None
        self._min_task = None
        self._max_node = None
        self._min_node = None
        self.discriminator = None

        if max_task is not None:
            self.max_task = max_task
        if min_task is not None:
            self.min_task = min_task
        if max_node is not None:
            self.max_node = max_node
        if min_node is not None:
            self.min_node = min_node

    @property
    def max_task(self):
        """Gets the max_task of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最大任务数。

        :return: The max_task of this ListEngineSupportFeaturesPropertiesEntity.
        :rtype: str
        """
        return self._max_task

    @max_task.setter
    def max_task(self, max_task):
        """Sets the max_task of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最大任务数。

        :param max_task: The max_task of this ListEngineSupportFeaturesPropertiesEntity.
        :type max_task: str
        """
        self._max_task = max_task

    @property
    def min_task(self):
        """Gets the min_task of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最小任务数。

        :return: The min_task of this ListEngineSupportFeaturesPropertiesEntity.
        :rtype: str
        """
        return self._min_task

    @min_task.setter
    def min_task(self, min_task):
        """Sets the min_task of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最小任务数。

        :param min_task: The min_task of this ListEngineSupportFeaturesPropertiesEntity.
        :type min_task: str
        """
        self._min_task = min_task

    @property
    def max_node(self):
        """Gets the max_node of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最大节点数。

        :return: The max_node of this ListEngineSupportFeaturesPropertiesEntity.
        :rtype: str
        """
        return self._max_node

    @max_node.setter
    def max_node(self, max_node):
        """Sets the max_node of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最大节点数。

        :param max_node: The max_node of this ListEngineSupportFeaturesPropertiesEntity.
        :type max_node: str
        """
        self._max_node = max_node

    @property
    def min_node(self):
        """Gets the min_node of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最小节点数。

        :return: The min_node of this ListEngineSupportFeaturesPropertiesEntity.
        :rtype: str
        """
        return self._min_node

    @min_node.setter
    def min_node(self, min_node):
        """Sets the min_node of this ListEngineSupportFeaturesPropertiesEntity.

        转储功能的最小节点数。

        :param min_node: The min_node of this ListEngineSupportFeaturesPropertiesEntity.
        :type min_node: str
        """
        self._min_node = min_node

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
        if not isinstance(other, ListEngineSupportFeaturesPropertiesEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
