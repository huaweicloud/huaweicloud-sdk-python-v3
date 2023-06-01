# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseInfoDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'int',
        'name': 'str',
        'case_type': 'int',
        'contents': 'list[Contents]',
        'for_loop_params': 'list[object]',
        'increase_setting': 'list[object]',
        'stages': 'list[TestCaseStage]',
        'status': 'int',
        'temp_id': 'int',
        'sort': 'int',
        'directory_id': 'int',
        'setup_contents': 'list[Contents]',
        'user_replicas': 'int',
        'collect_log_policy': 'int',
        'link_app_list': 'list[int]',
        'case_info': 'CaseDoc'
    }

    attribute_map = {
        'case_id': 'case_id',
        'name': 'name',
        'case_type': 'case_type',
        'contents': 'contents',
        'for_loop_params': 'for_loop_params',
        'increase_setting': 'increase_setting',
        'stages': 'stages',
        'status': 'status',
        'temp_id': 'temp_id',
        'sort': 'sort',
        'directory_id': 'directory_id',
        'setup_contents': 'setup_contents',
        'user_replicas': 'user_replicas',
        'collect_log_policy': 'collect_log_policy',
        'link_app_list': 'link_app_list',
        'case_info': 'case_info'
    }

    def __init__(self, case_id=None, name=None, case_type=None, contents=None, for_loop_params=None, increase_setting=None, stages=None, status=None, temp_id=None, sort=None, directory_id=None, setup_contents=None, user_replicas=None, collect_log_policy=None, link_app_list=None, case_info=None):
        """CaseInfoDetail

        The model defined in huaweicloud sdk

        :param case_id: case_id
        :type case_id: int
        :param name: 用例名称
        :type name: str
        :param case_type: case_type
        :type case_type: int
        :param contents: contents
        :type contents: list[:class:`huaweicloudsdkcpts.v1.Contents`]
        :param for_loop_params: for_loop_params
        :type for_loop_params: list[object]
        :param increase_setting: increase_setting
        :type increase_setting: list[object]
        :param stages: stages
        :type stages: list[:class:`huaweicloudsdkcpts.v1.TestCaseStage`]
        :param status: 状态，0：已删除；1：启用；2：禁用
        :type status: int
        :param temp_id: temp_id
        :type temp_id: int
        :param sort: 排序字段
        :type sort: int
        :param directory_id: 用例所属目录id（旧版接口可不传）
        :type directory_id: int
        :param setup_contents: 前置步骤
        :type setup_contents: list[:class:`huaweicloudsdkcpts.v1.Contents`]
        :param user_replicas: 执行器个数
        :type user_replicas: int
        :param collect_log_policy: 日志采集策略（0-请求模式；1-用例模式）
        :type collect_log_policy: int
        :param link_app_list: 关联全链路应用列表
        :type link_app_list: list[int]
        :param case_info: 
        :type case_info: :class:`huaweicloudsdkcpts.v1.CaseDoc`
        """
        
        

        self._case_id = None
        self._name = None
        self._case_type = None
        self._contents = None
        self._for_loop_params = None
        self._increase_setting = None
        self._stages = None
        self._status = None
        self._temp_id = None
        self._sort = None
        self._directory_id = None
        self._setup_contents = None
        self._user_replicas = None
        self._collect_log_policy = None
        self._link_app_list = None
        self._case_info = None
        self.discriminator = None

        if case_id is not None:
            self.case_id = case_id
        if name is not None:
            self.name = name
        if case_type is not None:
            self.case_type = case_type
        if contents is not None:
            self.contents = contents
        if for_loop_params is not None:
            self.for_loop_params = for_loop_params
        if increase_setting is not None:
            self.increase_setting = increase_setting
        if stages is not None:
            self.stages = stages
        if status is not None:
            self.status = status
        if temp_id is not None:
            self.temp_id = temp_id
        if sort is not None:
            self.sort = sort
        if directory_id is not None:
            self.directory_id = directory_id
        if setup_contents is not None:
            self.setup_contents = setup_contents
        if user_replicas is not None:
            self.user_replicas = user_replicas
        if collect_log_policy is not None:
            self.collect_log_policy = collect_log_policy
        if link_app_list is not None:
            self.link_app_list = link_app_list
        if case_info is not None:
            self.case_info = case_info

    @property
    def case_id(self):
        """Gets the case_id of this CaseInfoDetail.

        case_id

        :return: The case_id of this CaseInfoDetail.
        :rtype: int
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this CaseInfoDetail.

        case_id

        :param case_id: The case_id of this CaseInfoDetail.
        :type case_id: int
        """
        self._case_id = case_id

    @property
    def name(self):
        """Gets the name of this CaseInfoDetail.

        用例名称

        :return: The name of this CaseInfoDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CaseInfoDetail.

        用例名称

        :param name: The name of this CaseInfoDetail.
        :type name: str
        """
        self._name = name

    @property
    def case_type(self):
        """Gets the case_type of this CaseInfoDetail.

        case_type

        :return: The case_type of this CaseInfoDetail.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        """Sets the case_type of this CaseInfoDetail.

        case_type

        :param case_type: The case_type of this CaseInfoDetail.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def contents(self):
        """Gets the contents of this CaseInfoDetail.

        contents

        :return: The contents of this CaseInfoDetail.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.Contents`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this CaseInfoDetail.

        contents

        :param contents: The contents of this CaseInfoDetail.
        :type contents: list[:class:`huaweicloudsdkcpts.v1.Contents`]
        """
        self._contents = contents

    @property
    def for_loop_params(self):
        """Gets the for_loop_params of this CaseInfoDetail.

        for_loop_params

        :return: The for_loop_params of this CaseInfoDetail.
        :rtype: list[object]
        """
        return self._for_loop_params

    @for_loop_params.setter
    def for_loop_params(self, for_loop_params):
        """Sets the for_loop_params of this CaseInfoDetail.

        for_loop_params

        :param for_loop_params: The for_loop_params of this CaseInfoDetail.
        :type for_loop_params: list[object]
        """
        self._for_loop_params = for_loop_params

    @property
    def increase_setting(self):
        """Gets the increase_setting of this CaseInfoDetail.

        increase_setting

        :return: The increase_setting of this CaseInfoDetail.
        :rtype: list[object]
        """
        return self._increase_setting

    @increase_setting.setter
    def increase_setting(self, increase_setting):
        """Sets the increase_setting of this CaseInfoDetail.

        increase_setting

        :param increase_setting: The increase_setting of this CaseInfoDetail.
        :type increase_setting: list[object]
        """
        self._increase_setting = increase_setting

    @property
    def stages(self):
        """Gets the stages of this CaseInfoDetail.

        stages

        :return: The stages of this CaseInfoDetail.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.TestCaseStage`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this CaseInfoDetail.

        stages

        :param stages: The stages of this CaseInfoDetail.
        :type stages: list[:class:`huaweicloudsdkcpts.v1.TestCaseStage`]
        """
        self._stages = stages

    @property
    def status(self):
        """Gets the status of this CaseInfoDetail.

        状态，0：已删除；1：启用；2：禁用

        :return: The status of this CaseInfoDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CaseInfoDetail.

        状态，0：已删除；1：启用；2：禁用

        :param status: The status of this CaseInfoDetail.
        :type status: int
        """
        self._status = status

    @property
    def temp_id(self):
        """Gets the temp_id of this CaseInfoDetail.

        temp_id

        :return: The temp_id of this CaseInfoDetail.
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        """Sets the temp_id of this CaseInfoDetail.

        temp_id

        :param temp_id: The temp_id of this CaseInfoDetail.
        :type temp_id: int
        """
        self._temp_id = temp_id

    @property
    def sort(self):
        """Gets the sort of this CaseInfoDetail.

        排序字段

        :return: The sort of this CaseInfoDetail.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this CaseInfoDetail.

        排序字段

        :param sort: The sort of this CaseInfoDetail.
        :type sort: int
        """
        self._sort = sort

    @property
    def directory_id(self):
        """Gets the directory_id of this CaseInfoDetail.

        用例所属目录id（旧版接口可不传）

        :return: The directory_id of this CaseInfoDetail.
        :rtype: int
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this CaseInfoDetail.

        用例所属目录id（旧版接口可不传）

        :param directory_id: The directory_id of this CaseInfoDetail.
        :type directory_id: int
        """
        self._directory_id = directory_id

    @property
    def setup_contents(self):
        """Gets the setup_contents of this CaseInfoDetail.

        前置步骤

        :return: The setup_contents of this CaseInfoDetail.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.Contents`]
        """
        return self._setup_contents

    @setup_contents.setter
    def setup_contents(self, setup_contents):
        """Sets the setup_contents of this CaseInfoDetail.

        前置步骤

        :param setup_contents: The setup_contents of this CaseInfoDetail.
        :type setup_contents: list[:class:`huaweicloudsdkcpts.v1.Contents`]
        """
        self._setup_contents = setup_contents

    @property
    def user_replicas(self):
        """Gets the user_replicas of this CaseInfoDetail.

        执行器个数

        :return: The user_replicas of this CaseInfoDetail.
        :rtype: int
        """
        return self._user_replicas

    @user_replicas.setter
    def user_replicas(self, user_replicas):
        """Sets the user_replicas of this CaseInfoDetail.

        执行器个数

        :param user_replicas: The user_replicas of this CaseInfoDetail.
        :type user_replicas: int
        """
        self._user_replicas = user_replicas

    @property
    def collect_log_policy(self):
        """Gets the collect_log_policy of this CaseInfoDetail.

        日志采集策略（0-请求模式；1-用例模式）

        :return: The collect_log_policy of this CaseInfoDetail.
        :rtype: int
        """
        return self._collect_log_policy

    @collect_log_policy.setter
    def collect_log_policy(self, collect_log_policy):
        """Sets the collect_log_policy of this CaseInfoDetail.

        日志采集策略（0-请求模式；1-用例模式）

        :param collect_log_policy: The collect_log_policy of this CaseInfoDetail.
        :type collect_log_policy: int
        """
        self._collect_log_policy = collect_log_policy

    @property
    def link_app_list(self):
        """Gets the link_app_list of this CaseInfoDetail.

        关联全链路应用列表

        :return: The link_app_list of this CaseInfoDetail.
        :rtype: list[int]
        """
        return self._link_app_list

    @link_app_list.setter
    def link_app_list(self, link_app_list):
        """Sets the link_app_list of this CaseInfoDetail.

        关联全链路应用列表

        :param link_app_list: The link_app_list of this CaseInfoDetail.
        :type link_app_list: list[int]
        """
        self._link_app_list = link_app_list

    @property
    def case_info(self):
        """Gets the case_info of this CaseInfoDetail.

        :return: The case_info of this CaseInfoDetail.
        :rtype: :class:`huaweicloudsdkcpts.v1.CaseDoc`
        """
        return self._case_info

    @case_info.setter
    def case_info(self, case_info):
        """Sets the case_info of this CaseInfoDetail.

        :param case_info: The case_info of this CaseInfoDetail.
        :type case_info: :class:`huaweicloudsdkcpts.v1.CaseDoc`
        """
        self._case_info = case_info

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
        if not isinstance(other, CaseInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
