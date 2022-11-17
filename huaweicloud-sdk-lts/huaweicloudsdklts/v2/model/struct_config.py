# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'demo_fields': 'list[FieldModel]',
        'tag_fields': 'list[FieldModel]',
        'quick_analysis': 'bool'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'demo_fields': 'demo_fields',
        'tag_fields': 'tag_fields',
        'quick_analysis': 'quick_analysis'
    }

    def __init__(self, log_group_id=None, log_stream_id=None, template_id=None, template_name=None, template_type=None, demo_fields=None, tag_fields=None, quick_analysis=None):
        """StructConfig

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。
        :type log_group_id: str
        :param log_stream_id: 日志流ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。
        :type log_stream_id: str
        :param template_id: 所用模板id。当使用系统模板时，当前属性可以为空
        :type template_id: str
        :param template_name: 所用模板名称，会对模板名称及id进行校验
        :type template_name: str
        :param template_type: 所用模板类型，分为built_in及custom两种类型，对应系统模板和自定义模板，系统模板分为CTS，VPC和ELB三种。
        :type template_type: str
        :param demo_fields: 示例字段数组，只需要填写与模板中is_analysis状态不同的字段
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.FieldModel`]
        :param tag_fields: Tag字段数组，只需要填写与模板中is_analysis状态不同的字段
        :type tag_fields: list[:class:`huaweicloudsdklts.v2.FieldModel`]
        :param quick_analysis: 是否开启demo_fields和tag_fields快速分析,为true时，所有的demo_fields和tag_fields全部字段均打开快速分析;不填或者为false，以模板中的demo_fields和tag_fields中的is_analysis决定是否开启快速分析。
        :type quick_analysis: bool
        """
        
        

        self._log_group_id = None
        self._log_stream_id = None
        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._demo_fields = None
        self._tag_fields = None
        self._quick_analysis = None
        self.discriminator = None

        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id
        self.template_id = template_id
        self.template_name = template_name
        self.template_type = template_type
        if demo_fields is not None:
            self.demo_fields = demo_fields
        if tag_fields is not None:
            self.tag_fields = tag_fields
        if quick_analysis is not None:
            self.quick_analysis = quick_analysis

    @property
    def log_group_id(self):
        """Gets the log_group_id of this StructConfig.

        日志组ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :return: The log_group_id of this StructConfig.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this StructConfig.

        日志组ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :param log_group_id: The log_group_id of this StructConfig.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this StructConfig.

        日志流ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :return: The log_stream_id of this StructConfig.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this StructConfig.

        日志流ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :param log_stream_id: The log_stream_id of this StructConfig.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def template_id(self):
        """Gets the template_id of this StructConfig.

        所用模板id。当使用系统模板时，当前属性可以为空

        :return: The template_id of this StructConfig.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this StructConfig.

        所用模板id。当使用系统模板时，当前属性可以为空

        :param template_id: The template_id of this StructConfig.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this StructConfig.

        所用模板名称，会对模板名称及id进行校验

        :return: The template_name of this StructConfig.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this StructConfig.

        所用模板名称，会对模板名称及id进行校验

        :param template_name: The template_name of this StructConfig.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        """Gets the template_type of this StructConfig.

        所用模板类型，分为built_in及custom两种类型，对应系统模板和自定义模板，系统模板分为CTS，VPC和ELB三种。

        :return: The template_type of this StructConfig.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this StructConfig.

        所用模板类型，分为built_in及custom两种类型，对应系统模板和自定义模板，系统模板分为CTS，VPC和ELB三种。

        :param template_type: The template_type of this StructConfig.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def demo_fields(self):
        """Gets the demo_fields of this StructConfig.

        示例字段数组，只需要填写与模板中is_analysis状态不同的字段

        :return: The demo_fields of this StructConfig.
        :rtype: list[:class:`huaweicloudsdklts.v2.FieldModel`]
        """
        return self._demo_fields

    @demo_fields.setter
    def demo_fields(self, demo_fields):
        """Sets the demo_fields of this StructConfig.

        示例字段数组，只需要填写与模板中is_analysis状态不同的字段

        :param demo_fields: The demo_fields of this StructConfig.
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.FieldModel`]
        """
        self._demo_fields = demo_fields

    @property
    def tag_fields(self):
        """Gets the tag_fields of this StructConfig.

        Tag字段数组，只需要填写与模板中is_analysis状态不同的字段

        :return: The tag_fields of this StructConfig.
        :rtype: list[:class:`huaweicloudsdklts.v2.FieldModel`]
        """
        return self._tag_fields

    @tag_fields.setter
    def tag_fields(self, tag_fields):
        """Sets the tag_fields of this StructConfig.

        Tag字段数组，只需要填写与模板中is_analysis状态不同的字段

        :param tag_fields: The tag_fields of this StructConfig.
        :type tag_fields: list[:class:`huaweicloudsdklts.v2.FieldModel`]
        """
        self._tag_fields = tag_fields

    @property
    def quick_analysis(self):
        """Gets the quick_analysis of this StructConfig.

        是否开启demo_fields和tag_fields快速分析,为true时，所有的demo_fields和tag_fields全部字段均打开快速分析;不填或者为false，以模板中的demo_fields和tag_fields中的is_analysis决定是否开启快速分析。

        :return: The quick_analysis of this StructConfig.
        :rtype: bool
        """
        return self._quick_analysis

    @quick_analysis.setter
    def quick_analysis(self, quick_analysis):
        """Sets the quick_analysis of this StructConfig.

        是否开启demo_fields和tag_fields快速分析,为true时，所有的demo_fields和tag_fields全部字段均打开快速分析;不填或者为false，以模板中的demo_fields和tag_fields中的is_analysis决定是否开启快速分析。

        :param quick_analysis: The quick_analysis of this StructConfig.
        :type quick_analysis: bool
        """
        self._quick_analysis = quick_analysis

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
        if not isinstance(other, StructConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
