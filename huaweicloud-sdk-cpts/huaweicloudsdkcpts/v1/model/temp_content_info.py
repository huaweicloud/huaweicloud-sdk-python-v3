# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TempContentInfo:

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
        'data': 'object',
        'data_type': 'int'
    }

    attribute_map = {
        'content_id': 'content_id',
        'content': 'content',
        'index': 'index',
        'data': 'data',
        'data_type': 'data_type'
    }

    def __init__(self, content_id=None, content=None, index=None, data=None, data_type=None):
        r"""TempContentInfo

        The model defined in huaweicloud sdk

        :param content_id: 报文id或者事务id或者插件id
        :type content_id: int
        :param content: 内容
        :type content: list[:class:`huaweicloudsdkcpts.v1.Content`]
        :param index: 索引
        :type index: int
        :param data: 数据指令内容
        :type data: object
        :param data_type: 数据指令类型（0：默认请求卡片；1：数据指令；201：循环指令；202：条件指令；301：集合点[；203：vu百分比控制器；204：吞吐量控制器；302：插件请求](tag:hws,hws_hk)）
        :type data_type: int
        """
        
        

        self._content_id = None
        self._content = None
        self._index = None
        self._data = None
        self._data_type = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if content is not None:
            self.content = content
        if index is not None:
            self.index = index
        if data is not None:
            self.data = data
        if data_type is not None:
            self.data_type = data_type

    @property
    def content_id(self):
        r"""Gets the content_id of this TempContentInfo.

        报文id或者事务id或者插件id

        :return: The content_id of this TempContentInfo.
        :rtype: int
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        r"""Sets the content_id of this TempContentInfo.

        报文id或者事务id或者插件id

        :param content_id: The content_id of this TempContentInfo.
        :type content_id: int
        """
        self._content_id = content_id

    @property
    def content(self):
        r"""Gets the content of this TempContentInfo.

        内容

        :return: The content of this TempContentInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.Content`]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this TempContentInfo.

        内容

        :param content: The content of this TempContentInfo.
        :type content: list[:class:`huaweicloudsdkcpts.v1.Content`]
        """
        self._content = content

    @property
    def index(self):
        r"""Gets the index of this TempContentInfo.

        索引

        :return: The index of this TempContentInfo.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this TempContentInfo.

        索引

        :param index: The index of this TempContentInfo.
        :type index: int
        """
        self._index = index

    @property
    def data(self):
        r"""Gets the data of this TempContentInfo.

        数据指令内容

        :return: The data of this TempContentInfo.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this TempContentInfo.

        数据指令内容

        :param data: The data of this TempContentInfo.
        :type data: object
        """
        self._data = data

    @property
    def data_type(self):
        r"""Gets the data_type of this TempContentInfo.

        数据指令类型（0：默认请求卡片；1：数据指令；201：循环指令；202：条件指令；301：集合点[；203：vu百分比控制器；204：吞吐量控制器；302：插件请求](tag:hws,hws_hk)）

        :return: The data_type of this TempContentInfo.
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this TempContentInfo.

        数据指令类型（0：默认请求卡片；1：数据指令；201：循环指令；202：条件指令；301：集合点[；203：vu百分比控制器；204：吞吐量控制器；302：插件请求](tag:hws,hws_hk)）

        :param data_type: The data_type of this TempContentInfo.
        :type data_type: int
        """
        self._data_type = data_type

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
        if not isinstance(other, TempContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
