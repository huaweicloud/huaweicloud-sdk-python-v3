# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VarInfo:

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
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, name=None, type=None):
        r"""VarInfo

        The model defined in huaweicloud sdk

        :param name: 动参变量占位符名称。  &gt; 格式：#p_N#（N表示第几个参数，与模板文件占位名称保持一致），如：#p_1#。 
        :type name: str
        :param type: 动参变量类型。  - 类型为文字：txt - 类型为图片：jpg/jpeg/png/gif - 类型为音频：mp3/wav - 类型为视频：mp4/3gp 
        :type type: str
        """
        
        

        self._name = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def name(self):
        r"""Gets the name of this VarInfo.

        动参变量占位符名称。  > 格式：#p_N#（N表示第几个参数，与模板文件占位名称保持一致），如：#p_1#。 

        :return: The name of this VarInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VarInfo.

        动参变量占位符名称。  > 格式：#p_N#（N表示第几个参数，与模板文件占位名称保持一致），如：#p_1#。 

        :param name: The name of this VarInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this VarInfo.

        动参变量类型。  - 类型为文字：txt - 类型为图片：jpg/jpeg/png/gif - 类型为音频：mp3/wav - 类型为视频：mp4/3gp 

        :return: The type of this VarInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VarInfo.

        动参变量类型。  - 类型为文字：txt - 类型为图片：jpg/jpeg/png/gif - 类型为音频：mp3/wav - 类型为视频：mp4/3gp 

        :param type: The type of this VarInfo.
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
        if not isinstance(other, VarInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
