# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccountRequest:

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
        'delegator': 'str',
        'status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'delegator': 'delegator',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, name=None, delegator=None, status=None, offset=None, limit=None):
        r"""ShowAccountRequest

        The model defined in huaweicloud sdk

        :param name: 账号名称
        :type name: str
        :param delegator: 账号id
        :type delegator: str
        :param status: 账号状态
        :type status: str
        :param offset: 分页参数
        :type offset: int
        :param limit: 分页参数
        :type limit: int
        """
        
        

        self._name = None
        self._delegator = None
        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if delegator is not None:
            self.delegator = delegator
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        r"""Gets the name of this ShowAccountRequest.

        账号名称

        :return: The name of this ShowAccountRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAccountRequest.

        账号名称

        :param name: The name of this ShowAccountRequest.
        :type name: str
        """
        self._name = name

    @property
    def delegator(self):
        r"""Gets the delegator of this ShowAccountRequest.

        账号id

        :return: The delegator of this ShowAccountRequest.
        :rtype: str
        """
        return self._delegator

    @delegator.setter
    def delegator(self, delegator):
        r"""Sets the delegator of this ShowAccountRequest.

        账号id

        :param delegator: The delegator of this ShowAccountRequest.
        :type delegator: str
        """
        self._delegator = delegator

    @property
    def status(self):
        r"""Gets the status of this ShowAccountRequest.

        账号状态

        :return: The status of this ShowAccountRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAccountRequest.

        账号状态

        :param status: The status of this ShowAccountRequest.
        :type status: str
        """
        self._status = status

    @property
    def offset(self):
        r"""Gets the offset of this ShowAccountRequest.

        分页参数

        :return: The offset of this ShowAccountRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAccountRequest.

        分页参数

        :param offset: The offset of this ShowAccountRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowAccountRequest.

        分页参数

        :return: The limit of this ShowAccountRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAccountRequest.

        分页参数

        :param limit: The limit of this ShowAccountRequest.
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
        if not isinstance(other, ShowAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
