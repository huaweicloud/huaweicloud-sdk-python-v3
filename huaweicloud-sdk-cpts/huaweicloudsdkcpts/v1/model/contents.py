# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Contents:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_id': 'int',
        'content': 'list[Content]',
        'index': 'int',
        'selected_temp_name': 'str',
        'data': 'object',
        'data_type': 'int',
        'conditions': 'object',
        'is_disabled': 'bool'
    }

    attribute_map = {
        'content_id': 'content_id',
        'content': 'content',
        'index': 'index',
        'selected_temp_name': 'selected_temp_name',
        'data': 'data',
        'data_type': 'data_type',
        'conditions': 'conditions',
        'is_disabled': 'is_disabled'
    }

    def __init__(self, content_id=None, content=None, index=None, selected_temp_name=None, data=None, data_type=None, conditions=None, is_disabled=None):
        """Contents

        The model defined in huaweicloud sdk

        :param content_id: 事务id，若不为0表示此卡片为事务；为0表示非事务
        :type content_id: int
        :param content: 内容
        :type content: list[:class:`huaweicloudsdkcpts.v1.Content`]
        :param index: 排序索引标识
        :type index: int
        :param selected_temp_name: 选择的事务或者用例名称
        :type selected_temp_name: str
        :param data: 数据（循环、条件控制器作用的数据）
        :type data: object
        :param data_type: 数据指令类型（0：默认请求卡片；1：数据指令；201：循环指令；202：条件指令；301：集合点[；203：vu百分比控制器；204：吞吐量控制器；302：插件请求](tag:hws,hws_hk)）
        :type data_type: int
        :param conditions: 若类型为202:条件指令，该字段为条件配置
        :type conditions: object
        :param is_disabled: 是否禁用
        :type is_disabled: bool
        """
        
        

        self._content_id = None
        self._content = None
        self._index = None
        self._selected_temp_name = None
        self._data = None
        self._data_type = None
        self._conditions = None
        self._is_disabled = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if content is not None:
            self.content = content
        if index is not None:
            self.index = index
        if selected_temp_name is not None:
            self.selected_temp_name = selected_temp_name
        if data is not None:
            self.data = data
        if data_type is not None:
            self.data_type = data_type
        if conditions is not None:
            self.conditions = conditions
        if is_disabled is not None:
            self.is_disabled = is_disabled

    @property
    def content_id(self):
        """Gets the content_id of this Contents.

        事务id，若不为0表示此卡片为事务；为0表示非事务

        :return: The content_id of this Contents.
        :rtype: int
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this Contents.

        事务id，若不为0表示此卡片为事务；为0表示非事务

        :param content_id: The content_id of this Contents.
        :type content_id: int
        """
        self._content_id = content_id

    @property
    def content(self):
        """Gets the content of this Contents.

        内容

        :return: The content of this Contents.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.Content`]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Contents.

        内容

        :param content: The content of this Contents.
        :type content: list[:class:`huaweicloudsdkcpts.v1.Content`]
        """
        self._content = content

    @property
    def index(self):
        """Gets the index of this Contents.

        排序索引标识

        :return: The index of this Contents.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Contents.

        排序索引标识

        :param index: The index of this Contents.
        :type index: int
        """
        self._index = index

    @property
    def selected_temp_name(self):
        """Gets the selected_temp_name of this Contents.

        选择的事务或者用例名称

        :return: The selected_temp_name of this Contents.
        :rtype: str
        """
        return self._selected_temp_name

    @selected_temp_name.setter
    def selected_temp_name(self, selected_temp_name):
        """Sets the selected_temp_name of this Contents.

        选择的事务或者用例名称

        :param selected_temp_name: The selected_temp_name of this Contents.
        :type selected_temp_name: str
        """
        self._selected_temp_name = selected_temp_name

    @property
    def data(self):
        """Gets the data of this Contents.

        数据（循环、条件控制器作用的数据）

        :return: The data of this Contents.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Contents.

        数据（循环、条件控制器作用的数据）

        :param data: The data of this Contents.
        :type data: object
        """
        self._data = data

    @property
    def data_type(self):
        """Gets the data_type of this Contents.

        数据指令类型（0：默认请求卡片；1：数据指令；201：循环指令；202：条件指令；301：集合点[；203：vu百分比控制器；204：吞吐量控制器；302：插件请求](tag:hws,hws_hk)）

        :return: The data_type of this Contents.
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Contents.

        数据指令类型（0：默认请求卡片；1：数据指令；201：循环指令；202：条件指令；301：集合点[；203：vu百分比控制器；204：吞吐量控制器；302：插件请求](tag:hws,hws_hk)）

        :param data_type: The data_type of this Contents.
        :type data_type: int
        """
        self._data_type = data_type

    @property
    def conditions(self):
        """Gets the conditions of this Contents.

        若类型为202:条件指令，该字段为条件配置

        :return: The conditions of this Contents.
        :rtype: object
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Contents.

        若类型为202:条件指令，该字段为条件配置

        :param conditions: The conditions of this Contents.
        :type conditions: object
        """
        self._conditions = conditions

    @property
    def is_disabled(self):
        """Gets the is_disabled of this Contents.

        是否禁用

        :return: The is_disabled of this Contents.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this Contents.

        是否禁用

        :param is_disabled: The is_disabled of this Contents.
        :type is_disabled: bool
        """
        self._is_disabled = is_disabled

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
        if not isinstance(other, Contents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
