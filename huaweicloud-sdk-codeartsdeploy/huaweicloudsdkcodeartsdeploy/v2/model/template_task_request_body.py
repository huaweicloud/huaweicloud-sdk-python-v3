# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateTaskRequestBody:

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
        'project_name': 'str',
        'template_id': 'str',
        'task_name': 'str',
        'slave_cluster_id': 'str',
        'configs': 'list[ConfigInfoDO]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'template_id': 'template_id',
        'task_name': 'task_name',
        'slave_cluster_id': 'slave_cluster_id',
        'configs': 'configs'
    }

    def __init__(self, project_id=None, project_name=None, template_id=None, task_name=None, slave_cluster_id=None, configs=None):
        """TemplateTaskRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param template_id: 部署模板id
        :type template_id: str
        :param task_name: 应用名称
        :type task_name: str
        :param slave_cluster_id: 自定义slave资源池id
        :type slave_cluster_id: str
        :param configs: 部署参数类
        :type configs: list[:class:`huaweicloudsdkcodeartsdeploy.v2.ConfigInfoDO`]
        """
        
        

        self._project_id = None
        self._project_name = None
        self._template_id = None
        self._task_name = None
        self._slave_cluster_id = None
        self._configs = None
        self.discriminator = None

        self.project_id = project_id
        self.project_name = project_name
        self.template_id = template_id
        self.task_name = task_name
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if configs is not None:
            self.configs = configs

    @property
    def project_id(self):
        """Gets the project_id of this TemplateTaskRequestBody.

        项目ID

        :return: The project_id of this TemplateTaskRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TemplateTaskRequestBody.

        项目ID

        :param project_id: The project_id of this TemplateTaskRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this TemplateTaskRequestBody.

        项目名称

        :return: The project_name of this TemplateTaskRequestBody.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TemplateTaskRequestBody.

        项目名称

        :param project_name: The project_name of this TemplateTaskRequestBody.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def template_id(self):
        """Gets the template_id of this TemplateTaskRequestBody.

        部署模板id

        :return: The template_id of this TemplateTaskRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplateTaskRequestBody.

        部署模板id

        :param template_id: The template_id of this TemplateTaskRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def task_name(self):
        """Gets the task_name of this TemplateTaskRequestBody.

        应用名称

        :return: The task_name of this TemplateTaskRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TemplateTaskRequestBody.

        应用名称

        :param task_name: The task_name of this TemplateTaskRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this TemplateTaskRequestBody.

        自定义slave资源池id

        :return: The slave_cluster_id of this TemplateTaskRequestBody.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this TemplateTaskRequestBody.

        自定义slave资源池id

        :param slave_cluster_id: The slave_cluster_id of this TemplateTaskRequestBody.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def configs(self):
        """Gets the configs of this TemplateTaskRequestBody.

        部署参数类

        :return: The configs of this TemplateTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.ConfigInfoDO`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this TemplateTaskRequestBody.

        部署参数类

        :param configs: The configs of this TemplateTaskRequestBody.
        :type configs: list[:class:`huaweicloudsdkcodeartsdeploy.v2.ConfigInfoDO`]
        """
        self._configs = configs

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
        if not isinstance(other, TemplateTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
