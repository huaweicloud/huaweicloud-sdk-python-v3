# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateInfo:

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
        'component_id': 'str',
        'template_name': 'str',
        'task_config': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'component_id': 'component_id',
        'template_name': 'template_name',
        'task_config': 'task_config',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, component_id=None, template_name=None, task_config=None, create_time=None, update_time=None, project_id=None):
        r"""TemplateInfo

        The model defined in huaweicloud sdk

        :param id: 模板id
        :type id: str
        :param component_id: 插件id
        :type component_id: str
        :param template_name: 插件配置模板名称
        :type template_name: str
        :param task_config: 插件action的配置内容
        :type task_config: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._id = None
        self._component_id = None
        self._template_name = None
        self._task_config = None
        self._create_time = None
        self._update_time = None
        self._project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if component_id is not None:
            self.component_id = component_id
        if template_name is not None:
            self.template_name = template_name
        if task_config is not None:
            self.task_config = task_config
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if project_id is not None:
            self.project_id = project_id

    @property
    def id(self):
        r"""Gets the id of this TemplateInfo.

        模板id

        :return: The id of this TemplateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TemplateInfo.

        模板id

        :param id: The id of this TemplateInfo.
        :type id: str
        """
        self._id = id

    @property
    def component_id(self):
        r"""Gets the component_id of this TemplateInfo.

        插件id

        :return: The component_id of this TemplateInfo.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this TemplateInfo.

        插件id

        :param component_id: The component_id of this TemplateInfo.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def template_name(self):
        r"""Gets the template_name of this TemplateInfo.

        插件配置模板名称

        :return: The template_name of this TemplateInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this TemplateInfo.

        插件配置模板名称

        :param template_name: The template_name of this TemplateInfo.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def task_config(self):
        r"""Gets the task_config of this TemplateInfo.

        插件action的配置内容

        :return: The task_config of this TemplateInfo.
        :rtype: str
        """
        return self._task_config

    @task_config.setter
    def task_config(self, task_config):
        r"""Sets the task_config of this TemplateInfo.

        插件action的配置内容

        :param task_config: The task_config of this TemplateInfo.
        :type task_config: str
        """
        self._task_config = task_config

    @property
    def create_time(self):
        r"""Gets the create_time of this TemplateInfo.

        创建时间

        :return: The create_time of this TemplateInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TemplateInfo.

        创建时间

        :param create_time: The create_time of this TemplateInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TemplateInfo.

        更新时间

        :return: The update_time of this TemplateInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TemplateInfo.

        更新时间

        :param update_time: The update_time of this TemplateInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        r"""Gets the project_id of this TemplateInfo.

        项目id

        :return: The project_id of this TemplateInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TemplateInfo.

        项目id

        :param project_id: The project_id of this TemplateInfo.
        :type project_id: str
        """
        self._project_id = project_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
