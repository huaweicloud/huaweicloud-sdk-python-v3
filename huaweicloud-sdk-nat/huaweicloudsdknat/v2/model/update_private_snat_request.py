# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrivateSnatRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snat_rule_id': 'str',
        'body': 'UpdatePrivateSnatOptionBody'
    }

    attribute_map = {
        'snat_rule_id': 'snat_rule_id',
        'body': 'body'
    }

    def __init__(self, snat_rule_id=None, body=None):
        """UpdatePrivateSnatRequest

        The model defined in huaweicloud sdk

        :param snat_rule_id: SNAT规则的ID。
        :type snat_rule_id: str
        :param body: Body of the UpdatePrivateSnatRequest
        :type body: :class:`huaweicloudsdknat.v2.UpdatePrivateSnatOptionBody`
        """
        
        

        self._snat_rule_id = None
        self._body = None
        self.discriminator = None

        self.snat_rule_id = snat_rule_id
        if body is not None:
            self.body = body

    @property
    def snat_rule_id(self):
        """Gets the snat_rule_id of this UpdatePrivateSnatRequest.

        SNAT规则的ID。

        :return: The snat_rule_id of this UpdatePrivateSnatRequest.
        :rtype: str
        """
        return self._snat_rule_id

    @snat_rule_id.setter
    def snat_rule_id(self, snat_rule_id):
        """Sets the snat_rule_id of this UpdatePrivateSnatRequest.

        SNAT规则的ID。

        :param snat_rule_id: The snat_rule_id of this UpdatePrivateSnatRequest.
        :type snat_rule_id: str
        """
        self._snat_rule_id = snat_rule_id

    @property
    def body(self):
        """Gets the body of this UpdatePrivateSnatRequest.

        :return: The body of this UpdatePrivateSnatRequest.
        :rtype: :class:`huaweicloudsdknat.v2.UpdatePrivateSnatOptionBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePrivateSnatRequest.

        :param body: The body of this UpdatePrivateSnatRequest.
        :type body: :class:`huaweicloudsdknat.v2.UpdatePrivateSnatOptionBody`
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
        if not isinstance(other, UpdatePrivateSnatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other