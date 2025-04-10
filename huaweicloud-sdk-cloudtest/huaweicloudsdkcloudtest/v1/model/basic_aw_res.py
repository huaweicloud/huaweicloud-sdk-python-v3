# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicAwRes:

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
        'aw_mark': 'int',
        'aw_operationid': 'str',
        'aw_tags': 'str',
        'aw_type': 'int',
        'aw_uniqueid': 'str',
        'by_order': 'int',
        'create_time': 'str',
        'create_time_stamp': 'int',
        'create_time_string': 'str',
        'create_user': 'str',
        'create_user_id': 'str',
        'delete_time': 'str',
        'delete_user': 'str',
        'description': 'str',
        'dft_check_point_list': 'list[object]',
        'dft_custom_header': 'list[object]',
        'dft_retry_interval': 'str',
        'dft_retry_times': 'str',
        'dft_variable_list': 'list[object]',
        'extra_info': 'object',
        'group_name': 'str',
        'has_code': 'int',
        'id': 'str',
        'import_package': 'list[str]',
        'interface_label': 'str',
        'is_favorite': 'int',
        'method': 'str',
        'name': 'str',
        'name_view': 'str',
        'origin_project': 'str',
        'param_type_and_dft_value': 'list[object]',
        'project_id': 'str',
        'protocol_type': 'str',
        'public_aw_lib': 'object',
        'public_aw_lib_id': 'str',
        'region': 'str',
        'return_type': 'str',
        'root_id': 'str',
        'source': 'str',
        'special_type': 'int',
        'tmss_case_number': 'str',
        'tmss_case_id': 'str',
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
        'aw_mark': 'aw_mark',
        'aw_operationid': 'aw_operationid',
        'aw_tags': 'aw_tags',
        'aw_type': 'aw_type',
        'aw_uniqueid': 'aw_uniqueid',
        'by_order': 'by_order',
        'create_time': 'create_time',
        'create_time_stamp': 'create_time_stamp',
        'create_time_string': 'create_time_string',
        'create_user': 'create_user',
        'create_user_id': 'create_user_id',
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
        'method': 'method',
        'name': 'name',
        'name_view': 'nameView',
        'origin_project': 'origin_project',
        'param_type_and_dft_value': 'param_type_and_dft_value',
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
        'update_time': 'update_time',
        'update_time_stamp': 'update_time_stamp',
        'update_time_string': 'update_time_string',
        'update_user': 'update_user',
        'warning_msg': 'warningMsg',
        'yaml_name': 'yamlName'
    }

    def __init__(self, aw_code=None, aw_description=None, aw_mark=None, aw_operationid=None, aw_tags=None, aw_type=None, aw_uniqueid=None, by_order=None, create_time=None, create_time_stamp=None, create_time_string=None, create_user=None, create_user_id=None, delete_time=None, delete_user=None, description=None, dft_check_point_list=None, dft_custom_header=None, dft_retry_interval=None, dft_retry_times=None, dft_variable_list=None, extra_info=None, group_name=None, has_code=None, id=None, import_package=None, interface_label=None, is_favorite=None, method=None, name=None, name_view=None, origin_project=None, param_type_and_dft_value=None, project_id=None, protocol_type=None, public_aw_lib=None, public_aw_lib_id=None, region=None, return_type=None, root_id=None, source=None, special_type=None, tmss_case_number=None, tmss_case_id=None, update_time=None, update_time_stamp=None, update_time_string=None, update_user=None, warning_msg=None, yaml_name=None):
        r"""BasicAwRes

        The model defined in huaweicloud sdk

        :param aw_code: 
        :type aw_code: str
        :param aw_description: 
        :type aw_description: str
        :param aw_mark: 
        :type aw_mark: int
        :param aw_operationid: 
        :type aw_operationid: str
        :param aw_tags: 
        :type aw_tags: str
        :param aw_type: 
        :type aw_type: int
        :param aw_uniqueid: 
        :type aw_uniqueid: str
        :param by_order: 
        :type by_order: int
        :param create_time: 创建时间
        :type create_time: str
        :param create_time_stamp: 
        :type create_time_stamp: int
        :param create_time_string: 
        :type create_time_string: str
        :param create_user: 创建人
        :type create_user: str
        :param create_user_id: 
        :type create_user_id: str
        :param delete_time: 更新时间
        :type delete_time: str
        :param delete_user: 删除人
        :type delete_user: str
        :param description: 
        :type description: str
        :param dft_check_point_list: 
        :type dft_check_point_list: list[object]
        :param dft_custom_header: 
        :type dft_custom_header: list[object]
        :param dft_retry_interval: 
        :type dft_retry_interval: str
        :param dft_retry_times: 
        :type dft_retry_times: str
        :param dft_variable_list: 
        :type dft_variable_list: list[object]
        :param extra_info: 
        :type extra_info: object
        :param group_name: 
        :type group_name: str
        :param has_code: 
        :type has_code: int
        :param id: id
        :type id: str
        :param import_package: 
        :type import_package: list[str]
        :param interface_label: 
        :type interface_label: str
        :param is_favorite: 
        :type is_favorite: int
        :param method: 
        :type method: str
        :param name: 
        :type name: str
        :param name_view: 
        :type name_view: str
        :param origin_project: 
        :type origin_project: str
        :param param_type_and_dft_value: 
        :type param_type_and_dft_value: list[object]
        :param project_id: 
        :type project_id: str
        :param protocol_type: 
        :type protocol_type: str
        :param public_aw_lib: 
        :type public_aw_lib: object
        :param public_aw_lib_id: 
        :type public_aw_lib_id: str
        :param region: 
        :type region: str
        :param return_type: 
        :type return_type: str
        :param root_id: 
        :type root_id: str
        :param source: 
        :type source: str
        :param special_type: 
        :type special_type: int
        :param tmss_case_number: 
        :type tmss_case_number: str
        :param tmss_case_id: 
        :type tmss_case_id: str
        :param update_time: 更新时间
        :type update_time: str
        :param update_time_stamp: 
        :type update_time_stamp: int
        :param update_time_string: 
        :type update_time_string: str
        :param update_user: 更新人
        :type update_user: str
        :param warning_msg: 
        :type warning_msg: str
        :param yaml_name: 
        :type yaml_name: str
        """
        
        

        self._aw_code = None
        self._aw_description = None
        self._aw_mark = None
        self._aw_operationid = None
        self._aw_tags = None
        self._aw_type = None
        self._aw_uniqueid = None
        self._by_order = None
        self._create_time = None
        self._create_time_stamp = None
        self._create_time_string = None
        self._create_user = None
        self._create_user_id = None
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
        self._method = None
        self._name = None
        self._name_view = None
        self._origin_project = None
        self._param_type_and_dft_value = None
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
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if name_view is not None:
            self.name_view = name_view
        if origin_project is not None:
            self.origin_project = origin_project
        if param_type_and_dft_value is not None:
            self.param_type_and_dft_value = param_type_and_dft_value
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
        r"""Gets the aw_code of this BasicAwRes.

        :return: The aw_code of this BasicAwRes.
        :rtype: str
        """
        return self._aw_code

    @aw_code.setter
    def aw_code(self, aw_code):
        r"""Sets the aw_code of this BasicAwRes.

        :param aw_code: The aw_code of this BasicAwRes.
        :type aw_code: str
        """
        self._aw_code = aw_code

    @property
    def aw_description(self):
        r"""Gets the aw_description of this BasicAwRes.

        :return: The aw_description of this BasicAwRes.
        :rtype: str
        """
        return self._aw_description

    @aw_description.setter
    def aw_description(self, aw_description):
        r"""Sets the aw_description of this BasicAwRes.

        :param aw_description: The aw_description of this BasicAwRes.
        :type aw_description: str
        """
        self._aw_description = aw_description

    @property
    def aw_mark(self):
        r"""Gets the aw_mark of this BasicAwRes.

        :return: The aw_mark of this BasicAwRes.
        :rtype: int
        """
        return self._aw_mark

    @aw_mark.setter
    def aw_mark(self, aw_mark):
        r"""Sets the aw_mark of this BasicAwRes.

        :param aw_mark: The aw_mark of this BasicAwRes.
        :type aw_mark: int
        """
        self._aw_mark = aw_mark

    @property
    def aw_operationid(self):
        r"""Gets the aw_operationid of this BasicAwRes.

        :return: The aw_operationid of this BasicAwRes.
        :rtype: str
        """
        return self._aw_operationid

    @aw_operationid.setter
    def aw_operationid(self, aw_operationid):
        r"""Sets the aw_operationid of this BasicAwRes.

        :param aw_operationid: The aw_operationid of this BasicAwRes.
        :type aw_operationid: str
        """
        self._aw_operationid = aw_operationid

    @property
    def aw_tags(self):
        r"""Gets the aw_tags of this BasicAwRes.

        :return: The aw_tags of this BasicAwRes.
        :rtype: str
        """
        return self._aw_tags

    @aw_tags.setter
    def aw_tags(self, aw_tags):
        r"""Sets the aw_tags of this BasicAwRes.

        :param aw_tags: The aw_tags of this BasicAwRes.
        :type aw_tags: str
        """
        self._aw_tags = aw_tags

    @property
    def aw_type(self):
        r"""Gets the aw_type of this BasicAwRes.

        :return: The aw_type of this BasicAwRes.
        :rtype: int
        """
        return self._aw_type

    @aw_type.setter
    def aw_type(self, aw_type):
        r"""Sets the aw_type of this BasicAwRes.

        :param aw_type: The aw_type of this BasicAwRes.
        :type aw_type: int
        """
        self._aw_type = aw_type

    @property
    def aw_uniqueid(self):
        r"""Gets the aw_uniqueid of this BasicAwRes.

        :return: The aw_uniqueid of this BasicAwRes.
        :rtype: str
        """
        return self._aw_uniqueid

    @aw_uniqueid.setter
    def aw_uniqueid(self, aw_uniqueid):
        r"""Sets the aw_uniqueid of this BasicAwRes.

        :param aw_uniqueid: The aw_uniqueid of this BasicAwRes.
        :type aw_uniqueid: str
        """
        self._aw_uniqueid = aw_uniqueid

    @property
    def by_order(self):
        r"""Gets the by_order of this BasicAwRes.

        :return: The by_order of this BasicAwRes.
        :rtype: int
        """
        return self._by_order

    @by_order.setter
    def by_order(self, by_order):
        r"""Sets the by_order of this BasicAwRes.

        :param by_order: The by_order of this BasicAwRes.
        :type by_order: int
        """
        self._by_order = by_order

    @property
    def create_time(self):
        r"""Gets the create_time of this BasicAwRes.

        创建时间

        :return: The create_time of this BasicAwRes.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BasicAwRes.

        创建时间

        :param create_time: The create_time of this BasicAwRes.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_time_stamp(self):
        r"""Gets the create_time_stamp of this BasicAwRes.

        :return: The create_time_stamp of this BasicAwRes.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        r"""Sets the create_time_stamp of this BasicAwRes.

        :param create_time_stamp: The create_time_stamp of this BasicAwRes.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def create_time_string(self):
        r"""Gets the create_time_string of this BasicAwRes.

        :return: The create_time_string of this BasicAwRes.
        :rtype: str
        """
        return self._create_time_string

    @create_time_string.setter
    def create_time_string(self, create_time_string):
        r"""Sets the create_time_string of this BasicAwRes.

        :param create_time_string: The create_time_string of this BasicAwRes.
        :type create_time_string: str
        """
        self._create_time_string = create_time_string

    @property
    def create_user(self):
        r"""Gets the create_user of this BasicAwRes.

        创建人

        :return: The create_user of this BasicAwRes.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this BasicAwRes.

        创建人

        :param create_user: The create_user of this BasicAwRes.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this BasicAwRes.

        :return: The create_user_id of this BasicAwRes.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this BasicAwRes.

        :param create_user_id: The create_user_id of this BasicAwRes.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def delete_time(self):
        r"""Gets the delete_time of this BasicAwRes.

        更新时间

        :return: The delete_time of this BasicAwRes.
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this BasicAwRes.

        更新时间

        :param delete_time: The delete_time of this BasicAwRes.
        :type delete_time: str
        """
        self._delete_time = delete_time

    @property
    def delete_user(self):
        r"""Gets the delete_user of this BasicAwRes.

        删除人

        :return: The delete_user of this BasicAwRes.
        :rtype: str
        """
        return self._delete_user

    @delete_user.setter
    def delete_user(self, delete_user):
        r"""Sets the delete_user of this BasicAwRes.

        删除人

        :param delete_user: The delete_user of this BasicAwRes.
        :type delete_user: str
        """
        self._delete_user = delete_user

    @property
    def description(self):
        r"""Gets the description of this BasicAwRes.

        :return: The description of this BasicAwRes.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BasicAwRes.

        :param description: The description of this BasicAwRes.
        :type description: str
        """
        self._description = description

    @property
    def dft_check_point_list(self):
        r"""Gets the dft_check_point_list of this BasicAwRes.

        :return: The dft_check_point_list of this BasicAwRes.
        :rtype: list[object]
        """
        return self._dft_check_point_list

    @dft_check_point_list.setter
    def dft_check_point_list(self, dft_check_point_list):
        r"""Sets the dft_check_point_list of this BasicAwRes.

        :param dft_check_point_list: The dft_check_point_list of this BasicAwRes.
        :type dft_check_point_list: list[object]
        """
        self._dft_check_point_list = dft_check_point_list

    @property
    def dft_custom_header(self):
        r"""Gets the dft_custom_header of this BasicAwRes.

        :return: The dft_custom_header of this BasicAwRes.
        :rtype: list[object]
        """
        return self._dft_custom_header

    @dft_custom_header.setter
    def dft_custom_header(self, dft_custom_header):
        r"""Sets the dft_custom_header of this BasicAwRes.

        :param dft_custom_header: The dft_custom_header of this BasicAwRes.
        :type dft_custom_header: list[object]
        """
        self._dft_custom_header = dft_custom_header

    @property
    def dft_retry_interval(self):
        r"""Gets the dft_retry_interval of this BasicAwRes.

        :return: The dft_retry_interval of this BasicAwRes.
        :rtype: str
        """
        return self._dft_retry_interval

    @dft_retry_interval.setter
    def dft_retry_interval(self, dft_retry_interval):
        r"""Sets the dft_retry_interval of this BasicAwRes.

        :param dft_retry_interval: The dft_retry_interval of this BasicAwRes.
        :type dft_retry_interval: str
        """
        self._dft_retry_interval = dft_retry_interval

    @property
    def dft_retry_times(self):
        r"""Gets the dft_retry_times of this BasicAwRes.

        :return: The dft_retry_times of this BasicAwRes.
        :rtype: str
        """
        return self._dft_retry_times

    @dft_retry_times.setter
    def dft_retry_times(self, dft_retry_times):
        r"""Sets the dft_retry_times of this BasicAwRes.

        :param dft_retry_times: The dft_retry_times of this BasicAwRes.
        :type dft_retry_times: str
        """
        self._dft_retry_times = dft_retry_times

    @property
    def dft_variable_list(self):
        r"""Gets the dft_variable_list of this BasicAwRes.

        :return: The dft_variable_list of this BasicAwRes.
        :rtype: list[object]
        """
        return self._dft_variable_list

    @dft_variable_list.setter
    def dft_variable_list(self, dft_variable_list):
        r"""Sets the dft_variable_list of this BasicAwRes.

        :param dft_variable_list: The dft_variable_list of this BasicAwRes.
        :type dft_variable_list: list[object]
        """
        self._dft_variable_list = dft_variable_list

    @property
    def extra_info(self):
        r"""Gets the extra_info of this BasicAwRes.

        :return: The extra_info of this BasicAwRes.
        :rtype: object
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this BasicAwRes.

        :param extra_info: The extra_info of this BasicAwRes.
        :type extra_info: object
        """
        self._extra_info = extra_info

    @property
    def group_name(self):
        r"""Gets the group_name of this BasicAwRes.

        :return: The group_name of this BasicAwRes.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this BasicAwRes.

        :param group_name: The group_name of this BasicAwRes.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def has_code(self):
        r"""Gets the has_code of this BasicAwRes.

        :return: The has_code of this BasicAwRes.
        :rtype: int
        """
        return self._has_code

    @has_code.setter
    def has_code(self, has_code):
        r"""Sets the has_code of this BasicAwRes.

        :param has_code: The has_code of this BasicAwRes.
        :type has_code: int
        """
        self._has_code = has_code

    @property
    def id(self):
        r"""Gets the id of this BasicAwRes.

        id

        :return: The id of this BasicAwRes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BasicAwRes.

        id

        :param id: The id of this BasicAwRes.
        :type id: str
        """
        self._id = id

    @property
    def import_package(self):
        r"""Gets the import_package of this BasicAwRes.

        :return: The import_package of this BasicAwRes.
        :rtype: list[str]
        """
        return self._import_package

    @import_package.setter
    def import_package(self, import_package):
        r"""Sets the import_package of this BasicAwRes.

        :param import_package: The import_package of this BasicAwRes.
        :type import_package: list[str]
        """
        self._import_package = import_package

    @property
    def interface_label(self):
        r"""Gets the interface_label of this BasicAwRes.

        :return: The interface_label of this BasicAwRes.
        :rtype: str
        """
        return self._interface_label

    @interface_label.setter
    def interface_label(self, interface_label):
        r"""Sets the interface_label of this BasicAwRes.

        :param interface_label: The interface_label of this BasicAwRes.
        :type interface_label: str
        """
        self._interface_label = interface_label

    @property
    def is_favorite(self):
        r"""Gets the is_favorite of this BasicAwRes.

        :return: The is_favorite of this BasicAwRes.
        :rtype: int
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        r"""Sets the is_favorite of this BasicAwRes.

        :param is_favorite: The is_favorite of this BasicAwRes.
        :type is_favorite: int
        """
        self._is_favorite = is_favorite

    @property
    def method(self):
        r"""Gets the method of this BasicAwRes.

        :return: The method of this BasicAwRes.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this BasicAwRes.

        :param method: The method of this BasicAwRes.
        :type method: str
        """
        self._method = method

    @property
    def name(self):
        r"""Gets the name of this BasicAwRes.

        :return: The name of this BasicAwRes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BasicAwRes.

        :param name: The name of this BasicAwRes.
        :type name: str
        """
        self._name = name

    @property
    def name_view(self):
        r"""Gets the name_view of this BasicAwRes.

        :return: The name_view of this BasicAwRes.
        :rtype: str
        """
        return self._name_view

    @name_view.setter
    def name_view(self, name_view):
        r"""Sets the name_view of this BasicAwRes.

        :param name_view: The name_view of this BasicAwRes.
        :type name_view: str
        """
        self._name_view = name_view

    @property
    def origin_project(self):
        r"""Gets the origin_project of this BasicAwRes.

        :return: The origin_project of this BasicAwRes.
        :rtype: str
        """
        return self._origin_project

    @origin_project.setter
    def origin_project(self, origin_project):
        r"""Sets the origin_project of this BasicAwRes.

        :param origin_project: The origin_project of this BasicAwRes.
        :type origin_project: str
        """
        self._origin_project = origin_project

    @property
    def param_type_and_dft_value(self):
        r"""Gets the param_type_and_dft_value of this BasicAwRes.

        :return: The param_type_and_dft_value of this BasicAwRes.
        :rtype: list[object]
        """
        return self._param_type_and_dft_value

    @param_type_and_dft_value.setter
    def param_type_and_dft_value(self, param_type_and_dft_value):
        r"""Sets the param_type_and_dft_value of this BasicAwRes.

        :param param_type_and_dft_value: The param_type_and_dft_value of this BasicAwRes.
        :type param_type_and_dft_value: list[object]
        """
        self._param_type_and_dft_value = param_type_and_dft_value

    @property
    def project_id(self):
        r"""Gets the project_id of this BasicAwRes.

        :return: The project_id of this BasicAwRes.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BasicAwRes.

        :param project_id: The project_id of this BasicAwRes.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this BasicAwRes.

        :return: The protocol_type of this BasicAwRes.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this BasicAwRes.

        :param protocol_type: The protocol_type of this BasicAwRes.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def public_aw_lib(self):
        r"""Gets the public_aw_lib of this BasicAwRes.

        :return: The public_aw_lib of this BasicAwRes.
        :rtype: object
        """
        return self._public_aw_lib

    @public_aw_lib.setter
    def public_aw_lib(self, public_aw_lib):
        r"""Sets the public_aw_lib of this BasicAwRes.

        :param public_aw_lib: The public_aw_lib of this BasicAwRes.
        :type public_aw_lib: object
        """
        self._public_aw_lib = public_aw_lib

    @property
    def public_aw_lib_id(self):
        r"""Gets the public_aw_lib_id of this BasicAwRes.

        :return: The public_aw_lib_id of this BasicAwRes.
        :rtype: str
        """
        return self._public_aw_lib_id

    @public_aw_lib_id.setter
    def public_aw_lib_id(self, public_aw_lib_id):
        r"""Sets the public_aw_lib_id of this BasicAwRes.

        :param public_aw_lib_id: The public_aw_lib_id of this BasicAwRes.
        :type public_aw_lib_id: str
        """
        self._public_aw_lib_id = public_aw_lib_id

    @property
    def region(self):
        r"""Gets the region of this BasicAwRes.

        :return: The region of this BasicAwRes.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this BasicAwRes.

        :param region: The region of this BasicAwRes.
        :type region: str
        """
        self._region = region

    @property
    def return_type(self):
        r"""Gets the return_type of this BasicAwRes.

        :return: The return_type of this BasicAwRes.
        :rtype: str
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        r"""Sets the return_type of this BasicAwRes.

        :param return_type: The return_type of this BasicAwRes.
        :type return_type: str
        """
        self._return_type = return_type

    @property
    def root_id(self):
        r"""Gets the root_id of this BasicAwRes.

        :return: The root_id of this BasicAwRes.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this BasicAwRes.

        :param root_id: The root_id of this BasicAwRes.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def source(self):
        r"""Gets the source of this BasicAwRes.

        :return: The source of this BasicAwRes.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this BasicAwRes.

        :param source: The source of this BasicAwRes.
        :type source: str
        """
        self._source = source

    @property
    def special_type(self):
        r"""Gets the special_type of this BasicAwRes.

        :return: The special_type of this BasicAwRes.
        :rtype: int
        """
        return self._special_type

    @special_type.setter
    def special_type(self, special_type):
        r"""Sets the special_type of this BasicAwRes.

        :param special_type: The special_type of this BasicAwRes.
        :type special_type: int
        """
        self._special_type = special_type

    @property
    def tmss_case_number(self):
        r"""Gets the tmss_case_number of this BasicAwRes.

        :return: The tmss_case_number of this BasicAwRes.
        :rtype: str
        """
        return self._tmss_case_number

    @tmss_case_number.setter
    def tmss_case_number(self, tmss_case_number):
        r"""Sets the tmss_case_number of this BasicAwRes.

        :param tmss_case_number: The tmss_case_number of this BasicAwRes.
        :type tmss_case_number: str
        """
        self._tmss_case_number = tmss_case_number

    @property
    def tmss_case_id(self):
        r"""Gets the tmss_case_id of this BasicAwRes.

        :return: The tmss_case_id of this BasicAwRes.
        :rtype: str
        """
        return self._tmss_case_id

    @tmss_case_id.setter
    def tmss_case_id(self, tmss_case_id):
        r"""Sets the tmss_case_id of this BasicAwRes.

        :param tmss_case_id: The tmss_case_id of this BasicAwRes.
        :type tmss_case_id: str
        """
        self._tmss_case_id = tmss_case_id

    @property
    def update_time(self):
        r"""Gets the update_time of this BasicAwRes.

        更新时间

        :return: The update_time of this BasicAwRes.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this BasicAwRes.

        更新时间

        :param update_time: The update_time of this BasicAwRes.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_time_stamp(self):
        r"""Gets the update_time_stamp of this BasicAwRes.

        :return: The update_time_stamp of this BasicAwRes.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        r"""Sets the update_time_stamp of this BasicAwRes.

        :param update_time_stamp: The update_time_stamp of this BasicAwRes.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

    @property
    def update_time_string(self):
        r"""Gets the update_time_string of this BasicAwRes.

        :return: The update_time_string of this BasicAwRes.
        :rtype: str
        """
        return self._update_time_string

    @update_time_string.setter
    def update_time_string(self, update_time_string):
        r"""Sets the update_time_string of this BasicAwRes.

        :param update_time_string: The update_time_string of this BasicAwRes.
        :type update_time_string: str
        """
        self._update_time_string = update_time_string

    @property
    def update_user(self):
        r"""Gets the update_user of this BasicAwRes.

        更新人

        :return: The update_user of this BasicAwRes.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this BasicAwRes.

        更新人

        :param update_user: The update_user of this BasicAwRes.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def warning_msg(self):
        r"""Gets the warning_msg of this BasicAwRes.

        :return: The warning_msg of this BasicAwRes.
        :rtype: str
        """
        return self._warning_msg

    @warning_msg.setter
    def warning_msg(self, warning_msg):
        r"""Sets the warning_msg of this BasicAwRes.

        :param warning_msg: The warning_msg of this BasicAwRes.
        :type warning_msg: str
        """
        self._warning_msg = warning_msg

    @property
    def yaml_name(self):
        r"""Gets the yaml_name of this BasicAwRes.

        :return: The yaml_name of this BasicAwRes.
        :rtype: str
        """
        return self._yaml_name

    @yaml_name.setter
    def yaml_name(self, yaml_name):
        r"""Sets the yaml_name of this BasicAwRes.

        :param yaml_name: The yaml_name of this BasicAwRes.
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
        if not isinstance(other, BasicAwRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
