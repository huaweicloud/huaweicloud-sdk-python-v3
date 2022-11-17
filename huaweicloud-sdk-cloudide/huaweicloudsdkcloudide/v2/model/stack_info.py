# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arm_config': 'StacksConfig',
        'bundle_url': 'str',
        'config': 'StacksConfig',
        'created_time': 'datetime',
        'delete': 'bool',
        'description': 'str',
        'disable': 'bool',
        'display_name': 'str',
        'id': 'int',
        'label': 'str',
        'logo': 'str',
        'region': 'str',
        'show': 'bool',
        'stack_name': 'str',
        'tags': 'list[str]',
        'updated_time': 'datetime',
        'users': 'list[str]'
    }

    attribute_map = {
        'arm_config': 'arm_config',
        'bundle_url': 'bundle_url',
        'config': 'config',
        'created_time': 'created_time',
        'delete': 'delete',
        'description': 'description',
        'disable': 'disable',
        'display_name': 'display_name',
        'id': 'id',
        'label': 'label',
        'logo': 'logo',
        'region': 'region',
        'show': 'show',
        'stack_name': 'stack_name',
        'tags': 'tags',
        'updated_time': 'updated_time',
        'users': 'users'
    }

    def __init__(self, arm_config=None, bundle_url=None, config=None, created_time=None, delete=None, description=None, disable=None, display_name=None, id=None, label=None, logo=None, region=None, show=None, stack_name=None, tags=None, updated_time=None, users=None):
        """StackInfo

        The model defined in huaweicloud sdk

        :param arm_config: 
        :type arm_config: :class:`huaweicloudsdkcloudide.v2.StacksConfig`
        :param bundle_url: bundleUrl
        :type bundle_url: str
        :param config: 
        :type config: :class:`huaweicloudsdkcloudide.v2.StacksConfig`
        :param created_time: 创建时间
        :type created_time: datetime
        :param delete: 是否删除
        :type delete: bool
        :param description: 描述
        :type description: str
        :param disable: 是否可用
        :type disable: bool
        :param display_name: 显示名称
        :type display_name: str
        :param id: id
        :type id: int
        :param label: 标签
        :type label: str
        :param logo: 图标
        :type logo: str
        :param region: region
        :type region: str
        :param show: 是否显示
        :type show: bool
        :param stack_name: 技术栈名称
        :type stack_name: str
        :param tags: tags
        :type tags: list[str]
        :param updated_time: 修改时间
        :type updated_time: datetime
        :param users: 使用者
        :type users: list[str]
        """
        
        

        self._arm_config = None
        self._bundle_url = None
        self._config = None
        self._created_time = None
        self._delete = None
        self._description = None
        self._disable = None
        self._display_name = None
        self._id = None
        self._label = None
        self._logo = None
        self._region = None
        self._show = None
        self._stack_name = None
        self._tags = None
        self._updated_time = None
        self._users = None
        self.discriminator = None

        if arm_config is not None:
            self.arm_config = arm_config
        if bundle_url is not None:
            self.bundle_url = bundle_url
        if config is not None:
            self.config = config
        if created_time is not None:
            self.created_time = created_time
        if delete is not None:
            self.delete = delete
        if description is not None:
            self.description = description
        if disable is not None:
            self.disable = disable
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if logo is not None:
            self.logo = logo
        if region is not None:
            self.region = region
        if show is not None:
            self.show = show
        if stack_name is not None:
            self.stack_name = stack_name
        if tags is not None:
            self.tags = tags
        if updated_time is not None:
            self.updated_time = updated_time
        if users is not None:
            self.users = users

    @property
    def arm_config(self):
        """Gets the arm_config of this StackInfo.

        :return: The arm_config of this StackInfo.
        :rtype: :class:`huaweicloudsdkcloudide.v2.StacksConfig`
        """
        return self._arm_config

    @arm_config.setter
    def arm_config(self, arm_config):
        """Sets the arm_config of this StackInfo.

        :param arm_config: The arm_config of this StackInfo.
        :type arm_config: :class:`huaweicloudsdkcloudide.v2.StacksConfig`
        """
        self._arm_config = arm_config

    @property
    def bundle_url(self):
        """Gets the bundle_url of this StackInfo.

        bundleUrl

        :return: The bundle_url of this StackInfo.
        :rtype: str
        """
        return self._bundle_url

    @bundle_url.setter
    def bundle_url(self, bundle_url):
        """Sets the bundle_url of this StackInfo.

        bundleUrl

        :param bundle_url: The bundle_url of this StackInfo.
        :type bundle_url: str
        """
        self._bundle_url = bundle_url

    @property
    def config(self):
        """Gets the config of this StackInfo.

        :return: The config of this StackInfo.
        :rtype: :class:`huaweicloudsdkcloudide.v2.StacksConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this StackInfo.

        :param config: The config of this StackInfo.
        :type config: :class:`huaweicloudsdkcloudide.v2.StacksConfig`
        """
        self._config = config

    @property
    def created_time(self):
        """Gets the created_time of this StackInfo.

        创建时间

        :return: The created_time of this StackInfo.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this StackInfo.

        创建时间

        :param created_time: The created_time of this StackInfo.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def delete(self):
        """Gets the delete of this StackInfo.

        是否删除

        :return: The delete of this StackInfo.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this StackInfo.

        是否删除

        :param delete: The delete of this StackInfo.
        :type delete: bool
        """
        self._delete = delete

    @property
    def description(self):
        """Gets the description of this StackInfo.

        描述

        :return: The description of this StackInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StackInfo.

        描述

        :param description: The description of this StackInfo.
        :type description: str
        """
        self._description = description

    @property
    def disable(self):
        """Gets the disable of this StackInfo.

        是否可用

        :return: The disable of this StackInfo.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        """Sets the disable of this StackInfo.

        是否可用

        :param disable: The disable of this StackInfo.
        :type disable: bool
        """
        self._disable = disable

    @property
    def display_name(self):
        """Gets the display_name of this StackInfo.

        显示名称

        :return: The display_name of this StackInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this StackInfo.

        显示名称

        :param display_name: The display_name of this StackInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this StackInfo.

        id

        :return: The id of this StackInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StackInfo.

        id

        :param id: The id of this StackInfo.
        :type id: int
        """
        self._id = id

    @property
    def label(self):
        """Gets the label of this StackInfo.

        标签

        :return: The label of this StackInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this StackInfo.

        标签

        :param label: The label of this StackInfo.
        :type label: str
        """
        self._label = label

    @property
    def logo(self):
        """Gets the logo of this StackInfo.

        图标

        :return: The logo of this StackInfo.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this StackInfo.

        图标

        :param logo: The logo of this StackInfo.
        :type logo: str
        """
        self._logo = logo

    @property
    def region(self):
        """Gets the region of this StackInfo.

        region

        :return: The region of this StackInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this StackInfo.

        region

        :param region: The region of this StackInfo.
        :type region: str
        """
        self._region = region

    @property
    def show(self):
        """Gets the show of this StackInfo.

        是否显示

        :return: The show of this StackInfo.
        :rtype: bool
        """
        return self._show

    @show.setter
    def show(self, show):
        """Sets the show of this StackInfo.

        是否显示

        :param show: The show of this StackInfo.
        :type show: bool
        """
        self._show = show

    @property
    def stack_name(self):
        """Gets the stack_name of this StackInfo.

        技术栈名称

        :return: The stack_name of this StackInfo.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this StackInfo.

        技术栈名称

        :param stack_name: The stack_name of this StackInfo.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def tags(self):
        """Gets the tags of this StackInfo.

        tags

        :return: The tags of this StackInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StackInfo.

        tags

        :param tags: The tags of this StackInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def updated_time(self):
        """Gets the updated_time of this StackInfo.

        修改时间

        :return: The updated_time of this StackInfo.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this StackInfo.

        修改时间

        :param updated_time: The updated_time of this StackInfo.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def users(self):
        """Gets the users of this StackInfo.

        使用者

        :return: The users of this StackInfo.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this StackInfo.

        使用者

        :param users: The users of this StackInfo.
        :type users: list[str]
        """
        self._users = users

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
        if not isinstance(other, StackInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
