# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelFactoryPackagesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_ids': 'list[str]'
    }

    attribute_map = {
        'package_ids': 'package_ids'
    }

    def __init__(self, package_ids=None):
        r"""CancelFactoryPackagesRequestBody

        The model defined in huaweicloud sdk

        :param package_ids: 发布包id列表信息
        :type package_ids: list[str]
        """
        
        

        self._package_ids = None
        self.discriminator = None

        if package_ids is not None:
            self.package_ids = package_ids

    @property
    def package_ids(self):
        r"""Gets the package_ids of this CancelFactoryPackagesRequestBody.

        发布包id列表信息

        :return: The package_ids of this CancelFactoryPackagesRequestBody.
        :rtype: list[str]
        """
        return self._package_ids

    @package_ids.setter
    def package_ids(self, package_ids):
        r"""Sets the package_ids of this CancelFactoryPackagesRequestBody.

        发布包id列表信息

        :param package_ids: The package_ids of this CancelFactoryPackagesRequestBody.
        :type package_ids: list[str]
        """
        self._package_ids = package_ids

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
        if not isinstance(other, CancelFactoryPackagesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
