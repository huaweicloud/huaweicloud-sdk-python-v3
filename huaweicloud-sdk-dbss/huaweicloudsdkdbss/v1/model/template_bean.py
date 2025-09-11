# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_ids': 'str',
        'db_names': 'str',
        'desc': 'str',
        'frequency': 'str',
        'group': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'db_ids': 'db_ids',
        'db_names': 'db_names',
        'desc': 'desc',
        'frequency': 'frequency',
        'group': 'group',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, db_ids=None, db_names=None, desc=None, frequency=None, group=None, id=None, name=None, status=None, type=None):
        r"""TemplateBean

        The model defined in huaweicloud sdk

        :param db_ids: 数据库ID
        :type db_ids: str
        :param db_names: 数据库名称
        :type db_names: str
        :param desc: 描述
        :type desc: str
        :param frequency: 周期
        :type frequency: str
        :param group: 类型 - COMPREHENSIVE: 综合报表 - COMPLIANCE: 合规报表 - DB_SPECIAL：数据库专项报表 - CLIENT_SPECIAL：客户端专项报表 - SQL_SPECIAL：SQL
        :type group: str
        :param id: 模板ID
        :type id: str
        :param name: 报表模板名称
        :type name: str
        :param status: 状态 - OFF：已关闭 - ON：已开启
        :type status: str
        :param type: 报表类型 - COMPREHENSIVE: 数据库安全综合报表 - COMPLIANCE: 数据库安全合规报表 - SOX: SOX-萨班斯报表 - PCI: 行业标准安全报表 - DB_ANALYSIS: 数据库服务器分析报表 - CLIENT_IP_ANALYSIS: 客户端IP分析报表 - SQL_DCL_COMMAND: DCL命令报表 - SQL_DDL_COMMAND: DDL命令报表 - SQL_DML_COMMAND: DML命令报表
        :type type: str
        """
        
        

        self._db_ids = None
        self._db_names = None
        self._desc = None
        self._frequency = None
        self._group = None
        self._id = None
        self._name = None
        self._status = None
        self._type = None
        self.discriminator = None

        if db_ids is not None:
            self.db_ids = db_ids
        if db_names is not None:
            self.db_names = db_names
        if desc is not None:
            self.desc = desc
        if frequency is not None:
            self.frequency = frequency
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def db_ids(self):
        r"""Gets the db_ids of this TemplateBean.

        数据库ID

        :return: The db_ids of this TemplateBean.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this TemplateBean.

        数据库ID

        :param db_ids: The db_ids of this TemplateBean.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def db_names(self):
        r"""Gets the db_names of this TemplateBean.

        数据库名称

        :return: The db_names of this TemplateBean.
        :rtype: str
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this TemplateBean.

        数据库名称

        :param db_names: The db_names of this TemplateBean.
        :type db_names: str
        """
        self._db_names = db_names

    @property
    def desc(self):
        r"""Gets the desc of this TemplateBean.

        描述

        :return: The desc of this TemplateBean.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this TemplateBean.

        描述

        :param desc: The desc of this TemplateBean.
        :type desc: str
        """
        self._desc = desc

    @property
    def frequency(self):
        r"""Gets the frequency of this TemplateBean.

        周期

        :return: The frequency of this TemplateBean.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this TemplateBean.

        周期

        :param frequency: The frequency of this TemplateBean.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def group(self):
        r"""Gets the group of this TemplateBean.

        类型 - COMPREHENSIVE: 综合报表 - COMPLIANCE: 合规报表 - DB_SPECIAL：数据库专项报表 - CLIENT_SPECIAL：客户端专项报表 - SQL_SPECIAL：SQL

        :return: The group of this TemplateBean.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this TemplateBean.

        类型 - COMPREHENSIVE: 综合报表 - COMPLIANCE: 合规报表 - DB_SPECIAL：数据库专项报表 - CLIENT_SPECIAL：客户端专项报表 - SQL_SPECIAL：SQL

        :param group: The group of this TemplateBean.
        :type group: str
        """
        self._group = group

    @property
    def id(self):
        r"""Gets the id of this TemplateBean.

        模板ID

        :return: The id of this TemplateBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TemplateBean.

        模板ID

        :param id: The id of this TemplateBean.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TemplateBean.

        报表模板名称

        :return: The name of this TemplateBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateBean.

        报表模板名称

        :param name: The name of this TemplateBean.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this TemplateBean.

        状态 - OFF：已关闭 - ON：已开启

        :return: The status of this TemplateBean.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TemplateBean.

        状态 - OFF：已关闭 - ON：已开启

        :param status: The status of this TemplateBean.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this TemplateBean.

        报表类型 - COMPREHENSIVE: 数据库安全综合报表 - COMPLIANCE: 数据库安全合规报表 - SOX: SOX-萨班斯报表 - PCI: 行业标准安全报表 - DB_ANALYSIS: 数据库服务器分析报表 - CLIENT_IP_ANALYSIS: 客户端IP分析报表 - SQL_DCL_COMMAND: DCL命令报表 - SQL_DDL_COMMAND: DDL命令报表 - SQL_DML_COMMAND: DML命令报表

        :return: The type of this TemplateBean.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TemplateBean.

        报表类型 - COMPREHENSIVE: 数据库安全综合报表 - COMPLIANCE: 数据库安全合规报表 - SOX: SOX-萨班斯报表 - PCI: 行业标准安全报表 - DB_ANALYSIS: 数据库服务器分析报表 - CLIENT_IP_ANALYSIS: 客户端IP分析报表 - SQL_DCL_COMMAND: DCL命令报表 - SQL_DDL_COMMAND: DDL命令报表 - SQL_DML_COMMAND: DML命令报表

        :param type: The type of this TemplateBean.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, TemplateBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
