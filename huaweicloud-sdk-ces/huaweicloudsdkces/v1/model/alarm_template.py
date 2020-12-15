# coding: utf-8

import pprint
import re

import six





class AlarmTemplate:


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
        'template_items': 'list[TemplateItem]',
        'template_id': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_description': 'template_description',
        'namespace': 'namespace',
        'dimension_name': 'dimension_name',
        'template_items': 'template_items',
        'template_id': 'template_id'
    }

    def __init__(self, template_name=None, template_description=None, namespace=None, dimension_name=None, template_items=None, template_id=None):
        """AlarmTemplate - a model defined in huaweicloud sdk"""
        
        

        self._template_name = None
        self._template_description = None
        self._namespace = None
        self._dimension_name = None
        self._template_items = None
        self._template_id = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if template_description is not None:
            self.template_description = template_description
        if namespace is not None:
            self.namespace = namespace
        if dimension_name is not None:
            self.dimension_name = dimension_name
        if template_items is not None:
            self.template_items = template_items
        if template_id is not None:
            self.template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this AlarmTemplate.

        自定义告警模板名称，如：alarmTemplate-Test01。

        :return: The template_name of this AlarmTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this AlarmTemplate.

        自定义告警模板名称，如：alarmTemplate-Test01。

        :param template_name: The template_name of this AlarmTemplate.
        :type: str
        """
        self._template_name = template_name

    @property
    def template_description(self):
        """Gets the template_description of this AlarmTemplate.

        自定义告警模板描述。

        :return: The template_description of this AlarmTemplate.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this AlarmTemplate.

        自定义告警模板描述。

        :param template_description: The template_description of this AlarmTemplate.
        :type: str
        """
        self._template_description = template_description

    @property
    def namespace(self):
        """Gets the namespace of this AlarmTemplate.

        自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS，各资源的监控指标名称可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this AlarmTemplate.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AlarmTemplate.

        自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS，各资源的监控指标名称可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this AlarmTemplate.
        :type: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        """Gets the dimension_name of this AlarmTemplate.

        自定义告警模板选择的资源维度，如：弹性云服务器，则维度为instance_id，各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dimension_name of this AlarmTemplate.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        """Sets the dimension_name of this AlarmTemplate.

        自定义告警模板选择的资源维度，如：弹性云服务器，则维度为instance_id，各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dimension_name: The dimension_name of this AlarmTemplate.
        :type: str
        """
        self._dimension_name = dimension_name

    @property
    def template_items(self):
        """Gets the template_items of this AlarmTemplate.

        自定义告警模板添加的一组或者多个告警策略。

        :return: The template_items of this AlarmTemplate.
        :rtype: list[TemplateItem]
        """
        return self._template_items

    @template_items.setter
    def template_items(self, template_items):
        """Sets the template_items of this AlarmTemplate.

        自定义告警模板添加的一组或者多个告警策略。

        :param template_items: The template_items of this AlarmTemplate.
        :type: list[TemplateItem]
        """
        self._template_items = template_items

    @property
    def template_id(self):
        """Gets the template_id of this AlarmTemplate.

        自定义告警模板的ID，如：at1603330892378wkDm77y6B。

        :return: The template_id of this AlarmTemplate.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this AlarmTemplate.

        自定义告警模板的ID，如：at1603330892378wkDm77y6B。

        :param template_id: The template_id of this AlarmTemplate.
        :type: str
        """
        self._template_id = template_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlarmTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
