# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenEntityWithExtInfoEntity:

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
        'create_time': 'float',
        'created_by': 'str',
        'display_text': 'str',
        'guid': 'str',
        'relationship_attributes': 'object',
        'type_name': 'str',
        'updated_by': 'str',
        'update_time': 'float',
        'tags': 'list[TagHeader]',
        'classification_names': 'list[str]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'connection': 'connection',
        'create_time': 'create_time',
        'created_by': 'created_by',
        'display_text': 'display_text',
        'guid': 'guid',
        'relationship_attributes': 'relationship_attributes',
        'type_name': 'type_name',
        'updated_by': 'updated_by',
        'update_time': 'update_time',
        'tags': 'tags',
        'classification_names': 'classification_names'
    }

    def __init__(self, attributes=None, connection=None, create_time=None, created_by=None, display_text=None, guid=None, relationship_attributes=None, type_name=None, updated_by=None, update_time=None, tags=None, classification_names=None):
        r"""OpenEntityWithExtInfoEntity

        The model defined in huaweicloud sdk

        :param attributes: 属性Map&lt;String, Object&gt;
        :type attributes: object
        :param connection: 
        :type connection: :class:`huaweicloudsdkdataartsstudio.v1.Connection`
        :param create_time: 创建时间
        :type create_time: float
        :param created_by: 创建人
        :type created_by: str
        :param display_text: 资产的名称
        :type display_text: str
        :param guid: 资产guid
        :type guid: str
        :param relationship_attributes: 相关的属性 Map&lt;String, Object&gt;
        :type relationship_attributes: object
        :param type_name: 资产类型
        :type type_name: str
        :param updated_by: 更新人
        :type updated_by: str
        :param update_time: 更新时间
        :type update_time: float
        :param tags: 标签 List&lt;TagHeader&gt;
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagHeader`]
        :param classification_names: 分类名称 List&lt;String&gt;
        :type classification_names: list[str]
        """
        
        

        self._attributes = None
        self._connection = None
        self._create_time = None
        self._created_by = None
        self._display_text = None
        self._guid = None
        self._relationship_attributes = None
        self._type_name = None
        self._updated_by = None
        self._update_time = None
        self._tags = None
        self._classification_names = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if connection is not None:
            self.connection = connection
        if create_time is not None:
            self.create_time = create_time
        if created_by is not None:
            self.created_by = created_by
        if display_text is not None:
            self.display_text = display_text
        if guid is not None:
            self.guid = guid
        if relationship_attributes is not None:
            self.relationship_attributes = relationship_attributes
        if type_name is not None:
            self.type_name = type_name
        if updated_by is not None:
            self.updated_by = updated_by
        if update_time is not None:
            self.update_time = update_time
        if tags is not None:
            self.tags = tags
        if classification_names is not None:
            self.classification_names = classification_names

    @property
    def attributes(self):
        r"""Gets the attributes of this OpenEntityWithExtInfoEntity.

        属性Map<String, Object>

        :return: The attributes of this OpenEntityWithExtInfoEntity.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this OpenEntityWithExtInfoEntity.

        属性Map<String, Object>

        :param attributes: The attributes of this OpenEntityWithExtInfoEntity.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def connection(self):
        r"""Gets the connection of this OpenEntityWithExtInfoEntity.

        :return: The connection of this OpenEntityWithExtInfoEntity.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.Connection`
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this OpenEntityWithExtInfoEntity.

        :param connection: The connection of this OpenEntityWithExtInfoEntity.
        :type connection: :class:`huaweicloudsdkdataartsstudio.v1.Connection`
        """
        self._connection = connection

    @property
    def create_time(self):
        r"""Gets the create_time of this OpenEntityWithExtInfoEntity.

        创建时间

        :return: The create_time of this OpenEntityWithExtInfoEntity.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this OpenEntityWithExtInfoEntity.

        创建时间

        :param create_time: The create_time of this OpenEntityWithExtInfoEntity.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def created_by(self):
        r"""Gets the created_by of this OpenEntityWithExtInfoEntity.

        创建人

        :return: The created_by of this OpenEntityWithExtInfoEntity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this OpenEntityWithExtInfoEntity.

        创建人

        :param created_by: The created_by of this OpenEntityWithExtInfoEntity.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def display_text(self):
        r"""Gets the display_text of this OpenEntityWithExtInfoEntity.

        资产的名称

        :return: The display_text of this OpenEntityWithExtInfoEntity.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        r"""Sets the display_text of this OpenEntityWithExtInfoEntity.

        资产的名称

        :param display_text: The display_text of this OpenEntityWithExtInfoEntity.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def guid(self):
        r"""Gets the guid of this OpenEntityWithExtInfoEntity.

        资产guid

        :return: The guid of this OpenEntityWithExtInfoEntity.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this OpenEntityWithExtInfoEntity.

        资产guid

        :param guid: The guid of this OpenEntityWithExtInfoEntity.
        :type guid: str
        """
        self._guid = guid

    @property
    def relationship_attributes(self):
        r"""Gets the relationship_attributes of this OpenEntityWithExtInfoEntity.

        相关的属性 Map<String, Object>

        :return: The relationship_attributes of this OpenEntityWithExtInfoEntity.
        :rtype: object
        """
        return self._relationship_attributes

    @relationship_attributes.setter
    def relationship_attributes(self, relationship_attributes):
        r"""Sets the relationship_attributes of this OpenEntityWithExtInfoEntity.

        相关的属性 Map<String, Object>

        :param relationship_attributes: The relationship_attributes of this OpenEntityWithExtInfoEntity.
        :type relationship_attributes: object
        """
        self._relationship_attributes = relationship_attributes

    @property
    def type_name(self):
        r"""Gets the type_name of this OpenEntityWithExtInfoEntity.

        资产类型

        :return: The type_name of this OpenEntityWithExtInfoEntity.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        r"""Sets the type_name of this OpenEntityWithExtInfoEntity.

        资产类型

        :param type_name: The type_name of this OpenEntityWithExtInfoEntity.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def updated_by(self):
        r"""Gets the updated_by of this OpenEntityWithExtInfoEntity.

        更新人

        :return: The updated_by of this OpenEntityWithExtInfoEntity.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this OpenEntityWithExtInfoEntity.

        更新人

        :param updated_by: The updated_by of this OpenEntityWithExtInfoEntity.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def update_time(self):
        r"""Gets the update_time of this OpenEntityWithExtInfoEntity.

        更新时间

        :return: The update_time of this OpenEntityWithExtInfoEntity.
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this OpenEntityWithExtInfoEntity.

        更新时间

        :param update_time: The update_time of this OpenEntityWithExtInfoEntity.
        :type update_time: float
        """
        self._update_time = update_time

    @property
    def tags(self):
        r"""Gets the tags of this OpenEntityWithExtInfoEntity.

        标签 List<TagHeader>

        :return: The tags of this OpenEntityWithExtInfoEntity.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TagHeader`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpenEntityWithExtInfoEntity.

        标签 List<TagHeader>

        :param tags: The tags of this OpenEntityWithExtInfoEntity.
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagHeader`]
        """
        self._tags = tags

    @property
    def classification_names(self):
        r"""Gets the classification_names of this OpenEntityWithExtInfoEntity.

        分类名称 List<String>

        :return: The classification_names of this OpenEntityWithExtInfoEntity.
        :rtype: list[str]
        """
        return self._classification_names

    @classification_names.setter
    def classification_names(self, classification_names):
        r"""Sets the classification_names of this OpenEntityWithExtInfoEntity.

        分类名称 List<String>

        :param classification_names: The classification_names of this OpenEntityWithExtInfoEntity.
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
        if not isinstance(other, OpenEntityWithExtInfoEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
