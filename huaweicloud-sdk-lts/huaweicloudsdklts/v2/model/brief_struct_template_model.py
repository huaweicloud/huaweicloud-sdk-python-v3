# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BriefStructTemplateModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'id': 'id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'project_id': 'project_id'
    }

    def __init__(self, create_time=None, id=None, template_name=None, template_type=None, project_id=None):
        """BriefStructTemplateModel

        The model defined in huaweicloud sdk

        :param create_time: 模板创建/更新时间
        :type create_time: int
        :param id: 模板id
        :type id: str
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 结构化类型，当前支持regex,json,split,nginx
        :type template_type: str
        :param project_id: 项目ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。
        :type project_id: str
        """
        
        

        self._create_time = None
        self._id = None
        self._template_name = None
        self._template_type = None
        self._project_id = None
        self.discriminator = None

        self.create_time = create_time
        self.id = id
        self.template_name = template_name
        self.template_type = template_type
        self.project_id = project_id

    @property
    def create_time(self):
        """Gets the create_time of this BriefStructTemplateModel.

        模板创建/更新时间

        :return: The create_time of this BriefStructTemplateModel.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BriefStructTemplateModel.

        模板创建/更新时间

        :param create_time: The create_time of this BriefStructTemplateModel.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this BriefStructTemplateModel.

        模板id

        :return: The id of this BriefStructTemplateModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BriefStructTemplateModel.

        模板id

        :param id: The id of this BriefStructTemplateModel.
        :type id: str
        """
        self._id = id

    @property
    def template_name(self):
        """Gets the template_name of this BriefStructTemplateModel.

        模板名称

        :return: The template_name of this BriefStructTemplateModel.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this BriefStructTemplateModel.

        模板名称

        :param template_name: The template_name of this BriefStructTemplateModel.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        """Gets the template_type of this BriefStructTemplateModel.

        结构化类型，当前支持regex,json,split,nginx

        :return: The template_type of this BriefStructTemplateModel.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this BriefStructTemplateModel.

        结构化类型，当前支持regex,json,split,nginx

        :param template_type: The template_type of this BriefStructTemplateModel.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def project_id(self):
        """Gets the project_id of this BriefStructTemplateModel.

        项目ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :return: The project_id of this BriefStructTemplateModel.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BriefStructTemplateModel.

        项目ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :param project_id: The project_id of this BriefStructTemplateModel.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, BriefStructTemplateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
