# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateRsp:

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
        'name': 'str',
        'description': 'str',
        'source_project_name': 'str',
        'source_project_id': 'str',
        'source_template_id': 'str',
        'creator': 'str',
        'columns': 'list[DatabaseColumnDto]',
        'create_time': 'str',
        'primary_key': 'str',
        'is_prefab': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'source_project_name': 'source_project_name',
        'source_project_id': 'source_project_id',
        'source_template_id': 'source_template_id',
        'creator': 'creator',
        'columns': 'columns',
        'create_time': 'create_time',
        'primary_key': 'primary_key',
        'is_prefab': 'is_prefab'
    }

    def __init__(self, id=None, name=None, description=None, source_project_name=None, source_project_id=None, source_template_id=None, creator=None, columns=None, create_time=None, primary_key=None, is_prefab=None):
        r"""TemplateRsp

        The model defined in huaweicloud sdk

        :param id: 模板id
        :type id: str
        :param name: 模板名称
        :type name: str
        :param description: 模板描述
        :type description: str
        :param source_project_name: 来源项目名称
        :type source_project_name: str
        :param source_project_id: 来源项目id
        :type source_project_id: str
        :param source_template_id: 来源模板id
        :type source_template_id: str
        :param creator: 创建者
        :type creator: str
        :param columns: 数据库列信息列表
        :type columns: list[:class:`huaweicloudsdkeihealth.v1.DatabaseColumnDto`]
        :param create_time: 创建时间
        :type create_time: str
        :param primary_key: 主键
        :type primary_key: str
        :param is_prefab: 是否是预置模板
        :type is_prefab: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._source_project_name = None
        self._source_project_id = None
        self._source_template_id = None
        self._creator = None
        self._columns = None
        self._create_time = None
        self._primary_key = None
        self._is_prefab = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if source_template_id is not None:
            self.source_template_id = source_template_id
        if creator is not None:
            self.creator = creator
        if columns is not None:
            self.columns = columns
        if create_time is not None:
            self.create_time = create_time
        if primary_key is not None:
            self.primary_key = primary_key
        if is_prefab is not None:
            self.is_prefab = is_prefab

    @property
    def id(self):
        r"""Gets the id of this TemplateRsp.

        模板id

        :return: The id of this TemplateRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TemplateRsp.

        模板id

        :param id: The id of this TemplateRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TemplateRsp.

        模板名称

        :return: The name of this TemplateRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateRsp.

        模板名称

        :param name: The name of this TemplateRsp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TemplateRsp.

        模板描述

        :return: The description of this TemplateRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateRsp.

        模板描述

        :param description: The description of this TemplateRsp.
        :type description: str
        """
        self._description = description

    @property
    def source_project_name(self):
        r"""Gets the source_project_name of this TemplateRsp.

        来源项目名称

        :return: The source_project_name of this TemplateRsp.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        r"""Sets the source_project_name of this TemplateRsp.

        来源项目名称

        :param source_project_name: The source_project_name of this TemplateRsp.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_project_id(self):
        r"""Gets the source_project_id of this TemplateRsp.

        来源项目id

        :return: The source_project_id of this TemplateRsp.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        r"""Sets the source_project_id of this TemplateRsp.

        来源项目id

        :param source_project_id: The source_project_id of this TemplateRsp.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_template_id(self):
        r"""Gets the source_template_id of this TemplateRsp.

        来源模板id

        :return: The source_template_id of this TemplateRsp.
        :rtype: str
        """
        return self._source_template_id

    @source_template_id.setter
    def source_template_id(self, source_template_id):
        r"""Sets the source_template_id of this TemplateRsp.

        来源模板id

        :param source_template_id: The source_template_id of this TemplateRsp.
        :type source_template_id: str
        """
        self._source_template_id = source_template_id

    @property
    def creator(self):
        r"""Gets the creator of this TemplateRsp.

        创建者

        :return: The creator of this TemplateRsp.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this TemplateRsp.

        创建者

        :param creator: The creator of this TemplateRsp.
        :type creator: str
        """
        self._creator = creator

    @property
    def columns(self):
        r"""Gets the columns of this TemplateRsp.

        数据库列信息列表

        :return: The columns of this TemplateRsp.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DatabaseColumnDto`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this TemplateRsp.

        数据库列信息列表

        :param columns: The columns of this TemplateRsp.
        :type columns: list[:class:`huaweicloudsdkeihealth.v1.DatabaseColumnDto`]
        """
        self._columns = columns

    @property
    def create_time(self):
        r"""Gets the create_time of this TemplateRsp.

        创建时间

        :return: The create_time of this TemplateRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TemplateRsp.

        创建时间

        :param create_time: The create_time of this TemplateRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def primary_key(self):
        r"""Gets the primary_key of this TemplateRsp.

        主键

        :return: The primary_key of this TemplateRsp.
        :rtype: str
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this TemplateRsp.

        主键

        :param primary_key: The primary_key of this TemplateRsp.
        :type primary_key: str
        """
        self._primary_key = primary_key

    @property
    def is_prefab(self):
        r"""Gets the is_prefab of this TemplateRsp.

        是否是预置模板

        :return: The is_prefab of this TemplateRsp.
        :rtype: bool
        """
        return self._is_prefab

    @is_prefab.setter
    def is_prefab(self, is_prefab):
        r"""Sets the is_prefab of this TemplateRsp.

        是否是预置模板

        :param is_prefab: The is_prefab of this TemplateRsp.
        :type is_prefab: bool
        """
        self._is_prefab = is_prefab

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
        if not isinstance(other, TemplateRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
