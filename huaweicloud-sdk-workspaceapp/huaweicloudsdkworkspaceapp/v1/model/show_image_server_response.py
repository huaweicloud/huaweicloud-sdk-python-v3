# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageServerResponse(SdkResponse):

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
        'description': 'str',
        'image_ref': 'ImageRef',
        'server_group_id': 'str',
        'app_group_id': 'str',
        'server_id': 'str',
        'instance_id': 'str',
        'image_id': 'str',
        'status': 'ImageServerStatus',
        'authorize_accounts': 'list[ImageAccountInfo]',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'image_ref': 'image_ref',
        'server_group_id': 'server_group_id',
        'app_group_id': 'app_group_id',
        'server_id': 'server_id',
        'instance_id': 'instance_id',
        'image_id': 'image_id',
        'status': 'status',
        'authorize_accounts': 'authorize_accounts',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, description=None, image_ref=None, server_group_id=None, app_group_id=None, server_id=None, instance_id=None, image_id=None, status=None, authorize_accounts=None, create_time=None, update_time=None, enterprise_project_id=None):
        r"""ShowImageServerResponse

        The model defined in huaweicloud sdk

        :param id: 实例的唯一标识。
        :type id: str
        :param name: 镜像实例名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param image_ref: 
        :type image_ref: :class:`huaweicloudsdkworkspaceapp.v1.ImageRef`
        :param server_group_id: APS服务器组ID。
        :type server_group_id: str
        :param app_group_id: 应用组ID。
        :type app_group_id: str
        :param server_id: APS实例ID。
        :type server_id: str
        :param instance_id: ECS服务器ID。
        :type instance_id: str
        :param image_id: 镜像产物唯一标识。
        :type image_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ImageServerStatus`
        :param authorize_accounts: 应用组授权用户， * 限制用户类型：&#39;USER&#39; - 用户
        :type authorize_accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.ImageAccountInfo`]
        :param create_time: 镜像实例创建时间。
        :type create_time: datetime
        :param update_time: 更新时间。
        :type update_time: datetime
        :param enterprise_project_id: 企业项目ID,仅企业项目需配置(字段为空或者0表示使用默认default企业项目)。
        :type enterprise_project_id: str
        """
        
        super(ShowImageServerResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._image_ref = None
        self._server_group_id = None
        self._app_group_id = None
        self._server_id = None
        self._instance_id = None
        self._image_id = None
        self._status = None
        self._authorize_accounts = None
        self._create_time = None
        self._update_time = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if image_ref is not None:
            self.image_ref = image_ref
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if server_id is not None:
            self.server_id = server_id
        if instance_id is not None:
            self.instance_id = instance_id
        if image_id is not None:
            self.image_id = image_id
        if status is not None:
            self.status = status
        if authorize_accounts is not None:
            self.authorize_accounts = authorize_accounts
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ShowImageServerResponse.

        实例的唯一标识。

        :return: The id of this ShowImageServerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowImageServerResponse.

        实例的唯一标识。

        :param id: The id of this ShowImageServerResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowImageServerResponse.

        镜像实例名称。

        :return: The name of this ShowImageServerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowImageServerResponse.

        镜像实例名称。

        :param name: The name of this ShowImageServerResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowImageServerResponse.

        描述。

        :return: The description of this ShowImageServerResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowImageServerResponse.

        描述。

        :param description: The description of this ShowImageServerResponse.
        :type description: str
        """
        self._description = description

    @property
    def image_ref(self):
        r"""Gets the image_ref of this ShowImageServerResponse.

        :return: The image_ref of this ShowImageServerResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ImageRef`
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        r"""Sets the image_ref of this ShowImageServerResponse.

        :param image_ref: The image_ref of this ShowImageServerResponse.
        :type image_ref: :class:`huaweicloudsdkworkspaceapp.v1.ImageRef`
        """
        self._image_ref = image_ref

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this ShowImageServerResponse.

        APS服务器组ID。

        :return: The server_group_id of this ShowImageServerResponse.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this ShowImageServerResponse.

        APS服务器组ID。

        :param server_group_id: The server_group_id of this ShowImageServerResponse.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def app_group_id(self):
        r"""Gets the app_group_id of this ShowImageServerResponse.

        应用组ID。

        :return: The app_group_id of this ShowImageServerResponse.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        r"""Sets the app_group_id of this ShowImageServerResponse.

        应用组ID。

        :param app_group_id: The app_group_id of this ShowImageServerResponse.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def server_id(self):
        r"""Gets the server_id of this ShowImageServerResponse.

        APS实例ID。

        :return: The server_id of this ShowImageServerResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ShowImageServerResponse.

        APS实例ID。

        :param server_id: The server_id of this ShowImageServerResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowImageServerResponse.

        ECS服务器ID。

        :return: The instance_id of this ShowImageServerResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowImageServerResponse.

        ECS服务器ID。

        :param instance_id: The instance_id of this ShowImageServerResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ShowImageServerResponse.

        镜像产物唯一标识。

        :return: The image_id of this ShowImageServerResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ShowImageServerResponse.

        镜像产物唯一标识。

        :param image_id: The image_id of this ShowImageServerResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def status(self):
        r"""Gets the status of this ShowImageServerResponse.

        :return: The status of this ShowImageServerResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ImageServerStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowImageServerResponse.

        :param status: The status of this ShowImageServerResponse.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ImageServerStatus`
        """
        self._status = status

    @property
    def authorize_accounts(self):
        r"""Gets the authorize_accounts of this ShowImageServerResponse.

        应用组授权用户， * 限制用户类型：'USER' - 用户

        :return: The authorize_accounts of this ShowImageServerResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.ImageAccountInfo`]
        """
        return self._authorize_accounts

    @authorize_accounts.setter
    def authorize_accounts(self, authorize_accounts):
        r"""Sets the authorize_accounts of this ShowImageServerResponse.

        应用组授权用户， * 限制用户类型：'USER' - 用户

        :param authorize_accounts: The authorize_accounts of this ShowImageServerResponse.
        :type authorize_accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.ImageAccountInfo`]
        """
        self._authorize_accounts = authorize_accounts

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowImageServerResponse.

        镜像实例创建时间。

        :return: The create_time of this ShowImageServerResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowImageServerResponse.

        镜像实例创建时间。

        :param create_time: The create_time of this ShowImageServerResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowImageServerResponse.

        更新时间。

        :return: The update_time of this ShowImageServerResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowImageServerResponse.

        更新时间。

        :param update_time: The update_time of this ShowImageServerResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowImageServerResponse.

        企业项目ID,仅企业项目需配置(字段为空或者0表示使用默认default企业项目)。

        :return: The enterprise_project_id of this ShowImageServerResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowImageServerResponse.

        企业项目ID,仅企业项目需配置(字段为空或者0表示使用默认default企业项目)。

        :param enterprise_project_id: The enterprise_project_id of this ShowImageServerResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowImageServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
