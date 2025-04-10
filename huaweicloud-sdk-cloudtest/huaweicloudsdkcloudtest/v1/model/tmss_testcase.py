# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmssTestcase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'activity_id': 'str',
        'applied_product': 'str',
        'author': 'str',
        'auto_type': 'str',
        'cata_id': 'str',
        'creation_date': 'str',
        'custom_field_1': 'str',
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
        'custom_field_2': 'str',
        'custom_field_20': 'str',
        'custom_field_21': 'str',
        'custom_field_22': 'str',
        'custom_field_23': 'str',
        'custom_field_24': 'str',
        'custom_field_25': 'str',
        'custom_field_3': 'str',
        'custom_field_4': 'str',
        'custom_field_5': 'str',
        'custom_field_6': 'str',
        'custom_field_7': 'str',
        'custom_field_8': 'str',
        'custom_field_9': 'str',
        'description': 'str',
        'dr_relationid': 'str',
        'env_type': 'str',
        'exe_platform': 'str',
        'expect_output': 'str',
        'feature_path': 'str',
        'is_key_word': 'int',
        'is_contract_testcase': 'str',
        'is_para_validator_testcase': 'str',
        'label_id': 'list[str]',
        'last_modified': 'str',
        'last_modifier': 'str',
        'last_result': 'str',
        'level': 'int',
        'market': 'str',
        'module_id': 'str',
        'name': 'str',
        'network_script_name': 'str',
        'node_name': 'str',
        'number': 'str',
        'origin_uri': 'str',
        'owner': 'str',
        'owner_id': 'str',
        'preparation': 'str',
        'release_dev': 'str',
        'release_id': 'str',
        'remark': 'str',
        'stage': 'str',
        'steps': 'list[TmssStep]',
        'svn_script_path': 'str',
        'tags': 'str',
        'test_feature': 'str',
        'test_step': 'str',
        'test_type': 'int',
        'uri': 'str'
    }

    attribute_map = {
        'activity_id': 'activity_id',
        'applied_product': 'applied_product',
        'author': 'author',
        'auto_type': 'auto_type',
        'cata_id': 'cataId',
        'creation_date': 'creation_date',
        'custom_field_1': 'custom_field_1',
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
        'custom_field_2': 'custom_field_2',
        'custom_field_20': 'custom_field_20',
        'custom_field_21': 'custom_field_21',
        'custom_field_22': 'custom_field_22',
        'custom_field_23': 'custom_field_23',
        'custom_field_24': 'custom_field_24',
        'custom_field_25': 'custom_field_25',
        'custom_field_3': 'custom_field_3',
        'custom_field_4': 'custom_field_4',
        'custom_field_5': 'custom_field_5',
        'custom_field_6': 'custom_field_6',
        'custom_field_7': 'custom_field_7',
        'custom_field_8': 'custom_field_8',
        'custom_field_9': 'custom_field_9',
        'description': 'description',
        'dr_relationid': 'dr_relationid',
        'env_type': 'env_type',
        'exe_platform': 'exe_platform',
        'expect_output': 'expect_output',
        'feature_path': 'feature_path',
        'is_key_word': 'isKeyWord',
        'is_contract_testcase': 'is_contract_testcase',
        'is_para_validator_testcase': 'is_paraValidator_testcase',
        'label_id': 'labelId',
        'last_modified': 'last_modified',
        'last_modifier': 'last_modifier',
        'last_result': 'last_result',
        'level': 'level',
        'market': 'market',
        'module_id': 'moduleId',
        'name': 'name',
        'network_script_name': 'networkScriptName',
        'node_name': 'node_name',
        'number': 'number',
        'origin_uri': 'originUri',
        'owner': 'owner',
        'owner_id': 'ownerId',
        'preparation': 'preparation',
        'release_dev': 'releaseDev',
        'release_id': 'releaseId',
        'remark': 'remark',
        'stage': 'stage',
        'steps': 'steps',
        'svn_script_path': 'svnScriptPath',
        'tags': 'tags',
        'test_feature': 'test_feature',
        'test_step': 'test_step',
        'test_type': 'test_type',
        'uri': 'uri'
    }

    def __init__(self, activity_id=None, applied_product=None, author=None, auto_type=None, cata_id=None, creation_date=None, custom_field_1=None, custom_field_10=None, custom_field_11=None, custom_field_12=None, custom_field_13=None, custom_field_14=None, custom_field_15=None, custom_field_16=None, custom_field_17=None, custom_field_18=None, custom_field_19=None, custom_field_2=None, custom_field_20=None, custom_field_21=None, custom_field_22=None, custom_field_23=None, custom_field_24=None, custom_field_25=None, custom_field_3=None, custom_field_4=None, custom_field_5=None, custom_field_6=None, custom_field_7=None, custom_field_8=None, custom_field_9=None, description=None, dr_relationid=None, env_type=None, exe_platform=None, expect_output=None, feature_path=None, is_key_word=None, is_contract_testcase=None, is_para_validator_testcase=None, label_id=None, last_modified=None, last_modifier=None, last_result=None, level=None, market=None, module_id=None, name=None, network_script_name=None, node_name=None, number=None, origin_uri=None, owner=None, owner_id=None, preparation=None, release_dev=None, release_id=None, remark=None, stage=None, steps=None, svn_script_path=None, tags=None, test_feature=None, test_step=None, test_type=None, uri=None):
        r"""TmssTestcase

        The model defined in huaweicloud sdk

        :param activity_id: 活动id
        :type activity_id: str
        :param applied_product: 应用产品
        :type applied_product: str
        :param author: 创建人
        :type author: str
        :param auto_type: 自动化类型
        :type auto_type: str
        :param cata_id: 用例分类ID
        :type cata_id: str
        :param creation_date: 创建日期
        :type creation_date: str
        :param custom_field_1: 
        :type custom_field_1: str
        :param custom_field_10: 
        :type custom_field_10: str
        :param custom_field_11: 
        :type custom_field_11: str
        :param custom_field_12: 
        :type custom_field_12: str
        :param custom_field_13: 
        :type custom_field_13: str
        :param custom_field_14: 
        :type custom_field_14: str
        :param custom_field_15: 
        :type custom_field_15: str
        :param custom_field_16: 
        :type custom_field_16: str
        :param custom_field_17: 
        :type custom_field_17: str
        :param custom_field_18: 
        :type custom_field_18: str
        :param custom_field_19: 
        :type custom_field_19: str
        :param custom_field_2: 
        :type custom_field_2: str
        :param custom_field_20: 
        :type custom_field_20: str
        :param custom_field_21: 
        :type custom_field_21: str
        :param custom_field_22: 
        :type custom_field_22: str
        :param custom_field_23: 
        :type custom_field_23: str
        :param custom_field_24: 
        :type custom_field_24: str
        :param custom_field_25: 
        :type custom_field_25: str
        :param custom_field_3: 
        :type custom_field_3: str
        :param custom_field_4: 
        :type custom_field_4: str
        :param custom_field_5: 
        :type custom_field_5: str
        :param custom_field_6: 
        :type custom_field_6: str
        :param custom_field_7: 
        :type custom_field_7: str
        :param custom_field_8: 
        :type custom_field_8: str
        :param custom_field_9: 
        :type custom_field_9: str
        :param description: 描述
        :type description: str
        :param dr_relationid: dr关系ID
        :type dr_relationid: str
        :param env_type: 环境类型
        :type env_type: str
        :param exe_platform: 执行平台
        :type exe_platform: str
        :param expect_output: 内部预期输出
        :type expect_output: str
        :param feature_path: 特性路径
        :type feature_path: str
        :param is_key_word: 是否为关键字
        :type is_key_word: int
        :param is_contract_testcase: 是否为合同测试用例
        :type is_contract_testcase: str
        :param is_para_validator_testcase: 是否为参数校验测试用例
        :type is_para_validator_testcase: str
        :param label_id: 标签ID列表
        :type label_id: list[str]
        :param last_modified: 最后修改时间
        :type last_modified: str
        :param last_modifier: 最后修改人
        :type last_modifier: str
        :param last_result: 最后的结果
        :type last_result: str
        :param level: 用例级别
        :type level: int
        :param market: 市场
        :type market: str
        :param module_id: 模块ID
        :type module_id: str
        :param name: 用例名称
        :type name: str
        :param network_script_name: 公共aw和项目的关联关系
        :type network_script_name: str
        :param node_name: 节点名称
        :type node_name: str
        :param number: 用例编号
        :type number: str
        :param origin_uri: 原始的uri
        :type origin_uri: str
        :param owner: 测试的所有者
        :type owner: str
        :param owner_id: 所有者ID
        :type owner_id: str
        :param preparation: 测试前置条件
        :type preparation: str
        :param release_dev: 新服务新建用例版本号
        :type release_dev: str
        :param release_id: 发布ID
        :type release_id: str
        :param remark: 备注
        :type remark: str
        :param stage: 阶段
        :type stage: str
        :param steps: 存储测试步骤和预期结果值对象
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.TmssStep`]
        :param svn_script_path: 脚本路径
        :type svn_script_path: str
        :param tags: 标签
        :type tags: str
        :param test_feature: 测试特性
        :type test_feature: str
        :param test_step: 内部测试步骤
        :type test_step: str
        :param test_type: 测试类型
        :type test_type: int
        :param uri: 用例基线Uri(BAM 接口覆盖率迭代下用例信息获取用)
        :type uri: str
        """
        
        

        self._activity_id = None
        self._applied_product = None
        self._author = None
        self._auto_type = None
        self._cata_id = None
        self._creation_date = None
        self._custom_field_1 = None
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
        self._custom_field_2 = None
        self._custom_field_20 = None
        self._custom_field_21 = None
        self._custom_field_22 = None
        self._custom_field_23 = None
        self._custom_field_24 = None
        self._custom_field_25 = None
        self._custom_field_3 = None
        self._custom_field_4 = None
        self._custom_field_5 = None
        self._custom_field_6 = None
        self._custom_field_7 = None
        self._custom_field_8 = None
        self._custom_field_9 = None
        self._description = None
        self._dr_relationid = None
        self._env_type = None
        self._exe_platform = None
        self._expect_output = None
        self._feature_path = None
        self._is_key_word = None
        self._is_contract_testcase = None
        self._is_para_validator_testcase = None
        self._label_id = None
        self._last_modified = None
        self._last_modifier = None
        self._last_result = None
        self._level = None
        self._market = None
        self._module_id = None
        self._name = None
        self._network_script_name = None
        self._node_name = None
        self._number = None
        self._origin_uri = None
        self._owner = None
        self._owner_id = None
        self._preparation = None
        self._release_dev = None
        self._release_id = None
        self._remark = None
        self._stage = None
        self._steps = None
        self._svn_script_path = None
        self._tags = None
        self._test_feature = None
        self._test_step = None
        self._test_type = None
        self._uri = None
        self.discriminator = None

        if activity_id is not None:
            self.activity_id = activity_id
        if applied_product is not None:
            self.applied_product = applied_product
        if author is not None:
            self.author = author
        if auto_type is not None:
            self.auto_type = auto_type
        if cata_id is not None:
            self.cata_id = cata_id
        if creation_date is not None:
            self.creation_date = creation_date
        if custom_field_1 is not None:
            self.custom_field_1 = custom_field_1
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
        if custom_field_2 is not None:
            self.custom_field_2 = custom_field_2
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
        if description is not None:
            self.description = description
        if dr_relationid is not None:
            self.dr_relationid = dr_relationid
        if env_type is not None:
            self.env_type = env_type
        if exe_platform is not None:
            self.exe_platform = exe_platform
        if expect_output is not None:
            self.expect_output = expect_output
        if feature_path is not None:
            self.feature_path = feature_path
        if is_key_word is not None:
            self.is_key_word = is_key_word
        if is_contract_testcase is not None:
            self.is_contract_testcase = is_contract_testcase
        if is_para_validator_testcase is not None:
            self.is_para_validator_testcase = is_para_validator_testcase
        if label_id is not None:
            self.label_id = label_id
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modifier is not None:
            self.last_modifier = last_modifier
        if last_result is not None:
            self.last_result = last_result
        if level is not None:
            self.level = level
        if market is not None:
            self.market = market
        if module_id is not None:
            self.module_id = module_id
        if name is not None:
            self.name = name
        if network_script_name is not None:
            self.network_script_name = network_script_name
        if node_name is not None:
            self.node_name = node_name
        if number is not None:
            self.number = number
        if origin_uri is not None:
            self.origin_uri = origin_uri
        if owner is not None:
            self.owner = owner
        if owner_id is not None:
            self.owner_id = owner_id
        if preparation is not None:
            self.preparation = preparation
        if release_dev is not None:
            self.release_dev = release_dev
        if release_id is not None:
            self.release_id = release_id
        if remark is not None:
            self.remark = remark
        if stage is not None:
            self.stage = stage
        if steps is not None:
            self.steps = steps
        if svn_script_path is not None:
            self.svn_script_path = svn_script_path
        if tags is not None:
            self.tags = tags
        if test_feature is not None:
            self.test_feature = test_feature
        if test_step is not None:
            self.test_step = test_step
        if test_type is not None:
            self.test_type = test_type
        if uri is not None:
            self.uri = uri

    @property
    def activity_id(self):
        r"""Gets the activity_id of this TmssTestcase.

        活动id

        :return: The activity_id of this TmssTestcase.
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        r"""Sets the activity_id of this TmssTestcase.

        活动id

        :param activity_id: The activity_id of this TmssTestcase.
        :type activity_id: str
        """
        self._activity_id = activity_id

    @property
    def applied_product(self):
        r"""Gets the applied_product of this TmssTestcase.

        应用产品

        :return: The applied_product of this TmssTestcase.
        :rtype: str
        """
        return self._applied_product

    @applied_product.setter
    def applied_product(self, applied_product):
        r"""Sets the applied_product of this TmssTestcase.

        应用产品

        :param applied_product: The applied_product of this TmssTestcase.
        :type applied_product: str
        """
        self._applied_product = applied_product

    @property
    def author(self):
        r"""Gets the author of this TmssTestcase.

        创建人

        :return: The author of this TmssTestcase.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this TmssTestcase.

        创建人

        :param author: The author of this TmssTestcase.
        :type author: str
        """
        self._author = author

    @property
    def auto_type(self):
        r"""Gets the auto_type of this TmssTestcase.

        自动化类型

        :return: The auto_type of this TmssTestcase.
        :rtype: str
        """
        return self._auto_type

    @auto_type.setter
    def auto_type(self, auto_type):
        r"""Sets the auto_type of this TmssTestcase.

        自动化类型

        :param auto_type: The auto_type of this TmssTestcase.
        :type auto_type: str
        """
        self._auto_type = auto_type

    @property
    def cata_id(self):
        r"""Gets the cata_id of this TmssTestcase.

        用例分类ID

        :return: The cata_id of this TmssTestcase.
        :rtype: str
        """
        return self._cata_id

    @cata_id.setter
    def cata_id(self, cata_id):
        r"""Sets the cata_id of this TmssTestcase.

        用例分类ID

        :param cata_id: The cata_id of this TmssTestcase.
        :type cata_id: str
        """
        self._cata_id = cata_id

    @property
    def creation_date(self):
        r"""Gets the creation_date of this TmssTestcase.

        创建日期

        :return: The creation_date of this TmssTestcase.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this TmssTestcase.

        创建日期

        :param creation_date: The creation_date of this TmssTestcase.
        :type creation_date: str
        """
        self._creation_date = creation_date

    @property
    def custom_field_1(self):
        r"""Gets the custom_field_1 of this TmssTestcase.

        :return: The custom_field_1 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_1

    @custom_field_1.setter
    def custom_field_1(self, custom_field_1):
        r"""Sets the custom_field_1 of this TmssTestcase.

        :param custom_field_1: The custom_field_1 of this TmssTestcase.
        :type custom_field_1: str
        """
        self._custom_field_1 = custom_field_1

    @property
    def custom_field_10(self):
        r"""Gets the custom_field_10 of this TmssTestcase.

        :return: The custom_field_10 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_10

    @custom_field_10.setter
    def custom_field_10(self, custom_field_10):
        r"""Sets the custom_field_10 of this TmssTestcase.

        :param custom_field_10: The custom_field_10 of this TmssTestcase.
        :type custom_field_10: str
        """
        self._custom_field_10 = custom_field_10

    @property
    def custom_field_11(self):
        r"""Gets the custom_field_11 of this TmssTestcase.

        :return: The custom_field_11 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_11

    @custom_field_11.setter
    def custom_field_11(self, custom_field_11):
        r"""Sets the custom_field_11 of this TmssTestcase.

        :param custom_field_11: The custom_field_11 of this TmssTestcase.
        :type custom_field_11: str
        """
        self._custom_field_11 = custom_field_11

    @property
    def custom_field_12(self):
        r"""Gets the custom_field_12 of this TmssTestcase.

        :return: The custom_field_12 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_12

    @custom_field_12.setter
    def custom_field_12(self, custom_field_12):
        r"""Sets the custom_field_12 of this TmssTestcase.

        :param custom_field_12: The custom_field_12 of this TmssTestcase.
        :type custom_field_12: str
        """
        self._custom_field_12 = custom_field_12

    @property
    def custom_field_13(self):
        r"""Gets the custom_field_13 of this TmssTestcase.

        :return: The custom_field_13 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_13

    @custom_field_13.setter
    def custom_field_13(self, custom_field_13):
        r"""Sets the custom_field_13 of this TmssTestcase.

        :param custom_field_13: The custom_field_13 of this TmssTestcase.
        :type custom_field_13: str
        """
        self._custom_field_13 = custom_field_13

    @property
    def custom_field_14(self):
        r"""Gets the custom_field_14 of this TmssTestcase.

        :return: The custom_field_14 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_14

    @custom_field_14.setter
    def custom_field_14(self, custom_field_14):
        r"""Sets the custom_field_14 of this TmssTestcase.

        :param custom_field_14: The custom_field_14 of this TmssTestcase.
        :type custom_field_14: str
        """
        self._custom_field_14 = custom_field_14

    @property
    def custom_field_15(self):
        r"""Gets the custom_field_15 of this TmssTestcase.

        :return: The custom_field_15 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_15

    @custom_field_15.setter
    def custom_field_15(self, custom_field_15):
        r"""Sets the custom_field_15 of this TmssTestcase.

        :param custom_field_15: The custom_field_15 of this TmssTestcase.
        :type custom_field_15: str
        """
        self._custom_field_15 = custom_field_15

    @property
    def custom_field_16(self):
        r"""Gets the custom_field_16 of this TmssTestcase.

        :return: The custom_field_16 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_16

    @custom_field_16.setter
    def custom_field_16(self, custom_field_16):
        r"""Sets the custom_field_16 of this TmssTestcase.

        :param custom_field_16: The custom_field_16 of this TmssTestcase.
        :type custom_field_16: str
        """
        self._custom_field_16 = custom_field_16

    @property
    def custom_field_17(self):
        r"""Gets the custom_field_17 of this TmssTestcase.

        :return: The custom_field_17 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_17

    @custom_field_17.setter
    def custom_field_17(self, custom_field_17):
        r"""Sets the custom_field_17 of this TmssTestcase.

        :param custom_field_17: The custom_field_17 of this TmssTestcase.
        :type custom_field_17: str
        """
        self._custom_field_17 = custom_field_17

    @property
    def custom_field_18(self):
        r"""Gets the custom_field_18 of this TmssTestcase.

        :return: The custom_field_18 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_18

    @custom_field_18.setter
    def custom_field_18(self, custom_field_18):
        r"""Sets the custom_field_18 of this TmssTestcase.

        :param custom_field_18: The custom_field_18 of this TmssTestcase.
        :type custom_field_18: str
        """
        self._custom_field_18 = custom_field_18

    @property
    def custom_field_19(self):
        r"""Gets the custom_field_19 of this TmssTestcase.

        :return: The custom_field_19 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_19

    @custom_field_19.setter
    def custom_field_19(self, custom_field_19):
        r"""Sets the custom_field_19 of this TmssTestcase.

        :param custom_field_19: The custom_field_19 of this TmssTestcase.
        :type custom_field_19: str
        """
        self._custom_field_19 = custom_field_19

    @property
    def custom_field_2(self):
        r"""Gets the custom_field_2 of this TmssTestcase.

        :return: The custom_field_2 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_2

    @custom_field_2.setter
    def custom_field_2(self, custom_field_2):
        r"""Sets the custom_field_2 of this TmssTestcase.

        :param custom_field_2: The custom_field_2 of this TmssTestcase.
        :type custom_field_2: str
        """
        self._custom_field_2 = custom_field_2

    @property
    def custom_field_20(self):
        r"""Gets the custom_field_20 of this TmssTestcase.

        :return: The custom_field_20 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_20

    @custom_field_20.setter
    def custom_field_20(self, custom_field_20):
        r"""Sets the custom_field_20 of this TmssTestcase.

        :param custom_field_20: The custom_field_20 of this TmssTestcase.
        :type custom_field_20: str
        """
        self._custom_field_20 = custom_field_20

    @property
    def custom_field_21(self):
        r"""Gets the custom_field_21 of this TmssTestcase.

        :return: The custom_field_21 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_21

    @custom_field_21.setter
    def custom_field_21(self, custom_field_21):
        r"""Sets the custom_field_21 of this TmssTestcase.

        :param custom_field_21: The custom_field_21 of this TmssTestcase.
        :type custom_field_21: str
        """
        self._custom_field_21 = custom_field_21

    @property
    def custom_field_22(self):
        r"""Gets the custom_field_22 of this TmssTestcase.

        :return: The custom_field_22 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_22

    @custom_field_22.setter
    def custom_field_22(self, custom_field_22):
        r"""Sets the custom_field_22 of this TmssTestcase.

        :param custom_field_22: The custom_field_22 of this TmssTestcase.
        :type custom_field_22: str
        """
        self._custom_field_22 = custom_field_22

    @property
    def custom_field_23(self):
        r"""Gets the custom_field_23 of this TmssTestcase.

        :return: The custom_field_23 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_23

    @custom_field_23.setter
    def custom_field_23(self, custom_field_23):
        r"""Sets the custom_field_23 of this TmssTestcase.

        :param custom_field_23: The custom_field_23 of this TmssTestcase.
        :type custom_field_23: str
        """
        self._custom_field_23 = custom_field_23

    @property
    def custom_field_24(self):
        r"""Gets the custom_field_24 of this TmssTestcase.

        :return: The custom_field_24 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_24

    @custom_field_24.setter
    def custom_field_24(self, custom_field_24):
        r"""Sets the custom_field_24 of this TmssTestcase.

        :param custom_field_24: The custom_field_24 of this TmssTestcase.
        :type custom_field_24: str
        """
        self._custom_field_24 = custom_field_24

    @property
    def custom_field_25(self):
        r"""Gets the custom_field_25 of this TmssTestcase.

        :return: The custom_field_25 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_25

    @custom_field_25.setter
    def custom_field_25(self, custom_field_25):
        r"""Sets the custom_field_25 of this TmssTestcase.

        :param custom_field_25: The custom_field_25 of this TmssTestcase.
        :type custom_field_25: str
        """
        self._custom_field_25 = custom_field_25

    @property
    def custom_field_3(self):
        r"""Gets the custom_field_3 of this TmssTestcase.

        :return: The custom_field_3 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_3

    @custom_field_3.setter
    def custom_field_3(self, custom_field_3):
        r"""Sets the custom_field_3 of this TmssTestcase.

        :param custom_field_3: The custom_field_3 of this TmssTestcase.
        :type custom_field_3: str
        """
        self._custom_field_3 = custom_field_3

    @property
    def custom_field_4(self):
        r"""Gets the custom_field_4 of this TmssTestcase.

        :return: The custom_field_4 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_4

    @custom_field_4.setter
    def custom_field_4(self, custom_field_4):
        r"""Sets the custom_field_4 of this TmssTestcase.

        :param custom_field_4: The custom_field_4 of this TmssTestcase.
        :type custom_field_4: str
        """
        self._custom_field_4 = custom_field_4

    @property
    def custom_field_5(self):
        r"""Gets the custom_field_5 of this TmssTestcase.

        :return: The custom_field_5 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_5

    @custom_field_5.setter
    def custom_field_5(self, custom_field_5):
        r"""Sets the custom_field_5 of this TmssTestcase.

        :param custom_field_5: The custom_field_5 of this TmssTestcase.
        :type custom_field_5: str
        """
        self._custom_field_5 = custom_field_5

    @property
    def custom_field_6(self):
        r"""Gets the custom_field_6 of this TmssTestcase.

        :return: The custom_field_6 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_6

    @custom_field_6.setter
    def custom_field_6(self, custom_field_6):
        r"""Sets the custom_field_6 of this TmssTestcase.

        :param custom_field_6: The custom_field_6 of this TmssTestcase.
        :type custom_field_6: str
        """
        self._custom_field_6 = custom_field_6

    @property
    def custom_field_7(self):
        r"""Gets the custom_field_7 of this TmssTestcase.

        :return: The custom_field_7 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_7

    @custom_field_7.setter
    def custom_field_7(self, custom_field_7):
        r"""Sets the custom_field_7 of this TmssTestcase.

        :param custom_field_7: The custom_field_7 of this TmssTestcase.
        :type custom_field_7: str
        """
        self._custom_field_7 = custom_field_7

    @property
    def custom_field_8(self):
        r"""Gets the custom_field_8 of this TmssTestcase.

        :return: The custom_field_8 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_8

    @custom_field_8.setter
    def custom_field_8(self, custom_field_8):
        r"""Sets the custom_field_8 of this TmssTestcase.

        :param custom_field_8: The custom_field_8 of this TmssTestcase.
        :type custom_field_8: str
        """
        self._custom_field_8 = custom_field_8

    @property
    def custom_field_9(self):
        r"""Gets the custom_field_9 of this TmssTestcase.

        :return: The custom_field_9 of this TmssTestcase.
        :rtype: str
        """
        return self._custom_field_9

    @custom_field_9.setter
    def custom_field_9(self, custom_field_9):
        r"""Sets the custom_field_9 of this TmssTestcase.

        :param custom_field_9: The custom_field_9 of this TmssTestcase.
        :type custom_field_9: str
        """
        self._custom_field_9 = custom_field_9

    @property
    def description(self):
        r"""Gets the description of this TmssTestcase.

        描述

        :return: The description of this TmssTestcase.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TmssTestcase.

        描述

        :param description: The description of this TmssTestcase.
        :type description: str
        """
        self._description = description

    @property
    def dr_relationid(self):
        r"""Gets the dr_relationid of this TmssTestcase.

        dr关系ID

        :return: The dr_relationid of this TmssTestcase.
        :rtype: str
        """
        return self._dr_relationid

    @dr_relationid.setter
    def dr_relationid(self, dr_relationid):
        r"""Sets the dr_relationid of this TmssTestcase.

        dr关系ID

        :param dr_relationid: The dr_relationid of this TmssTestcase.
        :type dr_relationid: str
        """
        self._dr_relationid = dr_relationid

    @property
    def env_type(self):
        r"""Gets the env_type of this TmssTestcase.

        环境类型

        :return: The env_type of this TmssTestcase.
        :rtype: str
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        r"""Sets the env_type of this TmssTestcase.

        环境类型

        :param env_type: The env_type of this TmssTestcase.
        :type env_type: str
        """
        self._env_type = env_type

    @property
    def exe_platform(self):
        r"""Gets the exe_platform of this TmssTestcase.

        执行平台

        :return: The exe_platform of this TmssTestcase.
        :rtype: str
        """
        return self._exe_platform

    @exe_platform.setter
    def exe_platform(self, exe_platform):
        r"""Sets the exe_platform of this TmssTestcase.

        执行平台

        :param exe_platform: The exe_platform of this TmssTestcase.
        :type exe_platform: str
        """
        self._exe_platform = exe_platform

    @property
    def expect_output(self):
        r"""Gets the expect_output of this TmssTestcase.

        内部预期输出

        :return: The expect_output of this TmssTestcase.
        :rtype: str
        """
        return self._expect_output

    @expect_output.setter
    def expect_output(self, expect_output):
        r"""Sets the expect_output of this TmssTestcase.

        内部预期输出

        :param expect_output: The expect_output of this TmssTestcase.
        :type expect_output: str
        """
        self._expect_output = expect_output

    @property
    def feature_path(self):
        r"""Gets the feature_path of this TmssTestcase.

        特性路径

        :return: The feature_path of this TmssTestcase.
        :rtype: str
        """
        return self._feature_path

    @feature_path.setter
    def feature_path(self, feature_path):
        r"""Sets the feature_path of this TmssTestcase.

        特性路径

        :param feature_path: The feature_path of this TmssTestcase.
        :type feature_path: str
        """
        self._feature_path = feature_path

    @property
    def is_key_word(self):
        r"""Gets the is_key_word of this TmssTestcase.

        是否为关键字

        :return: The is_key_word of this TmssTestcase.
        :rtype: int
        """
        return self._is_key_word

    @is_key_word.setter
    def is_key_word(self, is_key_word):
        r"""Sets the is_key_word of this TmssTestcase.

        是否为关键字

        :param is_key_word: The is_key_word of this TmssTestcase.
        :type is_key_word: int
        """
        self._is_key_word = is_key_word

    @property
    def is_contract_testcase(self):
        r"""Gets the is_contract_testcase of this TmssTestcase.

        是否为合同测试用例

        :return: The is_contract_testcase of this TmssTestcase.
        :rtype: str
        """
        return self._is_contract_testcase

    @is_contract_testcase.setter
    def is_contract_testcase(self, is_contract_testcase):
        r"""Sets the is_contract_testcase of this TmssTestcase.

        是否为合同测试用例

        :param is_contract_testcase: The is_contract_testcase of this TmssTestcase.
        :type is_contract_testcase: str
        """
        self._is_contract_testcase = is_contract_testcase

    @property
    def is_para_validator_testcase(self):
        r"""Gets the is_para_validator_testcase of this TmssTestcase.

        是否为参数校验测试用例

        :return: The is_para_validator_testcase of this TmssTestcase.
        :rtype: str
        """
        return self._is_para_validator_testcase

    @is_para_validator_testcase.setter
    def is_para_validator_testcase(self, is_para_validator_testcase):
        r"""Sets the is_para_validator_testcase of this TmssTestcase.

        是否为参数校验测试用例

        :param is_para_validator_testcase: The is_para_validator_testcase of this TmssTestcase.
        :type is_para_validator_testcase: str
        """
        self._is_para_validator_testcase = is_para_validator_testcase

    @property
    def label_id(self):
        r"""Gets the label_id of this TmssTestcase.

        标签ID列表

        :return: The label_id of this TmssTestcase.
        :rtype: list[str]
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        r"""Sets the label_id of this TmssTestcase.

        标签ID列表

        :param label_id: The label_id of this TmssTestcase.
        :type label_id: list[str]
        """
        self._label_id = label_id

    @property
    def last_modified(self):
        r"""Gets the last_modified of this TmssTestcase.

        最后修改时间

        :return: The last_modified of this TmssTestcase.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this TmssTestcase.

        最后修改时间

        :param last_modified: The last_modified of this TmssTestcase.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def last_modifier(self):
        r"""Gets the last_modifier of this TmssTestcase.

        最后修改人

        :return: The last_modifier of this TmssTestcase.
        :rtype: str
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        r"""Sets the last_modifier of this TmssTestcase.

        最后修改人

        :param last_modifier: The last_modifier of this TmssTestcase.
        :type last_modifier: str
        """
        self._last_modifier = last_modifier

    @property
    def last_result(self):
        r"""Gets the last_result of this TmssTestcase.

        最后的结果

        :return: The last_result of this TmssTestcase.
        :rtype: str
        """
        return self._last_result

    @last_result.setter
    def last_result(self, last_result):
        r"""Sets the last_result of this TmssTestcase.

        最后的结果

        :param last_result: The last_result of this TmssTestcase.
        :type last_result: str
        """
        self._last_result = last_result

    @property
    def level(self):
        r"""Gets the level of this TmssTestcase.

        用例级别

        :return: The level of this TmssTestcase.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this TmssTestcase.

        用例级别

        :param level: The level of this TmssTestcase.
        :type level: int
        """
        self._level = level

    @property
    def market(self):
        r"""Gets the market of this TmssTestcase.

        市场

        :return: The market of this TmssTestcase.
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        r"""Sets the market of this TmssTestcase.

        市场

        :param market: The market of this TmssTestcase.
        :type market: str
        """
        self._market = market

    @property
    def module_id(self):
        r"""Gets the module_id of this TmssTestcase.

        模块ID

        :return: The module_id of this TmssTestcase.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this TmssTestcase.

        模块ID

        :param module_id: The module_id of this TmssTestcase.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def name(self):
        r"""Gets the name of this TmssTestcase.

        用例名称

        :return: The name of this TmssTestcase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TmssTestcase.

        用例名称

        :param name: The name of this TmssTestcase.
        :type name: str
        """
        self._name = name

    @property
    def network_script_name(self):
        r"""Gets the network_script_name of this TmssTestcase.

        公共aw和项目的关联关系

        :return: The network_script_name of this TmssTestcase.
        :rtype: str
        """
        return self._network_script_name

    @network_script_name.setter
    def network_script_name(self, network_script_name):
        r"""Sets the network_script_name of this TmssTestcase.

        公共aw和项目的关联关系

        :param network_script_name: The network_script_name of this TmssTestcase.
        :type network_script_name: str
        """
        self._network_script_name = network_script_name

    @property
    def node_name(self):
        r"""Gets the node_name of this TmssTestcase.

        节点名称

        :return: The node_name of this TmssTestcase.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this TmssTestcase.

        节点名称

        :param node_name: The node_name of this TmssTestcase.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def number(self):
        r"""Gets the number of this TmssTestcase.

        用例编号

        :return: The number of this TmssTestcase.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this TmssTestcase.

        用例编号

        :param number: The number of this TmssTestcase.
        :type number: str
        """
        self._number = number

    @property
    def origin_uri(self):
        r"""Gets the origin_uri of this TmssTestcase.

        原始的uri

        :return: The origin_uri of this TmssTestcase.
        :rtype: str
        """
        return self._origin_uri

    @origin_uri.setter
    def origin_uri(self, origin_uri):
        r"""Sets the origin_uri of this TmssTestcase.

        原始的uri

        :param origin_uri: The origin_uri of this TmssTestcase.
        :type origin_uri: str
        """
        self._origin_uri = origin_uri

    @property
    def owner(self):
        r"""Gets the owner of this TmssTestcase.

        测试的所有者

        :return: The owner of this TmssTestcase.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TmssTestcase.

        测试的所有者

        :param owner: The owner of this TmssTestcase.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_id(self):
        r"""Gets the owner_id of this TmssTestcase.

        所有者ID

        :return: The owner_id of this TmssTestcase.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this TmssTestcase.

        所有者ID

        :param owner_id: The owner_id of this TmssTestcase.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def preparation(self):
        r"""Gets the preparation of this TmssTestcase.

        测试前置条件

        :return: The preparation of this TmssTestcase.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        r"""Sets the preparation of this TmssTestcase.

        测试前置条件

        :param preparation: The preparation of this TmssTestcase.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def release_dev(self):
        r"""Gets the release_dev of this TmssTestcase.

        新服务新建用例版本号

        :return: The release_dev of this TmssTestcase.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this TmssTestcase.

        新服务新建用例版本号

        :param release_dev: The release_dev of this TmssTestcase.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def release_id(self):
        r"""Gets the release_id of this TmssTestcase.

        发布ID

        :return: The release_id of this TmssTestcase.
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        r"""Sets the release_id of this TmssTestcase.

        发布ID

        :param release_id: The release_id of this TmssTestcase.
        :type release_id: str
        """
        self._release_id = release_id

    @property
    def remark(self):
        r"""Gets the remark of this TmssTestcase.

        备注

        :return: The remark of this TmssTestcase.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this TmssTestcase.

        备注

        :param remark: The remark of this TmssTestcase.
        :type remark: str
        """
        self._remark = remark

    @property
    def stage(self):
        r"""Gets the stage of this TmssTestcase.

        阶段

        :return: The stage of this TmssTestcase.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this TmssTestcase.

        阶段

        :param stage: The stage of this TmssTestcase.
        :type stage: str
        """
        self._stage = stage

    @property
    def steps(self):
        r"""Gets the steps of this TmssTestcase.

        存储测试步骤和预期结果值对象

        :return: The steps of this TmssTestcase.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TmssStep`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this TmssTestcase.

        存储测试步骤和预期结果值对象

        :param steps: The steps of this TmssTestcase.
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.TmssStep`]
        """
        self._steps = steps

    @property
    def svn_script_path(self):
        r"""Gets the svn_script_path of this TmssTestcase.

        脚本路径

        :return: The svn_script_path of this TmssTestcase.
        :rtype: str
        """
        return self._svn_script_path

    @svn_script_path.setter
    def svn_script_path(self, svn_script_path):
        r"""Sets the svn_script_path of this TmssTestcase.

        脚本路径

        :param svn_script_path: The svn_script_path of this TmssTestcase.
        :type svn_script_path: str
        """
        self._svn_script_path = svn_script_path

    @property
    def tags(self):
        r"""Gets the tags of this TmssTestcase.

        标签

        :return: The tags of this TmssTestcase.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TmssTestcase.

        标签

        :param tags: The tags of this TmssTestcase.
        :type tags: str
        """
        self._tags = tags

    @property
    def test_feature(self):
        r"""Gets the test_feature of this TmssTestcase.

        测试特性

        :return: The test_feature of this TmssTestcase.
        :rtype: str
        """
        return self._test_feature

    @test_feature.setter
    def test_feature(self, test_feature):
        r"""Sets the test_feature of this TmssTestcase.

        测试特性

        :param test_feature: The test_feature of this TmssTestcase.
        :type test_feature: str
        """
        self._test_feature = test_feature

    @property
    def test_step(self):
        r"""Gets the test_step of this TmssTestcase.

        内部测试步骤

        :return: The test_step of this TmssTestcase.
        :rtype: str
        """
        return self._test_step

    @test_step.setter
    def test_step(self, test_step):
        r"""Sets the test_step of this TmssTestcase.

        内部测试步骤

        :param test_step: The test_step of this TmssTestcase.
        :type test_step: str
        """
        self._test_step = test_step

    @property
    def test_type(self):
        r"""Gets the test_type of this TmssTestcase.

        测试类型

        :return: The test_type of this TmssTestcase.
        :rtype: int
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        r"""Sets the test_type of this TmssTestcase.

        测试类型

        :param test_type: The test_type of this TmssTestcase.
        :type test_type: int
        """
        self._test_type = test_type

    @property
    def uri(self):
        r"""Gets the uri of this TmssTestcase.

        用例基线Uri(BAM 接口覆盖率迭代下用例信息获取用)

        :return: The uri of this TmssTestcase.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TmssTestcase.

        用例基线Uri(BAM 接口覆盖率迭代下用例信息获取用)

        :param uri: The uri of this TmssTestcase.
        :type uri: str
        """
        self._uri = uri

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
        if not isinstance(other, TmssTestcase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
