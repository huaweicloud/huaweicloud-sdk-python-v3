# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketNotificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketNotificationResponse"

    sensitive_list = []

    openapi_types = {
        'notification_configuration': 'SetBucketNotificationRequestBody',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'e_tag': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'notification_configuration': 'NotificationConfiguration',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'e_tag': 'ETag',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, notification_configuration=None, x_obs_id_2=None, x_obs_request_id=None, e_tag=None, connection=None, content_length=None, date=None):
        r"""GetBucketNotificationResponse

        The model defined in huaweicloud sdk

        :param notification_configuration: 
        :type notification_configuration: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequestBody`
        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param e_tag: 
        :type e_tag: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(GetBucketNotificationResponse, self).__init__()

        self._notification_configuration = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._e_tag = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if notification_configuration is not None:
            self.notification_configuration = notification_configuration
        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if e_tag is not None:
            self.e_tag = e_tag
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def notification_configuration(self):
        r"""Gets the notification_configuration of this GetBucketNotificationResponse.

        :return: The notification_configuration of this GetBucketNotificationResponse.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequestBody`
        """
        return self._notification_configuration

    @notification_configuration.setter
    def notification_configuration(self, notification_configuration):
        r"""Sets the notification_configuration of this GetBucketNotificationResponse.

        :param notification_configuration: The notification_configuration of this GetBucketNotificationResponse.
        :type notification_configuration: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequestBody`
        """
        self._notification_configuration = notification_configuration

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this GetBucketNotificationResponse.

        :return: The x_obs_id_2 of this GetBucketNotificationResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this GetBucketNotificationResponse.

        :param x_obs_id_2: The x_obs_id_2 of this GetBucketNotificationResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this GetBucketNotificationResponse.

        :return: The x_obs_request_id of this GetBucketNotificationResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this GetBucketNotificationResponse.

        :param x_obs_request_id: The x_obs_request_id of this GetBucketNotificationResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def e_tag(self):
        r"""Gets the e_tag of this GetBucketNotificationResponse.

        :return: The e_tag of this GetBucketNotificationResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this GetBucketNotificationResponse.

        :param e_tag: The e_tag of this GetBucketNotificationResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def connection(self):
        r"""Gets the connection of this GetBucketNotificationResponse.

        :return: The connection of this GetBucketNotificationResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this GetBucketNotificationResponse.

        :param connection: The connection of this GetBucketNotificationResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this GetBucketNotificationResponse.

        :return: The content_length of this GetBucketNotificationResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this GetBucketNotificationResponse.

        :param content_length: The content_length of this GetBucketNotificationResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this GetBucketNotificationResponse.

        :return: The date of this GetBucketNotificationResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketNotificationResponse.

        :param date: The date of this GetBucketNotificationResponse.
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
        if not isinstance(other, GetBucketNotificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
