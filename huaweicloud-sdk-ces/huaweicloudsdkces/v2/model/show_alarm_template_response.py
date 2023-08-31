# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmTemplateResponse(SdkResponse):

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
        'template_type': 'TemplateType',
        'create_time': 'datetime',
        'template_description': 'str',
        'policies': 'list[AlarmTemplatePolicies]'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'create_time': 'create_time',
        'template_description': 'template_description',
        'policies': 'policies'
    }

    def __init__(self, template_id=None, template_name=None, template_type=None, create_time=None, template_description=None, policies=None):
        """ShowAlarmTemplateResponse

        The model defined in huaweicloud sdk

        :param template_id: 告警模板的ID，以at开头，后跟字母、数字，长度最长为64
        :type template_id: str
        :param template_name: 告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]
        :type template_name: str
        :param template_type: 
        :type template_type: :class:`huaweicloudsdkces.v2.TemplateType`
        :param create_time: 告警模板的创建时间
        :type create_time: datetime
        :param template_description: 告警模板的描述，长度范围[0,256]，该字段默认值为空字符串
        :type template_description: str
        :param policies: 告警模板策略列表
        :type policies: list[:class:`huaweicloudsdkces.v2.AlarmTemplatePolicies`]
        """
        
        super(ShowAlarmTemplateResponse, self).__init__()

        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._create_time = None
        self._template_description = None
        self._policies = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type
        if create_time is not None:
            self.create_time = create_time
        if template_description is not None:
            self.template_description = template_description
        if policies is not None:
            self.policies = policies

    @property
    def template_id(self):
        """Gets the template_id of this ShowAlarmTemplateResponse.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :return: The template_id of this ShowAlarmTemplateResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ShowAlarmTemplateResponse.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :param template_id: The template_id of this ShowAlarmTemplateResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this ShowAlarmTemplateResponse.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]

        :return: The template_name of this ShowAlarmTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ShowAlarmTemplateResponse.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]

        :param template_name: The template_name of this ShowAlarmTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        """Gets the template_type of this ShowAlarmTemplateResponse.

        :return: The template_type of this ShowAlarmTemplateResponse.
        :rtype: :class:`huaweicloudsdkces.v2.TemplateType`
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ShowAlarmTemplateResponse.

        :param template_type: The template_type of this ShowAlarmTemplateResponse.
        :type template_type: :class:`huaweicloudsdkces.v2.TemplateType`
        """
        self._template_type = template_type

    @property
    def create_time(self):
        """Gets the create_time of this ShowAlarmTemplateResponse.

        告警模板的创建时间

        :return: The create_time of this ShowAlarmTemplateResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAlarmTemplateResponse.

        告警模板的创建时间

        :param create_time: The create_time of this ShowAlarmTemplateResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def template_description(self):
        """Gets the template_description of this ShowAlarmTemplateResponse.

        告警模板的描述，长度范围[0,256]，该字段默认值为空字符串

        :return: The template_description of this ShowAlarmTemplateResponse.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this ShowAlarmTemplateResponse.

        告警模板的描述，长度范围[0,256]，该字段默认值为空字符串

        :param template_description: The template_description of this ShowAlarmTemplateResponse.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def policies(self):
        """Gets the policies of this ShowAlarmTemplateResponse.

        告警模板策略列表

        :return: The policies of this ShowAlarmTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.AlarmTemplatePolicies`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ShowAlarmTemplateResponse.

        告警模板策略列表

        :param policies: The policies of this ShowAlarmTemplateResponse.
        :type policies: list[:class:`huaweicloudsdkces.v2.AlarmTemplatePolicies`]
        """
        self._policies = policies

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
        if not isinstance(other, ShowAlarmTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
