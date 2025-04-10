# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountMultiResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor': 'str',
        'view_id': 'str',
        'is_resource': 'bool',
        'region_id': 'str'
    }

    attribute_map = {
        'vendor': 'vendor',
        'view_id': 'view_id',
        'is_resource': 'is_resource',
        'region_id': 'region_id'
    }

    def __init__(self, vendor=None, view_id=None, is_resource=None, region_id=None):
        r"""CountMultiResourcesRequest

        The model defined in huaweicloud sdk

        :param vendor: 厂商来源（默认RMS，可填RMS/ALI/AWS）
        :type vendor: str
        :param view_id: 视图 id，视图模式下必填
        :type view_id: str
        :param is_resource: 是否为资源模块
        :type is_resource: bool
        :param region_id: 区域 id
        :type region_id: str
        """
        
        

        self._vendor = None
        self._view_id = None
        self._is_resource = None
        self._region_id = None
        self.discriminator = None

        self.vendor = vendor
        if view_id is not None:
            self.view_id = view_id
        if is_resource is not None:
            self.is_resource = is_resource
        if region_id is not None:
            self.region_id = region_id

    @property
    def vendor(self):
        r"""Gets the vendor of this CountMultiResourcesRequest.

        厂商来源（默认RMS，可填RMS/ALI/AWS）

        :return: The vendor of this CountMultiResourcesRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this CountMultiResourcesRequest.

        厂商来源（默认RMS，可填RMS/ALI/AWS）

        :param vendor: The vendor of this CountMultiResourcesRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def view_id(self):
        r"""Gets the view_id of this CountMultiResourcesRequest.

        视图 id，视图模式下必填

        :return: The view_id of this CountMultiResourcesRequest.
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        r"""Sets the view_id of this CountMultiResourcesRequest.

        视图 id，视图模式下必填

        :param view_id: The view_id of this CountMultiResourcesRequest.
        :type view_id: str
        """
        self._view_id = view_id

    @property
    def is_resource(self):
        r"""Gets the is_resource of this CountMultiResourcesRequest.

        是否为资源模块

        :return: The is_resource of this CountMultiResourcesRequest.
        :rtype: bool
        """
        return self._is_resource

    @is_resource.setter
    def is_resource(self, is_resource):
        r"""Sets the is_resource of this CountMultiResourcesRequest.

        是否为资源模块

        :param is_resource: The is_resource of this CountMultiResourcesRequest.
        :type is_resource: bool
        """
        self._is_resource = is_resource

    @property
    def region_id(self):
        r"""Gets the region_id of this CountMultiResourcesRequest.

        区域 id

        :return: The region_id of this CountMultiResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CountMultiResourcesRequest.

        区域 id

        :param region_id: The region_id of this CountMultiResourcesRequest.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, CountMultiResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
