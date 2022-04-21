# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'branch': 'str',
        'language': 'str',
        'exclude_dir': 'str',
        'encode': 'str',
        'compile_config': 'str',
        'rule_template': 'str'
    }

    attribute_map = {
        'url': 'url',
        'branch': 'branch',
        'language': 'language',
        'exclude_dir': 'exclude_dir',
        'encode': 'encode',
        'compile_config': 'compile_config',
        'rule_template': 'rule_template'
    }

    def __init__(self, url=None, branch=None, language=None, exclude_dir=None, encode=None, compile_config=None, rule_template=None):
        """ParamInfo

        The model defined in huaweicloud sdk

        :param url: 仓库地址
        :type url: str
        :param branch: 仓库分支
        :type branch: str
        :param language: 仓库语言
        :type language: str
        :param exclude_dir: 排除的目录
        :type exclude_dir: str
        :param encode: 编码格式
        :type encode: str
        :param compile_config: 编译配置信息
        :type compile_config: str
        :param rule_template: g规则集名称
        :type rule_template: str
        """
        
        

        self._url = None
        self._branch = None
        self._language = None
        self._exclude_dir = None
        self._encode = None
        self._compile_config = None
        self._rule_template = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if branch is not None:
            self.branch = branch
        if language is not None:
            self.language = language
        if exclude_dir is not None:
            self.exclude_dir = exclude_dir
        if encode is not None:
            self.encode = encode
        if compile_config is not None:
            self.compile_config = compile_config
        if rule_template is not None:
            self.rule_template = rule_template

    @property
    def url(self):
        """Gets the url of this ParamInfo.

        仓库地址

        :return: The url of this ParamInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ParamInfo.

        仓库地址

        :param url: The url of this ParamInfo.
        :type url: str
        """
        self._url = url

    @property
    def branch(self):
        """Gets the branch of this ParamInfo.

        仓库分支

        :return: The branch of this ParamInfo.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this ParamInfo.

        仓库分支

        :param branch: The branch of this ParamInfo.
        :type branch: str
        """
        self._branch = branch

    @property
    def language(self):
        """Gets the language of this ParamInfo.

        仓库语言

        :return: The language of this ParamInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ParamInfo.

        仓库语言

        :param language: The language of this ParamInfo.
        :type language: str
        """
        self._language = language

    @property
    def exclude_dir(self):
        """Gets the exclude_dir of this ParamInfo.

        排除的目录

        :return: The exclude_dir of this ParamInfo.
        :rtype: str
        """
        return self._exclude_dir

    @exclude_dir.setter
    def exclude_dir(self, exclude_dir):
        """Sets the exclude_dir of this ParamInfo.

        排除的目录

        :param exclude_dir: The exclude_dir of this ParamInfo.
        :type exclude_dir: str
        """
        self._exclude_dir = exclude_dir

    @property
    def encode(self):
        """Gets the encode of this ParamInfo.

        编码格式

        :return: The encode of this ParamInfo.
        :rtype: str
        """
        return self._encode

    @encode.setter
    def encode(self, encode):
        """Sets the encode of this ParamInfo.

        编码格式

        :param encode: The encode of this ParamInfo.
        :type encode: str
        """
        self._encode = encode

    @property
    def compile_config(self):
        """Gets the compile_config of this ParamInfo.

        编译配置信息

        :return: The compile_config of this ParamInfo.
        :rtype: str
        """
        return self._compile_config

    @compile_config.setter
    def compile_config(self, compile_config):
        """Sets the compile_config of this ParamInfo.

        编译配置信息

        :param compile_config: The compile_config of this ParamInfo.
        :type compile_config: str
        """
        self._compile_config = compile_config

    @property
    def rule_template(self):
        """Gets the rule_template of this ParamInfo.

        g规则集名称

        :return: The rule_template of this ParamInfo.
        :rtype: str
        """
        return self._rule_template

    @rule_template.setter
    def rule_template(self, rule_template):
        """Sets the rule_template of this ParamInfo.

        g规则集名称

        :param rule_template: The rule_template of this ParamInfo.
        :type rule_template: str
        """
        self._rule_template = rule_template

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
        if not isinstance(other, ParamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
