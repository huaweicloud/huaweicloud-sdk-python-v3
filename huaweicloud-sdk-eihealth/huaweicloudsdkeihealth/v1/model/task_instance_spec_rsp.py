# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInstanceSpecRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'containers': 'list[TaskInstanceSpecContainersRsp]'
    }

    attribute_map = {
        'containers': 'containers'
    }

    def __init__(self, containers=None):
        """TaskInstanceSpecRsp

        The model defined in huaweicloud sdk

        :param containers: 实例详情响应体
        :type containers: list[:class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecContainersRsp`]
        """
        
        

        self._containers = None
        self.discriminator = None

        if containers is not None:
            self.containers = containers

    @property
    def containers(self):
        """Gets the containers of this TaskInstanceSpecRsp.

        实例详情响应体

        :return: The containers of this TaskInstanceSpecRsp.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecContainersRsp`]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this TaskInstanceSpecRsp.

        实例详情响应体

        :param containers: The containers of this TaskInstanceSpecRsp.
        :type containers: list[:class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecContainersRsp`]
        """
        self._containers = containers

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
        if not isinstance(other, TaskInstanceSpecRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
