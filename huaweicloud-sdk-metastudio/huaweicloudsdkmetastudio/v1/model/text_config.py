# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text': 'str'
    }

    attribute_map = {
        'text': 'text'
    }

    def __init__(self, text=None):
        """TextConfig

        The model defined in huaweicloud sdk

        :param text: 台词脚本。  支持两种模式，纯文本模式和标签模式。  ### 纯文本模式 纯文本模式，使用方法，如“大家好，我是人工智大家，是个虚拟主播”  ### 标签模式 标签模式的定义使用SSML（Speech Synthesis Markup Language）标记语言。  - **\\&lt;speak&gt;**    \\&lt;speak&gt;标签是所有文本的根节点。一切需要调用SSML标签的文本都要包含在\\&lt;speak&gt; \\&lt;/speak&gt;对中。  - **\\&lt;emotion&gt;**    \\&lt;emotion&gt;标签是情感标签。对指定一句或多句话生效，标签开始在句子起始位置，标签关闭在句子结尾。用法：\\&lt;emotion type&#x3D;\&quot;情感标签\&quot;&gt;。type可取值包括：HAPPY、SAD、CALM、ANGER  - **\\&lt;insert-action&gt;**    \\&lt;insert-action&gt;标签是动作标签。在文本的指定位置插入动作。用法：\\&lt;insert-action id&#x3D;\&quot;动作资产ID\&quot; name&#x3D;\&quot;动作名称\&quot; tag&#x3D;\&quot;动作标识\&quot;/&gt;。动作资产信息通过资产库接口查询获取。  - **\\&lt;break&gt;**     \\&lt;break&gt;标签是停顿标签。在文本的指定位置插入停顿。用法：\\&lt;break time&#x3D;\&quot;停顿时长\&quot;/&gt;。停顿时长单位是毫秒，最小值200毫秒。  - **\\&lt;phoneme&gt;**     \\&lt;phoneme&gt;标签是多音字标签。多音字标签可以指定单个汉字的读音。标签起始和关闭之间只能包含1个汉字。属性可取值为汉语拼音，声调用1、2、3、4表示。用法：\\&lt;phoneme ph&#x3D;\&quot;拼音\&quot;/&gt;字\\&lt;/phoneme&gt;。   &gt; * 举例：\\&lt;speak&gt; \\&lt;emotion type&#x3D;\\\&quot;HAPPY\\\&quot;&gt;\\&lt;insert-action id&#x3D;\&quot;2692ea5d095caaafcfed21dc4590b701\&quot; name&#x3D;\&quot;双手指尖交触\&quot; tag&#x3D;\&quot;system_female_animation_0026\&quot;/&gt;大家好，\\&lt;break time&#x3D;\&quot;200ms\&quot;/&gt;我是MetaStudio制作的人工智能数字人。\\&lt;/emotion&gt;我带大家\\&lt;phoneme ph&#x3D;\&quot;liao3\&quot;&gt;了\\&lt;/phoneme&gt;解MetaStudio。\\&lt;/speak&gt; &gt; * 分身数字人视频制作仅break和phoneme标签生效。
        :type text: str
        """
        
        

        self._text = None
        self.discriminator = None

        self.text = text

    @property
    def text(self):
        """Gets the text of this TextConfig.

        台词脚本。  支持两种模式，纯文本模式和标签模式。  ### 纯文本模式 纯文本模式，使用方法，如“大家好，我是人工智大家，是个虚拟主播”  ### 标签模式 标签模式的定义使用SSML（Speech Synthesis Markup Language）标记语言。  - **\\<speak>**    \\<speak>标签是所有文本的根节点。一切需要调用SSML标签的文本都要包含在\\<speak> \\</speak>对中。  - **\\<emotion>**    \\<emotion>标签是情感标签。对指定一句或多句话生效，标签开始在句子起始位置，标签关闭在句子结尾。用法：\\<emotion type=\"情感标签\">。type可取值包括：HAPPY、SAD、CALM、ANGER  - **\\<insert-action>**    \\<insert-action>标签是动作标签。在文本的指定位置插入动作。用法：\\<insert-action id=\"动作资产ID\" name=\"动作名称\" tag=\"动作标识\"/>。动作资产信息通过资产库接口查询获取。  - **\\<break>**     \\<break>标签是停顿标签。在文本的指定位置插入停顿。用法：\\<break time=\"停顿时长\"/>。停顿时长单位是毫秒，最小值200毫秒。  - **\\<phoneme>**     \\<phoneme>标签是多音字标签。多音字标签可以指定单个汉字的读音。标签起始和关闭之间只能包含1个汉字。属性可取值为汉语拼音，声调用1、2、3、4表示。用法：\\<phoneme ph=\"拼音\"/>字\\</phoneme>。   > * 举例：\\<speak> \\<emotion type=\\\"HAPPY\\\">\\<insert-action id=\"2692ea5d095caaafcfed21dc4590b701\" name=\"双手指尖交触\" tag=\"system_female_animation_0026\"/>大家好，\\<break time=\"200ms\"/>我是MetaStudio制作的人工智能数字人。\\</emotion>我带大家\\<phoneme ph=\"liao3\">了\\</phoneme>解MetaStudio。\\</speak> > * 分身数字人视频制作仅break和phoneme标签生效。

        :return: The text of this TextConfig.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextConfig.

        台词脚本。  支持两种模式，纯文本模式和标签模式。  ### 纯文本模式 纯文本模式，使用方法，如“大家好，我是人工智大家，是个虚拟主播”  ### 标签模式 标签模式的定义使用SSML（Speech Synthesis Markup Language）标记语言。  - **\\<speak>**    \\<speak>标签是所有文本的根节点。一切需要调用SSML标签的文本都要包含在\\<speak> \\</speak>对中。  - **\\<emotion>**    \\<emotion>标签是情感标签。对指定一句或多句话生效，标签开始在句子起始位置，标签关闭在句子结尾。用法：\\<emotion type=\"情感标签\">。type可取值包括：HAPPY、SAD、CALM、ANGER  - **\\<insert-action>**    \\<insert-action>标签是动作标签。在文本的指定位置插入动作。用法：\\<insert-action id=\"动作资产ID\" name=\"动作名称\" tag=\"动作标识\"/>。动作资产信息通过资产库接口查询获取。  - **\\<break>**     \\<break>标签是停顿标签。在文本的指定位置插入停顿。用法：\\<break time=\"停顿时长\"/>。停顿时长单位是毫秒，最小值200毫秒。  - **\\<phoneme>**     \\<phoneme>标签是多音字标签。多音字标签可以指定单个汉字的读音。标签起始和关闭之间只能包含1个汉字。属性可取值为汉语拼音，声调用1、2、3、4表示。用法：\\<phoneme ph=\"拼音\"/>字\\</phoneme>。   > * 举例：\\<speak> \\<emotion type=\\\"HAPPY\\\">\\<insert-action id=\"2692ea5d095caaafcfed21dc4590b701\" name=\"双手指尖交触\" tag=\"system_female_animation_0026\"/>大家好，\\<break time=\"200ms\"/>我是MetaStudio制作的人工智能数字人。\\</emotion>我带大家\\<phoneme ph=\"liao3\">了\\</phoneme>解MetaStudio。\\</speak> > * 分身数字人视频制作仅break和phoneme标签生效。

        :param text: The text of this TextConfig.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, TextConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
