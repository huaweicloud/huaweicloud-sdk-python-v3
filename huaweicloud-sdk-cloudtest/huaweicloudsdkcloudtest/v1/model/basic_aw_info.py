# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicAWInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aw_code': 'str',
        'aw_description': 'str',
        'aw_ins_list': 'list[AwInstanceRes]',
        'aw_mark': 'int',
        'aw_operationid': 'str',
        'aw_tags': 'str',
        'aw_type': 'int',
        'aw_uniqueid': 'str',
        'by_order': 'int',
        'cata_type': 'int',
        'child_list': 'list[BasicAWInfo]',
        'create_time': 'str',
        'create_time_stamp': 'int',
        'create_time_string': 'str',
        'create_user': 'str',
        'create_user_id': 'str',
        'custom_aw_libs': 'list[UploadFileRes]',
        'delete_time': 'str',
        'delete_user': 'str',
        'description': 'str',
        'dft_check_point_list': 'list[CheckPoint]',
        'dft_custom_header': 'list[AwParam]',
        'dft_retry_interval': 'str',
        'dft_retry_times': 'str',
        'dft_variable_list': 'list[AwVariable]',
        'extra_info': 'JsonNode',
        'group_name': 'str',
        'has_code': 'int',
        'id': 'str',
        'import_package': 'list[str]',
        'interface_label': 'str',
        'is_favorite': 'int',
        'is_folder': 'str',
        'keyword_variable_value': 'list[AwVariable]',
        'method': 'str',
        'name': 'str',
        'name_view': 'str',
        'origin_project': 'str',
        'output_param_list': 'list[AwVariable]',
        'page_no': 'int',
        'page_size': 'int',
        'param_type_and_dft_value': 'list[AwParam]',
        'parent_id': 'str',
        'project_id': 'str',
        'protocol_type': 'str',
        'public_aw_lib': 'PublicAwLibRes',
        'public_aw_lib_id': 'str',
        'region': 'str',
        'return_type': 'str',
        'root_id': 'str',
        'source': 'str',
        'special_type': 'int',
        'tmss_case_number': 'str',
        'tmss_case_id': 'str',
        'total_page': 'int',
        'total_size': 'int',
        'update_time': 'str',
        'update_time_stamp': 'int',
        'update_time_string': 'str',
        'update_user': 'str',
        'warning_msg': 'str',
        'yaml_name': 'str'
    }

    attribute_map = {
        'aw_code': 'aw_code',
        'aw_description': 'aw_description',
        'aw_ins_list': 'aw_ins_list',
        'aw_mark': 'aw_mark',
        'aw_operationid': 'aw_operationid',
        'aw_tags': 'aw_tags',
        'aw_type': 'aw_type',
        'aw_uniqueid': 'aw_uniqueid',
        'by_order': 'by_order',
        'cata_type': 'cata_type',
        'child_list': 'child_list',
        'create_time': 'create_time',
        'create_time_stamp': 'create_time_stamp',
        'create_time_string': 'create_time_string',
        'create_user': 'create_user',
        'create_user_id': 'create_user_id',
        'custom_aw_libs': 'custom_aw_libs',
        'delete_time': 'delete_time',
        'delete_user': 'delete_user',
        'description': 'description',
        'dft_check_point_list': 'dft_check_point_list',
        'dft_custom_header': 'dft_custom_header',
        'dft_retry_interval': 'dft_retry_interval',
        'dft_retry_times': 'dft_retry_times',
        'dft_variable_list': 'dft_variable_list',
        'extra_info': 'extra_info',
        'group_name': 'group_name',
        'has_code': 'has_code',
        'id': 'id',
        'import_package': 'import_package',
        'interface_label': 'interface_label',
        'is_favorite': 'is_favorite',
        'is_folder': 'is_folder',
        'keyword_variable_value': 'keyword_variable_value',
        'method': 'method',
        'name': 'name',
        'name_view': 'nameView',
        'origin_project': 'origin_project',
        'output_param_list': 'output_param_list',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'param_type_and_dft_value': 'param_type_and_dft_value',
        'parent_id': 'parent_id',
        'project_id': 'project_id',
        'protocol_type': 'protocol_type',
        'public_aw_lib': 'public_aw_lib',
        'public_aw_lib_id': 'public_aw_lib_id',
        'region': 'region',
        'return_type': 'return_type',
        'root_id': 'root_id',
        'source': 'source',
        'special_type': 'special_type',
        'tmss_case_number': 'tmssCaseNumber',
        'tmss_case_id': 'tmss_case_id',
        'total_page': 'total_page',
        'total_size': 'total_size',
        'update_time': 'update_time',
        'update_time_stamp': 'update_time_stamp',
        'update_time_string': 'update_time_string',
        'update_user': 'update_user',
        'warning_msg': 'warningMsg',
        'yaml_name': 'yamlName'
    }

    def __init__(self, aw_code=None, aw_description=None, aw_ins_list=None, aw_mark=None, aw_operationid=None, aw_tags=None, aw_type=None, aw_uniqueid=None, by_order=None, cata_type=None, child_list=None, create_time=None, create_time_stamp=None, create_time_string=None, create_user=None, create_user_id=None, custom_aw_libs=None, delete_time=None, delete_user=None, description=None, dft_check_point_list=None, dft_custom_header=None, dft_retry_interval=None, dft_retry_times=None, dft_variable_list=None, extra_info=None, group_name=None, has_code=None, id=None, import_package=None, interface_label=None, is_favorite=None, is_folder=None, keyword_variable_value=None, method=None, name=None, name_view=None, origin_project=None, output_param_list=None, page_no=None, page_size=None, param_type_and_dft_value=None, parent_id=None, project_id=None, protocol_type=None, public_aw_lib=None, public_aw_lib_id=None, region=None, return_type=None, root_id=None, source=None, special_type=None, tmss_case_number=None, tmss_case_id=None, total_page=None, total_size=None, update_time=None, update_time_stamp=None, update_time_string=None, update_user=None, warning_msg=None, yaml_name=None):
        """BasicAWInfo

        The model defined in huaweicloud sdk

        :param aw_code: aw代码, hasCode为1时有效
        :type aw_code: str
        :param aw_description: 模板描述
        :type aw_description: str
        :param aw_ins_list: 组合aw包含的aw实例信息，awType为2时该字段有效
        :type aw_ins_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstanceRes`]
        :param aw_mark: aw标记 0-normal；1-new；2-update 3-delete
        :type aw_mark: int
        :param aw_operationid: 接口的operationId
        :type aw_operationid: str
        :param aw_tags: 接口的tags
        :type aw_tags: str
        :param aw_type: AW类型1-普通aw,2-组合aw,3-导入aw
        :type aw_type: int
        :param aw_uniqueid: awOperationId_awTags的拼接
        :type aw_uniqueid: str
        :param by_order: 顺序
        :type by_order: int
        :param cata_type: 目录层级
        :type cata_type: int
        :param child_list: 新增childList以支持嵌套层级结构
        :type child_list: list[:class:`huaweicloudsdkcloudtest.v1.BasicAWInfo`]
        :param create_time: 创建时间
        :type create_time: str
        :param create_time_stamp: 时间戳字段
        :type create_time_stamp: int
        :param create_time_string: 时间字符串
        :type create_time_string: str
        :param create_user: 创建人
        :type create_user: str
        :param create_user_id: 创建人id
        :type create_user_id: str
        :param custom_aw_libs: aw库的文件列表
        :type custom_aw_libs: list[:class:`huaweicloudsdkcloudtest.v1.UploadFileRes`]
        :param delete_time: 更新时间
        :type delete_time: str
        :param delete_user: 删除人
        :type delete_user: str
        :param description: 描述
        :type description: str
        :param dft_check_point_list: 默认检查点List
        :type dft_check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        :param dft_custom_header: 默认请求头参数对象
        :type dft_custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        :param dft_retry_interval: 重试间隔时间 (ms) 为空表示不等待
        :type dft_retry_interval: str
        :param dft_retry_times: 重试次数
        :type dft_retry_times: str
        :param dft_variable_list: 默认变量信息List
        :type dft_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcloudtest.v1.JsonNode`
        :param group_name: 组名
        :type group_name: str
        :param has_code: 是否自带代码 0-不自带代码，该aw依赖source字段中的源；1-自带代码
        :type has_code: int
        :param id: id
        :type id: str
        :param import_package: 导入的包
        :type import_package: list[str]
        :param interface_label: 接口的x-extend
        :type interface_label: str
        :param is_favorite: 是否是当前工程的收藏aw，该字段不存数据库，每次获取时实时判断
        :type is_favorite: int
        :param is_folder: 判断是否为文件夹的标识
        :type is_folder: str
        :param keyword_variable_value: 关键字局部变量
        :type keyword_variable_value: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        :param method: 方法
        :type method: str
        :param name: 名称
        :type name: str
        :param name_view: aw在页面上显示的名字
        :type name_view: str
        :param origin_project: 源工程信息，如果该aw是从其他工程过来的(继承或者copy to local)
        :type origin_project: str
        :param output_param_list: 组合aw的输出参数信息，该字段不存数据库，实时获取
        :type output_param_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param param_type_and_dft_value: 参数类型和参数默认值对应List
        :type param_type_and_dft_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        :param parent_id: aw目录父编号
        :type parent_id: str
        :param project_id: aw目录父编号
        :type project_id: str
        :param protocol_type: 协议类型 (http/dsf/other)
        :type protocol_type: str
        :param public_aw_lib: 
        :type public_aw_lib: :class:`huaweicloudsdkcloudtest.v1.PublicAwLibRes`
        :param public_aw_lib_id: 所属公共aw库Id
        :type public_aw_lib_id: str
        :param region: 区域名称
        :type region: str
        :param return_type: 返回类型
        :type return_type: str
        :param root_id: root id
        :type root_id: str
        :param source: 来源
        :type source: str
        :param special_type: 特殊AW类型 0-common,10-header,1-beforeHeader
        :type special_type: int
        :param tmss_case_number: 关键字管理的用例编号
        :type tmss_case_number: str
        :param tmss_case_id: 关键字aw管理的用例ID
        :type tmss_case_id: str
        :param total_page: 总页数
        :type total_page: int
        :param total_size: 总条数
        :type total_size: int
        :param update_time: 更新时间
        :type update_time: str
        :param update_time_stamp: 更新时间戳
        :type update_time_stamp: int
        :param update_time_string: 更新字符串
        :type update_time_string: str
        :param update_user: 更新人
        :type update_user: str
        :param warning_msg: 警告信息
        :type warning_msg: str
        :param yaml_name: 所属yaml文件名称,该字段不存库，用来记录从哪个yaml文件导入
        :type yaml_name: str
        """
        
        

        self._aw_code = None
        self._aw_description = None
        self._aw_ins_list = None
        self._aw_mark = None
        self._aw_operationid = None
        self._aw_tags = None
        self._aw_type = None
        self._aw_uniqueid = None
        self._by_order = None
        self._cata_type = None
        self._child_list = None
        self._create_time = None
        self._create_time_stamp = None
        self._create_time_string = None
        self._create_user = None
        self._create_user_id = None
        self._custom_aw_libs = None
        self._delete_time = None
        self._delete_user = None
        self._description = None
        self._dft_check_point_list = None
        self._dft_custom_header = None
        self._dft_retry_interval = None
        self._dft_retry_times = None
        self._dft_variable_list = None
        self._extra_info = None
        self._group_name = None
        self._has_code = None
        self._id = None
        self._import_package = None
        self._interface_label = None
        self._is_favorite = None
        self._is_folder = None
        self._keyword_variable_value = None
        self._method = None
        self._name = None
        self._name_view = None
        self._origin_project = None
        self._output_param_list = None
        self._page_no = None
        self._page_size = None
        self._param_type_and_dft_value = None
        self._parent_id = None
        self._project_id = None
        self._protocol_type = None
        self._public_aw_lib = None
        self._public_aw_lib_id = None
        self._region = None
        self._return_type = None
        self._root_id = None
        self._source = None
        self._special_type = None
        self._tmss_case_number = None
        self._tmss_case_id = None
        self._total_page = None
        self._total_size = None
        self._update_time = None
        self._update_time_stamp = None
        self._update_time_string = None
        self._update_user = None
        self._warning_msg = None
        self._yaml_name = None
        self.discriminator = None

        if aw_code is not None:
            self.aw_code = aw_code
        if aw_description is not None:
            self.aw_description = aw_description
        if aw_ins_list is not None:
            self.aw_ins_list = aw_ins_list
        if aw_mark is not None:
            self.aw_mark = aw_mark
        if aw_operationid is not None:
            self.aw_operationid = aw_operationid
        if aw_tags is not None:
            self.aw_tags = aw_tags
        if aw_type is not None:
            self.aw_type = aw_type
        if aw_uniqueid is not None:
            self.aw_uniqueid = aw_uniqueid
        if by_order is not None:
            self.by_order = by_order
        if cata_type is not None:
            self.cata_type = cata_type
        if child_list is not None:
            self.child_list = child_list
        if create_time is not None:
            self.create_time = create_time
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if create_time_string is not None:
            self.create_time_string = create_time_string
        if create_user is not None:
            self.create_user = create_user
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if custom_aw_libs is not None:
            self.custom_aw_libs = custom_aw_libs
        if delete_time is not None:
            self.delete_time = delete_time
        if delete_user is not None:
            self.delete_user = delete_user
        if description is not None:
            self.description = description
        if dft_check_point_list is not None:
            self.dft_check_point_list = dft_check_point_list
        if dft_custom_header is not None:
            self.dft_custom_header = dft_custom_header
        if dft_retry_interval is not None:
            self.dft_retry_interval = dft_retry_interval
        if dft_retry_times is not None:
            self.dft_retry_times = dft_retry_times
        if dft_variable_list is not None:
            self.dft_variable_list = dft_variable_list
        if extra_info is not None:
            self.extra_info = extra_info
        if group_name is not None:
            self.group_name = group_name
        if has_code is not None:
            self.has_code = has_code
        if id is not None:
            self.id = id
        if import_package is not None:
            self.import_package = import_package
        if interface_label is not None:
            self.interface_label = interface_label
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if is_folder is not None:
            self.is_folder = is_folder
        if keyword_variable_value is not None:
            self.keyword_variable_value = keyword_variable_value
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if name_view is not None:
            self.name_view = name_view
        if origin_project is not None:
            self.origin_project = origin_project
        if output_param_list is not None:
            self.output_param_list = output_param_list
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if param_type_and_dft_value is not None:
            self.param_type_and_dft_value = param_type_and_dft_value
        if parent_id is not None:
            self.parent_id = parent_id
        if project_id is not None:
            self.project_id = project_id
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if public_aw_lib is not None:
            self.public_aw_lib = public_aw_lib
        if public_aw_lib_id is not None:
            self.public_aw_lib_id = public_aw_lib_id
        if region is not None:
            self.region = region
        if return_type is not None:
            self.return_type = return_type
        if root_id is not None:
            self.root_id = root_id
        if source is not None:
            self.source = source
        if special_type is not None:
            self.special_type = special_type
        if tmss_case_number is not None:
            self.tmss_case_number = tmss_case_number
        if tmss_case_id is not None:
            self.tmss_case_id = tmss_case_id
        if total_page is not None:
            self.total_page = total_page
        if total_size is not None:
            self.total_size = total_size
        if update_time is not None:
            self.update_time = update_time
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp
        if update_time_string is not None:
            self.update_time_string = update_time_string
        if update_user is not None:
            self.update_user = update_user
        if warning_msg is not None:
            self.warning_msg = warning_msg
        if yaml_name is not None:
            self.yaml_name = yaml_name

    @property
    def aw_code(self):
        """Gets the aw_code of this BasicAWInfo.

        aw代码, hasCode为1时有效

        :return: The aw_code of this BasicAWInfo.
        :rtype: str
        """
        return self._aw_code

    @aw_code.setter
    def aw_code(self, aw_code):
        """Sets the aw_code of this BasicAWInfo.

        aw代码, hasCode为1时有效

        :param aw_code: The aw_code of this BasicAWInfo.
        :type aw_code: str
        """
        self._aw_code = aw_code

    @property
    def aw_description(self):
        """Gets the aw_description of this BasicAWInfo.

        模板描述

        :return: The aw_description of this BasicAWInfo.
        :rtype: str
        """
        return self._aw_description

    @aw_description.setter
    def aw_description(self, aw_description):
        """Sets the aw_description of this BasicAWInfo.

        模板描述

        :param aw_description: The aw_description of this BasicAWInfo.
        :type aw_description: str
        """
        self._aw_description = aw_description

    @property
    def aw_ins_list(self):
        """Gets the aw_ins_list of this BasicAWInfo.

        组合aw包含的aw实例信息，awType为2时该字段有效

        :return: The aw_ins_list of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwInstanceRes`]
        """
        return self._aw_ins_list

    @aw_ins_list.setter
    def aw_ins_list(self, aw_ins_list):
        """Sets the aw_ins_list of this BasicAWInfo.

        组合aw包含的aw实例信息，awType为2时该字段有效

        :param aw_ins_list: The aw_ins_list of this BasicAWInfo.
        :type aw_ins_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstanceRes`]
        """
        self._aw_ins_list = aw_ins_list

    @property
    def aw_mark(self):
        """Gets the aw_mark of this BasicAWInfo.

        aw标记 0-normal；1-new；2-update 3-delete

        :return: The aw_mark of this BasicAWInfo.
        :rtype: int
        """
        return self._aw_mark

    @aw_mark.setter
    def aw_mark(self, aw_mark):
        """Sets the aw_mark of this BasicAWInfo.

        aw标记 0-normal；1-new；2-update 3-delete

        :param aw_mark: The aw_mark of this BasicAWInfo.
        :type aw_mark: int
        """
        self._aw_mark = aw_mark

    @property
    def aw_operationid(self):
        """Gets the aw_operationid of this BasicAWInfo.

        接口的operationId

        :return: The aw_operationid of this BasicAWInfo.
        :rtype: str
        """
        return self._aw_operationid

    @aw_operationid.setter
    def aw_operationid(self, aw_operationid):
        """Sets the aw_operationid of this BasicAWInfo.

        接口的operationId

        :param aw_operationid: The aw_operationid of this BasicAWInfo.
        :type aw_operationid: str
        """
        self._aw_operationid = aw_operationid

    @property
    def aw_tags(self):
        """Gets the aw_tags of this BasicAWInfo.

        接口的tags

        :return: The aw_tags of this BasicAWInfo.
        :rtype: str
        """
        return self._aw_tags

    @aw_tags.setter
    def aw_tags(self, aw_tags):
        """Sets the aw_tags of this BasicAWInfo.

        接口的tags

        :param aw_tags: The aw_tags of this BasicAWInfo.
        :type aw_tags: str
        """
        self._aw_tags = aw_tags

    @property
    def aw_type(self):
        """Gets the aw_type of this BasicAWInfo.

        AW类型1-普通aw,2-组合aw,3-导入aw

        :return: The aw_type of this BasicAWInfo.
        :rtype: int
        """
        return self._aw_type

    @aw_type.setter
    def aw_type(self, aw_type):
        """Sets the aw_type of this BasicAWInfo.

        AW类型1-普通aw,2-组合aw,3-导入aw

        :param aw_type: The aw_type of this BasicAWInfo.
        :type aw_type: int
        """
        self._aw_type = aw_type

    @property
    def aw_uniqueid(self):
        """Gets the aw_uniqueid of this BasicAWInfo.

        awOperationId_awTags的拼接

        :return: The aw_uniqueid of this BasicAWInfo.
        :rtype: str
        """
        return self._aw_uniqueid

    @aw_uniqueid.setter
    def aw_uniqueid(self, aw_uniqueid):
        """Sets the aw_uniqueid of this BasicAWInfo.

        awOperationId_awTags的拼接

        :param aw_uniqueid: The aw_uniqueid of this BasicAWInfo.
        :type aw_uniqueid: str
        """
        self._aw_uniqueid = aw_uniqueid

    @property
    def by_order(self):
        """Gets the by_order of this BasicAWInfo.

        顺序

        :return: The by_order of this BasicAWInfo.
        :rtype: int
        """
        return self._by_order

    @by_order.setter
    def by_order(self, by_order):
        """Sets the by_order of this BasicAWInfo.

        顺序

        :param by_order: The by_order of this BasicAWInfo.
        :type by_order: int
        """
        self._by_order = by_order

    @property
    def cata_type(self):
        """Gets the cata_type of this BasicAWInfo.

        目录层级

        :return: The cata_type of this BasicAWInfo.
        :rtype: int
        """
        return self._cata_type

    @cata_type.setter
    def cata_type(self, cata_type):
        """Sets the cata_type of this BasicAWInfo.

        目录层级

        :param cata_type: The cata_type of this BasicAWInfo.
        :type cata_type: int
        """
        self._cata_type = cata_type

    @property
    def child_list(self):
        """Gets the child_list of this BasicAWInfo.

        新增childList以支持嵌套层级结构

        :return: The child_list of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.BasicAWInfo`]
        """
        return self._child_list

    @child_list.setter
    def child_list(self, child_list):
        """Sets the child_list of this BasicAWInfo.

        新增childList以支持嵌套层级结构

        :param child_list: The child_list of this BasicAWInfo.
        :type child_list: list[:class:`huaweicloudsdkcloudtest.v1.BasicAWInfo`]
        """
        self._child_list = child_list

    @property
    def create_time(self):
        """Gets the create_time of this BasicAWInfo.

        创建时间

        :return: The create_time of this BasicAWInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BasicAWInfo.

        创建时间

        :param create_time: The create_time of this BasicAWInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_time_stamp(self):
        """Gets the create_time_stamp of this BasicAWInfo.

        时间戳字段

        :return: The create_time_stamp of this BasicAWInfo.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        """Sets the create_time_stamp of this BasicAWInfo.

        时间戳字段

        :param create_time_stamp: The create_time_stamp of this BasicAWInfo.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def create_time_string(self):
        """Gets the create_time_string of this BasicAWInfo.

        时间字符串

        :return: The create_time_string of this BasicAWInfo.
        :rtype: str
        """
        return self._create_time_string

    @create_time_string.setter
    def create_time_string(self, create_time_string):
        """Sets the create_time_string of this BasicAWInfo.

        时间字符串

        :param create_time_string: The create_time_string of this BasicAWInfo.
        :type create_time_string: str
        """
        self._create_time_string = create_time_string

    @property
    def create_user(self):
        """Gets the create_user of this BasicAWInfo.

        创建人

        :return: The create_user of this BasicAWInfo.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this BasicAWInfo.

        创建人

        :param create_user: The create_user of this BasicAWInfo.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_user_id(self):
        """Gets the create_user_id of this BasicAWInfo.

        创建人id

        :return: The create_user_id of this BasicAWInfo.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        """Sets the create_user_id of this BasicAWInfo.

        创建人id

        :param create_user_id: The create_user_id of this BasicAWInfo.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def custom_aw_libs(self):
        """Gets the custom_aw_libs of this BasicAWInfo.

        aw库的文件列表

        :return: The custom_aw_libs of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.UploadFileRes`]
        """
        return self._custom_aw_libs

    @custom_aw_libs.setter
    def custom_aw_libs(self, custom_aw_libs):
        """Sets the custom_aw_libs of this BasicAWInfo.

        aw库的文件列表

        :param custom_aw_libs: The custom_aw_libs of this BasicAWInfo.
        :type custom_aw_libs: list[:class:`huaweicloudsdkcloudtest.v1.UploadFileRes`]
        """
        self._custom_aw_libs = custom_aw_libs

    @property
    def delete_time(self):
        """Gets the delete_time of this BasicAWInfo.

        更新时间

        :return: The delete_time of this BasicAWInfo.
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this BasicAWInfo.

        更新时间

        :param delete_time: The delete_time of this BasicAWInfo.
        :type delete_time: str
        """
        self._delete_time = delete_time

    @property
    def delete_user(self):
        """Gets the delete_user of this BasicAWInfo.

        删除人

        :return: The delete_user of this BasicAWInfo.
        :rtype: str
        """
        return self._delete_user

    @delete_user.setter
    def delete_user(self, delete_user):
        """Sets the delete_user of this BasicAWInfo.

        删除人

        :param delete_user: The delete_user of this BasicAWInfo.
        :type delete_user: str
        """
        self._delete_user = delete_user

    @property
    def description(self):
        """Gets the description of this BasicAWInfo.

        描述

        :return: The description of this BasicAWInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BasicAWInfo.

        描述

        :param description: The description of this BasicAWInfo.
        :type description: str
        """
        self._description = description

    @property
    def dft_check_point_list(self):
        """Gets the dft_check_point_list of this BasicAWInfo.

        默认检查点List

        :return: The dft_check_point_list of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        return self._dft_check_point_list

    @dft_check_point_list.setter
    def dft_check_point_list(self, dft_check_point_list):
        """Sets the dft_check_point_list of this BasicAWInfo.

        默认检查点List

        :param dft_check_point_list: The dft_check_point_list of this BasicAWInfo.
        :type dft_check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        self._dft_check_point_list = dft_check_point_list

    @property
    def dft_custom_header(self):
        """Gets the dft_custom_header of this BasicAWInfo.

        默认请求头参数对象

        :return: The dft_custom_header of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._dft_custom_header

    @dft_custom_header.setter
    def dft_custom_header(self, dft_custom_header):
        """Sets the dft_custom_header of this BasicAWInfo.

        默认请求头参数对象

        :param dft_custom_header: The dft_custom_header of this BasicAWInfo.
        :type dft_custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._dft_custom_header = dft_custom_header

    @property
    def dft_retry_interval(self):
        """Gets the dft_retry_interval of this BasicAWInfo.

        重试间隔时间 (ms) 为空表示不等待

        :return: The dft_retry_interval of this BasicAWInfo.
        :rtype: str
        """
        return self._dft_retry_interval

    @dft_retry_interval.setter
    def dft_retry_interval(self, dft_retry_interval):
        """Sets the dft_retry_interval of this BasicAWInfo.

        重试间隔时间 (ms) 为空表示不等待

        :param dft_retry_interval: The dft_retry_interval of this BasicAWInfo.
        :type dft_retry_interval: str
        """
        self._dft_retry_interval = dft_retry_interval

    @property
    def dft_retry_times(self):
        """Gets the dft_retry_times of this BasicAWInfo.

        重试次数

        :return: The dft_retry_times of this BasicAWInfo.
        :rtype: str
        """
        return self._dft_retry_times

    @dft_retry_times.setter
    def dft_retry_times(self, dft_retry_times):
        """Sets the dft_retry_times of this BasicAWInfo.

        重试次数

        :param dft_retry_times: The dft_retry_times of this BasicAWInfo.
        :type dft_retry_times: str
        """
        self._dft_retry_times = dft_retry_times

    @property
    def dft_variable_list(self):
        """Gets the dft_variable_list of this BasicAWInfo.

        默认变量信息List

        :return: The dft_variable_list of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._dft_variable_list

    @dft_variable_list.setter
    def dft_variable_list(self, dft_variable_list):
        """Sets the dft_variable_list of this BasicAWInfo.

        默认变量信息List

        :param dft_variable_list: The dft_variable_list of this BasicAWInfo.
        :type dft_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._dft_variable_list = dft_variable_list

    @property
    def extra_info(self):
        """Gets the extra_info of this BasicAWInfo.

        :return: The extra_info of this BasicAWInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.JsonNode`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this BasicAWInfo.

        :param extra_info: The extra_info of this BasicAWInfo.
        :type extra_info: :class:`huaweicloudsdkcloudtest.v1.JsonNode`
        """
        self._extra_info = extra_info

    @property
    def group_name(self):
        """Gets the group_name of this BasicAWInfo.

        组名

        :return: The group_name of this BasicAWInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this BasicAWInfo.

        组名

        :param group_name: The group_name of this BasicAWInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def has_code(self):
        """Gets the has_code of this BasicAWInfo.

        是否自带代码 0-不自带代码，该aw依赖source字段中的源；1-自带代码

        :return: The has_code of this BasicAWInfo.
        :rtype: int
        """
        return self._has_code

    @has_code.setter
    def has_code(self, has_code):
        """Sets the has_code of this BasicAWInfo.

        是否自带代码 0-不自带代码，该aw依赖source字段中的源；1-自带代码

        :param has_code: The has_code of this BasicAWInfo.
        :type has_code: int
        """
        self._has_code = has_code

    @property
    def id(self):
        """Gets the id of this BasicAWInfo.

        id

        :return: The id of this BasicAWInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicAWInfo.

        id

        :param id: The id of this BasicAWInfo.
        :type id: str
        """
        self._id = id

    @property
    def import_package(self):
        """Gets the import_package of this BasicAWInfo.

        导入的包

        :return: The import_package of this BasicAWInfo.
        :rtype: list[str]
        """
        return self._import_package

    @import_package.setter
    def import_package(self, import_package):
        """Sets the import_package of this BasicAWInfo.

        导入的包

        :param import_package: The import_package of this BasicAWInfo.
        :type import_package: list[str]
        """
        self._import_package = import_package

    @property
    def interface_label(self):
        """Gets the interface_label of this BasicAWInfo.

        接口的x-extend

        :return: The interface_label of this BasicAWInfo.
        :rtype: str
        """
        return self._interface_label

    @interface_label.setter
    def interface_label(self, interface_label):
        """Sets the interface_label of this BasicAWInfo.

        接口的x-extend

        :param interface_label: The interface_label of this BasicAWInfo.
        :type interface_label: str
        """
        self._interface_label = interface_label

    @property
    def is_favorite(self):
        """Gets the is_favorite of this BasicAWInfo.

        是否是当前工程的收藏aw，该字段不存数据库，每次获取时实时判断

        :return: The is_favorite of this BasicAWInfo.
        :rtype: int
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this BasicAWInfo.

        是否是当前工程的收藏aw，该字段不存数据库，每次获取时实时判断

        :param is_favorite: The is_favorite of this BasicAWInfo.
        :type is_favorite: int
        """
        self._is_favorite = is_favorite

    @property
    def is_folder(self):
        """Gets the is_folder of this BasicAWInfo.

        判断是否为文件夹的标识

        :return: The is_folder of this BasicAWInfo.
        :rtype: str
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder):
        """Sets the is_folder of this BasicAWInfo.

        判断是否为文件夹的标识

        :param is_folder: The is_folder of this BasicAWInfo.
        :type is_folder: str
        """
        self._is_folder = is_folder

    @property
    def keyword_variable_value(self):
        """Gets the keyword_variable_value of this BasicAWInfo.

        关键字局部变量

        :return: The keyword_variable_value of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._keyword_variable_value

    @keyword_variable_value.setter
    def keyword_variable_value(self, keyword_variable_value):
        """Sets the keyword_variable_value of this BasicAWInfo.

        关键字局部变量

        :param keyword_variable_value: The keyword_variable_value of this BasicAWInfo.
        :type keyword_variable_value: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._keyword_variable_value = keyword_variable_value

    @property
    def method(self):
        """Gets the method of this BasicAWInfo.

        方法

        :return: The method of this BasicAWInfo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this BasicAWInfo.

        方法

        :param method: The method of this BasicAWInfo.
        :type method: str
        """
        self._method = method

    @property
    def name(self):
        """Gets the name of this BasicAWInfo.

        名称

        :return: The name of this BasicAWInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicAWInfo.

        名称

        :param name: The name of this BasicAWInfo.
        :type name: str
        """
        self._name = name

    @property
    def name_view(self):
        """Gets the name_view of this BasicAWInfo.

        aw在页面上显示的名字

        :return: The name_view of this BasicAWInfo.
        :rtype: str
        """
        return self._name_view

    @name_view.setter
    def name_view(self, name_view):
        """Sets the name_view of this BasicAWInfo.

        aw在页面上显示的名字

        :param name_view: The name_view of this BasicAWInfo.
        :type name_view: str
        """
        self._name_view = name_view

    @property
    def origin_project(self):
        """Gets the origin_project of this BasicAWInfo.

        源工程信息，如果该aw是从其他工程过来的(继承或者copy to local)

        :return: The origin_project of this BasicAWInfo.
        :rtype: str
        """
        return self._origin_project

    @origin_project.setter
    def origin_project(self, origin_project):
        """Sets the origin_project of this BasicAWInfo.

        源工程信息，如果该aw是从其他工程过来的(继承或者copy to local)

        :param origin_project: The origin_project of this BasicAWInfo.
        :type origin_project: str
        """
        self._origin_project = origin_project

    @property
    def output_param_list(self):
        """Gets the output_param_list of this BasicAWInfo.

        组合aw的输出参数信息，该字段不存数据库，实时获取

        :return: The output_param_list of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._output_param_list

    @output_param_list.setter
    def output_param_list(self, output_param_list):
        """Sets the output_param_list of this BasicAWInfo.

        组合aw的输出参数信息，该字段不存数据库，实时获取

        :param output_param_list: The output_param_list of this BasicAWInfo.
        :type output_param_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._output_param_list = output_param_list

    @property
    def page_no(self):
        """Gets the page_no of this BasicAWInfo.

        当前页数

        :return: The page_no of this BasicAWInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this BasicAWInfo.

        当前页数

        :param page_no: The page_no of this BasicAWInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this BasicAWInfo.

        每页条数

        :return: The page_size of this BasicAWInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this BasicAWInfo.

        每页条数

        :param page_size: The page_size of this BasicAWInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def param_type_and_dft_value(self):
        """Gets the param_type_and_dft_value of this BasicAWInfo.

        参数类型和参数默认值对应List

        :return: The param_type_and_dft_value of this BasicAWInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._param_type_and_dft_value

    @param_type_and_dft_value.setter
    def param_type_and_dft_value(self, param_type_and_dft_value):
        """Sets the param_type_and_dft_value of this BasicAWInfo.

        参数类型和参数默认值对应List

        :param param_type_and_dft_value: The param_type_and_dft_value of this BasicAWInfo.
        :type param_type_and_dft_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._param_type_and_dft_value = param_type_and_dft_value

    @property
    def parent_id(self):
        """Gets the parent_id of this BasicAWInfo.

        aw目录父编号

        :return: The parent_id of this BasicAWInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BasicAWInfo.

        aw目录父编号

        :param parent_id: The parent_id of this BasicAWInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def project_id(self):
        """Gets the project_id of this BasicAWInfo.

        aw目录父编号

        :return: The project_id of this BasicAWInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BasicAWInfo.

        aw目录父编号

        :param project_id: The project_id of this BasicAWInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol_type(self):
        """Gets the protocol_type of this BasicAWInfo.

        协议类型 (http/dsf/other)

        :return: The protocol_type of this BasicAWInfo.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this BasicAWInfo.

        协议类型 (http/dsf/other)

        :param protocol_type: The protocol_type of this BasicAWInfo.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def public_aw_lib(self):
        """Gets the public_aw_lib of this BasicAWInfo.

        :return: The public_aw_lib of this BasicAWInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.PublicAwLibRes`
        """
        return self._public_aw_lib

    @public_aw_lib.setter
    def public_aw_lib(self, public_aw_lib):
        """Sets the public_aw_lib of this BasicAWInfo.

        :param public_aw_lib: The public_aw_lib of this BasicAWInfo.
        :type public_aw_lib: :class:`huaweicloudsdkcloudtest.v1.PublicAwLibRes`
        """
        self._public_aw_lib = public_aw_lib

    @property
    def public_aw_lib_id(self):
        """Gets the public_aw_lib_id of this BasicAWInfo.

        所属公共aw库Id

        :return: The public_aw_lib_id of this BasicAWInfo.
        :rtype: str
        """
        return self._public_aw_lib_id

    @public_aw_lib_id.setter
    def public_aw_lib_id(self, public_aw_lib_id):
        """Sets the public_aw_lib_id of this BasicAWInfo.

        所属公共aw库Id

        :param public_aw_lib_id: The public_aw_lib_id of this BasicAWInfo.
        :type public_aw_lib_id: str
        """
        self._public_aw_lib_id = public_aw_lib_id

    @property
    def region(self):
        """Gets the region of this BasicAWInfo.

        区域名称

        :return: The region of this BasicAWInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BasicAWInfo.

        区域名称

        :param region: The region of this BasicAWInfo.
        :type region: str
        """
        self._region = region

    @property
    def return_type(self):
        """Gets the return_type of this BasicAWInfo.

        返回类型

        :return: The return_type of this BasicAWInfo.
        :rtype: str
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets the return_type of this BasicAWInfo.

        返回类型

        :param return_type: The return_type of this BasicAWInfo.
        :type return_type: str
        """
        self._return_type = return_type

    @property
    def root_id(self):
        """Gets the root_id of this BasicAWInfo.

        root id

        :return: The root_id of this BasicAWInfo.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this BasicAWInfo.

        root id

        :param root_id: The root_id of this BasicAWInfo.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def source(self):
        """Gets the source of this BasicAWInfo.

        来源

        :return: The source of this BasicAWInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BasicAWInfo.

        来源

        :param source: The source of this BasicAWInfo.
        :type source: str
        """
        self._source = source

    @property
    def special_type(self):
        """Gets the special_type of this BasicAWInfo.

        特殊AW类型 0-common,10-header,1-beforeHeader

        :return: The special_type of this BasicAWInfo.
        :rtype: int
        """
        return self._special_type

    @special_type.setter
    def special_type(self, special_type):
        """Sets the special_type of this BasicAWInfo.

        特殊AW类型 0-common,10-header,1-beforeHeader

        :param special_type: The special_type of this BasicAWInfo.
        :type special_type: int
        """
        self._special_type = special_type

    @property
    def tmss_case_number(self):
        """Gets the tmss_case_number of this BasicAWInfo.

        关键字管理的用例编号

        :return: The tmss_case_number of this BasicAWInfo.
        :rtype: str
        """
        return self._tmss_case_number

    @tmss_case_number.setter
    def tmss_case_number(self, tmss_case_number):
        """Sets the tmss_case_number of this BasicAWInfo.

        关键字管理的用例编号

        :param tmss_case_number: The tmss_case_number of this BasicAWInfo.
        :type tmss_case_number: str
        """
        self._tmss_case_number = tmss_case_number

    @property
    def tmss_case_id(self):
        """Gets the tmss_case_id of this BasicAWInfo.

        关键字aw管理的用例ID

        :return: The tmss_case_id of this BasicAWInfo.
        :rtype: str
        """
        return self._tmss_case_id

    @tmss_case_id.setter
    def tmss_case_id(self, tmss_case_id):
        """Sets the tmss_case_id of this BasicAWInfo.

        关键字aw管理的用例ID

        :param tmss_case_id: The tmss_case_id of this BasicAWInfo.
        :type tmss_case_id: str
        """
        self._tmss_case_id = tmss_case_id

    @property
    def total_page(self):
        """Gets the total_page of this BasicAWInfo.

        总页数

        :return: The total_page of this BasicAWInfo.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this BasicAWInfo.

        总页数

        :param total_page: The total_page of this BasicAWInfo.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def total_size(self):
        """Gets the total_size of this BasicAWInfo.

        总条数

        :return: The total_size of this BasicAWInfo.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this BasicAWInfo.

        总条数

        :param total_size: The total_size of this BasicAWInfo.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def update_time(self):
        """Gets the update_time of this BasicAWInfo.

        更新时间

        :return: The update_time of this BasicAWInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BasicAWInfo.

        更新时间

        :param update_time: The update_time of this BasicAWInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_time_stamp(self):
        """Gets the update_time_stamp of this BasicAWInfo.

        更新时间戳

        :return: The update_time_stamp of this BasicAWInfo.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        """Sets the update_time_stamp of this BasicAWInfo.

        更新时间戳

        :param update_time_stamp: The update_time_stamp of this BasicAWInfo.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

    @property
    def update_time_string(self):
        """Gets the update_time_string of this BasicAWInfo.

        更新字符串

        :return: The update_time_string of this BasicAWInfo.
        :rtype: str
        """
        return self._update_time_string

    @update_time_string.setter
    def update_time_string(self, update_time_string):
        """Sets the update_time_string of this BasicAWInfo.

        更新字符串

        :param update_time_string: The update_time_string of this BasicAWInfo.
        :type update_time_string: str
        """
        self._update_time_string = update_time_string

    @property
    def update_user(self):
        """Gets the update_user of this BasicAWInfo.

        更新人

        :return: The update_user of this BasicAWInfo.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this BasicAWInfo.

        更新人

        :param update_user: The update_user of this BasicAWInfo.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def warning_msg(self):
        """Gets the warning_msg of this BasicAWInfo.

        警告信息

        :return: The warning_msg of this BasicAWInfo.
        :rtype: str
        """
        return self._warning_msg

    @warning_msg.setter
    def warning_msg(self, warning_msg):
        """Sets the warning_msg of this BasicAWInfo.

        警告信息

        :param warning_msg: The warning_msg of this BasicAWInfo.
        :type warning_msg: str
        """
        self._warning_msg = warning_msg

    @property
    def yaml_name(self):
        """Gets the yaml_name of this BasicAWInfo.

        所属yaml文件名称,该字段不存库，用来记录从哪个yaml文件导入

        :return: The yaml_name of this BasicAWInfo.
        :rtype: str
        """
        return self._yaml_name

    @yaml_name.setter
    def yaml_name(self, yaml_name):
        """Sets the yaml_name of this BasicAWInfo.

        所属yaml文件名称,该字段不存库，用来记录从哪个yaml文件导入

        :param yaml_name: The yaml_name of this BasicAWInfo.
        :type yaml_name: str
        """
        self._yaml_name = yaml_name

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
        if not isinstance(other, BasicAWInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
