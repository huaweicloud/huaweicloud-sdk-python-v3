# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubjectLevelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'levels': 'list[CatalogLevelVO]'
    }

    attribute_map = {
        'levels': 'levels'
    }

    def __init__(self, levels=None):
        """ListSubjectLevelsResponse

        The model defined in huaweicloud sdk

        :param levels: 主题层级信息
        :type levels: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogLevelVO`]
        """
        
        super(ListSubjectLevelsResponse, self).__init__()

        self._levels = None
        self.discriminator = None

        if levels is not None:
            self.levels = levels

    @property
    def levels(self):
        """Gets the levels of this ListSubjectLevelsResponse.

        主题层级信息

        :return: The levels of this ListSubjectLevelsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogLevelVO`]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this ListSubjectLevelsResponse.

        主题层级信息

        :param levels: The levels of this ListSubjectLevelsResponse.
        :type levels: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogLevelVO`]
        """
        self._levels = levels

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
        if not isinstance(other, ListSubjectLevelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
