# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePackageNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_id': 'str',
        'body': 'UpdatePackageNameRequestBody'
    }

    attribute_map = {
        'package_id': 'package_id',
        'body': 'body'
    }

    def __init__(self, package_id=None, body=None):
        r"""UpdatePackageNameRequest

        The model defined in huaweicloud sdk

        :param package_id: 实例id
        :type package_id: str
        :param body: Body of the UpdatePackageNameRequest
        :type body: :class:`huaweicloudsdkaad.v1.UpdatePackageNameRequestBody`
        """
        
        

        self._package_id = None
        self._body = None
        self.discriminator = None

        self.package_id = package_id
        if body is not None:
            self.body = body

    @property
    def package_id(self):
        r"""Gets the package_id of this UpdatePackageNameRequest.

        实例id

        :return: The package_id of this UpdatePackageNameRequest.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this UpdatePackageNameRequest.

        实例id

        :param package_id: The package_id of this UpdatePackageNameRequest.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePackageNameRequest.

        :return: The body of this UpdatePackageNameRequest.
        :rtype: :class:`huaweicloudsdkaad.v1.UpdatePackageNameRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePackageNameRequest.

        :param body: The body of this UpdatePackageNameRequest.
        :type body: :class:`huaweicloudsdkaad.v1.UpdatePackageNameRequestBody`
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
        if not isinstance(other, UpdatePackageNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
