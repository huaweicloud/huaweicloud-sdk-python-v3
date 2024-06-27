# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVersionTestCaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'type': 'str',
        'author': 'str',
        'name': 'str',
        'rank': 'int',
        'preparation': 'str',
        'remark': 'str',
        'stage': 'str',
        'activity': 'str',
        'keywords': 'str',
        'market': 'str',
        'designer': 'str',
        'tags': 'str',
        'execute_parameter': 'str',
        'region': 'str',
        'owner': 'str',
        'last_modifier': 'str',
        'last_modified': 'datetime',
        'last_modified_timestamp': 'int',
        'last_change_time': 'datetime',
        'version_uri': 'str',
        'origin_uri': 'str',
        'parent_uri': 'str',
        'parent_path': 'str',
        'creation_version_uri': 'str',
        'creation_date': 'datetime',
        'creation_date_timestamp': 'int',
        'author_name': 'str',
        'comment': 'str',
        'number': 'str',
        'case_type': 'int',
        'platform_type': 'int',
        'service_type': 'int',
        'service_type_name': 'str',
        'test_type': 'int',
        'test_type_name': 'str',
        'design_note': 'str',
        'test_step': 'str',
        'expect_output': 'str',
        'env_type': 'str',
        'exe_platform': 'str',
        'testcase_project': 'str',
        'svn_script_path': 'str',
        'map_restrict': 'str',
        'network_script_name': 'str',
        'auto_type': 'int',
        'to_be_auto_exec': 'int',
        'last_result': 'str',
        'last_result_uri': 'str',
        'feature_uri': 'str',
        'feature_name': 'str',
        'interface_name': 'str',
        'snp_no': 'str',
        'dr_relation_id': 'str',
        'issue_name': 'str',
        'test_base_num': 'str',
        'automatically_executed': 'int',
        'first_execute_time': 'datetime',
        'detect_type': 'str',
        'execute_param': 'str',
        'test_feature': 'str',
        'is_contract_testcase': 'int',
        'time_cost': 'float',
        'be_auto_type_time': 'datetime',
        'compare_number': 'str',
        'scene_flag': 'str',
        'base_flag': 'str',
        'para_validator': 'str',
        'knet_node_id': 'str',
        'last_exe_author': 'str',
        'cloud_carrier': 'str',
        'market_place': 'str',
        'test_mind_id': 'str',
        'test_mind_url': 'str',
        'commit_url': 'str',
        'test_pattern_number': 'str',
        'test_factor_number': 'str',
        'status_code': 'str',
        'result_code': 'str',
        'release_id': 'str',
        'label_id': 'str',
        'labels': 'str',
        'module_id': 'str',
        'module_name': 'str',
        'module_path': 'str',
        'module_path_name': 'str',
        'execute_latest_time': 'datetime',
        'execute_duration': 'str',
        'execute_times': 'int',
        'is_keyword': 'int',
        'release_dev': 'str',
        'new_created': 'str',
        'project_uuid': 'str',
        'creation_version_name': 'str',
        'feature_path': 'str',
        'testcase_uri': 'str',
        'owner_name': 'str',
        'iterator_case_uri': 'str',
        'script_link': 'str',
        'custom_field_1': 'str',
        'custom_field_2': 'str',
        'custom_field_3': 'str',
        'custom_field_4': 'str',
        'custom_field_5': 'str',
        'custom_field_6': 'str',
        'custom_field_7': 'str',
        'custom_field_8': 'str',
        'custom_field_9': 'str',
        'custom_field_10': 'str',
        'custom_field_11': 'str',
        'custom_field_12': 'str',
        'custom_field_13': 'str',
        'custom_field_14': 'str',
        'custom_field_15': 'str',
        'custom_field_16': 'str',
        'custom_field_17': 'str',
        'custom_field_18': 'str',
        'custom_field_19': 'str',
        'custom_field_20': 'str',
        'custom_field_21': 'str',
        'custom_field_22': 'str',
        'custom_field_23': 'str',
        'custom_field_24': 'str',
        'custom_field_25': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'type': 'type',
        'author': 'author',
        'name': 'name',
        'rank': 'rank',
        'preparation': 'preparation',
        'remark': 'remark',
        'stage': 'stage',
        'activity': 'activity',
        'keywords': 'keywords',
        'market': 'market',
        'designer': 'designer',
        'tags': 'tags',
        'execute_parameter': 'execute_parameter',
        'region': 'region',
        'owner': 'owner',
        'last_modifier': 'last_modifier',
        'last_modified': 'last_modified',
        'last_modified_timestamp': 'last_modified_timestamp',
        'last_change_time': 'last_change_time',
        'version_uri': 'version_uri',
        'origin_uri': 'origin_uri',
        'parent_uri': 'parent_uri',
        'parent_path': 'parent_path',
        'creation_version_uri': 'creation_version_uri',
        'creation_date': 'creation_date',
        'creation_date_timestamp': 'creation_date_timestamp',
        'author_name': 'author_name',
        'comment': 'comment',
        'number': 'number',
        'case_type': 'case_type',
        'platform_type': 'platform_type',
        'service_type': 'service_type',
        'service_type_name': 'service_type_name',
        'test_type': 'test_type',
        'test_type_name': 'test_type_name',
        'design_note': 'design_note',
        'test_step': 'test_step',
        'expect_output': 'expect_output',
        'env_type': 'env_type',
        'exe_platform': 'exe_platform',
        'testcase_project': 'testcase_project',
        'svn_script_path': 'svn_script_path',
        'map_restrict': 'map_restrict',
        'network_script_name': 'network_script_name',
        'auto_type': 'auto_type',
        'to_be_auto_exec': 'to_be_auto_exec',
        'last_result': 'last_result',
        'last_result_uri': 'last_result_uri',
        'feature_uri': 'feature_uri',
        'feature_name': 'feature_name',
        'interface_name': 'interface_name',
        'snp_no': 'snp_no',
        'dr_relation_id': 'dr_relation_id',
        'issue_name': 'issue_name',
        'test_base_num': 'test_base_num',
        'automatically_executed': 'automatically_executed',
        'first_execute_time': 'first_execute_time',
        'detect_type': 'detect_type',
        'execute_param': 'execute_param',
        'test_feature': 'test_feature',
        'is_contract_testcase': 'is_contract_testcase',
        'time_cost': 'time_cost',
        'be_auto_type_time': 'be_auto_type_time',
        'compare_number': 'compare_number',
        'scene_flag': 'scene_flag',
        'base_flag': 'base_flag',
        'para_validator': 'para_validator',
        'knet_node_id': 'knet_node_id',
        'last_exe_author': 'last_exe_author',
        'cloud_carrier': 'cloud_carrier',
        'market_place': 'market_place',
        'test_mind_id': 'test_mind_id',
        'test_mind_url': 'test_mind_url',
        'commit_url': 'commit_url',
        'test_pattern_number': 'test_pattern_number',
        'test_factor_number': 'test_factor_number',
        'status_code': 'status_code',
        'result_code': 'result_code',
        'release_id': 'release_id',
        'label_id': 'label_id',
        'labels': 'labels',
        'module_id': 'module_id',
        'module_name': 'module_name',
        'module_path': 'module_path',
        'module_path_name': 'module_path_name',
        'execute_latest_time': 'execute_latest_time',
        'execute_duration': 'execute_duration',
        'execute_times': 'execute_times',
        'is_keyword': 'is_keyword',
        'release_dev': 'release_dev',
        'new_created': 'new_created',
        'project_uuid': 'project_uuid',
        'creation_version_name': 'creation_version_name',
        'feature_path': 'feature_path',
        'testcase_uri': 'testcase_uri',
        'owner_name': 'owner_name',
        'iterator_case_uri': 'iterator_case_uri',
        'script_link': 'script_link',
        'custom_field_1': 'custom_field_1',
        'custom_field_2': 'custom_field_2',
        'custom_field_3': 'custom_field_3',
        'custom_field_4': 'custom_field_4',
        'custom_field_5': 'custom_field_5',
        'custom_field_6': 'custom_field_6',
        'custom_field_7': 'custom_field_7',
        'custom_field_8': 'custom_field_8',
        'custom_field_9': 'custom_field_9',
        'custom_field_10': 'custom_field_10',
        'custom_field_11': 'custom_field_11',
        'custom_field_12': 'custom_field_12',
        'custom_field_13': 'custom_field_13',
        'custom_field_14': 'custom_field_14',
        'custom_field_15': 'custom_field_15',
        'custom_field_16': 'custom_field_16',
        'custom_field_17': 'custom_field_17',
        'custom_field_18': 'custom_field_18',
        'custom_field_19': 'custom_field_19',
        'custom_field_20': 'custom_field_20',
        'custom_field_21': 'custom_field_21',
        'custom_field_22': 'custom_field_22',
        'custom_field_23': 'custom_field_23',
        'custom_field_24': 'custom_field_24',
        'custom_field_25': 'custom_field_25'
    }

    def __init__(self, uri=None, type=None, author=None, name=None, rank=None, preparation=None, remark=None, stage=None, activity=None, keywords=None, market=None, designer=None, tags=None, execute_parameter=None, region=None, owner=None, last_modifier=None, last_modified=None, last_modified_timestamp=None, last_change_time=None, version_uri=None, origin_uri=None, parent_uri=None, parent_path=None, creation_version_uri=None, creation_date=None, creation_date_timestamp=None, author_name=None, comment=None, number=None, case_type=None, platform_type=None, service_type=None, service_type_name=None, test_type=None, test_type_name=None, design_note=None, test_step=None, expect_output=None, env_type=None, exe_platform=None, testcase_project=None, svn_script_path=None, map_restrict=None, network_script_name=None, auto_type=None, to_be_auto_exec=None, last_result=None, last_result_uri=None, feature_uri=None, feature_name=None, interface_name=None, snp_no=None, dr_relation_id=None, issue_name=None, test_base_num=None, automatically_executed=None, first_execute_time=None, detect_type=None, execute_param=None, test_feature=None, is_contract_testcase=None, time_cost=None, be_auto_type_time=None, compare_number=None, scene_flag=None, base_flag=None, para_validator=None, knet_node_id=None, last_exe_author=None, cloud_carrier=None, market_place=None, test_mind_id=None, test_mind_url=None, commit_url=None, test_pattern_number=None, test_factor_number=None, status_code=None, result_code=None, release_id=None, label_id=None, labels=None, module_id=None, module_name=None, module_path=None, module_path_name=None, execute_latest_time=None, execute_duration=None, execute_times=None, is_keyword=None, release_dev=None, new_created=None, project_uuid=None, creation_version_name=None, feature_path=None, testcase_uri=None, owner_name=None, iterator_case_uri=None, script_link=None, custom_field_1=None, custom_field_2=None, custom_field_3=None, custom_field_4=None, custom_field_5=None, custom_field_6=None, custom_field_7=None, custom_field_8=None, custom_field_9=None, custom_field_10=None, custom_field_11=None, custom_field_12=None, custom_field_13=None, custom_field_14=None, custom_field_15=None, custom_field_16=None, custom_field_17=None, custom_field_18=None, custom_field_19=None, custom_field_20=None, custom_field_21=None, custom_field_22=None, custom_field_23=None, custom_field_24=None, custom_field_25=None):
        """CreateVersionTestCaseResponse

        The model defined in huaweicloud sdk

        :param uri: 资源URI
        :type uri: str
        :param type: 资源类型
        :type type: str
        :param author: 创建人
        :type author: str
        :param name: 名称
        :type name: str
        :param rank: 级别
        :type rank: int
        :param preparation: 前置条件
        :type preparation: str
        :param remark: 备注
        :type remark: str
        :param stage: 测试阶段
        :type stage: str
        :param activity: 测试类型
        :type activity: str
        :param keywords: 关键词
        :type keywords: str
        :param market: apitest标记是否代码已提交
        :type market: str
        :param designer: 设计者
        :type designer: str
        :param tags: 标签
        :type tags: str
        :param execute_parameter: 执行参数
        :type execute_parameter: str
        :param region: 逻辑region
        :type region: str
        :param owner: 处理人id，IteratorTestCase字段
        :type owner: str
        :param last_modifier: 最后修改人
        :type last_modifier: str
        :param last_modified: 最后修改时间
        :type last_modified: datetime
        :param last_modified_timestamp: 修改时间时间戳
        :type last_modified_timestamp: int
        :param last_change_time: 最后变更时间
        :type last_change_time: datetime
        :param version_uri: 版本URI
        :type version_uri: str
        :param origin_uri: 源资源URI
        :type origin_uri: str
        :param parent_uri: 父资源URI
        :type parent_uri: str
        :param parent_path: 父资源路径
        :type parent_path: str
        :param creation_version_uri: 创建版本URI
        :type creation_version_uri: str
        :param creation_date: 创建时间
        :type creation_date: datetime
        :param creation_date_timestamp: 创建时间时间戳
        :type creation_date_timestamp: int
        :param author_name: 创建人名称
        :type author_name: str
        :param comment: 备注
        :type comment: str
        :param number: 编号
        :type number: str
        :param case_type: 用例类型
        :type case_type: int
        :param platform_type: 执行平台类型
        :type platform_type: int
        :param service_type: 服务类型
        :type service_type: int
        :param service_type_name: 服务类型名称
        :type service_type_name: str
        :param test_type: 测试类型
        :type test_type: int
        :param test_type_name: 测试类型名称
        :type test_type_name: str
        :param design_note: 设计描述
        :type design_note: str
        :param test_step: 测试步骤
        :type test_step: str
        :param expect_output: 期望结果
        :type expect_output: str
        :param env_type: 测试环境类型
        :type env_type: str
        :param exe_platform: 执行平台
        :type exe_platform: str
        :param testcase_project: 测试工程
        :type testcase_project: str
        :param svn_script_path: 脚本路径
        :type svn_script_path: str
        :param map_restrict: 约束条件
        :type map_restrict: str
        :param network_script_name: 网络脚本名
        :type network_script_name: str
        :param auto_type: 自动化类型，非自动化:0, 是自动化:1
        :type auto_type: int
        :param to_be_auto_exec: 被自动化执行
        :type to_be_auto_exec: int
        :param last_result: 最后一次结果
        :type last_result: str
        :param last_result_uri: 最后一次结果Uri
        :type last_result_uri: str
        :param feature_uri: 目录Uri
        :type feature_uri: str
        :param feature_name: 目录名称
        :type feature_name: str
        :param interface_name: 测试接口名
        :type interface_name: str
        :param snp_no: 网络问题ID
        :type snp_no: str
        :param dr_relation_id: 关联需求编号
        :type dr_relation_id: str
        :param issue_name: 需求名称
        :type issue_name: str
        :param test_base_num: 测试基数
        :type test_base_num: str
        :param automatically_executed: 是否被自动化执行
        :type automatically_executed: int
        :param first_execute_time: 第一次执行时间
        :type first_execute_time: datetime
        :param detect_type: 检测类型
        :type detect_type: str
        :param execute_param: 执行参数
        :type execute_param: str
        :param test_feature: 分析领域
        :type test_feature: str
        :param is_contract_testcase: 是否是契约用例，0:表示非契约用例, 1：表示契约用例
        :type is_contract_testcase: int
        :param time_cost: 总共耗时
        :type time_cost: float
        :param be_auto_type_time: 记录用例由非自动化变为自动化类型的时间
        :type be_auto_type_time: datetime
        :param compare_number: 配对用例编号
        :type compare_number: str
        :param scene_flag: 场景标识
        :type scene_flag: str
        :param base_flag: 场景标识
        :type base_flag: str
        :param para_validator: 区别是否从yaml中生成的用例，默认false
        :type para_validator: str
        :param knet_node_id: knet节点id
        :type knet_node_id: str
        :param last_exe_author: 最后一次执行用户
        :type last_exe_author: str
        :param cloud_carrier: 运营商
        :type cloud_carrier: str
        :param market_place: 应用市场
        :type market_place: str
        :param test_mind_id: 脑图id
        :type test_mind_id: str
        :param test_mind_url: 脑图url
        :type test_mind_url: str
        :param commit_url: git提交url
        :type commit_url: str
        :param test_pattern_number: 测试模式编号
        :type test_pattern_number: str
        :param test_factor_number: 测试因子编号
        :type test_factor_number: str
        :param status_code: 状态Code
        :type status_code: str
        :param result_code: 结果Code
        :type result_code: str
        :param release_id: 迭代ID
        :type release_id: str
        :param label_id: 标签ID
        :type label_id: str
        :param labels: 用例标签名称列表
        :type labels: str
        :param module_id: 模块ID
        :type module_id: str
        :param module_name: 模块名称
        :type module_name: str
        :param module_path: 模块path
        :type module_path: str
        :param module_path_name: 模块路径名称
        :type module_path_name: str
        :param execute_latest_time: 最后执行时间
        :type execute_latest_time: datetime
        :param execute_duration: 执行时长
        :type execute_duration: str
        :param execute_times: 执行次数
        :type execute_times: int
        :param is_keyword: 是否关键用例
        :type is_keyword: int
        :param release_dev: 测试版本号
        :type release_dev: str
        :param new_created: 是否用户新增用例
        :type new_created: str
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param creation_version_name: 创建版本名称，原逻辑marshall添加字段
        :type creation_version_name: str
        :param feature_path: 特性路径，原逻辑marshall添加字段
        :type feature_path: str
        :param testcase_uri: 实体用例Uri，IteratorTestCase字段
        :type testcase_uri: str
        :param owner_name: 处理人名称
        :type owner_name: str
        :param iterator_case_uri: 迭代用例Uri，IteratorTestCase字段
        :type iterator_case_uri: str
        :param script_link: 脚本链接scriptLink
        :type script_link: str
        :param custom_field_1: 自定义字段1
        :type custom_field_1: str
        :param custom_field_2: 自定义字段2
        :type custom_field_2: str
        :param custom_field_3: 自定义字段3
        :type custom_field_3: str
        :param custom_field_4: 自定义字段4
        :type custom_field_4: str
        :param custom_field_5: 自定义字段5
        :type custom_field_5: str
        :param custom_field_6: 自定义字段6
        :type custom_field_6: str
        :param custom_field_7: 自定义字段7
        :type custom_field_7: str
        :param custom_field_8: 自定义字段8
        :type custom_field_8: str
        :param custom_field_9: 自定义字段9
        :type custom_field_9: str
        :param custom_field_10: 自定义字段10
        :type custom_field_10: str
        :param custom_field_11: 自定义字段11
        :type custom_field_11: str
        :param custom_field_12: 自定义字段12
        :type custom_field_12: str
        :param custom_field_13: 自定义字段13
        :type custom_field_13: str
        :param custom_field_14: 自定义字段14
        :type custom_field_14: str
        :param custom_field_15: 自定义字段15
        :type custom_field_15: str
        :param custom_field_16: 自定义字段16
        :type custom_field_16: str
        :param custom_field_17: 自定义字段17
        :type custom_field_17: str
        :param custom_field_18: 自定义字段18
        :type custom_field_18: str
        :param custom_field_19: 自定义字段19
        :type custom_field_19: str
        :param custom_field_20: 自定义字段20
        :type custom_field_20: str
        :param custom_field_21: 自定义字段21
        :type custom_field_21: str
        :param custom_field_22: 自定义字段22
        :type custom_field_22: str
        :param custom_field_23: 自定义字段23
        :type custom_field_23: str
        :param custom_field_24: 自定义字段24
        :type custom_field_24: str
        :param custom_field_25: 自定义字段25
        :type custom_field_25: str
        """
        
        super(CreateVersionTestCaseResponse, self).__init__()

        self._uri = None
        self._type = None
        self._author = None
        self._name = None
        self._rank = None
        self._preparation = None
        self._remark = None
        self._stage = None
        self._activity = None
        self._keywords = None
        self._market = None
        self._designer = None
        self._tags = None
        self._execute_parameter = None
        self._region = None
        self._owner = None
        self._last_modifier = None
        self._last_modified = None
        self._last_modified_timestamp = None
        self._last_change_time = None
        self._version_uri = None
        self._origin_uri = None
        self._parent_uri = None
        self._parent_path = None
        self._creation_version_uri = None
        self._creation_date = None
        self._creation_date_timestamp = None
        self._author_name = None
        self._comment = None
        self._number = None
        self._case_type = None
        self._platform_type = None
        self._service_type = None
        self._service_type_name = None
        self._test_type = None
        self._test_type_name = None
        self._design_note = None
        self._test_step = None
        self._expect_output = None
        self._env_type = None
        self._exe_platform = None
        self._testcase_project = None
        self._svn_script_path = None
        self._map_restrict = None
        self._network_script_name = None
        self._auto_type = None
        self._to_be_auto_exec = None
        self._last_result = None
        self._last_result_uri = None
        self._feature_uri = None
        self._feature_name = None
        self._interface_name = None
        self._snp_no = None
        self._dr_relation_id = None
        self._issue_name = None
        self._test_base_num = None
        self._automatically_executed = None
        self._first_execute_time = None
        self._detect_type = None
        self._execute_param = None
        self._test_feature = None
        self._is_contract_testcase = None
        self._time_cost = None
        self._be_auto_type_time = None
        self._compare_number = None
        self._scene_flag = None
        self._base_flag = None
        self._para_validator = None
        self._knet_node_id = None
        self._last_exe_author = None
        self._cloud_carrier = None
        self._market_place = None
        self._test_mind_id = None
        self._test_mind_url = None
        self._commit_url = None
        self._test_pattern_number = None
        self._test_factor_number = None
        self._status_code = None
        self._result_code = None
        self._release_id = None
        self._label_id = None
        self._labels = None
        self._module_id = None
        self._module_name = None
        self._module_path = None
        self._module_path_name = None
        self._execute_latest_time = None
        self._execute_duration = None
        self._execute_times = None
        self._is_keyword = None
        self._release_dev = None
        self._new_created = None
        self._project_uuid = None
        self._creation_version_name = None
        self._feature_path = None
        self._testcase_uri = None
        self._owner_name = None
        self._iterator_case_uri = None
        self._script_link = None
        self._custom_field_1 = None
        self._custom_field_2 = None
        self._custom_field_3 = None
        self._custom_field_4 = None
        self._custom_field_5 = None
        self._custom_field_6 = None
        self._custom_field_7 = None
        self._custom_field_8 = None
        self._custom_field_9 = None
        self._custom_field_10 = None
        self._custom_field_11 = None
        self._custom_field_12 = None
        self._custom_field_13 = None
        self._custom_field_14 = None
        self._custom_field_15 = None
        self._custom_field_16 = None
        self._custom_field_17 = None
        self._custom_field_18 = None
        self._custom_field_19 = None
        self._custom_field_20 = None
        self._custom_field_21 = None
        self._custom_field_22 = None
        self._custom_field_23 = None
        self._custom_field_24 = None
        self._custom_field_25 = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if type is not None:
            self.type = type
        if author is not None:
            self.author = author
        if name is not None:
            self.name = name
        if rank is not None:
            self.rank = rank
        if preparation is not None:
            self.preparation = preparation
        if remark is not None:
            self.remark = remark
        if stage is not None:
            self.stage = stage
        if activity is not None:
            self.activity = activity
        if keywords is not None:
            self.keywords = keywords
        if market is not None:
            self.market = market
        if designer is not None:
            self.designer = designer
        if tags is not None:
            self.tags = tags
        if execute_parameter is not None:
            self.execute_parameter = execute_parameter
        if region is not None:
            self.region = region
        if owner is not None:
            self.owner = owner
        if last_modifier is not None:
            self.last_modifier = last_modifier
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modified_timestamp is not None:
            self.last_modified_timestamp = last_modified_timestamp
        if last_change_time is not None:
            self.last_change_time = last_change_time
        if version_uri is not None:
            self.version_uri = version_uri
        if origin_uri is not None:
            self.origin_uri = origin_uri
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if parent_path is not None:
            self.parent_path = parent_path
        if creation_version_uri is not None:
            self.creation_version_uri = creation_version_uri
        if creation_date is not None:
            self.creation_date = creation_date
        if creation_date_timestamp is not None:
            self.creation_date_timestamp = creation_date_timestamp
        if author_name is not None:
            self.author_name = author_name
        if comment is not None:
            self.comment = comment
        if number is not None:
            self.number = number
        if case_type is not None:
            self.case_type = case_type
        if platform_type is not None:
            self.platform_type = platform_type
        if service_type is not None:
            self.service_type = service_type
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if test_type is not None:
            self.test_type = test_type
        if test_type_name is not None:
            self.test_type_name = test_type_name
        if design_note is not None:
            self.design_note = design_note
        if test_step is not None:
            self.test_step = test_step
        if expect_output is not None:
            self.expect_output = expect_output
        if env_type is not None:
            self.env_type = env_type
        if exe_platform is not None:
            self.exe_platform = exe_platform
        if testcase_project is not None:
            self.testcase_project = testcase_project
        if svn_script_path is not None:
            self.svn_script_path = svn_script_path
        if map_restrict is not None:
            self.map_restrict = map_restrict
        if network_script_name is not None:
            self.network_script_name = network_script_name
        if auto_type is not None:
            self.auto_type = auto_type
        if to_be_auto_exec is not None:
            self.to_be_auto_exec = to_be_auto_exec
        if last_result is not None:
            self.last_result = last_result
        if last_result_uri is not None:
            self.last_result_uri = last_result_uri
        if feature_uri is not None:
            self.feature_uri = feature_uri
        if feature_name is not None:
            self.feature_name = feature_name
        if interface_name is not None:
            self.interface_name = interface_name
        if snp_no is not None:
            self.snp_no = snp_no
        if dr_relation_id is not None:
            self.dr_relation_id = dr_relation_id
        if issue_name is not None:
            self.issue_name = issue_name
        if test_base_num is not None:
            self.test_base_num = test_base_num
        if automatically_executed is not None:
            self.automatically_executed = automatically_executed
        if first_execute_time is not None:
            self.first_execute_time = first_execute_time
        if detect_type is not None:
            self.detect_type = detect_type
        if execute_param is not None:
            self.execute_param = execute_param
        if test_feature is not None:
            self.test_feature = test_feature
        if is_contract_testcase is not None:
            self.is_contract_testcase = is_contract_testcase
        if time_cost is not None:
            self.time_cost = time_cost
        if be_auto_type_time is not None:
            self.be_auto_type_time = be_auto_type_time
        if compare_number is not None:
            self.compare_number = compare_number
        if scene_flag is not None:
            self.scene_flag = scene_flag
        if base_flag is not None:
            self.base_flag = base_flag
        if para_validator is not None:
            self.para_validator = para_validator
        if knet_node_id is not None:
            self.knet_node_id = knet_node_id
        if last_exe_author is not None:
            self.last_exe_author = last_exe_author
        if cloud_carrier is not None:
            self.cloud_carrier = cloud_carrier
        if market_place is not None:
            self.market_place = market_place
        if test_mind_id is not None:
            self.test_mind_id = test_mind_id
        if test_mind_url is not None:
            self.test_mind_url = test_mind_url
        if commit_url is not None:
            self.commit_url = commit_url
        if test_pattern_number is not None:
            self.test_pattern_number = test_pattern_number
        if test_factor_number is not None:
            self.test_factor_number = test_factor_number
        if status_code is not None:
            self.status_code = status_code
        if result_code is not None:
            self.result_code = result_code
        if release_id is not None:
            self.release_id = release_id
        if label_id is not None:
            self.label_id = label_id
        if labels is not None:
            self.labels = labels
        if module_id is not None:
            self.module_id = module_id
        if module_name is not None:
            self.module_name = module_name
        if module_path is not None:
            self.module_path = module_path
        if module_path_name is not None:
            self.module_path_name = module_path_name
        if execute_latest_time is not None:
            self.execute_latest_time = execute_latest_time
        if execute_duration is not None:
            self.execute_duration = execute_duration
        if execute_times is not None:
            self.execute_times = execute_times
        if is_keyword is not None:
            self.is_keyword = is_keyword
        if release_dev is not None:
            self.release_dev = release_dev
        if new_created is not None:
            self.new_created = new_created
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if creation_version_name is not None:
            self.creation_version_name = creation_version_name
        if feature_path is not None:
            self.feature_path = feature_path
        if testcase_uri is not None:
            self.testcase_uri = testcase_uri
        if owner_name is not None:
            self.owner_name = owner_name
        if iterator_case_uri is not None:
            self.iterator_case_uri = iterator_case_uri
        if script_link is not None:
            self.script_link = script_link
        if custom_field_1 is not None:
            self.custom_field_1 = custom_field_1
        if custom_field_2 is not None:
            self.custom_field_2 = custom_field_2
        if custom_field_3 is not None:
            self.custom_field_3 = custom_field_3
        if custom_field_4 is not None:
            self.custom_field_4 = custom_field_4
        if custom_field_5 is not None:
            self.custom_field_5 = custom_field_5
        if custom_field_6 is not None:
            self.custom_field_6 = custom_field_6
        if custom_field_7 is not None:
            self.custom_field_7 = custom_field_7
        if custom_field_8 is not None:
            self.custom_field_8 = custom_field_8
        if custom_field_9 is not None:
            self.custom_field_9 = custom_field_9
        if custom_field_10 is not None:
            self.custom_field_10 = custom_field_10
        if custom_field_11 is not None:
            self.custom_field_11 = custom_field_11
        if custom_field_12 is not None:
            self.custom_field_12 = custom_field_12
        if custom_field_13 is not None:
            self.custom_field_13 = custom_field_13
        if custom_field_14 is not None:
            self.custom_field_14 = custom_field_14
        if custom_field_15 is not None:
            self.custom_field_15 = custom_field_15
        if custom_field_16 is not None:
            self.custom_field_16 = custom_field_16
        if custom_field_17 is not None:
            self.custom_field_17 = custom_field_17
        if custom_field_18 is not None:
            self.custom_field_18 = custom_field_18
        if custom_field_19 is not None:
            self.custom_field_19 = custom_field_19
        if custom_field_20 is not None:
            self.custom_field_20 = custom_field_20
        if custom_field_21 is not None:
            self.custom_field_21 = custom_field_21
        if custom_field_22 is not None:
            self.custom_field_22 = custom_field_22
        if custom_field_23 is not None:
            self.custom_field_23 = custom_field_23
        if custom_field_24 is not None:
            self.custom_field_24 = custom_field_24
        if custom_field_25 is not None:
            self.custom_field_25 = custom_field_25

    @property
    def uri(self):
        """Gets the uri of this CreateVersionTestCaseResponse.

        资源URI

        :return: The uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CreateVersionTestCaseResponse.

        资源URI

        :param uri: The uri of this CreateVersionTestCaseResponse.
        :type uri: str
        """
        self._uri = uri

    @property
    def type(self):
        """Gets the type of this CreateVersionTestCaseResponse.

        资源类型

        :return: The type of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateVersionTestCaseResponse.

        资源类型

        :param type: The type of this CreateVersionTestCaseResponse.
        :type type: str
        """
        self._type = type

    @property
    def author(self):
        """Gets the author of this CreateVersionTestCaseResponse.

        创建人

        :return: The author of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CreateVersionTestCaseResponse.

        创建人

        :param author: The author of this CreateVersionTestCaseResponse.
        :type author: str
        """
        self._author = author

    @property
    def name(self):
        """Gets the name of this CreateVersionTestCaseResponse.

        名称

        :return: The name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVersionTestCaseResponse.

        名称

        :param name: The name of this CreateVersionTestCaseResponse.
        :type name: str
        """
        self._name = name

    @property
    def rank(self):
        """Gets the rank of this CreateVersionTestCaseResponse.

        级别

        :return: The rank of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this CreateVersionTestCaseResponse.

        级别

        :param rank: The rank of this CreateVersionTestCaseResponse.
        :type rank: int
        """
        self._rank = rank

    @property
    def preparation(self):
        """Gets the preparation of this CreateVersionTestCaseResponse.

        前置条件

        :return: The preparation of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        """Sets the preparation of this CreateVersionTestCaseResponse.

        前置条件

        :param preparation: The preparation of this CreateVersionTestCaseResponse.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def remark(self):
        """Gets the remark of this CreateVersionTestCaseResponse.

        备注

        :return: The remark of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateVersionTestCaseResponse.

        备注

        :param remark: The remark of this CreateVersionTestCaseResponse.
        :type remark: str
        """
        self._remark = remark

    @property
    def stage(self):
        """Gets the stage of this CreateVersionTestCaseResponse.

        测试阶段

        :return: The stage of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this CreateVersionTestCaseResponse.

        测试阶段

        :param stage: The stage of this CreateVersionTestCaseResponse.
        :type stage: str
        """
        self._stage = stage

    @property
    def activity(self):
        """Gets the activity of this CreateVersionTestCaseResponse.

        测试类型

        :return: The activity of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this CreateVersionTestCaseResponse.

        测试类型

        :param activity: The activity of this CreateVersionTestCaseResponse.
        :type activity: str
        """
        self._activity = activity

    @property
    def keywords(self):
        """Gets the keywords of this CreateVersionTestCaseResponse.

        关键词

        :return: The keywords of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this CreateVersionTestCaseResponse.

        关键词

        :param keywords: The keywords of this CreateVersionTestCaseResponse.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def market(self):
        """Gets the market of this CreateVersionTestCaseResponse.

        apitest标记是否代码已提交

        :return: The market of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this CreateVersionTestCaseResponse.

        apitest标记是否代码已提交

        :param market: The market of this CreateVersionTestCaseResponse.
        :type market: str
        """
        self._market = market

    @property
    def designer(self):
        """Gets the designer of this CreateVersionTestCaseResponse.

        设计者

        :return: The designer of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._designer

    @designer.setter
    def designer(self, designer):
        """Sets the designer of this CreateVersionTestCaseResponse.

        设计者

        :param designer: The designer of this CreateVersionTestCaseResponse.
        :type designer: str
        """
        self._designer = designer

    @property
    def tags(self):
        """Gets the tags of this CreateVersionTestCaseResponse.

        标签

        :return: The tags of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateVersionTestCaseResponse.

        标签

        :param tags: The tags of this CreateVersionTestCaseResponse.
        :type tags: str
        """
        self._tags = tags

    @property
    def execute_parameter(self):
        """Gets the execute_parameter of this CreateVersionTestCaseResponse.

        执行参数

        :return: The execute_parameter of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._execute_parameter

    @execute_parameter.setter
    def execute_parameter(self, execute_parameter):
        """Sets the execute_parameter of this CreateVersionTestCaseResponse.

        执行参数

        :param execute_parameter: The execute_parameter of this CreateVersionTestCaseResponse.
        :type execute_parameter: str
        """
        self._execute_parameter = execute_parameter

    @property
    def region(self):
        """Gets the region of this CreateVersionTestCaseResponse.

        逻辑region

        :return: The region of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateVersionTestCaseResponse.

        逻辑region

        :param region: The region of this CreateVersionTestCaseResponse.
        :type region: str
        """
        self._region = region

    @property
    def owner(self):
        """Gets the owner of this CreateVersionTestCaseResponse.

        处理人id，IteratorTestCase字段

        :return: The owner of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateVersionTestCaseResponse.

        处理人id，IteratorTestCase字段

        :param owner: The owner of this CreateVersionTestCaseResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def last_modifier(self):
        """Gets the last_modifier of this CreateVersionTestCaseResponse.

        最后修改人

        :return: The last_modifier of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        """Sets the last_modifier of this CreateVersionTestCaseResponse.

        最后修改人

        :param last_modifier: The last_modifier of this CreateVersionTestCaseResponse.
        :type last_modifier: str
        """
        self._last_modifier = last_modifier

    @property
    def last_modified(self):
        """Gets the last_modified of this CreateVersionTestCaseResponse.

        最后修改时间

        :return: The last_modified of this CreateVersionTestCaseResponse.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this CreateVersionTestCaseResponse.

        最后修改时间

        :param last_modified: The last_modified of this CreateVersionTestCaseResponse.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def last_modified_timestamp(self):
        """Gets the last_modified_timestamp of this CreateVersionTestCaseResponse.

        修改时间时间戳

        :return: The last_modified_timestamp of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        """Sets the last_modified_timestamp of this CreateVersionTestCaseResponse.

        修改时间时间戳

        :param last_modified_timestamp: The last_modified_timestamp of this CreateVersionTestCaseResponse.
        :type last_modified_timestamp: int
        """
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_change_time(self):
        """Gets the last_change_time of this CreateVersionTestCaseResponse.

        最后变更时间

        :return: The last_change_time of this CreateVersionTestCaseResponse.
        :rtype: datetime
        """
        return self._last_change_time

    @last_change_time.setter
    def last_change_time(self, last_change_time):
        """Sets the last_change_time of this CreateVersionTestCaseResponse.

        最后变更时间

        :param last_change_time: The last_change_time of this CreateVersionTestCaseResponse.
        :type last_change_time: datetime
        """
        self._last_change_time = last_change_time

    @property
    def version_uri(self):
        """Gets the version_uri of this CreateVersionTestCaseResponse.

        版本URI

        :return: The version_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this CreateVersionTestCaseResponse.

        版本URI

        :param version_uri: The version_uri of this CreateVersionTestCaseResponse.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def origin_uri(self):
        """Gets the origin_uri of this CreateVersionTestCaseResponse.

        源资源URI

        :return: The origin_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._origin_uri

    @origin_uri.setter
    def origin_uri(self, origin_uri):
        """Sets the origin_uri of this CreateVersionTestCaseResponse.

        源资源URI

        :param origin_uri: The origin_uri of this CreateVersionTestCaseResponse.
        :type origin_uri: str
        """
        self._origin_uri = origin_uri

    @property
    def parent_uri(self):
        """Gets the parent_uri of this CreateVersionTestCaseResponse.

        父资源URI

        :return: The parent_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        """Sets the parent_uri of this CreateVersionTestCaseResponse.

        父资源URI

        :param parent_uri: The parent_uri of this CreateVersionTestCaseResponse.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def parent_path(self):
        """Gets the parent_path of this CreateVersionTestCaseResponse.

        父资源路径

        :return: The parent_path of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        """Sets the parent_path of this CreateVersionTestCaseResponse.

        父资源路径

        :param parent_path: The parent_path of this CreateVersionTestCaseResponse.
        :type parent_path: str
        """
        self._parent_path = parent_path

    @property
    def creation_version_uri(self):
        """Gets the creation_version_uri of this CreateVersionTestCaseResponse.

        创建版本URI

        :return: The creation_version_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._creation_version_uri

    @creation_version_uri.setter
    def creation_version_uri(self, creation_version_uri):
        """Sets the creation_version_uri of this CreateVersionTestCaseResponse.

        创建版本URI

        :param creation_version_uri: The creation_version_uri of this CreateVersionTestCaseResponse.
        :type creation_version_uri: str
        """
        self._creation_version_uri = creation_version_uri

    @property
    def creation_date(self):
        """Gets the creation_date of this CreateVersionTestCaseResponse.

        创建时间

        :return: The creation_date of this CreateVersionTestCaseResponse.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this CreateVersionTestCaseResponse.

        创建时间

        :param creation_date: The creation_date of this CreateVersionTestCaseResponse.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def creation_date_timestamp(self):
        """Gets the creation_date_timestamp of this CreateVersionTestCaseResponse.

        创建时间时间戳

        :return: The creation_date_timestamp of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._creation_date_timestamp

    @creation_date_timestamp.setter
    def creation_date_timestamp(self, creation_date_timestamp):
        """Sets the creation_date_timestamp of this CreateVersionTestCaseResponse.

        创建时间时间戳

        :param creation_date_timestamp: The creation_date_timestamp of this CreateVersionTestCaseResponse.
        :type creation_date_timestamp: int
        """
        self._creation_date_timestamp = creation_date_timestamp

    @property
    def author_name(self):
        """Gets the author_name of this CreateVersionTestCaseResponse.

        创建人名称

        :return: The author_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this CreateVersionTestCaseResponse.

        创建人名称

        :param author_name: The author_name of this CreateVersionTestCaseResponse.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def comment(self):
        """Gets the comment of this CreateVersionTestCaseResponse.

        备注

        :return: The comment of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateVersionTestCaseResponse.

        备注

        :param comment: The comment of this CreateVersionTestCaseResponse.
        :type comment: str
        """
        self._comment = comment

    @property
    def number(self):
        """Gets the number of this CreateVersionTestCaseResponse.

        编号

        :return: The number of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreateVersionTestCaseResponse.

        编号

        :param number: The number of this CreateVersionTestCaseResponse.
        :type number: str
        """
        self._number = number

    @property
    def case_type(self):
        """Gets the case_type of this CreateVersionTestCaseResponse.

        用例类型

        :return: The case_type of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        """Sets the case_type of this CreateVersionTestCaseResponse.

        用例类型

        :param case_type: The case_type of this CreateVersionTestCaseResponse.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def platform_type(self):
        """Gets the platform_type of this CreateVersionTestCaseResponse.

        执行平台类型

        :return: The platform_type of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this CreateVersionTestCaseResponse.

        执行平台类型

        :param platform_type: The platform_type of this CreateVersionTestCaseResponse.
        :type platform_type: int
        """
        self._platform_type = platform_type

    @property
    def service_type(self):
        """Gets the service_type of this CreateVersionTestCaseResponse.

        服务类型

        :return: The service_type of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this CreateVersionTestCaseResponse.

        服务类型

        :param service_type: The service_type of this CreateVersionTestCaseResponse.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def service_type_name(self):
        """Gets the service_type_name of this CreateVersionTestCaseResponse.

        服务类型名称

        :return: The service_type_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this CreateVersionTestCaseResponse.

        服务类型名称

        :param service_type_name: The service_type_name of this CreateVersionTestCaseResponse.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def test_type(self):
        """Gets the test_type of this CreateVersionTestCaseResponse.

        测试类型

        :return: The test_type of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this CreateVersionTestCaseResponse.

        测试类型

        :param test_type: The test_type of this CreateVersionTestCaseResponse.
        :type test_type: int
        """
        self._test_type = test_type

    @property
    def test_type_name(self):
        """Gets the test_type_name of this CreateVersionTestCaseResponse.

        测试类型名称

        :return: The test_type_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_type_name

    @test_type_name.setter
    def test_type_name(self, test_type_name):
        """Sets the test_type_name of this CreateVersionTestCaseResponse.

        测试类型名称

        :param test_type_name: The test_type_name of this CreateVersionTestCaseResponse.
        :type test_type_name: str
        """
        self._test_type_name = test_type_name

    @property
    def design_note(self):
        """Gets the design_note of this CreateVersionTestCaseResponse.

        设计描述

        :return: The design_note of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._design_note

    @design_note.setter
    def design_note(self, design_note):
        """Sets the design_note of this CreateVersionTestCaseResponse.

        设计描述

        :param design_note: The design_note of this CreateVersionTestCaseResponse.
        :type design_note: str
        """
        self._design_note = design_note

    @property
    def test_step(self):
        """Gets the test_step of this CreateVersionTestCaseResponse.

        测试步骤

        :return: The test_step of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_step

    @test_step.setter
    def test_step(self, test_step):
        """Sets the test_step of this CreateVersionTestCaseResponse.

        测试步骤

        :param test_step: The test_step of this CreateVersionTestCaseResponse.
        :type test_step: str
        """
        self._test_step = test_step

    @property
    def expect_output(self):
        """Gets the expect_output of this CreateVersionTestCaseResponse.

        期望结果

        :return: The expect_output of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._expect_output

    @expect_output.setter
    def expect_output(self, expect_output):
        """Sets the expect_output of this CreateVersionTestCaseResponse.

        期望结果

        :param expect_output: The expect_output of this CreateVersionTestCaseResponse.
        :type expect_output: str
        """
        self._expect_output = expect_output

    @property
    def env_type(self):
        """Gets the env_type of this CreateVersionTestCaseResponse.

        测试环境类型

        :return: The env_type of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        """Sets the env_type of this CreateVersionTestCaseResponse.

        测试环境类型

        :param env_type: The env_type of this CreateVersionTestCaseResponse.
        :type env_type: str
        """
        self._env_type = env_type

    @property
    def exe_platform(self):
        """Gets the exe_platform of this CreateVersionTestCaseResponse.

        执行平台

        :return: The exe_platform of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._exe_platform

    @exe_platform.setter
    def exe_platform(self, exe_platform):
        """Sets the exe_platform of this CreateVersionTestCaseResponse.

        执行平台

        :param exe_platform: The exe_platform of this CreateVersionTestCaseResponse.
        :type exe_platform: str
        """
        self._exe_platform = exe_platform

    @property
    def testcase_project(self):
        """Gets the testcase_project of this CreateVersionTestCaseResponse.

        测试工程

        :return: The testcase_project of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._testcase_project

    @testcase_project.setter
    def testcase_project(self, testcase_project):
        """Sets the testcase_project of this CreateVersionTestCaseResponse.

        测试工程

        :param testcase_project: The testcase_project of this CreateVersionTestCaseResponse.
        :type testcase_project: str
        """
        self._testcase_project = testcase_project

    @property
    def svn_script_path(self):
        """Gets the svn_script_path of this CreateVersionTestCaseResponse.

        脚本路径

        :return: The svn_script_path of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._svn_script_path

    @svn_script_path.setter
    def svn_script_path(self, svn_script_path):
        """Sets the svn_script_path of this CreateVersionTestCaseResponse.

        脚本路径

        :param svn_script_path: The svn_script_path of this CreateVersionTestCaseResponse.
        :type svn_script_path: str
        """
        self._svn_script_path = svn_script_path

    @property
    def map_restrict(self):
        """Gets the map_restrict of this CreateVersionTestCaseResponse.

        约束条件

        :return: The map_restrict of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._map_restrict

    @map_restrict.setter
    def map_restrict(self, map_restrict):
        """Sets the map_restrict of this CreateVersionTestCaseResponse.

        约束条件

        :param map_restrict: The map_restrict of this CreateVersionTestCaseResponse.
        :type map_restrict: str
        """
        self._map_restrict = map_restrict

    @property
    def network_script_name(self):
        """Gets the network_script_name of this CreateVersionTestCaseResponse.

        网络脚本名

        :return: The network_script_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._network_script_name

    @network_script_name.setter
    def network_script_name(self, network_script_name):
        """Sets the network_script_name of this CreateVersionTestCaseResponse.

        网络脚本名

        :param network_script_name: The network_script_name of this CreateVersionTestCaseResponse.
        :type network_script_name: str
        """
        self._network_script_name = network_script_name

    @property
    def auto_type(self):
        """Gets the auto_type of this CreateVersionTestCaseResponse.

        自动化类型，非自动化:0, 是自动化:1

        :return: The auto_type of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._auto_type

    @auto_type.setter
    def auto_type(self, auto_type):
        """Sets the auto_type of this CreateVersionTestCaseResponse.

        自动化类型，非自动化:0, 是自动化:1

        :param auto_type: The auto_type of this CreateVersionTestCaseResponse.
        :type auto_type: int
        """
        self._auto_type = auto_type

    @property
    def to_be_auto_exec(self):
        """Gets the to_be_auto_exec of this CreateVersionTestCaseResponse.

        被自动化执行

        :return: The to_be_auto_exec of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._to_be_auto_exec

    @to_be_auto_exec.setter
    def to_be_auto_exec(self, to_be_auto_exec):
        """Sets the to_be_auto_exec of this CreateVersionTestCaseResponse.

        被自动化执行

        :param to_be_auto_exec: The to_be_auto_exec of this CreateVersionTestCaseResponse.
        :type to_be_auto_exec: int
        """
        self._to_be_auto_exec = to_be_auto_exec

    @property
    def last_result(self):
        """Gets the last_result of this CreateVersionTestCaseResponse.

        最后一次结果

        :return: The last_result of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._last_result

    @last_result.setter
    def last_result(self, last_result):
        """Sets the last_result of this CreateVersionTestCaseResponse.

        最后一次结果

        :param last_result: The last_result of this CreateVersionTestCaseResponse.
        :type last_result: str
        """
        self._last_result = last_result

    @property
    def last_result_uri(self):
        """Gets the last_result_uri of this CreateVersionTestCaseResponse.

        最后一次结果Uri

        :return: The last_result_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._last_result_uri

    @last_result_uri.setter
    def last_result_uri(self, last_result_uri):
        """Sets the last_result_uri of this CreateVersionTestCaseResponse.

        最后一次结果Uri

        :param last_result_uri: The last_result_uri of this CreateVersionTestCaseResponse.
        :type last_result_uri: str
        """
        self._last_result_uri = last_result_uri

    @property
    def feature_uri(self):
        """Gets the feature_uri of this CreateVersionTestCaseResponse.

        目录Uri

        :return: The feature_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        """Sets the feature_uri of this CreateVersionTestCaseResponse.

        目录Uri

        :param feature_uri: The feature_uri of this CreateVersionTestCaseResponse.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

    @property
    def feature_name(self):
        """Gets the feature_name of this CreateVersionTestCaseResponse.

        目录名称

        :return: The feature_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this CreateVersionTestCaseResponse.

        目录名称

        :param feature_name: The feature_name of this CreateVersionTestCaseResponse.
        :type feature_name: str
        """
        self._feature_name = feature_name

    @property
    def interface_name(self):
        """Gets the interface_name of this CreateVersionTestCaseResponse.

        测试接口名

        :return: The interface_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this CreateVersionTestCaseResponse.

        测试接口名

        :param interface_name: The interface_name of this CreateVersionTestCaseResponse.
        :type interface_name: str
        """
        self._interface_name = interface_name

    @property
    def snp_no(self):
        """Gets the snp_no of this CreateVersionTestCaseResponse.

        网络问题ID

        :return: The snp_no of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._snp_no

    @snp_no.setter
    def snp_no(self, snp_no):
        """Sets the snp_no of this CreateVersionTestCaseResponse.

        网络问题ID

        :param snp_no: The snp_no of this CreateVersionTestCaseResponse.
        :type snp_no: str
        """
        self._snp_no = snp_no

    @property
    def dr_relation_id(self):
        """Gets the dr_relation_id of this CreateVersionTestCaseResponse.

        关联需求编号

        :return: The dr_relation_id of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._dr_relation_id

    @dr_relation_id.setter
    def dr_relation_id(self, dr_relation_id):
        """Sets the dr_relation_id of this CreateVersionTestCaseResponse.

        关联需求编号

        :param dr_relation_id: The dr_relation_id of this CreateVersionTestCaseResponse.
        :type dr_relation_id: str
        """
        self._dr_relation_id = dr_relation_id

    @property
    def issue_name(self):
        """Gets the issue_name of this CreateVersionTestCaseResponse.

        需求名称

        :return: The issue_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._issue_name

    @issue_name.setter
    def issue_name(self, issue_name):
        """Sets the issue_name of this CreateVersionTestCaseResponse.

        需求名称

        :param issue_name: The issue_name of this CreateVersionTestCaseResponse.
        :type issue_name: str
        """
        self._issue_name = issue_name

    @property
    def test_base_num(self):
        """Gets the test_base_num of this CreateVersionTestCaseResponse.

        测试基数

        :return: The test_base_num of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_base_num

    @test_base_num.setter
    def test_base_num(self, test_base_num):
        """Sets the test_base_num of this CreateVersionTestCaseResponse.

        测试基数

        :param test_base_num: The test_base_num of this CreateVersionTestCaseResponse.
        :type test_base_num: str
        """
        self._test_base_num = test_base_num

    @property
    def automatically_executed(self):
        """Gets the automatically_executed of this CreateVersionTestCaseResponse.

        是否被自动化执行

        :return: The automatically_executed of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._automatically_executed

    @automatically_executed.setter
    def automatically_executed(self, automatically_executed):
        """Sets the automatically_executed of this CreateVersionTestCaseResponse.

        是否被自动化执行

        :param automatically_executed: The automatically_executed of this CreateVersionTestCaseResponse.
        :type automatically_executed: int
        """
        self._automatically_executed = automatically_executed

    @property
    def first_execute_time(self):
        """Gets the first_execute_time of this CreateVersionTestCaseResponse.

        第一次执行时间

        :return: The first_execute_time of this CreateVersionTestCaseResponse.
        :rtype: datetime
        """
        return self._first_execute_time

    @first_execute_time.setter
    def first_execute_time(self, first_execute_time):
        """Sets the first_execute_time of this CreateVersionTestCaseResponse.

        第一次执行时间

        :param first_execute_time: The first_execute_time of this CreateVersionTestCaseResponse.
        :type first_execute_time: datetime
        """
        self._first_execute_time = first_execute_time

    @property
    def detect_type(self):
        """Gets the detect_type of this CreateVersionTestCaseResponse.

        检测类型

        :return: The detect_type of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        """Sets the detect_type of this CreateVersionTestCaseResponse.

        检测类型

        :param detect_type: The detect_type of this CreateVersionTestCaseResponse.
        :type detect_type: str
        """
        self._detect_type = detect_type

    @property
    def execute_param(self):
        """Gets the execute_param of this CreateVersionTestCaseResponse.

        执行参数

        :return: The execute_param of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._execute_param

    @execute_param.setter
    def execute_param(self, execute_param):
        """Sets the execute_param of this CreateVersionTestCaseResponse.

        执行参数

        :param execute_param: The execute_param of this CreateVersionTestCaseResponse.
        :type execute_param: str
        """
        self._execute_param = execute_param

    @property
    def test_feature(self):
        """Gets the test_feature of this CreateVersionTestCaseResponse.

        分析领域

        :return: The test_feature of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_feature

    @test_feature.setter
    def test_feature(self, test_feature):
        """Sets the test_feature of this CreateVersionTestCaseResponse.

        分析领域

        :param test_feature: The test_feature of this CreateVersionTestCaseResponse.
        :type test_feature: str
        """
        self._test_feature = test_feature

    @property
    def is_contract_testcase(self):
        """Gets the is_contract_testcase of this CreateVersionTestCaseResponse.

        是否是契约用例，0:表示非契约用例, 1：表示契约用例

        :return: The is_contract_testcase of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._is_contract_testcase

    @is_contract_testcase.setter
    def is_contract_testcase(self, is_contract_testcase):
        """Sets the is_contract_testcase of this CreateVersionTestCaseResponse.

        是否是契约用例，0:表示非契约用例, 1：表示契约用例

        :param is_contract_testcase: The is_contract_testcase of this CreateVersionTestCaseResponse.
        :type is_contract_testcase: int
        """
        self._is_contract_testcase = is_contract_testcase

    @property
    def time_cost(self):
        """Gets the time_cost of this CreateVersionTestCaseResponse.

        总共耗时

        :return: The time_cost of this CreateVersionTestCaseResponse.
        :rtype: float
        """
        return self._time_cost

    @time_cost.setter
    def time_cost(self, time_cost):
        """Sets the time_cost of this CreateVersionTestCaseResponse.

        总共耗时

        :param time_cost: The time_cost of this CreateVersionTestCaseResponse.
        :type time_cost: float
        """
        self._time_cost = time_cost

    @property
    def be_auto_type_time(self):
        """Gets the be_auto_type_time of this CreateVersionTestCaseResponse.

        记录用例由非自动化变为自动化类型的时间

        :return: The be_auto_type_time of this CreateVersionTestCaseResponse.
        :rtype: datetime
        """
        return self._be_auto_type_time

    @be_auto_type_time.setter
    def be_auto_type_time(self, be_auto_type_time):
        """Sets the be_auto_type_time of this CreateVersionTestCaseResponse.

        记录用例由非自动化变为自动化类型的时间

        :param be_auto_type_time: The be_auto_type_time of this CreateVersionTestCaseResponse.
        :type be_auto_type_time: datetime
        """
        self._be_auto_type_time = be_auto_type_time

    @property
    def compare_number(self):
        """Gets the compare_number of this CreateVersionTestCaseResponse.

        配对用例编号

        :return: The compare_number of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._compare_number

    @compare_number.setter
    def compare_number(self, compare_number):
        """Sets the compare_number of this CreateVersionTestCaseResponse.

        配对用例编号

        :param compare_number: The compare_number of this CreateVersionTestCaseResponse.
        :type compare_number: str
        """
        self._compare_number = compare_number

    @property
    def scene_flag(self):
        """Gets the scene_flag of this CreateVersionTestCaseResponse.

        场景标识

        :return: The scene_flag of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._scene_flag

    @scene_flag.setter
    def scene_flag(self, scene_flag):
        """Sets the scene_flag of this CreateVersionTestCaseResponse.

        场景标识

        :param scene_flag: The scene_flag of this CreateVersionTestCaseResponse.
        :type scene_flag: str
        """
        self._scene_flag = scene_flag

    @property
    def base_flag(self):
        """Gets the base_flag of this CreateVersionTestCaseResponse.

        场景标识

        :return: The base_flag of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._base_flag

    @base_flag.setter
    def base_flag(self, base_flag):
        """Sets the base_flag of this CreateVersionTestCaseResponse.

        场景标识

        :param base_flag: The base_flag of this CreateVersionTestCaseResponse.
        :type base_flag: str
        """
        self._base_flag = base_flag

    @property
    def para_validator(self):
        """Gets the para_validator of this CreateVersionTestCaseResponse.

        区别是否从yaml中生成的用例，默认false

        :return: The para_validator of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._para_validator

    @para_validator.setter
    def para_validator(self, para_validator):
        """Sets the para_validator of this CreateVersionTestCaseResponse.

        区别是否从yaml中生成的用例，默认false

        :param para_validator: The para_validator of this CreateVersionTestCaseResponse.
        :type para_validator: str
        """
        self._para_validator = para_validator

    @property
    def knet_node_id(self):
        """Gets the knet_node_id of this CreateVersionTestCaseResponse.

        knet节点id

        :return: The knet_node_id of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._knet_node_id

    @knet_node_id.setter
    def knet_node_id(self, knet_node_id):
        """Sets the knet_node_id of this CreateVersionTestCaseResponse.

        knet节点id

        :param knet_node_id: The knet_node_id of this CreateVersionTestCaseResponse.
        :type knet_node_id: str
        """
        self._knet_node_id = knet_node_id

    @property
    def last_exe_author(self):
        """Gets the last_exe_author of this CreateVersionTestCaseResponse.

        最后一次执行用户

        :return: The last_exe_author of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._last_exe_author

    @last_exe_author.setter
    def last_exe_author(self, last_exe_author):
        """Sets the last_exe_author of this CreateVersionTestCaseResponse.

        最后一次执行用户

        :param last_exe_author: The last_exe_author of this CreateVersionTestCaseResponse.
        :type last_exe_author: str
        """
        self._last_exe_author = last_exe_author

    @property
    def cloud_carrier(self):
        """Gets the cloud_carrier of this CreateVersionTestCaseResponse.

        运营商

        :return: The cloud_carrier of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._cloud_carrier

    @cloud_carrier.setter
    def cloud_carrier(self, cloud_carrier):
        """Sets the cloud_carrier of this CreateVersionTestCaseResponse.

        运营商

        :param cloud_carrier: The cloud_carrier of this CreateVersionTestCaseResponse.
        :type cloud_carrier: str
        """
        self._cloud_carrier = cloud_carrier

    @property
    def market_place(self):
        """Gets the market_place of this CreateVersionTestCaseResponse.

        应用市场

        :return: The market_place of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._market_place

    @market_place.setter
    def market_place(self, market_place):
        """Sets the market_place of this CreateVersionTestCaseResponse.

        应用市场

        :param market_place: The market_place of this CreateVersionTestCaseResponse.
        :type market_place: str
        """
        self._market_place = market_place

    @property
    def test_mind_id(self):
        """Gets the test_mind_id of this CreateVersionTestCaseResponse.

        脑图id

        :return: The test_mind_id of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_mind_id

    @test_mind_id.setter
    def test_mind_id(self, test_mind_id):
        """Sets the test_mind_id of this CreateVersionTestCaseResponse.

        脑图id

        :param test_mind_id: The test_mind_id of this CreateVersionTestCaseResponse.
        :type test_mind_id: str
        """
        self._test_mind_id = test_mind_id

    @property
    def test_mind_url(self):
        """Gets the test_mind_url of this CreateVersionTestCaseResponse.

        脑图url

        :return: The test_mind_url of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_mind_url

    @test_mind_url.setter
    def test_mind_url(self, test_mind_url):
        """Sets the test_mind_url of this CreateVersionTestCaseResponse.

        脑图url

        :param test_mind_url: The test_mind_url of this CreateVersionTestCaseResponse.
        :type test_mind_url: str
        """
        self._test_mind_url = test_mind_url

    @property
    def commit_url(self):
        """Gets the commit_url of this CreateVersionTestCaseResponse.

        git提交url

        :return: The commit_url of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._commit_url

    @commit_url.setter
    def commit_url(self, commit_url):
        """Sets the commit_url of this CreateVersionTestCaseResponse.

        git提交url

        :param commit_url: The commit_url of this CreateVersionTestCaseResponse.
        :type commit_url: str
        """
        self._commit_url = commit_url

    @property
    def test_pattern_number(self):
        """Gets the test_pattern_number of this CreateVersionTestCaseResponse.

        测试模式编号

        :return: The test_pattern_number of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_pattern_number

    @test_pattern_number.setter
    def test_pattern_number(self, test_pattern_number):
        """Sets the test_pattern_number of this CreateVersionTestCaseResponse.

        测试模式编号

        :param test_pattern_number: The test_pattern_number of this CreateVersionTestCaseResponse.
        :type test_pattern_number: str
        """
        self._test_pattern_number = test_pattern_number

    @property
    def test_factor_number(self):
        """Gets the test_factor_number of this CreateVersionTestCaseResponse.

        测试因子编号

        :return: The test_factor_number of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._test_factor_number

    @test_factor_number.setter
    def test_factor_number(self, test_factor_number):
        """Sets the test_factor_number of this CreateVersionTestCaseResponse.

        测试因子编号

        :param test_factor_number: The test_factor_number of this CreateVersionTestCaseResponse.
        :type test_factor_number: str
        """
        self._test_factor_number = test_factor_number

    @property
    def status_code(self):
        """Gets the status_code of this CreateVersionTestCaseResponse.

        状态Code

        :return: The status_code of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CreateVersionTestCaseResponse.

        状态Code

        :param status_code: The status_code of this CreateVersionTestCaseResponse.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def result_code(self):
        """Gets the result_code of this CreateVersionTestCaseResponse.

        结果Code

        :return: The result_code of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this CreateVersionTestCaseResponse.

        结果Code

        :param result_code: The result_code of this CreateVersionTestCaseResponse.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def release_id(self):
        """Gets the release_id of this CreateVersionTestCaseResponse.

        迭代ID

        :return: The release_id of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this CreateVersionTestCaseResponse.

        迭代ID

        :param release_id: The release_id of this CreateVersionTestCaseResponse.
        :type release_id: str
        """
        self._release_id = release_id

    @property
    def label_id(self):
        """Gets the label_id of this CreateVersionTestCaseResponse.

        标签ID

        :return: The label_id of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this CreateVersionTestCaseResponse.

        标签ID

        :param label_id: The label_id of this CreateVersionTestCaseResponse.
        :type label_id: str
        """
        self._label_id = label_id

    @property
    def labels(self):
        """Gets the labels of this CreateVersionTestCaseResponse.

        用例标签名称列表

        :return: The labels of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateVersionTestCaseResponse.

        用例标签名称列表

        :param labels: The labels of this CreateVersionTestCaseResponse.
        :type labels: str
        """
        self._labels = labels

    @property
    def module_id(self):
        """Gets the module_id of this CreateVersionTestCaseResponse.

        模块ID

        :return: The module_id of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this CreateVersionTestCaseResponse.

        模块ID

        :param module_id: The module_id of this CreateVersionTestCaseResponse.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def module_name(self):
        """Gets the module_name of this CreateVersionTestCaseResponse.

        模块名称

        :return: The module_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this CreateVersionTestCaseResponse.

        模块名称

        :param module_name: The module_name of this CreateVersionTestCaseResponse.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_path(self):
        """Gets the module_path of this CreateVersionTestCaseResponse.

        模块path

        :return: The module_path of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._module_path

    @module_path.setter
    def module_path(self, module_path):
        """Sets the module_path of this CreateVersionTestCaseResponse.

        模块path

        :param module_path: The module_path of this CreateVersionTestCaseResponse.
        :type module_path: str
        """
        self._module_path = module_path

    @property
    def module_path_name(self):
        """Gets the module_path_name of this CreateVersionTestCaseResponse.

        模块路径名称

        :return: The module_path_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._module_path_name

    @module_path_name.setter
    def module_path_name(self, module_path_name):
        """Sets the module_path_name of this CreateVersionTestCaseResponse.

        模块路径名称

        :param module_path_name: The module_path_name of this CreateVersionTestCaseResponse.
        :type module_path_name: str
        """
        self._module_path_name = module_path_name

    @property
    def execute_latest_time(self):
        """Gets the execute_latest_time of this CreateVersionTestCaseResponse.

        最后执行时间

        :return: The execute_latest_time of this CreateVersionTestCaseResponse.
        :rtype: datetime
        """
        return self._execute_latest_time

    @execute_latest_time.setter
    def execute_latest_time(self, execute_latest_time):
        """Sets the execute_latest_time of this CreateVersionTestCaseResponse.

        最后执行时间

        :param execute_latest_time: The execute_latest_time of this CreateVersionTestCaseResponse.
        :type execute_latest_time: datetime
        """
        self._execute_latest_time = execute_latest_time

    @property
    def execute_duration(self):
        """Gets the execute_duration of this CreateVersionTestCaseResponse.

        执行时长

        :return: The execute_duration of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._execute_duration

    @execute_duration.setter
    def execute_duration(self, execute_duration):
        """Sets the execute_duration of this CreateVersionTestCaseResponse.

        执行时长

        :param execute_duration: The execute_duration of this CreateVersionTestCaseResponse.
        :type execute_duration: str
        """
        self._execute_duration = execute_duration

    @property
    def execute_times(self):
        """Gets the execute_times of this CreateVersionTestCaseResponse.

        执行次数

        :return: The execute_times of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._execute_times

    @execute_times.setter
    def execute_times(self, execute_times):
        """Sets the execute_times of this CreateVersionTestCaseResponse.

        执行次数

        :param execute_times: The execute_times of this CreateVersionTestCaseResponse.
        :type execute_times: int
        """
        self._execute_times = execute_times

    @property
    def is_keyword(self):
        """Gets the is_keyword of this CreateVersionTestCaseResponse.

        是否关键用例

        :return: The is_keyword of this CreateVersionTestCaseResponse.
        :rtype: int
        """
        return self._is_keyword

    @is_keyword.setter
    def is_keyword(self, is_keyword):
        """Sets the is_keyword of this CreateVersionTestCaseResponse.

        是否关键用例

        :param is_keyword: The is_keyword of this CreateVersionTestCaseResponse.
        :type is_keyword: int
        """
        self._is_keyword = is_keyword

    @property
    def release_dev(self):
        """Gets the release_dev of this CreateVersionTestCaseResponse.

        测试版本号

        :return: The release_dev of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        """Sets the release_dev of this CreateVersionTestCaseResponse.

        测试版本号

        :param release_dev: The release_dev of this CreateVersionTestCaseResponse.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def new_created(self):
        """Gets the new_created of this CreateVersionTestCaseResponse.

        是否用户新增用例

        :return: The new_created of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._new_created

    @new_created.setter
    def new_created(self, new_created):
        """Sets the new_created of this CreateVersionTestCaseResponse.

        是否用户新增用例

        :param new_created: The new_created of this CreateVersionTestCaseResponse.
        :type new_created: str
        """
        self._new_created = new_created

    @property
    def project_uuid(self):
        """Gets the project_uuid of this CreateVersionTestCaseResponse.

        项目ID

        :return: The project_uuid of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this CreateVersionTestCaseResponse.

        项目ID

        :param project_uuid: The project_uuid of this CreateVersionTestCaseResponse.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def creation_version_name(self):
        """Gets the creation_version_name of this CreateVersionTestCaseResponse.

        创建版本名称，原逻辑marshall添加字段

        :return: The creation_version_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._creation_version_name

    @creation_version_name.setter
    def creation_version_name(self, creation_version_name):
        """Sets the creation_version_name of this CreateVersionTestCaseResponse.

        创建版本名称，原逻辑marshall添加字段

        :param creation_version_name: The creation_version_name of this CreateVersionTestCaseResponse.
        :type creation_version_name: str
        """
        self._creation_version_name = creation_version_name

    @property
    def feature_path(self):
        """Gets the feature_path of this CreateVersionTestCaseResponse.

        特性路径，原逻辑marshall添加字段

        :return: The feature_path of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._feature_path

    @feature_path.setter
    def feature_path(self, feature_path):
        """Sets the feature_path of this CreateVersionTestCaseResponse.

        特性路径，原逻辑marshall添加字段

        :param feature_path: The feature_path of this CreateVersionTestCaseResponse.
        :type feature_path: str
        """
        self._feature_path = feature_path

    @property
    def testcase_uri(self):
        """Gets the testcase_uri of this CreateVersionTestCaseResponse.

        实体用例Uri，IteratorTestCase字段

        :return: The testcase_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._testcase_uri

    @testcase_uri.setter
    def testcase_uri(self, testcase_uri):
        """Sets the testcase_uri of this CreateVersionTestCaseResponse.

        实体用例Uri，IteratorTestCase字段

        :param testcase_uri: The testcase_uri of this CreateVersionTestCaseResponse.
        :type testcase_uri: str
        """
        self._testcase_uri = testcase_uri

    @property
    def owner_name(self):
        """Gets the owner_name of this CreateVersionTestCaseResponse.

        处理人名称

        :return: The owner_name of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this CreateVersionTestCaseResponse.

        处理人名称

        :param owner_name: The owner_name of this CreateVersionTestCaseResponse.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def iterator_case_uri(self):
        """Gets the iterator_case_uri of this CreateVersionTestCaseResponse.

        迭代用例Uri，IteratorTestCase字段

        :return: The iterator_case_uri of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._iterator_case_uri

    @iterator_case_uri.setter
    def iterator_case_uri(self, iterator_case_uri):
        """Sets the iterator_case_uri of this CreateVersionTestCaseResponse.

        迭代用例Uri，IteratorTestCase字段

        :param iterator_case_uri: The iterator_case_uri of this CreateVersionTestCaseResponse.
        :type iterator_case_uri: str
        """
        self._iterator_case_uri = iterator_case_uri

    @property
    def script_link(self):
        """Gets the script_link of this CreateVersionTestCaseResponse.

        脚本链接scriptLink

        :return: The script_link of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._script_link

    @script_link.setter
    def script_link(self, script_link):
        """Sets the script_link of this CreateVersionTestCaseResponse.

        脚本链接scriptLink

        :param script_link: The script_link of this CreateVersionTestCaseResponse.
        :type script_link: str
        """
        self._script_link = script_link

    @property
    def custom_field_1(self):
        """Gets the custom_field_1 of this CreateVersionTestCaseResponse.

        自定义字段1

        :return: The custom_field_1 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_1

    @custom_field_1.setter
    def custom_field_1(self, custom_field_1):
        """Sets the custom_field_1 of this CreateVersionTestCaseResponse.

        自定义字段1

        :param custom_field_1: The custom_field_1 of this CreateVersionTestCaseResponse.
        :type custom_field_1: str
        """
        self._custom_field_1 = custom_field_1

    @property
    def custom_field_2(self):
        """Gets the custom_field_2 of this CreateVersionTestCaseResponse.

        自定义字段2

        :return: The custom_field_2 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_2

    @custom_field_2.setter
    def custom_field_2(self, custom_field_2):
        """Sets the custom_field_2 of this CreateVersionTestCaseResponse.

        自定义字段2

        :param custom_field_2: The custom_field_2 of this CreateVersionTestCaseResponse.
        :type custom_field_2: str
        """
        self._custom_field_2 = custom_field_2

    @property
    def custom_field_3(self):
        """Gets the custom_field_3 of this CreateVersionTestCaseResponse.

        自定义字段3

        :return: The custom_field_3 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_3

    @custom_field_3.setter
    def custom_field_3(self, custom_field_3):
        """Sets the custom_field_3 of this CreateVersionTestCaseResponse.

        自定义字段3

        :param custom_field_3: The custom_field_3 of this CreateVersionTestCaseResponse.
        :type custom_field_3: str
        """
        self._custom_field_3 = custom_field_3

    @property
    def custom_field_4(self):
        """Gets the custom_field_4 of this CreateVersionTestCaseResponse.

        自定义字段4

        :return: The custom_field_4 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_4

    @custom_field_4.setter
    def custom_field_4(self, custom_field_4):
        """Sets the custom_field_4 of this CreateVersionTestCaseResponse.

        自定义字段4

        :param custom_field_4: The custom_field_4 of this CreateVersionTestCaseResponse.
        :type custom_field_4: str
        """
        self._custom_field_4 = custom_field_4

    @property
    def custom_field_5(self):
        """Gets the custom_field_5 of this CreateVersionTestCaseResponse.

        自定义字段5

        :return: The custom_field_5 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_5

    @custom_field_5.setter
    def custom_field_5(self, custom_field_5):
        """Sets the custom_field_5 of this CreateVersionTestCaseResponse.

        自定义字段5

        :param custom_field_5: The custom_field_5 of this CreateVersionTestCaseResponse.
        :type custom_field_5: str
        """
        self._custom_field_5 = custom_field_5

    @property
    def custom_field_6(self):
        """Gets the custom_field_6 of this CreateVersionTestCaseResponse.

        自定义字段6

        :return: The custom_field_6 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_6

    @custom_field_6.setter
    def custom_field_6(self, custom_field_6):
        """Sets the custom_field_6 of this CreateVersionTestCaseResponse.

        自定义字段6

        :param custom_field_6: The custom_field_6 of this CreateVersionTestCaseResponse.
        :type custom_field_6: str
        """
        self._custom_field_6 = custom_field_6

    @property
    def custom_field_7(self):
        """Gets the custom_field_7 of this CreateVersionTestCaseResponse.

        自定义字段7

        :return: The custom_field_7 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_7

    @custom_field_7.setter
    def custom_field_7(self, custom_field_7):
        """Sets the custom_field_7 of this CreateVersionTestCaseResponse.

        自定义字段7

        :param custom_field_7: The custom_field_7 of this CreateVersionTestCaseResponse.
        :type custom_field_7: str
        """
        self._custom_field_7 = custom_field_7

    @property
    def custom_field_8(self):
        """Gets the custom_field_8 of this CreateVersionTestCaseResponse.

        自定义字段8

        :return: The custom_field_8 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_8

    @custom_field_8.setter
    def custom_field_8(self, custom_field_8):
        """Sets the custom_field_8 of this CreateVersionTestCaseResponse.

        自定义字段8

        :param custom_field_8: The custom_field_8 of this CreateVersionTestCaseResponse.
        :type custom_field_8: str
        """
        self._custom_field_8 = custom_field_8

    @property
    def custom_field_9(self):
        """Gets the custom_field_9 of this CreateVersionTestCaseResponse.

        自定义字段9

        :return: The custom_field_9 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_9

    @custom_field_9.setter
    def custom_field_9(self, custom_field_9):
        """Sets the custom_field_9 of this CreateVersionTestCaseResponse.

        自定义字段9

        :param custom_field_9: The custom_field_9 of this CreateVersionTestCaseResponse.
        :type custom_field_9: str
        """
        self._custom_field_9 = custom_field_9

    @property
    def custom_field_10(self):
        """Gets the custom_field_10 of this CreateVersionTestCaseResponse.

        自定义字段10

        :return: The custom_field_10 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_10

    @custom_field_10.setter
    def custom_field_10(self, custom_field_10):
        """Sets the custom_field_10 of this CreateVersionTestCaseResponse.

        自定义字段10

        :param custom_field_10: The custom_field_10 of this CreateVersionTestCaseResponse.
        :type custom_field_10: str
        """
        self._custom_field_10 = custom_field_10

    @property
    def custom_field_11(self):
        """Gets the custom_field_11 of this CreateVersionTestCaseResponse.

        自定义字段11

        :return: The custom_field_11 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_11

    @custom_field_11.setter
    def custom_field_11(self, custom_field_11):
        """Sets the custom_field_11 of this CreateVersionTestCaseResponse.

        自定义字段11

        :param custom_field_11: The custom_field_11 of this CreateVersionTestCaseResponse.
        :type custom_field_11: str
        """
        self._custom_field_11 = custom_field_11

    @property
    def custom_field_12(self):
        """Gets the custom_field_12 of this CreateVersionTestCaseResponse.

        自定义字段12

        :return: The custom_field_12 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_12

    @custom_field_12.setter
    def custom_field_12(self, custom_field_12):
        """Sets the custom_field_12 of this CreateVersionTestCaseResponse.

        自定义字段12

        :param custom_field_12: The custom_field_12 of this CreateVersionTestCaseResponse.
        :type custom_field_12: str
        """
        self._custom_field_12 = custom_field_12

    @property
    def custom_field_13(self):
        """Gets the custom_field_13 of this CreateVersionTestCaseResponse.

        自定义字段13

        :return: The custom_field_13 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_13

    @custom_field_13.setter
    def custom_field_13(self, custom_field_13):
        """Sets the custom_field_13 of this CreateVersionTestCaseResponse.

        自定义字段13

        :param custom_field_13: The custom_field_13 of this CreateVersionTestCaseResponse.
        :type custom_field_13: str
        """
        self._custom_field_13 = custom_field_13

    @property
    def custom_field_14(self):
        """Gets the custom_field_14 of this CreateVersionTestCaseResponse.

        自定义字段14

        :return: The custom_field_14 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_14

    @custom_field_14.setter
    def custom_field_14(self, custom_field_14):
        """Sets the custom_field_14 of this CreateVersionTestCaseResponse.

        自定义字段14

        :param custom_field_14: The custom_field_14 of this CreateVersionTestCaseResponse.
        :type custom_field_14: str
        """
        self._custom_field_14 = custom_field_14

    @property
    def custom_field_15(self):
        """Gets the custom_field_15 of this CreateVersionTestCaseResponse.

        自定义字段15

        :return: The custom_field_15 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_15

    @custom_field_15.setter
    def custom_field_15(self, custom_field_15):
        """Sets the custom_field_15 of this CreateVersionTestCaseResponse.

        自定义字段15

        :param custom_field_15: The custom_field_15 of this CreateVersionTestCaseResponse.
        :type custom_field_15: str
        """
        self._custom_field_15 = custom_field_15

    @property
    def custom_field_16(self):
        """Gets the custom_field_16 of this CreateVersionTestCaseResponse.

        自定义字段16

        :return: The custom_field_16 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_16

    @custom_field_16.setter
    def custom_field_16(self, custom_field_16):
        """Sets the custom_field_16 of this CreateVersionTestCaseResponse.

        自定义字段16

        :param custom_field_16: The custom_field_16 of this CreateVersionTestCaseResponse.
        :type custom_field_16: str
        """
        self._custom_field_16 = custom_field_16

    @property
    def custom_field_17(self):
        """Gets the custom_field_17 of this CreateVersionTestCaseResponse.

        自定义字段17

        :return: The custom_field_17 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_17

    @custom_field_17.setter
    def custom_field_17(self, custom_field_17):
        """Sets the custom_field_17 of this CreateVersionTestCaseResponse.

        自定义字段17

        :param custom_field_17: The custom_field_17 of this CreateVersionTestCaseResponse.
        :type custom_field_17: str
        """
        self._custom_field_17 = custom_field_17

    @property
    def custom_field_18(self):
        """Gets the custom_field_18 of this CreateVersionTestCaseResponse.

        自定义字段18

        :return: The custom_field_18 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_18

    @custom_field_18.setter
    def custom_field_18(self, custom_field_18):
        """Sets the custom_field_18 of this CreateVersionTestCaseResponse.

        自定义字段18

        :param custom_field_18: The custom_field_18 of this CreateVersionTestCaseResponse.
        :type custom_field_18: str
        """
        self._custom_field_18 = custom_field_18

    @property
    def custom_field_19(self):
        """Gets the custom_field_19 of this CreateVersionTestCaseResponse.

        自定义字段19

        :return: The custom_field_19 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_19

    @custom_field_19.setter
    def custom_field_19(self, custom_field_19):
        """Sets the custom_field_19 of this CreateVersionTestCaseResponse.

        自定义字段19

        :param custom_field_19: The custom_field_19 of this CreateVersionTestCaseResponse.
        :type custom_field_19: str
        """
        self._custom_field_19 = custom_field_19

    @property
    def custom_field_20(self):
        """Gets the custom_field_20 of this CreateVersionTestCaseResponse.

        自定义字段20

        :return: The custom_field_20 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_20

    @custom_field_20.setter
    def custom_field_20(self, custom_field_20):
        """Sets the custom_field_20 of this CreateVersionTestCaseResponse.

        自定义字段20

        :param custom_field_20: The custom_field_20 of this CreateVersionTestCaseResponse.
        :type custom_field_20: str
        """
        self._custom_field_20 = custom_field_20

    @property
    def custom_field_21(self):
        """Gets the custom_field_21 of this CreateVersionTestCaseResponse.

        自定义字段21

        :return: The custom_field_21 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_21

    @custom_field_21.setter
    def custom_field_21(self, custom_field_21):
        """Sets the custom_field_21 of this CreateVersionTestCaseResponse.

        自定义字段21

        :param custom_field_21: The custom_field_21 of this CreateVersionTestCaseResponse.
        :type custom_field_21: str
        """
        self._custom_field_21 = custom_field_21

    @property
    def custom_field_22(self):
        """Gets the custom_field_22 of this CreateVersionTestCaseResponse.

        自定义字段22

        :return: The custom_field_22 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_22

    @custom_field_22.setter
    def custom_field_22(self, custom_field_22):
        """Sets the custom_field_22 of this CreateVersionTestCaseResponse.

        自定义字段22

        :param custom_field_22: The custom_field_22 of this CreateVersionTestCaseResponse.
        :type custom_field_22: str
        """
        self._custom_field_22 = custom_field_22

    @property
    def custom_field_23(self):
        """Gets the custom_field_23 of this CreateVersionTestCaseResponse.

        自定义字段23

        :return: The custom_field_23 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_23

    @custom_field_23.setter
    def custom_field_23(self, custom_field_23):
        """Sets the custom_field_23 of this CreateVersionTestCaseResponse.

        自定义字段23

        :param custom_field_23: The custom_field_23 of this CreateVersionTestCaseResponse.
        :type custom_field_23: str
        """
        self._custom_field_23 = custom_field_23

    @property
    def custom_field_24(self):
        """Gets the custom_field_24 of this CreateVersionTestCaseResponse.

        自定义字段24

        :return: The custom_field_24 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_24

    @custom_field_24.setter
    def custom_field_24(self, custom_field_24):
        """Sets the custom_field_24 of this CreateVersionTestCaseResponse.

        自定义字段24

        :param custom_field_24: The custom_field_24 of this CreateVersionTestCaseResponse.
        :type custom_field_24: str
        """
        self._custom_field_24 = custom_field_24

    @property
    def custom_field_25(self):
        """Gets the custom_field_25 of this CreateVersionTestCaseResponse.

        自定义字段25

        :return: The custom_field_25 of this CreateVersionTestCaseResponse.
        :rtype: str
        """
        return self._custom_field_25

    @custom_field_25.setter
    def custom_field_25(self, custom_field_25):
        """Sets the custom_field_25 of this CreateVersionTestCaseResponse.

        自定义字段25

        :param custom_field_25: The custom_field_25 of this CreateVersionTestCaseResponse.
        :type custom_field_25: str
        """
        self._custom_field_25 = custom_field_25

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
        if not isinstance(other, CreateVersionTestCaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
