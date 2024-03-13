# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskRulesetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'language': 'str',
        'template_name': 'str',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'language': 'language',
        'template_name': 'template_name',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, template_id=None, language=None, template_name=None, type=None, status=None):
        """TaskRulesetInfo

        The model defined in huaweicloud sdk

        :param template_id: 规则集id
        :type template_id: str
        :param language: 规则集语言
        :type language: str
        :param template_name: 规则集名称
        :type template_name: str
        :param type: 规则集状态optional：可选，selected：已选
        :type type: str
        :param status: 规则集属性0 是默认用户规则集,1 是系统默认规则集
        :type status: str
        """
        
        

        self._template_id = None
        self._language = None
        self._template_name = None
        self._type = None
        self._status = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if language is not None:
            self.language = language
        if template_name is not None:
            self.template_name = template_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status

    @property
    def template_id(self):
        """Gets the template_id of this TaskRulesetInfo.

        规则集id

        :return: The template_id of this TaskRulesetInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TaskRulesetInfo.

        规则集id

        :param template_id: The template_id of this TaskRulesetInfo.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def language(self):
        """Gets the language of this TaskRulesetInfo.

        规则集语言

        :return: The language of this TaskRulesetInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TaskRulesetInfo.

        规则集语言

        :param language: The language of this TaskRulesetInfo.
        :type language: str
        """
        self._language = language

    @property
    def template_name(self):
        """Gets the template_name of this TaskRulesetInfo.

        规则集名称

        :return: The template_name of this TaskRulesetInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TaskRulesetInfo.

        规则集名称

        :param template_name: The template_name of this TaskRulesetInfo.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def type(self):
        """Gets the type of this TaskRulesetInfo.

        规则集状态optional：可选，selected：已选

        :return: The type of this TaskRulesetInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskRulesetInfo.

        规则集状态optional：可选，selected：已选

        :param type: The type of this TaskRulesetInfo.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this TaskRulesetInfo.

        规则集属性0 是默认用户规则集,1 是系统默认规则集

        :return: The status of this TaskRulesetInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskRulesetInfo.

        规则集属性0 是默认用户规则集,1 是系统默认规则集

        :param status: The status of this TaskRulesetInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, TaskRulesetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
