# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_type': 'str',
        'value': 'str',
        'description': 'str'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'value': 'value',
        'description': 'description'
    }

    def __init__(self, cloud_type=None, value=None, description=None):
        r"""RegionInfo

        The model defined in huaweicloud sdk

        :param cloud_type: 云服务名称
        :type cloud_type: str
        :param value: region名称
        :type value: str
        :param description: region的描述信息
        :type description: str
        """
        
        

        self._cloud_type = None
        self._value = None
        self._description = None
        self.discriminator = None

        if cloud_type is not None:
            self.cloud_type = cloud_type
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description

    @property
    def cloud_type(self):
        r"""Gets the cloud_type of this RegionInfo.

        云服务名称

        :return: The cloud_type of this RegionInfo.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        r"""Sets the cloud_type of this RegionInfo.

        云服务名称

        :param cloud_type: The cloud_type of this RegionInfo.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def value(self):
        r"""Gets the value of this RegionInfo.

        region名称

        :return: The value of this RegionInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RegionInfo.

        region名称

        :param value: The value of this RegionInfo.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        r"""Gets the description of this RegionInfo.

        region的描述信息

        :return: The description of this RegionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RegionInfo.

        region的描述信息

        :param description: The description of this RegionInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RegionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
