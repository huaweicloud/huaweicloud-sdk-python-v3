# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppGroupReq:

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
        'app_server_group_id': 'str',
        'description': 'str',
        'authorization_type': 'AuthorizationTypeEnum',
        'app_type': 'AppTypeEnum'
    }

    attribute_map = {
        'name': 'name',
        'app_server_group_id': 'app_server_group_id',
        'description': 'description',
        'authorization_type': 'authorization_type',
        'app_type': 'app_type'
    }

    def __init__(self, name=None, app_server_group_id=None, description=None, authorization_type=None, app_type=None):
        """CreateAppGroupReq

        The model defined in huaweicloud sdk

        :param name: 应用组名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成 2. 长度范围1~64个字符
        :type name: str
        :param app_server_group_id: 应用服务器组ID
        :type app_server_group_id: str
        :param description: 应用组描述
        :type description: str
        :param authorization_type: 
        :type authorization_type: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizationTypeEnum`
        :param app_type: 
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        
        

        self._name = None
        self._app_server_group_id = None
        self._description = None
        self._authorization_type = None
        self._app_type = None
        self.discriminator = None

        self.name = name
        if app_server_group_id is not None:
            self.app_server_group_id = app_server_group_id
        if description is not None:
            self.description = description
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if app_type is not None:
            self.app_type = app_type

    @property
    def name(self):
        """Gets the name of this CreateAppGroupReq.

        应用组名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成 2. 长度范围1~64个字符

        :return: The name of this CreateAppGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAppGroupReq.

        应用组名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成 2. 长度范围1~64个字符

        :param name: The name of this CreateAppGroupReq.
        :type name: str
        """
        self._name = name

    @property
    def app_server_group_id(self):
        """Gets the app_server_group_id of this CreateAppGroupReq.

        应用服务器组ID

        :return: The app_server_group_id of this CreateAppGroupReq.
        :rtype: str
        """
        return self._app_server_group_id

    @app_server_group_id.setter
    def app_server_group_id(self, app_server_group_id):
        """Sets the app_server_group_id of this CreateAppGroupReq.

        应用服务器组ID

        :param app_server_group_id: The app_server_group_id of this CreateAppGroupReq.
        :type app_server_group_id: str
        """
        self._app_server_group_id = app_server_group_id

    @property
    def description(self):
        """Gets the description of this CreateAppGroupReq.

        应用组描述

        :return: The description of this CreateAppGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAppGroupReq.

        应用组描述

        :param description: The description of this CreateAppGroupReq.
        :type description: str
        """
        self._description = description

    @property
    def authorization_type(self):
        """Gets the authorization_type of this CreateAppGroupReq.

        :return: The authorization_type of this CreateAppGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizationTypeEnum`
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        """Sets the authorization_type of this CreateAppGroupReq.

        :param authorization_type: The authorization_type of this CreateAppGroupReq.
        :type authorization_type: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizationTypeEnum`
        """
        self._authorization_type = authorization_type

    @property
    def app_type(self):
        """Gets the app_type of this CreateAppGroupReq.

        :return: The app_type of this CreateAppGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this CreateAppGroupReq.

        :param app_type: The app_type of this CreateAppGroupReq.
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        self._app_type = app_type

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
        if not isinstance(other, CreateAppGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
