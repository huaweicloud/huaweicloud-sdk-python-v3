# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppResp:


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
        'alias': 'str',
        'description': 'str',
        'icon_url': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'visibility': 'str',
        'app_versions': 'list[AppVersionDetail]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'alias': 'alias',
        'description': 'description',
        'icon_url': 'icon_url',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'visibility': 'visibility',
        'app_versions': 'app_versions'
    }

    def __init__(self, id=None, name=None, alias=None, description=None, icon_url=None, created_at=None, updated_at=None, project_id=None, visibility=None, app_versions=None):
        """AppResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._alias = None
        self._description = None
        self._icon_url = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._visibility = None
        self._app_versions = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.alias = alias
        self.description = description
        self.icon_url = icon_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.project_id = project_id
        self.visibility = visibility
        self.app_versions = app_versions

    @property
    def id(self):
        """Gets the id of this AppResp.

        应用模板ID

        :return: The id of this AppResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppResp.

        应用模板ID

        :param id: The id of this AppResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AppResp.

        应用模板名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾 Name为必填字段，且本租户中唯一

        :return: The name of this AppResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppResp.

        应用模板名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾 Name为必填字段，且本租户中唯一

        :param name: The name of this AppResp.
        :type: str
        """
        self._name = name

    @property
    def alias(self):
        """Gets the alias of this AppResp.

        应用模板别名，中文英文字母、数字、中划线、下划线，最大64字符

        :return: The alias of this AppResp.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AppResp.

        应用模板别名，中文英文字母、数字、中划线、下划线，最大64字符

        :param alias: The alias of this AppResp.
        :type: str
        """
        self._alias = alias

    @property
    def description(self):
        """Gets the description of this AppResp.

        应用模板描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this AppResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppResp.

        应用模板描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this AppResp.
        :type: str
        """
        self._description = description

    @property
    def icon_url(self):
        """Gets the icon_url of this AppResp.

        应用图标存储url地址，最大长度2083

        :return: The icon_url of this AppResp.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this AppResp.

        应用图标存储url地址，最大长度2083

        :param icon_url: The icon_url of this AppResp.
        :type: str
        """
        self._icon_url = icon_url

    @property
    def created_at(self):
        """Gets the created_at of this AppResp.

        创建时间

        :return: The created_at of this AppResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AppResp.

        创建时间

        :param created_at: The created_at of this AppResp.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AppResp.

        更新时间

        :return: The updated_at of this AppResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AppResp.

        更新时间

        :param updated_at: The updated_at of this AppResp.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this AppResp.

        项目ID

        :return: The project_id of this AppResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AppResp.

        项目ID

        :param project_id: The project_id of this AppResp.
        :type: str
        """
        self._project_id = project_id

    @property
    def visibility(self):
        """Gets the visibility of this AppResp.

        模板类型

        :return: The visibility of this AppResp.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this AppResp.

        模板类型

        :param visibility: The visibility of this AppResp.
        :type: str
        """
        self._visibility = visibility

    @property
    def app_versions(self):
        """Gets the app_versions of this AppResp.

        app详情

        :return: The app_versions of this AppResp.
        :rtype: list[AppVersionDetail]
        """
        return self._app_versions

    @app_versions.setter
    def app_versions(self, app_versions):
        """Sets the app_versions of this AppResp.

        app详情

        :param app_versions: The app_versions of this AppResp.
        :type: list[AppVersionDetail]
        """
        self._app_versions = app_versions

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
        if not isinstance(other, AppResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other