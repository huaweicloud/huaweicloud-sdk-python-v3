# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutObjectResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "PutObjectResponse"

    sensitive_list = []

    openapi_types = {
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'e_tag': 'str',
        'x_obs_server_side_encryption': 'str',
        'x_obs_server_side_encryption_customer_algorithm': 'str',
        'x_obs_storage_class': 'str',
        'connection': 'str',
        'x_obs_server_side_encryption_customer_key_md5': 'str',
        'x_obs_server_side_encryption_kms_key_id': 'str',
        'content_length': 'str',
        'date': 'str',
        'x_obs_version_id': 'str'
    }

    attribute_map = {
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'e_tag': 'ETag',
        'x_obs_server_side_encryption': 'x-obs-server-side-encryption',
        'x_obs_server_side_encryption_customer_algorithm': 'x-obs-server-side-encryption-customer-algorithm',
        'x_obs_storage_class': 'x-obs-storage-class',
        'connection': 'Connection',
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5',
        'x_obs_server_side_encryption_kms_key_id': 'x-obs-server-side-encryption-kms-key-id',
        'content_length': 'Content-Length',
        'date': 'Date',
        'x_obs_version_id': 'x-obs-version-id'
    }

    def __init__(self, x_obs_id_2=None, x_obs_request_id=None, e_tag=None, x_obs_server_side_encryption=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_storage_class=None, connection=None, x_obs_server_side_encryption_customer_key_md5=None, x_obs_server_side_encryption_kms_key_id=None, content_length=None, date=None, x_obs_version_id=None):
        r"""PutObjectResponse

        The model defined in huaweicloud sdk

        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param e_tag: 
        :type e_tag: str
        :param x_obs_server_side_encryption: 
        :type x_obs_server_side_encryption: str
        :param x_obs_server_side_encryption_customer_algorithm: 
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_storage_class: 
        :type x_obs_storage_class: str
        :param connection: 
        :type connection: str
        :param x_obs_server_side_encryption_customer_key_md5: 
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param x_obs_server_side_encryption_kms_key_id: 
        :type x_obs_server_side_encryption_kms_key_id: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        :param x_obs_version_id: 
        :type x_obs_version_id: str
        """
        
        super(PutObjectResponse, self).__init__()

        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._e_tag = None
        self._x_obs_server_side_encryption = None
        self._x_obs_server_side_encryption_customer_algorithm = None
        self._x_obs_storage_class = None
        self._connection = None
        self._x_obs_server_side_encryption_customer_key_md5 = None
        self._x_obs_server_side_encryption_kms_key_id = None
        self._content_length = None
        self._date = None
        self._x_obs_version_id = None
        self.discriminator = None

        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if e_tag is not None:
            self.e_tag = e_tag
        if x_obs_server_side_encryption is not None:
            self.x_obs_server_side_encryption = x_obs_server_side_encryption
        if x_obs_server_side_encryption_customer_algorithm is not None:
            self.x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
        if connection is not None:
            self.connection = connection
        if x_obs_server_side_encryption_customer_key_md5 is not None:
            self.x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5
        if x_obs_server_side_encryption_kms_key_id is not None:
            self.x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date
        if x_obs_version_id is not None:
            self.x_obs_version_id = x_obs_version_id

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this PutObjectResponse.

        :return: The x_obs_id_2 of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this PutObjectResponse.

        :param x_obs_id_2: The x_obs_id_2 of this PutObjectResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this PutObjectResponse.

        :return: The x_obs_request_id of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this PutObjectResponse.

        :param x_obs_request_id: The x_obs_request_id of this PutObjectResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def e_tag(self):
        r"""Gets the e_tag of this PutObjectResponse.

        :return: The e_tag of this PutObjectResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this PutObjectResponse.

        :param e_tag: The e_tag of this PutObjectResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def x_obs_server_side_encryption(self):
        r"""Gets the x_obs_server_side_encryption of this PutObjectResponse.

        :return: The x_obs_server_side_encryption of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        r"""Sets the x_obs_server_side_encryption of this PutObjectResponse.

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this PutObjectResponse.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this PutObjectResponse.

        :return: The x_obs_server_side_encryption_customer_algorithm of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this PutObjectResponse.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this PutObjectResponse.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_storage_class(self):
        r"""Gets the x_obs_storage_class of this PutObjectResponse.

        :return: The x_obs_storage_class of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        r"""Sets the x_obs_storage_class of this PutObjectResponse.

        :param x_obs_storage_class: The x_obs_storage_class of this PutObjectResponse.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def connection(self):
        r"""Gets the connection of this PutObjectResponse.

        :return: The connection of this PutObjectResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this PutObjectResponse.

        :param connection: The connection of this PutObjectResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this PutObjectResponse.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this PutObjectResponse.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this PutObjectResponse.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        r"""Gets the x_obs_server_side_encryption_kms_key_id of this PutObjectResponse.

        :return: The x_obs_server_side_encryption_kms_key_id of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        r"""Sets the x_obs_server_side_encryption_kms_key_id of this PutObjectResponse.

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this PutObjectResponse.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def content_length(self):
        r"""Gets the content_length of this PutObjectResponse.

        :return: The content_length of this PutObjectResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this PutObjectResponse.

        :param content_length: The content_length of this PutObjectResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this PutObjectResponse.

        :return: The date of this PutObjectResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this PutObjectResponse.

        :param date: The date of this PutObjectResponse.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_version_id(self):
        r"""Gets the x_obs_version_id of this PutObjectResponse.

        :return: The x_obs_version_id of this PutObjectResponse.
        :rtype: str
        """
        return self._x_obs_version_id

    @x_obs_version_id.setter
    def x_obs_version_id(self, x_obs_version_id):
        r"""Sets the x_obs_version_id of this PutObjectResponse.

        :param x_obs_version_id: The x_obs_version_id of this PutObjectResponse.
        :type x_obs_version_id: str
        """
        self._x_obs_version_id = x_obs_version_id

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
        if not isinstance(other, PutObjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
