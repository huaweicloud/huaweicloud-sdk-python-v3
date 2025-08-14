# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApplicationAssignmentReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'principal_id': 'str',
        'principal_type': 'str'
    }

    attribute_map = {
        'principal_id': 'principal_id',
        'principal_type': 'principal_type'
    }

    def __init__(self, principal_id=None, principal_type=None):
        r"""CreateApplicationAssignmentReqBody

        The model defined in huaweicloud sdk

        :param principal_id: 主体Id
        :type principal_id: str
        :param principal_type: 主体类型
        :type principal_type: str
        """
        
        

        self._principal_id = None
        self._principal_type = None
        self.discriminator = None

        self.principal_id = principal_id
        self.principal_type = principal_type

    @property
    def principal_id(self):
        r"""Gets the principal_id of this CreateApplicationAssignmentReqBody.

        主体Id

        :return: The principal_id of this CreateApplicationAssignmentReqBody.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        r"""Sets the principal_id of this CreateApplicationAssignmentReqBody.

        主体Id

        :param principal_id: The principal_id of this CreateApplicationAssignmentReqBody.
        :type principal_id: str
        """
        self._principal_id = principal_id

    @property
    def principal_type(self):
        r"""Gets the principal_type of this CreateApplicationAssignmentReqBody.

        主体类型

        :return: The principal_type of this CreateApplicationAssignmentReqBody.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        r"""Sets the principal_type of this CreateApplicationAssignmentReqBody.

        主体类型

        :param principal_type: The principal_type of this CreateApplicationAssignmentReqBody.
        :type principal_type: str
        """
        self._principal_type = principal_type

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
        if not isinstance(other, CreateApplicationAssignmentReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
