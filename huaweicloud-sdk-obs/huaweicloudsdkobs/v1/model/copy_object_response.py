# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyObjectResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "CopyObjectResponse"

    sensitive_list = []

    openapi_types = {
        'last_modified': 'str',
        'e_tag': 'str',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'x_obs_server_side_encryption': 'str',
        'connection': 'str',
        'x_obs_server_side_encryption_customer_key_md5': 'str',
        'date': 'str',
        'x_obs_server_side_encryption_customer_algorithm': 'str',
        'x_obs_copy_source_version_id': 'str',
        'x_obs_storage_class': 'str',
        'x_obs_server_side_encryption_kms_key_id': 'str',
        'content_length': 'str',
        'x_obs_version_id': 'str'
    }

    attribute_map = {
        'last_modified': 'LastModified',
        'e_tag': 'ETag',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'x_obs_server_side_encryption': 'x-obs-server-side-encryption',
        'connection': 'Connection',
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5',
        'date': 'Date',
        'x_obs_server_side_encryption_customer_algorithm': 'x-obs-server-side-encryption-customer-algorithm',
        'x_obs_copy_source_version_id': 'x-obs-copy-source-version-id',
        'x_obs_storage_class': 'x-obs-storage-class',
        'x_obs_server_side_encryption_kms_key_id': 'x-obs-server-side-encryption-kms-key-id',
        'content_length': 'Content-Length',
        'x_obs_version_id': 'x-obs-version-id'
    }

    def __init__(self, last_modified=None, e_tag=None, x_obs_id_2=None, x_obs_request_id=None, x_obs_server_side_encryption=None, connection=None, x_obs_server_side_encryption_customer_key_md5=None, date=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_copy_source_version_id=None, x_obs_storage_class=None, x_obs_server_side_encryption_kms_key_id=None, content_length=None, x_obs_version_id=None):
        r"""CopyObjectResponse

        The model defined in huaweicloud sdk

        :param last_modified: Time when the object was last modified
        :type last_modified: str
        :param e_tag: 
        :type e_tag: str
        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param x_obs_server_side_encryption: 
        :type x_obs_server_side_encryption: str
        :param connection: 
        :type connection: str
        :param x_obs_server_side_encryption_customer_key_md5: 
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param date: 
        :type date: str
        :param x_obs_server_side_encryption_customer_algorithm: 
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_copy_source_version_id: 
        :type x_obs_copy_source_version_id: str
        :param x_obs_storage_class: 
        :type x_obs_storage_class: str
        :param x_obs_server_side_encryption_kms_key_id: 
        :type x_obs_server_side_encryption_kms_key_id: str
        :param content_length: 
        :type content_length: str
        :param x_obs_version_id: 
        :type x_obs_version_id: str
        """
        
        super(CopyObjectResponse, self).__init__()

        self._last_modified = None
        self._e_tag = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._x_obs_server_side_encryption = None
        self._connection = None
        self._x_obs_server_side_encryption_customer_key_md5 = None
        self._date = None
        self._x_obs_server_side_encryption_customer_algorithm = None
        self._x_obs_copy_source_version_id = None
        self._x_obs_storage_class = None
        self._x_obs_server_side_encryption_kms_key_id = None
        self._content_length = None
        self._x_obs_version_id = None
        self.discriminator = None

        if last_modified is not None:
            self.last_modified = last_modified
        if e_tag is not None:
            self.e_tag = e_tag
        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if x_obs_server_side_encryption is not None:
            self.x_obs_server_side_encryption = x_obs_server_side_encryption
        if connection is not None:
            self.connection = connection
        if x_obs_server_side_encryption_customer_key_md5 is not None:
            self.x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5
        if date is not None:
            self.date = date
        if x_obs_server_side_encryption_customer_algorithm is not None:
            self.x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm
        if x_obs_copy_source_version_id is not None:
            self.x_obs_copy_source_version_id = x_obs_copy_source_version_id
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
        if x_obs_server_side_encryption_kms_key_id is not None:
            self.x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id
        if content_length is not None:
            self.content_length = content_length
        if x_obs_version_id is not None:
            self.x_obs_version_id = x_obs_version_id

    @property
    def last_modified(self):
        r"""Gets the last_modified of this CopyObjectResponse.

        Time when the object was last modified

        :return: The last_modified of this CopyObjectResponse.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this CopyObjectResponse.

        Time when the object was last modified

        :param last_modified: The last_modified of this CopyObjectResponse.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def e_tag(self):
        r"""Gets the e_tag of this CopyObjectResponse.

        :return: The e_tag of this CopyObjectResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this CopyObjectResponse.

        :param e_tag: The e_tag of this CopyObjectResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this CopyObjectResponse.

        :return: The x_obs_id_2 of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this CopyObjectResponse.

        :param x_obs_id_2: The x_obs_id_2 of this CopyObjectResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this CopyObjectResponse.

        :return: The x_obs_request_id of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this CopyObjectResponse.

        :param x_obs_request_id: The x_obs_request_id of this CopyObjectResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def x_obs_server_side_encryption(self):
        r"""Gets the x_obs_server_side_encryption of this CopyObjectResponse.

        :return: The x_obs_server_side_encryption of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        r"""Sets the x_obs_server_side_encryption of this CopyObjectResponse.

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this CopyObjectResponse.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def connection(self):
        r"""Gets the connection of this CopyObjectResponse.

        :return: The connection of this CopyObjectResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this CopyObjectResponse.

        :param connection: The connection of this CopyObjectResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this CopyObjectResponse.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this CopyObjectResponse.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this CopyObjectResponse.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def date(self):
        r"""Gets the date of this CopyObjectResponse.

        :return: The date of this CopyObjectResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this CopyObjectResponse.

        :param date: The date of this CopyObjectResponse.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this CopyObjectResponse.

        :return: The x_obs_server_side_encryption_customer_algorithm of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this CopyObjectResponse.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this CopyObjectResponse.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_copy_source_version_id(self):
        r"""Gets the x_obs_copy_source_version_id of this CopyObjectResponse.

        :return: The x_obs_copy_source_version_id of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_copy_source_version_id

    @x_obs_copy_source_version_id.setter
    def x_obs_copy_source_version_id(self, x_obs_copy_source_version_id):
        r"""Sets the x_obs_copy_source_version_id of this CopyObjectResponse.

        :param x_obs_copy_source_version_id: The x_obs_copy_source_version_id of this CopyObjectResponse.
        :type x_obs_copy_source_version_id: str
        """
        self._x_obs_copy_source_version_id = x_obs_copy_source_version_id

    @property
    def x_obs_storage_class(self):
        r"""Gets the x_obs_storage_class of this CopyObjectResponse.

        :return: The x_obs_storage_class of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        r"""Sets the x_obs_storage_class of this CopyObjectResponse.

        :param x_obs_storage_class: The x_obs_storage_class of this CopyObjectResponse.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        r"""Gets the x_obs_server_side_encryption_kms_key_id of this CopyObjectResponse.

        :return: The x_obs_server_side_encryption_kms_key_id of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        r"""Sets the x_obs_server_side_encryption_kms_key_id of this CopyObjectResponse.

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this CopyObjectResponse.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def content_length(self):
        r"""Gets the content_length of this CopyObjectResponse.

        :return: The content_length of this CopyObjectResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this CopyObjectResponse.

        :param content_length: The content_length of this CopyObjectResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def x_obs_version_id(self):
        r"""Gets the x_obs_version_id of this CopyObjectResponse.

        :return: The x_obs_version_id of this CopyObjectResponse.
        :rtype: str
        """
        return self._x_obs_version_id

    @x_obs_version_id.setter
    def x_obs_version_id(self, x_obs_version_id):
        r"""Sets the x_obs_version_id of this CopyObjectResponse.

        :param x_obs_version_id: The x_obs_version_id of this CopyObjectResponse.
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
        if not isinstance(other, CopyObjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
