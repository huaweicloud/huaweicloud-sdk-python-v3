# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBucketRegionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'support': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'support': 'support'
    }

    def __init__(self, id=None, name=None, support=None):
        """ShowBucketRegionResponse

        The model defined in huaweicloud sdk

        :param id: region ID
        :type id: str
        :param name: region 名称
        :type name: str
        :param support: 此region是否支持迁移
        :type support: bool
        """
        
        super(ShowBucketRegionResponse, self).__init__()

        self._id = None
        self._name = None
        self._support = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if support is not None:
            self.support = support

    @property
    def id(self):
        """Gets the id of this ShowBucketRegionResponse.

        region ID

        :return: The id of this ShowBucketRegionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowBucketRegionResponse.

        region ID

        :param id: The id of this ShowBucketRegionResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowBucketRegionResponse.

        region 名称

        :return: The name of this ShowBucketRegionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowBucketRegionResponse.

        region 名称

        :param name: The name of this ShowBucketRegionResponse.
        :type name: str
        """
        self._name = name

    @property
    def support(self):
        """Gets the support of this ShowBucketRegionResponse.

        此region是否支持迁移

        :return: The support of this ShowBucketRegionResponse.
        :rtype: bool
        """
        return self._support

    @support.setter
    def support(self, support):
        """Sets the support of this ShowBucketRegionResponse.

        此region是否支持迁移

        :param support: The support of this ShowBucketRegionResponse.
        :type support: bool
        """
        self._support = support

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
        if not isinstance(other, ShowBucketRegionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
