# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'template_name': 'str',
        'task_config': 'str'
    }

    attribute_map = {
        'component_id': 'component_id',
        'template_name': 'template_name',
        'task_config': 'task_config'
    }

    def __init__(self, component_id=None, template_name=None, task_config=None):
        r"""CreateTemplateReq

        The model defined in huaweicloud sdk

        :param component_id: 插件ID
        :type component_id: str
        :param template_name: 插件模板的名称
        :type template_name: str
        :param task_config: 插件action的配置内容
        :type task_config: str
        """
        
        

        self._component_id = None
        self._template_name = None
        self._task_config = None
        self.discriminator = None

        self.component_id = component_id
        self.template_name = template_name
        self.task_config = task_config

    @property
    def component_id(self):
        r"""Gets the component_id of this CreateTemplateReq.

        插件ID

        :return: The component_id of this CreateTemplateReq.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this CreateTemplateReq.

        插件ID

        :param component_id: The component_id of this CreateTemplateReq.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateTemplateReq.

        插件模板的名称

        :return: The template_name of this CreateTemplateReq.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateTemplateReq.

        插件模板的名称

        :param template_name: The template_name of this CreateTemplateReq.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def task_config(self):
        r"""Gets the task_config of this CreateTemplateReq.

        插件action的配置内容

        :return: The task_config of this CreateTemplateReq.
        :rtype: str
        """
        return self._task_config

    @task_config.setter
    def task_config(self, task_config):
        r"""Sets the task_config of this CreateTemplateReq.

        插件action的配置内容

        :param task_config: The task_config of this CreateTemplateReq.
        :type task_config: str
        """
        self._task_config = task_config

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
        if not isinstance(other, CreateTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
