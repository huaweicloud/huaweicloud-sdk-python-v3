# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'authorization': 'str',
        'x_sdk_date': 'str',
        'x_project_id': 'str',
        'app_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'app_id': 'app_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, content_type=None, authorization=None, x_sdk_date=None, x_project_id=None, app_id=None, offset=None, limit=None):
        """ListRecordRulesRequest

        The model defined in huaweicloud sdk

        :param content_type: 内容类型。
        :type content_type: str
        :param authorization: 使用AK/SK方式认证时必选，携带的鉴权信息。
        :type authorization: str
        :param x_sdk_date: 使用AK/SK方式认证时必选，请求的发生时间。
        :type x_sdk_date: str
        :param x_project_id: 使用AK/SK方式认证时必选，携带项目ID信息。
        :type x_project_id: str
        :param app_id: 应用id
        :type app_id: str
        :param offset: 查询结果起始编号，此处代表分页的页码
        :type offset: int
        :param limit: 查询结果集数量，此处代表每一页的条数
        :type limit: int
        """
        
        

        self._content_type = None
        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._app_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.content_type = content_type
        if authorization is not None:
            self.authorization = authorization
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.app_id = app_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def content_type(self):
        """Gets the content_type of this ListRecordRulesRequest.

        内容类型。

        :return: The content_type of this ListRecordRulesRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListRecordRulesRequest.

        内容类型。

        :param content_type: The content_type of this ListRecordRulesRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def authorization(self):
        """Gets the authorization of this ListRecordRulesRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。

        :return: The authorization of this ListRecordRulesRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListRecordRulesRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。

        :param authorization: The authorization of this ListRecordRulesRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListRecordRulesRequest.

        使用AK/SK方式认证时必选，请求的发生时间。

        :return: The x_sdk_date of this ListRecordRulesRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListRecordRulesRequest.

        使用AK/SK方式认证时必选，请求的发生时间。

        :param x_sdk_date: The x_sdk_date of this ListRecordRulesRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListRecordRulesRequest.

        使用AK/SK方式认证时必选，携带项目ID信息。

        :return: The x_project_id of this ListRecordRulesRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListRecordRulesRequest.

        使用AK/SK方式认证时必选，携带项目ID信息。

        :param x_project_id: The x_project_id of this ListRecordRulesRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def app_id(self):
        """Gets the app_id of this ListRecordRulesRequest.

        应用id

        :return: The app_id of this ListRecordRulesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListRecordRulesRequest.

        应用id

        :param app_id: The app_id of this ListRecordRulesRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def offset(self):
        """Gets the offset of this ListRecordRulesRequest.

        查询结果起始编号，此处代表分页的页码

        :return: The offset of this ListRecordRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRecordRulesRequest.

        查询结果起始编号，此处代表分页的页码

        :param offset: The offset of this ListRecordRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRecordRulesRequest.

        查询结果集数量，此处代表每一页的条数

        :return: The limit of this ListRecordRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRecordRulesRequest.

        查询结果集数量，此处代表每一页的条数

        :param limit: The limit of this ListRecordRulesRequest.
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
        if not isinstance(other, ListRecordRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
