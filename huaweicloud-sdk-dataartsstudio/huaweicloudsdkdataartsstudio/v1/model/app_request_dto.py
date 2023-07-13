# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_type': 'str',
        'name': 'str',
        'description': 'str',
        'apig_type': 'str',
        'apig_instance_id': 'str'
    }

    attribute_map = {
        'app_type': 'app_type',
        'name': 'name',
        'description': 'description',
        'apig_type': 'apig_type',
        'apig_instance_id': 'apig_instance_id'
    }

    def __init__(self, app_type=None, name=None, description=None, apig_type=None, apig_instance_id=None):
        """AppRequestDTO

        The model defined in huaweicloud sdk

        :param app_type: 应用类型
        :type app_type: str
        :param name: 应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param apig_type: 网关类型
        :type apig_type: str
        :param apig_instance_id: 网关实例编号
        :type apig_instance_id: str
        """
        
        

        self._app_type = None
        self._name = None
        self._description = None
        self._apig_type = None
        self._apig_instance_id = None
        self.discriminator = None

        if app_type is not None:
            self.app_type = app_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if apig_type is not None:
            self.apig_type = apig_type
        if apig_instance_id is not None:
            self.apig_instance_id = apig_instance_id

    @property
    def app_type(self):
        """Gets the app_type of this AppRequestDTO.

        应用类型

        :return: The app_type of this AppRequestDTO.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AppRequestDTO.

        应用类型

        :param app_type: The app_type of this AppRequestDTO.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def name(self):
        """Gets the name of this AppRequestDTO.

        应用名称

        :return: The name of this AppRequestDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppRequestDTO.

        应用名称

        :param name: The name of this AppRequestDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AppRequestDTO.

        应用描述

        :return: The description of this AppRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppRequestDTO.

        应用描述

        :param description: The description of this AppRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def apig_type(self):
        """Gets the apig_type of this AppRequestDTO.

        网关类型

        :return: The apig_type of this AppRequestDTO.
        :rtype: str
        """
        return self._apig_type

    @apig_type.setter
    def apig_type(self, apig_type):
        """Sets the apig_type of this AppRequestDTO.

        网关类型

        :param apig_type: The apig_type of this AppRequestDTO.
        :type apig_type: str
        """
        self._apig_type = apig_type

    @property
    def apig_instance_id(self):
        """Gets the apig_instance_id of this AppRequestDTO.

        网关实例编号

        :return: The apig_instance_id of this AppRequestDTO.
        :rtype: str
        """
        return self._apig_instance_id

    @apig_instance_id.setter
    def apig_instance_id(self, apig_instance_id):
        """Sets the apig_instance_id of this AppRequestDTO.

        网关实例编号

        :param apig_instance_id: The apig_instance_id of this AppRequestDTO.
        :type apig_instance_id: str
        """
        self._apig_instance_id = apig_instance_id

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
        if not isinstance(other, AppRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
