# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlanListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'current_stage': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'current_stage': 'current_stage'
    }

    def __init__(self, project_id=None, offset=None, limit=None, name=None, current_stage=None):
        """ShowPlanListRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id，项目唯一标识，固定长度32位字符
        :type project_id: str
        :param offset: 起始偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量,最大支持200条
        :type limit: int
        :param name: 模糊查询使用(针对测试计划名称)
        :type name: str
        :param current_stage: 测试计划所处阶段（create,design,execute,report）
        :type current_stage: str
        """
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._current_stage = None
        self.discriminator = None

        self.project_id = project_id
        self.offset = offset
        self.limit = limit
        if name is not None:
            self.name = name
        if current_stage is not None:
            self.current_stage = current_stage

    @property
    def project_id(self):
        """Gets the project_id of this ShowPlanListRequest.

        项目id，项目唯一标识，固定长度32位字符

        :return: The project_id of this ShowPlanListRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowPlanListRequest.

        项目id，项目唯一标识，固定长度32位字符

        :param project_id: The project_id of this ShowPlanListRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        """Gets the offset of this ShowPlanListRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ShowPlanListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowPlanListRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ShowPlanListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowPlanListRequest.

        每页显示的条目数量,最大支持200条

        :return: The limit of this ShowPlanListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowPlanListRequest.

        每页显示的条目数量,最大支持200条

        :param limit: The limit of this ShowPlanListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ShowPlanListRequest.

        模糊查询使用(针对测试计划名称)

        :return: The name of this ShowPlanListRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowPlanListRequest.

        模糊查询使用(针对测试计划名称)

        :param name: The name of this ShowPlanListRequest.
        :type name: str
        """
        self._name = name

    @property
    def current_stage(self):
        """Gets the current_stage of this ShowPlanListRequest.

        测试计划所处阶段（create,design,execute,report）

        :return: The current_stage of this ShowPlanListRequest.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this ShowPlanListRequest.

        测试计划所处阶段（create,design,execute,report）

        :param current_stage: The current_stage of this ShowPlanListRequest.
        :type current_stage: str
        """
        self._current_stage = current_stage

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
        if not isinstance(other, ShowPlanListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
