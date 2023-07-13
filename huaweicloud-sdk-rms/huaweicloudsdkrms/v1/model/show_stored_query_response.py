# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStoredQueryResponse(SdkResponse):

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
        'description': 'str',
        'expression': 'str',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'expression': 'expression',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, description=None, expression=None, created=None, updated=None):
        """ShowStoredQueryResponse

        The model defined in huaweicloud sdk

        :param id: ResourceQL ID
        :type id: str
        :param name: ResourceQL 名字
        :type name: str
        :param description: ResourceQL 描述
        :type description: str
        :param expression: ResourceQL 表达式
        :type expression: str
        :param created: ResourceQL 创建时间
        :type created: str
        :param updated: ResourceQL 更新时间
        :type updated: str
        """
        
        super(ShowStoredQueryResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._expression = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if expression is not None:
            self.expression = expression
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this ShowStoredQueryResponse.

        ResourceQL ID

        :return: The id of this ShowStoredQueryResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowStoredQueryResponse.

        ResourceQL ID

        :param id: The id of this ShowStoredQueryResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowStoredQueryResponse.

        ResourceQL 名字

        :return: The name of this ShowStoredQueryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowStoredQueryResponse.

        ResourceQL 名字

        :param name: The name of this ShowStoredQueryResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowStoredQueryResponse.

        ResourceQL 描述

        :return: The description of this ShowStoredQueryResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowStoredQueryResponse.

        ResourceQL 描述

        :param description: The description of this ShowStoredQueryResponse.
        :type description: str
        """
        self._description = description

    @property
    def expression(self):
        """Gets the expression of this ShowStoredQueryResponse.

        ResourceQL 表达式

        :return: The expression of this ShowStoredQueryResponse.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ShowStoredQueryResponse.

        ResourceQL 表达式

        :param expression: The expression of this ShowStoredQueryResponse.
        :type expression: str
        """
        self._expression = expression

    @property
    def created(self):
        """Gets the created of this ShowStoredQueryResponse.

        ResourceQL 创建时间

        :return: The created of this ShowStoredQueryResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowStoredQueryResponse.

        ResourceQL 创建时间

        :param created: The created of this ShowStoredQueryResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowStoredQueryResponse.

        ResourceQL 更新时间

        :return: The updated of this ShowStoredQueryResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowStoredQueryResponse.

        ResourceQL 更新时间

        :param updated: The updated of this ShowStoredQueryResponse.
        :type updated: str
        """
        self._updated = updated

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
        if not isinstance(other, ShowStoredQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
