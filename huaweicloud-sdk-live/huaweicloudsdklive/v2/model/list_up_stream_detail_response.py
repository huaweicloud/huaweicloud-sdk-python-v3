# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpStreamDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'data': 'list[UpStreamDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'data': 'data',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, data=None, x_request_id=None):
        r"""ListUpStreamDetailResponse

        The model defined in huaweicloud sdk

        :param publish_domain: 推流域名
        :type publish_domain: str
        :param app: 应用名
        :type app: str
        :param stream: 流名
        :type stream: str
        :param data: 推流质量数据
        :type data: list[:class:`huaweicloudsdklive.v2.UpStreamDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListUpStreamDetailResponse, self).__init__()

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if publish_domain is not None:
            self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def publish_domain(self):
        r"""Gets the publish_domain of this ListUpStreamDetailResponse.

        推流域名

        :return: The publish_domain of this ListUpStreamDetailResponse.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        r"""Sets the publish_domain of this ListUpStreamDetailResponse.

        推流域名

        :param publish_domain: The publish_domain of this ListUpStreamDetailResponse.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        r"""Gets the app of this ListUpStreamDetailResponse.

        应用名

        :return: The app of this ListUpStreamDetailResponse.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ListUpStreamDetailResponse.

        应用名

        :param app: The app of this ListUpStreamDetailResponse.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this ListUpStreamDetailResponse.

        流名

        :return: The stream of this ListUpStreamDetailResponse.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this ListUpStreamDetailResponse.

        流名

        :param stream: The stream of this ListUpStreamDetailResponse.
        :type stream: str
        """
        self._stream = stream

    @property
    def data(self):
        r"""Gets the data of this ListUpStreamDetailResponse.

        推流质量数据

        :return: The data of this ListUpStreamDetailResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.UpStreamDetail`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListUpStreamDetailResponse.

        推流质量数据

        :param data: The data of this ListUpStreamDetailResponse.
        :type data: list[:class:`huaweicloudsdklive.v2.UpStreamDetail`]
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListUpStreamDetailResponse.

        :return: The x_request_id of this ListUpStreamDetailResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListUpStreamDetailResponse.

        :param x_request_id: The x_request_id of this ListUpStreamDetailResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListUpStreamDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
