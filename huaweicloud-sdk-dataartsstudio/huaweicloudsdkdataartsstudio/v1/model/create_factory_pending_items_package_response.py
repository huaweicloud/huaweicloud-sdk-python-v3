# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFactoryPendingItemsPackageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_name': 'str',
        'release_package_id': 'str'
    }

    attribute_map = {
        'package_name': 'package_name',
        'release_package_id': 'release_package_id'
    }

    def __init__(self, package_name=None, release_package_id=None):
        r"""CreateFactoryPendingItemsPackageResponse

        The model defined in huaweicloud sdk

        :param package_name: 发布包名称
        :type package_name: str
        :param release_package_id: 发布包ID
        :type release_package_id: str
        """
        
        super(CreateFactoryPendingItemsPackageResponse, self).__init__()

        self._package_name = None
        self._release_package_id = None
        self.discriminator = None

        if package_name is not None:
            self.package_name = package_name
        if release_package_id is not None:
            self.release_package_id = release_package_id

    @property
    def package_name(self):
        r"""Gets the package_name of this CreateFactoryPendingItemsPackageResponse.

        发布包名称

        :return: The package_name of this CreateFactoryPendingItemsPackageResponse.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this CreateFactoryPendingItemsPackageResponse.

        发布包名称

        :param package_name: The package_name of this CreateFactoryPendingItemsPackageResponse.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def release_package_id(self):
        r"""Gets the release_package_id of this CreateFactoryPendingItemsPackageResponse.

        发布包ID

        :return: The release_package_id of this CreateFactoryPendingItemsPackageResponse.
        :rtype: str
        """
        return self._release_package_id

    @release_package_id.setter
    def release_package_id(self, release_package_id):
        r"""Sets the release_package_id of this CreateFactoryPendingItemsPackageResponse.

        发布包ID

        :param release_package_id: The release_package_id of this CreateFactoryPendingItemsPackageResponse.
        :type release_package_id: str
        """
        self._release_package_id = release_package_id

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
        if not isinstance(other, CreateFactoryPendingItemsPackageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
