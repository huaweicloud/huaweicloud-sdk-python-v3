# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataSummaryRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'name': 'str',
        'type': 'PathType',
        'size': 'int',
        'create_time': 'str',
        'allowed_operate': 'bool',
        'deletable': 'bool'
    }

    attribute_map = {
        'path': 'path',
        'name': 'name',
        'type': 'type',
        'size': 'size',
        'create_time': 'create_time',
        'allowed_operate': 'allowed_operate',
        'deletable': 'deletable'
    }

    def __init__(self, path=None, name=None, type=None, size=None, create_time=None, allowed_operate=None, deletable=None):
        r"""DataSummaryRsp

        The model defined in huaweicloud sdk

        :param path: 对象全路径（项目名称:/路径）
        :type path: str
        :param name: 名称
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.PathType`
        :param size: 大小
        :type size: int
        :param create_time: 创建时间
        :type create_time: str
        :param allowed_operate: 可操作标记
        :type allowed_operate: bool
        :param deletable: 可删除标记
        :type deletable: bool
        """
        
        

        self._path = None
        self._name = None
        self._type = None
        self._size = None
        self._create_time = None
        self._allowed_operate = None
        self._deletable = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if create_time is not None:
            self.create_time = create_time
        if allowed_operate is not None:
            self.allowed_operate = allowed_operate
        if deletable is not None:
            self.deletable = deletable

    @property
    def path(self):
        r"""Gets the path of this DataSummaryRsp.

        对象全路径（项目名称:/路径）

        :return: The path of this DataSummaryRsp.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this DataSummaryRsp.

        对象全路径（项目名称:/路径）

        :param path: The path of this DataSummaryRsp.
        :type path: str
        """
        self._path = path

    @property
    def name(self):
        r"""Gets the name of this DataSummaryRsp.

        名称

        :return: The name of this DataSummaryRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataSummaryRsp.

        名称

        :param name: The name of this DataSummaryRsp.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DataSummaryRsp.

        :return: The type of this DataSummaryRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PathType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DataSummaryRsp.

        :param type: The type of this DataSummaryRsp.
        :type type: :class:`huaweicloudsdkeihealth.v1.PathType`
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this DataSummaryRsp.

        大小

        :return: The size of this DataSummaryRsp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this DataSummaryRsp.

        大小

        :param size: The size of this DataSummaryRsp.
        :type size: int
        """
        self._size = size

    @property
    def create_time(self):
        r"""Gets the create_time of this DataSummaryRsp.

        创建时间

        :return: The create_time of this DataSummaryRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DataSummaryRsp.

        创建时间

        :param create_time: The create_time of this DataSummaryRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def allowed_operate(self):
        r"""Gets the allowed_operate of this DataSummaryRsp.

        可操作标记

        :return: The allowed_operate of this DataSummaryRsp.
        :rtype: bool
        """
        return self._allowed_operate

    @allowed_operate.setter
    def allowed_operate(self, allowed_operate):
        r"""Sets the allowed_operate of this DataSummaryRsp.

        可操作标记

        :param allowed_operate: The allowed_operate of this DataSummaryRsp.
        :type allowed_operate: bool
        """
        self._allowed_operate = allowed_operate

    @property
    def deletable(self):
        r"""Gets the deletable of this DataSummaryRsp.

        可删除标记

        :return: The deletable of this DataSummaryRsp.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this DataSummaryRsp.

        可删除标记

        :param deletable: The deletable of this DataSummaryRsp.
        :type deletable: bool
        """
        self._deletable = deletable

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
        if not isinstance(other, DataSummaryRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
