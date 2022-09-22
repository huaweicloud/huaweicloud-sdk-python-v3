# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDiskInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'source_id': 'str',
        'body': 'PutDiskInfoReq'
    }

    attribute_map = {
        'source_id': 'source_id',
        'body': 'body'
    }

    def __init__(self, source_id=None, body=None):
        """UpdateDiskInfoRequest

        The model defined in huaweicloud sdk

        :param source_id: 源端服务器ID
        :type source_id: str
        :param body: Body of the UpdateDiskInfoRequest
        :type body: :class:`huaweicloudsdksms.v3.PutDiskInfoReq`
        """
        
        

        self._source_id = None
        self._body = None
        self.discriminator = None

        self.source_id = source_id
        if body is not None:
            self.body = body

    @property
    def source_id(self):
        """Gets the source_id of this UpdateDiskInfoRequest.

        源端服务器ID

        :return: The source_id of this UpdateDiskInfoRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this UpdateDiskInfoRequest.

        源端服务器ID

        :param source_id: The source_id of this UpdateDiskInfoRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def body(self):
        """Gets the body of this UpdateDiskInfoRequest.


        :return: The body of this UpdateDiskInfoRequest.
        :rtype: :class:`huaweicloudsdksms.v3.PutDiskInfoReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDiskInfoRequest.


        :param body: The body of this UpdateDiskInfoRequest.
        :type body: :class:`huaweicloudsdksms.v3.PutDiskInfoReq`
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
        if not isinstance(other, UpdateDiskInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
