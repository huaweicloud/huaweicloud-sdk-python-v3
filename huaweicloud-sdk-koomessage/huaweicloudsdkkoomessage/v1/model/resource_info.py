# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'str',
        'type': 'str',
        'name': 'str',
        'source': 'str',
        'content': 'str'
    }

    attribute_map = {
        'index': 'index',
        'type': 'type',
        'name': 'name',
        'source': 'source',
        'content': 'content'
    }

    def __init__(self, index=None, type=None, name=None, source=None, content=None):
        r"""ResourceInfo

        The model defined in huaweicloud sdk

        :param index: 智能信息基础版序号。  从1开始，例如: 1-1，表示第1帧第1个元素；1-2：表示第1帧第2个元素；2-1：表示第2帧第1个元素。  &gt; - 每帧支持最多2个元素，2个元素中必须包含有文本 &gt; - 如果未填该字段，则每个元素独占一帧并按数组顺序排序 &gt; - 最多支持8帧 &gt; - 最多2帧同时包含2个元素 &gt; - index必须全部指定，或者全为空，不能重复 
        :type index: str
        :param type: 智能信息基础版资源类型。 - 类型为文字填：txt - 类型为图片填：jpg/jpeg/png/gif - 类型为音频填：mp3/wav - 类型为视频填：3gp 
        :type type: str
        :param name: 智能信息基础版资源名称。
        :type name: str
        :param source: 智能信息基础版资源来源。  - txt：表示资源内容是纯文字 - file：表示资源内容来源于文件流 - url：表示资源内容来源于URL外链  &gt; 资源来自于文字/文件流/URL外链。 
        :type source: str
        :param content: 智能信息基础版。 - 当source&#x3D;txt时，填写经过UTF-8编码的文字 - 当source&#x3D;file时，填写经过Base64编码的文件流，不须带文件格式前缀，样例：\&quot;iVBORw0KGgoAAAANSUhEUgA...\&quot;，样例过长，未显示全部 - 当source&#x3D;url时，填写资源URL地址，URL长度不能超过1024个字节  &gt; - 支持文字图片，文字和图片使用#p_n#参数变量占位，n为1~100内的数字，不同类型的资源中不允许有重复的参数占位符，相同类型的资源同一参数占位符可复用。如：#p_1#已表示是文本参数占位符时，不可以同时是图片又是文本参数占位符。不能包含除模板签名外的“【】” &gt; - 第一个文本帧，内容必须以：【签名】开始，&#39;签名&#39; 标识客户信息 
        :type content: str
        """
        
        

        self._index = None
        self._type = None
        self._name = None
        self._source = None
        self._content = None
        self.discriminator = None

        if index is not None:
            self.index = index
        self.type = type
        self.name = name
        self.source = source
        self.content = content

    @property
    def index(self):
        r"""Gets the index of this ResourceInfo.

        智能信息基础版序号。  从1开始，例如: 1-1，表示第1帧第1个元素；1-2：表示第1帧第2个元素；2-1：表示第2帧第1个元素。  > - 每帧支持最多2个元素，2个元素中必须包含有文本 > - 如果未填该字段，则每个元素独占一帧并按数组顺序排序 > - 最多支持8帧 > - 最多2帧同时包含2个元素 > - index必须全部指定，或者全为空，不能重复 

        :return: The index of this ResourceInfo.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this ResourceInfo.

        智能信息基础版序号。  从1开始，例如: 1-1，表示第1帧第1个元素；1-2：表示第1帧第2个元素；2-1：表示第2帧第1个元素。  > - 每帧支持最多2个元素，2个元素中必须包含有文本 > - 如果未填该字段，则每个元素独占一帧并按数组顺序排序 > - 最多支持8帧 > - 最多2帧同时包含2个元素 > - index必须全部指定，或者全为空，不能重复 

        :param index: The index of this ResourceInfo.
        :type index: str
        """
        self._index = index

    @property
    def type(self):
        r"""Gets the type of this ResourceInfo.

        智能信息基础版资源类型。 - 类型为文字填：txt - 类型为图片填：jpg/jpeg/png/gif - 类型为音频填：mp3/wav - 类型为视频填：3gp 

        :return: The type of this ResourceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceInfo.

        智能信息基础版资源类型。 - 类型为文字填：txt - 类型为图片填：jpg/jpeg/png/gif - 类型为音频填：mp3/wav - 类型为视频填：3gp 

        :param type: The type of this ResourceInfo.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ResourceInfo.

        智能信息基础版资源名称。

        :return: The name of this ResourceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResourceInfo.

        智能信息基础版资源名称。

        :param name: The name of this ResourceInfo.
        :type name: str
        """
        self._name = name

    @property
    def source(self):
        r"""Gets the source of this ResourceInfo.

        智能信息基础版资源来源。  - txt：表示资源内容是纯文字 - file：表示资源内容来源于文件流 - url：表示资源内容来源于URL外链  > 资源来自于文字/文件流/URL外链。 

        :return: The source of this ResourceInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ResourceInfo.

        智能信息基础版资源来源。  - txt：表示资源内容是纯文字 - file：表示资源内容来源于文件流 - url：表示资源内容来源于URL外链  > 资源来自于文字/文件流/URL外链。 

        :param source: The source of this ResourceInfo.
        :type source: str
        """
        self._source = source

    @property
    def content(self):
        r"""Gets the content of this ResourceInfo.

        智能信息基础版。 - 当source=txt时，填写经过UTF-8编码的文字 - 当source=file时，填写经过Base64编码的文件流，不须带文件格式前缀，样例：\"iVBORw0KGgoAAAANSUhEUgA...\"，样例过长，未显示全部 - 当source=url时，填写资源URL地址，URL长度不能超过1024个字节  > - 支持文字图片，文字和图片使用#p_n#参数变量占位，n为1~100内的数字，不同类型的资源中不允许有重复的参数占位符，相同类型的资源同一参数占位符可复用。如：#p_1#已表示是文本参数占位符时，不可以同时是图片又是文本参数占位符。不能包含除模板签名外的“【】” > - 第一个文本帧，内容必须以：【签名】开始，'签名' 标识客户信息 

        :return: The content of this ResourceInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ResourceInfo.

        智能信息基础版。 - 当source=txt时，填写经过UTF-8编码的文字 - 当source=file时，填写经过Base64编码的文件流，不须带文件格式前缀，样例：\"iVBORw0KGgoAAAANSUhEUgA...\"，样例过长，未显示全部 - 当source=url时，填写资源URL地址，URL长度不能超过1024个字节  > - 支持文字图片，文字和图片使用#p_n#参数变量占位，n为1~100内的数字，不同类型的资源中不允许有重复的参数占位符，相同类型的资源同一参数占位符可复用。如：#p_1#已表示是文本参数占位符时，不可以同时是图片又是文本参数占位符。不能包含除模板签名外的“【】” > - 第一个文本帧，内容必须以：【签名】开始，'签名' 标识客户信息 

        :param content: The content of this ResourceInfo.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, ResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
