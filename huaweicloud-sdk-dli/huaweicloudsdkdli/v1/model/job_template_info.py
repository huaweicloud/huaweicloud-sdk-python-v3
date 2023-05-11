# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobTemplateInfo:

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
        'id': 'str',
        'name': 'str',
        'body': 'BatchJobInfo',
        'group': 'str',
        'description': 'str',
        'language': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'body': 'body',
        'group': 'group',
        'description': 'description',
        'language': 'language',
        'owner': 'owner'
    }

    def __init__(self, type=None, id=None, name=None, body=None, group=None, description=None, language=None, owner=None):
        """JobTemplateInfo

        The model defined in huaweicloud sdk

        :param type: 模板类型
        :type type: str
        :param id: 模板id
        :type id: str
        :param name: 模板名字
        :type name: str
        :param body: 
        :type body: :class:`huaweicloudsdkdli.v1.BatchJobInfo`
        :param group: 组名
        :type group: str
        :param description: 模板描述
        :type description: str
        :param language: 语言
        :type language: str
        :param owner: 模板拥有者
        :type owner: str
        """
        
        

        self._type = None
        self._id = None
        self._name = None
        self._body = None
        self._group = None
        self._description = None
        self._language = None
        self._owner = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if body is not None:
            self.body = body
        if group is not None:
            self.group = group
        if description is not None:
            self.description = description
        if language is not None:
            self.language = language
        if owner is not None:
            self.owner = owner

    @property
    def type(self):
        """Gets the type of this JobTemplateInfo.

        模板类型

        :return: The type of this JobTemplateInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobTemplateInfo.

        模板类型

        :param type: The type of this JobTemplateInfo.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this JobTemplateInfo.

        模板id

        :return: The id of this JobTemplateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobTemplateInfo.

        模板id

        :param id: The id of this JobTemplateInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this JobTemplateInfo.

        模板名字

        :return: The name of this JobTemplateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobTemplateInfo.

        模板名字

        :param name: The name of this JobTemplateInfo.
        :type name: str
        """
        self._name = name

    @property
    def body(self):
        """Gets the body of this JobTemplateInfo.

        :return: The body of this JobTemplateInfo.
        :rtype: :class:`huaweicloudsdkdli.v1.BatchJobInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this JobTemplateInfo.

        :param body: The body of this JobTemplateInfo.
        :type body: :class:`huaweicloudsdkdli.v1.BatchJobInfo`
        """
        self._body = body

    @property
    def group(self):
        """Gets the group of this JobTemplateInfo.

        组名

        :return: The group of this JobTemplateInfo.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this JobTemplateInfo.

        组名

        :param group: The group of this JobTemplateInfo.
        :type group: str
        """
        self._group = group

    @property
    def description(self):
        """Gets the description of this JobTemplateInfo.

        模板描述

        :return: The description of this JobTemplateInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobTemplateInfo.

        模板描述

        :param description: The description of this JobTemplateInfo.
        :type description: str
        """
        self._description = description

    @property
    def language(self):
        """Gets the language of this JobTemplateInfo.

        语言

        :return: The language of this JobTemplateInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this JobTemplateInfo.

        语言

        :param language: The language of this JobTemplateInfo.
        :type language: str
        """
        self._language = language

    @property
    def owner(self):
        """Gets the owner of this JobTemplateInfo.

        模板拥有者

        :return: The owner of this JobTemplateInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this JobTemplateInfo.

        模板拥有者

        :param owner: The owner of this JobTemplateInfo.
        :type owner: str
        """
        self._owner = owner

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
        if not isinstance(other, JobTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
