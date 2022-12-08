# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlanSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_add': 'int',
        'resource_update': 'int',
        'resource_delete': 'int'
    }

    attribute_map = {
        'resource_add': 'resource_add',
        'resource_update': 'resource_update',
        'resource_delete': 'resource_delete'
    }

    def __init__(self, resource_add=None, resource_update=None, resource_delete=None):
        """ExecutionPlanSummary

        The model defined in huaweicloud sdk

        :param resource_add: 新增资源数
        :type resource_add: int
        :param resource_update: 更新资源数
        :type resource_update: int
        :param resource_delete: 删除资源数
        :type resource_delete: int
        """
        
        

        self._resource_add = None
        self._resource_update = None
        self._resource_delete = None
        self.discriminator = None

        if resource_add is not None:
            self.resource_add = resource_add
        if resource_update is not None:
            self.resource_update = resource_update
        if resource_delete is not None:
            self.resource_delete = resource_delete

    @property
    def resource_add(self):
        """Gets the resource_add of this ExecutionPlanSummary.

        新增资源数

        :return: The resource_add of this ExecutionPlanSummary.
        :rtype: int
        """
        return self._resource_add

    @resource_add.setter
    def resource_add(self, resource_add):
        """Sets the resource_add of this ExecutionPlanSummary.

        新增资源数

        :param resource_add: The resource_add of this ExecutionPlanSummary.
        :type resource_add: int
        """
        self._resource_add = resource_add

    @property
    def resource_update(self):
        """Gets the resource_update of this ExecutionPlanSummary.

        更新资源数

        :return: The resource_update of this ExecutionPlanSummary.
        :rtype: int
        """
        return self._resource_update

    @resource_update.setter
    def resource_update(self, resource_update):
        """Sets the resource_update of this ExecutionPlanSummary.

        更新资源数

        :param resource_update: The resource_update of this ExecutionPlanSummary.
        :type resource_update: int
        """
        self._resource_update = resource_update

    @property
    def resource_delete(self):
        """Gets the resource_delete of this ExecutionPlanSummary.

        删除资源数

        :return: The resource_delete of this ExecutionPlanSummary.
        :rtype: int
        """
        return self._resource_delete

    @resource_delete.setter
    def resource_delete(self, resource_delete):
        """Sets the resource_delete of this ExecutionPlanSummary.

        删除资源数

        :param resource_delete: The resource_delete of this ExecutionPlanSummary.
        :type resource_delete: int
        """
        self._resource_delete = resource_delete

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
        if not isinstance(other, ExecutionPlanSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
