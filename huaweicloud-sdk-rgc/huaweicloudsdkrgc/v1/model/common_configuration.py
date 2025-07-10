# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'home_region': 'str',
        'cloud_trail_type': 'bool',
        'identity_center_status': 'str',
        'organization_structure_type': 'str'
    }

    attribute_map = {
        'home_region': 'home_region',
        'cloud_trail_type': 'cloud_trail_type',
        'identity_center_status': 'identity_center_status',
        'organization_structure_type': 'organization_structure_type'
    }

    def __init__(self, home_region=None, cloud_trail_type=None, identity_center_status=None, organization_structure_type=None):
        r"""CommonConfiguration

        The model defined in huaweicloud sdk

        :param home_region: 主区域名。
        :type home_region: str
        :param cloud_trail_type: CTS配置状态。
        :type cloud_trail_type: bool
        :param identity_center_status: 是否设置Landing Zone的identity center。
        :type identity_center_status: str
        :param organization_structure_type: 设置organization的类型。STANDARD和NON_STANDARD。
        :type organization_structure_type: str
        """
        
        

        self._home_region = None
        self._cloud_trail_type = None
        self._identity_center_status = None
        self._organization_structure_type = None
        self.discriminator = None

        if home_region is not None:
            self.home_region = home_region
        if cloud_trail_type is not None:
            self.cloud_trail_type = cloud_trail_type
        if identity_center_status is not None:
            self.identity_center_status = identity_center_status
        if organization_structure_type is not None:
            self.organization_structure_type = organization_structure_type

    @property
    def home_region(self):
        r"""Gets the home_region of this CommonConfiguration.

        主区域名。

        :return: The home_region of this CommonConfiguration.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        r"""Sets the home_region of this CommonConfiguration.

        主区域名。

        :param home_region: The home_region of this CommonConfiguration.
        :type home_region: str
        """
        self._home_region = home_region

    @property
    def cloud_trail_type(self):
        r"""Gets the cloud_trail_type of this CommonConfiguration.

        CTS配置状态。

        :return: The cloud_trail_type of this CommonConfiguration.
        :rtype: bool
        """
        return self._cloud_trail_type

    @cloud_trail_type.setter
    def cloud_trail_type(self, cloud_trail_type):
        r"""Sets the cloud_trail_type of this CommonConfiguration.

        CTS配置状态。

        :param cloud_trail_type: The cloud_trail_type of this CommonConfiguration.
        :type cloud_trail_type: bool
        """
        self._cloud_trail_type = cloud_trail_type

    @property
    def identity_center_status(self):
        r"""Gets the identity_center_status of this CommonConfiguration.

        是否设置Landing Zone的identity center。

        :return: The identity_center_status of this CommonConfiguration.
        :rtype: str
        """
        return self._identity_center_status

    @identity_center_status.setter
    def identity_center_status(self, identity_center_status):
        r"""Sets the identity_center_status of this CommonConfiguration.

        是否设置Landing Zone的identity center。

        :param identity_center_status: The identity_center_status of this CommonConfiguration.
        :type identity_center_status: str
        """
        self._identity_center_status = identity_center_status

    @property
    def organization_structure_type(self):
        r"""Gets the organization_structure_type of this CommonConfiguration.

        设置organization的类型。STANDARD和NON_STANDARD。

        :return: The organization_structure_type of this CommonConfiguration.
        :rtype: str
        """
        return self._organization_structure_type

    @organization_structure_type.setter
    def organization_structure_type(self, organization_structure_type):
        r"""Sets the organization_structure_type of this CommonConfiguration.

        设置organization的类型。STANDARD和NON_STANDARD。

        :param organization_structure_type: The organization_structure_type of this CommonConfiguration.
        :type organization_structure_type: str
        """
        self._organization_structure_type = organization_structure_type

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
        if not isinstance(other, CommonConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
