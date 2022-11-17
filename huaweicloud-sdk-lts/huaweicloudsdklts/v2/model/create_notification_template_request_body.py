# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotificationTemplateRequestBody:

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
        'type': 'list[str]',
        'desc': 'str',
        'source': 'str',
        'locale': 'str',
        'templates': 'list[SubTemplate]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'desc': 'desc',
        'source': 'source',
        'locale': 'locale',
        'templates': 'templates'
    }

    def __init__(self, name=None, type=None, desc=None, source=None, locale=None, templates=None):
        """CreateNotificationTemplateRequestBody

        The model defined in huaweicloud sdk

        :param name: 通知规则名称，必填，只含有汉字、数字、字母、下划线、中划线，不能以下划线等特殊符号开头和结尾，长度为 1 - 100，创建后不可修改
        :type name: str
        :param type: 保留字段，非必填，只支持sms（短信），dingding（钉钉），wechat（企业微信），email（邮件）和webhook（网络钩子）
        :type type: list[str]
        :param desc: 模板描述，必填，只含有汉字、数字、字母、下划线不能以下划线开头和结尾，长度为0--1024
        :type desc: str
        :param source: 模板来源，目前必填为LTS，否则会筛选不出来
        :type source: str
        :param locale: 语言，必填，目前可填zh-cn和en-us
        :type locale: str
        :param templates: 模板正文，为一个数组
        :type templates: list[:class:`huaweicloudsdklts.v2.SubTemplate`]
        """
        
        

        self._name = None
        self._type = None
        self._desc = None
        self._source = None
        self._locale = None
        self._templates = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        self.desc = desc
        self.source = source
        self.locale = locale
        self.templates = templates

    @property
    def name(self):
        """Gets the name of this CreateNotificationTemplateRequestBody.

        通知规则名称，必填，只含有汉字、数字、字母、下划线、中划线，不能以下划线等特殊符号开头和结尾，长度为 1 - 100，创建后不可修改

        :return: The name of this CreateNotificationTemplateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNotificationTemplateRequestBody.

        通知规则名称，必填，只含有汉字、数字、字母、下划线、中划线，不能以下划线等特殊符号开头和结尾，长度为 1 - 100，创建后不可修改

        :param name: The name of this CreateNotificationTemplateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateNotificationTemplateRequestBody.

        保留字段，非必填，只支持sms（短信），dingding（钉钉），wechat（企业微信），email（邮件）和webhook（网络钩子）

        :return: The type of this CreateNotificationTemplateRequestBody.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateNotificationTemplateRequestBody.

        保留字段，非必填，只支持sms（短信），dingding（钉钉），wechat（企业微信），email（邮件）和webhook（网络钩子）

        :param type: The type of this CreateNotificationTemplateRequestBody.
        :type type: list[str]
        """
        self._type = type

    @property
    def desc(self):
        """Gets the desc of this CreateNotificationTemplateRequestBody.

        模板描述，必填，只含有汉字、数字、字母、下划线不能以下划线开头和结尾，长度为0--1024

        :return: The desc of this CreateNotificationTemplateRequestBody.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateNotificationTemplateRequestBody.

        模板描述，必填，只含有汉字、数字、字母、下划线不能以下划线开头和结尾，长度为0--1024

        :param desc: The desc of this CreateNotificationTemplateRequestBody.
        :type desc: str
        """
        self._desc = desc

    @property
    def source(self):
        """Gets the source of this CreateNotificationTemplateRequestBody.

        模板来源，目前必填为LTS，否则会筛选不出来

        :return: The source of this CreateNotificationTemplateRequestBody.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateNotificationTemplateRequestBody.

        模板来源，目前必填为LTS，否则会筛选不出来

        :param source: The source of this CreateNotificationTemplateRequestBody.
        :type source: str
        """
        self._source = source

    @property
    def locale(self):
        """Gets the locale of this CreateNotificationTemplateRequestBody.

        语言，必填，目前可填zh-cn和en-us

        :return: The locale of this CreateNotificationTemplateRequestBody.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CreateNotificationTemplateRequestBody.

        语言，必填，目前可填zh-cn和en-us

        :param locale: The locale of this CreateNotificationTemplateRequestBody.
        :type locale: str
        """
        self._locale = locale

    @property
    def templates(self):
        """Gets the templates of this CreateNotificationTemplateRequestBody.

        模板正文，为一个数组

        :return: The templates of this CreateNotificationTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.SubTemplate`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this CreateNotificationTemplateRequestBody.

        模板正文，为一个数组

        :param templates: The templates of this CreateNotificationTemplateRequestBody.
        :type templates: list[:class:`huaweicloudsdklts.v2.SubTemplate`]
        """
        self._templates = templates

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
        if not isinstance(other, CreateNotificationTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
