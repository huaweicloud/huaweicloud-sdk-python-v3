# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImStatusV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'incident_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'incident_id': 'incident_id'
    }

    def __init__(self, status=None, incident_id=None):
        """ImStatusV2

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: int
        :param incident_id: 工单id
        :type incident_id: str
        """
        
        

        self._status = None
        self._incident_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if incident_id is not None:
            self.incident_id = incident_id

    @property
    def status(self):
        """Gets the status of this ImStatusV2.

        状态

        :return: The status of this ImStatusV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImStatusV2.

        状态

        :param status: The status of this ImStatusV2.
        :type status: int
        """
        self._status = status

    @property
    def incident_id(self):
        """Gets the incident_id of this ImStatusV2.

        工单id

        :return: The incident_id of this ImStatusV2.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this ImStatusV2.

        工单id

        :param incident_id: The incident_id of this ImStatusV2.
        :type incident_id: str
        """
        self._incident_id = incident_id

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
        if not isinstance(other, ImStatusV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
