# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'spec': 'MigrateNodesSpec',
        'status': 'TaskStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, spec=None, status=None):
        """MigrateNodeResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值“v3”。
        :type api_version: str
        :param kind: API类型，固定值“MigrateNodesTask”。
        :type kind: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.MigrateNodesSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.TaskStatus`
        """
        
        super(MigrateNodeResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        """Gets the api_version of this MigrateNodeResponse.

        API版本，固定值“v3”。

        :return: The api_version of this MigrateNodeResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this MigrateNodeResponse.

        API版本，固定值“v3”。

        :param api_version: The api_version of this MigrateNodeResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this MigrateNodeResponse.

        API类型，固定值“MigrateNodesTask”。

        :return: The kind of this MigrateNodeResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this MigrateNodeResponse.

        API类型，固定值“MigrateNodesTask”。

        :param kind: The kind of this MigrateNodeResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def spec(self):
        """Gets the spec of this MigrateNodeResponse.

        :return: The spec of this MigrateNodeResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.MigrateNodesSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this MigrateNodeResponse.

        :param spec: The spec of this MigrateNodeResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.MigrateNodesSpec`
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this MigrateNodeResponse.

        :return: The status of this MigrateNodeResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.TaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MigrateNodeResponse.

        :param status: The status of this MigrateNodeResponse.
        :type status: :class:`huaweicloudsdkcce.v3.TaskStatus`
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
        if not isinstance(other, MigrateNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
