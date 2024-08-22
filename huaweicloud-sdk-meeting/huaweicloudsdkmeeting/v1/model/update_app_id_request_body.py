# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppIdRequestBody:

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
        'description': 'str',
        'status': 'int'
    }

    attribute_map = {
        'app_name': 'app_name',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, app_name=None, description=None, status=None):
        """UpdateAppIdRequestBody

        The model defined in huaweicloud sdk

        :param app_name: 企业应用名称
        :type app_name: str
        :param description: 企业应用描述
        :type description: str
        :param status: 企业应用状态  * 0：正常  * 1：停用 
        :type status: int
        """
        
        

        self._app_name = None
        self._description = None
        self._status = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def app_name(self):
        """Gets the app_name of this UpdateAppIdRequestBody.

        企业应用名称

        :return: The app_name of this UpdateAppIdRequestBody.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this UpdateAppIdRequestBody.

        企业应用名称

        :param app_name: The app_name of this UpdateAppIdRequestBody.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def description(self):
        """Gets the description of this UpdateAppIdRequestBody.

        企业应用描述

        :return: The description of this UpdateAppIdRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAppIdRequestBody.

        企业应用描述

        :param description: The description of this UpdateAppIdRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateAppIdRequestBody.

        企业应用状态  * 0：正常  * 1：停用 

        :return: The status of this UpdateAppIdRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateAppIdRequestBody.

        企业应用状态  * 0：正常  * 1：停用 

        :param status: The status of this UpdateAppIdRequestBody.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, UpdateAppIdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
