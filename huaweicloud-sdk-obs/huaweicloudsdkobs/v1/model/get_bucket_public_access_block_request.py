# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketPublicAccessBlockRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketPublicAccessBlockRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'public_access_block_': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'public_access_block_': 'publicAccessBlock '
    }

    def __init__(self, date=None, bucket_name=None, public_access_block_=None):
        r"""GetBucketPublicAccessBlockRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param public_access_block_: Indicates the API for Obtaining the Public Access Block Configuration of a Bucket.
        :type public_access_block_: str
        """
        
        

        self._date = None
        self._bucket_name = None
        self._public_access_block_ = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        if public_access_block_ is not None:
            self.public_access_block_ = public_access_block_

    @property
    def date(self):
        r"""Gets the date of this GetBucketPublicAccessBlockRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this GetBucketPublicAccessBlockRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketPublicAccessBlockRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this GetBucketPublicAccessBlockRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this GetBucketPublicAccessBlockRequest.

        Name of the requested bucket

        :return: The bucket_name of this GetBucketPublicAccessBlockRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this GetBucketPublicAccessBlockRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this GetBucketPublicAccessBlockRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def public_access_block_(self):
        r"""Gets the public_access_block_ of this GetBucketPublicAccessBlockRequest.

        Indicates the API for Obtaining the Public Access Block Configuration of a Bucket.

        :return: The public_access_block_ of this GetBucketPublicAccessBlockRequest.
        :rtype: str
        """
        return self._public_access_block_

    @public_access_block_.setter
    def public_access_block_(self, public_access_block_):
        r"""Sets the public_access_block_ of this GetBucketPublicAccessBlockRequest.

        Indicates the API for Obtaining the Public Access Block Configuration of a Bucket.

        :param public_access_block_: The public_access_block_ of this GetBucketPublicAccessBlockRequest.
        :type public_access_block_: str
        """
        self._public_access_block_ = public_access_block_

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
        if not isinstance(other, GetBucketPublicAccessBlockRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
