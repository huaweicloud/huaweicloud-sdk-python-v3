# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ToolInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tool_id': 'str',
        'tool_name': 'str',
        'tool_version': 'str',
        'tool_type': 'str'
    }

    attribute_map = {
        'tool_id': 'tool_id',
        'tool_name': 'tool_name',
        'tool_version': 'tool_version',
        'tool_type': 'tool_type'
    }

    def __init__(self, tool_id=None, tool_name=None, tool_version=None, tool_type=None):
        """ToolInfoDto

        The model defined in huaweicloud sdk

        :param tool_id: 作业依赖的组件id
        :type tool_id: str
        :param tool_name: 作业依赖的组件名称
        :type tool_name: str
        :param tool_version: 作业依赖的组件版本
        :type tool_version: str
        :param tool_type: 作业依赖的组件类型，取值范围app|workflow
        :type tool_type: str
        """
        
        

        self._tool_id = None
        self._tool_name = None
        self._tool_version = None
        self._tool_type = None
        self.discriminator = None

        if tool_id is not None:
            self.tool_id = tool_id
        if tool_name is not None:
            self.tool_name = tool_name
        if tool_version is not None:
            self.tool_version = tool_version
        if tool_type is not None:
            self.tool_type = tool_type

    @property
    def tool_id(self):
        """Gets the tool_id of this ToolInfoDto.

        作业依赖的组件id

        :return: The tool_id of this ToolInfoDto.
        :rtype: str
        """
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        """Sets the tool_id of this ToolInfoDto.

        作业依赖的组件id

        :param tool_id: The tool_id of this ToolInfoDto.
        :type tool_id: str
        """
        self._tool_id = tool_id

    @property
    def tool_name(self):
        """Gets the tool_name of this ToolInfoDto.

        作业依赖的组件名称

        :return: The tool_name of this ToolInfoDto.
        :rtype: str
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name):
        """Sets the tool_name of this ToolInfoDto.

        作业依赖的组件名称

        :param tool_name: The tool_name of this ToolInfoDto.
        :type tool_name: str
        """
        self._tool_name = tool_name

    @property
    def tool_version(self):
        """Gets the tool_version of this ToolInfoDto.

        作业依赖的组件版本

        :return: The tool_version of this ToolInfoDto.
        :rtype: str
        """
        return self._tool_version

    @tool_version.setter
    def tool_version(self, tool_version):
        """Sets the tool_version of this ToolInfoDto.

        作业依赖的组件版本

        :param tool_version: The tool_version of this ToolInfoDto.
        :type tool_version: str
        """
        self._tool_version = tool_version

    @property
    def tool_type(self):
        """Gets the tool_type of this ToolInfoDto.

        作业依赖的组件类型，取值范围app|workflow

        :return: The tool_type of this ToolInfoDto.
        :rtype: str
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        """Sets the tool_type of this ToolInfoDto.

        作业依赖的组件类型，取值范围app|workflow

        :param tool_type: The tool_type of this ToolInfoDto.
        :type tool_type: str
        """
        self._tool_type = tool_type

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
        if not isinstance(other, ToolInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
