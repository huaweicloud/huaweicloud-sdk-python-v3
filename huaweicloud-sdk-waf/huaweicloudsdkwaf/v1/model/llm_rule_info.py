# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LlmRuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'discription': 'str',
        'url': 'str',
        'prompt_detect_opts': 'LlmRuleInfoPromptDetectOpts',
        'resp_detect_opts': 'LlmRuleInfoRespDetectOpts'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'discription': 'discription',
        'url': 'url',
        'prompt_detect_opts': 'prompt_detect_opts',
        'resp_detect_opts': 'resp_detect_opts'
    }

    def __init__(self, id=None, name=None, discription=None, url=None, prompt_detect_opts=None, resp_detect_opts=None):
        r"""LlmRuleInfo

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 规则名
        :type name: str
        :param discription: 规则描述
        :type discription: str
        :param url: 模型问答URL
        :type url: str
        :param prompt_detect_opts: 
        :type prompt_detect_opts: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOpts`
        :param resp_detect_opts: 
        :type resp_detect_opts: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoRespDetectOpts`
        """
        
        

        self._id = None
        self._name = None
        self._discription = None
        self._url = None
        self._prompt_detect_opts = None
        self._resp_detect_opts = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if discription is not None:
            self.discription = discription
        if url is not None:
            self.url = url
        if prompt_detect_opts is not None:
            self.prompt_detect_opts = prompt_detect_opts
        if resp_detect_opts is not None:
            self.resp_detect_opts = resp_detect_opts

    @property
    def id(self):
        r"""Gets the id of this LlmRuleInfo.

        规则id

        :return: The id of this LlmRuleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LlmRuleInfo.

        规则id

        :param id: The id of this LlmRuleInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this LlmRuleInfo.

        规则名

        :return: The name of this LlmRuleInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LlmRuleInfo.

        规则名

        :param name: The name of this LlmRuleInfo.
        :type name: str
        """
        self._name = name

    @property
    def discription(self):
        r"""Gets the discription of this LlmRuleInfo.

        规则描述

        :return: The discription of this LlmRuleInfo.
        :rtype: str
        """
        return self._discription

    @discription.setter
    def discription(self, discription):
        r"""Sets the discription of this LlmRuleInfo.

        规则描述

        :param discription: The discription of this LlmRuleInfo.
        :type discription: str
        """
        self._discription = discription

    @property
    def url(self):
        r"""Gets the url of this LlmRuleInfo.

        模型问答URL

        :return: The url of this LlmRuleInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this LlmRuleInfo.

        模型问答URL

        :param url: The url of this LlmRuleInfo.
        :type url: str
        """
        self._url = url

    @property
    def prompt_detect_opts(self):
        r"""Gets the prompt_detect_opts of this LlmRuleInfo.

        :return: The prompt_detect_opts of this LlmRuleInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOpts`
        """
        return self._prompt_detect_opts

    @prompt_detect_opts.setter
    def prompt_detect_opts(self, prompt_detect_opts):
        r"""Sets the prompt_detect_opts of this LlmRuleInfo.

        :param prompt_detect_opts: The prompt_detect_opts of this LlmRuleInfo.
        :type prompt_detect_opts: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOpts`
        """
        self._prompt_detect_opts = prompt_detect_opts

    @property
    def resp_detect_opts(self):
        r"""Gets the resp_detect_opts of this LlmRuleInfo.

        :return: The resp_detect_opts of this LlmRuleInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoRespDetectOpts`
        """
        return self._resp_detect_opts

    @resp_detect_opts.setter
    def resp_detect_opts(self, resp_detect_opts):
        r"""Sets the resp_detect_opts of this LlmRuleInfo.

        :param resp_detect_opts: The resp_detect_opts of this LlmRuleInfo.
        :type resp_detect_opts: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoRespDetectOpts`
        """
        self._resp_detect_opts = resp_detect_opts

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
        if not isinstance(other, LlmRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
