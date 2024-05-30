# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MallParaDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'str',
        'visibility': 'str',
        'market_sort_type': 'str',
        'asc_or_desc': 'str',
        'offset': 'int',
        'limit': 'int',
        'is_owner': 'bool',
        'is_authorized': 'bool',
        'is_update_recently': 'bool',
        'is_release_recently': 'bool',
        'is_hot_recently': 'bool',
        'success_and_failure_rate': 'bool'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'visibility': 'visibility',
        'market_sort_type': 'market_sort_type',
        'asc_or_desc': 'asc_or_desc',
        'offset': 'offset',
        'limit': 'limit',
        'is_owner': 'is_owner',
        'is_authorized': 'is_authorized',
        'is_update_recently': 'is_update_recently',
        'is_release_recently': 'is_release_recently',
        'is_hot_recently': 'is_hot_recently',
        'success_and_failure_rate': 'success_and_failure_rate'
    }

    def __init__(self, auth_type=None, visibility=None, market_sort_type=None, asc_or_desc=None, offset=None, limit=None, is_owner=None, is_authorized=None, is_update_recently=None, is_release_recently=None, is_hot_recently=None, success_and_failure_rate=None):
        """MallParaDTO

        The model defined in huaweicloud sdk

        :param auth_type: 认证类型。
        :type auth_type: str
        :param visibility: API可见性，WORKSPACE：工作空间可见，PROJECT： 项目可见，DOMAIN：租户可见，SPECIFIC_PROJECT：指定项目可见。
        :type visibility: str
        :param market_sort_type: 排序参数。
        :type market_sort_type: str
        :param asc_or_desc: 升序、降序。
        :type asc_or_desc: str
        :param offset: 查询起始坐标。
        :type offset: int
        :param limit: 查询条数。
        :type limit: int
        :param is_owner: 是否显示拥有者。
        :type is_owner: bool
        :param is_authorized: 是否显示已被授权。
        :type is_authorized: bool
        :param is_update_recently: 是否显示最近更新。
        :type is_update_recently: bool
        :param is_release_recently: 是否显示最近发布。
        :type is_release_recently: bool
        :param is_hot_recently: 是否显示热销状态。
        :type is_hot_recently: bool
        :param success_and_failure_rate: 是否显示7天内成功率与失败率。
        :type success_and_failure_rate: bool
        """
        
        

        self._auth_type = None
        self._visibility = None
        self._market_sort_type = None
        self._asc_or_desc = None
        self._offset = None
        self._limit = None
        self._is_owner = None
        self._is_authorized = None
        self._is_update_recently = None
        self._is_release_recently = None
        self._is_hot_recently = None
        self._success_and_failure_rate = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if visibility is not None:
            self.visibility = visibility
        if market_sort_type is not None:
            self.market_sort_type = market_sort_type
        if asc_or_desc is not None:
            self.asc_or_desc = asc_or_desc
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if is_owner is not None:
            self.is_owner = is_owner
        if is_authorized is not None:
            self.is_authorized = is_authorized
        if is_update_recently is not None:
            self.is_update_recently = is_update_recently
        if is_release_recently is not None:
            self.is_release_recently = is_release_recently
        if is_hot_recently is not None:
            self.is_hot_recently = is_hot_recently
        if success_and_failure_rate is not None:
            self.success_and_failure_rate = success_and_failure_rate

    @property
    def auth_type(self):
        """Gets the auth_type of this MallParaDTO.

        认证类型。

        :return: The auth_type of this MallParaDTO.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this MallParaDTO.

        认证类型。

        :param auth_type: The auth_type of this MallParaDTO.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def visibility(self):
        """Gets the visibility of this MallParaDTO.

        API可见性，WORKSPACE：工作空间可见，PROJECT： 项目可见，DOMAIN：租户可见，SPECIFIC_PROJECT：指定项目可见。

        :return: The visibility of this MallParaDTO.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this MallParaDTO.

        API可见性，WORKSPACE：工作空间可见，PROJECT： 项目可见，DOMAIN：租户可见，SPECIFIC_PROJECT：指定项目可见。

        :param visibility: The visibility of this MallParaDTO.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def market_sort_type(self):
        """Gets the market_sort_type of this MallParaDTO.

        排序参数。

        :return: The market_sort_type of this MallParaDTO.
        :rtype: str
        """
        return self._market_sort_type

    @market_sort_type.setter
    def market_sort_type(self, market_sort_type):
        """Sets the market_sort_type of this MallParaDTO.

        排序参数。

        :param market_sort_type: The market_sort_type of this MallParaDTO.
        :type market_sort_type: str
        """
        self._market_sort_type = market_sort_type

    @property
    def asc_or_desc(self):
        """Gets the asc_or_desc of this MallParaDTO.

        升序、降序。

        :return: The asc_or_desc of this MallParaDTO.
        :rtype: str
        """
        return self._asc_or_desc

    @asc_or_desc.setter
    def asc_or_desc(self, asc_or_desc):
        """Sets the asc_or_desc of this MallParaDTO.

        升序、降序。

        :param asc_or_desc: The asc_or_desc of this MallParaDTO.
        :type asc_or_desc: str
        """
        self._asc_or_desc = asc_or_desc

    @property
    def offset(self):
        """Gets the offset of this MallParaDTO.

        查询起始坐标。

        :return: The offset of this MallParaDTO.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this MallParaDTO.

        查询起始坐标。

        :param offset: The offset of this MallParaDTO.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this MallParaDTO.

        查询条数。

        :return: The limit of this MallParaDTO.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this MallParaDTO.

        查询条数。

        :param limit: The limit of this MallParaDTO.
        :type limit: int
        """
        self._limit = limit

    @property
    def is_owner(self):
        """Gets the is_owner of this MallParaDTO.

        是否显示拥有者。

        :return: The is_owner of this MallParaDTO.
        :rtype: bool
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        """Sets the is_owner of this MallParaDTO.

        是否显示拥有者。

        :param is_owner: The is_owner of this MallParaDTO.
        :type is_owner: bool
        """
        self._is_owner = is_owner

    @property
    def is_authorized(self):
        """Gets the is_authorized of this MallParaDTO.

        是否显示已被授权。

        :return: The is_authorized of this MallParaDTO.
        :rtype: bool
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        """Sets the is_authorized of this MallParaDTO.

        是否显示已被授权。

        :param is_authorized: The is_authorized of this MallParaDTO.
        :type is_authorized: bool
        """
        self._is_authorized = is_authorized

    @property
    def is_update_recently(self):
        """Gets the is_update_recently of this MallParaDTO.

        是否显示最近更新。

        :return: The is_update_recently of this MallParaDTO.
        :rtype: bool
        """
        return self._is_update_recently

    @is_update_recently.setter
    def is_update_recently(self, is_update_recently):
        """Sets the is_update_recently of this MallParaDTO.

        是否显示最近更新。

        :param is_update_recently: The is_update_recently of this MallParaDTO.
        :type is_update_recently: bool
        """
        self._is_update_recently = is_update_recently

    @property
    def is_release_recently(self):
        """Gets the is_release_recently of this MallParaDTO.

        是否显示最近发布。

        :return: The is_release_recently of this MallParaDTO.
        :rtype: bool
        """
        return self._is_release_recently

    @is_release_recently.setter
    def is_release_recently(self, is_release_recently):
        """Sets the is_release_recently of this MallParaDTO.

        是否显示最近发布。

        :param is_release_recently: The is_release_recently of this MallParaDTO.
        :type is_release_recently: bool
        """
        self._is_release_recently = is_release_recently

    @property
    def is_hot_recently(self):
        """Gets the is_hot_recently of this MallParaDTO.

        是否显示热销状态。

        :return: The is_hot_recently of this MallParaDTO.
        :rtype: bool
        """
        return self._is_hot_recently

    @is_hot_recently.setter
    def is_hot_recently(self, is_hot_recently):
        """Sets the is_hot_recently of this MallParaDTO.

        是否显示热销状态。

        :param is_hot_recently: The is_hot_recently of this MallParaDTO.
        :type is_hot_recently: bool
        """
        self._is_hot_recently = is_hot_recently

    @property
    def success_and_failure_rate(self):
        """Gets the success_and_failure_rate of this MallParaDTO.

        是否显示7天内成功率与失败率。

        :return: The success_and_failure_rate of this MallParaDTO.
        :rtype: bool
        """
        return self._success_and_failure_rate

    @success_and_failure_rate.setter
    def success_and_failure_rate(self, success_and_failure_rate):
        """Sets the success_and_failure_rate of this MallParaDTO.

        是否显示7天内成功率与失败率。

        :param success_and_failure_rate: The success_and_failure_rate of this MallParaDTO.
        :type success_and_failure_rate: bool
        """
        self._success_and_failure_rate = success_and_failure_rate

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
        if not isinstance(other, MallParaDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
