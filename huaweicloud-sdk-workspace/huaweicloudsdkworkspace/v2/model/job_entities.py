# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'product_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'product_id': 'product_id',
        'user_name': 'user_name'
    }

    def __init__(self, desktop_id=None, product_id=None, user_name=None):
        """JobEntities

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param product_id: 套餐ID。
        :type product_id: str
        :param user_name: 用户名。
        :type user_name: str
        """
        
        

        self._desktop_id = None
        self._product_id = None
        self._user_name = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if product_id is not None:
            self.product_id = product_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def desktop_id(self):
        """Gets the desktop_id of this JobEntities.

        桌面ID。

        :return: The desktop_id of this JobEntities.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this JobEntities.

        桌面ID。

        :param desktop_id: The desktop_id of this JobEntities.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def product_id(self):
        """Gets the product_id of this JobEntities.

        套餐ID。

        :return: The product_id of this JobEntities.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this JobEntities.

        套餐ID。

        :param product_id: The product_id of this JobEntities.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def user_name(self):
        """Gets the user_name of this JobEntities.

        用户名。

        :return: The user_name of this JobEntities.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this JobEntities.

        用户名。

        :param user_name: The user_name of this JobEntities.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, JobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
