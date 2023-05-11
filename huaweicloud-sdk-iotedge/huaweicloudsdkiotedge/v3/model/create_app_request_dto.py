# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_name': 'str',
        'description': 'str',
        'app_type': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'description': 'description',
        'app_type': 'app_type'
    }

    def __init__(self, app_id=None, app_name=None, description=None, app_type=None):
        """CreateAppRequestDTO

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param description: 应用描述
        :type description: str
        :param app_type: 应用类型
        :type app_type: str
        """
        
        

        self._app_id = None
        self._app_name = None
        self._description = None
        self._app_type = None
        self.discriminator = None

        self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if description is not None:
            self.description = description
        self.app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this CreateAppRequestDTO.

        应用ID

        :return: The app_id of this CreateAppRequestDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateAppRequestDTO.

        应用ID

        :param app_id: The app_id of this CreateAppRequestDTO.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this CreateAppRequestDTO.

        应用名称

        :return: The app_name of this CreateAppRequestDTO.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this CreateAppRequestDTO.

        应用名称

        :param app_name: The app_name of this CreateAppRequestDTO.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def description(self):
        """Gets the description of this CreateAppRequestDTO.

        应用描述

        :return: The description of this CreateAppRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAppRequestDTO.

        应用描述

        :param description: The description of this CreateAppRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def app_type(self):
        """Gets the app_type of this CreateAppRequestDTO.

        应用类型

        :return: The app_type of this CreateAppRequestDTO.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this CreateAppRequestDTO.

        应用类型

        :param app_type: The app_type of this CreateAppRequestDTO.
        :type app_type: str
        """
        self._app_type = app_type

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
        if not isinstance(other, CreateAppRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
