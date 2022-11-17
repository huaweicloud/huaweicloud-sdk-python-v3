# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'template_description': 'str',
        'namespace': 'str',
        'dimension_name': 'str',
        'template_items': 'list[TemplateItem]'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_description': 'template_description',
        'namespace': 'namespace',
        'dimension_name': 'dimension_name',
        'template_items': 'template_items'
    }

    def __init__(self, template_name=None, template_description=None, namespace=None, dimension_name=None, template_items=None):
        """UpdateAlarmTemplateRequestBody

        The model defined in huaweicloud sdk

        :param template_name: 自定义告警模板名称，只能包含0-9/a-z/A-Z/_/-或汉字，长度为1-128。。
        :type template_name: str
        :param template_description: 自定义告警模板详细描述，长度为0-256。
        :type template_description: str
        :param namespace: 创建自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param dimension_name: 资源类型对应的指标监控维度，选择弹性云服务器，则维度为云服务器，dimension_name值为instance_id；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dimension_name: str
        :param template_items: 创建自定义告警模板添加一个或者多个指标的告警规则；目前最多可增加30组告警规则策略。
        :type template_items: list[:class:`huaweicloudsdkces.v1.TemplateItem`]
        """
        
        

        self._template_name = None
        self._template_description = None
        self._namespace = None
        self._dimension_name = None
        self._template_items = None
        self.discriminator = None

        self.template_name = template_name
        if template_description is not None:
            self.template_description = template_description
        self.namespace = namespace
        self.dimension_name = dimension_name
        self.template_items = template_items

    @property
    def template_name(self):
        """Gets the template_name of this UpdateAlarmTemplateRequestBody.

        自定义告警模板名称，只能包含0-9/a-z/A-Z/_/-或汉字，长度为1-128。。

        :return: The template_name of this UpdateAlarmTemplateRequestBody.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this UpdateAlarmTemplateRequestBody.

        自定义告警模板名称，只能包含0-9/a-z/A-Z/_/-或汉字，长度为1-128。。

        :param template_name: The template_name of this UpdateAlarmTemplateRequestBody.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_description(self):
        """Gets the template_description of this UpdateAlarmTemplateRequestBody.

        自定义告警模板详细描述，长度为0-256。

        :return: The template_description of this UpdateAlarmTemplateRequestBody.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this UpdateAlarmTemplateRequestBody.

        自定义告警模板详细描述，长度为0-256。

        :param template_description: The template_description of this UpdateAlarmTemplateRequestBody.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def namespace(self):
        """Gets the namespace of this UpdateAlarmTemplateRequestBody.

        创建自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this UpdateAlarmTemplateRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UpdateAlarmTemplateRequestBody.

        创建自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this UpdateAlarmTemplateRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        """Gets the dimension_name of this UpdateAlarmTemplateRequestBody.

        资源类型对应的指标监控维度，选择弹性云服务器，则维度为云服务器，dimension_name值为instance_id；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dimension_name of this UpdateAlarmTemplateRequestBody.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        """Sets the dimension_name of this UpdateAlarmTemplateRequestBody.

        资源类型对应的指标监控维度，选择弹性云服务器，则维度为云服务器，dimension_name值为instance_id；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dimension_name: The dimension_name of this UpdateAlarmTemplateRequestBody.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

    @property
    def template_items(self):
        """Gets the template_items of this UpdateAlarmTemplateRequestBody.

        创建自定义告警模板添加一个或者多个指标的告警规则；目前最多可增加30组告警规则策略。

        :return: The template_items of this UpdateAlarmTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.TemplateItem`]
        """
        return self._template_items

    @template_items.setter
    def template_items(self, template_items):
        """Sets the template_items of this UpdateAlarmTemplateRequestBody.

        创建自定义告警模板添加一个或者多个指标的告警规则；目前最多可增加30组告警规则策略。

        :param template_items: The template_items of this UpdateAlarmTemplateRequestBody.
        :type template_items: list[:class:`huaweicloudsdkces.v1.TemplateItem`]
        """
        self._template_items = template_items

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
        if not isinstance(other, UpdateAlarmTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
