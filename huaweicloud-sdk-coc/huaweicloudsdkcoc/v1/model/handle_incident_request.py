# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandleIncidentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'incident_id': 'str',
        'body': 'ExecuteActionParamsV2'
    }

    attribute_map = {
        'incident_id': 'incident_id',
        'body': 'body'
    }

    def __init__(self, incident_id=None, body=None):
        r"""HandleIncidentRequest

        The model defined in huaweicloud sdk

        :param incident_id: 事件单ID
        :type incident_id: str
        :param body: Body of the HandleIncidentRequest
        :type body: :class:`huaweicloudsdkcoc.v1.ExecuteActionParamsV2`
        """
        
        

        self._incident_id = None
        self._body = None
        self.discriminator = None

        self.incident_id = incident_id
        if body is not None:
            self.body = body

    @property
    def incident_id(self):
        r"""Gets the incident_id of this HandleIncidentRequest.

        事件单ID

        :return: The incident_id of this HandleIncidentRequest.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        r"""Sets the incident_id of this HandleIncidentRequest.

        事件单ID

        :param incident_id: The incident_id of this HandleIncidentRequest.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def body(self):
        r"""Gets the body of this HandleIncidentRequest.

        :return: The body of this HandleIncidentRequest.
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecuteActionParamsV2`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this HandleIncidentRequest.

        :param body: The body of this HandleIncidentRequest.
        :type body: :class:`huaweicloudsdkcoc.v1.ExecuteActionParamsV2`
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
        if not isinstance(other, HandleIncidentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
