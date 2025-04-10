# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DependencyParserWord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'word': 'str',
        'head_word_id': 'int',
        'pos': 'str',
        'dependency_label': 'str'
    }

    attribute_map = {
        'id': 'id',
        'word': 'word',
        'head_word_id': 'head_word_id',
        'pos': 'pos',
        'dependency_label': 'dependency_label'
    }

    def __init__(self, id=None, word=None, head_word_id=None, pos=None, dependency_label=None):
        r"""DependencyParserWord

        The model defined in huaweicloud sdk

        :param id: 词汇id
        :type id: int
        :param word: 词汇内容
        :type word: str
        :param head_word_id: 头节点ID，根节点默认为0
        :type head_word_id: int
        :param pos: 词性
        :type pos: str
        :param dependency_label: 词与头节点的依存关系，包括以下几种类型 1.根节点root 根节点是指整个句子的谓语动词。 如：我/爱/妈妈(root-&gt;爱)。 2.同主语同宾语关系sasubj-obj  (same subject and object) 同主语同宾语关系是指句子中属于同一级且具有相同的主语和宾语的两个动词。 如：我/一直在/研究/和/思考/这个/问题/。(研究–&gt;思考)。 3.同主语关系sasubj (same subject) 同主语关系是指句子中属于同一级且具有相同的主语中的两个动词。 如：我/走进/操场/打/篮球/。(走进–&gt;打)。 4.不同主语关系dfsubj (different subject ) 不同主语关系是指句子中属于同一级且具有不同的主语的两个动词。 如：我/走进/操场/打/篮球/。(走进–&gt;打)。 5.主语关系subj (subject) 主语关系是指动词的主语 如：我/爱/妈妈(我&lt;-爱)。 6.主谓谓语中的内部主语关系subj-in (subject inside a subject-predicate predicate) 句子中一个主谓短语，是对主语动作或状态的陈述或说明时，那么就认为这个主谓短语整体作为谓语。 为了区分两个主语，里面那个主语的依存关系类型为subj-in，外面的主语的依存关系类型为subj。 如：他/确实/头/疼(头&lt;–疼)。 7.宾语关系obj (object) 宾语是指谓语动词的承受对象，即受事。 如：我/爱/妈妈(爱-&gt;妈妈)。 8.谓语关系pred (predicate) 兼语结构句式一般有两个动词(V1+N+V2)，其中N 是V1 的宾语，同时又是V2 的主语，V2即为N的谓语。 如：命令 /他/扫地(他–&gt;扫地)。 9.定语关系att (attribute) 定语关系是指定语和中心词之间的关系，定语对中心词起修饰或限制作用。 如：国家/主席(国家&lt;–主席)。 10.状语关系adv (adverbial) 状语一般修饰谓语动词或形容词，状语在核心词的前面。 如：非常/喜欢(非常&lt;–喜欢)。 11.补语关系cmp (complement) 补语一般修饰谓语动词或形容词，补语在核心词的后面（和状语相反）。 如：洗/干净/手(洗–&gt;干净)。 12.并列关系coo (coordination ) 并列关系是指两个相同性质的词并列在一起。 如：鲜花/和/掌声(鲜花–&gt;掌声)。 13.介宾关系pobj (preposition-object) 介词后面的名词或代词称为介词宾语。 如：在/家/看书(在–&gt;家)。 14.间接宾语关系iobj (indirect-object) 有些动词可以同时支配两个宾语。为了区分，将第一个宾语称为间接宾语。 如：给/他/书(给–&gt;他)。 15.“的”字关系de (de-construction) “的”字关系是指“的” 后面很明显应该有名词或代词，但被省略，此时“的”与前面的成分构成“的”字关系。 如：这/是/他/的(他&lt;–的)。 16.附加关系adjct (adjunct) 附加关系是指一些句子中没有实际意义的、只是为了让句子结构完整、或者讲起来更有韵味（抑扬顿挫）的词语。 如：我/走/了(走–&gt;了)。 17.称呼关系app (appellation) 称呼关系是指对人的称呼，主要是口语中的现象。 如：老师/，/你/好(老师&lt;–好)。 18.进一步解释关系exp (explanation) 汉语书面语中，常常会使用括号在原本流畅的表达中，插入一些解释说明的话。括号中的内容如果是解释说明对应的词、或短语、或句子则为进一步解释关系。 如：普京/（/俄罗斯/总统/）(普京–&gt;总统)。 19.标点关系punc (punctuation) 标点符号依存于其前面句子的核心词。 如：我/爱/妈妈(爱-&gt;。)。 20.片段关系frag (fragment) 片段关系是指汉语中不符合语法、支离破碎、病句的汉语句子。 如：你/，/我/，/中国/。(你–&gt;我–&gt;中国)。 21.重复关系repet (repetition) 重复关系是指汉语口语中出现说话结巴、重复称呼、表示强调等情况。 如：你 吃/，/吃/饭/了/吗/？(吃–&gt;吃)。
        :type dependency_label: str
        """
        
        

        self._id = None
        self._word = None
        self._head_word_id = None
        self._pos = None
        self._dependency_label = None
        self.discriminator = None

        self.id = id
        self.word = word
        self.head_word_id = head_word_id
        self.pos = pos
        self.dependency_label = dependency_label

    @property
    def id(self):
        r"""Gets the id of this DependencyParserWord.

        词汇id

        :return: The id of this DependencyParserWord.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DependencyParserWord.

        词汇id

        :param id: The id of this DependencyParserWord.
        :type id: int
        """
        self._id = id

    @property
    def word(self):
        r"""Gets the word of this DependencyParserWord.

        词汇内容

        :return: The word of this DependencyParserWord.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        r"""Sets the word of this DependencyParserWord.

        词汇内容

        :param word: The word of this DependencyParserWord.
        :type word: str
        """
        self._word = word

    @property
    def head_word_id(self):
        r"""Gets the head_word_id of this DependencyParserWord.

        头节点ID，根节点默认为0

        :return: The head_word_id of this DependencyParserWord.
        :rtype: int
        """
        return self._head_word_id

    @head_word_id.setter
    def head_word_id(self, head_word_id):
        r"""Sets the head_word_id of this DependencyParserWord.

        头节点ID，根节点默认为0

        :param head_word_id: The head_word_id of this DependencyParserWord.
        :type head_word_id: int
        """
        self._head_word_id = head_word_id

    @property
    def pos(self):
        r"""Gets the pos of this DependencyParserWord.

        词性

        :return: The pos of this DependencyParserWord.
        :rtype: str
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        r"""Sets the pos of this DependencyParserWord.

        词性

        :param pos: The pos of this DependencyParserWord.
        :type pos: str
        """
        self._pos = pos

    @property
    def dependency_label(self):
        r"""Gets the dependency_label of this DependencyParserWord.

        词与头节点的依存关系，包括以下几种类型 1.根节点root 根节点是指整个句子的谓语动词。 如：我/爱/妈妈(root->爱)。 2.同主语同宾语关系sasubj-obj  (same subject and object) 同主语同宾语关系是指句子中属于同一级且具有相同的主语和宾语的两个动词。 如：我/一直在/研究/和/思考/这个/问题/。(研究–>思考)。 3.同主语关系sasubj (same subject) 同主语关系是指句子中属于同一级且具有相同的主语中的两个动词。 如：我/走进/操场/打/篮球/。(走进–>打)。 4.不同主语关系dfsubj (different subject ) 不同主语关系是指句子中属于同一级且具有不同的主语的两个动词。 如：我/走进/操场/打/篮球/。(走进–>打)。 5.主语关系subj (subject) 主语关系是指动词的主语 如：我/爱/妈妈(我<-爱)。 6.主谓谓语中的内部主语关系subj-in (subject inside a subject-predicate predicate) 句子中一个主谓短语，是对主语动作或状态的陈述或说明时，那么就认为这个主谓短语整体作为谓语。 为了区分两个主语，里面那个主语的依存关系类型为subj-in，外面的主语的依存关系类型为subj。 如：他/确实/头/疼(头<–疼)。 7.宾语关系obj (object) 宾语是指谓语动词的承受对象，即受事。 如：我/爱/妈妈(爱->妈妈)。 8.谓语关系pred (predicate) 兼语结构句式一般有两个动词(V1+N+V2)，其中N 是V1 的宾语，同时又是V2 的主语，V2即为N的谓语。 如：命令 /他/扫地(他–>扫地)。 9.定语关系att (attribute) 定语关系是指定语和中心词之间的关系，定语对中心词起修饰或限制作用。 如：国家/主席(国家<–主席)。 10.状语关系adv (adverbial) 状语一般修饰谓语动词或形容词，状语在核心词的前面。 如：非常/喜欢(非常<–喜欢)。 11.补语关系cmp (complement) 补语一般修饰谓语动词或形容词，补语在核心词的后面（和状语相反）。 如：洗/干净/手(洗–>干净)。 12.并列关系coo (coordination ) 并列关系是指两个相同性质的词并列在一起。 如：鲜花/和/掌声(鲜花–>掌声)。 13.介宾关系pobj (preposition-object) 介词后面的名词或代词称为介词宾语。 如：在/家/看书(在–>家)。 14.间接宾语关系iobj (indirect-object) 有些动词可以同时支配两个宾语。为了区分，将第一个宾语称为间接宾语。 如：给/他/书(给–>他)。 15.“的”字关系de (de-construction) “的”字关系是指“的” 后面很明显应该有名词或代词，但被省略，此时“的”与前面的成分构成“的”字关系。 如：这/是/他/的(他<–的)。 16.附加关系adjct (adjunct) 附加关系是指一些句子中没有实际意义的、只是为了让句子结构完整、或者讲起来更有韵味（抑扬顿挫）的词语。 如：我/走/了(走–>了)。 17.称呼关系app (appellation) 称呼关系是指对人的称呼，主要是口语中的现象。 如：老师/，/你/好(老师<–好)。 18.进一步解释关系exp (explanation) 汉语书面语中，常常会使用括号在原本流畅的表达中，插入一些解释说明的话。括号中的内容如果是解释说明对应的词、或短语、或句子则为进一步解释关系。 如：普京/（/俄罗斯/总统/）(普京–>总统)。 19.标点关系punc (punctuation) 标点符号依存于其前面句子的核心词。 如：我/爱/妈妈(爱->。)。 20.片段关系frag (fragment) 片段关系是指汉语中不符合语法、支离破碎、病句的汉语句子。 如：你/，/我/，/中国/。(你–>我–>中国)。 21.重复关系repet (repetition) 重复关系是指汉语口语中出现说话结巴、重复称呼、表示强调等情况。 如：你 吃/，/吃/饭/了/吗/？(吃–>吃)。

        :return: The dependency_label of this DependencyParserWord.
        :rtype: str
        """
        return self._dependency_label

    @dependency_label.setter
    def dependency_label(self, dependency_label):
        r"""Sets the dependency_label of this DependencyParserWord.

        词与头节点的依存关系，包括以下几种类型 1.根节点root 根节点是指整个句子的谓语动词。 如：我/爱/妈妈(root->爱)。 2.同主语同宾语关系sasubj-obj  (same subject and object) 同主语同宾语关系是指句子中属于同一级且具有相同的主语和宾语的两个动词。 如：我/一直在/研究/和/思考/这个/问题/。(研究–>思考)。 3.同主语关系sasubj (same subject) 同主语关系是指句子中属于同一级且具有相同的主语中的两个动词。 如：我/走进/操场/打/篮球/。(走进–>打)。 4.不同主语关系dfsubj (different subject ) 不同主语关系是指句子中属于同一级且具有不同的主语的两个动词。 如：我/走进/操场/打/篮球/。(走进–>打)。 5.主语关系subj (subject) 主语关系是指动词的主语 如：我/爱/妈妈(我<-爱)。 6.主谓谓语中的内部主语关系subj-in (subject inside a subject-predicate predicate) 句子中一个主谓短语，是对主语动作或状态的陈述或说明时，那么就认为这个主谓短语整体作为谓语。 为了区分两个主语，里面那个主语的依存关系类型为subj-in，外面的主语的依存关系类型为subj。 如：他/确实/头/疼(头<–疼)。 7.宾语关系obj (object) 宾语是指谓语动词的承受对象，即受事。 如：我/爱/妈妈(爱->妈妈)。 8.谓语关系pred (predicate) 兼语结构句式一般有两个动词(V1+N+V2)，其中N 是V1 的宾语，同时又是V2 的主语，V2即为N的谓语。 如：命令 /他/扫地(他–>扫地)。 9.定语关系att (attribute) 定语关系是指定语和中心词之间的关系，定语对中心词起修饰或限制作用。 如：国家/主席(国家<–主席)。 10.状语关系adv (adverbial) 状语一般修饰谓语动词或形容词，状语在核心词的前面。 如：非常/喜欢(非常<–喜欢)。 11.补语关系cmp (complement) 补语一般修饰谓语动词或形容词，补语在核心词的后面（和状语相反）。 如：洗/干净/手(洗–>干净)。 12.并列关系coo (coordination ) 并列关系是指两个相同性质的词并列在一起。 如：鲜花/和/掌声(鲜花–>掌声)。 13.介宾关系pobj (preposition-object) 介词后面的名词或代词称为介词宾语。 如：在/家/看书(在–>家)。 14.间接宾语关系iobj (indirect-object) 有些动词可以同时支配两个宾语。为了区分，将第一个宾语称为间接宾语。 如：给/他/书(给–>他)。 15.“的”字关系de (de-construction) “的”字关系是指“的” 后面很明显应该有名词或代词，但被省略，此时“的”与前面的成分构成“的”字关系。 如：这/是/他/的(他<–的)。 16.附加关系adjct (adjunct) 附加关系是指一些句子中没有实际意义的、只是为了让句子结构完整、或者讲起来更有韵味（抑扬顿挫）的词语。 如：我/走/了(走–>了)。 17.称呼关系app (appellation) 称呼关系是指对人的称呼，主要是口语中的现象。 如：老师/，/你/好(老师<–好)。 18.进一步解释关系exp (explanation) 汉语书面语中，常常会使用括号在原本流畅的表达中，插入一些解释说明的话。括号中的内容如果是解释说明对应的词、或短语、或句子则为进一步解释关系。 如：普京/（/俄罗斯/总统/）(普京–>总统)。 19.标点关系punc (punctuation) 标点符号依存于其前面句子的核心词。 如：我/爱/妈妈(爱->。)。 20.片段关系frag (fragment) 片段关系是指汉语中不符合语法、支离破碎、病句的汉语句子。 如：你/，/我/，/中国/。(你–>我–>中国)。 21.重复关系repet (repetition) 重复关系是指汉语口语中出现说话结巴、重复称呼、表示强调等情况。 如：你 吃/，/吃/饭/了/吗/？(吃–>吃)。

        :param dependency_label: The dependency_label of this DependencyParserWord.
        :type dependency_label: str
        """
        self._dependency_label = dependency_label

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
        if not isinstance(other, DependencyParserWord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
