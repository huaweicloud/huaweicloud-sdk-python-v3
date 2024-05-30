# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStandardTemplateResultDataValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_fields': 'list[StandElementFieldVO]',
        'optional': 'list[StandElementFieldVO]',
        'system_default': 'list[StandElementFieldVO]',
        'custom': 'list[StandElementFieldVO]',
        'has_template': 'bool'
    }

    attribute_map = {
        'all_fields': 'allFields',
        'optional': 'optional',
        'system_default': 'system_default',
        'custom': 'custom',
        'has_template': 'hasTemplate'
    }

    def __init__(self, all_fields=None, optional=None, system_default=None, custom=None, has_template=None):
        """ShowStandardTemplateResultDataValue

        The model defined in huaweicloud sdk

        :param all_fields: 数据标准全部属性，集合中是单个StandElementFieldVO对象
        :type all_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        :param optional: 可选项,集合中是单个StandElementFieldVO对象
        :type optional: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        :param system_default: 系统默认项，集合中是单个StandElementFieldVO对象
        :type system_default: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        :param custom: 自定义项,集合中是单个StandElementFieldVO对象
        :type custom: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        :param has_template: 是否使用模板
        :type has_template: bool
        """
        
        

        self._all_fields = None
        self._optional = None
        self._system_default = None
        self._custom = None
        self._has_template = None
        self.discriminator = None

        if all_fields is not None:
            self.all_fields = all_fields
        if optional is not None:
            self.optional = optional
        if system_default is not None:
            self.system_default = system_default
        if custom is not None:
            self.custom = custom
        if has_template is not None:
            self.has_template = has_template

    @property
    def all_fields(self):
        """Gets the all_fields of this ShowStandardTemplateResultDataValue.

        数据标准全部属性，集合中是单个StandElementFieldVO对象

        :return: The all_fields of this ShowStandardTemplateResultDataValue.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this ShowStandardTemplateResultDataValue.

        数据标准全部属性，集合中是单个StandElementFieldVO对象

        :param all_fields: The all_fields of this ShowStandardTemplateResultDataValue.
        :type all_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        self._all_fields = all_fields

    @property
    def optional(self):
        """Gets the optional of this ShowStandardTemplateResultDataValue.

        可选项,集合中是单个StandElementFieldVO对象

        :return: The optional of this ShowStandardTemplateResultDataValue.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this ShowStandardTemplateResultDataValue.

        可选项,集合中是单个StandElementFieldVO对象

        :param optional: The optional of this ShowStandardTemplateResultDataValue.
        :type optional: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        self._optional = optional

    @property
    def system_default(self):
        """Gets the system_default of this ShowStandardTemplateResultDataValue.

        系统默认项，集合中是单个StandElementFieldVO对象

        :return: The system_default of this ShowStandardTemplateResultDataValue.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        return self._system_default

    @system_default.setter
    def system_default(self, system_default):
        """Sets the system_default of this ShowStandardTemplateResultDataValue.

        系统默认项，集合中是单个StandElementFieldVO对象

        :param system_default: The system_default of this ShowStandardTemplateResultDataValue.
        :type system_default: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        self._system_default = system_default

    @property
    def custom(self):
        """Gets the custom of this ShowStandardTemplateResultDataValue.

        自定义项,集合中是单个StandElementFieldVO对象

        :return: The custom of this ShowStandardTemplateResultDataValue.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this ShowStandardTemplateResultDataValue.

        自定义项,集合中是单个StandElementFieldVO对象

        :param custom: The custom of this ShowStandardTemplateResultDataValue.
        :type custom: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementFieldVO`]
        """
        self._custom = custom

    @property
    def has_template(self):
        """Gets the has_template of this ShowStandardTemplateResultDataValue.

        是否使用模板

        :return: The has_template of this ShowStandardTemplateResultDataValue.
        :rtype: bool
        """
        return self._has_template

    @has_template.setter
    def has_template(self, has_template):
        """Sets the has_template of this ShowStandardTemplateResultDataValue.

        是否使用模板

        :param has_template: The has_template of this ShowStandardTemplateResultDataValue.
        :type has_template: bool
        """
        self._has_template = has_template

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
        if not isinstance(other, ShowStandardTemplateResultDataValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
