# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlansRequest:

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
        'name': 'str',
        'current_stage': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'current_stage': 'current_stage',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, name=None, current_stage=None, offset=None, limit=None):
        r"""ShowPlansRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id，项目唯一标识，固定长度32位字符
        :type project_id: str
        :param name: 模糊查询使用(针对测试计划名称)
        :type name: str
        :param current_stage: 测试计划所处阶段（create,design,execute,report）
        :type current_stage: str
        :param offset: 页号，取值范围为1-20000
        :type offset: int
        :param limit: 每页显示的条目数量，取值范围为1-200
        :type limit: int
        """
        
        

        self._project_id = None
        self._name = None
        self._current_stage = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        if name is not None:
            self.name = name
        if current_stage is not None:
            self.current_stage = current_stage
        self.offset = offset
        self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPlansRequest.

        项目id，项目唯一标识，固定长度32位字符

        :return: The project_id of this ShowPlansRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPlansRequest.

        项目id，项目唯一标识，固定长度32位字符

        :param project_id: The project_id of this ShowPlansRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this ShowPlansRequest.

        模糊查询使用(针对测试计划名称)

        :return: The name of this ShowPlansRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPlansRequest.

        模糊查询使用(针对测试计划名称)

        :param name: The name of this ShowPlansRequest.
        :type name: str
        """
        self._name = name

    @property
    def current_stage(self):
        r"""Gets the current_stage of this ShowPlansRequest.

        测试计划所处阶段（create,design,execute,report）

        :return: The current_stage of this ShowPlansRequest.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        r"""Sets the current_stage of this ShowPlansRequest.

        测试计划所处阶段（create,design,execute,report）

        :param current_stage: The current_stage of this ShowPlansRequest.
        :type current_stage: str
        """
        self._current_stage = current_stage

    @property
    def offset(self):
        r"""Gets the offset of this ShowPlansRequest.

        页号，取值范围为1-20000

        :return: The offset of this ShowPlansRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowPlansRequest.

        页号，取值范围为1-20000

        :param offset: The offset of this ShowPlansRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowPlansRequest.

        每页显示的条目数量，取值范围为1-200

        :return: The limit of this ShowPlansRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowPlansRequest.

        每页显示的条目数量，取值范围为1-200

        :param limit: The limit of this ShowPlansRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowPlansRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
