# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInstanceContainerStatusRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'restart_count': 'int'
    }

    attribute_map = {
        'restart_count': 'restart_count'
    }

    def __init__(self, restart_count=None):
        """TaskInstanceContainerStatusRsp

        The model defined in huaweicloud sdk

        :param restart_count: 重启次数
        :type restart_count: int
        """
        
        

        self._restart_count = None
        self.discriminator = None

        if restart_count is not None:
            self.restart_count = restart_count

    @property
    def restart_count(self):
        """Gets the restart_count of this TaskInstanceContainerStatusRsp.

        重启次数

        :return: The restart_count of this TaskInstanceContainerStatusRsp.
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        """Sets the restart_count of this TaskInstanceContainerStatusRsp.

        重启次数

        :param restart_count: The restart_count of this TaskInstanceContainerStatusRsp.
        :type restart_count: int
        """
        self._restart_count = restart_count

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
        if not isinstance(other, TaskInstanceContainerStatusRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
