# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VodPackageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'packaging_group_id': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'packaging_group_id': 'packaging_group_id',
        'resource_id': 'resource_id'
    }

    def __init__(self, packaging_group_id=None, resource_id=None):
        r"""VodPackageInfo

        The model defined in huaweicloud sdk

        :param packaging_group_id: VOD 打包信息，转封装模板ID，模板ID通过VOD查询
        :type packaging_group_id: str
        :param resource_id: DRM resourceID
        :type resource_id: str
        """
        
        

        self._packaging_group_id = None
        self._resource_id = None
        self.discriminator = None

        if packaging_group_id is not None:
            self.packaging_group_id = packaging_group_id
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def packaging_group_id(self):
        r"""Gets the packaging_group_id of this VodPackageInfo.

        VOD 打包信息，转封装模板ID，模板ID通过VOD查询

        :return: The packaging_group_id of this VodPackageInfo.
        :rtype: str
        """
        return self._packaging_group_id

    @packaging_group_id.setter
    def packaging_group_id(self, packaging_group_id):
        r"""Sets the packaging_group_id of this VodPackageInfo.

        VOD 打包信息，转封装模板ID，模板ID通过VOD查询

        :param packaging_group_id: The packaging_group_id of this VodPackageInfo.
        :type packaging_group_id: str
        """
        self._packaging_group_id = packaging_group_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this VodPackageInfo.

        DRM resourceID

        :return: The resource_id of this VodPackageInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this VodPackageInfo.

        DRM resourceID

        :param resource_id: The resource_id of this VodPackageInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, VodPackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
