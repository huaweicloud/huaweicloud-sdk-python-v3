# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDependencyVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'depend_id': 'str',
        'marker': 'str',
        'maxitems': 'str'
    }

    attribute_map = {
        'depend_id': 'depend_id',
        'marker': 'marker',
        'maxitems': 'maxitems'
    }

    def __init__(self, depend_id=None, marker=None, maxitems=None):
        """ListDependencyVersionRequest

        The model defined in huaweicloud sdk

        :param depend_id: 依赖包的ID。
        :type depend_id: str
        :param marker: 上一次查询依赖包的最后记录位置，默认为\&quot;0\&quot;。
        :type marker: str
        :param maxitems: 单次查询最大条数
        :type maxitems: str
        """
        
        

        self._depend_id = None
        self._marker = None
        self._maxitems = None
        self.discriminator = None

        self.depend_id = depend_id
        if marker is not None:
            self.marker = marker
        if maxitems is not None:
            self.maxitems = maxitems

    @property
    def depend_id(self):
        """Gets the depend_id of this ListDependencyVersionRequest.

        依赖包的ID。

        :return: The depend_id of this ListDependencyVersionRequest.
        :rtype: str
        """
        return self._depend_id

    @depend_id.setter
    def depend_id(self, depend_id):
        """Sets the depend_id of this ListDependencyVersionRequest.

        依赖包的ID。

        :param depend_id: The depend_id of this ListDependencyVersionRequest.
        :type depend_id: str
        """
        self._depend_id = depend_id

    @property
    def marker(self):
        """Gets the marker of this ListDependencyVersionRequest.

        上一次查询依赖包的最后记录位置，默认为\"0\"。

        :return: The marker of this ListDependencyVersionRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDependencyVersionRequest.

        上一次查询依赖包的最后记录位置，默认为\"0\"。

        :param marker: The marker of this ListDependencyVersionRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def maxitems(self):
        """Gets the maxitems of this ListDependencyVersionRequest.

        单次查询最大条数

        :return: The maxitems of this ListDependencyVersionRequest.
        :rtype: str
        """
        return self._maxitems

    @maxitems.setter
    def maxitems(self, maxitems):
        """Sets the maxitems of this ListDependencyVersionRequest.

        单次查询最大条数

        :param maxitems: The maxitems of this ListDependencyVersionRequest.
        :type maxitems: str
        """
        self._maxitems = maxitems

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
        if not isinstance(other, ListDependencyVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
