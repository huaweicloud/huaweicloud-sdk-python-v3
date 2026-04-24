# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetObjectLockRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SetObjectLockRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'object_key': 'str',
        'retention': 'str',
        'version_id': 'str',
        'body': 'SetObjectLockRequestBody'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'object_key': 'object_key',
        'retention': 'retention',
        'version_id': 'versionId',
        'body': 'body'
    }

    def __init__(self, date=None, bucket_name=None, object_key=None, retention=None, version_id=None, body=None):
        r"""SetObjectLockRequest

        The model defined in huaweicloud sdk

        :param date: The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.
        :type date: str
        :param bucket_name: The name of the requested bucket.
        :type bucket_name: str
        :param object_key: Object name configured for worm retention.
        :type object_key: str
        :param retention: Definition: Indicates that the operation is to configure or modify the retention period of an object. Constraints: None Range: None Default value: None 
        :type retention: str
        :param version_id: Definition: Object version ID The WORM policy of the specified object version is to be changed. If this parameter is not carried, the operation applies to the current object version. Constraints: None Range: The value must contain 32 characters. Default value: None. If this parameter is not configured, the latest version of the object is specified. 
        :type version_id: str
        :param body: Body of the SetObjectLockRequest
        :type body: :class:`huaweicloudsdkobs.v1.SetObjectLockRequestBody`
        """
        
        

        self._date = None
        self._bucket_name = None
        self._object_key = None
        self._retention = None
        self._version_id = None
        self._body = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.object_key = object_key
        self.retention = retention
        if version_id is not None:
            self.version_id = version_id
        if body is not None:
            self.body = body

    @property
    def date(self):
        r"""Gets the date of this SetObjectLockRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.

        :return: The date of this SetObjectLockRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SetObjectLockRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.

        :param date: The date of this SetObjectLockRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SetObjectLockRequest.

        The name of the requested bucket.

        :return: The bucket_name of this SetObjectLockRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SetObjectLockRequest.

        The name of the requested bucket.

        :param bucket_name: The bucket_name of this SetObjectLockRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this SetObjectLockRequest.

        Object name configured for worm retention.

        :return: The object_key of this SetObjectLockRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this SetObjectLockRequest.

        Object name configured for worm retention.

        :param object_key: The object_key of this SetObjectLockRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def retention(self):
        r"""Gets the retention of this SetObjectLockRequest.

        Definition: Indicates that the operation is to configure or modify the retention period of an object. Constraints: None Range: None Default value: None 

        :return: The retention of this SetObjectLockRequest.
        :rtype: str
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        r"""Sets the retention of this SetObjectLockRequest.

        Definition: Indicates that the operation is to configure or modify the retention period of an object. Constraints: None Range: None Default value: None 

        :param retention: The retention of this SetObjectLockRequest.
        :type retention: str
        """
        self._retention = retention

    @property
    def version_id(self):
        r"""Gets the version_id of this SetObjectLockRequest.

        Definition: Object version ID The WORM policy of the specified object version is to be changed. If this parameter is not carried, the operation applies to the current object version. Constraints: None Range: The value must contain 32 characters. Default value: None. If this parameter is not configured, the latest version of the object is specified. 

        :return: The version_id of this SetObjectLockRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this SetObjectLockRequest.

        Definition: Object version ID The WORM policy of the specified object version is to be changed. If this parameter is not carried, the operation applies to the current object version. Constraints: None Range: The value must contain 32 characters. Default value: None. If this parameter is not configured, the latest version of the object is specified. 

        :param version_id: The version_id of this SetObjectLockRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def body(self):
        r"""Gets the body of this SetObjectLockRequest.

        :return: The body of this SetObjectLockRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.SetObjectLockRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SetObjectLockRequest.

        :param body: The body of this SetObjectLockRequest.
        :type body: :class:`huaweicloudsdkobs.v1.SetObjectLockRequestBody`
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
        if not isinstance(other, SetObjectLockRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
