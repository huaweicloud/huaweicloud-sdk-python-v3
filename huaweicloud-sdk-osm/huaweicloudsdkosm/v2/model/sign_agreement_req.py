# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignAgreementReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_id': 'str'
    }

    attribute_map = {
        'relation_id': 'relation_id'
    }

    def __init__(self, relation_id=None):
        """SignAgreementReq

        The model defined in huaweicloud sdk

        :param relation_id: 关联id
        :type relation_id: str
        """
        
        

        self._relation_id = None
        self.discriminator = None

        if relation_id is not None:
            self.relation_id = relation_id

    @property
    def relation_id(self):
        """Gets the relation_id of this SignAgreementReq.

        关联id

        :return: The relation_id of this SignAgreementReq.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        """Sets the relation_id of this SignAgreementReq.

        关联id

        :param relation_id: The relation_id of this SignAgreementReq.
        :type relation_id: str
        """
        self._relation_id = relation_id

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
        if not isinstance(other, SignAgreementReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
