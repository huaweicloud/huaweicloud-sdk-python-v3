# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'org_id': 'str',
        'body': 'InstanceParam'
    }

    attribute_map = {
        'org_id': 'org_id',
        'body': 'body'
    }

    def __init__(self, org_id=None, body=None):
        """CreateInstanceRequest

        The model defined in huaweicloud sdk

        :param org_id: 租户id（对应华为云帐号的domainId）
        :type org_id: str
        :param body: Body of the CreateInstanceRequest
        :type body: :class:`huaweicloudsdkcloudide.v2.InstanceParam`
        """
        
        

        self._org_id = None
        self._body = None
        self.discriminator = None

        self.org_id = org_id
        if body is not None:
            self.body = body

    @property
    def org_id(self):
        """Gets the org_id of this CreateInstanceRequest.

        租户id（对应华为云帐号的domainId）

        :return: The org_id of this CreateInstanceRequest.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CreateInstanceRequest.

        租户id（对应华为云帐号的domainId）

        :param org_id: The org_id of this CreateInstanceRequest.
        :type org_id: str
        """
        self._org_id = org_id

    @property
    def body(self):
        """Gets the body of this CreateInstanceRequest.


        :return: The body of this CreateInstanceRequest.
        :rtype: :class:`huaweicloudsdkcloudide.v2.InstanceParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateInstanceRequest.


        :param body: The body of this CreateInstanceRequest.
        :type body: :class:`huaweicloudsdkcloudide.v2.InstanceParam`
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
        if not isinstance(other, CreateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
