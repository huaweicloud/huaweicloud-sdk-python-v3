# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCocIncidentDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'incident_num': 'str'
    }

    attribute_map = {
        'incident_num': 'incident_num'
    }

    def __init__(self, incident_num=None):
        r"""ShowCocIncidentDetailRequest

        The model defined in huaweicloud sdk

        :param incident_num: 事件单号
        :type incident_num: str
        """
        
        

        self._incident_num = None
        self.discriminator = None

        self.incident_num = incident_num

    @property
    def incident_num(self):
        r"""Gets the incident_num of this ShowCocIncidentDetailRequest.

        事件单号

        :return: The incident_num of this ShowCocIncidentDetailRequest.
        :rtype: str
        """
        return self._incident_num

    @incident_num.setter
    def incident_num(self, incident_num):
        r"""Sets the incident_num of this ShowCocIncidentDetailRequest.

        事件单号

        :param incident_num: The incident_num of this ShowCocIncidentDetailRequest.
        :type incident_num: str
        """
        self._incident_num = incident_num

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
        if not isinstance(other, ShowCocIncidentDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
