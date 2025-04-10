# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceAccesslog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'request_id': 'str',
        'api_id': 'str',
        'api_name': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'access_time': 'int',
        'duration': 'int',
        'status_code': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'detail': 'str',
        'in_flow_size': 'int',
        'out_flow_size': 'int',
        'out_total_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'request_id': 'request_id',
        'api_id': 'api_id',
        'api_name': 'api_name',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'access_time': 'access_time',
        'duration': 'duration',
        'status_code': 'status_code',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'detail': 'detail',
        'in_flow_size': 'in_flow_size',
        'out_flow_size': 'out_flow_size',
        'out_total_size': 'out_total_size'
    }

    def __init__(self, id=None, request_id=None, api_id=None, api_name=None, app_id=None, app_name=None, access_time=None, duration=None, status_code=None, error_code=None, error_message=None, detail=None, in_flow_size=None, out_flow_size=None, out_total_size=None):
        r"""InstanceAccesslog

        The model defined in huaweicloud sdk

        :param id: 集群ID。
        :type id: str
        :param request_id: 请求ID。
        :type request_id: str
        :param api_id: API ID。
        :type api_id: str
        :param api_name: API名称。
        :type api_name: str
        :param app_id: APP ID。
        :type app_id: str
        :param app_name: APP名称。
        :type app_name: str
        :param access_time: 访问时间。
        :type access_time: int
        :param duration: 访问时长。
        :type duration: int
        :param status_code: 状态码。
        :type status_code: str
        :param error_code: 错误码。
        :type error_code: str
        :param error_message: 错误信息。
        :type error_message: str
        :param detail: 日志详情。
        :type detail: str
        :param in_flow_size: 输入流量大小。
        :type in_flow_size: int
        :param out_flow_size: 输出流量大小。
        :type out_flow_size: int
        :param out_total_size: 输出数据条数。
        :type out_total_size: int
        """
        
        

        self._id = None
        self._request_id = None
        self._api_id = None
        self._api_name = None
        self._app_id = None
        self._app_name = None
        self._access_time = None
        self._duration = None
        self._status_code = None
        self._error_code = None
        self._error_message = None
        self._detail = None
        self._in_flow_size = None
        self._out_flow_size = None
        self._out_total_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if request_id is not None:
            self.request_id = request_id
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if access_time is not None:
            self.access_time = access_time
        if duration is not None:
            self.duration = duration
        if status_code is not None:
            self.status_code = status_code
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if detail is not None:
            self.detail = detail
        if in_flow_size is not None:
            self.in_flow_size = in_flow_size
        if out_flow_size is not None:
            self.out_flow_size = out_flow_size
        if out_total_size is not None:
            self.out_total_size = out_total_size

    @property
    def id(self):
        r"""Gets the id of this InstanceAccesslog.

        集群ID。

        :return: The id of this InstanceAccesslog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceAccesslog.

        集群ID。

        :param id: The id of this InstanceAccesslog.
        :type id: str
        """
        self._id = id

    @property
    def request_id(self):
        r"""Gets the request_id of this InstanceAccesslog.

        请求ID。

        :return: The request_id of this InstanceAccesslog.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this InstanceAccesslog.

        请求ID。

        :param request_id: The request_id of this InstanceAccesslog.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def api_id(self):
        r"""Gets the api_id of this InstanceAccesslog.

        API ID。

        :return: The api_id of this InstanceAccesslog.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this InstanceAccesslog.

        API ID。

        :param api_id: The api_id of this InstanceAccesslog.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        r"""Gets the api_name of this InstanceAccesslog.

        API名称。

        :return: The api_name of this InstanceAccesslog.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this InstanceAccesslog.

        API名称。

        :param api_name: The api_name of this InstanceAccesslog.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def app_id(self):
        r"""Gets the app_id of this InstanceAccesslog.

        APP ID。

        :return: The app_id of this InstanceAccesslog.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this InstanceAccesslog.

        APP ID。

        :param app_id: The app_id of this InstanceAccesslog.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this InstanceAccesslog.

        APP名称。

        :return: The app_name of this InstanceAccesslog.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this InstanceAccesslog.

        APP名称。

        :param app_name: The app_name of this InstanceAccesslog.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def access_time(self):
        r"""Gets the access_time of this InstanceAccesslog.

        访问时间。

        :return: The access_time of this InstanceAccesslog.
        :rtype: int
        """
        return self._access_time

    @access_time.setter
    def access_time(self, access_time):
        r"""Sets the access_time of this InstanceAccesslog.

        访问时间。

        :param access_time: The access_time of this InstanceAccesslog.
        :type access_time: int
        """
        self._access_time = access_time

    @property
    def duration(self):
        r"""Gets the duration of this InstanceAccesslog.

        访问时长。

        :return: The duration of this InstanceAccesslog.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this InstanceAccesslog.

        访问时长。

        :param duration: The duration of this InstanceAccesslog.
        :type duration: int
        """
        self._duration = duration

    @property
    def status_code(self):
        r"""Gets the status_code of this InstanceAccesslog.

        状态码。

        :return: The status_code of this InstanceAccesslog.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this InstanceAccesslog.

        状态码。

        :param status_code: The status_code of this InstanceAccesslog.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def error_code(self):
        r"""Gets the error_code of this InstanceAccesslog.

        错误码。

        :return: The error_code of this InstanceAccesslog.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this InstanceAccesslog.

        错误码。

        :param error_code: The error_code of this InstanceAccesslog.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this InstanceAccesslog.

        错误信息。

        :return: The error_message of this InstanceAccesslog.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this InstanceAccesslog.

        错误信息。

        :param error_message: The error_message of this InstanceAccesslog.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def detail(self):
        r"""Gets the detail of this InstanceAccesslog.

        日志详情。

        :return: The detail of this InstanceAccesslog.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this InstanceAccesslog.

        日志详情。

        :param detail: The detail of this InstanceAccesslog.
        :type detail: str
        """
        self._detail = detail

    @property
    def in_flow_size(self):
        r"""Gets the in_flow_size of this InstanceAccesslog.

        输入流量大小。

        :return: The in_flow_size of this InstanceAccesslog.
        :rtype: int
        """
        return self._in_flow_size

    @in_flow_size.setter
    def in_flow_size(self, in_flow_size):
        r"""Sets the in_flow_size of this InstanceAccesslog.

        输入流量大小。

        :param in_flow_size: The in_flow_size of this InstanceAccesslog.
        :type in_flow_size: int
        """
        self._in_flow_size = in_flow_size

    @property
    def out_flow_size(self):
        r"""Gets the out_flow_size of this InstanceAccesslog.

        输出流量大小。

        :return: The out_flow_size of this InstanceAccesslog.
        :rtype: int
        """
        return self._out_flow_size

    @out_flow_size.setter
    def out_flow_size(self, out_flow_size):
        r"""Sets the out_flow_size of this InstanceAccesslog.

        输出流量大小。

        :param out_flow_size: The out_flow_size of this InstanceAccesslog.
        :type out_flow_size: int
        """
        self._out_flow_size = out_flow_size

    @property
    def out_total_size(self):
        r"""Gets the out_total_size of this InstanceAccesslog.

        输出数据条数。

        :return: The out_total_size of this InstanceAccesslog.
        :rtype: int
        """
        return self._out_total_size

    @out_total_size.setter
    def out_total_size(self, out_total_size):
        r"""Sets the out_total_size of this InstanceAccesslog.

        输出数据条数。

        :param out_total_size: The out_total_size of this InstanceAccesslog.
        :type out_total_size: int
        """
        self._out_total_size = out_total_size

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
        if not isinstance(other, InstanceAccesslog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
