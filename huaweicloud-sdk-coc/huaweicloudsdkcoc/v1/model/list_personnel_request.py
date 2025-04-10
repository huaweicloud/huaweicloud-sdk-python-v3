# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPersonnelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_mobile': 'bool',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'has_mobile': 'has_mobile',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, has_mobile=None, name=None, offset=None, limit=None):
        r"""ListPersonnelRequest

        The model defined in huaweicloud sdk

        :param has_mobile: 是否有手机号
        :type has_mobile: bool
        :param name: IAM账号
        :type name: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 分页
        :type limit: int
        """
        
        

        self._has_mobile = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if has_mobile is not None:
            self.has_mobile = has_mobile
        if name is not None:
            self.name = name
        self.offset = offset
        self.limit = limit

    @property
    def has_mobile(self):
        r"""Gets the has_mobile of this ListPersonnelRequest.

        是否有手机号

        :return: The has_mobile of this ListPersonnelRequest.
        :rtype: bool
        """
        return self._has_mobile

    @has_mobile.setter
    def has_mobile(self, has_mobile):
        r"""Sets the has_mobile of this ListPersonnelRequest.

        是否有手机号

        :param has_mobile: The has_mobile of this ListPersonnelRequest.
        :type has_mobile: bool
        """
        self._has_mobile = has_mobile

    @property
    def name(self):
        r"""Gets the name of this ListPersonnelRequest.

        IAM账号

        :return: The name of this ListPersonnelRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPersonnelRequest.

        IAM账号

        :param name: The name of this ListPersonnelRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListPersonnelRequest.

        偏移量

        :return: The offset of this ListPersonnelRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPersonnelRequest.

        偏移量

        :param offset: The offset of this ListPersonnelRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPersonnelRequest.

        分页

        :return: The limit of this ListPersonnelRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPersonnelRequest.

        分页

        :param limit: The limit of this ListPersonnelRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPersonnelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
