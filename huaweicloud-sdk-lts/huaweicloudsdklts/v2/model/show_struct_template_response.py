# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStructTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'demo_fields': 'list[StructFieldInfoReturn]',
        'tag_fields': 'list[TagFieldsInfo]',
        'demo_log': 'str',
        'demo_label': 'str',
        'id': 'str',
        'log_group_id': 'str',
        'rule': 'ShowStructTemplateRule',
        'cluster_info': 'ShowStructTemplateclusterInfo',
        'log_stream_id': 'str',
        'project_id': 'str',
        'template_name': 'str',
        'regex': 'str'
    }

    attribute_map = {
        'demo_fields': 'demoFields',
        'tag_fields': 'tagFields',
        'demo_log': 'demoLog',
        'demo_label': 'demoLabel',
        'id': 'id',
        'log_group_id': 'logGroupId',
        'rule': 'rule',
        'cluster_info': 'cluster_info',
        'log_stream_id': 'logStreamId',
        'project_id': 'projectId',
        'template_name': 'templateName',
        'regex': 'regex'
    }

    def __init__(self, demo_fields=None, tag_fields=None, demo_log=None, demo_label=None, id=None, log_group_id=None, rule=None, cluster_info=None, log_stream_id=None, project_id=None, template_name=None, regex=None):
        """ShowStructTemplateResponse

        The model defined in huaweicloud sdk

        :param demo_fields: 结构化字段
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.StructFieldInfoReturn`]
        :param tag_fields: 关键词详细信息
        :type tag_fields: list[:class:`huaweicloudsdklts.v2.TagFieldsInfo`]
        :param demo_log: 示例日志
        :type demo_log: str
        :param demo_label: 测试
        :type demo_label: str
        :param id: id
        :type id: str
        :param log_group_id: 日志组ID
        :type log_group_id: str
        :param rule: 
        :type rule: :class:`huaweicloudsdklts.v2.ShowStructTemplateRule`
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdklts.v2.ShowStructTemplateclusterInfo`
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param template_name: 测试
        :type template_name: str
        :param regex: 为了兼容前台数据格式
        :type regex: str
        """
        
        super(ShowStructTemplateResponse, self).__init__()

        self._demo_fields = None
        self._tag_fields = None
        self._demo_log = None
        self._demo_label = None
        self._id = None
        self._log_group_id = None
        self._rule = None
        self._cluster_info = None
        self._log_stream_id = None
        self._project_id = None
        self._template_name = None
        self._regex = None
        self.discriminator = None

        if demo_fields is not None:
            self.demo_fields = demo_fields
        if tag_fields is not None:
            self.tag_fields = tag_fields
        if demo_log is not None:
            self.demo_log = demo_log
        if demo_label is not None:
            self.demo_label = demo_label
        if id is not None:
            self.id = id
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if rule is not None:
            self.rule = rule
        if cluster_info is not None:
            self.cluster_info = cluster_info
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if project_id is not None:
            self.project_id = project_id
        if template_name is not None:
            self.template_name = template_name
        if regex is not None:
            self.regex = regex

    @property
    def demo_fields(self):
        """Gets the demo_fields of this ShowStructTemplateResponse.

        结构化字段

        :return: The demo_fields of this ShowStructTemplateResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.StructFieldInfoReturn`]
        """
        return self._demo_fields

    @demo_fields.setter
    def demo_fields(self, demo_fields):
        """Sets the demo_fields of this ShowStructTemplateResponse.

        结构化字段

        :param demo_fields: The demo_fields of this ShowStructTemplateResponse.
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.StructFieldInfoReturn`]
        """
        self._demo_fields = demo_fields

    @property
    def tag_fields(self):
        """Gets the tag_fields of this ShowStructTemplateResponse.

        关键词详细信息

        :return: The tag_fields of this ShowStructTemplateResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.TagFieldsInfo`]
        """
        return self._tag_fields

    @tag_fields.setter
    def tag_fields(self, tag_fields):
        """Sets the tag_fields of this ShowStructTemplateResponse.

        关键词详细信息

        :param tag_fields: The tag_fields of this ShowStructTemplateResponse.
        :type tag_fields: list[:class:`huaweicloudsdklts.v2.TagFieldsInfo`]
        """
        self._tag_fields = tag_fields

    @property
    def demo_log(self):
        """Gets the demo_log of this ShowStructTemplateResponse.

        示例日志

        :return: The demo_log of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._demo_log

    @demo_log.setter
    def demo_log(self, demo_log):
        """Sets the demo_log of this ShowStructTemplateResponse.

        示例日志

        :param demo_log: The demo_log of this ShowStructTemplateResponse.
        :type demo_log: str
        """
        self._demo_log = demo_log

    @property
    def demo_label(self):
        """Gets the demo_label of this ShowStructTemplateResponse.

        测试

        :return: The demo_label of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._demo_label

    @demo_label.setter
    def demo_label(self, demo_label):
        """Sets the demo_label of this ShowStructTemplateResponse.

        测试

        :param demo_label: The demo_label of this ShowStructTemplateResponse.
        :type demo_label: str
        """
        self._demo_label = demo_label

    @property
    def id(self):
        """Gets the id of this ShowStructTemplateResponse.

        id

        :return: The id of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowStructTemplateResponse.

        id

        :param id: The id of this ShowStructTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ShowStructTemplateResponse.

        日志组ID

        :return: The log_group_id of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ShowStructTemplateResponse.

        日志组ID

        :param log_group_id: The log_group_id of this ShowStructTemplateResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def rule(self):
        """Gets the rule of this ShowStructTemplateResponse.

        :return: The rule of this ShowStructTemplateResponse.
        :rtype: :class:`huaweicloudsdklts.v2.ShowStructTemplateRule`
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ShowStructTemplateResponse.

        :param rule: The rule of this ShowStructTemplateResponse.
        :type rule: :class:`huaweicloudsdklts.v2.ShowStructTemplateRule`
        """
        self._rule = rule

    @property
    def cluster_info(self):
        """Gets the cluster_info of this ShowStructTemplateResponse.

        :return: The cluster_info of this ShowStructTemplateResponse.
        :rtype: :class:`huaweicloudsdklts.v2.ShowStructTemplateclusterInfo`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        """Sets the cluster_info of this ShowStructTemplateResponse.

        :param cluster_info: The cluster_info of this ShowStructTemplateResponse.
        :type cluster_info: :class:`huaweicloudsdklts.v2.ShowStructTemplateclusterInfo`
        """
        self._cluster_info = cluster_info

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this ShowStructTemplateResponse.

        日志流ID

        :return: The log_stream_id of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this ShowStructTemplateResponse.

        日志流ID

        :param log_stream_id: The log_stream_id of this ShowStructTemplateResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowStructTemplateResponse.

        项目ID

        :return: The project_id of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowStructTemplateResponse.

        项目ID

        :param project_id: The project_id of this ShowStructTemplateResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def template_name(self):
        """Gets the template_name of this ShowStructTemplateResponse.

        测试

        :return: The template_name of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ShowStructTemplateResponse.

        测试

        :param template_name: The template_name of this ShowStructTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def regex(self):
        """Gets the regex of this ShowStructTemplateResponse.

        为了兼容前台数据格式

        :return: The regex of this ShowStructTemplateResponse.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this ShowStructTemplateResponse.

        为了兼容前台数据格式

        :param regex: The regex of this ShowStructTemplateResponse.
        :type regex: str
        """
        self._regex = regex

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
        if not isinstance(other, ShowStructTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
