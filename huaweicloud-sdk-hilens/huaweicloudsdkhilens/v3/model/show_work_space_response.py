# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkSpaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'ma_workspace_id': 'str',
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'owner': 'str',
        'user_id': 'str',
        'used_flag': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'ma_workspace_id': 'ma_workspace_id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'owner': 'owner',
        'user_id': 'user_id',
        'used_flag': 'used_flag'
    }

    def __init__(self, workspace_id=None, ma_workspace_id=None, project_id=None, name=None, description=None, enterprise_project_id=None, enterprise_project_name=None, create_time=None, update_time=None, owner=None, user_id=None, used_flag=None):
        """ShowWorkSpaceResponse

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param ma_workspace_id: 对应的Modelarts工作空间的id
        :type ma_workspace_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param name: 工作空间名称
        :type name: str
        :param description: 工作空间描述
        :type description: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param owner: 创建者
        :type owner: str
        :param user_id: 创建者的USER_ID
        :type user_id: str
        :param used_flag: 正在被使用
        :type used_flag: str
        """
        
        super(ShowWorkSpaceResponse, self).__init__()

        self._workspace_id = None
        self._ma_workspace_id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._create_time = None
        self._update_time = None
        self._owner = None
        self._user_id = None
        self._used_flag = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if ma_workspace_id is not None:
            self.ma_workspace_id = ma_workspace_id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if owner is not None:
            self.owner = owner
        if user_id is not None:
            self.user_id = user_id
        if used_flag is not None:
            self.used_flag = used_flag

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ShowWorkSpaceResponse.

        工作空间id

        :return: The workspace_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ShowWorkSpaceResponse.

        工作空间id

        :param workspace_id: The workspace_id of this ShowWorkSpaceResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def ma_workspace_id(self):
        """Gets the ma_workspace_id of this ShowWorkSpaceResponse.

        对应的Modelarts工作空间的id

        :return: The ma_workspace_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._ma_workspace_id

    @ma_workspace_id.setter
    def ma_workspace_id(self, ma_workspace_id):
        """Sets the ma_workspace_id of this ShowWorkSpaceResponse.

        对应的Modelarts工作空间的id

        :param ma_workspace_id: The ma_workspace_id of this ShowWorkSpaceResponse.
        :type ma_workspace_id: str
        """
        self._ma_workspace_id = ma_workspace_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowWorkSpaceResponse.

        项目ID

        :return: The project_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowWorkSpaceResponse.

        项目ID

        :param project_id: The project_id of this ShowWorkSpaceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this ShowWorkSpaceResponse.

        工作空间名称

        :return: The name of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowWorkSpaceResponse.

        工作空间名称

        :param name: The name of this ShowWorkSpaceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowWorkSpaceResponse.

        工作空间描述

        :return: The description of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowWorkSpaceResponse.

        工作空间描述

        :param description: The description of this ShowWorkSpaceResponse.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowWorkSpaceResponse.

        企业项目ID

        :return: The enterprise_project_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowWorkSpaceResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowWorkSpaceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this ShowWorkSpaceResponse.

        企业项目名称

        :return: The enterprise_project_name of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this ShowWorkSpaceResponse.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this ShowWorkSpaceResponse.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def create_time(self):
        """Gets the create_time of this ShowWorkSpaceResponse.

        创建时间

        :return: The create_time of this ShowWorkSpaceResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowWorkSpaceResponse.

        创建时间

        :param create_time: The create_time of this ShowWorkSpaceResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowWorkSpaceResponse.

        更新时间

        :return: The update_time of this ShowWorkSpaceResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowWorkSpaceResponse.

        更新时间

        :param update_time: The update_time of this ShowWorkSpaceResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def owner(self):
        """Gets the owner of this ShowWorkSpaceResponse.

        创建者

        :return: The owner of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowWorkSpaceResponse.

        创建者

        :param owner: The owner of this ShowWorkSpaceResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def user_id(self):
        """Gets the user_id of this ShowWorkSpaceResponse.

        创建者的USER_ID

        :return: The user_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShowWorkSpaceResponse.

        创建者的USER_ID

        :param user_id: The user_id of this ShowWorkSpaceResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def used_flag(self):
        """Gets the used_flag of this ShowWorkSpaceResponse.

        正在被使用

        :return: The used_flag of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._used_flag

    @used_flag.setter
    def used_flag(self, used_flag):
        """Sets the used_flag of this ShowWorkSpaceResponse.

        正在被使用

        :param used_flag: The used_flag of this ShowWorkSpaceResponse.
        :type used_flag: str
        """
        self._used_flag = used_flag

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
        if not isinstance(other, ShowWorkSpaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
