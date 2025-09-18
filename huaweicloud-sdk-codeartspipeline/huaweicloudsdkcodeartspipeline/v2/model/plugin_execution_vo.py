# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginExecutionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'target': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'type': 'type',
        'target': 'target',
        'file_path': 'file_path'
    }

    def __init__(self, type=None, target=None, file_path=None):
        r"""PluginExecutionVO

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 插件执行脚本类型。 **取值范围**： - Shell：Shell类型脚本。 - Nodejs：Nodejs类型脚本。 - Java：Java类型脚本。 - Python：Python类型脚本。 
        :type type: str
        :param target: **参数解释**： 插件执行脚本入口文件。 **取值范围**： 不涉及。 
        :type target: str
        :param file_path: **参数解释**： 插件的OBS存放路径。 **取值范围**： 不涉及。 
        :type file_path: str
        """
        
        

        self._type = None
        self._target = None
        self._file_path = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if target is not None:
            self.target = target
        if file_path is not None:
            self.file_path = file_path

    @property
    def type(self):
        r"""Gets the type of this PluginExecutionVO.

        **参数解释**： 插件执行脚本类型。 **取值范围**： - Shell：Shell类型脚本。 - Nodejs：Nodejs类型脚本。 - Java：Java类型脚本。 - Python：Python类型脚本。 

        :return: The type of this PluginExecutionVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PluginExecutionVO.

        **参数解释**： 插件执行脚本类型。 **取值范围**： - Shell：Shell类型脚本。 - Nodejs：Nodejs类型脚本。 - Java：Java类型脚本。 - Python：Python类型脚本。 

        :param type: The type of this PluginExecutionVO.
        :type type: str
        """
        self._type = type

    @property
    def target(self):
        r"""Gets the target of this PluginExecutionVO.

        **参数解释**： 插件执行脚本入口文件。 **取值范围**： 不涉及。 

        :return: The target of this PluginExecutionVO.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this PluginExecutionVO.

        **参数解释**： 插件执行脚本入口文件。 **取值范围**： 不涉及。 

        :param target: The target of this PluginExecutionVO.
        :type target: str
        """
        self._target = target

    @property
    def file_path(self):
        r"""Gets the file_path of this PluginExecutionVO.

        **参数解释**： 插件的OBS存放路径。 **取值范围**： 不涉及。 

        :return: The file_path of this PluginExecutionVO.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this PluginExecutionVO.

        **参数解释**： 插件的OBS存放路径。 **取值范围**： 不涉及。 

        :param file_path: The file_path of this PluginExecutionVO.
        :type file_path: str
        """
        self._file_path = file_path

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
        if not isinstance(other, PluginExecutionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
