# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclApiBindingCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'acl_id': 'str',
        'publish_ids': 'list[str]'
    }

    attribute_map = {
        'acl_id': 'acl_id',
        'publish_ids': 'publish_ids'
    }

    def __init__(self, acl_id=None, publish_ids=None):
        """AclApiBindingCreate

        The model defined in huaweicloud sdk

        :param acl_id: ACL策略编号
        :type acl_id: str
        :param publish_ids: API发布记录编号
        :type publish_ids: list[str]
        """
        
        

        self._acl_id = None
        self._publish_ids = None
        self.discriminator = None

        if acl_id is not None:
            self.acl_id = acl_id
        if publish_ids is not None:
            self.publish_ids = publish_ids

    @property
    def acl_id(self):
        """Gets the acl_id of this AclApiBindingCreate.

        ACL策略编号

        :return: The acl_id of this AclApiBindingCreate.
        :rtype: str
        """
        return self._acl_id

    @acl_id.setter
    def acl_id(self, acl_id):
        """Sets the acl_id of this AclApiBindingCreate.

        ACL策略编号

        :param acl_id: The acl_id of this AclApiBindingCreate.
        :type acl_id: str
        """
        self._acl_id = acl_id

    @property
    def publish_ids(self):
        """Gets the publish_ids of this AclApiBindingCreate.

        API发布记录编号

        :return: The publish_ids of this AclApiBindingCreate.
        :rtype: list[str]
        """
        return self._publish_ids

    @publish_ids.setter
    def publish_ids(self, publish_ids):
        """Sets the publish_ids of this AclApiBindingCreate.

        API发布记录编号

        :param publish_ids: The publish_ids of this AclApiBindingCreate.
        :type publish_ids: list[str]
        """
        self._publish_ids = publish_ids

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
        if not isinstance(other, AclApiBindingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
