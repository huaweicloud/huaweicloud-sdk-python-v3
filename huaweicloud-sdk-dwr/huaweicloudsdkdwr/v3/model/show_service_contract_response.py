# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServiceContractResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreement_type': 'str',
        'create_time': 'str',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'agreement_type': 'agreement_type',
        'create_time': 'create_time',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, agreement_type=None, create_time=None, x_request_id=None, connection=None, content_length=None, date=None):
        """ShowServiceContractResponse

        The model defined in huaweicloud sdk

        :param agreement_type: 服务协议类型,默认为use_public_action_privacy_statement。
        :type agreement_type: str
        :param create_time: 同意时间。
        :type create_time: str
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ShowServiceContractResponse, self).__init__()

        self._agreement_type = None
        self._create_time = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if agreement_type is not None:
            self.agreement_type = agreement_type
        if create_time is not None:
            self.create_time = create_time
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def agreement_type(self):
        """Gets the agreement_type of this ShowServiceContractResponse.

        服务协议类型,默认为use_public_action_privacy_statement。

        :return: The agreement_type of this ShowServiceContractResponse.
        :rtype: str
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, agreement_type):
        """Sets the agreement_type of this ShowServiceContractResponse.

        服务协议类型,默认为use_public_action_privacy_statement。

        :param agreement_type: The agreement_type of this ShowServiceContractResponse.
        :type agreement_type: str
        """
        self._agreement_type = agreement_type

    @property
    def create_time(self):
        """Gets the create_time of this ShowServiceContractResponse.

        同意时间。

        :return: The create_time of this ShowServiceContractResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowServiceContractResponse.

        同意时间。

        :param create_time: The create_time of this ShowServiceContractResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowServiceContractResponse.

        :return: The x_request_id of this ShowServiceContractResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowServiceContractResponse.

        :param x_request_id: The x_request_id of this ShowServiceContractResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this ShowServiceContractResponse.

        :return: The connection of this ShowServiceContractResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ShowServiceContractResponse.

        :param connection: The connection of this ShowServiceContractResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this ShowServiceContractResponse.

        :return: The content_length of this ShowServiceContractResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ShowServiceContractResponse.

        :param content_length: The content_length of this ShowServiceContractResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this ShowServiceContractResponse.

        :return: The date of this ShowServiceContractResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ShowServiceContractResponse.

        :param date: The date of this ShowServiceContractResponse.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, ShowServiceContractResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
