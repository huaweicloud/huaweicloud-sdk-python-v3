# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateValueListRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'valuelistid': 'str',
        'body': 'UpdateValueListRequestBody'
    }

    attribute_map = {
        'valuelistid': 'valuelistid',
        'body': 'body'
    }

    def __init__(self, valuelistid=None, body=None):
        """UpdateValueListRequest - a model defined in huaweicloud sdk"""
        
        

        self._valuelistid = None
        self._body = None
        self.discriminator = None

        self.valuelistid = valuelistid
        if body is not None:
            self.body = body

    @property
    def valuelistid(self):
        """Gets the valuelistid of this UpdateValueListRequest.

        引用表id

        :return: The valuelistid of this UpdateValueListRequest.
        :rtype: str
        """
        return self._valuelistid

    @valuelistid.setter
    def valuelistid(self, valuelistid):
        """Sets the valuelistid of this UpdateValueListRequest.

        引用表id

        :param valuelistid: The valuelistid of this UpdateValueListRequest.
        :type: str
        """
        self._valuelistid = valuelistid

    @property
    def body(self):
        """Gets the body of this UpdateValueListRequest.


        :return: The body of this UpdateValueListRequest.
        :rtype: UpdateValueListRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateValueListRequest.


        :param body: The body of this UpdateValueListRequest.
        :type: UpdateValueListRequestBody
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateValueListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other