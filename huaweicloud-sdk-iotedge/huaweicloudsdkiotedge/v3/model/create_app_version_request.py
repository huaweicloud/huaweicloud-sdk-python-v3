# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppVersionRequest:

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
        'version': 'str',
        'body': 'CreateAppVersionRequestBody'
    }

    attribute_map = {
        'app_id': 'app_id',
        'version': 'version',
        'body': 'body'
    }

    def __init__(self, app_id=None, version=None, body=None):
        """CreateAppVersionRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param version: 应用版本
        :type version: str
        :param body: Body of the CreateAppVersionRequest
        :type body: :class:`huaweicloudsdkiotedge.v3.CreateAppVersionRequestBody`
        """
        
        

        self._app_id = None
        self._version = None
        self._body = None
        self.discriminator = None

        self.app_id = app_id
        self.version = version
        if body is not None:
            self.body = body

    @property
    def app_id(self):
        """Gets the app_id of this CreateAppVersionRequest.

        应用ID

        :return: The app_id of this CreateAppVersionRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateAppVersionRequest.

        应用ID

        :param app_id: The app_id of this CreateAppVersionRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def version(self):
        """Gets the version of this CreateAppVersionRequest.

        应用版本

        :return: The version of this CreateAppVersionRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateAppVersionRequest.

        应用版本

        :param version: The version of this CreateAppVersionRequest.
        :type version: str
        """
        self._version = version

    @property
    def body(self):
        """Gets the body of this CreateAppVersionRequest.

        :return: The body of this CreateAppVersionRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v3.CreateAppVersionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateAppVersionRequest.

        :param body: The body of this CreateAppVersionRequest.
        :type body: :class:`huaweicloudsdkiotedge.v3.CreateAppVersionRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateAppVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
