# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'updated_at': 'str',
        'enable_show': 'bool'
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
        'updated_at': 'updated_at',
        'enable_show': 'enable_show'
    }

    def __init__(self, id=None, name=None, details=None, user_name=None, user_id=None, params=None, status=None, created_at=None, updated_at=None, enable_show=None):
        r"""SingleBackgroundTask

        The model defined in huaweicloud sdk

        :param id: 后台任务ID
        :type id: str
        :param name: 后台任务名，目前支持以下取值：  ChangeInstanceSpec：变更规格  BindEip：开启公网访问  UnBindEip：关闭公网访问  AddReplica：添加副本  DelReplica：删除副本  AddWhitelist：设置IP白名单  UpdatePort：修改端口  RemoveIpFromDns：域名摘除IP 
        :type name: str
        :param details: 
        :type details: :class:`huaweicloudsdkdcs.v2.DetailsBody`
        :param user_name: 用户名
        :type user_name: str
        :param user_id: 用户ID
        :type user_id: str
        :param params: 任务相关参数
        :type params: str
        :param status: 任务状态
        :type status: str
        :param created_at: 任务启动时间，格式为2020-06-17T07:38:42.503Z
        :type created_at: str
        :param updated_at: 任务结束时间，格式为2020-06-17T07:38:42.503Z
        :type updated_at: str
        :param enable_show: 是否有详细任务进展，可以展开查看
        :type enable_show: bool
        """
        
        

        self._id = None
        self._name = None
        self._details = None
        self._user_name = None
        self._user_id = None
        self._params = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._enable_show = None
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
        if enable_show is not None:
            self.enable_show = enable_show

    @property
    def id(self):
        r"""Gets the id of this SingleBackgroundTask.

        后台任务ID

        :return: The id of this SingleBackgroundTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SingleBackgroundTask.

        后台任务ID

        :param id: The id of this SingleBackgroundTask.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SingleBackgroundTask.

        后台任务名，目前支持以下取值：  ChangeInstanceSpec：变更规格  BindEip：开启公网访问  UnBindEip：关闭公网访问  AddReplica：添加副本  DelReplica：删除副本  AddWhitelist：设置IP白名单  UpdatePort：修改端口  RemoveIpFromDns：域名摘除IP 

        :return: The name of this SingleBackgroundTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SingleBackgroundTask.

        后台任务名，目前支持以下取值：  ChangeInstanceSpec：变更规格  BindEip：开启公网访问  UnBindEip：关闭公网访问  AddReplica：添加副本  DelReplica：删除副本  AddWhitelist：设置IP白名单  UpdatePort：修改端口  RemoveIpFromDns：域名摘除IP 

        :param name: The name of this SingleBackgroundTask.
        :type name: str
        """
        self._name = name

    @property
    def details(self):
        r"""Gets the details of this SingleBackgroundTask.

        :return: The details of this SingleBackgroundTask.
        :rtype: :class:`huaweicloudsdkdcs.v2.DetailsBody`
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this SingleBackgroundTask.

        :param details: The details of this SingleBackgroundTask.
        :type details: :class:`huaweicloudsdkdcs.v2.DetailsBody`
        """
        self._details = details

    @property
    def user_name(self):
        r"""Gets the user_name of this SingleBackgroundTask.

        用户名

        :return: The user_name of this SingleBackgroundTask.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SingleBackgroundTask.

        用户名

        :param user_name: The user_name of this SingleBackgroundTask.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this SingleBackgroundTask.

        用户ID

        :return: The user_id of this SingleBackgroundTask.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this SingleBackgroundTask.

        用户ID

        :param user_id: The user_id of this SingleBackgroundTask.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def params(self):
        r"""Gets the params of this SingleBackgroundTask.

        任务相关参数

        :return: The params of this SingleBackgroundTask.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this SingleBackgroundTask.

        任务相关参数

        :param params: The params of this SingleBackgroundTask.
        :type params: str
        """
        self._params = params

    @property
    def status(self):
        r"""Gets the status of this SingleBackgroundTask.

        任务状态

        :return: The status of this SingleBackgroundTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SingleBackgroundTask.

        任务状态

        :param status: The status of this SingleBackgroundTask.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this SingleBackgroundTask.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :return: The created_at of this SingleBackgroundTask.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SingleBackgroundTask.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :param created_at: The created_at of this SingleBackgroundTask.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SingleBackgroundTask.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :return: The updated_at of this SingleBackgroundTask.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SingleBackgroundTask.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :param updated_at: The updated_at of this SingleBackgroundTask.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def enable_show(self):
        r"""Gets the enable_show of this SingleBackgroundTask.

        是否有详细任务进展，可以展开查看

        :return: The enable_show of this SingleBackgroundTask.
        :rtype: bool
        """
        return self._enable_show

    @enable_show.setter
    def enable_show(self, enable_show):
        r"""Sets the enable_show of this SingleBackgroundTask.

        是否有详细任务进展，可以展开查看

        :param enable_show: The enable_show of this SingleBackgroundTask.
        :type enable_show: bool
        """
        self._enable_show = enable_show

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
        if not isinstance(other, SingleBackgroundTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
