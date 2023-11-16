# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpenSourceStrategyResponse(SdkResponse):

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
        'level': 'str',
        'parent_id': 'str',
        'version': 'str',
        'is_valid': 'bool',
        'is_public': 'bool',
        'creator': 'str',
        'create_time': 'str',
        'updater': 'str',
        'update_time': 'str',
        'content': 'OpenSourceRuleContent'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'level': 'level',
        'parent_id': 'parent_id',
        'version': 'version',
        'is_valid': 'is_valid',
        'is_public': 'is_public',
        'creator': 'creator',
        'create_time': 'create_time',
        'updater': 'updater',
        'update_time': 'update_time',
        'content': 'content'
    }

    def __init__(self, id=None, name=None, level=None, parent_id=None, version=None, is_valid=None, is_public=None, creator=None, create_time=None, updater=None, update_time=None, content=None):
        """ShowOpenSourceStrategyResponse

        The model defined in huaweicloud sdk

        :param id: 策略ID
        :type id: str
        :param name: 策略名称
        :type name: str
        :param level: 策略级别
        :type level: str
        :param parent_id: 父策略ID
        :type parent_id: str
        :param version: 策略版本
        :type version: str
        :param is_valid: 是否启用
        :type is_valid: bool
        :param is_public: 是否系统级策略
        :type is_public: bool
        :param creator: 创建人
        :type creator: str
        :param create_time: 创建时间
        :type create_time: str
        :param updater: 更新人
        :type updater: str
        :param update_time: 更新时间
        :type update_time: str
        :param content: 
        :type content: :class:`huaweicloudsdkcodeartspipeline.v2.OpenSourceRuleContent`
        """
        
        super(ShowOpenSourceStrategyResponse, self).__init__()

        self._id = None
        self._name = None
        self._level = None
        self._parent_id = None
        self._version = None
        self._is_valid = None
        self._is_public = None
        self._creator = None
        self._create_time = None
        self._updater = None
        self._update_time = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if level is not None:
            self.level = level
        if parent_id is not None:
            self.parent_id = parent_id
        if version is not None:
            self.version = version
        if is_valid is not None:
            self.is_valid = is_valid
        if is_public is not None:
            self.is_public = is_public
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if updater is not None:
            self.updater = updater
        if update_time is not None:
            self.update_time = update_time
        if content is not None:
            self.content = content

    @property
    def id(self):
        """Gets the id of this ShowOpenSourceStrategyResponse.

        策略ID

        :return: The id of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowOpenSourceStrategyResponse.

        策略ID

        :param id: The id of this ShowOpenSourceStrategyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowOpenSourceStrategyResponse.

        策略名称

        :return: The name of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowOpenSourceStrategyResponse.

        策略名称

        :param name: The name of this ShowOpenSourceStrategyResponse.
        :type name: str
        """
        self._name = name

    @property
    def level(self):
        """Gets the level of this ShowOpenSourceStrategyResponse.

        策略级别

        :return: The level of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ShowOpenSourceStrategyResponse.

        策略级别

        :param level: The level of this ShowOpenSourceStrategyResponse.
        :type level: str
        """
        self._level = level

    @property
    def parent_id(self):
        """Gets the parent_id of this ShowOpenSourceStrategyResponse.

        父策略ID

        :return: The parent_id of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ShowOpenSourceStrategyResponse.

        父策略ID

        :param parent_id: The parent_id of this ShowOpenSourceStrategyResponse.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def version(self):
        """Gets the version of this ShowOpenSourceStrategyResponse.

        策略版本

        :return: The version of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowOpenSourceStrategyResponse.

        策略版本

        :param version: The version of this ShowOpenSourceStrategyResponse.
        :type version: str
        """
        self._version = version

    @property
    def is_valid(self):
        """Gets the is_valid of this ShowOpenSourceStrategyResponse.

        是否启用

        :return: The is_valid of this ShowOpenSourceStrategyResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this ShowOpenSourceStrategyResponse.

        是否启用

        :param is_valid: The is_valid of this ShowOpenSourceStrategyResponse.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def is_public(self):
        """Gets the is_public of this ShowOpenSourceStrategyResponse.

        是否系统级策略

        :return: The is_public of this ShowOpenSourceStrategyResponse.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ShowOpenSourceStrategyResponse.

        是否系统级策略

        :param is_public: The is_public of this ShowOpenSourceStrategyResponse.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def creator(self):
        """Gets the creator of this ShowOpenSourceStrategyResponse.

        创建人

        :return: The creator of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowOpenSourceStrategyResponse.

        创建人

        :param creator: The creator of this ShowOpenSourceStrategyResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this ShowOpenSourceStrategyResponse.

        创建时间

        :return: The create_time of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowOpenSourceStrategyResponse.

        创建时间

        :param create_time: The create_time of this ShowOpenSourceStrategyResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def updater(self):
        """Gets the updater of this ShowOpenSourceStrategyResponse.

        更新人

        :return: The updater of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        """Sets the updater of this ShowOpenSourceStrategyResponse.

        更新人

        :param updater: The updater of this ShowOpenSourceStrategyResponse.
        :type updater: str
        """
        self._updater = updater

    @property
    def update_time(self):
        """Gets the update_time of this ShowOpenSourceStrategyResponse.

        更新时间

        :return: The update_time of this ShowOpenSourceStrategyResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowOpenSourceStrategyResponse.

        更新时间

        :param update_time: The update_time of this ShowOpenSourceStrategyResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def content(self):
        """Gets the content of this ShowOpenSourceStrategyResponse.

        :return: The content of this ShowOpenSourceStrategyResponse.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.OpenSourceRuleContent`
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ShowOpenSourceStrategyResponse.

        :param content: The content of this ShowOpenSourceStrategyResponse.
        :type content: :class:`huaweicloudsdkcodeartspipeline.v2.OpenSourceRuleContent`
        """
        self._content = content

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
        if not isinstance(other, ShowOpenSourceStrategyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
