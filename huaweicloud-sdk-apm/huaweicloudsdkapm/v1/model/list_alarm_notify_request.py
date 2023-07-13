# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmNotifyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_business_id': 'int',
        'body': 'AlarmNotifyListRequest'
    }

    attribute_map = {
        'x_business_id': 'x-business-id',
        'body': 'body'
    }

    def __init__(self, x_business_id=None, body=None):
        """ListAlarmNotifyRequest

        The model defined in huaweicloud sdk

        :param x_business_id: 应用id，用于鉴权。
        :type x_business_id: int
        :param body: Body of the ListAlarmNotifyRequest
        :type body: :class:`huaweicloudsdkapm.v1.AlarmNotifyListRequest`
        """
        
        

        self._x_business_id = None
        self._body = None
        self.discriminator = None

        self.x_business_id = x_business_id
        if body is not None:
            self.body = body

    @property
    def x_business_id(self):
        """Gets the x_business_id of this ListAlarmNotifyRequest.

        应用id，用于鉴权。

        :return: The x_business_id of this ListAlarmNotifyRequest.
        :rtype: int
        """
        return self._x_business_id

    @x_business_id.setter
    def x_business_id(self, x_business_id):
        """Sets the x_business_id of this ListAlarmNotifyRequest.

        应用id，用于鉴权。

        :param x_business_id: The x_business_id of this ListAlarmNotifyRequest.
        :type x_business_id: int
        """
        self._x_business_id = x_business_id

    @property
    def body(self):
        """Gets the body of this ListAlarmNotifyRequest.

        :return: The body of this ListAlarmNotifyRequest.
        :rtype: :class:`huaweicloudsdkapm.v1.AlarmNotifyListRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListAlarmNotifyRequest.

        :param body: The body of this ListAlarmNotifyRequest.
        :type body: :class:`huaweicloudsdkapm.v1.AlarmNotifyListRequest`
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
        if not isinstance(other, ListAlarmNotifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
