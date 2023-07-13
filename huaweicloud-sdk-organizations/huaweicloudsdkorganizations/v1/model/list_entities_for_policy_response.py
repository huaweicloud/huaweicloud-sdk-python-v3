# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEntitiesForPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attached_entities': 'list[EntityDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'attached_entities': 'attached_entities',
        'page_info': 'page_info'
    }

    def __init__(self, attached_entities=None, page_info=None):
        """ListEntitiesForPolicyResponse

        The model defined in huaweicloud sdk

        :param attached_entities: 结构列表，每个结构都包含有关指定策略附加到的实体的详细信息。
        :type attached_entities: list[:class:`huaweicloudsdkorganizations.v1.EntityDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListEntitiesForPolicyResponse, self).__init__()

        self._attached_entities = None
        self._page_info = None
        self.discriminator = None

        if attached_entities is not None:
            self.attached_entities = attached_entities
        if page_info is not None:
            self.page_info = page_info

    @property
    def attached_entities(self):
        """Gets the attached_entities of this ListEntitiesForPolicyResponse.

        结构列表，每个结构都包含有关指定策略附加到的实体的详细信息。

        :return: The attached_entities of this ListEntitiesForPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.EntityDto`]
        """
        return self._attached_entities

    @attached_entities.setter
    def attached_entities(self, attached_entities):
        """Sets the attached_entities of this ListEntitiesForPolicyResponse.

        结构列表，每个结构都包含有关指定策略附加到的实体的详细信息。

        :param attached_entities: The attached_entities of this ListEntitiesForPolicyResponse.
        :type attached_entities: list[:class:`huaweicloudsdkorganizations.v1.EntityDto`]
        """
        self._attached_entities = attached_entities

    @property
    def page_info(self):
        """Gets the page_info of this ListEntitiesForPolicyResponse.

        :return: The page_info of this ListEntitiesForPolicyResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListEntitiesForPolicyResponse.

        :param page_info: The page_info of this ListEntitiesForPolicyResponse.
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
        if not isinstance(other, ListEntitiesForPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
