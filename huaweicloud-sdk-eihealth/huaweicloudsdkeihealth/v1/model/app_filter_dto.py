# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppFilterDto:

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
        'app_version': 'str',
        'app_node_labels': 'list[str]'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'app_version': 'app_version',
        'app_node_labels': 'app_node_labels'
    }

    def __init__(self, app_id=None, app_name=None, app_version=None, app_node_labels=None):
        """AppFilterDto

        The model defined in huaweicloud sdk

        :param app_id: 应用id
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param app_version: 应用版本
        :type app_version: str
        :param app_node_labels: 计算节点标签
        :type app_node_labels: list[str]
        """
        
        

        self._app_id = None
        self._app_name = None
        self._app_version = None
        self._app_node_labels = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if app_node_labels is not None:
            self.app_node_labels = app_node_labels

    @property
    def app_id(self):
        """Gets the app_id of this AppFilterDto.

        应用id

        :return: The app_id of this AppFilterDto.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppFilterDto.

        应用id

        :param app_id: The app_id of this AppFilterDto.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this AppFilterDto.

        应用名称

        :return: The app_name of this AppFilterDto.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppFilterDto.

        应用名称

        :param app_name: The app_name of this AppFilterDto.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        """Gets the app_version of this AppFilterDto.

        应用版本

        :return: The app_version of this AppFilterDto.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this AppFilterDto.

        应用版本

        :param app_version: The app_version of this AppFilterDto.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def app_node_labels(self):
        """Gets the app_node_labels of this AppFilterDto.

        计算节点标签

        :return: The app_node_labels of this AppFilterDto.
        :rtype: list[str]
        """
        return self._app_node_labels

    @app_node_labels.setter
    def app_node_labels(self, app_node_labels):
        """Sets the app_node_labels of this AppFilterDto.

        计算节点标签

        :param app_node_labels: The app_node_labels of this AppFilterDto.
        :type app_node_labels: list[str]
        """
        self._app_node_labels = app_node_labels

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
        if not isinstance(other, AppFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
