# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetArchiveConfigRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'current_region': 'bool'
    }

    attribute_map = {
        'region_id': 'region_id',
        'current_region': 'current_region'
    }

    def __init__(self, region_id=None, current_region=None):
        """GetArchiveConfigRsp

        The model defined in huaweicloud sdk

        :param region_id: 华为云项目
        :type region_id: str
        :param current_region: 该区域是否是当前设置的归档区域
        :type current_region: bool
        """
        
        

        self._region_id = None
        self._current_region = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if current_region is not None:
            self.current_region = current_region

    @property
    def region_id(self):
        """Gets the region_id of this GetArchiveConfigRsp.

        华为云项目

        :return: The region_id of this GetArchiveConfigRsp.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this GetArchiveConfigRsp.

        华为云项目

        :param region_id: The region_id of this GetArchiveConfigRsp.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def current_region(self):
        """Gets the current_region of this GetArchiveConfigRsp.

        该区域是否是当前设置的归档区域

        :return: The current_region of this GetArchiveConfigRsp.
        :rtype: bool
        """
        return self._current_region

    @current_region.setter
    def current_region(self, current_region):
        """Sets the current_region of this GetArchiveConfigRsp.

        该区域是否是当前设置的归档区域

        :param current_region: The current_region of this GetArchiveConfigRsp.
        :type current_region: bool
        """
        self._current_region = current_region

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
        if not isinstance(other, GetArchiveConfigRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
