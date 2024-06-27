# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplatePageParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator_num': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str'
    }

    attribute_map = {
        'creator_num': 'creator_num',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name'
    }

    def __init__(self, creator_num=None, offset=None, limit=None, name=None):
        """TemplatePageParam

        The model defined in huaweicloud sdk

        :param creator_num: 创建人ID
        :type creator_num: str
        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000
        :type offset: int
        :param limit: 每页显示的条目数量，最大支持200条
        :type limit: int
        :param name: 脑图名称
        :type name: str
        """
        
        

        self._creator_num = None
        self._offset = None
        self._limit = None
        self._name = None
        self.discriminator = None

        if creator_num is not None:
            self.creator_num = creator_num
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name

    @property
    def creator_num(self):
        """Gets the creator_num of this TemplatePageParam.

        创建人ID

        :return: The creator_num of this TemplatePageParam.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        """Sets the creator_num of this TemplatePageParam.

        创建人ID

        :param creator_num: The creator_num of this TemplatePageParam.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def offset(self):
        """Gets the offset of this TemplatePageParam.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :return: The offset of this TemplatePageParam.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TemplatePageParam.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :param offset: The offset of this TemplatePageParam.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this TemplatePageParam.

        每页显示的条目数量，最大支持200条

        :return: The limit of this TemplatePageParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TemplatePageParam.

        每页显示的条目数量，最大支持200条

        :param limit: The limit of this TemplatePageParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this TemplatePageParam.

        脑图名称

        :return: The name of this TemplatePageParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplatePageParam.

        脑图名称

        :param name: The name of this TemplatePageParam.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, TemplatePageParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
