# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenEntityHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attributes': 'object',
        'connection': 'Connection',
        'display_text': 'str',
        'guid': 'str',
        'type_name': 'str',
        'tags': 'list[TagHeader]',
        'classification_names': 'list[str]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'connection': 'connection',
        'display_text': 'display_text',
        'guid': 'guid',
        'type_name': 'type_name',
        'tags': 'tags',
        'classification_names': 'classification_names'
    }

    def __init__(self, attributes=None, connection=None, display_text=None, guid=None, type_name=None, tags=None, classification_names=None):
        """OpenEntityHeader

        The model defined in huaweicloud sdk

        :param attributes: 属性
        :type attributes: object
        :param connection: 
        :type connection: :class:`huaweicloudsdkdataartsstudio.v1.Connection`
        :param display_text: 展示文档
        :type display_text: str
        :param guid: 资产guid
        :type guid: str
        :param type_name: 类型名称
        :type type_name: str
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagHeader`]
        :param classification_names: 分类名称列表
        :type classification_names: list[str]
        """
        
        

        self._attributes = None
        self._connection = None
        self._display_text = None
        self._guid = None
        self._type_name = None
        self._tags = None
        self._classification_names = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if connection is not None:
            self.connection = connection
        if display_text is not None:
            self.display_text = display_text
        if guid is not None:
            self.guid = guid
        if type_name is not None:
            self.type_name = type_name
        if tags is not None:
            self.tags = tags
        if classification_names is not None:
            self.classification_names = classification_names

    @property
    def attributes(self):
        """Gets the attributes of this OpenEntityHeader.

        属性

        :return: The attributes of this OpenEntityHeader.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this OpenEntityHeader.

        属性

        :param attributes: The attributes of this OpenEntityHeader.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def connection(self):
        """Gets the connection of this OpenEntityHeader.

        :return: The connection of this OpenEntityHeader.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.Connection`
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this OpenEntityHeader.

        :param connection: The connection of this OpenEntityHeader.
        :type connection: :class:`huaweicloudsdkdataartsstudio.v1.Connection`
        """
        self._connection = connection

    @property
    def display_text(self):
        """Gets the display_text of this OpenEntityHeader.

        展示文档

        :return: The display_text of this OpenEntityHeader.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this OpenEntityHeader.

        展示文档

        :param display_text: The display_text of this OpenEntityHeader.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def guid(self):
        """Gets the guid of this OpenEntityHeader.

        资产guid

        :return: The guid of this OpenEntityHeader.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this OpenEntityHeader.

        资产guid

        :param guid: The guid of this OpenEntityHeader.
        :type guid: str
        """
        self._guid = guid

    @property
    def type_name(self):
        """Gets the type_name of this OpenEntityHeader.

        类型名称

        :return: The type_name of this OpenEntityHeader.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this OpenEntityHeader.

        类型名称

        :param type_name: The type_name of this OpenEntityHeader.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def tags(self):
        """Gets the tags of this OpenEntityHeader.

        标签列表

        :return: The tags of this OpenEntityHeader.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TagHeader`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this OpenEntityHeader.

        标签列表

        :param tags: The tags of this OpenEntityHeader.
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagHeader`]
        """
        self._tags = tags

    @property
    def classification_names(self):
        """Gets the classification_names of this OpenEntityHeader.

        分类名称列表

        :return: The classification_names of this OpenEntityHeader.
        :rtype: list[str]
        """
        return self._classification_names

    @classification_names.setter
    def classification_names(self, classification_names):
        """Sets the classification_names of this OpenEntityHeader.

        分类名称列表

        :param classification_names: The classification_names of this OpenEntityHeader.
        :type classification_names: list[str]
        """
        self._classification_names = classification_names

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
        if not isinstance(other, OpenEntityHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
