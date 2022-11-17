# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueCustomField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'custom_field': 'str',
        'options': 'str',
        'type': 'str',
        'tracker_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'custom_field': 'custom_field',
        'options': 'options',
        'type': 'type',
        'tracker_ids': 'tracker_ids'
    }

    def __init__(self, name=None, custom_field=None, options=None, type=None, tracker_ids=None):
        """IssueCustomField

        The model defined in huaweicloud sdk

        :param name: 自定义字段
        :type name: str
        :param custom_field: 自定义字段
        :type custom_field: str
        :param options: 自定义字段的可选值，多个值以英文逗号区分
        :type options: str
        :param type: 自定义字段类型， textArea 多行文本，只能包含汉字、英文大小写字母、数字、下划线和连接符，不能超过500字符； text 单行文本， 只能包含汉字、英文大小写字母、数字、下划线和连接符，不能超过500字符； select 下拉框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项； number 数字，取值范围由用户创建自定义字段时设置； date 日期 精确到年月日， time_date 日期 精确到时分秒， 长整型时间戳； checkbox 多选框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项； radio 单选框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项；
        :type type: str
        :param tracker_ids: 自定义字段支持的工作项类型 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story
        :type tracker_ids: list[int]
        """
        
        

        self._name = None
        self._custom_field = None
        self._options = None
        self._type = None
        self._tracker_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if custom_field is not None:
            self.custom_field = custom_field
        if options is not None:
            self.options = options
        if type is not None:
            self.type = type
        if tracker_ids is not None:
            self.tracker_ids = tracker_ids

    @property
    def name(self):
        """Gets the name of this IssueCustomField.

        自定义字段

        :return: The name of this IssueCustomField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IssueCustomField.

        自定义字段

        :param name: The name of this IssueCustomField.
        :type name: str
        """
        self._name = name

    @property
    def custom_field(self):
        """Gets the custom_field of this IssueCustomField.

        自定义字段

        :return: The custom_field of this IssueCustomField.
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this IssueCustomField.

        自定义字段

        :param custom_field: The custom_field of this IssueCustomField.
        :type custom_field: str
        """
        self._custom_field = custom_field

    @property
    def options(self):
        """Gets the options of this IssueCustomField.

        自定义字段的可选值，多个值以英文逗号区分

        :return: The options of this IssueCustomField.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this IssueCustomField.

        自定义字段的可选值，多个值以英文逗号区分

        :param options: The options of this IssueCustomField.
        :type options: str
        """
        self._options = options

    @property
    def type(self):
        """Gets the type of this IssueCustomField.

        自定义字段类型， textArea 多行文本，只能包含汉字、英文大小写字母、数字、下划线和连接符，不能超过500字符； text 单行文本， 只能包含汉字、英文大小写字母、数字、下划线和连接符，不能超过500字符； select 下拉框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项； number 数字，取值范围由用户创建自定义字段时设置； date 日期 精确到年月日， time_date 日期 精确到时分秒， 长整型时间戳； checkbox 多选框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项； radio 单选框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项；

        :return: The type of this IssueCustomField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IssueCustomField.

        自定义字段类型， textArea 多行文本，只能包含汉字、英文大小写字母、数字、下划线和连接符，不能超过500字符； text 单行文本， 只能包含汉字、英文大小写字母、数字、下划线和连接符，不能超过500字符； select 下拉框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项； number 数字，取值范围由用户创建自定义字段时设置； date 日期 精确到年月日， time_date 日期 精确到时分秒， 长整型时间戳； checkbox 多选框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项； radio 单选框，只能包含汉字、英文大小写字母、数字、下划线和连接符，每个选项最大长度40个字符，最多可定义60个选项；

        :param type: The type of this IssueCustomField.
        :type type: str
        """
        self._type = type

    @property
    def tracker_ids(self):
        """Gets the tracker_ids of this IssueCustomField.

        自定义字段支持的工作项类型 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story

        :return: The tracker_ids of this IssueCustomField.
        :rtype: list[int]
        """
        return self._tracker_ids

    @tracker_ids.setter
    def tracker_ids(self, tracker_ids):
        """Sets the tracker_ids of this IssueCustomField.

        自定义字段支持的工作项类型 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story

        :param tracker_ids: The tracker_ids of this IssueCustomField.
        :type tracker_ids: list[int]
        """
        self._tracker_ids = tracker_ids

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
        if not isinstance(other, IssueCustomField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
