# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBlackWhiteListUsingPutRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list_id': 'str',
        'body': 'UpdateBlackWhiteListDto'
    }

    attribute_map = {
        'list_id': 'list_id',
        'body': 'body'
    }

    def __init__(self, list_id=None, body=None):
        """UpdateBlackWhiteListUsingPutRequest

        The model defined in huaweicloud sdk

        :param list_id: 黑白名单列表id
        :type list_id: str
        :param body: Body of the UpdateBlackWhiteListUsingPutRequest
        :type body: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListDto`
        """
        
        

        self._list_id = None
        self._body = None
        self.discriminator = None

        self.list_id = list_id
        if body is not None:
            self.body = body

    @property
    def list_id(self):
        """Gets the list_id of this UpdateBlackWhiteListUsingPutRequest.

        黑白名单列表id

        :return: The list_id of this UpdateBlackWhiteListUsingPutRequest.
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this UpdateBlackWhiteListUsingPutRequest.

        黑白名单列表id

        :param list_id: The list_id of this UpdateBlackWhiteListUsingPutRequest.
        :type list_id: str
        """
        self._list_id = list_id

    @property
    def body(self):
        """Gets the body of this UpdateBlackWhiteListUsingPutRequest.

        :return: The body of this UpdateBlackWhiteListUsingPutRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateBlackWhiteListUsingPutRequest.

        :param body: The body of this UpdateBlackWhiteListUsingPutRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListDto`
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
        if not isinstance(other, UpdateBlackWhiteListUsingPutRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
