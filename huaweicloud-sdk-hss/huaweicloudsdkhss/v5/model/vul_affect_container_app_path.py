# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulAffectContainerAppPath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'app_version': 'str',
        'app_path': 'str'
    }

    attribute_map = {
        'status': 'status',
        'app_version': 'app_version',
        'app_path': 'app_path'
    }

    def __init__(self, status=None, app_version=None, app_path=None):
        r"""VulAffectContainerAppPath

        The model defined in huaweicloud sdk

        :param status: 处理状态
        :type status: str
        :param app_version: 软件版本
        :type app_version: str
        :param app_path: 软件路径
        :type app_path: str
        """
        
        

        self._status = None
        self._app_version = None
        self._app_path = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if app_version is not None:
            self.app_version = app_version
        if app_path is not None:
            self.app_path = app_path

    @property
    def status(self):
        r"""Gets the status of this VulAffectContainerAppPath.

        处理状态

        :return: The status of this VulAffectContainerAppPath.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulAffectContainerAppPath.

        处理状态

        :param status: The status of this VulAffectContainerAppPath.
        :type status: str
        """
        self._status = status

    @property
    def app_version(self):
        r"""Gets the app_version of this VulAffectContainerAppPath.

        软件版本

        :return: The app_version of this VulAffectContainerAppPath.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this VulAffectContainerAppPath.

        软件版本

        :param app_version: The app_version of this VulAffectContainerAppPath.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def app_path(self):
        r"""Gets the app_path of this VulAffectContainerAppPath.

        软件路径

        :return: The app_path of this VulAffectContainerAppPath.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this VulAffectContainerAppPath.

        软件路径

        :param app_path: The app_path of this VulAffectContainerAppPath.
        :type app_path: str
        """
        self._app_path = app_path

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
        if not isinstance(other, VulAffectContainerAppPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
