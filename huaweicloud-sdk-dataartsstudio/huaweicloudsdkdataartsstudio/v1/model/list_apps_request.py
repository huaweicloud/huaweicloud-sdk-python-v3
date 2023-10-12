# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'app_type': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'app_type': 'app_type'
    }

    def __init__(self, workspace=None, dlm_type=None, limit=None, offset=None, name=None, app_type=None):
        """ListAppsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param name: 应用名称
        :type name: str
        :param app_type: 应用类型
        :type app_type: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._limit = None
        self._offset = None
        self._name = None
        self._app_type = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if app_type is not None:
            self.app_type = app_type

    @property
    def workspace(self):
        """Gets the workspace of this ListAppsRequest.

        工作空间id

        :return: The workspace of this ListAppsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListAppsRequest.

        工作空间id

        :param workspace: The workspace of this ListAppsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ListAppsRequest.

        dlm版本类型

        :return: The dlm_type of this ListAppsRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ListAppsRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this ListAppsRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def limit(self):
        """Gets the limit of this ListAppsRequest.

        limit

        :return: The limit of this ListAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppsRequest.

        limit

        :param limit: The limit of this ListAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppsRequest.

        offset

        :return: The offset of this ListAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppsRequest.

        offset

        :param offset: The offset of this ListAppsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        """Gets the name of this ListAppsRequest.

        应用名称

        :return: The name of this ListAppsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAppsRequest.

        应用名称

        :param name: The name of this ListAppsRequest.
        :type name: str
        """
        self._name = name

    @property
    def app_type(self):
        """Gets the app_type of this ListAppsRequest.

        应用类型

        :return: The app_type of this ListAppsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ListAppsRequest.

        应用类型

        :param app_type: The app_type of this ListAppsRequest.
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
        if not isinstance(other, ListAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
