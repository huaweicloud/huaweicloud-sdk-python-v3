# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeEnvironmentResponse(SdkResponse):

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
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'charge_mode': 'str',
        'deploy_mode': 'str',
        'vpc_id': 'str',
        'base_resources': 'list[Resource]',
        'optional_resources': 'list[Resource]',
        'creator': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'alias': 'alias',
        'description': 'description',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'charge_mode': 'charge_mode',
        'deploy_mode': 'deploy_mode',
        'vpc_id': 'vpc_id',
        'base_resources': 'base_resources',
        'optional_resources': 'optional_resources',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, alias=None, description=None, project_id=None, enterprise_project_id=None, charge_mode=None, deploy_mode=None, vpc_id=None, base_resources=None, optional_resources=None, creator=None, create_time=None, update_time=None):
        """ChangeEnvironmentResponse

        The model defined in huaweicloud sdk

        :param id: 环境ID。
        :type id: str
        :param name: 环境名称。
        :type name: str
        :param alias: 环境别名。
        :type alias: str
        :param description: 环境描述。
        :type description: str
        :param project_id: 项目ID。
        :type project_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param charge_mode: 收费模式。
        :type charge_mode: str
        :param deploy_mode: 环境类型
        :type deploy_mode: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param base_resources: 基础资源。
        :type base_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        :param optional_resources: 可选资源。
        :type optional_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        :param creator: 创建人。
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        """
        
        super(ChangeEnvironmentResponse, self).__init__()

        self._id = None
        self._name = None
        self._alias = None
        self._description = None
        self._project_id = None
        self._enterprise_project_id = None
        self._charge_mode = None
        self._deploy_mode = None
        self._vpc_id = None
        self._base_resources = None
        self._optional_resources = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if base_resources is not None:
            self.base_resources = base_resources
        if optional_resources is not None:
            self.optional_resources = optional_resources
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ChangeEnvironmentResponse.

        环境ID。

        :return: The id of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangeEnvironmentResponse.

        环境ID。

        :param id: The id of this ChangeEnvironmentResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ChangeEnvironmentResponse.

        环境名称。

        :return: The name of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChangeEnvironmentResponse.

        环境名称。

        :param name: The name of this ChangeEnvironmentResponse.
        :type name: str
        """
        self._name = name

    @property
    def alias(self):
        """Gets the alias of this ChangeEnvironmentResponse.

        环境别名。

        :return: The alias of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ChangeEnvironmentResponse.

        环境别名。

        :param alias: The alias of this ChangeEnvironmentResponse.
        :type alias: str
        """
        self._alias = alias

    @property
    def description(self):
        """Gets the description of this ChangeEnvironmentResponse.

        环境描述。

        :return: The description of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChangeEnvironmentResponse.

        环境描述。

        :param description: The description of this ChangeEnvironmentResponse.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this ChangeEnvironmentResponse.

        项目ID。

        :return: The project_id of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ChangeEnvironmentResponse.

        项目ID。

        :param project_id: The project_id of this ChangeEnvironmentResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ChangeEnvironmentResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ChangeEnvironmentResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ChangeEnvironmentResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ChangeEnvironmentResponse.

        收费模式。

        :return: The charge_mode of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ChangeEnvironmentResponse.

        收费模式。

        :param charge_mode: The charge_mode of this ChangeEnvironmentResponse.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def deploy_mode(self):
        """Gets the deploy_mode of this ChangeEnvironmentResponse.

        环境类型

        :return: The deploy_mode of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        """Sets the deploy_mode of this ChangeEnvironmentResponse.

        环境类型

        :param deploy_mode: The deploy_mode of this ChangeEnvironmentResponse.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ChangeEnvironmentResponse.

        虚拟私有云ID。

        :return: The vpc_id of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ChangeEnvironmentResponse.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ChangeEnvironmentResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def base_resources(self):
        """Gets the base_resources of this ChangeEnvironmentResponse.

        基础资源。

        :return: The base_resources of this ChangeEnvironmentResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        return self._base_resources

    @base_resources.setter
    def base_resources(self, base_resources):
        """Sets the base_resources of this ChangeEnvironmentResponse.

        基础资源。

        :param base_resources: The base_resources of this ChangeEnvironmentResponse.
        :type base_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        self._base_resources = base_resources

    @property
    def optional_resources(self):
        """Gets the optional_resources of this ChangeEnvironmentResponse.

        可选资源。

        :return: The optional_resources of this ChangeEnvironmentResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        return self._optional_resources

    @optional_resources.setter
    def optional_resources(self, optional_resources):
        """Sets the optional_resources of this ChangeEnvironmentResponse.

        可选资源。

        :param optional_resources: The optional_resources of this ChangeEnvironmentResponse.
        :type optional_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        self._optional_resources = optional_resources

    @property
    def creator(self):
        """Gets the creator of this ChangeEnvironmentResponse.

        创建人。

        :return: The creator of this ChangeEnvironmentResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ChangeEnvironmentResponse.

        创建人。

        :param creator: The creator of this ChangeEnvironmentResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this ChangeEnvironmentResponse.

        创建时间。

        :return: The create_time of this ChangeEnvironmentResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ChangeEnvironmentResponse.

        创建时间。

        :param create_time: The create_time of this ChangeEnvironmentResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ChangeEnvironmentResponse.

        修改时间。

        :return: The update_time of this ChangeEnvironmentResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ChangeEnvironmentResponse.

        修改时间。

        :param update_time: The update_time of this ChangeEnvironmentResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ChangeEnvironmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
