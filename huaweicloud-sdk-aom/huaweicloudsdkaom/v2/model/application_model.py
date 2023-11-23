# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationModel:

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
        'app_type': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'app_type': 'app_type'
    }

    def __init__(self, app_id=None, app_name=None, app_type=None):
        """ApplicationModel

        The model defined in huaweicloud sdk

        :param app_id: 应用id
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param app_type: 应用来源
        :type app_type: str
        """
        
        

        self._app_id = None
        self._app_name = None
        self._app_type = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if app_type is not None:
            self.app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this ApplicationModel.

        应用id

        :return: The app_id of this ApplicationModel.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ApplicationModel.

        应用id

        :param app_id: The app_id of this ApplicationModel.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ApplicationModel.

        应用名称

        :return: The app_name of this ApplicationModel.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ApplicationModel.

        应用名称

        :param app_name: The app_name of this ApplicationModel.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_type(self):
        """Gets the app_type of this ApplicationModel.

        应用来源

        :return: The app_type of this ApplicationModel.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ApplicationModel.

        应用来源

        :param app_type: The app_type of this ApplicationModel.
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
        if not isinstance(other, ApplicationModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
