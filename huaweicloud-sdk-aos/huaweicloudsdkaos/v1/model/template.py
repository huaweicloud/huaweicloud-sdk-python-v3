# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Template:

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
        'template_description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'latest_version_id': 'str',
        'latest_version_description': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_description': 'template_description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'latest_version_id': 'latest_version_id',
        'latest_version_description': 'latest_version_description'
    }

    def __init__(self, template_id=None, template_name=None, template_description=None, create_time=None, update_time=None, latest_version_id=None, latest_version_description=None):
        """Template

        The model defined in huaweicloud sdk

        :param template_id: 模板的唯一ID，由模板服务随机生成
        :type template_id: str
        :param template_name: 用户希望创建的模板名称
        :type template_name: str
        :param template_description: 模板的描述。可用于客户识别自己的模板
        :type template_description: str
        :param create_time: 模板的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type create_time: str
        :param update_time: 模板的更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type update_time: str
        :param latest_version_id: 模板中最新的模板版本ID
        :type latest_version_id: str
        :param latest_version_description: 模板中最新模板版本的版本描述
        :type latest_version_description: str
        """
        
        

        self._template_id = None
        self._template_name = None
        self._template_description = None
        self._create_time = None
        self._update_time = None
        self._latest_version_id = None
        self._latest_version_description = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        if template_description is not None:
            self.template_description = template_description
        self.create_time = create_time
        self.update_time = update_time
        self.latest_version_id = latest_version_id
        self.latest_version_description = latest_version_description

    @property
    def template_id(self):
        """Gets the template_id of this Template.

        模板的唯一ID，由模板服务随机生成

        :return: The template_id of this Template.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Template.

        模板的唯一ID，由模板服务随机生成

        :param template_id: The template_id of this Template.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this Template.

        用户希望创建的模板名称

        :return: The template_name of this Template.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this Template.

        用户希望创建的模板名称

        :param template_name: The template_name of this Template.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_description(self):
        """Gets the template_description of this Template.

        模板的描述。可用于客户识别自己的模板

        :return: The template_description of this Template.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this Template.

        模板的描述。可用于客户识别自己的模板

        :param template_description: The template_description of this Template.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def create_time(self):
        """Gets the create_time of this Template.

        模板的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The create_time of this Template.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Template.

        模板的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param create_time: The create_time of this Template.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Template.

        模板的更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The update_time of this Template.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Template.

        模板的更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param update_time: The update_time of this Template.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def latest_version_id(self):
        """Gets the latest_version_id of this Template.

        模板中最新的模板版本ID

        :return: The latest_version_id of this Template.
        :rtype: str
        """
        return self._latest_version_id

    @latest_version_id.setter
    def latest_version_id(self, latest_version_id):
        """Sets the latest_version_id of this Template.

        模板中最新的模板版本ID

        :param latest_version_id: The latest_version_id of this Template.
        :type latest_version_id: str
        """
        self._latest_version_id = latest_version_id

    @property
    def latest_version_description(self):
        """Gets the latest_version_description of this Template.

        模板中最新模板版本的版本描述

        :return: The latest_version_description of this Template.
        :rtype: str
        """
        return self._latest_version_description

    @latest_version_description.setter
    def latest_version_description(self, latest_version_description):
        """Sets the latest_version_description of this Template.

        模板中最新模板版本的版本描述

        :param latest_version_description: The latest_version_description of this Template.
        :type latest_version_description: str
        """
        self._latest_version_description = latest_version_description

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
        if not isinstance(other, Template):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
