# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEdgeApplicationVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'version': 'version'
    }

    def __init__(self, edge_app_id=None, version=None):
        r"""ShowEdgeApplicationVersionRequest

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID，应用唯一。
        :type edge_app_id: str
        :param version: 应用版本,应用内版本唯一。
        :type version: str
        """
        
        

        self._edge_app_id = None
        self._version = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        self.version = version

    @property
    def edge_app_id(self):
        r"""Gets the edge_app_id of this ShowEdgeApplicationVersionRequest.

        应用ID，应用唯一。

        :return: The edge_app_id of this ShowEdgeApplicationVersionRequest.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        r"""Sets the edge_app_id of this ShowEdgeApplicationVersionRequest.

        应用ID，应用唯一。

        :param edge_app_id: The edge_app_id of this ShowEdgeApplicationVersionRequest.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def version(self):
        r"""Gets the version of this ShowEdgeApplicationVersionRequest.

        应用版本,应用内版本唯一。

        :return: The version of this ShowEdgeApplicationVersionRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowEdgeApplicationVersionRequest.

        应用版本,应用内版本唯一。

        :param version: The version of this ShowEdgeApplicationVersionRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowEdgeApplicationVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
