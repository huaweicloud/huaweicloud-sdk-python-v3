# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtlasAssetEntity:

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
        'version': 'int',
        'update_time': 'float',
        'update_user': 'str',
        'create_time': 'float',
        'create_user': 'str',
        'display_text': 'str',
        'status': 'str',
        'classifications': 'list[AtlasClassificationInfo]',
        'meanings': 'list[TermAssignmentHeader]',
        'relation_ship_attributes': 'object',
        'attributes': 'object'
    }

    attribute_map = {
        'type_name': 'type_name',
        'guid': 'guid',
        'version': 'version',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'display_text': 'display_text',
        'status': 'status',
        'classifications': 'classifications',
        'meanings': 'meanings',
        'relation_ship_attributes': 'relation_ship_attributes',
        'attributes': 'attributes'
    }

    def __init__(self, type_name=None, guid=None, version=None, update_time=None, update_user=None, create_time=None, create_user=None, display_text=None, status=None, classifications=None, meanings=None, relation_ship_attributes=None, attributes=None):
        """AtlasAssetEntity

        The model defined in huaweicloud sdk

        :param type_name: 类型名称
        :type type_name: str
        :param guid: guid
        :type guid: str
        :param version: 版本
        :type version: int
        :param update_time: 修改时间
        :type update_time: float
        :param update_user: 修改人
        :type update_user: str
        :param create_time: 创建时间
        :type create_time: float
        :param create_user: 创建人
        :type create_user: str
        :param display_text: 展示
        :type display_text: str
        :param status: 状态 枚举值：ACTIVE、DELETED
        :type status: str
        :param classifications: 分类信息
        :type classifications: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasClassificationInfo`]
        :param meanings: 关联任务
        :type meanings: list[:class:`huaweicloudsdkdataartsstudio.v1.TermAssignmentHeader`]
        :param relation_ship_attributes: 实体map Map&lt;String, Object&gt;
        :type relation_ship_attributes: object
        :param attributes: 实体map Map&lt;String, Object&gt;
        :type attributes: object
        """
        
        

        self._type_name = None
        self._guid = None
        self._version = None
        self._update_time = None
        self._update_user = None
        self._create_time = None
        self._create_user = None
        self._display_text = None
        self._status = None
        self._classifications = None
        self._meanings = None
        self._relation_ship_attributes = None
        self._attributes = None
        self.discriminator = None

        self.type_name = type_name
        if guid is not None:
            self.guid = guid
        if version is not None:
            self.version = version
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if display_text is not None:
            self.display_text = display_text
        if status is not None:
            self.status = status
        if classifications is not None:
            self.classifications = classifications
        if meanings is not None:
            self.meanings = meanings
        if relation_ship_attributes is not None:
            self.relation_ship_attributes = relation_ship_attributes
        self.attributes = attributes

    @property
    def type_name(self):
        """Gets the type_name of this AtlasAssetEntity.

        类型名称

        :return: The type_name of this AtlasAssetEntity.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this AtlasAssetEntity.

        类型名称

        :param type_name: The type_name of this AtlasAssetEntity.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def guid(self):
        """Gets the guid of this AtlasAssetEntity.

        guid

        :return: The guid of this AtlasAssetEntity.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this AtlasAssetEntity.

        guid

        :param guid: The guid of this AtlasAssetEntity.
        :type guid: str
        """
        self._guid = guid

    @property
    def version(self):
        """Gets the version of this AtlasAssetEntity.

        版本

        :return: The version of this AtlasAssetEntity.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AtlasAssetEntity.

        版本

        :param version: The version of this AtlasAssetEntity.
        :type version: int
        """
        self._version = version

    @property
    def update_time(self):
        """Gets the update_time of this AtlasAssetEntity.

        修改时间

        :return: The update_time of this AtlasAssetEntity.
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AtlasAssetEntity.

        修改时间

        :param update_time: The update_time of this AtlasAssetEntity.
        :type update_time: float
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this AtlasAssetEntity.

        修改人

        :return: The update_user of this AtlasAssetEntity.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this AtlasAssetEntity.

        修改人

        :param update_user: The update_user of this AtlasAssetEntity.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def create_time(self):
        """Gets the create_time of this AtlasAssetEntity.

        创建时间

        :return: The create_time of this AtlasAssetEntity.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AtlasAssetEntity.

        创建时间

        :param create_time: The create_time of this AtlasAssetEntity.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this AtlasAssetEntity.

        创建人

        :return: The create_user of this AtlasAssetEntity.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this AtlasAssetEntity.

        创建人

        :param create_user: The create_user of this AtlasAssetEntity.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def display_text(self):
        """Gets the display_text of this AtlasAssetEntity.

        展示

        :return: The display_text of this AtlasAssetEntity.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this AtlasAssetEntity.

        展示

        :param display_text: The display_text of this AtlasAssetEntity.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def status(self):
        """Gets the status of this AtlasAssetEntity.

        状态 枚举值：ACTIVE、DELETED

        :return: The status of this AtlasAssetEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AtlasAssetEntity.

        状态 枚举值：ACTIVE、DELETED

        :param status: The status of this AtlasAssetEntity.
        :type status: str
        """
        self._status = status

    @property
    def classifications(self):
        """Gets the classifications of this AtlasAssetEntity.

        分类信息

        :return: The classifications of this AtlasAssetEntity.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasClassificationInfo`]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this AtlasAssetEntity.

        分类信息

        :param classifications: The classifications of this AtlasAssetEntity.
        :type classifications: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasClassificationInfo`]
        """
        self._classifications = classifications

    @property
    def meanings(self):
        """Gets the meanings of this AtlasAssetEntity.

        关联任务

        :return: The meanings of this AtlasAssetEntity.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TermAssignmentHeader`]
        """
        return self._meanings

    @meanings.setter
    def meanings(self, meanings):
        """Sets the meanings of this AtlasAssetEntity.

        关联任务

        :param meanings: The meanings of this AtlasAssetEntity.
        :type meanings: list[:class:`huaweicloudsdkdataartsstudio.v1.TermAssignmentHeader`]
        """
        self._meanings = meanings

    @property
    def relation_ship_attributes(self):
        """Gets the relation_ship_attributes of this AtlasAssetEntity.

        实体map Map<String, Object>

        :return: The relation_ship_attributes of this AtlasAssetEntity.
        :rtype: object
        """
        return self._relation_ship_attributes

    @relation_ship_attributes.setter
    def relation_ship_attributes(self, relation_ship_attributes):
        """Sets the relation_ship_attributes of this AtlasAssetEntity.

        实体map Map<String, Object>

        :param relation_ship_attributes: The relation_ship_attributes of this AtlasAssetEntity.
        :type relation_ship_attributes: object
        """
        self._relation_ship_attributes = relation_ship_attributes

    @property
    def attributes(self):
        """Gets the attributes of this AtlasAssetEntity.

        实体map Map<String, Object>

        :return: The attributes of this AtlasAssetEntity.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AtlasAssetEntity.

        实体map Map<String, Object>

        :param attributes: The attributes of this AtlasAssetEntity.
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
        if not isinstance(other, AtlasAssetEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
