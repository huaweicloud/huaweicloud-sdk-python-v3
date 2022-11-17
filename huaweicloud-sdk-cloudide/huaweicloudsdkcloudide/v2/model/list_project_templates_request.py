# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'stack_id': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'stack_id': 'stack_id'
    }

    def __init__(self, arch=None, stack_id=None):
        """ListProjectTemplatesRequest

        The model defined in huaweicloud sdk

        :param arch: cpu架构 x86|arm
        :type arch: str
        :param stack_id: 技术栈ID，通过技术栈管理ListStacks接口获取。
        :type stack_id: str
        """
        
        

        self._arch = None
        self._stack_id = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        self.stack_id = stack_id

    @property
    def arch(self):
        """Gets the arch of this ListProjectTemplatesRequest.

        cpu架构 x86|arm

        :return: The arch of this ListProjectTemplatesRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ListProjectTemplatesRequest.

        cpu架构 x86|arm

        :param arch: The arch of this ListProjectTemplatesRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def stack_id(self):
        """Gets the stack_id of this ListProjectTemplatesRequest.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :return: The stack_id of this ListProjectTemplatesRequest.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this ListProjectTemplatesRequest.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :param stack_id: The stack_id of this ListProjectTemplatesRequest.
        :type stack_id: str
        """
        self._stack_id = stack_id

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
        if not isinstance(other, ListProjectTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
