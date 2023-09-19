# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveEventReportRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'job_id': 'str',
        'x_app_user_id': 'str',
        'auth_key': 'str',
        'expires_time': 'int',
        'refresh_url': 'bool',
        'body': 'ReportLiveEventReq'
    }

    attribute_map = {
        'room_id': 'room_id',
        'job_id': 'job_id',
        'x_app_user_id': 'X-App-UserId',
        'auth_key': 'auth_key',
        'expires_time': 'expires_time',
        'refresh_url': 'refresh_url',
        'body': 'body'
    }

    def __init__(self, room_id=None, job_id=None, x_app_user_id=None, auth_key=None, expires_time=None, refresh_url=None, body=None):
        """LiveEventReportRequest

        The model defined in huaweicloud sdk

        :param room_id: 剧本ID。
        :type room_id: str
        :param job_id: 任务ID。
        :type job_id: str
        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param auth_key: 鉴权Key。通过HmacSHA256生成的鉴权key
        :type auth_key: str
        :param expires_time: 鉴权key过期时间。从1970年1月1日（UTC/GMT的午夜）开始所经过的豪秒数。
        :type expires_time: int
        :param refresh_url: 是否刷新URL
        :type refresh_url: bool
        :param body: Body of the LiveEventReportRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.ReportLiveEventReq`
        """
        
        

        self._room_id = None
        self._job_id = None
        self._x_app_user_id = None
        self._auth_key = None
        self._expires_time = None
        self._refresh_url = None
        self._body = None
        self.discriminator = None

        self.room_id = room_id
        self.job_id = job_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if auth_key is not None:
            self.auth_key = auth_key
        if expires_time is not None:
            self.expires_time = expires_time
        if refresh_url is not None:
            self.refresh_url = refresh_url
        if body is not None:
            self.body = body

    @property
    def room_id(self):
        """Gets the room_id of this LiveEventReportRequest.

        剧本ID。

        :return: The room_id of this LiveEventReportRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this LiveEventReportRequest.

        剧本ID。

        :param room_id: The room_id of this LiveEventReportRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def job_id(self):
        """Gets the job_id of this LiveEventReportRequest.

        任务ID。

        :return: The job_id of this LiveEventReportRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this LiveEventReportRequest.

        任务ID。

        :param job_id: The job_id of this LiveEventReportRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this LiveEventReportRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this LiveEventReportRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this LiveEventReportRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this LiveEventReportRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def auth_key(self):
        """Gets the auth_key of this LiveEventReportRequest.

        鉴权Key。通过HmacSHA256生成的鉴权key

        :return: The auth_key of this LiveEventReportRequest.
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this LiveEventReportRequest.

        鉴权Key。通过HmacSHA256生成的鉴权key

        :param auth_key: The auth_key of this LiveEventReportRequest.
        :type auth_key: str
        """
        self._auth_key = auth_key

    @property
    def expires_time(self):
        """Gets the expires_time of this LiveEventReportRequest.

        鉴权key过期时间。从1970年1月1日（UTC/GMT的午夜）开始所经过的豪秒数。

        :return: The expires_time of this LiveEventReportRequest.
        :rtype: int
        """
        return self._expires_time

    @expires_time.setter
    def expires_time(self, expires_time):
        """Sets the expires_time of this LiveEventReportRequest.

        鉴权key过期时间。从1970年1月1日（UTC/GMT的午夜）开始所经过的豪秒数。

        :param expires_time: The expires_time of this LiveEventReportRequest.
        :type expires_time: int
        """
        self._expires_time = expires_time

    @property
    def refresh_url(self):
        """Gets the refresh_url of this LiveEventReportRequest.

        是否刷新URL

        :return: The refresh_url of this LiveEventReportRequest.
        :rtype: bool
        """
        return self._refresh_url

    @refresh_url.setter
    def refresh_url(self, refresh_url):
        """Sets the refresh_url of this LiveEventReportRequest.

        是否刷新URL

        :param refresh_url: The refresh_url of this LiveEventReportRequest.
        :type refresh_url: bool
        """
        self._refresh_url = refresh_url

    @property
    def body(self):
        """Gets the body of this LiveEventReportRequest.

        :return: The body of this LiveEventReportRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReportLiveEventReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this LiveEventReportRequest.

        :param body: The body of this LiveEventReportRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.ReportLiveEventReq`
        """
        self._body = body

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
        if not isinstance(other, LiveEventReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
