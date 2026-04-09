# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketPublicAccessBlockRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SetBucketPublicAccessBlockRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'public_access_block': 'str',
        'body': 'SetBpaRequestBody'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'public_access_block': 'publicAccessBlock',
        'body': 'body'
    }

    def __init__(self, date=None, bucket_name=None, public_access_block=None, body=None):
        r"""SetBucketPublicAccessBlockRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param public_access_block: Indicates the Public Access API of the bucket.
        :type public_access_block: str
        :param body: Body of the SetBucketPublicAccessBlockRequest
        :type body: :class:`huaweicloudsdkobs.v1.SetBpaRequestBody`
        """
        
        

        self._date = None
        self._bucket_name = None
        self._public_access_block = None
        self._body = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.public_access_block = public_access_block
        if body is not None:
            self.body = body

    @property
    def date(self):
        r"""Gets the date of this SetBucketPublicAccessBlockRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this SetBucketPublicAccessBlockRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SetBucketPublicAccessBlockRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this SetBucketPublicAccessBlockRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SetBucketPublicAccessBlockRequest.

        Name of the requested bucket

        :return: The bucket_name of this SetBucketPublicAccessBlockRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SetBucketPublicAccessBlockRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this SetBucketPublicAccessBlockRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def public_access_block(self):
        r"""Gets the public_access_block of this SetBucketPublicAccessBlockRequest.

        Indicates the Public Access API of the bucket.

        :return: The public_access_block of this SetBucketPublicAccessBlockRequest.
        :rtype: str
        """
        return self._public_access_block

    @public_access_block.setter
    def public_access_block(self, public_access_block):
        r"""Sets the public_access_block of this SetBucketPublicAccessBlockRequest.

        Indicates the Public Access API of the bucket.

        :param public_access_block: The public_access_block of this SetBucketPublicAccessBlockRequest.
        :type public_access_block: str
        """
        self._public_access_block = public_access_block

    @property
    def body(self):
        r"""Gets the body of this SetBucketPublicAccessBlockRequest.

        :return: The body of this SetBucketPublicAccessBlockRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBpaRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SetBucketPublicAccessBlockRequest.

        :param body: The body of this SetBucketPublicAccessBlockRequest.
        :type body: :class:`huaweicloudsdkobs.v1.SetBpaRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SetBucketPublicAccessBlockRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
