# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppListDto:

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
        'version': 'str',
        'summary': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'user_name': 'str',
        'source_project_name': 'str',
        'source_resource_id': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'summary': 'summary',
        'description': 'description',
        'labels': 'labels',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'user_name': 'user_name',
        'source_project_name': 'source_project_name',
        'source_resource_id': 'source_resource_id',
        'icon': 'icon'
    }

    def __init__(self, id=None, name=None, version=None, summary=None, description=None, labels=None, create_time=None, update_time=None, user_name=None, source_project_name=None, source_resource_id=None, icon=None):
        r"""AppListDto

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param version: 应用版本
        :type version: str
        :param summary: 应用简述
        :type summary: str
        :param description: 应用描述
        :type description: str
        :param labels: 应用标签
        :type labels: list[str]
        :param create_time: 创建应用时间
        :type create_time: str
        :param update_time: 更新应用时间
        :type update_time: str
        :param user_name: 创建应用的用户名
        :type user_name: str
        :param source_project_name: 源项目名称
        :type source_project_name: str
        :param source_resource_id: 源资源id
        :type source_resource_id: str
        :param icon: 图标base64编码
        :type icon: str
        """
        
        

        self._id = None
        self._name = None
        self._version = None
        self._summary = None
        self._description = None
        self._labels = None
        self._create_time = None
        self._update_time = None
        self._user_name = None
        self._source_project_name = None
        self._source_resource_id = None
        self._icon = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if user_name is not None:
            self.user_name = user_name
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_resource_id is not None:
            self.source_resource_id = source_resource_id
        if icon is not None:
            self.icon = icon

    @property
    def id(self):
        r"""Gets the id of this AppListDto.

        应用id

        :return: The id of this AppListDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AppListDto.

        应用id

        :param id: The id of this AppListDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AppListDto.

        应用名称

        :return: The name of this AppListDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AppListDto.

        应用名称

        :param name: The name of this AppListDto.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this AppListDto.

        应用版本

        :return: The version of this AppListDto.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AppListDto.

        应用版本

        :param version: The version of this AppListDto.
        :type version: str
        """
        self._version = version

    @property
    def summary(self):
        r"""Gets the summary of this AppListDto.

        应用简述

        :return: The summary of this AppListDto.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this AppListDto.

        应用简述

        :param summary: The summary of this AppListDto.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        r"""Gets the description of this AppListDto.

        应用描述

        :return: The description of this AppListDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AppListDto.

        应用描述

        :param description: The description of this AppListDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this AppListDto.

        应用标签

        :return: The labels of this AppListDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this AppListDto.

        应用标签

        :param labels: The labels of this AppListDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def create_time(self):
        r"""Gets the create_time of this AppListDto.

        创建应用时间

        :return: The create_time of this AppListDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AppListDto.

        创建应用时间

        :param create_time: The create_time of this AppListDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AppListDto.

        更新应用时间

        :return: The update_time of this AppListDto.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AppListDto.

        更新应用时间

        :param update_time: The update_time of this AppListDto.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def user_name(self):
        r"""Gets the user_name of this AppListDto.

        创建应用的用户名

        :return: The user_name of this AppListDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AppListDto.

        创建应用的用户名

        :param user_name: The user_name of this AppListDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def source_project_name(self):
        r"""Gets the source_project_name of this AppListDto.

        源项目名称

        :return: The source_project_name of this AppListDto.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        r"""Sets the source_project_name of this AppListDto.

        源项目名称

        :param source_project_name: The source_project_name of this AppListDto.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_resource_id(self):
        r"""Gets the source_resource_id of this AppListDto.

        源资源id

        :return: The source_resource_id of this AppListDto.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        r"""Sets the source_resource_id of this AppListDto.

        源资源id

        :param source_resource_id: The source_resource_id of this AppListDto.
        :type source_resource_id: str
        """
        self._source_resource_id = source_resource_id

    @property
    def icon(self):
        r"""Gets the icon of this AppListDto.

        图标base64编码

        :return: The icon of this AppListDto.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this AppListDto.

        图标base64编码

        :param icon: The icon of this AppListDto.
        :type icon: str
        """
        self._icon = icon

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
        if not isinstance(other, AppListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
