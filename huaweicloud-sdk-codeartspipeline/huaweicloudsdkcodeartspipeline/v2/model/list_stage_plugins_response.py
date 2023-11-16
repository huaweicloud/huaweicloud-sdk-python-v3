# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStagePluginsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_stage_plugins_item_list': 'list[FullStagePluginsRelationVOFullStagePluginsItemList]'
    }

    attribute_map = {
        'full_stage_plugins_item_list': 'full_stage_plugins_item_list'
    }

    def __init__(self, full_stage_plugins_item_list=None):
        """ListStagePluginsResponse

        The model defined in huaweicloud sdk

        :param full_stage_plugins_item_list: 结果集
        :type full_stage_plugins_item_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOFullStagePluginsItemList`]
        """
        
        super(ListStagePluginsResponse, self).__init__()

        self._full_stage_plugins_item_list = None
        self.discriminator = None

        if full_stage_plugins_item_list is not None:
            self.full_stage_plugins_item_list = full_stage_plugins_item_list

    @property
    def full_stage_plugins_item_list(self):
        """Gets the full_stage_plugins_item_list of this ListStagePluginsResponse.

        结果集

        :return: The full_stage_plugins_item_list of this ListStagePluginsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOFullStagePluginsItemList`]
        """
        return self._full_stage_plugins_item_list

    @full_stage_plugins_item_list.setter
    def full_stage_plugins_item_list(self, full_stage_plugins_item_list):
        """Sets the full_stage_plugins_item_list of this ListStagePluginsResponse.

        结果集

        :param full_stage_plugins_item_list: The full_stage_plugins_item_list of this ListStagePluginsResponse.
        :type full_stage_plugins_item_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOFullStagePluginsItemList`]
        """
        self._full_stage_plugins_item_list = full_stage_plugins_item_list

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
        if not isinstance(other, ListStagePluginsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
