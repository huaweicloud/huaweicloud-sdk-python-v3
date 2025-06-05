# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEntityDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entities': 'list[Entity]',
        'referred_entities': 'object'
    }

    attribute_map = {
        'entities': 'entities',
        'referred_entities': 'referred_entities'
    }

    def __init__(self, entities=None, referred_entities=None):
        r"""ListEntityDetailsResponse

        The model defined in huaweicloud sdk

        :param entities: 资产信息列表。
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        :param referred_entities: 关联资产信息，结构体Map&lt;String, Entity&gt;。key：资产guid，value：资产信息。
        :type referred_entities: object
        """
        
        super(ListEntityDetailsResponse, self).__init__()

        self._entities = None
        self._referred_entities = None
        self.discriminator = None

        if entities is not None:
            self.entities = entities
        if referred_entities is not None:
            self.referred_entities = referred_entities

    @property
    def entities(self):
        r"""Gets the entities of this ListEntityDetailsResponse.

        资产信息列表。

        :return: The entities of this ListEntityDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ListEntityDetailsResponse.

        资产信息列表。

        :param entities: The entities of this ListEntityDetailsResponse.
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        """
        self._entities = entities

    @property
    def referred_entities(self):
        r"""Gets the referred_entities of this ListEntityDetailsResponse.

        关联资产信息，结构体Map<String, Entity>。key：资产guid，value：资产信息。

        :return: The referred_entities of this ListEntityDetailsResponse.
        :rtype: object
        """
        return self._referred_entities

    @referred_entities.setter
    def referred_entities(self, referred_entities):
        r"""Sets the referred_entities of this ListEntityDetailsResponse.

        关联资产信息，结构体Map<String, Entity>。key：资产guid，value：资产信息。

        :param referred_entities: The referred_entities of this ListEntityDetailsResponse.
        :type referred_entities: object
        """
        self._referred_entities = referred_entities

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
        if not isinstance(other, ListEntityDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
