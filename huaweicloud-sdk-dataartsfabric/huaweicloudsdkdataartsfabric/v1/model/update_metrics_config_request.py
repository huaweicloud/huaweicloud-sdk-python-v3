# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMetricsConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'body': 'UpdateMetricsConfigInput'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, body=None):
        r"""UpdateMetricsConfigRequest

        The model defined in huaweicloud sdk

        :param workspace_id: Workspace的ID
        :type workspace_id: str
        :param body: Body of the UpdateMetricsConfigRequest
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.UpdateMetricsConfigInput`
        """
        
        

        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateMetricsConfigRequest.

        Workspace的ID

        :return: The workspace_id of this UpdateMetricsConfigRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateMetricsConfigRequest.

        Workspace的ID

        :param workspace_id: The workspace_id of this UpdateMetricsConfigRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this UpdateMetricsConfigRequest.

        :return: The body of this UpdateMetricsConfigRequest.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.UpdateMetricsConfigInput`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateMetricsConfigRequest.

        :param body: The body of this UpdateMetricsConfigRequest.
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.UpdateMetricsConfigInput`
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
        if not isinstance(other, UpdateMetricsConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
