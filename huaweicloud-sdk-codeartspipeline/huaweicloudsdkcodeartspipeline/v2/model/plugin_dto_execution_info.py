# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginDTOExecutionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inner_execution_info': 'object'
    }

    attribute_map = {
        'inner_execution_info': 'inner_execution_info'
    }

    def __init__(self, inner_execution_info=None):
        """PluginDTOExecutionInfo

        The model defined in huaweicloud sdk

        :param inner_execution_info: 执行信息
        :type inner_execution_info: object
        """
        
        

        self._inner_execution_info = None
        self.discriminator = None

        if inner_execution_info is not None:
            self.inner_execution_info = inner_execution_info

    @property
    def inner_execution_info(self):
        """Gets the inner_execution_info of this PluginDTOExecutionInfo.

        执行信息

        :return: The inner_execution_info of this PluginDTOExecutionInfo.
        :rtype: object
        """
        return self._inner_execution_info

    @inner_execution_info.setter
    def inner_execution_info(self, inner_execution_info):
        """Sets the inner_execution_info of this PluginDTOExecutionInfo.

        执行信息

        :param inner_execution_info: The inner_execution_info of this PluginDTOExecutionInfo.
        :type inner_execution_info: object
        """
        self._inner_execution_info = inner_execution_info

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
        if not isinstance(other, PluginDTOExecutionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
