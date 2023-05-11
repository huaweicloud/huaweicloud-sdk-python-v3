# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLabelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'label_id': 'int',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'label_id': 'label_id',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, offset=None, limit=None, name=None, label_id=None, x_site=None, x_language=None, x_time_zone=None):
        """ListLabelsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询偏移量，默认0
        :type offset: int
        :param limit: 查询数量，默认10，最大100
        :type limit: int
        :param name: 标签名称，最大64，支持模糊查询
        :type name: str
        :param label_id: 标签标识
        :type label_id: int
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._label_id = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if label_id is not None:
            self.label_id = label_id
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def offset(self):
        """Gets the offset of this ListLabelsRequest.

        查询偏移量，默认0

        :return: The offset of this ListLabelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListLabelsRequest.

        查询偏移量，默认0

        :param offset: The offset of this ListLabelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListLabelsRequest.

        查询数量，默认10，最大100

        :return: The limit of this ListLabelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLabelsRequest.

        查询数量，默认10，最大100

        :param limit: The limit of this ListLabelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListLabelsRequest.

        标签名称，最大64，支持模糊查询

        :return: The name of this ListLabelsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListLabelsRequest.

        标签名称，最大64，支持模糊查询

        :param name: The name of this ListLabelsRequest.
        :type name: str
        """
        self._name = name

    @property
    def label_id(self):
        """Gets the label_id of this ListLabelsRequest.

        标签标识

        :return: The label_id of this ListLabelsRequest.
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this ListLabelsRequest.

        标签标识

        :param label_id: The label_id of this ListLabelsRequest.
        :type label_id: int
        """
        self._label_id = label_id

    @property
    def x_site(self):
        """Gets the x_site of this ListLabelsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ListLabelsRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ListLabelsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ListLabelsRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ListLabelsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ListLabelsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListLabelsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ListLabelsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this ListLabelsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ListLabelsRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this ListLabelsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ListLabelsRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

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
        if not isinstance(other, ListLabelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
