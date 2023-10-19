# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_app_id': 'str',
        'body': 'SubAppUpdateParam'
    }

    attribute_map = {
        'sub_app_id': 'sub_app_id',
        'body': 'body'
    }

    def __init__(self, sub_app_id=None, body=None):
        """UpdateSubAppRequest

        The model defined in huaweicloud sdk

        :param sub_app_id: 子应用id
        :type sub_app_id: str
        :param body: Body of the UpdateSubAppRequest
        :type body: :class:`huaweicloudsdkaom.v3.SubAppUpdateParam`
        """
        
        

        self._sub_app_id = None
        self._body = None
        self.discriminator = None

        self.sub_app_id = sub_app_id
        if body is not None:
            self.body = body

    @property
    def sub_app_id(self):
        """Gets the sub_app_id of this UpdateSubAppRequest.

        子应用id

        :return: The sub_app_id of this UpdateSubAppRequest.
        :rtype: str
        """
        return self._sub_app_id

    @sub_app_id.setter
    def sub_app_id(self, sub_app_id):
        """Sets the sub_app_id of this UpdateSubAppRequest.

        子应用id

        :param sub_app_id: The sub_app_id of this UpdateSubAppRequest.
        :type sub_app_id: str
        """
        self._sub_app_id = sub_app_id

    @property
    def body(self):
        """Gets the body of this UpdateSubAppRequest.

        :return: The body of this UpdateSubAppRequest.
        :rtype: :class:`huaweicloudsdkaom.v3.SubAppUpdateParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSubAppRequest.

        :param body: The body of this UpdateSubAppRequest.
        :type body: :class:`huaweicloudsdkaom.v3.SubAppUpdateParam`
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
        if not isinstance(other, UpdateSubAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
