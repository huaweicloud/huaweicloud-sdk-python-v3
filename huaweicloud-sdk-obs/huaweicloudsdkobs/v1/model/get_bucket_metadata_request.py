# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketMetadataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketMetadataRequest"

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'date': 'str',
        'origin': 'str',
        'access_control_request_headers': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'date': 'Date',
        'origin': 'Origin',
        'access_control_request_headers': 'Access-Control-Request-Headers'
    }

    def __init__(self, bucket_name=None, date=None, origin=None, access_control_request_headers=None):
        r"""GetBucketMetadataRequest

        The model defined in huaweicloud sdk

        :param bucket_name: Name of the bucket.
        :type bucket_name: str
        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param origin: Origin (usually a domain name) specified by the pre-request (a cross-origin request). To obtain the CORS configuration information, you must add this header.
        :type origin: str
        :param access_control_request_headers: HTTP headers that can be contained in a request. To obtain the CORS configuration information, you can add this header.
        :type access_control_request_headers: str
        """
        
        

        self._bucket_name = None
        self._date = None
        self._origin = None
        self._access_control_request_headers = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if date is not None:
            self.date = date
        if origin is not None:
            self.origin = origin
        if access_control_request_headers is not None:
            self.access_control_request_headers = access_control_request_headers

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this GetBucketMetadataRequest.

        Name of the bucket.

        :return: The bucket_name of this GetBucketMetadataRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this GetBucketMetadataRequest.

        Name of the bucket.

        :param bucket_name: The bucket_name of this GetBucketMetadataRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def date(self):
        r"""Gets the date of this GetBucketMetadataRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this GetBucketMetadataRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketMetadataRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this GetBucketMetadataRequest.
        :type date: str
        """
        self._date = date

    @property
    def origin(self):
        r"""Gets the origin of this GetBucketMetadataRequest.

        Origin (usually a domain name) specified by the pre-request (a cross-origin request). To obtain the CORS configuration information, you must add this header.

        :return: The origin of this GetBucketMetadataRequest.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this GetBucketMetadataRequest.

        Origin (usually a domain name) specified by the pre-request (a cross-origin request). To obtain the CORS configuration information, you must add this header.

        :param origin: The origin of this GetBucketMetadataRequest.
        :type origin: str
        """
        self._origin = origin

    @property
    def access_control_request_headers(self):
        r"""Gets the access_control_request_headers of this GetBucketMetadataRequest.

        HTTP headers that can be contained in a request. To obtain the CORS configuration information, you can add this header.

        :return: The access_control_request_headers of this GetBucketMetadataRequest.
        :rtype: str
        """
        return self._access_control_request_headers

    @access_control_request_headers.setter
    def access_control_request_headers(self, access_control_request_headers):
        r"""Sets the access_control_request_headers of this GetBucketMetadataRequest.

        HTTP headers that can be contained in a request. To obtain the CORS configuration information, you can add this header.

        :param access_control_request_headers: The access_control_request_headers of this GetBucketMetadataRequest.
        :type access_control_request_headers: str
        """
        self._access_control_request_headers = access_control_request_headers

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
        if not isinstance(other, GetBucketMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
