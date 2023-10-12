# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCnfReq:

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
        'conf_content': 'str',
        'setting': 'Setting',
        'sensitive_words': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'conf_content': 'confContent',
        'setting': 'setting',
        'sensitive_words': 'sensitive_words'
    }

    def __init__(self, name=None, conf_content=None, setting=None, sensitive_words=None):
        """CreateCnfReq

        The model defined in huaweicloud sdk

        :param name: 配置文件名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。
        :type name: str
        :param conf_content: 配置文件内容。
        :type conf_content: str
        :param setting: 
        :type setting: :class:`huaweicloudsdkcss.v1.Setting`
        :param sensitive_words: 敏感字符替换 输入需要隐藏的敏感字串列表。配置隐藏字符串列表后，在返回的配置内容中，会将所有在列表中的字串隐藏为***（列表最大支持20条，单个字串最大长度512字节）
        :type sensitive_words: list[str]
        """
        
        

        self._name = None
        self._conf_content = None
        self._setting = None
        self._sensitive_words = None
        self.discriminator = None

        self.name = name
        self.conf_content = conf_content
        self.setting = setting
        if sensitive_words is not None:
            self.sensitive_words = sensitive_words

    @property
    def name(self):
        """Gets the name of this CreateCnfReq.

        配置文件名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :return: The name of this CreateCnfReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCnfReq.

        配置文件名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :param name: The name of this CreateCnfReq.
        :type name: str
        """
        self._name = name

    @property
    def conf_content(self):
        """Gets the conf_content of this CreateCnfReq.

        配置文件内容。

        :return: The conf_content of this CreateCnfReq.
        :rtype: str
        """
        return self._conf_content

    @conf_content.setter
    def conf_content(self, conf_content):
        """Sets the conf_content of this CreateCnfReq.

        配置文件内容。

        :param conf_content: The conf_content of this CreateCnfReq.
        :type conf_content: str
        """
        self._conf_content = conf_content

    @property
    def setting(self):
        """Gets the setting of this CreateCnfReq.

        :return: The setting of this CreateCnfReq.
        :rtype: :class:`huaweicloudsdkcss.v1.Setting`
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        """Sets the setting of this CreateCnfReq.

        :param setting: The setting of this CreateCnfReq.
        :type setting: :class:`huaweicloudsdkcss.v1.Setting`
        """
        self._setting = setting

    @property
    def sensitive_words(self):
        """Gets the sensitive_words of this CreateCnfReq.

        敏感字符替换 输入需要隐藏的敏感字串列表。配置隐藏字符串列表后，在返回的配置内容中，会将所有在列表中的字串隐藏为***（列表最大支持20条，单个字串最大长度512字节）

        :return: The sensitive_words of this CreateCnfReq.
        :rtype: list[str]
        """
        return self._sensitive_words

    @sensitive_words.setter
    def sensitive_words(self, sensitive_words):
        """Sets the sensitive_words of this CreateCnfReq.

        敏感字符替换 输入需要隐藏的敏感字串列表。配置隐藏字符串列表后，在返回的配置内容中，会将所有在列表中的字串隐藏为***（列表最大支持20条，单个字串最大长度512字节）

        :param sensitive_words: The sensitive_words of this CreateCnfReq.
        :type sensitive_words: list[str]
        """
        self._sensitive_words = sensitive_words

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
        if not isinstance(other, CreateCnfReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
