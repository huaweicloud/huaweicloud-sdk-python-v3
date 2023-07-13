# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateVersion:

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
        'version_description': 'str',
        'create_time': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'version_description': 'version_description',
        'create_time': 'create_time',
        'version_id': 'version_id'
    }

    def __init__(self, template_id=None, template_name=None, version_description=None, create_time=None, version_id=None):
        """TemplateVersion

        The model defined in huaweicloud sdk

        :param template_id: 模板的唯一ID，由模板服务随机生成
        :type template_id: str
        :param template_name: 用户希望创建的模板名称
        :type template_name: str
        :param version_description: 模板版本的描述。可用于客户识别自己的模板版本
        :type version_description: str
        :param create_time: 版本创建时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type create_time: str
        :param version_id: 模板模板版本ID
        :type version_id: str
        """
        
        

        self._template_id = None
        self._template_name = None
        self._version_description = None
        self._create_time = None
        self._version_id = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        if version_description is not None:
            self.version_description = version_description
        self.create_time = create_time
        self.version_id = version_id

    @property
    def template_id(self):
        """Gets the template_id of this TemplateVersion.

        模板的唯一ID，由模板服务随机生成

        :return: The template_id of this TemplateVersion.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplateVersion.

        模板的唯一ID，由模板服务随机生成

        :param template_id: The template_id of this TemplateVersion.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this TemplateVersion.

        用户希望创建的模板名称

        :return: The template_name of this TemplateVersion.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TemplateVersion.

        用户希望创建的模板名称

        :param template_name: The template_name of this TemplateVersion.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def version_description(self):
        """Gets the version_description of this TemplateVersion.

        模板版本的描述。可用于客户识别自己的模板版本

        :return: The version_description of this TemplateVersion.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        """Sets the version_description of this TemplateVersion.

        模板版本的描述。可用于客户识别自己的模板版本

        :param version_description: The version_description of this TemplateVersion.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def create_time(self):
        """Gets the create_time of this TemplateVersion.

        版本创建时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The create_time of this TemplateVersion.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TemplateVersion.

        版本创建时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param create_time: The create_time of this TemplateVersion.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def version_id(self):
        """Gets the version_id of this TemplateVersion.

        模板模板版本ID

        :return: The version_id of this TemplateVersion.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this TemplateVersion.

        模板模板版本ID

        :param version_id: The version_id of this TemplateVersion.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, TemplateVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
