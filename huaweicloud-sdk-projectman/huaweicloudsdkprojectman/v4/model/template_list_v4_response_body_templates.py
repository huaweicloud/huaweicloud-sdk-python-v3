# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateListV4ResponseBodyTemplates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'project_id': 'int',
        'tracker_id': 'int',
        'description': 'str',
        'issue_field_config': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'tracker_id': 'tracker_id',
        'description': 'description',
        'issue_field_config': 'issue_field_config'
    }

    def __init__(self, id=None, project_id=None, tracker_id=None, description=None, issue_field_config=None):
        """TemplateListV4ResponseBodyTemplates

        The model defined in huaweicloud sdk

        :param id: 模板id
        :type id: int
        :param project_id: 项目id
        :type project_id: int
        :param tracker_id: 工作项类型id
        :type tracker_id: int
        :param description: 工作项详情模板描述内容
        :type description: str
        :param issue_field_config: 模板配置
        :type issue_field_config: str
        """
        
        

        self._id = None
        self._project_id = None
        self._tracker_id = None
        self._description = None
        self._issue_field_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if description is not None:
            self.description = description
        if issue_field_config is not None:
            self.issue_field_config = issue_field_config

    @property
    def id(self):
        """Gets the id of this TemplateListV4ResponseBodyTemplates.

        模板id

        :return: The id of this TemplateListV4ResponseBodyTemplates.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateListV4ResponseBodyTemplates.

        模板id

        :param id: The id of this TemplateListV4ResponseBodyTemplates.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this TemplateListV4ResponseBodyTemplates.

        项目id

        :return: The project_id of this TemplateListV4ResponseBodyTemplates.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TemplateListV4ResponseBodyTemplates.

        项目id

        :param project_id: The project_id of this TemplateListV4ResponseBodyTemplates.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def tracker_id(self):
        """Gets the tracker_id of this TemplateListV4ResponseBodyTemplates.

        工作项类型id

        :return: The tracker_id of this TemplateListV4ResponseBodyTemplates.
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this TemplateListV4ResponseBodyTemplates.

        工作项类型id

        :param tracker_id: The tracker_id of this TemplateListV4ResponseBodyTemplates.
        :type tracker_id: int
        """
        self._tracker_id = tracker_id

    @property
    def description(self):
        """Gets the description of this TemplateListV4ResponseBodyTemplates.

        工作项详情模板描述内容

        :return: The description of this TemplateListV4ResponseBodyTemplates.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateListV4ResponseBodyTemplates.

        工作项详情模板描述内容

        :param description: The description of this TemplateListV4ResponseBodyTemplates.
        :type description: str
        """
        self._description = description

    @property
    def issue_field_config(self):
        """Gets the issue_field_config of this TemplateListV4ResponseBodyTemplates.

        模板配置

        :return: The issue_field_config of this TemplateListV4ResponseBodyTemplates.
        :rtype: str
        """
        return self._issue_field_config

    @issue_field_config.setter
    def issue_field_config(self, issue_field_config):
        """Sets the issue_field_config of this TemplateListV4ResponseBodyTemplates.

        模板配置

        :param issue_field_config: The issue_field_config of this TemplateListV4ResponseBodyTemplates.
        :type issue_field_config: str
        """
        self._issue_field_config = issue_field_config

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
        if not isinstance(other, TemplateListV4ResponseBodyTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
