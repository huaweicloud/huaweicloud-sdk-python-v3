# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteObjectsRequest"

    sensitive_list = []

    openapi_types = {
        'content_md5': 'str',
        'date': 'str',
        'bucket_name': 'str',
        'delete': 'str',
        'body': 'DeleteObjectsRequestBody'
    }

    attribute_map = {
        'content_md5': 'Content-MD5',
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'delete': 'delete',
        'body': 'body'
    }

    def __init__(self, content_md5=None, date=None, bucket_name=None, delete=None, body=None):
        r"""DeleteObjectsRequest

        The model defined in huaweicloud sdk

        :param content_md5: Base64-encoded 128-bit MD5 digest of the message according to RFC 1864.
        :type content_md5: str
        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param delete: Indicates the batch deletion API.
        :type delete: str
        :param body: Body of the DeleteObjectsRequest
        :type body: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequestBody`
        """
        
        

        self._content_md5 = None
        self._date = None
        self._bucket_name = None
        self._delete = None
        self._body = None
        self.discriminator = None

        self.content_md5 = content_md5
        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.delete = delete
        if body is not None:
            self.body = body

    @property
    def content_md5(self):
        r"""Gets the content_md5 of this DeleteObjectsRequest.

        Base64-encoded 128-bit MD5 digest of the message according to RFC 1864.

        :return: The content_md5 of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._content_md5

    @content_md5.setter
    def content_md5(self, content_md5):
        r"""Sets the content_md5 of this DeleteObjectsRequest.

        Base64-encoded 128-bit MD5 digest of the message according to RFC 1864.

        :param content_md5: The content_md5 of this DeleteObjectsRequest.
        :type content_md5: str
        """
        self._content_md5 = content_md5

    @property
    def date(self):
        r"""Gets the date of this DeleteObjectsRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this DeleteObjectsRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this DeleteObjectsRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this DeleteObjectsRequest.

        Name of the requested bucket

        :return: The bucket_name of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this DeleteObjectsRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this DeleteObjectsRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def delete(self):
        r"""Gets the delete of this DeleteObjectsRequest.

        Indicates the batch deletion API.

        :return: The delete of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this DeleteObjectsRequest.

        Indicates the batch deletion API.

        :param delete: The delete of this DeleteObjectsRequest.
        :type delete: str
        """
        self._delete = delete

    @property
    def body(self):
        r"""Gets the body of this DeleteObjectsRequest.

        :return: The body of this DeleteObjectsRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeleteObjectsRequest.

        :param body: The body of this DeleteObjectsRequest.
        :type body: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequestBody`
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
        if not isinstance(other, DeleteObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
