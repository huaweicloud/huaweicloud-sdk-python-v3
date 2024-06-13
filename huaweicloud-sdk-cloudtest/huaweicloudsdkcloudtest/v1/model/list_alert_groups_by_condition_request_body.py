# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertGroupsByConditionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_ids': 'list[str]',
        'page_num': 'int',
        'page_size': 'int',
        'test_service_id': 'str',
        'user_ids': 'list[str]',
        'user_name': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_ids': 'group_ids',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'test_service_id': 'test_service_id',
        'user_ids': 'userIds',
        'user_name': 'userName'
    }

    def __init__(self, group_id=None, group_ids=None, page_num=None, page_size=None, test_service_id=None, user_ids=None, user_name=None):
        """ListAlertGroupsByConditionRequestBody

        The model defined in huaweicloud sdk

        :param group_id: 告警组ID
        :type group_id: str
        :param group_ids: 告警组ID列表
        :type group_ids: list[str]
        :param page_num: 当前页数
        :type page_num: int
        :param page_size: 每页大小
        :type page_size: int
        :param test_service_id: 服务ID
        :type test_service_id: str
        :param user_ids: 用户ID列表
        :type user_ids: list[str]
        :param user_name: 用户名
        :type user_name: str
        """
        
        

        self._group_id = None
        self._group_ids = None
        self._page_num = None
        self._page_size = None
        self._test_service_id = None
        self._user_ids = None
        self._user_name = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_ids is not None:
            self.group_ids = group_ids
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if test_service_id is not None:
            self.test_service_id = test_service_id
        if user_ids is not None:
            self.user_ids = user_ids
        if user_name is not None:
            self.user_name = user_name

    @property
    def group_id(self):
        """Gets the group_id of this ListAlertGroupsByConditionRequestBody.

        告警组ID

        :return: The group_id of this ListAlertGroupsByConditionRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListAlertGroupsByConditionRequestBody.

        告警组ID

        :param group_id: The group_id of this ListAlertGroupsByConditionRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_ids(self):
        """Gets the group_ids of this ListAlertGroupsByConditionRequestBody.

        告警组ID列表

        :return: The group_ids of this ListAlertGroupsByConditionRequestBody.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this ListAlertGroupsByConditionRequestBody.

        告警组ID列表

        :param group_ids: The group_ids of this ListAlertGroupsByConditionRequestBody.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

    @property
    def page_num(self):
        """Gets the page_num of this ListAlertGroupsByConditionRequestBody.

        当前页数

        :return: The page_num of this ListAlertGroupsByConditionRequestBody.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListAlertGroupsByConditionRequestBody.

        当前页数

        :param page_num: The page_num of this ListAlertGroupsByConditionRequestBody.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListAlertGroupsByConditionRequestBody.

        每页大小

        :return: The page_size of this ListAlertGroupsByConditionRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListAlertGroupsByConditionRequestBody.

        每页大小

        :param page_size: The page_size of this ListAlertGroupsByConditionRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def test_service_id(self):
        """Gets the test_service_id of this ListAlertGroupsByConditionRequestBody.

        服务ID

        :return: The test_service_id of this ListAlertGroupsByConditionRequestBody.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        """Sets the test_service_id of this ListAlertGroupsByConditionRequestBody.

        服务ID

        :param test_service_id: The test_service_id of this ListAlertGroupsByConditionRequestBody.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

    @property
    def user_ids(self):
        """Gets the user_ids of this ListAlertGroupsByConditionRequestBody.

        用户ID列表

        :return: The user_ids of this ListAlertGroupsByConditionRequestBody.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this ListAlertGroupsByConditionRequestBody.

        用户ID列表

        :param user_ids: The user_ids of this ListAlertGroupsByConditionRequestBody.
        :type user_ids: list[str]
        """
        self._user_ids = user_ids

    @property
    def user_name(self):
        """Gets the user_name of this ListAlertGroupsByConditionRequestBody.

        用户名

        :return: The user_name of this ListAlertGroupsByConditionRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListAlertGroupsByConditionRequestBody.

        用户名

        :param user_name: The user_name of this ListAlertGroupsByConditionRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ListAlertGroupsByConditionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
