# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StyleInfo:

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
        'description': 'str',
        'project_id': 'str',
        'status': 'str',
        'sex': 'str',
        'tags': 'list[str]',
        'style_assets': 'list[StyleAssetItem]',
        'extra_meta': 'StyleExtraMeta',
        'style_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'status': 'status',
        'sex': 'sex',
        'tags': 'tags',
        'style_assets': 'style_assets',
        'extra_meta': 'extra_meta',
        'style_id': 'style_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'state': 'state'
    }

    def __init__(self, name=None, description=None, project_id=None, status=None, sex=None, tags=None, style_assets=None, extra_meta=None, style_id=None, create_time=None, update_time=None, state=None):
        """StyleInfo

        The model defined in huaweicloud sdk

        :param name: 数字人风格化名称
        :type name: str
        :param description: 数字人风格化描述
        :type description: str
        :param project_id: 租户ID
        :type project_id: str
        :param status: 状态
        :type status: str
        :param sex: 性别
        :type sex: str
        :param tags: 标签。单个标签16字节，多个用逗号分隔，最多50个。
        :type tags: list[str]
        :param style_assets: 风格化素材资产组合。
        :type style_assets: list[:class:`huaweicloudsdkmetastudio.v1.StyleAssetItem`]
        :param extra_meta: 
        :type extra_meta: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMeta`
        :param style_id: 数字人风格ID
        :type style_id: str
        :param create_time: 数字人风格创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type create_time: str
        :param update_time: 数字人风格更新时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type update_time: str
        :param state: 数字人风格状态枚举 * CREATING：创建中 * PUBLISHED：已发布 * DELETED：已删除 * UNPUBLISHED：未发布 * PUBLISHING：发布中
        :type state: str
        """
        
        

        self._name = None
        self._description = None
        self._project_id = None
        self._status = None
        self._sex = None
        self._tags = None
        self._style_assets = None
        self._extra_meta = None
        self._style_id = None
        self._create_time = None
        self._update_time = None
        self._state = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if sex is not None:
            self.sex = sex
        if tags is not None:
            self.tags = tags
        if style_assets is not None:
            self.style_assets = style_assets
        if extra_meta is not None:
            self.extra_meta = extra_meta
        if style_id is not None:
            self.style_id = style_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if state is not None:
            self.state = state

    @property
    def name(self):
        """Gets the name of this StyleInfo.

        数字人风格化名称

        :return: The name of this StyleInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StyleInfo.

        数字人风格化名称

        :param name: The name of this StyleInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this StyleInfo.

        数字人风格化描述

        :return: The description of this StyleInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StyleInfo.

        数字人风格化描述

        :param description: The description of this StyleInfo.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this StyleInfo.

        租户ID

        :return: The project_id of this StyleInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this StyleInfo.

        租户ID

        :param project_id: The project_id of this StyleInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this StyleInfo.

        状态

        :return: The status of this StyleInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StyleInfo.

        状态

        :param status: The status of this StyleInfo.
        :type status: str
        """
        self._status = status

    @property
    def sex(self):
        """Gets the sex of this StyleInfo.

        性别

        :return: The sex of this StyleInfo.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this StyleInfo.

        性别

        :param sex: The sex of this StyleInfo.
        :type sex: str
        """
        self._sex = sex

    @property
    def tags(self):
        """Gets the tags of this StyleInfo.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :return: The tags of this StyleInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StyleInfo.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :param tags: The tags of this StyleInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def style_assets(self):
        """Gets the style_assets of this StyleInfo.

        风格化素材资产组合。

        :return: The style_assets of this StyleInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.StyleAssetItem`]
        """
        return self._style_assets

    @style_assets.setter
    def style_assets(self, style_assets):
        """Sets the style_assets of this StyleInfo.

        风格化素材资产组合。

        :param style_assets: The style_assets of this StyleInfo.
        :type style_assets: list[:class:`huaweicloudsdkmetastudio.v1.StyleAssetItem`]
        """
        self._style_assets = style_assets

    @property
    def extra_meta(self):
        """Gets the extra_meta of this StyleInfo.

        :return: The extra_meta of this StyleInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMeta`
        """
        return self._extra_meta

    @extra_meta.setter
    def extra_meta(self, extra_meta):
        """Sets the extra_meta of this StyleInfo.

        :param extra_meta: The extra_meta of this StyleInfo.
        :type extra_meta: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMeta`
        """
        self._extra_meta = extra_meta

    @property
    def style_id(self):
        """Gets the style_id of this StyleInfo.

        数字人风格ID

        :return: The style_id of this StyleInfo.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this StyleInfo.

        数字人风格ID

        :param style_id: The style_id of this StyleInfo.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def create_time(self):
        """Gets the create_time of this StyleInfo.

        数字人风格创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The create_time of this StyleInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StyleInfo.

        数字人风格创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param create_time: The create_time of this StyleInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this StyleInfo.

        数字人风格更新时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The update_time of this StyleInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this StyleInfo.

        数字人风格更新时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param update_time: The update_time of this StyleInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        """Gets the state of this StyleInfo.

        数字人风格状态枚举 * CREATING：创建中 * PUBLISHED：已发布 * DELETED：已删除 * UNPUBLISHED：未发布 * PUBLISHING：发布中

        :return: The state of this StyleInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StyleInfo.

        数字人风格状态枚举 * CREATING：创建中 * PUBLISHED：已发布 * DELETED：已删除 * UNPUBLISHED：未发布 * PUBLISHING：发布中

        :param state: The state of this StyleInfo.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, StyleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
