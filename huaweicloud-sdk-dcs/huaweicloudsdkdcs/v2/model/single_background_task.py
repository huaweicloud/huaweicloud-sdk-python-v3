# coding: utf-8

import pprint
import re

import six





class SingleBackgroundTask:


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
        'details': 'DetailsBody',
        'user_name': 'str',
        'user_id': 'str',
        'params': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'details': 'details',
        'user_name': 'user_name',
        'user_id': 'user_id',
        'params': 'params',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, details=None, user_name=None, user_id=None, params=None, status=None, created_at=None, updated_at=None):
        """SingleBackgroundTask - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._details = None
        self._user_name = None
        self._user_id = None
        self._params = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if details is not None:
            self.details = details
        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id
        if params is not None:
            self.params = params
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this SingleBackgroundTask.

        后台任务ID

        :return: The id of this SingleBackgroundTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SingleBackgroundTask.

        后台任务ID

        :param id: The id of this SingleBackgroundTask.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SingleBackgroundTask.

        后台任务名，目前支持以下取值：  ChangeInstanceSpec：变更规格  BindEip：开启公网访问  UnBindEip：关闭公网访问  AddReplica：添加副本  DelReplica：删除副本  AddWhitelist：设置IP白名单  UpdatePort：修改端口  RemoveIpFromDns：域名摘除IP 

        :return: The name of this SingleBackgroundTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SingleBackgroundTask.

        后台任务名，目前支持以下取值：  ChangeInstanceSpec：变更规格  BindEip：开启公网访问  UnBindEip：关闭公网访问  AddReplica：添加副本  DelReplica：删除副本  AddWhitelist：设置IP白名单  UpdatePort：修改端口  RemoveIpFromDns：域名摘除IP 

        :param name: The name of this SingleBackgroundTask.
        :type: str
        """
        self._name = name

    @property
    def details(self):
        """Gets the details of this SingleBackgroundTask.


        :return: The details of this SingleBackgroundTask.
        :rtype: DetailsBody
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SingleBackgroundTask.


        :param details: The details of this SingleBackgroundTask.
        :type: DetailsBody
        """
        self._details = details

    @property
    def user_name(self):
        """Gets the user_name of this SingleBackgroundTask.

        用户名

        :return: The user_name of this SingleBackgroundTask.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SingleBackgroundTask.

        用户名

        :param user_name: The user_name of this SingleBackgroundTask.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        """Gets the user_id of this SingleBackgroundTask.

        用户ID

        :return: The user_id of this SingleBackgroundTask.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SingleBackgroundTask.

        用户ID

        :param user_id: The user_id of this SingleBackgroundTask.
        :type: str
        """
        self._user_id = user_id

    @property
    def params(self):
        """Gets the params of this SingleBackgroundTask.

        任务相关参数

        :return: The params of this SingleBackgroundTask.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this SingleBackgroundTask.

        任务相关参数

        :param params: The params of this SingleBackgroundTask.
        :type: str
        """
        self._params = params

    @property
    def status(self):
        """Gets the status of this SingleBackgroundTask.

        任务状态

        :return: The status of this SingleBackgroundTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SingleBackgroundTask.

        任务状态

        :param status: The status of this SingleBackgroundTask.
        :type: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this SingleBackgroundTask.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :return: The created_at of this SingleBackgroundTask.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SingleBackgroundTask.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :param created_at: The created_at of this SingleBackgroundTask.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SingleBackgroundTask.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :return: The updated_at of this SingleBackgroundTask.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SingleBackgroundTask.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :param updated_at: The updated_at of this SingleBackgroundTask.
        :type: str
        """
        self._updated_at = updated_at

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SingleBackgroundTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
