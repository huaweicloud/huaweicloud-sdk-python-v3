# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmTemplates:

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
        'template_description': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'create_time': 'create_time',
        'template_description': 'template_description'
    }

    def __init__(self, template_id=None, template_name=None, template_type=None, create_time=None, template_description=None):
        r"""AlarmTemplates

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
        """
        
        

        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._create_time = None
        self._template_description = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        self.template_type = template_type
        self.create_time = create_time
        if template_description is not None:
            self.template_description = template_description

    @property
    def template_id(self):
        r"""Gets the template_id of this AlarmTemplates.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :return: The template_id of this AlarmTemplates.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this AlarmTemplates.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :param template_id: The template_id of this AlarmTemplates.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this AlarmTemplates.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]

        :return: The template_name of this AlarmTemplates.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this AlarmTemplates.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]

        :param template_name: The template_name of this AlarmTemplates.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this AlarmTemplates.

        :return: The template_type of this AlarmTemplates.
        :rtype: :class:`huaweicloudsdkces.v2.TemplateType`
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this AlarmTemplates.

        :param template_type: The template_type of this AlarmTemplates.
        :type template_type: :class:`huaweicloudsdkces.v2.TemplateType`
        """
        self._template_type = template_type

    @property
    def create_time(self):
        r"""Gets the create_time of this AlarmTemplates.

        告警模板的创建时间

        :return: The create_time of this AlarmTemplates.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AlarmTemplates.

        告警模板的创建时间

        :param create_time: The create_time of this AlarmTemplates.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def template_description(self):
        r"""Gets the template_description of this AlarmTemplates.

        告警模板的描述，长度范围[0,256]，该字段默认值为空字符串

        :return: The template_description of this AlarmTemplates.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        r"""Sets the template_description of this AlarmTemplates.

        告警模板的描述，长度范围[0,256]，该字段默认值为空字符串

        :param template_description: The template_description of this AlarmTemplates.
        :type template_description: str
        """
        self._template_description = template_description

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
        if not isinstance(other, AlarmTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
