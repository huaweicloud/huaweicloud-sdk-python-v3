# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsTemplateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'template_name': 'str',
        'create_time': 'str',
        'template_type': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'signature_id': 'str',
        'template_content': 'str',
        'template_desc': 'str',
        'has_variable': 'str',
        'flow_status': 'str',
        'status': 'str',
        'universal_template': 'int',
        'urge_status': 'str',
        'urge_time': 'str',
        'urge_desc': 'str',
        'review_desc': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'create_time': 'create_time',
        'template_type': 'template_type',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'signature_id': 'signature_id',
        'template_content': 'template_content',
        'template_desc': 'template_desc',
        'has_variable': 'has_variable',
        'flow_status': 'flow_status',
        'status': 'status',
        'universal_template': 'universal_template',
        'urge_status': 'urge_status',
        'urge_time': 'urge_time',
        'urge_desc': 'urge_desc',
        'review_desc': 'review_desc'
    }

    def __init__(self, template_id=None, template_name=None, create_time=None, template_type=None, app_id=None, app_name=None, signature_id=None, template_content=None, template_desc=None, has_variable=None, flow_status=None, status=None, universal_template=None, urge_status=None, urge_time=None, urge_desc=None, review_desc=None):
        """SmsTemplateInfo

        The model defined in huaweicloud sdk

        :param template_id: 模板ID。
        :type template_id: str
        :param template_name: 模板名称。
        :type template_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param template_type: 模板类型。
        :type template_type: str
        :param app_id: 应用ID。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param signature_id: 签名ID。
        :type signature_id: str
        :param template_content: 模板内容。
        :type template_content: str
        :param template_desc: 申请描述。
        :type template_desc: str
        :param has_variable: 是否有变量。
        :type has_variable: str
        :param flow_status: 流程状态。
        :type flow_status: str
        :param status: 模板状态。
        :type status: str
        :param universal_template: 是否是通用模板。
        :type universal_template: int
        :param urge_status: 催审状态。
        :type urge_status: str
        :param urge_time: 催审时间。
        :type urge_time: str
        :param urge_desc: 催审描述。
        :type urge_desc: str
        :param review_desc: 审批描述。
        :type review_desc: str
        """
        
        

        self._template_id = None
        self._template_name = None
        self._create_time = None
        self._template_type = None
        self._app_id = None
        self._app_name = None
        self._signature_id = None
        self._template_content = None
        self._template_desc = None
        self._has_variable = None
        self._flow_status = None
        self._status = None
        self._universal_template = None
        self._urge_status = None
        self._urge_time = None
        self._urge_desc = None
        self._review_desc = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if create_time is not None:
            self.create_time = create_time
        if template_type is not None:
            self.template_type = template_type
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if signature_id is not None:
            self.signature_id = signature_id
        if template_content is not None:
            self.template_content = template_content
        if template_desc is not None:
            self.template_desc = template_desc
        if has_variable is not None:
            self.has_variable = has_variable
        if flow_status is not None:
            self.flow_status = flow_status
        if status is not None:
            self.status = status
        if universal_template is not None:
            self.universal_template = universal_template
        if urge_status is not None:
            self.urge_status = urge_status
        if urge_time is not None:
            self.urge_time = urge_time
        if urge_desc is not None:
            self.urge_desc = urge_desc
        if review_desc is not None:
            self.review_desc = review_desc

    @property
    def template_id(self):
        """Gets the template_id of this SmsTemplateInfo.

        模板ID。

        :return: The template_id of this SmsTemplateInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this SmsTemplateInfo.

        模板ID。

        :param template_id: The template_id of this SmsTemplateInfo.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this SmsTemplateInfo.

        模板名称。

        :return: The template_name of this SmsTemplateInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this SmsTemplateInfo.

        模板名称。

        :param template_name: The template_name of this SmsTemplateInfo.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def create_time(self):
        """Gets the create_time of this SmsTemplateInfo.

        创建时间。

        :return: The create_time of this SmsTemplateInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SmsTemplateInfo.

        创建时间。

        :param create_time: The create_time of this SmsTemplateInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def template_type(self):
        """Gets the template_type of this SmsTemplateInfo.

        模板类型。

        :return: The template_type of this SmsTemplateInfo.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this SmsTemplateInfo.

        模板类型。

        :param template_type: The template_type of this SmsTemplateInfo.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def app_id(self):
        """Gets the app_id of this SmsTemplateInfo.

        应用ID。

        :return: The app_id of this SmsTemplateInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SmsTemplateInfo.

        应用ID。

        :param app_id: The app_id of this SmsTemplateInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this SmsTemplateInfo.

        应用名称。

        :return: The app_name of this SmsTemplateInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this SmsTemplateInfo.

        应用名称。

        :param app_name: The app_name of this SmsTemplateInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def signature_id(self):
        """Gets the signature_id of this SmsTemplateInfo.

        签名ID。

        :return: The signature_id of this SmsTemplateInfo.
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """Sets the signature_id of this SmsTemplateInfo.

        签名ID。

        :param signature_id: The signature_id of this SmsTemplateInfo.
        :type signature_id: str
        """
        self._signature_id = signature_id

    @property
    def template_content(self):
        """Gets the template_content of this SmsTemplateInfo.

        模板内容。

        :return: The template_content of this SmsTemplateInfo.
        :rtype: str
        """
        return self._template_content

    @template_content.setter
    def template_content(self, template_content):
        """Sets the template_content of this SmsTemplateInfo.

        模板内容。

        :param template_content: The template_content of this SmsTemplateInfo.
        :type template_content: str
        """
        self._template_content = template_content

    @property
    def template_desc(self):
        """Gets the template_desc of this SmsTemplateInfo.

        申请描述。

        :return: The template_desc of this SmsTemplateInfo.
        :rtype: str
        """
        return self._template_desc

    @template_desc.setter
    def template_desc(self, template_desc):
        """Sets the template_desc of this SmsTemplateInfo.

        申请描述。

        :param template_desc: The template_desc of this SmsTemplateInfo.
        :type template_desc: str
        """
        self._template_desc = template_desc

    @property
    def has_variable(self):
        """Gets the has_variable of this SmsTemplateInfo.

        是否有变量。

        :return: The has_variable of this SmsTemplateInfo.
        :rtype: str
        """
        return self._has_variable

    @has_variable.setter
    def has_variable(self, has_variable):
        """Sets the has_variable of this SmsTemplateInfo.

        是否有变量。

        :param has_variable: The has_variable of this SmsTemplateInfo.
        :type has_variable: str
        """
        self._has_variable = has_variable

    @property
    def flow_status(self):
        """Gets the flow_status of this SmsTemplateInfo.

        流程状态。

        :return: The flow_status of this SmsTemplateInfo.
        :rtype: str
        """
        return self._flow_status

    @flow_status.setter
    def flow_status(self, flow_status):
        """Sets the flow_status of this SmsTemplateInfo.

        流程状态。

        :param flow_status: The flow_status of this SmsTemplateInfo.
        :type flow_status: str
        """
        self._flow_status = flow_status

    @property
    def status(self):
        """Gets the status of this SmsTemplateInfo.

        模板状态。

        :return: The status of this SmsTemplateInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SmsTemplateInfo.

        模板状态。

        :param status: The status of this SmsTemplateInfo.
        :type status: str
        """
        self._status = status

    @property
    def universal_template(self):
        """Gets the universal_template of this SmsTemplateInfo.

        是否是通用模板。

        :return: The universal_template of this SmsTemplateInfo.
        :rtype: int
        """
        return self._universal_template

    @universal_template.setter
    def universal_template(self, universal_template):
        """Sets the universal_template of this SmsTemplateInfo.

        是否是通用模板。

        :param universal_template: The universal_template of this SmsTemplateInfo.
        :type universal_template: int
        """
        self._universal_template = universal_template

    @property
    def urge_status(self):
        """Gets the urge_status of this SmsTemplateInfo.

        催审状态。

        :return: The urge_status of this SmsTemplateInfo.
        :rtype: str
        """
        return self._urge_status

    @urge_status.setter
    def urge_status(self, urge_status):
        """Sets the urge_status of this SmsTemplateInfo.

        催审状态。

        :param urge_status: The urge_status of this SmsTemplateInfo.
        :type urge_status: str
        """
        self._urge_status = urge_status

    @property
    def urge_time(self):
        """Gets the urge_time of this SmsTemplateInfo.

        催审时间。

        :return: The urge_time of this SmsTemplateInfo.
        :rtype: str
        """
        return self._urge_time

    @urge_time.setter
    def urge_time(self, urge_time):
        """Sets the urge_time of this SmsTemplateInfo.

        催审时间。

        :param urge_time: The urge_time of this SmsTemplateInfo.
        :type urge_time: str
        """
        self._urge_time = urge_time

    @property
    def urge_desc(self):
        """Gets the urge_desc of this SmsTemplateInfo.

        催审描述。

        :return: The urge_desc of this SmsTemplateInfo.
        :rtype: str
        """
        return self._urge_desc

    @urge_desc.setter
    def urge_desc(self, urge_desc):
        """Sets the urge_desc of this SmsTemplateInfo.

        催审描述。

        :param urge_desc: The urge_desc of this SmsTemplateInfo.
        :type urge_desc: str
        """
        self._urge_desc = urge_desc

    @property
    def review_desc(self):
        """Gets the review_desc of this SmsTemplateInfo.

        审批描述。

        :return: The review_desc of this SmsTemplateInfo.
        :rtype: str
        """
        return self._review_desc

    @review_desc.setter
    def review_desc(self, review_desc):
        """Sets the review_desc of this SmsTemplateInfo.

        审批描述。

        :param review_desc: The review_desc of this SmsTemplateInfo.
        :type review_desc: str
        """
        self._review_desc = review_desc

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
        if not isinstance(other, SmsTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
