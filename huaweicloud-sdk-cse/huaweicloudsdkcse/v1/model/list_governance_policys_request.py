# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGovernancePolicysRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'x_engine_id': 'str',
        'x_enterprise_project_id': 'str',
        'environment': 'str',
        'app': 'str'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'environment': 'environment',
        'app': 'app'
    }

    def __init__(self, content_type=None, x_engine_id=None, x_enterprise_project_id=None, environment=None, app=None):
        """ListGovernancePolicysRequest

        The model defined in huaweicloud sdk

        :param content_type: 该字段内容填为 \&quot;application/json;charset&#x3D;UTF-8\&quot;。
        :type content_type: str
        :param x_engine_id: 微服务引擎专享版的实例ID
        :type x_engine_id: str
        :param x_enterprise_project_id: 企业项目ID
        :type x_enterprise_project_id: str
        :param environment: 所属环境，填写all时表示查询所有环境。
        :type environment: str
        :param app: 所属应用
        :type app: str
        """
        
        

        self._content_type = None
        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._environment = None
        self._app = None
        self.discriminator = None

        self.content_type = content_type
        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        self.environment = environment
        if app is not None:
            self.app = app

    @property
    def content_type(self):
        """Gets the content_type of this ListGovernancePolicysRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :return: The content_type of this ListGovernancePolicysRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListGovernancePolicysRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"。

        :param content_type: The content_type of this ListGovernancePolicysRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def x_engine_id(self):
        """Gets the x_engine_id of this ListGovernancePolicysRequest.

        微服务引擎专享版的实例ID

        :return: The x_engine_id of this ListGovernancePolicysRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        """Sets the x_engine_id of this ListGovernancePolicysRequest.

        微服务引擎专享版的实例ID

        :param x_engine_id: The x_engine_id of this ListGovernancePolicysRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this ListGovernancePolicysRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this ListGovernancePolicysRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this ListGovernancePolicysRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this ListGovernancePolicysRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def environment(self):
        """Gets the environment of this ListGovernancePolicysRequest.

        所属环境，填写all时表示查询所有环境。

        :return: The environment of this ListGovernancePolicysRequest.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this ListGovernancePolicysRequest.

        所属环境，填写all时表示查询所有环境。

        :param environment: The environment of this ListGovernancePolicysRequest.
        :type environment: str
        """
        self._environment = environment

    @property
    def app(self):
        """Gets the app of this ListGovernancePolicysRequest.

        所属应用

        :return: The app of this ListGovernancePolicysRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListGovernancePolicysRequest.

        所属应用

        :param app: The app of this ListGovernancePolicysRequest.
        :type app: str
        """
        self._app = app

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
        if not isinstance(other, ListGovernancePolicysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
