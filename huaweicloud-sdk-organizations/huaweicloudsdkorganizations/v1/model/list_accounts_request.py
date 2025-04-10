# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'parent_id': 'str',
        'with_register_contact_info': 'bool',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'parent_id': 'parent_id',
        'with_register_contact_info': 'with_register_contact_info',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_security_token=None, parent_id=None, with_register_contact_info=None, limit=None, marker=None):
        r"""ListAccountsRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param parent_id: 父节点（根或组织单元）的唯一标识符（ID）。
        :type parent_id: str
        :param with_register_contact_info: 是否返回账号邮箱、手机号信息。若此参数为True，Limit最多200。
        :type with_register_contact_info: bool
        :param limit: 页面中最大结果数量。
        :type limit: int
        :param marker: 分页标记。
        :type marker: str
        """
        
        

        self._x_security_token = None
        self._parent_id = None
        self._with_register_contact_info = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if parent_id is not None:
            self.parent_id = parent_id
        if with_register_contact_info is not None:
            self.with_register_contact_info = with_register_contact_info
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListAccountsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListAccountsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListAccountsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListAccountsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ListAccountsRequest.

        父节点（根或组织单元）的唯一标识符（ID）。

        :return: The parent_id of this ListAccountsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ListAccountsRequest.

        父节点（根或组织单元）的唯一标识符（ID）。

        :param parent_id: The parent_id of this ListAccountsRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def with_register_contact_info(self):
        r"""Gets the with_register_contact_info of this ListAccountsRequest.

        是否返回账号邮箱、手机号信息。若此参数为True，Limit最多200。

        :return: The with_register_contact_info of this ListAccountsRequest.
        :rtype: bool
        """
        return self._with_register_contact_info

    @with_register_contact_info.setter
    def with_register_contact_info(self, with_register_contact_info):
        r"""Sets the with_register_contact_info of this ListAccountsRequest.

        是否返回账号邮箱、手机号信息。若此参数为True，Limit最多200。

        :param with_register_contact_info: The with_register_contact_info of this ListAccountsRequest.
        :type with_register_contact_info: bool
        """
        self._with_register_contact_info = with_register_contact_info

    @property
    def limit(self):
        r"""Gets the limit of this ListAccountsRequest.

        页面中最大结果数量。

        :return: The limit of this ListAccountsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAccountsRequest.

        页面中最大结果数量。

        :param limit: The limit of this ListAccountsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAccountsRequest.

        分页标记。

        :return: The marker of this ListAccountsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAccountsRequest.

        分页标记。

        :param marker: The marker of this ListAccountsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListAccountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
