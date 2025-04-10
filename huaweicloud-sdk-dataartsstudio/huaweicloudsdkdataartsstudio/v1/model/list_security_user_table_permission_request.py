# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityUserTablePermissionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'body': 'SecurityListUserTableList'
    }

    attribute_map = {
        'instance': 'instance',
        'body': 'body'
    }

    def __init__(self, instance=None, body=None):
        r"""ListSecurityUserTablePermissionRequest

        The model defined in huaweicloud sdk

        :param instance: dataarts实例id
        :type instance: str
        :param body: Body of the ListSecurityUserTablePermissionRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableList`
        """
        
        

        self._instance = None
        self._body = None
        self.discriminator = None

        if instance is not None:
            self.instance = instance
        if body is not None:
            self.body = body

    @property
    def instance(self):
        r"""Gets the instance of this ListSecurityUserTablePermissionRequest.

        dataarts实例id

        :return: The instance of this ListSecurityUserTablePermissionRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this ListSecurityUserTablePermissionRequest.

        dataarts实例id

        :param instance: The instance of this ListSecurityUserTablePermissionRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def body(self):
        r"""Gets the body of this ListSecurityUserTablePermissionRequest.

        :return: The body of this ListSecurityUserTablePermissionRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableList`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListSecurityUserTablePermissionRequest.

        :param body: The body of this ListSecurityUserTablePermissionRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableList`
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
        if not isinstance(other, ListSecurityUserTablePermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
