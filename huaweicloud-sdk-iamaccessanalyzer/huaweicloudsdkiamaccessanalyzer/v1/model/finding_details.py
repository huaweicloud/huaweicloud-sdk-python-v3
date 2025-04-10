# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FindingDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_access_details': 'ExternalAccessDetails',
        'unused_iam_user_access_key_details': 'UnusedIamUserAccessKeyDetails',
        'unused_iam_user_password_details': 'UnusedIamUserPasswordDetails',
        'unused_permission_details': 'UnusedPermissionDetails'
    }

    attribute_map = {
        'external_access_details': 'external_access_details',
        'unused_iam_user_access_key_details': 'unused_iam_user_access_key_details',
        'unused_iam_user_password_details': 'unused_iam_user_password_details',
        'unused_permission_details': 'unused_permission_details'
    }

    def __init__(self, external_access_details=None, unused_iam_user_access_key_details=None, unused_iam_user_password_details=None, unused_permission_details=None):
        r"""FindingDetails

        The model defined in huaweicloud sdk

        :param external_access_details: 
        :type external_access_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.ExternalAccessDetails`
        :param unused_iam_user_access_key_details: 
        :type unused_iam_user_access_key_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserAccessKeyDetails`
        :param unused_iam_user_password_details: 
        :type unused_iam_user_password_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserPasswordDetails`
        :param unused_permission_details: 
        :type unused_permission_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedPermissionDetails`
        """
        
        

        self._external_access_details = None
        self._unused_iam_user_access_key_details = None
        self._unused_iam_user_password_details = None
        self._unused_permission_details = None
        self.discriminator = None

        if external_access_details is not None:
            self.external_access_details = external_access_details
        if unused_iam_user_access_key_details is not None:
            self.unused_iam_user_access_key_details = unused_iam_user_access_key_details
        if unused_iam_user_password_details is not None:
            self.unused_iam_user_password_details = unused_iam_user_password_details
        if unused_permission_details is not None:
            self.unused_permission_details = unused_permission_details

    @property
    def external_access_details(self):
        r"""Gets the external_access_details of this FindingDetails.

        :return: The external_access_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ExternalAccessDetails`
        """
        return self._external_access_details

    @external_access_details.setter
    def external_access_details(self, external_access_details):
        r"""Sets the external_access_details of this FindingDetails.

        :param external_access_details: The external_access_details of this FindingDetails.
        :type external_access_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.ExternalAccessDetails`
        """
        self._external_access_details = external_access_details

    @property
    def unused_iam_user_access_key_details(self):
        r"""Gets the unused_iam_user_access_key_details of this FindingDetails.

        :return: The unused_iam_user_access_key_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserAccessKeyDetails`
        """
        return self._unused_iam_user_access_key_details

    @unused_iam_user_access_key_details.setter
    def unused_iam_user_access_key_details(self, unused_iam_user_access_key_details):
        r"""Sets the unused_iam_user_access_key_details of this FindingDetails.

        :param unused_iam_user_access_key_details: The unused_iam_user_access_key_details of this FindingDetails.
        :type unused_iam_user_access_key_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserAccessKeyDetails`
        """
        self._unused_iam_user_access_key_details = unused_iam_user_access_key_details

    @property
    def unused_iam_user_password_details(self):
        r"""Gets the unused_iam_user_password_details of this FindingDetails.

        :return: The unused_iam_user_password_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserPasswordDetails`
        """
        return self._unused_iam_user_password_details

    @unused_iam_user_password_details.setter
    def unused_iam_user_password_details(self, unused_iam_user_password_details):
        r"""Sets the unused_iam_user_password_details of this FindingDetails.

        :param unused_iam_user_password_details: The unused_iam_user_password_details of this FindingDetails.
        :type unused_iam_user_password_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserPasswordDetails`
        """
        self._unused_iam_user_password_details = unused_iam_user_password_details

    @property
    def unused_permission_details(self):
        r"""Gets the unused_permission_details of this FindingDetails.

        :return: The unused_permission_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedPermissionDetails`
        """
        return self._unused_permission_details

    @unused_permission_details.setter
    def unused_permission_details(self, unused_permission_details):
        r"""Sets the unused_permission_details of this FindingDetails.

        :param unused_permission_details: The unused_permission_details of this FindingDetails.
        :type unused_permission_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedPermissionDetails`
        """
        self._unused_permission_details = unused_permission_details

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
        if not isinstance(other, FindingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
