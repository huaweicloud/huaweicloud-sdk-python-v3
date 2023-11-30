# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonConditionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'field_ids': 'list[str]',
        'field_names': 'list[str]',
        'cal_exp': 'str',
        'cal_fn_ids': 'list[int]',
        'front_configs': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'field_ids': 'field_ids',
        'field_names': 'field_names',
        'cal_exp': 'cal_exp',
        'cal_fn_ids': 'cal_fn_ids',
        'front_configs': 'front_configs',
        'id': 'id'
    }

    def __init__(self, name=None, field_ids=None, field_names=None, cal_exp=None, cal_fn_ids=None, front_configs=None, id=None):
        """CommonConditionVO

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param field_ids: 字段id信息， 格式：table_id.field_id
        :type field_ids: list[str]
        :param field_names: 字段名称信息， 格式：表名称.字段名称
        :type field_names: list[str]
        :param cal_exp: 计算表达式
        :type cal_exp: str
        :param cal_fn_ids: 计算表达式id
        :type cal_fn_ids: list[int]
        :param front_configs: 前端表达式配置，用于前端数据恢复
        :type front_configs: str
        :param id: id
        :type id: int
        """
        
        

        self._name = None
        self._field_ids = None
        self._field_names = None
        self._cal_exp = None
        self._cal_fn_ids = None
        self._front_configs = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.field_ids = field_ids
        if field_names is not None:
            self.field_names = field_names
        self.cal_exp = cal_exp
        self.cal_fn_ids = cal_fn_ids
        if front_configs is not None:
            self.front_configs = front_configs
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this CommonConditionVO.

        名称

        :return: The name of this CommonConditionVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommonConditionVO.

        名称

        :param name: The name of this CommonConditionVO.
        :type name: str
        """
        self._name = name

    @property
    def field_ids(self):
        """Gets the field_ids of this CommonConditionVO.

        字段id信息， 格式：table_id.field_id

        :return: The field_ids of this CommonConditionVO.
        :rtype: list[str]
        """
        return self._field_ids

    @field_ids.setter
    def field_ids(self, field_ids):
        """Sets the field_ids of this CommonConditionVO.

        字段id信息， 格式：table_id.field_id

        :param field_ids: The field_ids of this CommonConditionVO.
        :type field_ids: list[str]
        """
        self._field_ids = field_ids

    @property
    def field_names(self):
        """Gets the field_names of this CommonConditionVO.

        字段名称信息， 格式：表名称.字段名称

        :return: The field_names of this CommonConditionVO.
        :rtype: list[str]
        """
        return self._field_names

    @field_names.setter
    def field_names(self, field_names):
        """Sets the field_names of this CommonConditionVO.

        字段名称信息， 格式：表名称.字段名称

        :param field_names: The field_names of this CommonConditionVO.
        :type field_names: list[str]
        """
        self._field_names = field_names

    @property
    def cal_exp(self):
        """Gets the cal_exp of this CommonConditionVO.

        计算表达式

        :return: The cal_exp of this CommonConditionVO.
        :rtype: str
        """
        return self._cal_exp

    @cal_exp.setter
    def cal_exp(self, cal_exp):
        """Sets the cal_exp of this CommonConditionVO.

        计算表达式

        :param cal_exp: The cal_exp of this CommonConditionVO.
        :type cal_exp: str
        """
        self._cal_exp = cal_exp

    @property
    def cal_fn_ids(self):
        """Gets the cal_fn_ids of this CommonConditionVO.

        计算表达式id

        :return: The cal_fn_ids of this CommonConditionVO.
        :rtype: list[int]
        """
        return self._cal_fn_ids

    @cal_fn_ids.setter
    def cal_fn_ids(self, cal_fn_ids):
        """Sets the cal_fn_ids of this CommonConditionVO.

        计算表达式id

        :param cal_fn_ids: The cal_fn_ids of this CommonConditionVO.
        :type cal_fn_ids: list[int]
        """
        self._cal_fn_ids = cal_fn_ids

    @property
    def front_configs(self):
        """Gets the front_configs of this CommonConditionVO.

        前端表达式配置，用于前端数据恢复

        :return: The front_configs of this CommonConditionVO.
        :rtype: str
        """
        return self._front_configs

    @front_configs.setter
    def front_configs(self, front_configs):
        """Sets the front_configs of this CommonConditionVO.

        前端表达式配置，用于前端数据恢复

        :param front_configs: The front_configs of this CommonConditionVO.
        :type front_configs: str
        """
        self._front_configs = front_configs

    @property
    def id(self):
        """Gets the id of this CommonConditionVO.

        id

        :return: The id of this CommonConditionVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommonConditionVO.

        id

        :param id: The id of this CommonConditionVO.
        :type id: int
        """
        self._id = id

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
        if not isinstance(other, CommonConditionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
