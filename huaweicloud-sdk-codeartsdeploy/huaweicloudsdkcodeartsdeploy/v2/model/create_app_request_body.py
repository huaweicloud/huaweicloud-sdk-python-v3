# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'group_id': 'str',
        'is_draft': 'bool',
        'create_type': 'str',
        'slave_cluster_id': 'str',
        'trigger': 'TaskTriggerVO',
        'arrange_infos': 'list[TaskV2RequestBody]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'group_id': 'group_id',
        'is_draft': 'is_draft',
        'create_type': 'create_type',
        'slave_cluster_id': 'slave_cluster_id',
        'trigger': 'trigger',
        'arrange_infos': 'arrange_infos'
    }

    def __init__(self, project_id=None, name=None, description=None, group_id=None, is_draft=None, create_type=None, slave_cluster_id=None, trigger=None, arrange_infos=None):
        """CreateAppRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param name: 应用名称
        :type name: str
        :param description: 描述
        :type description: str
        :param group_id: 分组id
        :type group_id: str
        :param is_draft: 是否为草稿
        :type is_draft: bool
        :param create_type: 创建类型，创建类型只有一个&#39;template&#39;，即根据模板创建
        :type create_type: str
        :param slave_cluster_id: 自定义slave资源池id
        :type slave_cluster_id: str
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkcodeartsdeploy.v2.TaskTriggerVO`
        :param arrange_infos: 部署任务列表信息
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskV2RequestBody`]
        """
        
        

        self._project_id = None
        self._name = None
        self._description = None
        self._group_id = None
        self._is_draft = None
        self._create_type = None
        self._slave_cluster_id = None
        self._trigger = None
        self._arrange_infos = None
        self.discriminator = None

        self.project_id = project_id
        self.name = name
        if description is not None:
            self.description = description
        if group_id is not None:
            self.group_id = group_id
        self.is_draft = is_draft
        self.create_type = create_type
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if trigger is not None:
            self.trigger = trigger
        if arrange_infos is not None:
            self.arrange_infos = arrange_infos

    @property
    def project_id(self):
        """Gets the project_id of this CreateAppRequestBody.

        项目ID

        :return: The project_id of this CreateAppRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateAppRequestBody.

        项目ID

        :param project_id: The project_id of this CreateAppRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this CreateAppRequestBody.

        应用名称

        :return: The name of this CreateAppRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAppRequestBody.

        应用名称

        :param name: The name of this CreateAppRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateAppRequestBody.

        描述

        :return: The description of this CreateAppRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAppRequestBody.

        描述

        :param description: The description of this CreateAppRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def group_id(self):
        """Gets the group_id of this CreateAppRequestBody.

        分组id

        :return: The group_id of this CreateAppRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateAppRequestBody.

        分组id

        :param group_id: The group_id of this CreateAppRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def is_draft(self):
        """Gets the is_draft of this CreateAppRequestBody.

        是否为草稿

        :return: The is_draft of this CreateAppRequestBody.
        :rtype: bool
        """
        return self._is_draft

    @is_draft.setter
    def is_draft(self, is_draft):
        """Sets the is_draft of this CreateAppRequestBody.

        是否为草稿

        :param is_draft: The is_draft of this CreateAppRequestBody.
        :type is_draft: bool
        """
        self._is_draft = is_draft

    @property
    def create_type(self):
        """Gets the create_type of this CreateAppRequestBody.

        创建类型，创建类型只有一个'template'，即根据模板创建

        :return: The create_type of this CreateAppRequestBody.
        :rtype: str
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        """Sets the create_type of this CreateAppRequestBody.

        创建类型，创建类型只有一个'template'，即根据模板创建

        :param create_type: The create_type of this CreateAppRequestBody.
        :type create_type: str
        """
        self._create_type = create_type

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this CreateAppRequestBody.

        自定义slave资源池id

        :return: The slave_cluster_id of this CreateAppRequestBody.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this CreateAppRequestBody.

        自定义slave资源池id

        :param slave_cluster_id: The slave_cluster_id of this CreateAppRequestBody.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def trigger(self):
        """Gets the trigger of this CreateAppRequestBody.

        :return: The trigger of this CreateAppRequestBody.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.TaskTriggerVO`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this CreateAppRequestBody.

        :param trigger: The trigger of this CreateAppRequestBody.
        :type trigger: :class:`huaweicloudsdkcodeartsdeploy.v2.TaskTriggerVO`
        """
        self._trigger = trigger

    @property
    def arrange_infos(self):
        """Gets the arrange_infos of this CreateAppRequestBody.

        部署任务列表信息

        :return: The arrange_infos of this CreateAppRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskV2RequestBody`]
        """
        return self._arrange_infos

    @arrange_infos.setter
    def arrange_infos(self, arrange_infos):
        """Sets the arrange_infos of this CreateAppRequestBody.

        部署任务列表信息

        :param arrange_infos: The arrange_infos of this CreateAppRequestBody.
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskV2RequestBody`]
        """
        self._arrange_infos = arrange_infos

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
        if not isinstance(other, CreateAppRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
