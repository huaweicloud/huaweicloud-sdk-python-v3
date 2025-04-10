# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoticeRsp:

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
        'type': 'str',
        'detail': 'str',
        'create_time': 'str',
        'is_read': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'detail': 'detail',
        'create_time': 'create_time',
        'is_read': 'is_read'
    }

    def __init__(self, id=None, type=None, detail=None, create_time=None, is_read=None):
        r"""NoticeRsp

        The model defined in huaweicloud sdk

        :param id: 消息id
        :type id: str
        :param type: 消息类型
        :type type: str
        :param detail: 消息详情
        :type detail: str
        :param create_time: 消息创建时间
        :type create_time: str
        :param is_read: 是否已读
        :type is_read: bool
        """
        
        

        self._id = None
        self._type = None
        self._detail = None
        self._create_time = None
        self._is_read = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if detail is not None:
            self.detail = detail
        if create_time is not None:
            self.create_time = create_time
        if is_read is not None:
            self.is_read = is_read

    @property
    def id(self):
        r"""Gets the id of this NoticeRsp.

        消息id

        :return: The id of this NoticeRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NoticeRsp.

        消息id

        :param id: The id of this NoticeRsp.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this NoticeRsp.

        消息类型

        :return: The type of this NoticeRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NoticeRsp.

        消息类型

        :param type: The type of this NoticeRsp.
        :type type: str
        """
        self._type = type

    @property
    def detail(self):
        r"""Gets the detail of this NoticeRsp.

        消息详情

        :return: The detail of this NoticeRsp.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this NoticeRsp.

        消息详情

        :param detail: The detail of this NoticeRsp.
        :type detail: str
        """
        self._detail = detail

    @property
    def create_time(self):
        r"""Gets the create_time of this NoticeRsp.

        消息创建时间

        :return: The create_time of this NoticeRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this NoticeRsp.

        消息创建时间

        :param create_time: The create_time of this NoticeRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def is_read(self):
        r"""Gets the is_read of this NoticeRsp.

        是否已读

        :return: The is_read of this NoticeRsp.
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        r"""Sets the is_read of this NoticeRsp.

        是否已读

        :param is_read: The is_read of this NoticeRsp.
        :type is_read: bool
        """
        self._is_read = is_read

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
        if not isinstance(other, NoticeRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
