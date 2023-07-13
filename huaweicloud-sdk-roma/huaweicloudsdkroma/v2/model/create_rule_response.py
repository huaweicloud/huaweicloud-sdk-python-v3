# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[str]',
        'rule_id': 'int',
        'name': 'str',
        'app_id': 'str',
        'description': 'str',
        'status': 'int',
        'data_parsing_status': 'int',
        'created_user': 'CreatedUser',
        'last_updated_user': 'LastUpdatedUser',
        'created_datetime': 'int',
        'last_updated_datetime': 'int'
    }

    attribute_map = {
        'permissions': 'permissions',
        'rule_id': 'rule_id',
        'name': 'name',
        'app_id': 'app_id',
        'description': 'description',
        'status': 'status',
        'data_parsing_status': 'data_parsing_status',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'created_datetime': 'created_datetime',
        'last_updated_datetime': 'last_updated_datetime'
    }

    def __init__(self, permissions=None, rule_id=None, name=None, app_id=None, description=None, status=None, data_parsing_status=None, created_user=None, last_updated_user=None, created_datetime=None, last_updated_datetime=None):
        """CreateRuleResponse

        The model defined in huaweicloud sdk

        :param permissions: 权限
        :type permissions: list[str]
        :param rule_id: 规则ID
        :type rule_id: int
        :param name: 规则名称，支持英文大小写，数字，下划线和中划线,长度1-64
        :type name: str
        :param app_id: 应用ID
        :type app_id: str
        :param description: 描述
        :type description: str
        :param status: 规则状态 0-启用 1-停用
        :type status: int
        :param data_parsing_status: 数据解析状态，ENABLE时data_parsing必填 0-启用 1-停用
        :type data_parsing_status: int
        :param created_user: 
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        :param last_updated_user: 
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        :param created_datetime: 创建时间，timestamp(ms)，使用UTC时区
        :type created_datetime: int
        :param last_updated_datetime: 最后修改时间，timestamp(ms)，使用UTC时区
        :type last_updated_datetime: int
        """
        
        super(CreateRuleResponse, self).__init__()

        self._permissions = None
        self._rule_id = None
        self._name = None
        self._app_id = None
        self._description = None
        self._status = None
        self._data_parsing_status = None
        self._created_user = None
        self._last_updated_user = None
        self._created_datetime = None
        self._last_updated_datetime = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if rule_id is not None:
            self.rule_id = rule_id
        if name is not None:
            self.name = name
        if app_id is not None:
            self.app_id = app_id
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if data_parsing_status is not None:
            self.data_parsing_status = data_parsing_status
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if last_updated_datetime is not None:
            self.last_updated_datetime = last_updated_datetime

    @property
    def permissions(self):
        """Gets the permissions of this CreateRuleResponse.

        权限

        :return: The permissions of this CreateRuleResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CreateRuleResponse.

        权限

        :param permissions: The permissions of this CreateRuleResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def rule_id(self):
        """Gets the rule_id of this CreateRuleResponse.

        规则ID

        :return: The rule_id of this CreateRuleResponse.
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CreateRuleResponse.

        规则ID

        :param rule_id: The rule_id of this CreateRuleResponse.
        :type rule_id: int
        """
        self._rule_id = rule_id

    @property
    def name(self):
        """Gets the name of this CreateRuleResponse.

        规则名称，支持英文大小写，数字，下划线和中划线,长度1-64

        :return: The name of this CreateRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRuleResponse.

        规则名称，支持英文大小写，数字，下划线和中划线,长度1-64

        :param name: The name of this CreateRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def app_id(self):
        """Gets the app_id of this CreateRuleResponse.

        应用ID

        :return: The app_id of this CreateRuleResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateRuleResponse.

        应用ID

        :param app_id: The app_id of this CreateRuleResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def description(self):
        """Gets the description of this CreateRuleResponse.

        描述

        :return: The description of this CreateRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRuleResponse.

        描述

        :param description: The description of this CreateRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateRuleResponse.

        规则状态 0-启用 1-停用

        :return: The status of this CreateRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRuleResponse.

        规则状态 0-启用 1-停用

        :param status: The status of this CreateRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def data_parsing_status(self):
        """Gets the data_parsing_status of this CreateRuleResponse.

        数据解析状态，ENABLE时data_parsing必填 0-启用 1-停用

        :return: The data_parsing_status of this CreateRuleResponse.
        :rtype: int
        """
        return self._data_parsing_status

    @data_parsing_status.setter
    def data_parsing_status(self, data_parsing_status):
        """Sets the data_parsing_status of this CreateRuleResponse.

        数据解析状态，ENABLE时data_parsing必填 0-启用 1-停用

        :param data_parsing_status: The data_parsing_status of this CreateRuleResponse.
        :type data_parsing_status: int
        """
        self._data_parsing_status = data_parsing_status

    @property
    def created_user(self):
        """Gets the created_user of this CreateRuleResponse.

        :return: The created_user of this CreateRuleResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        """Sets the created_user of this CreateRuleResponse.

        :param created_user: The created_user of this CreateRuleResponse.
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this CreateRuleResponse.

        :return: The last_updated_user of this CreateRuleResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this CreateRuleResponse.

        :param last_updated_user: The last_updated_user of this CreateRuleResponse.
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        self._last_updated_user = last_updated_user

    @property
    def created_datetime(self):
        """Gets the created_datetime of this CreateRuleResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :return: The created_datetime of this CreateRuleResponse.
        :rtype: int
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this CreateRuleResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :param created_datetime: The created_datetime of this CreateRuleResponse.
        :type created_datetime: int
        """
        self._created_datetime = created_datetime

    @property
    def last_updated_datetime(self):
        """Gets the last_updated_datetime of this CreateRuleResponse.

        最后修改时间，timestamp(ms)，使用UTC时区

        :return: The last_updated_datetime of this CreateRuleResponse.
        :rtype: int
        """
        return self._last_updated_datetime

    @last_updated_datetime.setter
    def last_updated_datetime(self, last_updated_datetime):
        """Sets the last_updated_datetime of this CreateRuleResponse.

        最后修改时间，timestamp(ms)，使用UTC时区

        :param last_updated_datetime: The last_updated_datetime of this CreateRuleResponse.
        :type last_updated_datetime: int
        """
        self._last_updated_datetime = last_updated_datetime

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
        if not isinstance(other, CreateRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
