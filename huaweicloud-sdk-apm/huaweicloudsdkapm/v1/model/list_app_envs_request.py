# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppEnvsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'int',
        'x_business_id': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'x_business_id': 'x-business-id'
    }

    def __init__(self, app_id=None, x_business_id=None):
        """ListAppEnvsRequest

        The model defined in huaweicloud sdk

        :param app_id: 组件id。
        :type app_id: int
        :param x_business_id: 应用id。
        :type x_business_id: int
        """
        
        

        self._app_id = None
        self._x_business_id = None
        self.discriminator = None

        self.app_id = app_id
        self.x_business_id = x_business_id

    @property
    def app_id(self):
        """Gets the app_id of this ListAppEnvsRequest.

        组件id。

        :return: The app_id of this ListAppEnvsRequest.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListAppEnvsRequest.

        组件id。

        :param app_id: The app_id of this ListAppEnvsRequest.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def x_business_id(self):
        """Gets the x_business_id of this ListAppEnvsRequest.

        应用id。

        :return: The x_business_id of this ListAppEnvsRequest.
        :rtype: int
        """
        return self._x_business_id

    @x_business_id.setter
    def x_business_id(self, x_business_id):
        """Sets the x_business_id of this ListAppEnvsRequest.

        应用id。

        :param x_business_id: The x_business_id of this ListAppEnvsRequest.
        :type x_business_id: int
        """
        self._x_business_id = x_business_id

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
        if not isinstance(other, ListAppEnvsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
