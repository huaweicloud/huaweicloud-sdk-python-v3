# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClientIpInfoResponse(SdkResponse):

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
        'ips': 'list[str]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ips': 'ips',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, ips=None, x_request_id=None):
        r"""ShowClientIpInfoResponse

        The model defined in huaweicloud sdk

        :param id: 文件系统ID
        :type id: str
        :param ips: 已挂载客户端的IP
        :type ips: list[str]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowClientIpInfoResponse, self).__init__()

        self._id = None
        self._ips = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ips is not None:
            self.ips = ips
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this ShowClientIpInfoResponse.

        文件系统ID

        :return: The id of this ShowClientIpInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowClientIpInfoResponse.

        文件系统ID

        :param id: The id of this ShowClientIpInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def ips(self):
        r"""Gets the ips of this ShowClientIpInfoResponse.

        已挂载客户端的IP

        :return: The ips of this ShowClientIpInfoResponse.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this ShowClientIpInfoResponse.

        已挂载客户端的IP

        :param ips: The ips of this ShowClientIpInfoResponse.
        :type ips: list[str]
        """
        self._ips = ips

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowClientIpInfoResponse.

        :return: The x_request_id of this ShowClientIpInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowClientIpInfoResponse.

        :param x_request_id: The x_request_id of this ShowClientIpInfoResponse.
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
        if not isinstance(other, ShowClientIpInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
