# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAppIdRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'description': 'description'
    }

    def __init__(self, app_name=None, description=None):
        r"""AddAppIdRequestBody

        The model defined in huaweicloud sdk

        :param app_name: 企业应用名称
        :type app_name: str
        :param description: 企业应用描述
        :type description: str
        """
        
        

        self._app_name = None
        self._description = None
        self.discriminator = None

        self.app_name = app_name
        if description is not None:
            self.description = description

    @property
    def app_name(self):
        r"""Gets the app_name of this AddAppIdRequestBody.

        企业应用名称

        :return: The app_name of this AddAppIdRequestBody.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AddAppIdRequestBody.

        企业应用名称

        :param app_name: The app_name of this AddAppIdRequestBody.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def description(self):
        r"""Gets the description of this AddAppIdRequestBody.

        企业应用描述

        :return: The description of this AddAppIdRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddAppIdRequestBody.

        企业应用描述

        :param description: The description of this AddAppIdRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AddAppIdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
