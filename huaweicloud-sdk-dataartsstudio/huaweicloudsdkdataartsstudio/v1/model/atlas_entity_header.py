# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtlasEntityHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type_name': 'str',
        'guid': 'str',
        'name': 'str',
        'display_text': 'str',
        'status': 'str',
        'classification_names': 'list[str]',
        'classifications': 'list[AtlasClassificationInfo]',
        'meaning_names': 'list[str]',
        'meanings': 'list[TermAssignmentHeader]',
        'children': 'object',
        'attributes': 'object'
    }

    attribute_map = {
        'type_name': 'type_name',
        'guid': 'guid',
        'name': 'name',
        'display_text': 'display_text',
        'status': 'status',
        'classification_names': 'classification_names',
        'classifications': 'classifications',
        'meaning_names': 'meaning_names',
        'meanings': 'meanings',
        'children': 'children',
        'attributes': 'attributes'
    }

    def __init__(self, type_name=None, guid=None, name=None, display_text=None, status=None, classification_names=None, classifications=None, meaning_names=None, meanings=None, children=None, attributes=None):
        """AtlasEntityHeader

        The model defined in huaweicloud sdk

        :param type_name: 类型名称
        :type type_name: str
        :param guid: guid
        :type guid: str
        :param name: 名称
        :type name: str
        :param display_text: 展示
        :type display_text: str
        :param status: 状态 枚举值：ACTIVE、DELETED
        :type status: str
        :param classification_names: 
        :type classification_names: list[str]
        :param classifications: 分类信息
        :type classifications: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasClassificationInfo`]
        :param meaning_names: 
        :type meaning_names: list[str]
        :param meanings: 关联任务
        :type meanings: list[:class:`huaweicloudsdkdataartsstudio.v1.TermAssignmentHeader`]
        :param children: 实体map Map&lt;String, AtlasEntityHeader&gt;
        :type children: object
        :param attributes: 实体map Map&lt;String, Object&gt;
        :type attributes: object
        """
        
        

        self._type_name = None
        self._guid = None
        self._name = None
        self._display_text = None
        self._status = None
        self._classification_names = None
        self._classifications = None
        self._meaning_names = None
        self._meanings = None
        self._children = None
        self._attributes = None
        self.discriminator = None

        if type_name is not None:
            self.type_name = type_name
        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if display_text is not None:
            self.display_text = display_text
        if status is not None:
            self.status = status
        if classification_names is not None:
            self.classification_names = classification_names
        if classifications is not None:
            self.classifications = classifications
        if meaning_names is not None:
            self.meaning_names = meaning_names
        if meanings is not None:
            self.meanings = meanings
        if children is not None:
            self.children = children
        if attributes is not None:
            self.attributes = attributes

    @property
    def type_name(self):
        """Gets the type_name of this AtlasEntityHeader.

        类型名称

        :return: The type_name of this AtlasEntityHeader.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this AtlasEntityHeader.

        类型名称

        :param type_name: The type_name of this AtlasEntityHeader.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def guid(self):
        """Gets the guid of this AtlasEntityHeader.

        guid

        :return: The guid of this AtlasEntityHeader.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this AtlasEntityHeader.

        guid

        :param guid: The guid of this AtlasEntityHeader.
        :type guid: str
        """
        self._guid = guid

    @property
    def name(self):
        """Gets the name of this AtlasEntityHeader.

        名称

        :return: The name of this AtlasEntityHeader.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AtlasEntityHeader.

        名称

        :param name: The name of this AtlasEntityHeader.
        :type name: str
        """
        self._name = name

    @property
    def display_text(self):
        """Gets the display_text of this AtlasEntityHeader.

        展示

        :return: The display_text of this AtlasEntityHeader.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this AtlasEntityHeader.

        展示

        :param display_text: The display_text of this AtlasEntityHeader.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def status(self):
        """Gets the status of this AtlasEntityHeader.

        状态 枚举值：ACTIVE、DELETED

        :return: The status of this AtlasEntityHeader.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AtlasEntityHeader.

        状态 枚举值：ACTIVE、DELETED

        :param status: The status of this AtlasEntityHeader.
        :type status: str
        """
        self._status = status

    @property
    def classification_names(self):
        """Gets the classification_names of this AtlasEntityHeader.

        :return: The classification_names of this AtlasEntityHeader.
        :rtype: list[str]
        """
        return self._classification_names

    @classification_names.setter
    def classification_names(self, classification_names):
        """Sets the classification_names of this AtlasEntityHeader.

        :param classification_names: The classification_names of this AtlasEntityHeader.
        :type classification_names: list[str]
        """
        self._classification_names = classification_names

    @property
    def classifications(self):
        """Gets the classifications of this AtlasEntityHeader.

        分类信息

        :return: The classifications of this AtlasEntityHeader.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasClassificationInfo`]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this AtlasEntityHeader.

        分类信息

        :param classifications: The classifications of this AtlasEntityHeader.
        :type classifications: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasClassificationInfo`]
        """
        self._classifications = classifications

    @property
    def meaning_names(self):
        """Gets the meaning_names of this AtlasEntityHeader.

        :return: The meaning_names of this AtlasEntityHeader.
        :rtype: list[str]
        """
        return self._meaning_names

    @meaning_names.setter
    def meaning_names(self, meaning_names):
        """Sets the meaning_names of this AtlasEntityHeader.

        :param meaning_names: The meaning_names of this AtlasEntityHeader.
        :type meaning_names: list[str]
        """
        self._meaning_names = meaning_names

    @property
    def meanings(self):
        """Gets the meanings of this AtlasEntityHeader.

        关联任务

        :return: The meanings of this AtlasEntityHeader.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TermAssignmentHeader`]
        """
        return self._meanings

    @meanings.setter
    def meanings(self, meanings):
        """Sets the meanings of this AtlasEntityHeader.

        关联任务

        :param meanings: The meanings of this AtlasEntityHeader.
        :type meanings: list[:class:`huaweicloudsdkdataartsstudio.v1.TermAssignmentHeader`]
        """
        self._meanings = meanings

    @property
    def children(self):
        """Gets the children of this AtlasEntityHeader.

        实体map Map<String, AtlasEntityHeader>

        :return: The children of this AtlasEntityHeader.
        :rtype: object
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this AtlasEntityHeader.

        实体map Map<String, AtlasEntityHeader>

        :param children: The children of this AtlasEntityHeader.
        :type children: object
        """
        self._children = children

    @property
    def attributes(self):
        """Gets the attributes of this AtlasEntityHeader.

        实体map Map<String, Object>

        :return: The attributes of this AtlasEntityHeader.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AtlasEntityHeader.

        实体map Map<String, Object>

        :param attributes: The attributes of this AtlasEntityHeader.
        :type attributes: object
        """
        self._attributes = attributes

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
        if not isinstance(other, AtlasEntityHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
