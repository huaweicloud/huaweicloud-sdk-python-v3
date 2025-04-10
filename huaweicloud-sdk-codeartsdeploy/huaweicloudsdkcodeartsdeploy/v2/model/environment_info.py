# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, name=None, app_id=None, app_name=None, project_id=None):
        r"""EnvironmentInfo

        The model defined in huaweicloud sdk

        :param id: 环境id
        :type id: str
        :param name: 环境名称
        :type name: str
        :param app_id: 应用id
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._app_id = None
        self._app_name = None
        self._project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if project_id is not None:
            self.project_id = project_id

    @property
    def id(self):
        r"""Gets the id of this EnvironmentInfo.

        环境id

        :return: The id of this EnvironmentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EnvironmentInfo.

        环境id

        :param id: The id of this EnvironmentInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EnvironmentInfo.

        环境名称

        :return: The name of this EnvironmentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnvironmentInfo.

        环境名称

        :param name: The name of this EnvironmentInfo.
        :type name: str
        """
        self._name = name

    @property
    def app_id(self):
        r"""Gets the app_id of this EnvironmentInfo.

        应用id

        :return: The app_id of this EnvironmentInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this EnvironmentInfo.

        应用id

        :param app_id: The app_id of this EnvironmentInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this EnvironmentInfo.

        应用名称

        :return: The app_name of this EnvironmentInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this EnvironmentInfo.

        应用名称

        :param app_name: The app_name of this EnvironmentInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def project_id(self):
        r"""Gets the project_id of this EnvironmentInfo.

        项目id

        :return: The project_id of this EnvironmentInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this EnvironmentInfo.

        项目id

        :param project_id: The project_id of this EnvironmentInfo.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, EnvironmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
