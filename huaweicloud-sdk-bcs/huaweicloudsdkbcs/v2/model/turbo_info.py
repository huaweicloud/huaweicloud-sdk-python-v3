# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TurboInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_type': 'str',
        'type': 'str',
        'available_zone': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'share_type': 'share_type',
        'type': 'type',
        'available_zone': 'available_zone',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, share_type=None, type=None, available_zone=None, resource_spec_code=None):
        """TurboInfo

        The model defined in huaweicloud sdk

        :param share_type: 共享方式，固定值为“STANDARD”
        :type share_type: str
        :param type: 类型，固定值为“efs-ha”
        :type type: str
        :param available_zone: 可用区，可填空字符串(\&quot;\&quot;)。
        :type available_zone: str
        :param resource_spec_code: 规格，固定值为“sfs.turbo.standard”
        :type resource_spec_code: str
        """
        
        

        self._share_type = None
        self._type = None
        self._available_zone = None
        self._resource_spec_code = None
        self.discriminator = None

        self.share_type = share_type
        self.type = type
        self.available_zone = available_zone
        self.resource_spec_code = resource_spec_code

    @property
    def share_type(self):
        """Gets the share_type of this TurboInfo.

        共享方式，固定值为“STANDARD”

        :return: The share_type of this TurboInfo.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this TurboInfo.

        共享方式，固定值为“STANDARD”

        :param share_type: The share_type of this TurboInfo.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def type(self):
        """Gets the type of this TurboInfo.

        类型，固定值为“efs-ha”

        :return: The type of this TurboInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TurboInfo.

        类型，固定值为“efs-ha”

        :param type: The type of this TurboInfo.
        :type type: str
        """
        self._type = type

    @property
    def available_zone(self):
        """Gets the available_zone of this TurboInfo.

        可用区，可填空字符串(\"\")。

        :return: The available_zone of this TurboInfo.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this TurboInfo.

        可用区，可填空字符串(\"\")。

        :param available_zone: The available_zone of this TurboInfo.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this TurboInfo.

        规格，固定值为“sfs.turbo.standard”

        :return: The resource_spec_code of this TurboInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this TurboInfo.

        规格，固定值为“sfs.turbo.standard”

        :param resource_spec_code: The resource_spec_code of this TurboInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, TurboInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
