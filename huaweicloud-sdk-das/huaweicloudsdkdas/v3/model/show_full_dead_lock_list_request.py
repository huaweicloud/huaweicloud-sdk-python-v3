# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFullDeadLockListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, start_at=None, end_at=None, page_num=None, page_size=None, x_language=None):
        r"""ShowFullDeadLockListRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param start_at: 开始时间
        :type start_at: int
        :param end_at: 结束时间
        :type end_at: int
        :param page_num: 当前页数
        :type page_num: int
        :param page_size: 每页返回数量，默认10
        :type page_size: int
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._start_at = None
        self._end_at = None
        self._page_num = None
        self._page_size = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_at = start_at
        self.end_at = end_at
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowFullDeadLockListRequest.

        实例id

        :return: The instance_id of this ShowFullDeadLockListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowFullDeadLockListRequest.

        实例id

        :param instance_id: The instance_id of this ShowFullDeadLockListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ShowFullDeadLockListRequest.

        开始时间

        :return: The start_at of this ShowFullDeadLockListRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ShowFullDeadLockListRequest.

        开始时间

        :param start_at: The start_at of this ShowFullDeadLockListRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ShowFullDeadLockListRequest.

        结束时间

        :return: The end_at of this ShowFullDeadLockListRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ShowFullDeadLockListRequest.

        结束时间

        :param end_at: The end_at of this ShowFullDeadLockListRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowFullDeadLockListRequest.

        当前页数

        :return: The page_num of this ShowFullDeadLockListRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowFullDeadLockListRequest.

        当前页数

        :param page_num: The page_num of this ShowFullDeadLockListRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowFullDeadLockListRequest.

        每页返回数量，默认10

        :return: The page_size of this ShowFullDeadLockListRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowFullDeadLockListRequest.

        每页返回数量，默认10

        :param page_size: The page_size of this ShowFullDeadLockListRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowFullDeadLockListRequest.

        语言

        :return: The x_language of this ShowFullDeadLockListRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowFullDeadLockListRequest.

        语言

        :param x_language: The x_language of this ShowFullDeadLockListRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowFullDeadLockListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
