# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProgressRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'operation_uri': 'str'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'operation_uri': 'operation_uri'
    }

    def __init__(self, project_uuid=None, operation_uri=None):
        r"""ShowProgressRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目ID
        :type project_uuid: str
        :param operation_uri: 异步操作uri
        :type operation_uri: str
        """
        
        

        self._project_uuid = None
        self._operation_uri = None
        self.discriminator = None

        if project_uuid is not None:
            self.project_uuid = project_uuid
        self.operation_uri = operation_uri

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ShowProgressRequest.

        项目ID

        :return: The project_uuid of this ShowProgressRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ShowProgressRequest.

        项目ID

        :param project_uuid: The project_uuid of this ShowProgressRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def operation_uri(self):
        r"""Gets the operation_uri of this ShowProgressRequest.

        异步操作uri

        :return: The operation_uri of this ShowProgressRequest.
        :rtype: str
        """
        return self._operation_uri

    @operation_uri.setter
    def operation_uri(self, operation_uri):
        r"""Sets the operation_uri of this ShowProgressRequest.

        异步操作uri

        :param operation_uri: The operation_uri of this ShowProgressRequest.
        :type operation_uri: str
        """
        self._operation_uri = operation_uri

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
        if not isinstance(other, ShowProgressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
