# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeTableVO:

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
        'name_en': 'str',
        'name_ch': 'str',
        'tb_version': 'int',
        'directory_id': 'str',
        'directory_path': 'str',
        'description': 'str',
        'create_by': 'str',
        'status': 'BizStatusEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'code_table_fields': 'list[CodeTableFieldVO]'
    }

    attribute_map = {
        'id': 'id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'tb_version': 'tb_version',
        'directory_id': 'directory_id',
        'directory_path': 'directory_path',
        'description': 'description',
        'create_by': 'create_by',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'code_table_fields': 'code_table_fields'
    }

    def __init__(self, id=None, name_en=None, name_ch=None, tb_version=None, directory_id=None, directory_path=None, description=None, create_by=None, status=None, create_time=None, update_time=None, approval_info=None, new_biz=None, code_table_fields=None):
        r"""CodeTableVO

        The model defined in huaweicloud sdk

        :param id: 码表ID，ID字符串。
        :type id: str
        :param name_en: 表名称，英文名。
        :type name_en: str
        :param name_ch: 表名称，中文名。
        :type name_ch: str
        :param tb_version: 表版本。
        :type tb_version: int
        :param directory_id: 目录ID，ID字符串。
        :type directory_id: str
        :param directory_path: 目录树。
        :type directory_path: str
        :param description: 描述。
        :type description: str
        :param create_by: 创建人。
        :type create_by: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param code_table_fields: 码表属性信息。
        :type code_table_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        
        

        self._id = None
        self._name_en = None
        self._name_ch = None
        self._tb_version = None
        self._directory_id = None
        self._directory_path = None
        self._description = None
        self._create_by = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._approval_info = None
        self._new_biz = None
        self._code_table_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_en = name_en
        self.name_ch = name_ch
        if tb_version is not None:
            self.tb_version = tb_version
        self.directory_id = directory_id
        if directory_path is not None:
            self.directory_path = directory_path
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz
        self.code_table_fields = code_table_fields

    @property
    def id(self):
        r"""Gets the id of this CodeTableVO.

        码表ID，ID字符串。

        :return: The id of this CodeTableVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CodeTableVO.

        码表ID，ID字符串。

        :param id: The id of this CodeTableVO.
        :type id: str
        """
        self._id = id

    @property
    def name_en(self):
        r"""Gets the name_en of this CodeTableVO.

        表名称，英文名。

        :return: The name_en of this CodeTableVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CodeTableVO.

        表名称，英文名。

        :param name_en: The name_en of this CodeTableVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        r"""Gets the name_ch of this CodeTableVO.

        表名称，中文名。

        :return: The name_ch of this CodeTableVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        r"""Sets the name_ch of this CodeTableVO.

        表名称，中文名。

        :param name_ch: The name_ch of this CodeTableVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def tb_version(self):
        r"""Gets the tb_version of this CodeTableVO.

        表版本。

        :return: The tb_version of this CodeTableVO.
        :rtype: int
        """
        return self._tb_version

    @tb_version.setter
    def tb_version(self, tb_version):
        r"""Sets the tb_version of this CodeTableVO.

        表版本。

        :param tb_version: The tb_version of this CodeTableVO.
        :type tb_version: int
        """
        self._tb_version = tb_version

    @property
    def directory_id(self):
        r"""Gets the directory_id of this CodeTableVO.

        目录ID，ID字符串。

        :return: The directory_id of this CodeTableVO.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        r"""Sets the directory_id of this CodeTableVO.

        目录ID，ID字符串。

        :param directory_id: The directory_id of this CodeTableVO.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def directory_path(self):
        r"""Gets the directory_path of this CodeTableVO.

        目录树。

        :return: The directory_path of this CodeTableVO.
        :rtype: str
        """
        return self._directory_path

    @directory_path.setter
    def directory_path(self, directory_path):
        r"""Sets the directory_path of this CodeTableVO.

        目录树。

        :param directory_path: The directory_path of this CodeTableVO.
        :type directory_path: str
        """
        self._directory_path = directory_path

    @property
    def description(self):
        r"""Gets the description of this CodeTableVO.

        描述。

        :return: The description of this CodeTableVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CodeTableVO.

        描述。

        :param description: The description of this CodeTableVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        r"""Gets the create_by of this CodeTableVO.

        创建人。

        :return: The create_by of this CodeTableVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CodeTableVO.

        创建人。

        :param create_by: The create_by of this CodeTableVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def status(self):
        r"""Gets the status of this CodeTableVO.

        :return: The status of this CodeTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CodeTableVO.

        :param status: The status of this CodeTableVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this CodeTableVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this CodeTableVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CodeTableVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this CodeTableVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CodeTableVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this CodeTableVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CodeTableVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this CodeTableVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def approval_info(self):
        r"""Gets the approval_info of this CodeTableVO.

        :return: The approval_info of this CodeTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        r"""Sets the approval_info of this CodeTableVO.

        :param approval_info: The approval_info of this CodeTableVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        r"""Gets the new_biz of this CodeTableVO.

        :return: The new_biz of this CodeTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        r"""Sets the new_biz of this CodeTableVO.

        :param new_biz: The new_biz of this CodeTableVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def code_table_fields(self):
        r"""Gets the code_table_fields of this CodeTableVO.

        码表属性信息。

        :return: The code_table_fields of this CodeTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        return self._code_table_fields

    @code_table_fields.setter
    def code_table_fields(self, code_table_fields):
        r"""Sets the code_table_fields of this CodeTableVO.

        码表属性信息。

        :param code_table_fields: The code_table_fields of this CodeTableVO.
        :type code_table_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        self._code_table_fields = code_table_fields

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
        if not isinstance(other, CodeTableVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
