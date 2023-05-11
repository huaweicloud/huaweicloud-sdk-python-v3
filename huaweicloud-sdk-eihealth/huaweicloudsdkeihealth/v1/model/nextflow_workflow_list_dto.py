# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowWorkflowListDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'creator': 'str',
        'source_project_name': 'str',
        'source_resource_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'creator': 'creator',
        'source_project_name': 'source_project_name',
        'source_resource_id': 'source_resource_id'
    }

    def __init__(self, id=None, name=None, description=None, labels=None, create_time=None, update_time=None, creator=None, source_project_name=None, source_resource_id=None):
        """NextflowWorkflowListDto

        The model defined in huaweicloud sdk

        :param id: 流程id
        :type id: str
        :param name: 流程名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param labels: 流程标签
        :type labels: list[str]
        :param create_time: 创建流程时间
        :type create_time: str
        :param update_time: 更新流程时间
        :type update_time: str
        :param creator: 创建用户名称
        :type creator: str
        :param source_project_name: 源项目名称
        :type source_project_name: str
        :param source_resource_id: 源资源id
        :type source_resource_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._labels = None
        self._create_time = None
        self._update_time = None
        self._creator = None
        self._source_project_name = None
        self._source_resource_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if creator is not None:
            self.creator = creator
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_resource_id is not None:
            self.source_resource_id = source_resource_id

    @property
    def id(self):
        """Gets the id of this NextflowWorkflowListDto.

        流程id

        :return: The id of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NextflowWorkflowListDto.

        流程id

        :param id: The id of this NextflowWorkflowListDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NextflowWorkflowListDto.

        流程名称

        :return: The name of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NextflowWorkflowListDto.

        流程名称

        :param name: The name of this NextflowWorkflowListDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NextflowWorkflowListDto.

        描述信息

        :return: The description of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NextflowWorkflowListDto.

        描述信息

        :param description: The description of this NextflowWorkflowListDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this NextflowWorkflowListDto.

        流程标签

        :return: The labels of this NextflowWorkflowListDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NextflowWorkflowListDto.

        流程标签

        :param labels: The labels of this NextflowWorkflowListDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def create_time(self):
        """Gets the create_time of this NextflowWorkflowListDto.

        创建流程时间

        :return: The create_time of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this NextflowWorkflowListDto.

        创建流程时间

        :param create_time: The create_time of this NextflowWorkflowListDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this NextflowWorkflowListDto.

        更新流程时间

        :return: The update_time of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this NextflowWorkflowListDto.

        更新流程时间

        :param update_time: The update_time of this NextflowWorkflowListDto.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def creator(self):
        """Gets the creator of this NextflowWorkflowListDto.

        创建用户名称

        :return: The creator of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this NextflowWorkflowListDto.

        创建用户名称

        :param creator: The creator of this NextflowWorkflowListDto.
        :type creator: str
        """
        self._creator = creator

    @property
    def source_project_name(self):
        """Gets the source_project_name of this NextflowWorkflowListDto.

        源项目名称

        :return: The source_project_name of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        """Sets the source_project_name of this NextflowWorkflowListDto.

        源项目名称

        :param source_project_name: The source_project_name of this NextflowWorkflowListDto.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_resource_id(self):
        """Gets the source_resource_id of this NextflowWorkflowListDto.

        源资源id

        :return: The source_resource_id of this NextflowWorkflowListDto.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        """Sets the source_resource_id of this NextflowWorkflowListDto.

        源资源id

        :param source_resource_id: The source_resource_id of this NextflowWorkflowListDto.
        :type source_resource_id: str
        """
        self._source_resource_id = source_resource_id

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
        if not isinstance(other, NextflowWorkflowListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
