# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketAclRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "AccessControlPolicy"

    sensitive_list = []

    openapi_types = {
        'owner': 'Owner',
        'access_control_list': 'AccessControlList'
    }

    attribute_map = {
        'owner': 'Owner',
        'access_control_list': 'AccessControlList'
    }

    def __init__(self, owner=None, access_control_list=None):
        r"""SetBucketAclRequestBody

        The model defined in huaweicloud sdk

        :param owner: 
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        :param access_control_list: 
        :type access_control_list: :class:`huaweicloudsdkobs.v1.AccessControlList`
        """
        
        

        self._owner = None
        self._access_control_list = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if access_control_list is not None:
            self.access_control_list = access_control_list

    @property
    def owner(self):
        r"""Gets the owner of this SetBucketAclRequestBody.

        :return: The owner of this SetBucketAclRequestBody.
        :rtype: :class:`huaweicloudsdkobs.v1.Owner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this SetBucketAclRequestBody.

        :param owner: The owner of this SetBucketAclRequestBody.
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        """
        self._owner = owner

    @property
    def access_control_list(self):
        r"""Gets the access_control_list of this SetBucketAclRequestBody.

        :return: The access_control_list of this SetBucketAclRequestBody.
        :rtype: :class:`huaweicloudsdkobs.v1.AccessControlList`
        """
        return self._access_control_list

    @access_control_list.setter
    def access_control_list(self, access_control_list):
        r"""Sets the access_control_list of this SetBucketAclRequestBody.

        :param access_control_list: The access_control_list of this SetBucketAclRequestBody.
        :type access_control_list: :class:`huaweicloudsdkobs.v1.AccessControlList`
        """
        self._access_control_list = access_control_list

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
        if not isinstance(other, SetBucketAclRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
