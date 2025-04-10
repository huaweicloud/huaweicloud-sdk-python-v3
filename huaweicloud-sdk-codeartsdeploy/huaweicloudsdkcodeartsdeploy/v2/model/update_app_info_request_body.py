# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppInfoRequestBody:

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
        'is_draft': 'bool',
        'create_type': 'str',
        'slave_cluster_id': 'str',
        'trigger': 'TaskTriggerVO',
        'arrange_infos': 'list[UpdateTaskV2RequestBody]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'is_draft': 'is_draft',
        'create_type': 'create_type',
        'slave_cluster_id': 'slave_cluster_id',
        'trigger': 'trigger',
        'arrange_infos': 'arrange_infos'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, is_draft=None, create_type=None, slave_cluster_id=None, trigger=None, arrange_infos=None):
        r"""UpdateAppInfoRequestBody

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param project_id: 项目id
        :type project_id: str
        :param name: 应用名称
        :type name: str
        :param description: 描述
        :type description: str
        :param is_draft: 是否为草稿
        :type is_draft: bool
        :param create_type: 创建类型，template：部署模板创建
        :type create_type: str
        :param slave_cluster_id: 自定义slave资源池id
        :type slave_cluster_id: str
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkcodeartsdeploy.v2.TaskTriggerVO`
        :param arrange_infos: 部署任务列表信息
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.UpdateTaskV2RequestBody`]
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._is_draft = None
        self._create_type = None
        self._slave_cluster_id = None
        self._trigger = None
        self._arrange_infos = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.name = name
        if description is not None:
            self.description = description
        self.is_draft = is_draft
        self.create_type = create_type
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if trigger is not None:
            self.trigger = trigger
        if arrange_infos is not None:
            self.arrange_infos = arrange_infos

    @property
    def id(self):
        r"""Gets the id of this UpdateAppInfoRequestBody.

        应用id

        :return: The id of this UpdateAppInfoRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateAppInfoRequestBody.

        应用id

        :param id: The id of this UpdateAppInfoRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateAppInfoRequestBody.

        项目id

        :return: The project_id of this UpdateAppInfoRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateAppInfoRequestBody.

        项目id

        :param project_id: The project_id of this UpdateAppInfoRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this UpdateAppInfoRequestBody.

        应用名称

        :return: The name of this UpdateAppInfoRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateAppInfoRequestBody.

        应用名称

        :param name: The name of this UpdateAppInfoRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateAppInfoRequestBody.

        描述

        :return: The description of this UpdateAppInfoRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAppInfoRequestBody.

        描述

        :param description: The description of this UpdateAppInfoRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def is_draft(self):
        r"""Gets the is_draft of this UpdateAppInfoRequestBody.

        是否为草稿

        :return: The is_draft of this UpdateAppInfoRequestBody.
        :rtype: bool
        """
        return self._is_draft

    @is_draft.setter
    def is_draft(self, is_draft):
        r"""Sets the is_draft of this UpdateAppInfoRequestBody.

        是否为草稿

        :param is_draft: The is_draft of this UpdateAppInfoRequestBody.
        :type is_draft: bool
        """
        self._is_draft = is_draft

    @property
    def create_type(self):
        r"""Gets the create_type of this UpdateAppInfoRequestBody.

        创建类型，template：部署模板创建

        :return: The create_type of this UpdateAppInfoRequestBody.
        :rtype: str
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        r"""Sets the create_type of this UpdateAppInfoRequestBody.

        创建类型，template：部署模板创建

        :param create_type: The create_type of this UpdateAppInfoRequestBody.
        :type create_type: str
        """
        self._create_type = create_type

    @property
    def slave_cluster_id(self):
        r"""Gets the slave_cluster_id of this UpdateAppInfoRequestBody.

        自定义slave资源池id

        :return: The slave_cluster_id of this UpdateAppInfoRequestBody.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        r"""Sets the slave_cluster_id of this UpdateAppInfoRequestBody.

        自定义slave资源池id

        :param slave_cluster_id: The slave_cluster_id of this UpdateAppInfoRequestBody.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def trigger(self):
        r"""Gets the trigger of this UpdateAppInfoRequestBody.

        :return: The trigger of this UpdateAppInfoRequestBody.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.TaskTriggerVO`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this UpdateAppInfoRequestBody.

        :param trigger: The trigger of this UpdateAppInfoRequestBody.
        :type trigger: :class:`huaweicloudsdkcodeartsdeploy.v2.TaskTriggerVO`
        """
        self._trigger = trigger

    @property
    def arrange_infos(self):
        r"""Gets the arrange_infos of this UpdateAppInfoRequestBody.

        部署任务列表信息

        :return: The arrange_infos of this UpdateAppInfoRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.UpdateTaskV2RequestBody`]
        """
        return self._arrange_infos

    @arrange_infos.setter
    def arrange_infos(self, arrange_infos):
        r"""Sets the arrange_infos of this UpdateAppInfoRequestBody.

        部署任务列表信息

        :param arrange_infos: The arrange_infos of this UpdateAppInfoRequestBody.
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.UpdateTaskV2RequestBody`]
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
        if not isinstance(other, UpdateAppInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
