# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyEnvironmentResponse(SdkResponse):

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
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'vpc_id': 'str',
        'creator': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'deploy_mode': 'str',
        'resources': 'list[Resource]',
        'labels': 'list[EnvironmentViewLabels]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'vpc_id': 'vpc_id',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'deploy_mode': 'deploy_mode',
        'resources': 'resources',
        'labels': 'labels'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, enterprise_project_id=None, vpc_id=None, creator=None, create_time=None, update_time=None, deploy_mode=None, resources=None, labels=None):
        """ModifyEnvironmentResponse

        The model defined in huaweicloud sdk

        :param id: 环境id
        :type id: str
        :param project_id: 
        :type project_id: str
        :param name: 环境名称
        :type name: str
        :param description: 环境描述
        :type description: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param vpc_id: 虚拟私有云id
        :type vpc_id: str
        :param creator: 创建者
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 更新时间。
        :type update_time: int
        :param deploy_mode: 环境类型
        :type deploy_mode: str
        :param resources: 
        :type resources: list[:class:`huaweicloudsdkservicestage.v3.Resource`]
        :param labels: 
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentViewLabels`]
        """
        
        super(ModifyEnvironmentResponse, self).__init__()

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._vpc_id = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._deploy_mode = None
        self._resources = None
        self._labels = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if resources is not None:
            self.resources = resources
        if labels is not None:
            self.labels = labels

    @property
    def id(self):
        """Gets the id of this ModifyEnvironmentResponse.

        环境id

        :return: The id of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModifyEnvironmentResponse.

        环境id

        :param id: The id of this ModifyEnvironmentResponse.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this ModifyEnvironmentResponse.

        :return: The project_id of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ModifyEnvironmentResponse.

        :param project_id: The project_id of this ModifyEnvironmentResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this ModifyEnvironmentResponse.

        环境名称

        :return: The name of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyEnvironmentResponse.

        环境名称

        :param name: The name of this ModifyEnvironmentResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ModifyEnvironmentResponse.

        环境描述

        :return: The description of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyEnvironmentResponse.

        环境描述

        :param description: The description of this ModifyEnvironmentResponse.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ModifyEnvironmentResponse.

        企业项目id

        :return: The enterprise_project_id of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ModifyEnvironmentResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ModifyEnvironmentResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ModifyEnvironmentResponse.

        虚拟私有云id

        :return: The vpc_id of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ModifyEnvironmentResponse.

        虚拟私有云id

        :param vpc_id: The vpc_id of this ModifyEnvironmentResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def creator(self):
        """Gets the creator of this ModifyEnvironmentResponse.

        创建者

        :return: The creator of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ModifyEnvironmentResponse.

        创建者

        :param creator: The creator of this ModifyEnvironmentResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this ModifyEnvironmentResponse.

        创建时间。

        :return: The create_time of this ModifyEnvironmentResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ModifyEnvironmentResponse.

        创建时间。

        :param create_time: The create_time of this ModifyEnvironmentResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ModifyEnvironmentResponse.

        更新时间。

        :return: The update_time of this ModifyEnvironmentResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ModifyEnvironmentResponse.

        更新时间。

        :param update_time: The update_time of this ModifyEnvironmentResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def deploy_mode(self):
        """Gets the deploy_mode of this ModifyEnvironmentResponse.

        环境类型

        :return: The deploy_mode of this ModifyEnvironmentResponse.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        """Sets the deploy_mode of this ModifyEnvironmentResponse.

        环境类型

        :param deploy_mode: The deploy_mode of this ModifyEnvironmentResponse.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def resources(self):
        """Gets the resources of this ModifyEnvironmentResponse.

        :return: The resources of this ModifyEnvironmentResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ModifyEnvironmentResponse.

        :param resources: The resources of this ModifyEnvironmentResponse.
        :type resources: list[:class:`huaweicloudsdkservicestage.v3.Resource`]
        """
        self._resources = resources

    @property
    def labels(self):
        """Gets the labels of this ModifyEnvironmentResponse.

        :return: The labels of this ModifyEnvironmentResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentViewLabels`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ModifyEnvironmentResponse.

        :param labels: The labels of this ModifyEnvironmentResponse.
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentViewLabels`]
        """
        self._labels = labels

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
        if not isinstance(other, ModifyEnvironmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
