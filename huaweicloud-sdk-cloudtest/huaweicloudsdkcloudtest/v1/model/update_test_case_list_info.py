# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestCaseListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'steps': 'list[TestCaseStepInfo]',
        'attachments': 'list[TestCaseAttachmentInfo]',
        'author': 'str',
        'name': 'str',
        'rank': 'int',
        'owner': 'str',
        'preparation': 'str',
        'remark': 'str',
        'stage': 'str',
        'activity': 'str',
        'keywords': 'str',
        'market': 'str',
        'designer': 'str',
        'tags': 'str',
        'region': 'str',
        'relate_type': 'str',
        'service_type': 'int',
        'only_change_script': 'str',
        'add_to_iterator': 'str',
        'need_update_relation': 'str',
        'creation_version_uri': 'str',
        'number': 'str',
        'case_type': 'int',
        'platform_type': 'int',
        'test_type': 'int',
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
        'interface_name': 'str',
        'snp_no': 'str',
        'dr_relation_id': 'str',
        'test_base_num': 'str',
        'automatically_executed': 'int',
        'first_execute_time': 'datetime',
        'detect_type': 'str',
        'execute_param': 'str',
        'test_feature': 'str',
        'is_contract_testcase': 'int',
        'time_cost': 'float',
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
        'custom_field_25': 'str',
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
        'label_names': 'list[str]',
        'module_id': 'str',
        'execute_latest_time': 'datetime',
        'execute_duration': 'str',
        'is_keyword': 'int',
        'release_dev': 'str',
        'new_created': 'int',
        'execute_parameter': 'str',
        'project_uuid': 'str',
        'version_uri': 'str',
        'case_list': 'list[CaseInfo]',
        'case_id_list': 'list[str]'
    }

    attribute_map = {
        'steps': 'steps',
        'attachments': 'attachments',
        'author': 'author',
        'name': 'name',
        'rank': 'rank',
        'owner': 'owner',
        'preparation': 'preparation',
        'remark': 'remark',
        'stage': 'stage',
        'activity': 'activity',
        'keywords': 'keywords',
        'market': 'market',
        'designer': 'designer',
        'tags': 'tags',
        'region': 'region',
        'relate_type': 'relate_type',
        'service_type': 'service_type',
        'only_change_script': 'only_change_script',
        'add_to_iterator': 'add_to_iterator',
        'need_update_relation': 'need_update_relation',
        'creation_version_uri': 'creation_version_uri',
        'number': 'number',
        'case_type': 'case_type',
        'platform_type': 'platform_type',
        'test_type': 'test_type',
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
        'interface_name': 'interface_name',
        'snp_no': 'snp_no',
        'dr_relation_id': 'dr_relation_id',
        'test_base_num': 'test_base_num',
        'automatically_executed': 'automatically_executed',
        'first_execute_time': 'first_execute_time',
        'detect_type': 'detect_type',
        'execute_param': 'execute_param',
        'test_feature': 'test_feature',
        'is_contract_testcase': 'is_contract_testcase',
        'time_cost': 'time_cost',
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
        'custom_field_25': 'custom_field_25',
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
        'label_names': 'label_names',
        'module_id': 'module_id',
        'execute_latest_time': 'execute_latest_time',
        'execute_duration': 'execute_duration',
        'is_keyword': 'is_keyword',
        'release_dev': 'release_dev',
        'new_created': 'new_created',
        'execute_parameter': 'execute_parameter',
        'project_uuid': 'project_uuid',
        'version_uri': 'version_uri',
        'case_list': 'case_list',
        'case_id_list': 'case_id_list'
    }

    def __init__(self, steps=None, attachments=None, author=None, name=None, rank=None, owner=None, preparation=None, remark=None, stage=None, activity=None, keywords=None, market=None, designer=None, tags=None, region=None, relate_type=None, service_type=None, only_change_script=None, add_to_iterator=None, need_update_relation=None, creation_version_uri=None, number=None, case_type=None, platform_type=None, test_type=None, design_note=None, test_step=None, expect_output=None, env_type=None, exe_platform=None, testcase_project=None, svn_script_path=None, map_restrict=None, network_script_name=None, auto_type=None, to_be_auto_exec=None, last_result=None, last_result_uri=None, feature_uri=None, interface_name=None, snp_no=None, dr_relation_id=None, test_base_num=None, automatically_executed=None, first_execute_time=None, detect_type=None, execute_param=None, test_feature=None, is_contract_testcase=None, time_cost=None, custom_field_1=None, custom_field_2=None, custom_field_3=None, custom_field_4=None, custom_field_5=None, custom_field_6=None, custom_field_7=None, custom_field_8=None, custom_field_9=None, custom_field_10=None, custom_field_11=None, custom_field_12=None, custom_field_13=None, custom_field_14=None, custom_field_15=None, custom_field_16=None, custom_field_17=None, custom_field_18=None, custom_field_19=None, custom_field_20=None, custom_field_21=None, custom_field_22=None, custom_field_23=None, custom_field_24=None, custom_field_25=None, be_auto_type_time=None, compare_number=None, scene_flag=None, base_flag=None, para_validator=None, knet_node_id=None, last_exe_author=None, cloud_carrier=None, market_place=None, test_mind_id=None, test_mind_url=None, commit_url=None, test_pattern_number=None, test_factor_number=None, status_code=None, result_code=None, release_id=None, label_id=None, label_names=None, module_id=None, execute_latest_time=None, execute_duration=None, is_keyword=None, release_dev=None, new_created=None, execute_parameter=None, project_uuid=None, version_uri=None, case_list=None, case_id_list=None):
        """UpdateTestCaseListInfo

        The model defined in huaweicloud sdk

        :param steps: 对外测试步骤
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseStepInfo`]
        :param attachments: 对外附件
        :type attachments: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseAttachmentInfo`]
        :param author: 创建人
        :type author: str
        :param name: 名称
        :type name: str
        :param rank: 用例等级
        :type rank: int
        :param owner: 处理人
        :type owner: str
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
        :param region: 逻辑region，外部使用公有云实际区域，内部使用默认值
        :type region: str
        :param relate_type: 对外关联资源类型
        :type relate_type: str
        :param service_type: 服务类型
        :type service_type: int
        :param only_change_script: 对外只更新接口用例的java脚本路径标识
        :type only_change_script: str
        :param add_to_iterator: 对外需求添加到迭代标识
        :type add_to_iterator: str
        :param need_update_relation: 是否修改关联关系
        :type need_update_relation: str
        :param creation_version_uri: 创建版本Uri
        :type creation_version_uri: str
        :param number: 用例编号
        :type number: str
        :param case_type: 用例类型
        :type case_type: int
        :param platform_type: 执行平台类型
        :type platform_type: int
        :param test_type: 测试类型
        :type test_type: int
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
        :param interface_name: 测试接口名
        :type interface_name: str
        :param snp_no: 网络问题ID
        :type snp_no: str
        :param dr_relation_id: 关联需求编号
        :type dr_relation_id: str
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
        :param label_names: 对外用例操作时，标签名列表
        :type label_names: list[str]
        :param module_id: 模块ID
        :type module_id: str
        :param execute_latest_time: 最后执行时间
        :type execute_latest_time: datetime
        :param execute_duration: 执行时长
        :type execute_duration: str
        :param is_keyword: 是否关键用例
        :type is_keyword: int
        :param release_dev: 测试版本号
        :type release_dev: str
        :param new_created: 是否用户新增用例
        :type new_created: int
        :param execute_parameter: 执行参数
        :type execute_parameter: str
        :param project_uuid: 项目ID，外部使用项目ID，内部使用默认值
        :type project_uuid: str
        :param version_uri: 分支或者迭代uri
        :type version_uri: str
        :param case_list: 更新用例信息列表
        :type case_list: list[:class:`huaweicloudsdkcloudtest.v1.CaseInfo`]
        :param case_id_list: 批量更新用例id列表
        :type case_id_list: list[str]
        """
        
        

        self._steps = None
        self._attachments = None
        self._author = None
        self._name = None
        self._rank = None
        self._owner = None
        self._preparation = None
        self._remark = None
        self._stage = None
        self._activity = None
        self._keywords = None
        self._market = None
        self._designer = None
        self._tags = None
        self._region = None
        self._relate_type = None
        self._service_type = None
        self._only_change_script = None
        self._add_to_iterator = None
        self._need_update_relation = None
        self._creation_version_uri = None
        self._number = None
        self._case_type = None
        self._platform_type = None
        self._test_type = None
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
        self._interface_name = None
        self._snp_no = None
        self._dr_relation_id = None
        self._test_base_num = None
        self._automatically_executed = None
        self._first_execute_time = None
        self._detect_type = None
        self._execute_param = None
        self._test_feature = None
        self._is_contract_testcase = None
        self._time_cost = None
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
        self._label_names = None
        self._module_id = None
        self._execute_latest_time = None
        self._execute_duration = None
        self._is_keyword = None
        self._release_dev = None
        self._new_created = None
        self._execute_parameter = None
        self._project_uuid = None
        self._version_uri = None
        self._case_list = None
        self._case_id_list = None
        self.discriminator = None

        if steps is not None:
            self.steps = steps
        if attachments is not None:
            self.attachments = attachments
        if author is not None:
            self.author = author
        self.name = name
        if rank is not None:
            self.rank = rank
        if owner is not None:
            self.owner = owner
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
        if region is not None:
            self.region = region
        if relate_type is not None:
            self.relate_type = relate_type
        if service_type is not None:
            self.service_type = service_type
        if only_change_script is not None:
            self.only_change_script = only_change_script
        if add_to_iterator is not None:
            self.add_to_iterator = add_to_iterator
        if need_update_relation is not None:
            self.need_update_relation = need_update_relation
        if creation_version_uri is not None:
            self.creation_version_uri = creation_version_uri
        if number is not None:
            self.number = number
        if case_type is not None:
            self.case_type = case_type
        if platform_type is not None:
            self.platform_type = platform_type
        if test_type is not None:
            self.test_type = test_type
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
        if interface_name is not None:
            self.interface_name = interface_name
        if snp_no is not None:
            self.snp_no = snp_no
        if dr_relation_id is not None:
            self.dr_relation_id = dr_relation_id
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
        if label_names is not None:
            self.label_names = label_names
        if module_id is not None:
            self.module_id = module_id
        if execute_latest_time is not None:
            self.execute_latest_time = execute_latest_time
        if execute_duration is not None:
            self.execute_duration = execute_duration
        if is_keyword is not None:
            self.is_keyword = is_keyword
        if release_dev is not None:
            self.release_dev = release_dev
        if new_created is not None:
            self.new_created = new_created
        if execute_parameter is not None:
            self.execute_parameter = execute_parameter
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if version_uri is not None:
            self.version_uri = version_uri
        if case_list is not None:
            self.case_list = case_list
        if case_id_list is not None:
            self.case_id_list = case_id_list

    @property
    def steps(self):
        """Gets the steps of this UpdateTestCaseListInfo.

        对外测试步骤

        :return: The steps of this UpdateTestCaseListInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseStepInfo`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this UpdateTestCaseListInfo.

        对外测试步骤

        :param steps: The steps of this UpdateTestCaseListInfo.
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseStepInfo`]
        """
        self._steps = steps

    @property
    def attachments(self):
        """Gets the attachments of this UpdateTestCaseListInfo.

        对外附件

        :return: The attachments of this UpdateTestCaseListInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseAttachmentInfo`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this UpdateTestCaseListInfo.

        对外附件

        :param attachments: The attachments of this UpdateTestCaseListInfo.
        :type attachments: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseAttachmentInfo`]
        """
        self._attachments = attachments

    @property
    def author(self):
        """Gets the author of this UpdateTestCaseListInfo.

        创建人

        :return: The author of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this UpdateTestCaseListInfo.

        创建人

        :param author: The author of this UpdateTestCaseListInfo.
        :type author: str
        """
        self._author = author

    @property
    def name(self):
        """Gets the name of this UpdateTestCaseListInfo.

        名称

        :return: The name of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTestCaseListInfo.

        名称

        :param name: The name of this UpdateTestCaseListInfo.
        :type name: str
        """
        self._name = name

    @property
    def rank(self):
        """Gets the rank of this UpdateTestCaseListInfo.

        用例等级

        :return: The rank of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this UpdateTestCaseListInfo.

        用例等级

        :param rank: The rank of this UpdateTestCaseListInfo.
        :type rank: int
        """
        self._rank = rank

    @property
    def owner(self):
        """Gets the owner of this UpdateTestCaseListInfo.

        处理人

        :return: The owner of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdateTestCaseListInfo.

        处理人

        :param owner: The owner of this UpdateTestCaseListInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def preparation(self):
        """Gets the preparation of this UpdateTestCaseListInfo.

        前置条件

        :return: The preparation of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        """Sets the preparation of this UpdateTestCaseListInfo.

        前置条件

        :param preparation: The preparation of this UpdateTestCaseListInfo.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def remark(self):
        """Gets the remark of this UpdateTestCaseListInfo.

        备注

        :return: The remark of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this UpdateTestCaseListInfo.

        备注

        :param remark: The remark of this UpdateTestCaseListInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def stage(self):
        """Gets the stage of this UpdateTestCaseListInfo.

        测试阶段

        :return: The stage of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this UpdateTestCaseListInfo.

        测试阶段

        :param stage: The stage of this UpdateTestCaseListInfo.
        :type stage: str
        """
        self._stage = stage

    @property
    def activity(self):
        """Gets the activity of this UpdateTestCaseListInfo.

        测试类型

        :return: The activity of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this UpdateTestCaseListInfo.

        测试类型

        :param activity: The activity of this UpdateTestCaseListInfo.
        :type activity: str
        """
        self._activity = activity

    @property
    def keywords(self):
        """Gets the keywords of this UpdateTestCaseListInfo.

        关键词

        :return: The keywords of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this UpdateTestCaseListInfo.

        关键词

        :param keywords: The keywords of this UpdateTestCaseListInfo.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def market(self):
        """Gets the market of this UpdateTestCaseListInfo.

        apitest标记是否代码已提交

        :return: The market of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this UpdateTestCaseListInfo.

        apitest标记是否代码已提交

        :param market: The market of this UpdateTestCaseListInfo.
        :type market: str
        """
        self._market = market

    @property
    def designer(self):
        """Gets the designer of this UpdateTestCaseListInfo.

        设计者

        :return: The designer of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._designer

    @designer.setter
    def designer(self, designer):
        """Sets the designer of this UpdateTestCaseListInfo.

        设计者

        :param designer: The designer of this UpdateTestCaseListInfo.
        :type designer: str
        """
        self._designer = designer

    @property
    def tags(self):
        """Gets the tags of this UpdateTestCaseListInfo.

        标签

        :return: The tags of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateTestCaseListInfo.

        标签

        :param tags: The tags of this UpdateTestCaseListInfo.
        :type tags: str
        """
        self._tags = tags

    @property
    def region(self):
        """Gets the region of this UpdateTestCaseListInfo.

        逻辑region，外部使用公有云实际区域，内部使用默认值

        :return: The region of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this UpdateTestCaseListInfo.

        逻辑region，外部使用公有云实际区域，内部使用默认值

        :param region: The region of this UpdateTestCaseListInfo.
        :type region: str
        """
        self._region = region

    @property
    def relate_type(self):
        """Gets the relate_type of this UpdateTestCaseListInfo.

        对外关联资源类型

        :return: The relate_type of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._relate_type

    @relate_type.setter
    def relate_type(self, relate_type):
        """Sets the relate_type of this UpdateTestCaseListInfo.

        对外关联资源类型

        :param relate_type: The relate_type of this UpdateTestCaseListInfo.
        :type relate_type: str
        """
        self._relate_type = relate_type

    @property
    def service_type(self):
        """Gets the service_type of this UpdateTestCaseListInfo.

        服务类型

        :return: The service_type of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this UpdateTestCaseListInfo.

        服务类型

        :param service_type: The service_type of this UpdateTestCaseListInfo.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def only_change_script(self):
        """Gets the only_change_script of this UpdateTestCaseListInfo.

        对外只更新接口用例的java脚本路径标识

        :return: The only_change_script of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._only_change_script

    @only_change_script.setter
    def only_change_script(self, only_change_script):
        """Sets the only_change_script of this UpdateTestCaseListInfo.

        对外只更新接口用例的java脚本路径标识

        :param only_change_script: The only_change_script of this UpdateTestCaseListInfo.
        :type only_change_script: str
        """
        self._only_change_script = only_change_script

    @property
    def add_to_iterator(self):
        """Gets the add_to_iterator of this UpdateTestCaseListInfo.

        对外需求添加到迭代标识

        :return: The add_to_iterator of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._add_to_iterator

    @add_to_iterator.setter
    def add_to_iterator(self, add_to_iterator):
        """Sets the add_to_iterator of this UpdateTestCaseListInfo.

        对外需求添加到迭代标识

        :param add_to_iterator: The add_to_iterator of this UpdateTestCaseListInfo.
        :type add_to_iterator: str
        """
        self._add_to_iterator = add_to_iterator

    @property
    def need_update_relation(self):
        """Gets the need_update_relation of this UpdateTestCaseListInfo.

        是否修改关联关系

        :return: The need_update_relation of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._need_update_relation

    @need_update_relation.setter
    def need_update_relation(self, need_update_relation):
        """Sets the need_update_relation of this UpdateTestCaseListInfo.

        是否修改关联关系

        :param need_update_relation: The need_update_relation of this UpdateTestCaseListInfo.
        :type need_update_relation: str
        """
        self._need_update_relation = need_update_relation

    @property
    def creation_version_uri(self):
        """Gets the creation_version_uri of this UpdateTestCaseListInfo.

        创建版本Uri

        :return: The creation_version_uri of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._creation_version_uri

    @creation_version_uri.setter
    def creation_version_uri(self, creation_version_uri):
        """Sets the creation_version_uri of this UpdateTestCaseListInfo.

        创建版本Uri

        :param creation_version_uri: The creation_version_uri of this UpdateTestCaseListInfo.
        :type creation_version_uri: str
        """
        self._creation_version_uri = creation_version_uri

    @property
    def number(self):
        """Gets the number of this UpdateTestCaseListInfo.

        用例编号

        :return: The number of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this UpdateTestCaseListInfo.

        用例编号

        :param number: The number of this UpdateTestCaseListInfo.
        :type number: str
        """
        self._number = number

    @property
    def case_type(self):
        """Gets the case_type of this UpdateTestCaseListInfo.

        用例类型

        :return: The case_type of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        """Sets the case_type of this UpdateTestCaseListInfo.

        用例类型

        :param case_type: The case_type of this UpdateTestCaseListInfo.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def platform_type(self):
        """Gets the platform_type of this UpdateTestCaseListInfo.

        执行平台类型

        :return: The platform_type of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this UpdateTestCaseListInfo.

        执行平台类型

        :param platform_type: The platform_type of this UpdateTestCaseListInfo.
        :type platform_type: int
        """
        self._platform_type = platform_type

    @property
    def test_type(self):
        """Gets the test_type of this UpdateTestCaseListInfo.

        测试类型

        :return: The test_type of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this UpdateTestCaseListInfo.

        测试类型

        :param test_type: The test_type of this UpdateTestCaseListInfo.
        :type test_type: int
        """
        self._test_type = test_type

    @property
    def design_note(self):
        """Gets the design_note of this UpdateTestCaseListInfo.

        设计描述

        :return: The design_note of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._design_note

    @design_note.setter
    def design_note(self, design_note):
        """Sets the design_note of this UpdateTestCaseListInfo.

        设计描述

        :param design_note: The design_note of this UpdateTestCaseListInfo.
        :type design_note: str
        """
        self._design_note = design_note

    @property
    def test_step(self):
        """Gets the test_step of this UpdateTestCaseListInfo.

        测试步骤

        :return: The test_step of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._test_step

    @test_step.setter
    def test_step(self, test_step):
        """Sets the test_step of this UpdateTestCaseListInfo.

        测试步骤

        :param test_step: The test_step of this UpdateTestCaseListInfo.
        :type test_step: str
        """
        self._test_step = test_step

    @property
    def expect_output(self):
        """Gets the expect_output of this UpdateTestCaseListInfo.

        期望结果

        :return: The expect_output of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._expect_output

    @expect_output.setter
    def expect_output(self, expect_output):
        """Sets the expect_output of this UpdateTestCaseListInfo.

        期望结果

        :param expect_output: The expect_output of this UpdateTestCaseListInfo.
        :type expect_output: str
        """
        self._expect_output = expect_output

    @property
    def env_type(self):
        """Gets the env_type of this UpdateTestCaseListInfo.

        测试环境类型

        :return: The env_type of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        """Sets the env_type of this UpdateTestCaseListInfo.

        测试环境类型

        :param env_type: The env_type of this UpdateTestCaseListInfo.
        :type env_type: str
        """
        self._env_type = env_type

    @property
    def exe_platform(self):
        """Gets the exe_platform of this UpdateTestCaseListInfo.

        执行平台

        :return: The exe_platform of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._exe_platform

    @exe_platform.setter
    def exe_platform(self, exe_platform):
        """Sets the exe_platform of this UpdateTestCaseListInfo.

        执行平台

        :param exe_platform: The exe_platform of this UpdateTestCaseListInfo.
        :type exe_platform: str
        """
        self._exe_platform = exe_platform

    @property
    def testcase_project(self):
        """Gets the testcase_project of this UpdateTestCaseListInfo.

        测试工程

        :return: The testcase_project of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._testcase_project

    @testcase_project.setter
    def testcase_project(self, testcase_project):
        """Sets the testcase_project of this UpdateTestCaseListInfo.

        测试工程

        :param testcase_project: The testcase_project of this UpdateTestCaseListInfo.
        :type testcase_project: str
        """
        self._testcase_project = testcase_project

    @property
    def svn_script_path(self):
        """Gets the svn_script_path of this UpdateTestCaseListInfo.

        脚本路径

        :return: The svn_script_path of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._svn_script_path

    @svn_script_path.setter
    def svn_script_path(self, svn_script_path):
        """Sets the svn_script_path of this UpdateTestCaseListInfo.

        脚本路径

        :param svn_script_path: The svn_script_path of this UpdateTestCaseListInfo.
        :type svn_script_path: str
        """
        self._svn_script_path = svn_script_path

    @property
    def map_restrict(self):
        """Gets the map_restrict of this UpdateTestCaseListInfo.

        约束条件

        :return: The map_restrict of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._map_restrict

    @map_restrict.setter
    def map_restrict(self, map_restrict):
        """Sets the map_restrict of this UpdateTestCaseListInfo.

        约束条件

        :param map_restrict: The map_restrict of this UpdateTestCaseListInfo.
        :type map_restrict: str
        """
        self._map_restrict = map_restrict

    @property
    def network_script_name(self):
        """Gets the network_script_name of this UpdateTestCaseListInfo.

        网络脚本名

        :return: The network_script_name of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._network_script_name

    @network_script_name.setter
    def network_script_name(self, network_script_name):
        """Sets the network_script_name of this UpdateTestCaseListInfo.

        网络脚本名

        :param network_script_name: The network_script_name of this UpdateTestCaseListInfo.
        :type network_script_name: str
        """
        self._network_script_name = network_script_name

    @property
    def auto_type(self):
        """Gets the auto_type of this UpdateTestCaseListInfo.

        自动化类型，非自动化:0, 是自动化:1

        :return: The auto_type of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._auto_type

    @auto_type.setter
    def auto_type(self, auto_type):
        """Sets the auto_type of this UpdateTestCaseListInfo.

        自动化类型，非自动化:0, 是自动化:1

        :param auto_type: The auto_type of this UpdateTestCaseListInfo.
        :type auto_type: int
        """
        self._auto_type = auto_type

    @property
    def to_be_auto_exec(self):
        """Gets the to_be_auto_exec of this UpdateTestCaseListInfo.

        被自动化执行

        :return: The to_be_auto_exec of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._to_be_auto_exec

    @to_be_auto_exec.setter
    def to_be_auto_exec(self, to_be_auto_exec):
        """Sets the to_be_auto_exec of this UpdateTestCaseListInfo.

        被自动化执行

        :param to_be_auto_exec: The to_be_auto_exec of this UpdateTestCaseListInfo.
        :type to_be_auto_exec: int
        """
        self._to_be_auto_exec = to_be_auto_exec

    @property
    def last_result(self):
        """Gets the last_result of this UpdateTestCaseListInfo.

        最后一次结果

        :return: The last_result of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._last_result

    @last_result.setter
    def last_result(self, last_result):
        """Sets the last_result of this UpdateTestCaseListInfo.

        最后一次结果

        :param last_result: The last_result of this UpdateTestCaseListInfo.
        :type last_result: str
        """
        self._last_result = last_result

    @property
    def last_result_uri(self):
        """Gets the last_result_uri of this UpdateTestCaseListInfo.

        最后一次结果Uri

        :return: The last_result_uri of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._last_result_uri

    @last_result_uri.setter
    def last_result_uri(self, last_result_uri):
        """Sets the last_result_uri of this UpdateTestCaseListInfo.

        最后一次结果Uri

        :param last_result_uri: The last_result_uri of this UpdateTestCaseListInfo.
        :type last_result_uri: str
        """
        self._last_result_uri = last_result_uri

    @property
    def feature_uri(self):
        """Gets the feature_uri of this UpdateTestCaseListInfo.

        目录Uri

        :return: The feature_uri of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        """Sets the feature_uri of this UpdateTestCaseListInfo.

        目录Uri

        :param feature_uri: The feature_uri of this UpdateTestCaseListInfo.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

    @property
    def interface_name(self):
        """Gets the interface_name of this UpdateTestCaseListInfo.

        测试接口名

        :return: The interface_name of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this UpdateTestCaseListInfo.

        测试接口名

        :param interface_name: The interface_name of this UpdateTestCaseListInfo.
        :type interface_name: str
        """
        self._interface_name = interface_name

    @property
    def snp_no(self):
        """Gets the snp_no of this UpdateTestCaseListInfo.

        网络问题ID

        :return: The snp_no of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._snp_no

    @snp_no.setter
    def snp_no(self, snp_no):
        """Sets the snp_no of this UpdateTestCaseListInfo.

        网络问题ID

        :param snp_no: The snp_no of this UpdateTestCaseListInfo.
        :type snp_no: str
        """
        self._snp_no = snp_no

    @property
    def dr_relation_id(self):
        """Gets the dr_relation_id of this UpdateTestCaseListInfo.

        关联需求编号

        :return: The dr_relation_id of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._dr_relation_id

    @dr_relation_id.setter
    def dr_relation_id(self, dr_relation_id):
        """Sets the dr_relation_id of this UpdateTestCaseListInfo.

        关联需求编号

        :param dr_relation_id: The dr_relation_id of this UpdateTestCaseListInfo.
        :type dr_relation_id: str
        """
        self._dr_relation_id = dr_relation_id

    @property
    def test_base_num(self):
        """Gets the test_base_num of this UpdateTestCaseListInfo.

        测试基数

        :return: The test_base_num of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._test_base_num

    @test_base_num.setter
    def test_base_num(self, test_base_num):
        """Sets the test_base_num of this UpdateTestCaseListInfo.

        测试基数

        :param test_base_num: The test_base_num of this UpdateTestCaseListInfo.
        :type test_base_num: str
        """
        self._test_base_num = test_base_num

    @property
    def automatically_executed(self):
        """Gets the automatically_executed of this UpdateTestCaseListInfo.

        是否被自动化执行

        :return: The automatically_executed of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._automatically_executed

    @automatically_executed.setter
    def automatically_executed(self, automatically_executed):
        """Sets the automatically_executed of this UpdateTestCaseListInfo.

        是否被自动化执行

        :param automatically_executed: The automatically_executed of this UpdateTestCaseListInfo.
        :type automatically_executed: int
        """
        self._automatically_executed = automatically_executed

    @property
    def first_execute_time(self):
        """Gets the first_execute_time of this UpdateTestCaseListInfo.

        第一次执行时间

        :return: The first_execute_time of this UpdateTestCaseListInfo.
        :rtype: datetime
        """
        return self._first_execute_time

    @first_execute_time.setter
    def first_execute_time(self, first_execute_time):
        """Sets the first_execute_time of this UpdateTestCaseListInfo.

        第一次执行时间

        :param first_execute_time: The first_execute_time of this UpdateTestCaseListInfo.
        :type first_execute_time: datetime
        """
        self._first_execute_time = first_execute_time

    @property
    def detect_type(self):
        """Gets the detect_type of this UpdateTestCaseListInfo.

        检测类型

        :return: The detect_type of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        """Sets the detect_type of this UpdateTestCaseListInfo.

        检测类型

        :param detect_type: The detect_type of this UpdateTestCaseListInfo.
        :type detect_type: str
        """
        self._detect_type = detect_type

    @property
    def execute_param(self):
        """Gets the execute_param of this UpdateTestCaseListInfo.

        执行参数

        :return: The execute_param of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._execute_param

    @execute_param.setter
    def execute_param(self, execute_param):
        """Sets the execute_param of this UpdateTestCaseListInfo.

        执行参数

        :param execute_param: The execute_param of this UpdateTestCaseListInfo.
        :type execute_param: str
        """
        self._execute_param = execute_param

    @property
    def test_feature(self):
        """Gets the test_feature of this UpdateTestCaseListInfo.

        分析领域

        :return: The test_feature of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._test_feature

    @test_feature.setter
    def test_feature(self, test_feature):
        """Sets the test_feature of this UpdateTestCaseListInfo.

        分析领域

        :param test_feature: The test_feature of this UpdateTestCaseListInfo.
        :type test_feature: str
        """
        self._test_feature = test_feature

    @property
    def is_contract_testcase(self):
        """Gets the is_contract_testcase of this UpdateTestCaseListInfo.

        是否是契约用例，0:表示非契约用例, 1：表示契约用例

        :return: The is_contract_testcase of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._is_contract_testcase

    @is_contract_testcase.setter
    def is_contract_testcase(self, is_contract_testcase):
        """Sets the is_contract_testcase of this UpdateTestCaseListInfo.

        是否是契约用例，0:表示非契约用例, 1：表示契约用例

        :param is_contract_testcase: The is_contract_testcase of this UpdateTestCaseListInfo.
        :type is_contract_testcase: int
        """
        self._is_contract_testcase = is_contract_testcase

    @property
    def time_cost(self):
        """Gets the time_cost of this UpdateTestCaseListInfo.

        总共耗时

        :return: The time_cost of this UpdateTestCaseListInfo.
        :rtype: float
        """
        return self._time_cost

    @time_cost.setter
    def time_cost(self, time_cost):
        """Sets the time_cost of this UpdateTestCaseListInfo.

        总共耗时

        :param time_cost: The time_cost of this UpdateTestCaseListInfo.
        :type time_cost: float
        """
        self._time_cost = time_cost

    @property
    def custom_field_1(self):
        """Gets the custom_field_1 of this UpdateTestCaseListInfo.

        自定义字段1

        :return: The custom_field_1 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_1

    @custom_field_1.setter
    def custom_field_1(self, custom_field_1):
        """Sets the custom_field_1 of this UpdateTestCaseListInfo.

        自定义字段1

        :param custom_field_1: The custom_field_1 of this UpdateTestCaseListInfo.
        :type custom_field_1: str
        """
        self._custom_field_1 = custom_field_1

    @property
    def custom_field_2(self):
        """Gets the custom_field_2 of this UpdateTestCaseListInfo.

        自定义字段2

        :return: The custom_field_2 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_2

    @custom_field_2.setter
    def custom_field_2(self, custom_field_2):
        """Sets the custom_field_2 of this UpdateTestCaseListInfo.

        自定义字段2

        :param custom_field_2: The custom_field_2 of this UpdateTestCaseListInfo.
        :type custom_field_2: str
        """
        self._custom_field_2 = custom_field_2

    @property
    def custom_field_3(self):
        """Gets the custom_field_3 of this UpdateTestCaseListInfo.

        自定义字段3

        :return: The custom_field_3 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_3

    @custom_field_3.setter
    def custom_field_3(self, custom_field_3):
        """Sets the custom_field_3 of this UpdateTestCaseListInfo.

        自定义字段3

        :param custom_field_3: The custom_field_3 of this UpdateTestCaseListInfo.
        :type custom_field_3: str
        """
        self._custom_field_3 = custom_field_3

    @property
    def custom_field_4(self):
        """Gets the custom_field_4 of this UpdateTestCaseListInfo.

        自定义字段4

        :return: The custom_field_4 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_4

    @custom_field_4.setter
    def custom_field_4(self, custom_field_4):
        """Sets the custom_field_4 of this UpdateTestCaseListInfo.

        自定义字段4

        :param custom_field_4: The custom_field_4 of this UpdateTestCaseListInfo.
        :type custom_field_4: str
        """
        self._custom_field_4 = custom_field_4

    @property
    def custom_field_5(self):
        """Gets the custom_field_5 of this UpdateTestCaseListInfo.

        自定义字段5

        :return: The custom_field_5 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_5

    @custom_field_5.setter
    def custom_field_5(self, custom_field_5):
        """Sets the custom_field_5 of this UpdateTestCaseListInfo.

        自定义字段5

        :param custom_field_5: The custom_field_5 of this UpdateTestCaseListInfo.
        :type custom_field_5: str
        """
        self._custom_field_5 = custom_field_5

    @property
    def custom_field_6(self):
        """Gets the custom_field_6 of this UpdateTestCaseListInfo.

        自定义字段6

        :return: The custom_field_6 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_6

    @custom_field_6.setter
    def custom_field_6(self, custom_field_6):
        """Sets the custom_field_6 of this UpdateTestCaseListInfo.

        自定义字段6

        :param custom_field_6: The custom_field_6 of this UpdateTestCaseListInfo.
        :type custom_field_6: str
        """
        self._custom_field_6 = custom_field_6

    @property
    def custom_field_7(self):
        """Gets the custom_field_7 of this UpdateTestCaseListInfo.

        自定义字段7

        :return: The custom_field_7 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_7

    @custom_field_7.setter
    def custom_field_7(self, custom_field_7):
        """Sets the custom_field_7 of this UpdateTestCaseListInfo.

        自定义字段7

        :param custom_field_7: The custom_field_7 of this UpdateTestCaseListInfo.
        :type custom_field_7: str
        """
        self._custom_field_7 = custom_field_7

    @property
    def custom_field_8(self):
        """Gets the custom_field_8 of this UpdateTestCaseListInfo.

        自定义字段8

        :return: The custom_field_8 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_8

    @custom_field_8.setter
    def custom_field_8(self, custom_field_8):
        """Sets the custom_field_8 of this UpdateTestCaseListInfo.

        自定义字段8

        :param custom_field_8: The custom_field_8 of this UpdateTestCaseListInfo.
        :type custom_field_8: str
        """
        self._custom_field_8 = custom_field_8

    @property
    def custom_field_9(self):
        """Gets the custom_field_9 of this UpdateTestCaseListInfo.

        自定义字段9

        :return: The custom_field_9 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_9

    @custom_field_9.setter
    def custom_field_9(self, custom_field_9):
        """Sets the custom_field_9 of this UpdateTestCaseListInfo.

        自定义字段9

        :param custom_field_9: The custom_field_9 of this UpdateTestCaseListInfo.
        :type custom_field_9: str
        """
        self._custom_field_9 = custom_field_9

    @property
    def custom_field_10(self):
        """Gets the custom_field_10 of this UpdateTestCaseListInfo.

        自定义字段10

        :return: The custom_field_10 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_10

    @custom_field_10.setter
    def custom_field_10(self, custom_field_10):
        """Sets the custom_field_10 of this UpdateTestCaseListInfo.

        自定义字段10

        :param custom_field_10: The custom_field_10 of this UpdateTestCaseListInfo.
        :type custom_field_10: str
        """
        self._custom_field_10 = custom_field_10

    @property
    def custom_field_11(self):
        """Gets the custom_field_11 of this UpdateTestCaseListInfo.

        自定义字段11

        :return: The custom_field_11 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_11

    @custom_field_11.setter
    def custom_field_11(self, custom_field_11):
        """Sets the custom_field_11 of this UpdateTestCaseListInfo.

        自定义字段11

        :param custom_field_11: The custom_field_11 of this UpdateTestCaseListInfo.
        :type custom_field_11: str
        """
        self._custom_field_11 = custom_field_11

    @property
    def custom_field_12(self):
        """Gets the custom_field_12 of this UpdateTestCaseListInfo.

        自定义字段12

        :return: The custom_field_12 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_12

    @custom_field_12.setter
    def custom_field_12(self, custom_field_12):
        """Sets the custom_field_12 of this UpdateTestCaseListInfo.

        自定义字段12

        :param custom_field_12: The custom_field_12 of this UpdateTestCaseListInfo.
        :type custom_field_12: str
        """
        self._custom_field_12 = custom_field_12

    @property
    def custom_field_13(self):
        """Gets the custom_field_13 of this UpdateTestCaseListInfo.

        自定义字段13

        :return: The custom_field_13 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_13

    @custom_field_13.setter
    def custom_field_13(self, custom_field_13):
        """Sets the custom_field_13 of this UpdateTestCaseListInfo.

        自定义字段13

        :param custom_field_13: The custom_field_13 of this UpdateTestCaseListInfo.
        :type custom_field_13: str
        """
        self._custom_field_13 = custom_field_13

    @property
    def custom_field_14(self):
        """Gets the custom_field_14 of this UpdateTestCaseListInfo.

        自定义字段14

        :return: The custom_field_14 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_14

    @custom_field_14.setter
    def custom_field_14(self, custom_field_14):
        """Sets the custom_field_14 of this UpdateTestCaseListInfo.

        自定义字段14

        :param custom_field_14: The custom_field_14 of this UpdateTestCaseListInfo.
        :type custom_field_14: str
        """
        self._custom_field_14 = custom_field_14

    @property
    def custom_field_15(self):
        """Gets the custom_field_15 of this UpdateTestCaseListInfo.

        自定义字段15

        :return: The custom_field_15 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_15

    @custom_field_15.setter
    def custom_field_15(self, custom_field_15):
        """Sets the custom_field_15 of this UpdateTestCaseListInfo.

        自定义字段15

        :param custom_field_15: The custom_field_15 of this UpdateTestCaseListInfo.
        :type custom_field_15: str
        """
        self._custom_field_15 = custom_field_15

    @property
    def custom_field_16(self):
        """Gets the custom_field_16 of this UpdateTestCaseListInfo.

        自定义字段16

        :return: The custom_field_16 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_16

    @custom_field_16.setter
    def custom_field_16(self, custom_field_16):
        """Sets the custom_field_16 of this UpdateTestCaseListInfo.

        自定义字段16

        :param custom_field_16: The custom_field_16 of this UpdateTestCaseListInfo.
        :type custom_field_16: str
        """
        self._custom_field_16 = custom_field_16

    @property
    def custom_field_17(self):
        """Gets the custom_field_17 of this UpdateTestCaseListInfo.

        自定义字段17

        :return: The custom_field_17 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_17

    @custom_field_17.setter
    def custom_field_17(self, custom_field_17):
        """Sets the custom_field_17 of this UpdateTestCaseListInfo.

        自定义字段17

        :param custom_field_17: The custom_field_17 of this UpdateTestCaseListInfo.
        :type custom_field_17: str
        """
        self._custom_field_17 = custom_field_17

    @property
    def custom_field_18(self):
        """Gets the custom_field_18 of this UpdateTestCaseListInfo.

        自定义字段18

        :return: The custom_field_18 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_18

    @custom_field_18.setter
    def custom_field_18(self, custom_field_18):
        """Sets the custom_field_18 of this UpdateTestCaseListInfo.

        自定义字段18

        :param custom_field_18: The custom_field_18 of this UpdateTestCaseListInfo.
        :type custom_field_18: str
        """
        self._custom_field_18 = custom_field_18

    @property
    def custom_field_19(self):
        """Gets the custom_field_19 of this UpdateTestCaseListInfo.

        自定义字段19

        :return: The custom_field_19 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_19

    @custom_field_19.setter
    def custom_field_19(self, custom_field_19):
        """Sets the custom_field_19 of this UpdateTestCaseListInfo.

        自定义字段19

        :param custom_field_19: The custom_field_19 of this UpdateTestCaseListInfo.
        :type custom_field_19: str
        """
        self._custom_field_19 = custom_field_19

    @property
    def custom_field_20(self):
        """Gets the custom_field_20 of this UpdateTestCaseListInfo.

        自定义字段20

        :return: The custom_field_20 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_20

    @custom_field_20.setter
    def custom_field_20(self, custom_field_20):
        """Sets the custom_field_20 of this UpdateTestCaseListInfo.

        自定义字段20

        :param custom_field_20: The custom_field_20 of this UpdateTestCaseListInfo.
        :type custom_field_20: str
        """
        self._custom_field_20 = custom_field_20

    @property
    def custom_field_21(self):
        """Gets the custom_field_21 of this UpdateTestCaseListInfo.

        自定义字段21

        :return: The custom_field_21 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_21

    @custom_field_21.setter
    def custom_field_21(self, custom_field_21):
        """Sets the custom_field_21 of this UpdateTestCaseListInfo.

        自定义字段21

        :param custom_field_21: The custom_field_21 of this UpdateTestCaseListInfo.
        :type custom_field_21: str
        """
        self._custom_field_21 = custom_field_21

    @property
    def custom_field_22(self):
        """Gets the custom_field_22 of this UpdateTestCaseListInfo.

        自定义字段22

        :return: The custom_field_22 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_22

    @custom_field_22.setter
    def custom_field_22(self, custom_field_22):
        """Sets the custom_field_22 of this UpdateTestCaseListInfo.

        自定义字段22

        :param custom_field_22: The custom_field_22 of this UpdateTestCaseListInfo.
        :type custom_field_22: str
        """
        self._custom_field_22 = custom_field_22

    @property
    def custom_field_23(self):
        """Gets the custom_field_23 of this UpdateTestCaseListInfo.

        自定义字段23

        :return: The custom_field_23 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_23

    @custom_field_23.setter
    def custom_field_23(self, custom_field_23):
        """Sets the custom_field_23 of this UpdateTestCaseListInfo.

        自定义字段23

        :param custom_field_23: The custom_field_23 of this UpdateTestCaseListInfo.
        :type custom_field_23: str
        """
        self._custom_field_23 = custom_field_23

    @property
    def custom_field_24(self):
        """Gets the custom_field_24 of this UpdateTestCaseListInfo.

        自定义字段24

        :return: The custom_field_24 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_24

    @custom_field_24.setter
    def custom_field_24(self, custom_field_24):
        """Sets the custom_field_24 of this UpdateTestCaseListInfo.

        自定义字段24

        :param custom_field_24: The custom_field_24 of this UpdateTestCaseListInfo.
        :type custom_field_24: str
        """
        self._custom_field_24 = custom_field_24

    @property
    def custom_field_25(self):
        """Gets the custom_field_25 of this UpdateTestCaseListInfo.

        自定义字段25

        :return: The custom_field_25 of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._custom_field_25

    @custom_field_25.setter
    def custom_field_25(self, custom_field_25):
        """Sets the custom_field_25 of this UpdateTestCaseListInfo.

        自定义字段25

        :param custom_field_25: The custom_field_25 of this UpdateTestCaseListInfo.
        :type custom_field_25: str
        """
        self._custom_field_25 = custom_field_25

    @property
    def be_auto_type_time(self):
        """Gets the be_auto_type_time of this UpdateTestCaseListInfo.

        记录用例由非自动化变为自动化类型的时间

        :return: The be_auto_type_time of this UpdateTestCaseListInfo.
        :rtype: datetime
        """
        return self._be_auto_type_time

    @be_auto_type_time.setter
    def be_auto_type_time(self, be_auto_type_time):
        """Sets the be_auto_type_time of this UpdateTestCaseListInfo.

        记录用例由非自动化变为自动化类型的时间

        :param be_auto_type_time: The be_auto_type_time of this UpdateTestCaseListInfo.
        :type be_auto_type_time: datetime
        """
        self._be_auto_type_time = be_auto_type_time

    @property
    def compare_number(self):
        """Gets the compare_number of this UpdateTestCaseListInfo.

        配对用例编号

        :return: The compare_number of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._compare_number

    @compare_number.setter
    def compare_number(self, compare_number):
        """Sets the compare_number of this UpdateTestCaseListInfo.

        配对用例编号

        :param compare_number: The compare_number of this UpdateTestCaseListInfo.
        :type compare_number: str
        """
        self._compare_number = compare_number

    @property
    def scene_flag(self):
        """Gets the scene_flag of this UpdateTestCaseListInfo.

        场景标识

        :return: The scene_flag of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._scene_flag

    @scene_flag.setter
    def scene_flag(self, scene_flag):
        """Sets the scene_flag of this UpdateTestCaseListInfo.

        场景标识

        :param scene_flag: The scene_flag of this UpdateTestCaseListInfo.
        :type scene_flag: str
        """
        self._scene_flag = scene_flag

    @property
    def base_flag(self):
        """Gets the base_flag of this UpdateTestCaseListInfo.

        场景标识

        :return: The base_flag of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._base_flag

    @base_flag.setter
    def base_flag(self, base_flag):
        """Sets the base_flag of this UpdateTestCaseListInfo.

        场景标识

        :param base_flag: The base_flag of this UpdateTestCaseListInfo.
        :type base_flag: str
        """
        self._base_flag = base_flag

    @property
    def para_validator(self):
        """Gets the para_validator of this UpdateTestCaseListInfo.

        区别是否从yaml中生成的用例，默认false

        :return: The para_validator of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._para_validator

    @para_validator.setter
    def para_validator(self, para_validator):
        """Sets the para_validator of this UpdateTestCaseListInfo.

        区别是否从yaml中生成的用例，默认false

        :param para_validator: The para_validator of this UpdateTestCaseListInfo.
        :type para_validator: str
        """
        self._para_validator = para_validator

    @property
    def knet_node_id(self):
        """Gets the knet_node_id of this UpdateTestCaseListInfo.

        knet节点id

        :return: The knet_node_id of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._knet_node_id

    @knet_node_id.setter
    def knet_node_id(self, knet_node_id):
        """Sets the knet_node_id of this UpdateTestCaseListInfo.

        knet节点id

        :param knet_node_id: The knet_node_id of this UpdateTestCaseListInfo.
        :type knet_node_id: str
        """
        self._knet_node_id = knet_node_id

    @property
    def last_exe_author(self):
        """Gets the last_exe_author of this UpdateTestCaseListInfo.

        最后一次执行用户

        :return: The last_exe_author of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._last_exe_author

    @last_exe_author.setter
    def last_exe_author(self, last_exe_author):
        """Sets the last_exe_author of this UpdateTestCaseListInfo.

        最后一次执行用户

        :param last_exe_author: The last_exe_author of this UpdateTestCaseListInfo.
        :type last_exe_author: str
        """
        self._last_exe_author = last_exe_author

    @property
    def cloud_carrier(self):
        """Gets the cloud_carrier of this UpdateTestCaseListInfo.

        运营商

        :return: The cloud_carrier of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._cloud_carrier

    @cloud_carrier.setter
    def cloud_carrier(self, cloud_carrier):
        """Sets the cloud_carrier of this UpdateTestCaseListInfo.

        运营商

        :param cloud_carrier: The cloud_carrier of this UpdateTestCaseListInfo.
        :type cloud_carrier: str
        """
        self._cloud_carrier = cloud_carrier

    @property
    def market_place(self):
        """Gets the market_place of this UpdateTestCaseListInfo.

        应用市场

        :return: The market_place of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._market_place

    @market_place.setter
    def market_place(self, market_place):
        """Sets the market_place of this UpdateTestCaseListInfo.

        应用市场

        :param market_place: The market_place of this UpdateTestCaseListInfo.
        :type market_place: str
        """
        self._market_place = market_place

    @property
    def test_mind_id(self):
        """Gets the test_mind_id of this UpdateTestCaseListInfo.

        脑图id

        :return: The test_mind_id of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._test_mind_id

    @test_mind_id.setter
    def test_mind_id(self, test_mind_id):
        """Sets the test_mind_id of this UpdateTestCaseListInfo.

        脑图id

        :param test_mind_id: The test_mind_id of this UpdateTestCaseListInfo.
        :type test_mind_id: str
        """
        self._test_mind_id = test_mind_id

    @property
    def test_mind_url(self):
        """Gets the test_mind_url of this UpdateTestCaseListInfo.

        脑图url

        :return: The test_mind_url of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._test_mind_url

    @test_mind_url.setter
    def test_mind_url(self, test_mind_url):
        """Sets the test_mind_url of this UpdateTestCaseListInfo.

        脑图url

        :param test_mind_url: The test_mind_url of this UpdateTestCaseListInfo.
        :type test_mind_url: str
        """
        self._test_mind_url = test_mind_url

    @property
    def commit_url(self):
        """Gets the commit_url of this UpdateTestCaseListInfo.

        git提交url

        :return: The commit_url of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._commit_url

    @commit_url.setter
    def commit_url(self, commit_url):
        """Sets the commit_url of this UpdateTestCaseListInfo.

        git提交url

        :param commit_url: The commit_url of this UpdateTestCaseListInfo.
        :type commit_url: str
        """
        self._commit_url = commit_url

    @property
    def test_pattern_number(self):
        """Gets the test_pattern_number of this UpdateTestCaseListInfo.

        测试模式编号

        :return: The test_pattern_number of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._test_pattern_number

    @test_pattern_number.setter
    def test_pattern_number(self, test_pattern_number):
        """Sets the test_pattern_number of this UpdateTestCaseListInfo.

        测试模式编号

        :param test_pattern_number: The test_pattern_number of this UpdateTestCaseListInfo.
        :type test_pattern_number: str
        """
        self._test_pattern_number = test_pattern_number

    @property
    def test_factor_number(self):
        """Gets the test_factor_number of this UpdateTestCaseListInfo.

        测试因子编号

        :return: The test_factor_number of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._test_factor_number

    @test_factor_number.setter
    def test_factor_number(self, test_factor_number):
        """Sets the test_factor_number of this UpdateTestCaseListInfo.

        测试因子编号

        :param test_factor_number: The test_factor_number of this UpdateTestCaseListInfo.
        :type test_factor_number: str
        """
        self._test_factor_number = test_factor_number

    @property
    def status_code(self):
        """Gets the status_code of this UpdateTestCaseListInfo.

        状态Code

        :return: The status_code of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this UpdateTestCaseListInfo.

        状态Code

        :param status_code: The status_code of this UpdateTestCaseListInfo.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def result_code(self):
        """Gets the result_code of this UpdateTestCaseListInfo.

        结果Code

        :return: The result_code of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this UpdateTestCaseListInfo.

        结果Code

        :param result_code: The result_code of this UpdateTestCaseListInfo.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def release_id(self):
        """Gets the release_id of this UpdateTestCaseListInfo.

        迭代ID

        :return: The release_id of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this UpdateTestCaseListInfo.

        迭代ID

        :param release_id: The release_id of this UpdateTestCaseListInfo.
        :type release_id: str
        """
        self._release_id = release_id

    @property
    def label_id(self):
        """Gets the label_id of this UpdateTestCaseListInfo.

        标签ID

        :return: The label_id of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this UpdateTestCaseListInfo.

        标签ID

        :param label_id: The label_id of this UpdateTestCaseListInfo.
        :type label_id: str
        """
        self._label_id = label_id

    @property
    def label_names(self):
        """Gets the label_names of this UpdateTestCaseListInfo.

        对外用例操作时，标签名列表

        :return: The label_names of this UpdateTestCaseListInfo.
        :rtype: list[str]
        """
        return self._label_names

    @label_names.setter
    def label_names(self, label_names):
        """Sets the label_names of this UpdateTestCaseListInfo.

        对外用例操作时，标签名列表

        :param label_names: The label_names of this UpdateTestCaseListInfo.
        :type label_names: list[str]
        """
        self._label_names = label_names

    @property
    def module_id(self):
        """Gets the module_id of this UpdateTestCaseListInfo.

        模块ID

        :return: The module_id of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this UpdateTestCaseListInfo.

        模块ID

        :param module_id: The module_id of this UpdateTestCaseListInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def execute_latest_time(self):
        """Gets the execute_latest_time of this UpdateTestCaseListInfo.

        最后执行时间

        :return: The execute_latest_time of this UpdateTestCaseListInfo.
        :rtype: datetime
        """
        return self._execute_latest_time

    @execute_latest_time.setter
    def execute_latest_time(self, execute_latest_time):
        """Sets the execute_latest_time of this UpdateTestCaseListInfo.

        最后执行时间

        :param execute_latest_time: The execute_latest_time of this UpdateTestCaseListInfo.
        :type execute_latest_time: datetime
        """
        self._execute_latest_time = execute_latest_time

    @property
    def execute_duration(self):
        """Gets the execute_duration of this UpdateTestCaseListInfo.

        执行时长

        :return: The execute_duration of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._execute_duration

    @execute_duration.setter
    def execute_duration(self, execute_duration):
        """Sets the execute_duration of this UpdateTestCaseListInfo.

        执行时长

        :param execute_duration: The execute_duration of this UpdateTestCaseListInfo.
        :type execute_duration: str
        """
        self._execute_duration = execute_duration

    @property
    def is_keyword(self):
        """Gets the is_keyword of this UpdateTestCaseListInfo.

        是否关键用例

        :return: The is_keyword of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._is_keyword

    @is_keyword.setter
    def is_keyword(self, is_keyword):
        """Sets the is_keyword of this UpdateTestCaseListInfo.

        是否关键用例

        :param is_keyword: The is_keyword of this UpdateTestCaseListInfo.
        :type is_keyword: int
        """
        self._is_keyword = is_keyword

    @property
    def release_dev(self):
        """Gets the release_dev of this UpdateTestCaseListInfo.

        测试版本号

        :return: The release_dev of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        """Sets the release_dev of this UpdateTestCaseListInfo.

        测试版本号

        :param release_dev: The release_dev of this UpdateTestCaseListInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def new_created(self):
        """Gets the new_created of this UpdateTestCaseListInfo.

        是否用户新增用例

        :return: The new_created of this UpdateTestCaseListInfo.
        :rtype: int
        """
        return self._new_created

    @new_created.setter
    def new_created(self, new_created):
        """Sets the new_created of this UpdateTestCaseListInfo.

        是否用户新增用例

        :param new_created: The new_created of this UpdateTestCaseListInfo.
        :type new_created: int
        """
        self._new_created = new_created

    @property
    def execute_parameter(self):
        """Gets the execute_parameter of this UpdateTestCaseListInfo.

        执行参数

        :return: The execute_parameter of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._execute_parameter

    @execute_parameter.setter
    def execute_parameter(self, execute_parameter):
        """Sets the execute_parameter of this UpdateTestCaseListInfo.

        执行参数

        :param execute_parameter: The execute_parameter of this UpdateTestCaseListInfo.
        :type execute_parameter: str
        """
        self._execute_parameter = execute_parameter

    @property
    def project_uuid(self):
        """Gets the project_uuid of this UpdateTestCaseListInfo.

        项目ID，外部使用项目ID，内部使用默认值

        :return: The project_uuid of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this UpdateTestCaseListInfo.

        项目ID，外部使用项目ID，内部使用默认值

        :param project_uuid: The project_uuid of this UpdateTestCaseListInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def version_uri(self):
        """Gets the version_uri of this UpdateTestCaseListInfo.

        分支或者迭代uri

        :return: The version_uri of this UpdateTestCaseListInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this UpdateTestCaseListInfo.

        分支或者迭代uri

        :param version_uri: The version_uri of this UpdateTestCaseListInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def case_list(self):
        """Gets the case_list of this UpdateTestCaseListInfo.

        更新用例信息列表

        :return: The case_list of this UpdateTestCaseListInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CaseInfo`]
        """
        return self._case_list

    @case_list.setter
    def case_list(self, case_list):
        """Sets the case_list of this UpdateTestCaseListInfo.

        更新用例信息列表

        :param case_list: The case_list of this UpdateTestCaseListInfo.
        :type case_list: list[:class:`huaweicloudsdkcloudtest.v1.CaseInfo`]
        """
        self._case_list = case_list

    @property
    def case_id_list(self):
        """Gets the case_id_list of this UpdateTestCaseListInfo.

        批量更新用例id列表

        :return: The case_id_list of this UpdateTestCaseListInfo.
        :rtype: list[str]
        """
        return self._case_id_list

    @case_id_list.setter
    def case_id_list(self, case_id_list):
        """Sets the case_id_list of this UpdateTestCaseListInfo.

        批量更新用例id列表

        :param case_id_list: The case_id_list of this UpdateTestCaseListInfo.
        :type case_id_list: list[str]
        """
        self._case_id_list = case_id_list

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
        if not isinstance(other, UpdateTestCaseListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
