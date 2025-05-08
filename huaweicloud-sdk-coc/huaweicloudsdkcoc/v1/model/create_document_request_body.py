# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDocumentRequestBody:

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
        'content': 'str',
        'enterprise_project_id': 'str',
        'risk_level': 'str',
        'description': 'str',
        'tags': 'list[CreateDocumentRequestBodyTags]'
    }

    attribute_map = {
        'name': 'name',
        'content': 'content',
        'enterprise_project_id': 'enterprise_project_id',
        'risk_level': 'risk_level',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, name=None, content=None, enterprise_project_id=None, risk_level=None, description=None, tags=None):
        r"""CreateDocumentRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业名称
        :type name: str
        :param content: 作业内容，DSL语句，最大长度64KB
        :type content: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param risk_level: 风险等级。 - LOW：低。 - MEDIUM：中。 - HIGH：高。
        :type risk_level: str
        :param description: 描述
        :type description: str
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        """
        
        

        self._name = None
        self._content = None
        self._enterprise_project_id = None
        self._risk_level = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.content = content
        self.enterprise_project_id = enterprise_project_id
        self.risk_level = risk_level
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateDocumentRequestBody.

        作业名称

        :return: The name of this CreateDocumentRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDocumentRequestBody.

        作业名称

        :param name: The name of this CreateDocumentRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        r"""Gets the content of this CreateDocumentRequestBody.

        作业内容，DSL语句，最大长度64KB

        :return: The content of this CreateDocumentRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateDocumentRequestBody.

        作业内容，DSL语句，最大长度64KB

        :param content: The content of this CreateDocumentRequestBody.
        :type content: str
        """
        self._content = content

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateDocumentRequestBody.

        企业项目id

        :return: The enterprise_project_id of this CreateDocumentRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateDocumentRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateDocumentRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def risk_level(self):
        r"""Gets the risk_level of this CreateDocumentRequestBody.

        风险等级。 - LOW：低。 - MEDIUM：中。 - HIGH：高。

        :return: The risk_level of this CreateDocumentRequestBody.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this CreateDocumentRequestBody.

        风险等级。 - LOW：低。 - MEDIUM：中。 - HIGH：高。

        :param risk_level: The risk_level of this CreateDocumentRequestBody.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def description(self):
        r"""Gets the description of this CreateDocumentRequestBody.

        描述

        :return: The description of this CreateDocumentRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDocumentRequestBody.

        描述

        :param description: The description of this CreateDocumentRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this CreateDocumentRequestBody.

        标签列表

        :return: The tags of this CreateDocumentRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateDocumentRequestBody.

        标签列表

        :param tags: The tags of this CreateDocumentRequestBody.
        :type tags: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateDocumentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
