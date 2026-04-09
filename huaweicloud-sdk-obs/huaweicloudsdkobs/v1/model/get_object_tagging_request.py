# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetObjectTaggingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetObjectTaggingRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'object_key': 'str',
        'tagging': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'object_key': 'object_key',
        'tagging': 'tagging',
        'version_id': 'versionId'
    }

    def __init__(self, date=None, bucket_name=None, object_key=None, tagging=None, version_id=None):
        r"""GetObjectTaggingRequest

        The model defined in huaweicloud sdk

        :param date: The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.
        :type date: str
        :param bucket_name: The name of the requested bucket.
        :type bucket_name: str
        :param object_key: Add tags object name.
        :type object_key: str
        :param tagging: Tagging indicates a request to add object tags API.
        :type tagging: str
        :param version_id: ID of the object version that the tag will be added to. Its response header is x-obs-version-id.
        :type version_id: str
        """
        
        

        self._date = None
        self._bucket_name = None
        self._object_key = None
        self._tagging = None
        self._version_id = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.object_key = object_key
        self.tagging = tagging
        if version_id is not None:
            self.version_id = version_id

    @property
    def date(self):
        r"""Gets the date of this GetObjectTaggingRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.

        :return: The date of this GetObjectTaggingRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetObjectTaggingRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.

        :param date: The date of this GetObjectTaggingRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this GetObjectTaggingRequest.

        The name of the requested bucket.

        :return: The bucket_name of this GetObjectTaggingRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this GetObjectTaggingRequest.

        The name of the requested bucket.

        :param bucket_name: The bucket_name of this GetObjectTaggingRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this GetObjectTaggingRequest.

        Add tags object name.

        :return: The object_key of this GetObjectTaggingRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this GetObjectTaggingRequest.

        Add tags object name.

        :param object_key: The object_key of this GetObjectTaggingRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def tagging(self):
        r"""Gets the tagging of this GetObjectTaggingRequest.

        Tagging indicates a request to add object tags API.

        :return: The tagging of this GetObjectTaggingRequest.
        :rtype: str
        """
        return self._tagging

    @tagging.setter
    def tagging(self, tagging):
        r"""Sets the tagging of this GetObjectTaggingRequest.

        Tagging indicates a request to add object tags API.

        :param tagging: The tagging of this GetObjectTaggingRequest.
        :type tagging: str
        """
        self._tagging = tagging

    @property
    def version_id(self):
        r"""Gets the version_id of this GetObjectTaggingRequest.

        ID of the object version that the tag will be added to. Its response header is x-obs-version-id.

        :return: The version_id of this GetObjectTaggingRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this GetObjectTaggingRequest.

        ID of the object version that the tag will be added to. Its response header is x-obs-version-id.

        :param version_id: The version_id of this GetObjectTaggingRequest.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, GetObjectTaggingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
