# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAddressSetInfoUsingPutRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'body': 'UpdateAddressSetDto'
    }

    attribute_map = {
        'set_id': 'set_id',
        'body': 'body'
    }

    def __init__(self, set_id=None, body=None):
        """UpdateAddressSetInfoUsingPutRequest

        The model defined in huaweicloud sdk

        :param set_id: 地址组id
        :type set_id: str
        :param body: Body of the UpdateAddressSetInfoUsingPutRequest
        :type body: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetDto`
        """
        
        

        self._set_id = None
        self._body = None
        self.discriminator = None

        self.set_id = set_id
        if body is not None:
            self.body = body

    @property
    def set_id(self):
        """Gets the set_id of this UpdateAddressSetInfoUsingPutRequest.

        地址组id

        :return: The set_id of this UpdateAddressSetInfoUsingPutRequest.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this UpdateAddressSetInfoUsingPutRequest.

        地址组id

        :param set_id: The set_id of this UpdateAddressSetInfoUsingPutRequest.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def body(self):
        """Gets the body of this UpdateAddressSetInfoUsingPutRequest.

        :return: The body of this UpdateAddressSetInfoUsingPutRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAddressSetInfoUsingPutRequest.

        :param body: The body of this UpdateAddressSetInfoUsingPutRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetDto`
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
        if not isinstance(other, UpdateAddressSetInfoUsingPutRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
