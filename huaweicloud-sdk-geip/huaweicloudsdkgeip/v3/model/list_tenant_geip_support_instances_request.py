# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantGeipSupportInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_site': 'str',
        'fields': 'list[str]'
    }

    attribute_map = {
        'access_site': 'access_site',
        'fields': 'fields'
    }

    def __init__(self, access_site=None, fields=None):
        r"""ListTenantGeipSupportInstancesRequest

        The model defined in huaweicloud sdk

        :param access_site: 
        :type access_site: str
        :param fields: 
        :type fields: list[str]
        """
        
        

        self._access_site = None
        self._fields = None
        self.discriminator = None

        self.access_site = access_site
        if fields is not None:
            self.fields = fields

    @property
    def access_site(self):
        r"""Gets the access_site of this ListTenantGeipSupportInstancesRequest.

        :return: The access_site of this ListTenantGeipSupportInstancesRequest.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        r"""Sets the access_site of this ListTenantGeipSupportInstancesRequest.

        :param access_site: The access_site of this ListTenantGeipSupportInstancesRequest.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def fields(self):
        r"""Gets the fields of this ListTenantGeipSupportInstancesRequest.

        :return: The fields of this ListTenantGeipSupportInstancesRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListTenantGeipSupportInstancesRequest.

        :param fields: The fields of this ListTenantGeipSupportInstancesRequest.
        :type fields: list[str]
        """
        self._fields = fields

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
        if not isinstance(other, ListTenantGeipSupportInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
