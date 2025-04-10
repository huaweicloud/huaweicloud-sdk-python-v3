# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BucketDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'region': 'str',
        'type': 'BucketType'
    }

    attribute_map = {
        'name': 'name',
        'region': 'region',
        'type': 'type'
    }

    def __init__(self, name=None, region=None, type=None):
        r"""BucketDto

        The model defined in huaweicloud sdk

        :param name: 桶名称
        :type name: str
        :param region: 区域
        :type region: str
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.BucketType`
        """
        
        

        self._name = None
        self._region = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type

    @property
    def name(self):
        r"""Gets the name of this BucketDto.

        桶名称

        :return: The name of this BucketDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BucketDto.

        桶名称

        :param name: The name of this BucketDto.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this BucketDto.

        区域

        :return: The region of this BucketDto.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this BucketDto.

        区域

        :param region: The region of this BucketDto.
        :type region: str
        """
        self._region = region

    @property
    def type(self):
        r"""Gets the type of this BucketDto.

        :return: The type of this BucketDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BucketType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BucketDto.

        :param type: The type of this BucketDto.
        :type type: :class:`huaweicloudsdkeihealth.v1.BucketType`
        """
        self._type = type

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
        if not isinstance(other, BucketDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
