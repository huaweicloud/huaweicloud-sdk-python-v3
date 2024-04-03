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
        'current_stage': 'str',
        'branch_uri': 'str',
        'query_all_version': 'bool',
        'fix_version_ids': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'current_stage': 'current_stage',
        'branch_uri': 'branch_uri',
        'query_all_version': 'query_all_version',
        'fix_version_ids': 'fix_version_ids'
    }

    def __init__(self, project_id=None, offset=None, limit=None, name=None, current_stage=None, branch_uri=None, query_all_version=None, fix_version_ids=None):
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
        :param branch_uri: 分支Uri，默认master
        :type branch_uri: str
        :param query_all_version: 是否查询所有版本下测试计划，默认为false。若值为true, 查询所有版本下测试计划; 若为false, 查询branch_uri指定分支下的测试计划, branch_uri为空时默认为master
        :type query_all_version: bool
        :param fix_version_ids: 测试计划关联的迭代。迭代id以逗号间隔
        :type fix_version_ids: str
        """
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._current_stage = None
        self._branch_uri = None
        self._query_all_version = None
        self._fix_version_ids = None
        self.discriminator = None

        self.project_id = project_id
        self.offset = offset
        self.limit = limit
        if name is not None:
            self.name = name
        if current_stage is not None:
            self.current_stage = current_stage
        if branch_uri is not None:
            self.branch_uri = branch_uri
        if query_all_version is not None:
            self.query_all_version = query_all_version
        if fix_version_ids is not None:
            self.fix_version_ids = fix_version_ids

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

    @property
    def branch_uri(self):
        """Gets the branch_uri of this ShowPlanListRequest.

        分支Uri，默认master

        :return: The branch_uri of this ShowPlanListRequest.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        """Sets the branch_uri of this ShowPlanListRequest.

        分支Uri，默认master

        :param branch_uri: The branch_uri of this ShowPlanListRequest.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def query_all_version(self):
        """Gets the query_all_version of this ShowPlanListRequest.

        是否查询所有版本下测试计划，默认为false。若值为true, 查询所有版本下测试计划; 若为false, 查询branch_uri指定分支下的测试计划, branch_uri为空时默认为master

        :return: The query_all_version of this ShowPlanListRequest.
        :rtype: bool
        """
        return self._query_all_version

    @query_all_version.setter
    def query_all_version(self, query_all_version):
        """Sets the query_all_version of this ShowPlanListRequest.

        是否查询所有版本下测试计划，默认为false。若值为true, 查询所有版本下测试计划; 若为false, 查询branch_uri指定分支下的测试计划, branch_uri为空时默认为master

        :param query_all_version: The query_all_version of this ShowPlanListRequest.
        :type query_all_version: bool
        """
        self._query_all_version = query_all_version

    @property
    def fix_version_ids(self):
        """Gets the fix_version_ids of this ShowPlanListRequest.

        测试计划关联的迭代。迭代id以逗号间隔

        :return: The fix_version_ids of this ShowPlanListRequest.
        :rtype: str
        """
        return self._fix_version_ids

    @fix_version_ids.setter
    def fix_version_ids(self, fix_version_ids):
        """Sets the fix_version_ids of this ShowPlanListRequest.

        测试计划关联的迭代。迭代id以逗号间隔

        :param fix_version_ids: The fix_version_ids of this ShowPlanListRequest.
        :type fix_version_ids: str
        """
        self._fix_version_ids = fix_version_ids

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
