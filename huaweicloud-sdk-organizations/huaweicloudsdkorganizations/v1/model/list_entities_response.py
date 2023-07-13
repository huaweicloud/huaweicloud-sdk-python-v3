# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEntitiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entities': 'list[EntityDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'entities': 'entities',
        'page_info': 'page_info'
    }

    def __init__(self, entities=None, page_info=None):
        """ListEntitiesResponse

        The model defined in huaweicloud sdk

        :param entities: 组织中的根、组织单元和帐号的列表。
        :type entities: list[:class:`huaweicloudsdkorganizations.v1.EntityDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListEntitiesResponse, self).__init__()

        self._entities = None
        self._page_info = None
        self.discriminator = None

        if entities is not None:
            self.entities = entities
        if page_info is not None:
            self.page_info = page_info

    @property
    def entities(self):
        """Gets the entities of this ListEntitiesResponse.

        组织中的根、组织单元和帐号的列表。

        :return: The entities of this ListEntitiesResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.EntityDto`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ListEntitiesResponse.

        组织中的根、组织单元和帐号的列表。

        :param entities: The entities of this ListEntitiesResponse.
        :type entities: list[:class:`huaweicloudsdkorganizations.v1.EntityDto`]
        """
        self._entities = entities

    @property
    def page_info(self):
        """Gets the page_info of this ListEntitiesResponse.

        :return: The page_info of this ListEntitiesResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListEntitiesResponse.

        :param page_info: The page_info of this ListEntitiesResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListEntitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
